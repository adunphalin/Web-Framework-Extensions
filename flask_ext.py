
from flask import Blueprint, current_app, g, request
import time

class FlaskExt:
    """Simple Flask extension providing a status blueprint and timing middleware."""
    def __init__(self, name='web_exts'):
        self.name = name
        self.bp = Blueprint('web_exts', __name__, url_prefix='/ext')
        self._register_routes()

    def _register_routes(self):
        @self.bp.route('/status')
        def status():
            return {'status': 'ok', 'ext': self.name}

    def init_app(self, app):
        app.register_blueprint(self.bp)
        # attach before_request and after_request handlers
        @app.before_request
        def _before():
            g.ext_start_time = time.time()
        @app.after_request
        def _after(response):
            start = getattr(g, 'ext_start_time', None)
            if start is not None:
                duration = time.time() - start
                # log if app has logger
                try:
                    app.logger.debug(f"[FlaskExt] request={request.path} duration={duration:.4f}s")
                except Exception:
                    pass
                response.headers['X-Ext-Duration'] = f"{duration:.4f}"
            return response
