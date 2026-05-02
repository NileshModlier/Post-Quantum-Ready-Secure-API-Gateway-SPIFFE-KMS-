
FROM python:3.11-slim
WORKDIR /gateway
COPY gateway/ ./gateway/
RUN pip install fastapi uvicorn
EXPOSE 8000
CMD ["uvicorn", "gateway.main:app", "--host", "0.0.0.0", "--port", "8000"]
