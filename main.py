from fastapi import FastAPI, Request
from fastapi_versioning import VersionedFastAPI, version
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI(
    title='Hema versioning apps',
    description='This api is to control backend versioning with fastappi',
    middleware=[
        Middleware(SessionMiddleware, secret_key='mysecretkey')
    ]
)

@app.get('/greet')
@version(1)
def greet(request: Request):
    request.session['last_version_used'] = 1
    return 'Hello'

@app.get('/greet')
@version(2)
def greet(request: Request):
    request.session['last_version_used'] = 2
    return 'Hi'

@app.get('/version')
def last_version(request: Request):
    return f'Your last greeting was sent from version {request.session["last_version_used"]}'

app = VersionedFastAPI(app,
    version_format='{major}',
    prefix_format='/v{major}',
    description='Greet users with a nice message',
    middleware=[
        Middleware(SessionMiddleware, secret_key='mysecretkey')
    ]
)