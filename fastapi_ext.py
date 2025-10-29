
from fastapi import APIRouter, Depends, Request
from starlette.middleware.base import BaseHTTPMiddleware
import time
import uuid

def get_request_id():
    return str(uuid.uuid4())

class FastAPIExt:
    """Simple FastAPI extension providing a router, dependency, and middleware."""
    def __init__(self, prefix='/ext'):
        self.prefix = prefix
        self.router = APIRouter(prefix=self.prefix)
        self._register_routes()

    def _register_routes(self):
        @self.router.get('/status')
        async def status(request_id: str = Depends(get_request_id)):
            return {'status': 'ok', 'request_id': request_id}

    def get_router(self):
        return self.router

class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = time.time() - start
        response.headers['X-Ext-Duration'] = f"{duration:.4f}"
        # attempt to log
        try:
            request.app.logger.debug(f"[FastAPIExt] path={request.url.path} duration={duration:.4f}s")
        except Exception:
            pass
        return response
