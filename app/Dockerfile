FROM python:3.12-slim

WORKDIR /server

COPY requirements.txt /server/

RUN pip install --upgrade pip && pip install -r /server/requirements.txt

EXPOSE 8080

# COPY ./ /app

CMD ["python", "main.py"]