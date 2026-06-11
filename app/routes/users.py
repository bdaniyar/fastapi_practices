from fastapi import APIRouter
from app.schemas import CreateUser

router = APIRouter(prefix="/users", tags=["users"])


@router.post("")
def create_user(user: CreateUser):
    """Create a new user."""
    return {
        "Success": "User created successfully",
        "email": user.email,
        "name": user.name
    }
