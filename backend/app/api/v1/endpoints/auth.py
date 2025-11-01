from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, Token
from app.core.security import get_password_hash, verify_password, create_access_token

router = APIRouter()


@router.post(
    "/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    # Check if user exists
    if db.query(User).filter(User.email == user_in.email).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )

    if db.query(User).filter(User.username == user_in.username).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Username already taken"
        )

    # Create user
    user = User(
        email=user_in.email,
        username=user_in.username,
        hashed_password=get_password_hash(user_in.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@router.post("/login", response_model=Token)
def login(username: str, password: str, db: Session = Depends(get_db)):
    # Find user
    user = db.query(User).filter(User.username == username).first()

    # Validate user and password
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create token
    access_token = create_access_token(data={"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}
