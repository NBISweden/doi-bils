FROM python:3.7.2-slim

WORKDIR /doi-nbis

USER root

COPY . ./

RUN useradd -ms /bin/bash nbis

RUN chown nbis:nbis app.py && \
    chown nbis:nbis settings.py && \
    chown nbis:nbis certs

RUN apt update && \
    python setup.py install

USER nbis

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
