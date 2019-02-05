# Automated Testing

When we release software, does the software perform the task it was created to do.
If not; why are we releasing it?

Rather than constantly running the software as a human; taking ages and getting board and making mistakes. Could we get a computer to do those checks and give us an "It works" or "It's buggered"? Wouldnt it be good if that happened automatically every time the software is changed?

Welcome to automated testing!
It's a highly employable skill and the concepts are fairly straightforward.


# This Repository: Python Automated Testing Demos

Automated testing tooling is hard to setup and deploy.

This repo has example flows of web and mobile automated testing.

This repo has additional information about [Learning Automation](learn_automation.md)

# Using These Examples

All examples in this repo use `docker`.

Install [Docker](https://www.docker.com/community-edition) for your OS.


# Technology's Used

* [selenium](https://www.seleniumhq.org/) Web Browser automation control
    * Technology to remotely control a web browser
* [appium](http://appium.io/) Android and iOS automation control
* [pytest](https://docs.pytest.org) Extendible python testing framework
    * [selenium-python](http://selenium-python.readthedocs.io/)
    * [appium:python-client](https://github.com/appium/python-client)
    * [pytest-selenium](https://github.com/pytest-dev/pytest-selenium/blob/master/docs/user_guide.rst)
    * [pytest-appium](https://github.com/calaldees/pytest-appium)
* [docker](https://www.docker.com/)
    * docker makes it simpler to setup for local development and easier to integrate into production build jobs.
* [cypress](www.cypress.io) Web Browser automation framework
    * Technology to run tests inside a web browser with javascript