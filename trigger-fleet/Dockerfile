FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir shipyard-api==0.2.0a0

ENTRYPOINT ["python", "/app/trigger_fleet.py"]

