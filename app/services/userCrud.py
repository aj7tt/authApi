from app.models.userModel import User, UserRole
from app.schemas.schemas import UserCreate, UserLogin
from app.services.authCrud import hash_password, verify_password
from sqlalchemy.orm import Session
from passlib.context import CryptContext  # For password hashing
from fastapi import Depends, Header, HTTPException
from jose import jwt, JWTError
from app.config.database import get_db

# Create a CryptContext instance for password hashing 
SECRET_KEY = "Aa1$2Bb3*Cc4Dd5Ee6Ff7Gg8Hh9Ii0JjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
 

ALGORITHM = "HS256"


# Define a function to extract and verify the JWT token
async def get_current_user(token: str = Header(None), db: Session = Depends(get_db)):
    if token is None:
        raise HTTPException(status_code=401, detail="Authorization token not provided")

    try:
        # Replace 'your-secret-key' with your actual JWT secret key
        payload = jwt.decode(token, SECRET_KEY, algorithms= ALGORITHM)
        user_id = payload.get("sub")

        # Check if the user exists in the database
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


# create a new instance of the User : superUser
def check_superuser(db: Session):
    # Check if a superuser already exists in the database
    existing_superuser = db.query(User).filter(User.role == "superuser").first()

    if existing_superuser:
        print("Superuser already exists.")
        return True
    return False
    # # Create a superuser account
    # superuser_data = UserCreate(
    #     username="superuser",
    #     password="superuser_password",  # Replace with an actual secure password
    #     role="superuser"
    # )
    # superuser_data.password = hash_password(superuser_data.password)

    # superuser = User(**superuser_data.dict())
    # db.add(superuser)
    # db.commit()
    # print("Superuser created successfully.")
    

def check_superuser_permission(db: Session, username: str) -> bool:
    # Query the database to fetch the user by username
    user = db.query(User).filter(User.username == username).first()

    # Check if the user exists and if their role is "superuser"
    if user and user.role == UserRole.superuser:
        return True

    return False


# Registration :: create a new user
def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(username=user.username, password=hashed_password, email = user.email, mobile = user.mobile, role=user.role.value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Login :: authicate the user with the given password
def authenticate_user(db: Session, request: UserLogin):    
    login_method = request.login_method
    credential = request.credential
    password = request.password
    
    # Create a mapping of login methods to database fields
    login_method_to_db_field = {
        "email": User.email,
        "mobile": User.mobile,
        "username": User.username,
    } 
    
    # Check if the login method is valid
    if login_method not in login_method_to_db_field:
        return None   
    
    # Define the database field to query based on the login method
    db_field = login_method_to_db_field[login_method]
    

    # Query the database for the user
    db_user = db.query(User).filter(db_field == credential).first()
 
    if db_user and verify_password(password, db_user.password):
        return db_user  
    
    return None  


# check if user already exist 
def does_user_exist(db: Session, request):
    # Define the database fields to query for each login method
    db_fields = [User.email, User.mobile, User.username]

    # Iterate through the database fields and query the database for each
    for db_field in db_fields:
        # Check if the attribute exists in the request
        if hasattr(request, db_field.name):
            credential = getattr(request, db_field.name)
            user = db.query(User).filter(db_field == credential).first()
            if user:
                return user  # Return the user object if a match is found

    return None
