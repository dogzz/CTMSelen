#coding: utf-8
import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
import time, Tools, CTMConst
import ucsv as csv
from selenium.webdriver.common import keys
f1 = open('studies.csv', 'rb')
Studies = csv.reader(f1)
f1.close
driver = webdriver.Ie()
driver.implicitly_wait(5)
Tools.WinAuthLogin(CTMConst.CTMUrl, driver)
#------------
Field = driver.find_element_by_xpath("//input[@type='text'][@id='LoginPart__ctl5_txtUserName']")
Field.send_keys("Viktor.klymenko")
Field = driver.find_element_by_xpath("//input[@type='password']")
Field.send_keys("Suicide1`")

htmlElement = Tools.FindInFramesXPRec("//input[@value='Sign In'][@type='submit']", driver)
if htmlElement != None:
    htmlElement.click()
else:
    print "Error - Button Sign In is not found."

#----------
for StudyNo in Studies:
    try:
        Tools.NavigateToScreen(CTMConst.StudyList, driver)
        inputElement = Tools.FindInFramesXPRec("//a[starts-with(text(), '3')]", driver)
        if inputElement != None:
            inputElement.click()
        else:
            print "Error - Next link is not found."
        driver.switch_to_default_content()


        inputElement = Tools.FindInFramesXPRec("//a[contains(text(), '" + StudyNo[0] +"')]", driver)
        if inputElement != None:
            inputElement.click()
        else:
            print "Error - Study is not found."
        driver.switch_to_default_content()

        inputElement = Tools.FindInFramesXPRec("//input[@value='Edit'][@id='btnSummary4']", driver)
        if inputElement != None:
            inputElement.click()
        else:
            print "Error - Edit button is not found."
        driver.switch_to_default_content()

        inputElement = Tools.FindInFramesXPRec("//a[contains(text(), 'Load from other Study')]", driver)
        if inputElement != None:
            inputElement.click()
        else:
            print "Error - Menu Item is not found."
        driver.switch_to_default_content()

        ParentWindow = driver.current_window_handle
        driver.switch_to_window(Tools.GetWindowHandle('Load Components', driver))

        htmlElement = Tools.FindInFramesXPRec("//input[@id='ddlStudyNo_txtValue']", driver)
        if htmlElement != None:
            htmlElement.send_keys(keys.Keys.ARROW_DOWN)
            htmlElement.send_keys(keys.Keys.ENTER)
        else:
            print "Error - Dropdown is not found."
        driver.switch_to_default_content()

        htmlElement = Tools.FindInFramesXPRec("//input[@value='Load'][@type='submit']", driver)
        if htmlElement != None:
            htmlElement.click()
        else:
            print "Error - Button Load is not found."
        driver.switch_to_default_content()
        driver.switch_to_window(ParentWindow)

        time.sleep(5)

        inputElement = Tools.FindInFramesXPRec("//a[contains(text(), 'Save')]", driver)
        if inputElement != None:
            inputElement.click()
        else:
            print "Error - Menu Item is not found."
        driver.switch_to_default_content()

        time.sleep(12)

        htmlElement = Tools.FindInFramesXPRec("//input[@value='Finish'][@type='submit']", driver)
        if htmlElement != None:
            #all this shit doesn't work - probably the Finish button is not disabled at all...
            wait = WebDriverWait(driver, 10)
            def enable(element):
                if element.is_enabled():
                    return element
                return null
            htmlElement = wait.until(lambda d: enable(htmlElement))
            htmlElement.click()
        else:
            print "Error - Button Finish is not found."
        driver.switch_to_default_content()
        driver.implicitly_wait(5)

        htmlElement = WebDriverWait(driver, 10).until(lambda driver : Tools.FindInFramesXPRec("//a[contains(text(), 'Deploy')]", driver))
        if htmlElement != None:
            htmlElement.click()
        else:
            print "Error - Deploy action link is not found."
        driver.switch_to_default_content()

        element = WebDriverWait(driver, 600).until(lambda driver : Tools.FindInFramesXPRec("//input[@value='Change Search...']", driver))
        driver.switch_to_default_content()
    except Exception, e:
        print "Exception message: %s" % e
        print "Some error occurs for " + StudyNo[0] + "!"
        try:
            driver.switch_to_alert().accept()
            time.sleep(4)
        except(WebDriverException):
            time.sleep(4)

