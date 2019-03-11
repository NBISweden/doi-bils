FROM python:3.7-slim

WORKDIR /doi-bils/

COPY . ./

RUN apt update && \
    python setup.py install

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
