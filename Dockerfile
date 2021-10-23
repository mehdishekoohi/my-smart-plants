ARG SOURCE

FROM ${SOURCE}python:3.6-buster

WORKDIR /code

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt


ENTRYPOINT ["bash"]
