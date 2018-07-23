FROM python:3
RUN pip3 install --upgrade pip setuptools virtualenv
WORKDIR /selenium
COPY requirements.pip requirements.pip
RUN pip3 install -r requirements.pip

# docker build -t python-selenium --file python-selenium.dockerfile .
# docker run --rm -it -v ${pwd}:/selenium:ro python-selenium /bin/bash
