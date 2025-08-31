FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT pytest tests/opencart_ui --browser remote  --alluredir allure-results --selenoid_url=${SELENOID_URL}