FROM python:3.11-alpine
LABEL org.opencontainers.image.title="semaphore-webhook-proxy"
LABEL org.opencontainers.image.authors="kowalski7cc"
LABEL org.opencontainers.image.source=https://github.com/kowalski7cc/semaphore-webhook-proxy
LABEL org.opencontainers.image.description="Send a webhook in a format Semaphore likes"
LABEL org.opencontainers.image.licenses=Unlicense
WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY src/semaphore_webhook_proxy semaphore_webhook_proxy
ENTRYPOINT [ "uvicorn", "semaphore_webhook_proxy.main:app" ]
CMD ["--host", "0.0.0.0", "--port", "80"]
