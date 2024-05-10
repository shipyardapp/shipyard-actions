FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir requests pandas

ENTRYPOINT ["python", "/app/trigger_fleet.py"]
