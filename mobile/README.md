# Mobile Automation Example

* Test Android `com.google.android.deskclock`
    * Set timer to 5 seconds, activate timer then stop
* Test iOS
    * TODO


## Setup

`docker` must be installed

Linux can use the `android-container` (docker-container)
Windows and OSX need to install `appium` and `avd` (Android Virtual Device) locally.

* Run [appium](https://github.com/appium/appium-desktop/releases/)
    * windows `choco install appium-desktop`
    * osx `brew cask install appium` or `npm install appium`
* Attach Device
    * Run an _Android Virtual Device_ [avd](https://developer.android.com/studio/run/emulator)
        * Android Studio [Managing AVDs](https://developer.android.com/studio/run/managing-avds)
    * or _real Android device_ via USB
        * Ensure the device has _Developer Mode_ on and has _USB Debugging_ enabled


## Run Example

```bash
    # windows/osx
    #   open `appium`
    #  run `avd` or `attach real device`
    docker-compose run --rm --service-ports android-container  # linux only (+see docker-compose.yml for --appium_host)

    docker-compose run --rm --no-deps pytest
```

* See the test working (linux only)
    * `http://docker-machine-host:6080/`

Reports are placed in `reports` folder. Open `report.html` file in your browser.

# Documentation

* [pytest](https://docs.pytest.org/) - The test runner (commandline options, layout tests)
    * [pytest-appium](https://github.com/calaldees/pytest-appium)
* [appium:python-client](https://github.com/appium/python-client)
* [appium](http://appium.io/docs/en/about-appium/intro/)
* [UISelector](https://developer.android.com/reference/android/support/test/uiautomator/UiSelector)


# Other notes

* [Identify apppackage-and-appactivity-name](http://www.automationtestinghub.com/apppackage-and-appactivity-name/)
* [Appium Capabilities](http://appium.io/docs/en/writing-running-appium/caps/)
