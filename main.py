from unicodedata import name
from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base
from apis.version1.route_users import router
from apis.base import api_router
from webs.base import api_router as web_router
from fastapi.staticfiles import StaticFiles
def create_tables():
    Base.metadata.create_all(bind = engine)

def include_router(app):
    app.include_router(api_router)
    app.include_router(web_router)

def configure_static(app):
    app.mount("/static",StaticFiles(directory="static"),name="static")

def start_app():
    app = FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    configure_static(app)
    return app


app = start_app()
