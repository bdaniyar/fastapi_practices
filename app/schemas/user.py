from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    """Schema for creating a new user."""
    email: EmailStr
    name: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "name": "John Doe"
            }
        }
