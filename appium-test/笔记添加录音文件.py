import cpability
import time
from appium.webdriver.common.appiumby import AppiumBy


#查找“创建笔记”按钮，并点击
el1 = cpability.driver.find_element(by=AppiumBy.ID, value="notes.notepad.notebook.color.note:id/floating_layout")
el1.click()
# 等待5s
time.sleep(5)
# 查找标题输入框点击并输入字符：“测试一下”
el2 = cpability.driver.find_element(by=AppiumBy.ID, value="notes.notepad.notebook.color.note:id/title_et")
el2.click()
el2.send_keys("测试一下")
#输入内容后等地2s
time.sleep(2)
# 查找文本输入框，并点击输入：test test
el3 = cpability.driver.find_element(by=AppiumBy.ID, value="notes.notepad.notebook.color.note:id/rich_editor_text")
el3.click()
el3.send_keys("test test")
#输入内容后等地2s
time.sleep(2)

# 查找”录音“按钮，并点击
el5 = cpability.driver.find_element(by=AppiumBy.ID, value="notes.notepad.notebook.color.note:id/recorder_iv")
el5.click()
#输入内容后等地5s
time.sleep(5)
# （弹出录音弹窗）查找”录制“按钮，并点击
el6 = cpability.driver.find_element(by=AppiumBy.ID, value="notes.notepad.notebook.color.note:id/record_iv")
el6.click()
# （录音弹窗）查找”完成“按钮，并点击
el7 = cpability.driver.find_element(by=AppiumBy.ID, value="notes.notepad.notebook.color.note:id/completed_layout")
el7.click()
# 点击录音文件“播放按钮
el8 = cpability.driver.find_element(by=AppiumBy.ID, value="notes.notepad.notebook.color.note:id/play_iv")
el8.click()
# 等待录制录制5s
time.sleep(5)
# 点击录音文件“暂停按钮
el8.click()
# 等待录制录制5s
time.sleep(5)
# 点击“返回”按钮，回至首页
el9 = cpability.driver.find_element(by=AppiumBy.ID, value="notes.notepad.notebook.color.note:id/back_iv")
el9.click()
def testdown_class(self):
    self.driver.quit()