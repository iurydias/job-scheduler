FROM python:3.8-slim
RUN apt-get update && apt-get install -y build-essential
ENV APPDIR /app
WORKDIR $APPDIR
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . $APPDIR
CMD python3 -u main.py