from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests
import os


if os.environ.get("SEMAPHORE_URL") is None:
    raise ValueError("SEMAPHORE_URL is not set")

semaphore_url = os.environ.get("SEMAPHORE_URL")

while semaphore_url.endswith("/"):
    semaphore_url = semaphore_url[:-1]


app = FastAPI()


@app.get("/webhook-ping/")
def webhook_ping():
    return {"ping": "pong"}


@app.post("/webhook/{project_id}/template/{template_id}/")
def webhook(project_id: int, template_id: int, secret: str | None = None):
    if secret is None:
        return HTMLResponse(status_code=401, content="Unauthorized\n")
    response = requests.post(
        f"{semaphore_url}/api/project/{project_id}/tasks",
        json={
            "template_id": template_id,
        },
        headers={
            "Authorization": f"Bearer {secret}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return HTMLResponse(
            status_code=response.status_code, content=response.text
        )
    try:
        return response.json()
    except ValueError:
        return response.text
