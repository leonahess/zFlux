FROM python:alpine

ADD src ./src
ADD config.json .
ADD zFlux.py .

ADD requirements.txt .

WORKDIR .

RUN pip3 install -r requirements.txt

RUN ln -sf /dev/stdout zFlux.log

CMD ["python3" , "zFlux.py"]
