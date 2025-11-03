from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from firebase_admin import auth
from app.schemas.user import User
from app.crud.user import crud_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token['uid']

        # Fetch user from the database to get their roles
        user = crud_user.get(uid)
        if not user:
            # If the user doesn't exist in our database, create them
            user_data = {"id": uid, "email": decoded_token.get("email", ""), "roles": ["user"]}
            user = User(**user_data)
            crud_user.create(user)

        return user
    except Exception as e:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
