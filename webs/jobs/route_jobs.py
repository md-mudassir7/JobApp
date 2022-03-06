from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import responses, status
from fastapi.security.utils import get_authorization_scheme_param
from db.repository.jobs import list_jobs
from sqlalchemy.orm import Session
from db.session import get_db
from fastapi import Depends
from db.repository.jobs import retreive_job

from db.models.users import User  
from apis.version1.route_login import get_current_user_from_token
# from webapps.jobs.forms import JobCreateForm
from schemas.jobs import JobCreate
from db.repository.jobs import create_new_job


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
def home(request:Request,db:Session = Depends(get_db),msg:str = None):
    jobs = list_jobs(db=db)
    return templates.TemplateResponse("jobs/homepage.html",{"request":request,"jobs":jobs,"msg":msg})

@router.get("/detail/{id}")
def job_detail(id:int, request:Request,db:Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    return templates.TemplateResponse("jobs/detail.html", {"request":request,
    "job":job})