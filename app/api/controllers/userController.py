

from app.models.userModel import User, UserRole
from app.schemas.schemas import UserCreate, UserLogin 
from app.services.userCrud import authenticate_user,  create_user, get_current_user
from fastapi import Header, Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session  
from jose import jwt
from app.config.database import get_db
from datetime import datetime, timedelta 

SECRET_KEY = "Aa1$2Bb3*Cc4Dd5Ee6Ff7Gg8Hh9Ii0JjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
 
#to register as admin
ADMIN_SECRET_KEY = "adminsecretkey"

ALGORITHM = "HS256"


userRouter = APIRouter()

@userRouter.get("/")
def healthCheck():
    return {"status : ok 200" }

# Register a new user
# User registration endpoint 
@userRouter.post("/register/")
def register(request: UserCreate, db: Session = Depends(get_db), admin_secret_key: str = Header(None)):
    
    # Check if user role is "admin" and requires permission
    if request.role == UserRole.admin:
        # Check for admin_secret_key
        if admin_secret_key != ADMIN_SECRET_KEY:
            raise HTTPException(status_code=401, detail="Admin registration requires a valid secret key")

    
    if request.role == UserRole.superuser:
        # db_user = check_superuser(db)
        # if db_user is None:
        #     raise HTTPException(status_code=401, detail="Invalid ")
        db_user = "superuser already registered"
        return db_user
    
    # Create the user record
    db_user = create_user(db, request)
    return db_user


# Authenticate and log in a user
@userRouter.post("/login/")
def login(request: UserLogin, db: Session = Depends(get_db)):
    
    db_user = authenticate_user(db, request)
    
    if db_user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    expiration_time = datetime.utcnow() + timedelta(hours=1)

    # Define the token data
    token_data = {
        "userId": db_user.id,
        "userName": db_user.username,
        "role": db_user.role,
        "exp": expiration_time  # Set the token expiration time
    }

    # Generate the JWT token with the expiration time
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": token, "token_type": "bearer"}


# Update user information (PUT)
@userRouter.put("/update/")
def update_user(updated_user: UserCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Update the user's information
    current_user.username = updated_user.username 
    db.commit()

    return current_user

# Partially update user information (PATCH)
@userRouter.patch("/update/")
def partial_update_user(updated_user: UserCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Update the user's information (only fields provided in the request)
    if updated_user.username:
        current_user.username = updated_user.username
    db.commit()

    return current_user


# Delete the authenticated user (DELETE)
@userRouter.delete("/delete/")
def delete_current_user(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Delete the authenticated user
    db.delete(current_user)
    db.commit()

    return {"message": "User deleted successfully"}
