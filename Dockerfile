FROM python:3.9
WORKDIR /app
COPY . /app
RUN apt-get update
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "-k", "gunicorn.workers.geventlet.EventletWorker"]
