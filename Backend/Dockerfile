FROM python:3.8-slim-buster

WORKDIR /Backend
COPY backend.py .
COPY req.txt .

RUN pip install -r req.txt
EXPOSE 30000 27017
CMD ["python","backend.py"]
