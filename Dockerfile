FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

WORKDIR /app

ADD requirements.txt .
ADD modules/ .
ADD main.py .

RUN pip -r requirements.txt

CMD [“python”, “./main.py”] 