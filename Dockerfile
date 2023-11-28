FROM python:3

ARG UNAME=app
ARG UID=1000
ARG GID=1000

RUN groupadd -g ${GID} -o ${UNAME}
RUN useradd -m -d /app -u ${UID} -g ${GID} -o -s /bin/bash ${UNAME}

USER $UNAME

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=${UID}:${GID} . /app

#CMD ["tail", "-f", "/dev/null"]
CMD [ "python", "./helloworld.py" ]

LABEL maintainer="dfulmer@umich.edu"