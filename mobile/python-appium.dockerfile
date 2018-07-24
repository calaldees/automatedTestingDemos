FROM python:3
RUN pip3 install --upgrade pip setuptools virtualenv
WORKDIR /appium
COPY requirements.pip requirements.pip
RUN pip3 install -r requirements.pip

# docker build -t python-appium --file python-appium.dockerfile .
# docker run --rm -it -v ${pwd}:/appium:ro python-appium /bin/bash
