import tempfile, os, pytest
from backend.app import create_app

@pytest.fixture
def app():
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    app = create_app(testing=True)
    app.config["DATABASE_PATH"] = path
    from backend.models.database import init_db
    init_db(path)
    yield app
    try: os.remove(path)
    except OSError: pass

@pytest.fixture
def client(app):
    return app.test_client()
