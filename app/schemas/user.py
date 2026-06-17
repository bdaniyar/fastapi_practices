from pydantic import BaseModel, EmailStr
from typing import Annotated
from annotated_types import MaxLen, MinLen

class CreateUser(BaseModel):
    email: EmailStr
    name: Annotated[str, MinLen(1), MaxLen(20)]
