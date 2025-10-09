FROM python:3.11.5-slim

WORKDIR /tracker_app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main:app", "--host", "0.0.0.0", "--port", "8000"]
