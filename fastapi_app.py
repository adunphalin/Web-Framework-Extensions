
from fastapi import FastAPI
from web_exts.fastapi_ext import FastAPIExt, TimingMiddleware

app = FastAPI()
ext = FastAPIExt()
app.include_router(ext.get_router())
app.add_middleware(TimingMiddleware)

@app.get('/')
async def index():
    return {'message': 'Hello from FastAPI with FastAPIExt!'}
