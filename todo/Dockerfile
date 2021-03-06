FROM python:3.9.2-alpine3.12

LABEL MAINTAINER="FirstName LastName <example@domain.com>"

WORKDIR /opt

COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP="/opt/todo/todo.py"
ENV FLASK_DEBUG=1
ENV FLASK_ENV="development"
CMD  ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]