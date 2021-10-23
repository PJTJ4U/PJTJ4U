from fastapi import FastAPI, Form, Request
from pyngrok import ngrok
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import nest_asyncio
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory = "C:/Workspace/python/빅데이터 지능형서비스 개발 팀프로젝트/PJTJ4U/조정범/static"), name = "static")
templates = Jinja2Templates(directory = "C:/Workspace/python/빅데이터 지능형서비스 개발 팀프로젝트/PJTJ4U/조정범/templates")

@app.get('/', response_class=HTMLResponse)
async def home(request : Request) :
    return templates.TemplateResponse("index.html", context={"request": request})

# @app.get('/video/')
# async def video(request : Request) :
#     return templates.TemplateResponse("video.html", context={"request": request})


ngrok_tunnel = ngrok.connect(8000)
print ('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, host='0.0.0.0', port=8000)