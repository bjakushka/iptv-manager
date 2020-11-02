FROM python:3.8-slim

RUN adduser flask

WORKDIR /home/flask

COPY requirements.txt requirements.txt
RUN python -m venv .venv
RUN .venv/bin/pip install --upgrade pip
RUN .venv/bin/pip install -r requirements.txt
RUN .venv/bin/pip install gunicorn==20.0.4

COPY app app
COPY app.py boot.sh ./

RUN chown -R flask:flask ./
RUN chmod +x boot.sh
USER flask

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
