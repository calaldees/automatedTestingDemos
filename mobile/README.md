# Mobile Automation Example

* Test Android `com.google.android.deskclock`
    * Set timer to 5 seconds and activate/stop
* Test iOS
    * TODO


# Setup

`docker` must be installed

Linux can use the `docker-container`
Windows and OSX need to install an `avd` (Android Virtual Device) and `appium` locally.

* Install an [avd](https://developer.android.com/studio/run/emulator)
    * Android Studio [Managing AVDs](https://developer.android.com/studio/run/managing-avds)
* Install [appium](https://github.com/appium/appium-desktop/releases/)
    * windows `choco install appium-desktop`
    * osx `brew cask install appium` or `npm install appium`


# Run Example

```bash
    # windows/osx open `avd` and `appium`
    docker-compose run --rm --service-ports android-container  # linux only (+see docker-compose.yml for --appium_host)

    docker-compose run --rm --no-deps pytest
```

* See the test working (linux only)
    * `http://docker-machine-host:6080/`

Reports are placed in `reports` folder. Open `report.html` file in your browser.

# Documentation

* [appium](http://appium.io/docs/en/about-appium/intro/)
* [UISelector](https://developer.android.com/reference/android/support/test/uiautomator/UiSelector)

# Other notes

http://www.automationtestinghub.com/apppackage-and-appactivity-name/
http://appium.io/docs/en/writing-running-appium/caps/
