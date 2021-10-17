FROM python:3.8-buster

WORKDIR /code

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt


ENTRYPOINT ["bash"]
