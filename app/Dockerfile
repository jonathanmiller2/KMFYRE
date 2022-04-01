FROM python:3

RUN echo 'got here'

ENV PYTHONUNBUFFERED 1

#Create and cd into /code/ on the container, then copy all of the files in the same directory as this Dockerfile from the normal filesystem into /code/ on the container
WORKDIR /code
COPY . .
WORKDIR /code/app

RUN apt-get update
RUN apt-get install binutils gettext libgettextpo-dev libproj-dev gdal-bin netcat -y

#Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#Run entrypoint.sh
ENTRYPOINT ["/code/app/entrypoint.sh"]