# Dockerfile

# pull base image
FROM python:3.7

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set working directory
WORKDIR /code

# copy dependency requirements file
COPY requirements.txt /code/

# install dependencies from file
RUN pip install -r requirements.txt

# Copy project
COPY . /code/