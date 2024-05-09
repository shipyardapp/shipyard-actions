FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir requests pandas


# Run script.py when the container launches
CMD ["python", "./trigger_fleet.py"]
