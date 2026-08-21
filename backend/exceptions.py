from logger import logger
from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from sqlalchemy.exc import IntegrityError

async def http_exception_handler(
    request: Request,
    exc: HTTPException
):
    logger.warning(
    f"{exc.status_code} - {exc.detail} | {request.method} {request.url.path}"
)
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail
        }
    )

async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    logger.warning(
    f"Validation failed | {request.method} {request.url.path} | Errors: {exc.errors()}"
)

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "message": "Validation failed",
            "errors": exc.errors()
        }
    )

async def integrity_error_handler(
    request: Request,
    exc: IntegrityError
):
    logger.error(
    f"Database Integrity Error | {request.method} {request.url.path} | {str(exc.orig)}"
)
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "success": False,
            "message": "Database integrity error."
        }
    )

async def general_exception_handler(
    request: Request,
    exc: Exception
):
    logger.exception(
    f"Unexpected exception at {request.method} {request.url.path}"
)

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "success": False,
            "message": "An unexpected server error occurred."
        }
    )