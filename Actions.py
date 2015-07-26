#coding: utf-8
import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
import time, Tools, CTMConst

driver = webdriver.Ie()
driver.implicitly_wait(2)

Tools.WinAuthLogin(driver)
Tools.NavigateToScreen(CTMConst.StudyList, driver)
#asdasdasd orig in main updated in feature updated in feature 2
#new line in master
inputElement = Tools.FindInFramesXPRec("//input[@value='Change Search...']", driver)
if inputElement != None:
    inputElement.click()
else:
    print "Error - Button Change Search is not found."

ParentWindow = driver.current_window_handle
driver.switch_to_window(Tools.GetWindowHandle('Change Search', driver))

htmlElement = Tools.FindInFramesXPRec("//input[@value='Reset'][@type='button']", driver)
if htmlElement != None:
    htmlElement.click()
else:
    print "Error - Button Reset is not found."
driver.switch_to_default_content()
#inputElement = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath("//input[@value='Search'][@type='submit']"))
htmlElement = Tools.FindInFramesXPRec("//input[@value='Search'][@type='submit']", driver)
if htmlElement != None:
    htmlElement.click()
else:
    print "Error - Button Search is not found."
driver.switch_to_default_content()
driver.switch_to_window(ParentWindow)
print 'Window ' + driver.title
#driver.quit()
