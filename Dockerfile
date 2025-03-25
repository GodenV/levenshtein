FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile --system

WORKDIR /app
COPY . .

RUN chmod 777 /app/run.sh

EXPOSE 8000

CMD /app/run.sh
