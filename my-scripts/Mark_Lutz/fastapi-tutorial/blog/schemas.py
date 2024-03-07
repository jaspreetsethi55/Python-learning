from pydantic import BaseModel

#request blog model
class Blog(BaseModel):
    title: str
    body: str

#response blog model
class ShowBlog(BaseModel):
    title: str
    #Below is to tell that we'll be getting the response from orm(e.g. sqlalchemly) db model
    class Config():
        orm_mode = True

#request user model
class User(BaseModel):
    name: str
    email: str
    password: str

#request user model
class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True
