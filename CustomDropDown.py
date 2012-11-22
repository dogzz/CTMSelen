#coding: utf-8
import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
import time, Tools, CTMConst

driver = webdriver.Ie()
driver.implicitly_wait(5)
Tools.WinAuthLogin(CTMConst.CTMUrl, driver)
#------------

Tools.NavigateToScreen(CTMConst.SiteList, driver)

inputElement = Tools.FindInFramesXPRec("//input[@value='Change Search...']", driver)
if inputElement != None:
    inputElement.click()
else:
    print "Error - Next link is not found."
driver.switch_to_default_content()

ParentWindow = driver.current_window_handle
driver.switch_to_window(Tools.GetWindowHandle('Change Search', driver))

htmlElement = Tools.FindInFramesXPRec("//img[@id='_ctl7_ddlStudyNo_imgExpand']", driver)
#htmlElement = Tools.FindInFramesXPRec("//td/span[contains(text(), '/Study/57 No.:')]/../following-sibling::td[1]//img[@id='_ctl7_ddlStudyNo_imgExpand']", driver)
if htmlElement != None:
    htmlElement.click()
    #htmlElement.send_keys(keys.Keys.ENTER)
else:
    print "Error - Dropdown is not found."

htmlElement = Tools.FindInFramesXPRec("//td[contains(@class, 'ddlExItem')][contains(text(), 'AutoQA')]", driver)
if htmlElement != None:
    htmlElement.click()
    #htmlElement.send_keys(keys.Keys.ENTER)
else:
    print "Error - List item is not found."


driver.switch_to_default_content()

htmlElement = Tools.FindInFramesXPRec("//input[@value='Search'][@type='button']", driver)
if htmlElement != None:
    htmlElement.click()
else:
    print "Error - Button Load is not found."
driver.switch_to_default_content()
driver.switch_to_window(ParentWindow)
