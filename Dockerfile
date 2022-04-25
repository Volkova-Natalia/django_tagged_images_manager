FROM python:3.8-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /tagged_images_manager_service
WORKDIR /tagged_images_manager_service/

ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY . /tagged_images_manager_service/

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade Pillow

RUN python3 -m pip install Django==3.1.6
RUN python3 -m pip install django-cors-headers==3.7.0
RUN python3 -m pip install djangorestframework==3.12.2
RUN python3 -m pip install psycopg2-binary==2.9.3
RUN python3 -m pip install python-dotenv==0.15.0