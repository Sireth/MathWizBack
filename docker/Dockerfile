FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3

RUN apt-get install -y pip

RUN mkdir /math_wiz_back

WORKDIR /math_wiz_back

COPY requirements.txt /math_wiz_back/requirements.txt


RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /math_wiz_back/