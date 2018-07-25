# Learning Test Automation

## Step 1: Learn the concept of `selectors`

* Selectors
    * A way of specifying a UI item/component for automated testing
        * [CSS Selectors](https://www.w3schools.com/cssref/css_selectors.asp) (Web)
        * [UISelector](https://developer.android.com/reference/android/support/test/uiautomator/UiSelector) (Android)
    * Other selector methods exists. I would avoid using these where possible
        * [XPath](https://www.w3schools.com/xml/xpath_intro.asp) (XML)


## Step 2: Construct a few simple basic tests

* Explore + Experiment with your automation api
    * [selenium-python](http://selenium-python.readthedocs.io/)
    * [appium:python-client](https://github.com/appium/python-client)
* Use a _debugger_
    * `--pdb`


## Step 3: Page Object Models

Page Object Models are a common _design pattern_ for tests.
When writing multiple test we often find we are duplicating a set of common instructions.
If we abstract ANY interaction with selenium/appium in our own _Business Level_ abstraction, we can write more readable reusable code.


## Common Testing Terminology

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
    * See above
