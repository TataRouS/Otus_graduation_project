FROM python:3.12
# Set working directory
WORKDIR /app

# Copy dependency files
COPY requirements.txt ./

# Install dependencies, including pytest
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir /app/logs
RUN mkdir /app/allure-results

# Copy application code and tests
COPY tests /app/tests
COPY pages /app/pages
COPY utils /app/utils
COPY conftest.py /app/conftest.py
COPY index.py /app/index.py
COPY pytest.ini /app/pytest.ini
COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

# Run tests
ENTRYPOINT /app/entrypoint.sh