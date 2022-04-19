FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /srv/homework2/app/static
COPY ./requirements.txt /srv/homework2/requirements.txt
RUN pip install -r /srv/homework2/requirements.txt

