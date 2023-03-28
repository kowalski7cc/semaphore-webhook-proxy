FROM python:3.11-alpine
WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY src/semaphore_webhook_proxy semaphore_webhook_proxy
ENTRYPOINT [ "uvicorn", "semaphore_webhook_proxy.main:app" ]
CMD ["--host", "0.0.0.0", "--port", "80"]
