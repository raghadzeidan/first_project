FROM python:3

WORKDIR /
ADD requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD cortex/ ./cortex/
ADD scripts/api_server.sh . 
EXPOSE 5000
CMD [ "bash", "api_server.sh" ]
