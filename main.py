from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

# Create an instance of the FastAPI class
app = FastAPI()

# Mount the static directory to serve static files like CSS, JavaScript, images, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load templates from the "templates" directory
templates = Jinja2Templates(directory="templates")

# Define a route for the root endpoint ("/")
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Render the landing page template
    return templates.TemplateResponse("landing.html", {"request": request})

# Run the FastAPI application using the built-in development server.
if __name__ == "__main__":
    import uvicorn
    port = os.environ.get("PORT", 8080)
    uvicorn.run(app, host="0.0.0.0", port=int(port))
