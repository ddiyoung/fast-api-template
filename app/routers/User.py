from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from app.schemas.pydantic.User import UserSchema
from app.services.UserService import UserService
from app.utils.error.error_response import ErrorResponseModel, ErrorResponseExample

UserRouter = APIRouter(
    prefix="/user", tags=['user']
)


@UserRouter.get("/{id}", response_model=UserSchema, responses={
    status.HTTP_500_INTERNAL_SERVER_ERROR: {
        "model": ErrorResponseModel,
        #"content": ErrorResponseExample.get_error_response(),
    },
})
def get(id: int, userService: UserService = Depends()):
    try:
        return userService.get(id).normalize()
    except:
        return JSONResponse(status_code=500, content={
            'error_code': 500,
            'error_message': "Internal Server Error"
        })

            #HTTPException(status_code=500, detail="Internal Server Error")
