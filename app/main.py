from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Mount static folder
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Load templates
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/privacy-policy", response_class=HTMLResponse)
async def privacy_policy(request: Request):
    return templates.TemplateResponse("Privacy_Policy.html", {"request": request, "title": "Home Page"})



@app.get("/terms-of-service", response_class=HTMLResponse)
async def terms_of_service(request: Request):
    return templates.TemplateResponse("Terms_of_Service.html", {"request": request, "title": "Home Page"})
