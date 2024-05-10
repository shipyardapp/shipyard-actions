FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir shipyard-api==0.1.1

ENTRYPOINT ["python3", "/app/shipyard_api/cli/trigger_fleet.py"]
