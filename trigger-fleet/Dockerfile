FROM python:3.9-slim

WORKDIR /app
COPY . .
COPY trigger_fleet.py .
RUN pip install --no-cache-dir requests pandas

CMD ["python", "./trigger_fleet.py"]
