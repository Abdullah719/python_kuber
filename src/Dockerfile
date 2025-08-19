FROM python:3.11-alpine
WORKDIR /app

# requirements.txt is in project root
COPY requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# copy the src folder (this Dockerfile's directory)
COPY . /app/src

# run the script directly (no PYTHONPATH, no -m)
CMD ["python", "/app/src/app.py"]
