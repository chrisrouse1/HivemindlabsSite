import starlette
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
import uvicorn
import fastapi


templates = Jinja2Templates(directory='templates')

app = Starlette(debug=True)
app.mount('/static', StaticFiles(directory='statics'), name='static')


@app.route('/')
async def homepage(request):
    template = "index.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)


@app.route('/home')
async def homepage(request):
    template = "index.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)



@app.route('/index.html')
async def homepage(request):
    template = "index.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)   

@app.route('/error')
async def error(request):
    """
    An example error. Switch the `debug` setting to see either tracebacks or 500 pages.
    """
    raise RuntimeError("Oh no")

@app.route('/faqs')
async def faqs(request):
    template = "faqs.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)

@app.route('/faqs.html')
async def faqs_html(request):
    template = "faqs.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)


@app.route('/contact.html')
async def contact_html(request):
    template = "contact.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)


@app.route('/contact')
async def contact(request):
    template = "contact.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)

@app.route('/services.html')
async def services_html(request):
    template = "services.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)

@app.route('/services')
async def services(request):
    template = "services.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)

@app.route('/about-us')
async def homepage(request):
    template = "about-us.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)

@app.route('/about-us.html')
async def homepage(request):
    template = "about-us.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)


@app.exception_handler(404)
async def not_found(request, exc):
    """
    Return an HTTP 404 page.
    """
    template = "404.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context, status_code=404)


@app.exception_handler(500)
async def server_error(request, exc):
    """
    Return an HTTP 500 page.
    """
    template = "500.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context, status_code=500)

from fastapi import FastAPI
from starlette.requests import Request



##
##

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
