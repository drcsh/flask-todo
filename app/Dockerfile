FROM python:3.9.2-alpine3.12

LABEL MAINTAINER="FirstName LastName <example@domain.com>"

WORKDIR /opt

COPY . .
RUN rm -rf *.pyc
RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1
CMD  ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]