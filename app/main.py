# import dependencies
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# create app instance
app = FastAPI()

# set location for templates
templates = Jinja2Templates(directory="app/view_templates")

# handle http get requests for the site root /
# return the index.html page
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/advice", response_class=HTMLResponse)
async def advice(request: Request):
    return templates.TemplateResponse(request=request, name="advice.html")

@app.get("/apod", response_class=HTMLResponse)
async def apod(request: Request):
    return templates.TemplateResponse(request=request, name="apod.html")

@app.get("/params", response_class=HTMLResponse)
async def params(request: Request):
    return templates.TemplateResponse(request=request, name="params.html")


app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

