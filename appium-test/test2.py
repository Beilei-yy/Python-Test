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
            "appium:noReset": False,
        }

# 初始化 driver
options = UiAutomator2Options()
options.load_capabilities(caps)
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
# # 设置全局隐藏式等待5s
# driver.implicitly_wait(5)

el1 = driver.find_element(by=AppiumBy.ID, value="notes.notepad.notebook.color.note:id/floating_layout")    #查找“创建笔记”按钮
el1.click()                                                                                                #点击
el2 = driver.find_element(by=AppiumBy.ID, value="notes.notepad.notebook.color.note:id/rich_editor_touch_layout")     #查找去掉主题提示
el2.click()                                                                                                #点击
el3 = driver.find_element(by=AppiumBy.ID, value="notes.notepad.notebook.color.note:id/title_et")           # 查找标题输入框
el3.click()
el3.send_keys("111")                                                                                       # 标题输入框输入字符：“111”
time.sleep(2)                                                                                              #输入内容后等地2s
el4 = driver.find_element(by=AppiumBy.ID, value="notes.notepad.notebook.color.note:id/rich_editor_text")    # 查找文本输入框
el4.click()
el4.send_keys("222")                                                                                        # 文本输入框输入字符：“222”
time.sleep(2)
el5 = driver.find_element(by=AppiumBy.ID, value="notes.notepad.notebook.color.note:id/back_iv")             # 点击“返回”按钮，回至首页
el5.click()

def testdown_class(self):
    self.driver.quit()