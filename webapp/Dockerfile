# syntax=docker/dockerfile:1

FROM ubuntu:latest
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3 python3-pip -y

# Set work dir
WORKDIR /app

# Copy files and install requirements
COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 8000

# Run the flask application
CMD ["python3", "-m", "gunicorn", "app:app"]