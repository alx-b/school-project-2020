FROM python:3.8-slim

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt \
 && mkdir -p /vol/static

WORKDIR /project

COPY . .

RUN chmod +x entrypoint.sh

RUN useradd user \
 && chown -R user:user /vol \
 && chmod -R 755 /vol/static \
 && chown -R user:user . \
 && chmod -R 755 .

USER user

WORKDIR /project/app

RUN python manage.py makemigrations \
 && python manage.py migrate --run-syncdb

CMD ["../entrypoint.sh"]
