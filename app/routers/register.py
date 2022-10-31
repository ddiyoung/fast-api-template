from fastapi import APIRouter

router = APIRouter(
    prefix = "/register",
    tags = ["items"],
    responses={404: {"description": "Not Found"}},
)

@router.get("/")
async def hello_admin():
    return {"message": "Hellow admin"}

@router.post("/")
async def register():


