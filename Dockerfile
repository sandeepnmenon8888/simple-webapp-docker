FROM python:3.9-alpine

WORKDIR /opt
COPY app.py .
RUN pip install flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
