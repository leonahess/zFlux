FROM python:alpine

ADD logs ./logs
ADD src ./src
ADD config.json .
ADD zFlux.py .

ADD requirements.txt .

WORKDIR .

RUN pip3 install -r requirements.txt

CMD ["python3" , "zFlux.py"]
