FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /kt_team_test
WORKDIR /kt_team_test
add . /kt_team_test/
RUN pip install -r requirements.txt
COPY . /code/
