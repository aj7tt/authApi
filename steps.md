
# virtual environment
pip install virtualenv
virtualenv --version
python -m venv env  
env\Scripts\activate 

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\env\Scripts\Activate



# pip install lib 
pip install fastapi[all]

pip install fastapi pydantic python-jose uvicorn pydantic sqlalchemy alembic python-multipart fastapi-users databases httpx fastapi-jwt-auth fastapi-cors tortoise-orm aioredis pyjwt email-validator fastapi-websocket fastapi-validation decouple fastapi-session gunicorn python-decouple


# To retrieve a list of installed Python packages along with their versions and save them into a requirements.txt file
pip freeze > requirements.txt



# database Migration 

alembic init alembic
change file sqlalchemy.url =""
alembic revision --autogenerate -m "Add_new_column"
alembic upgrade head





pip list

# learning point 

# alembic==1.12.0
#Description: Database migration tool for SQLAlchemy. It helps manage database schema changes.

# annotated-types==0.5.0
#Description: A library for handling annotated types.

# anyio==3.7.1
#Description: A library for asynchronous I/O, which can be useful for handling asynchronous tasks in FastAPI applications.

# bcrypt==4.0.1
#Description: A library for password hashing. You can use it for securely storing and verifying passwords.

# certifi==2023.7.22
#Description: A library containing trusted CA certificates, which can be used for secure communication.

# cffi==1.15.1
#Description: A library for calling C functions from Python, often used in conjunction with other libraries for low-level operations.

# click==8.1.7
#Description: A command-line interface creation kit.

# colorama==0.4.6
#Description: A library for adding color to console text.

# cryptography==41.0.4
#Description: A library for secure communication.

# databases==0.8.0
#Description: An asynchronous database library.

# dnspython==2.4.2
#Description: DNS toolkit for Python.

# email-validator==2.0.0.post2
#Description: Library for email validation.

# environs==9.5.0
#Description: Library for parsing environment variables.

# fastapi==0.103.1
#Description: A modern web framework for building APIs.

# fastapi-jwt-auth==0.2.0
#Description: JSON Web Token (JWT) authentication for FastAPI.

# fastapi-users==12.1.2
#Description: User authentication and management for FastAPI.

# fastapi_cors==0.0.6
#Description: CORS (Cross-Origin Resource Sharing) middleware for FastAPI.

# greenlet==2.0.2
#Description: Lightweight concurrent programming.

# h11==0.14.0
#Description: HTTP/1.1 client/server library.

# httpcore==0.18.0
#Description: Low-level, dependency-free HTTP client and server library.

# httpx==0.25.0
#Description: A fully-featured HTTP client for Python 3, which can be useful for making HTTP requests from your FastAPI application.

# idna==3.4
#Description: A library for handling Internationalized Domain Names (IDNA).

# makefun==1.15.1
#Description: A library for creating dynamic functions.

# Mako==1.2.4
#Description: A template library.

# MarkupSafe==2.1.3
#Description: A library for XML/HTML escaping.

# marshmallow==3.20.1
#Description: A library for object serialization/deserialization.

# packaging==23.1
#Description: A library for package and distribution management.

# passlib==1.7.4
#Description: A library for password hashing and authentication.

# pycparser==2.21
#Description: A library for parsing C code.

# pydantic==2.3.0
#Description: Data validation and parsing library, often used for request and response validation in FastAPI applications.

# pydantic_core==2.6.3
#Description: Core components of the Pydantic library.

# PyJWT==2.8.0
#Description: A library for encoding and decoding JSON Web Tokens (JWT).

# python-dotenv==1.0.0
#Description: A library for loading environment variables from a .env file.

# python-multipart==0.0.6
#Description: A library for handling multipart/form-data requests, often used for file uploads in FastAPI applications.

# sniffio==1.3.0
#Description: A library for working with asynchronous event loops.

# SQLAlchemy==1.4.49
#Description: A popular SQL toolkit and Object-Relational Mapping (ORM) library. You can use it to interact with databases in FastAPI applications.

# starlette==0.27.0
#Description: The ASGI framework that underlies FastAPI.

# typing_extensions==4.8.0
#Description: Extensions to the Python typing module.

# uvicorn==0.23.2
#Description: ASGI server for running FastAPI applications.
