from fastapi import status, HTTPException, Depends, Response, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import models, schemas, oauth2
from ..database import get_db


router = APIRouter(prefix='/posts', tags=['Posts'])


# @router.get('/', response_model=list[schemas.PostResponse])
@router.get('/', response_model=list[schemas.PostOut])
async def get_all_posts(db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: str | None = ""):
    """
    Gets all Posts
    """
    result = db.query(models.User, func.count(models.Vote.post_id).label('votes'))\
                .join(models.Vote, isouter=True)\
                .group_by(models.User.id)\
                .filter(models.User.title.contains(search)).limit(limit).offset(skip)\
                .all()

    return result


@router.post('/', response_model=schemas.PostResponse)
async def create_post(new_post: schemas.Post, db: Session = Depends(get_db), get_current_user : int = Depends(oauth2.get_current_user)):
    
    new_post = models.User(user_id=get_current_user.id, **new_post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get('/{id}', response_model=schemas.PostOut)
async def get_a_post(id: int, db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
    # post = list(filter(lambda x: x["id"]==id, temp_post))
    post = db.query(models.User, func.count(models.Vote.post_id).label('votes'))\
                .join(models.Vote, isouter=True)\
                .group_by(models.User.id)\
                .filter(models.User.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id: {id} not found')
    return post


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_post(id: int, db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
    count = db.query(models.User).filter(models.User.id == id)
    if not count or count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Post with id: {id} was not found')
    if count.first().user_id != get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    count.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)