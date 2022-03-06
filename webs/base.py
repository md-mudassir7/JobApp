from fastapi import APIRouter

from webs.jobs import route_jobs
from webs.users import route_users
from webs.auth import route_login
api_router = APIRouter()

api_router.include_router(route_jobs.router,prefix="",tags=["homepage"])
api_router.include_router(route_users.router,prefix="",tags=["users"])
api_router.include_router(route_login.router,prefix="",tags=["auth"])
