FROM python:3.9-slim

WORKDIR /usr/src/app

RUN pip install --no-cache-dir requests pyyaml

COPY . .

ENTRYPOINT ["python", "/usr/src/app/upsert_fleet.py"]
