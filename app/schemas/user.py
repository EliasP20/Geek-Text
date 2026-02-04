from pydantic import BaseModel
from typing import Optional

class UserResponse(BaseModel):
    id: int
    username: str
    name: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None

    class Config:
        from_attributes = True
