# syntax=docker/dockerfile:1

# get base image
FROM python:3.7-slim-bullseye

# Copy required files into the container
COPY ["templates", "app/templates/"]
COPY ["static", "app/static/"]
COPY ["db_connector.py", "app/"]
COPY ["rest_app.py", "app/"]
COPY ["requirements.txt", "app/"]

# Set the working directory inside the container
WORKDIR /app

#rest is 5000, web is 5001
EXPOSE 5000

RUN pip install -r requirements.txt

# running the app with some sample linux commands
CMD python rest_app.py 