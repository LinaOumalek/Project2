from pydantic import BaseModel

class UserModel(BaseModel):
    full_name: str
    email: str
    phone: str | None = None