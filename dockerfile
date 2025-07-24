FROM python:3.10-slim
WORKDIR /app
COPY . .

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential poppler-utils || \
    (sleep 10 && apt-get install -y --no-install-recommends build-essential poppler-utils) && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]