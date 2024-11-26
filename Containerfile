FROM python:3.10-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev && apt-get clean

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]