from fastapi import status, HTTPException, Depends, APIRouter
from fastapi.exceptions import ResponseValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db


router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
async def create_user(new_user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        new_user.password = utils.hash(new_user.password)
        user = models.MainUser(**new_user.dict())
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except ResponseValidationError as ex:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail=f'User with email already exists. {new_user.email}')
    except IntegrityError as ex:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail={"message": f'User with email already exists. {new_user.email}',
            "error": str(ex.args[0])})


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.UserResponse)
async def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.MainUser).filter(models.MainUser.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f'User with id: {id} does not exists.')

    return user