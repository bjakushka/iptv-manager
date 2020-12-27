# pull official base image
FROM python:3.8-alpine

RUN addgroup -g 1000 -S flask && \
    adduser -u 1000 -S flask -G flask

# set environment variables
ENV APP_HOME /home/flask
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR $APP_HOME

# install analog of `libmysqlclient-dev` for `mysqlclient` on python
# also install `gcc` for compling `mysqlclient` on python
# NOTE: probably we should not install such packages here - cause'
#       they are required only for setuping all dependencies
RUN apk add --update \
    mariadb-dev \
    gcc libc-dev \
    nodejs npm

# install dependencies
COPY ./requirements.txt $APP_HOME/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install gunicorn==20.0.4

# copy project
COPY . $APP_HOME
RUN chown -R flask:flask $APP_HOME && \
    chmod +x $APP_HOME/cli && \
    chmod +x $APP_HOME/docker-entrypoint.sh
USER flask

# building frontend
RUN npm install && \
    npm run build

# run application
EXPOSE 5000
ENTRYPOINT ["/home/flask/docker-entrypoint.sh"]
