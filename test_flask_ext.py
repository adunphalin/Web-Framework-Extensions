
from web_exts.flask_ext import FlaskExt
from flask import Flask

def test_flask_ext_status():
    app = Flask(__name__)
    ext = FlaskExt()
    ext.init_app(app)
    client = app.test_client()
    r = client.get('/ext/status')
    assert r.status_code == 200
    assert r.json.get('status') == 'ok'
    assert 'X-Ext-Duration' in r.headers
