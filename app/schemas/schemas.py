
from pydantic import BaseModel, EmailStr, validator
from app.models.userModel import UserRole

class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr 
    mobile: str
    role: UserRole = UserRole.customer
    
    @validator("email", "mobile", pre=True, always=True)
    def at_least_one_contact(cls, v, values):
        if not v and not values.get("mobile"):
            raise ValueError("At least one of 'email' or 'mobile' must be provided")
        return v

# Define a Pydantic model for the login request
class UserLogin(BaseModel):
    login_method: str
    credential: str
    password: str