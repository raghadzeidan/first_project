FROM python:3

WORKDIR /
ADD requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD cortex/ ./cortex/

ADD scripts/run_server.sh . 
EXPOSE 8000
CMD [ "bash", "run_server.sh" ]
