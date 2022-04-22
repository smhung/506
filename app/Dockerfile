FROM python:3.10.4-slim-bullseye
RUN pip3 install flask flask-wtf email_validator requests flask-login flask-sqlalchemy
COPY views.py views.py
CMD python views.py
