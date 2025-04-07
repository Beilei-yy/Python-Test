import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# class create:
#     def setup_class(self):
# 设置cpability
caps ={
            "platformName": "Android",
            "appium:platformVersion": "12",
            "appium:deviceName": "xiaomi",
            "appium:appPackage": "notes.notepad.notebook.color.note",
            "appium:appActivity": "com.coocent.note2.ui.activity.main.MainActivity",
            "automationName": "UiAutomator2",
            "appium:noReset": True,
        }

# 初始化 driver
options = UiAutomator2Options()
options.load_capabilities(caps)
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
# # 设置全局隐藏式等待5s
# driver.implicitly_wait(5)