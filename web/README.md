# Web Browser Automation Example

* Test some basic functionality of the [BBC Homepage](http://www.bbc.co.uk/)
    * Top Article
    * Terms of Use

# Setup

`docker` must be installed


# Run Example

```bash
    docker-compose run --rm --service-ports chrome-debug

    docker-compose run --rm --no-deps pytest --pdb
```

* See the tests working
    * `vnc://localhost:5900/` (`localhost` is your docker-machine hostname)
    * You need a `vnc` client
        * [tigervnc](http://tigervnc.org/)?

Reports are placed in `reports` folder. Open `report.html` file in your browser.

# Documentation

* [pytest](https://docs.pytest.org/) - The test runner (commandline options, layout tests)
    * [pytest-selenium](https://github.com/pytest-dev/pytest-selenium/blob/master/docs/user_guide.rst)
* [selenium-python](http://selenium-python.readthedocs.io/) - library for controlling the browser
