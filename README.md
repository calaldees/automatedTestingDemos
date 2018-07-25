# Automated Testing

When we release software, does the software perform the task it was created to do.
If not; why are we releasing it?

Rather than constantly running the software as a human; taking ages and getting board and making mistakes. Could we get a computer to do those checks and give us an "It works" or "It's buggered"? Wouldnt it be good if that happened automatically every time the software is changed?

Welcome to automated testing!
It's a highly employable skill and the concepts are fairly straightforward.


# This Repository: Python Automated Testing Demos

Automated testing tooling is hard to setup and deploy.

This repo has example flows of web and mobile automated testing.

# Technology's Used

* [selenium](https://www.seleniumhq.org/) Web Browser automation control
* [appium](http://appium.io/) Android and iOS automation control
* [pytest](https://docs.pytest.org) Extendible python testing framework
    * [selenium-python](http://selenium-python.readthedocs.io/)
    * [appium:python-client](https://github.com/appium/python-client)
    * [pytest-selenium](https://github.com/pytest-dev/pytest-selenium/blob/master/docs/user_guide.rst)
    * [pytest-appium](https://github.com/calaldees/pytest-appium)
* [docker](https://www.docker.com/)
    * docker makes it simpler to setup for local development and easyer to integrate into production build jobs.


# Common Testing Terminology

* Unit Tests
    * Tests that functions/methods/modules (normally in the software code/languages itself)
* Integration Tests (test multiple components work together)
    * Tests a user journey/flow
* Functional Test
    * Check 'x' feature works (login, purchase, terms & conditions)
* Non Functional Test
    * Performance
    * Security
* Assertion
    * Test have a number of assertions 'when we click the x, _assert_ we see the y'
* A 'Test Script'
    * A list of features/flows/instructions to test (can be automated or manual)
* A 'Test Report'
    * A list of tests that passed/failed (and why [screen-shots and error-messages]) (can be automated or manual)
* Business Features (in ranked order)
    * A unit of functionality the business requires (not the software provides). E.g. Terms and Conditions pages are of great legal importance to a business but not really for users.
* Release Process (automated is referred to as Release Pipeline)
    * The steps/checks/process's that must take place before software is released (can be automated or manual)
* Selector
    * A way of specifying a UI item/component for automated testing
        * [CSS](https://www.w3schools.com/cssref/css_selectors.asp) (Web)
        * [UISelector](https://developer.android.com/reference/android/support/test/uiautomator/UiSelector) (Android)
        * [XPath](https://www.w3schools.com/xml/xpath_intro.asp) (XML)
