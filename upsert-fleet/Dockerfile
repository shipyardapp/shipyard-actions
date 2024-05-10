FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir requests pyyaml

COPY . .

ENTRYPOINT ["python", "/app/upsert_fleet.py"]
