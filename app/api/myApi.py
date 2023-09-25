
from fastapi import APIRouter


router = APIRouter()

# route for Items api service
from .controllers.userController import userRouter as userApiRouter
router.include_router(userApiRouter)