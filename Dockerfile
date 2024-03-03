FROM python:3.12-slim

WORKDIR /app

COPY . /app

# RUN pip3 install flask flask_swagger_ui flask-restplus

RUN pip3 install flask flask-restful flask-swagger_ui

EXPOSE 8080

CMD ["python3", "new_app.py"]
