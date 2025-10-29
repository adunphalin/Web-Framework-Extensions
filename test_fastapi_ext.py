
import asyncio
from web_exts.fastapi_ext import FastAPIExt, TimingMiddleware
from fastapi import FastAPI
from fastapi.testclient import TestClient

def test_fastapi_ext_status():
    app = FastAPI()
    ext = FastAPIExt()
    app.include_router(ext.get_router())
    app.add_middleware(TimingMiddleware)
    client = TestClient(app)
    r = client.get('/ext/status')
    assert r.status_code == 200
    assert r.json().get('status') == 'ok'
    assert 'X-Ext-Duration' in r.headers
