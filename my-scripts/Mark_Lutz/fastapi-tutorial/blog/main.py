from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext

app = FastAPI()

models.Base.metadata.create_all(engine) ##this will create the db tables from models.py


'''
@app.post('/blog')
def create(request : schemas.Blog):
    return request
'''

##since we need to save our post request to db so, we also need to pass 'db' session in function
# E.g. def create(request : schemas.Blog, db):
#           return db
# but this will treat 'db' as query param
# Since we don't need as query param, so we can define 'db' as type of 'Session'(from sqlalchemy.orm import Session)
# def create(request : schemas.Blog, db: Session)
# but even now we'll get error "<class 'sqlalchemy.orm.session.Session'> is a valid pydantic field type"
# So, we have to use def create(request : schemas.Blog, db: Session = Depends(get_db ) -- this will actually
# convert Session in to pydantic form, where 'Depends' needs to be imported from fastapi and we need to create a
# new function named as 'get_db' which will get the db Session/connection

def get_db():
    db = SessionLocal() # coming from database.py
    try:
        yield db
    finally:
        db.close()

@app.post('/blog')
def create(request : schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog) ## adding row in db
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}')
def show(id,db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blogs

##Handling default response status code
##Ideally when we create something, the standard response is 201 but we get success response as 200. So we can
#change this via passing parameter 'status_code=201' in @app.post decorator
#@app.post('/blogs',status_code=201) #this will make 201 as default success response code
@app.post('/blogs',status_code=status.HTTP_201_CREATED) #we can directly use import 'status' from fastapi & use inbuilt fastapi codes
def create(request : schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog) ## adding row in db
    db.commit()
    db.refresh(new_blog)
    return new_blog

##changing response status code
#E.g. if we'll pass any {id} to below api that doesn't exists it will return 'null' response but in realtime, we need to
#handle this and return 404. We can handle this via below:
#we need to import 'Response' from fastapi & then create parameter in function of Response type.Eg. response: Response
#then use 'response.status_code' inside function to change the status based on any condition
@app.get('/blogs/{id}')
def show(id,response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return { 'details': f"Blog with id:{id} not found"}
        ##Instead of raising except manually & returning like we did above, we can directly import 'HTTPException' from
        # fastapi & use 'raise HTTPException(status_code: status.HTTP_404_NOT_FOUND, detail: f"Blog with id:{id} not found")'
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with id:{id} not found")
    return blogs

##Delete a record by id
@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {'success': f"id:{id} deleted"}


##Update a record by id
@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    # We don't have to use 'request' in function for this.
    #db.query(models.Blog).filter(models.Blog.id == id).update({'title': 'updated_title'})

    #we can directly pass the json request as well(use request in function too)
    #db.query(models.Blog).filter(models.Blog.id == id).update(request.dict())

    #using above, even if we'll pass any {id} i.e. not in DB, even then we'll not get error
    #so, we've to handle this
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id:{id} not found")

    blog.update(request)
    db.commit()

    return 'updated'

#####Response Model###
# we have 2 models here:
# 1. pydantic model(our schemas.py) - here we are talking about response model in schemas
# 2. sqlalchemy model i.e. database model(database.py models.py)

#we need to pass response model in decorator
@app.get('/get_blogs/{id}', response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with id:{id} not found")
    return blogs

#we need to pass 'List[schemas.ShowBlog]' in case of multiple(list) response. import 'List' from 'typing'
@app.get('/show_all_blogs', response_model=List[schemas.ShowBlog])
def show_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()

    return blogs


#####Creating User Info

@app.post('/user')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    #new_user = models.User(name=request.name,email=request.email,password=request.password)
    new_user = models.User(**request.dict())
    db.add(new_user)  ## adding row in db
    db.commit()
    db.refresh(new_user)
    return new_user

####password encryption
#we need to use 'passlib' module for this. So first install it via requirements.txt

pwd_cxt =  CryptContext(schemes=["bcrypt"], deprecated="auto")
#we also need to add 'brcypt' python module to use this, so add it to requirements.txt

@app.post('/en_user')
def create_encrypted_user(request: schemas.User, db: Session = Depends(get_db)):
    hashed_password = pwd_cxt.hash(request.password)
    new_user = models.User(name=request.name,email=request.email,password=hashed_password)
    db.add(new_user)  ## adding row in db
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post('/en_user_res',response_model=schemas.ShowUser) ##now we are not returning password in response
def create_encrypted_user_with_response(request: schemas.User, db: Session = Depends(get_db)):
    hashed_password = pwd_cxt.hash(request.password)
    new_user = models.User(name=request.name,email=request.email,password=hashed_password)
    db.add(new_user)  ## adding row in db
    db.commit()
    db.refresh(new_user)
    return new_user

##Also, we can pass 'tags' in our decorator, this will put this api under that particular tag instead of 'default' tag
@app.get('/user/{id}',response_model=schemas.ShowUser,tags=['user']) ##now we are not returning password in response
def create_encrypted_user_with_response(id, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id:{id} not found")
    return user