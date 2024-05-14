FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir shipyard-api==0.2.0a0

COPY . .

ENTRYPOINT ["python", "/app/upsert_fleet.py"]
