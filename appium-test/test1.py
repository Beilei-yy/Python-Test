from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
options.load_capabilities({                                #发送参数到Appium服务器，以便Appium知道你想要自动化的事物类型
	"platformName": "Android",
	"appium:platformVersion": "12",
	"appium:deviceName": "xiaomi",
	"appium:appPackage": "notes.notepad.notebook.color.note",
	"appium:appActivity": "com.coocent.note2.ui.activity.main.MainActivity",
    "automationName": "UiAutomator2",
	"appium:noReset": False,
	# "appium:ensureWebviewsHavePages": True,
	# "appium:nativeWebScreenshot": True,
	# "appium:newCommandTimeout": 3600,
	# "appium:connectHardwareKeyboard": True
})
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
print("已打开note应用..")

el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Drawer open")   #查找“侧边栏”按钮
el1.click()                                                                    #点击
el2 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"备份与恢复\"]")   #查找“备份与恢复”按钮
el2.click()                                                                     #点击

time.sleep(10)                               #qian

driver.quit()                                #关闭与appium的连接
print("结束")