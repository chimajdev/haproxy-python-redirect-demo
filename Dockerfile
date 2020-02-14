FROM python:3.8.1-alpine

RUN apk add --no-cache --virtual .build-deps gcc libc-dev make \
    && pip install uvicorn \
    && apk del .build-deps gcc libc-dev make

RUN mkdir /code
ADD app.py /code
ADD queueapp.py /code

WORKDIR /code

EXPOSE 8000

CMD  ["uvicorn", "app:main"]
