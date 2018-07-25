# Learning Test Automation

With guidance; I genuinely believe that any average computer user could become a professional tester in about 40 hours.

* 10 hours: Developer tooling and setup
* 10 hours: Selectors, 1 or 2 simple tests + debugger use
* 10 hours: Autonomous creation of your own tests and github repo
* 10 hours: Signup to crowd testing platform (for experience), update CV, study some testing terminology


## Step 1: Use developer tooling

* Understand the basics of your platforms _commandline_
* Use a _Package Manager_
    * Windows [choco](https://chocolatey.org/)
    * OSX [brew](https://brew.sh/)
    * Ubuntu [apt](https://help.ubuntu.com/lts/serverguide/apt.html.en)
* Use a _Code Editor_
    * [Visual Studio Code](https://code.visualstudio.com/)
        * `choco install vscode`
        * `brew cask install vscode`
* Understand basic [python3](https://docs.python.org/3/) syntax
    * Mostly by observation of the examples
* Understand the basics of _version control_ [git](https://git-scm.com/)
    * Beginners could start with [github native](https://desktop.github.com/)
    * Aspiring pros use _commandline_ `status`, `push`, `pull`, `commit`, `add`
* Understand basic formats
    * [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
    * [JSON](https://www.w3schools.com/js/js_json_syntax.asp)


## Step 2: Learn the concept of `selectors`

* Selectors
    * A way of specifying a UI item/component for automated testing
        * [CSS Selectors](https://www.w3schools.com/cssref/css_selectors.asp) (Web)
            * Chome/Firefox `ctrl+shift+i`
        * [UISelector](https://developer.android.com/reference/android/support/test/uiautomator/UiSelector) (Android)
            * [uiautomatorviewer](https://www.guru99.com/uiautomatorviewer-tutorial.html)
    * Other selector methods exists. I would avoid using these where possible
        * [XPath](https://www.w3schools.com/xml/xpath_intro.asp) (XML)


## Step 3: Construct a few simple basic tests

Create a few tests for a website you visit regularly.

* Explore + Experiment with your automation api
    * [selenium-python](http://selenium-python.readthedocs.io/)
    * [appium:python-client](https://github.com/appium/python-client)
* Use a _debugger_
    * `--pdb`
        * `assert False` (in the code to stop the execution of a test)
        * `aa = selenium.find_element(By.CSS_SELECTOR, '#any-element-on-page')`
        * `dir(aa)`


## Step 4: Page Object Models

Page Object Models are a common _design pattern_ for tests.
When writing multiple test we often find we are duplicating a set of common instructions.
If we abstract ANY interaction with selenium/appium in our own _Business Level_ abstraction, we can write more readable reusable code.

You don't need to be _master_ of them. But you should know what they are and why they are used.


## Step 5: Become a pro

1. Get some experience of remote crowd-sourced testing (and get paid)
    * [applause.com](https://www.applause.com/community/)
    * [crowdsourcedtesting.com](https://crowdsourcedtesting.com/en/freelance-software-testing-jobs)
    * [e4s](http://www.e4s.co.uk/part-time-jobs/online-user-testing-jobs.htm)
2. Show competence in _Test Automation_
    * Create some tests for any site
    * Create a `github` repo with your tests
    * Add to your CV that you know "Automated Testing with Selenium and Appium"
3. Get job


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
