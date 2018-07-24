from pytest_appium.android.UIAutomator2 import UiSelector


def test_android_clock_timer(appium_extended):
    appium = appium_extended

    def tap_tab(tab_name):
        appium.wait_for(
            UiSelector()
            .resourceIdMatches('.*tabs')
            .childSelector(
                UiSelector()
                    .className('android.widget.TextView')
                    .textContains(tab_name.upper())
            )
            .build()
        ).click()

    def tap_digit(digit):
        appium.wait_for(
            UiSelector()
            .resourceIdMatches(f'.*timer_setup_digit_{digit}')
            .build()
        ).click()

    def tap_fab(content_desc):
        appium.wait_for(
            UiSelector()
            .resourceIdMatches('.*fab')
            .descriptionContains(content_desc)
            .build()
        ).click()

    tap_tab('TIMER')
    tap_digit(5)
    tap_fab('Start')
    tap_fab('Stop')
