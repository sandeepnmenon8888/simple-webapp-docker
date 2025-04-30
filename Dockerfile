FROM registry.access.redhat.com/ubi8/python-39

WORKDIR /app
COPY app.py .

RUN pip install --no-cache-dir flask

EXPOSE 5000
CMD ["python", "app.py"]
