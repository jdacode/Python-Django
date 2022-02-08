# Recommended a lightweight image like Alpine
FROM python:3.7-alpine

# The python output is transmited directly to the terminal without been buffered
# That allow to display the application output in real time
# Also there is no partial output in the buffer in case that the python's program fails
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt

# Apk is the package manager for alpine
# --update = update the register
# --no-cache = no storing the register index in our docker file
# These options are for minimize the number of extra files and packages that are added to the docker container
RUN apk add --update --no-cache postgresql-client jpeg-dev

# --vitual = Sets an alias for the dependencies that can be remove easely later on
# And adding dependencies for postgres client
RUN apk add --update --no-cache --virtual .tmp-build-deps \ 
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Application folder
RUN mkdir /app
COPY ./app /app
WORKDIR /app