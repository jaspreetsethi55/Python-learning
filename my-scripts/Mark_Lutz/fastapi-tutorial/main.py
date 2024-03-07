from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI() ##this object is our application name
#If we name this as "myapp = FastAPI()", then we need to reload our server as "uvicorn main:myapp reload"
#and also in decorator , we need to give @myapp.get('/') instead of @app.get('/')

#"uvicorn main:app reload"
#basically, "main" is our python filename & "app" our application(object name i.e. app = FastAPI()) name
#if we have our script name as jaspreet.py then use "uvicorn jaspreet:app reload"



@app.get('/')  ##decorator the function with FastAPI object.
def index():
    return { 'data': {
                    'name' : 'Jaspreet Sethi'
                    }
    }

###Basic terminology
# "('/')" is known as "path" & "get" is known as "operation"
# and function we use below decorator is known as "path operation function".E.g. def index()

#Note: we can even use same name "path operation function" for different operation/path

@app.get('/about')
def index():
    return { 'data': 'About Page'}

@app.get('/blog/home')
def home():
    return { 'data': 'This is home' }

@app.get('/blog/{id}') ##{id} is path parameter
def blog(id : int):  #"id: int" means we are expecting id as integer , if another API will throw error
                     ##similarly, we can use other data types like str, float, etc as well
                     ## this 'type' system of any data conversion are done via 'pydantic' library
    return { 'data': id}

@app.get('/blog/{id}/comments') ##{id} is path parameter
def comments(id : int):  #"id: int" means we are expecting id as integer , if another API will throw error
    return { 'data': { id : ['1','2','3,'] }}


##Note: api path(resource path) should always be in specifid order i.e. path param should path should be
#after resource path. E.g. If we have 3 below api's path
#1. '/'
#2. '/path/name'
#3. '/path/{id}'
#The sequence of making api's path/functions should always be 1,2,3 else let us say, if we have provided
#in order 1,3,2 and for 3. {id} is int then if we search http://url/path/abc then we intend to match it with
#2. but accidentely it will match with 3. and give us error. So path param(e.g {id}) api i.e. dynamic route should
# always be after resource api i.e. static route if path-param resource are at same level

##Documentation(swagger like) -  http://127.0.0.1:8000/docs:
#Fast api provides default api documentation e.g. http://127.0.0.1:8000/docs - this will give us swagger like ui doc

##Another documentation -  http://127.0.0.1:8000/redoc


####Query params
@app.get('/records')
def get_records(limit = 10, published: bool = True, sort: Optional[str] = None): #limit,published & sort are query params e.g. /blog/records?limit=10&published=true
                                  #limit & published will be required bu default. We can default them in the
                                  # function header itself to make them optional or we can directly define query param optional
                                  # (from typing import Optional) as we have done for 'sort' via "sort : Optional[str] = None"
    if published:
        return { 'data': f'{limit} published blog records' }
    else:
        return { 'data': f'{limit} blog records' }

#param param vs query param
#@app.get('/records{id}')
#def get_records(limit = 10, published: bool = True, sort: Optional[str] = None):
#Fast api checks if function param is also there in resource param e.g. id and take it as patah param
# otherwise if not thre in resource param and there as a param in function then it is query param



####Request Body - put/post api's####
#To declare a request body, we use Pydantic models i.e. "from pydantic import BaseModel"
#then we can make ur own "data model" i.e. declare a class inheriting "BaseModel" and assign variables under it,
# then we can use this class in our function as "parameter" all these variables will be used as 'json' request

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return f'Blog {request.title} is created with request:{request}'


###Running fastapi uvicorn server directly from script or changing port
#if __name__ == '__main__':
#    import uvicorn
#    uvicorn.run(app,host="127.0.0.1",port=9000)
