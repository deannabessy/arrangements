# base image  
FROM python:3.8   

# setup environment variable  
ENV DOCKER_HOME=/code/tempFeedConsumer

# set work directory  
RUN mkdir -p $DOCKER_HOME

# where your code lives  
WORKDIR $DOCKER_HOME 

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy whole project to your docker home directory.
COPY . $DOCKER_HOME

# Upgrade pip, install dependencies
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt

# port where the Django app runs  
EXPOSE 8000  
# start server  
CMD python manage.py runserver
