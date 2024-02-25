FROM python:3.12-slim

WORKDIR /app

COPY . /app

# RUN pip3 install flask flask_swagger_ui flask-restplus

RUN pip3 install flask flask-restful flask-swagger

EXPOSE 5001

CMD ["python3", "api.py"]