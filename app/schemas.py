from pydantic import BaseModel, EmailStr, conint, validator


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


class PostResponse(Post):
    id: int
    user_id: int
    owner: UserResponse
    class Config:
        from_attributes = True


class PostOut(BaseModel):
    User: PostResponse
    votes: int
    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str




        
class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int | None = None
    username: str | None = None


class VoteData(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1)

    @validator('dir')
    def validate_dir(cls, v):
        if v not in [0, 1]:
            raise ValueError('dir must be either 0 or 1')
        return v