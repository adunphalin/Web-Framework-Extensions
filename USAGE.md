
# Usage Notes

This document explains how the extension pieces fit into real apps.

## Flask

- Create `FlaskExt()` and call `init_app(app)`.
- The extension registers `/ext/status`.
- The extension sets `X-Ext-Duration` response header.

## FastAPI

- Create `FastAPIExt()` and include `ext.get_router()` in your app.
- Add `TimingMiddleware` via `app.add_middleware`.
- Use the `get_request_id` dependency to get a per-request UUID.
