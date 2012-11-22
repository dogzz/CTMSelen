#coding: utf-8
import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
import time, Tools, CTMConst
import ucsv as csv
from selenium.webdriver.common import keys
f1 = open('payees.csv', 'rb')
Payees = csv.reader(f1)
FailedPayees = []
driver = webdriver.Ie()
driver.implicitly_wait(5)
Tools.WinAuthLogin(CTMConst.CTMUrl, driver)
#------------
Field = driver.find_element_by_xpath("//input[@type='text'][@id='LoginPart__ctl5_txtUserName']")
Field.send_keys("bioctest1")
Field = driver.find_element_by_xpath("//input[@type='password']")
Field.send_keys("Suicide1`")

htmlElement = Tools.FindInFramesXP("//input[@value='Sign In'][@type='submit']", driver)
if htmlElement != None:
    htmlElement.click()
else:
    print "Error - Button Sign In is not found."

try:
        driver.switch_to_alert().accept()
        time.sleep(4)
        #driver.get("http://ts-host-3/ctpm/StudySetup/StudyList.aspx")
except(WebDriverException):
        time.sleep(4)
        #driver.get("http://ts-host-3/ctpm/StudySetup/StudyList.aspx")

#----------
for Payee in Payees:
    try:
        Tools.NavigateToScreen(CTMConst.PayeeList, driver)
##        inputElement = Tools.FindInFramesXP("//a[contains(text(), 'Next')]", driver)
##        if inputElement != None:
##            inputElement.click()
##        else:
##            print "Error - Next link is not found."
##        driver.switch_to_default_content()


        inputElement = Tools.FindInFramesXP("//a[contains(text(), '" + Payee[0] +"')]", driver)
        if inputElement != None:
            inputElement.click()
        else:
            print "Error - Payee is not found."
        driver.switch_to_default_content()

        inputElement = Tools.FindInFramesXP("//input[@value='Edit'][@id='btnSummary2']", driver)
        if inputElement != None:
            inputElement.click()
        else:
            print "Error - Edit button (CRF) is not found."
        driver.switch_to_default_content()

        inputElement = Tools.FindInFramesXP("//a[contains(text(), 'Load Settings from other Site')]", driver)
        if inputElement != None:
            inputElement.click()
        else:
            print "Error - Menu Item is not found."
        driver.switch_to_default_content()

        ParentWindow = driver.current_window_handle
        driver.switch_to_window(Tools.GetWindowHandle('Site budget loading', driver))

        htmlElement = Tools.FindInFramesXP("//input[@id='ddlSiteNo_txtValue']", driver)
        if htmlElement != None:
            htmlElement.send_keys(keys.Keys.ARROW_DOWN)
            htmlElement.send_keys(keys.Keys.ENTER)
        else:
            print "Error - Dropdown is not found."
        driver.switch_to_default_content()

        htmlElement = Tools.FindInFramesXP("//input[@value='Load'][@type='submit']", driver)
        if htmlElement != None:
            htmlElement.click()
        else:
            print "Error - Button Load is not found."
        time.sleep(5)
        #driver.switch_to_default_content()
        driver.switch_to_window(ParentWindow)

        time.sleep(5)

        inputElement = Tools.FindInFramesXP("//a[contains(text(), 'Save Site Budget')]", driver)
        if inputElement != None:
            inputElement.click()
        else:
            print "Error - Menu Item is not found."
        driver.switch_to_default_content()

        time.sleep(5)

        htmlElement = Tools.FindInFramesXP("//input[@value='Finish'][@type='submit']", driver)
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
##------


        inputElement = Tools.FindInFramesXP("//input[@value='Edit'][@id='btnSummary3']", driver)
        if inputElement != None:
            inputElement.click()
        else:
            print "Error - Edit button (CRF) is not found."
        driver.switch_to_default_content()

        inputElement = Tools.FindInFramesXP("//a[contains(text(), 'Load Settings from other Site')]", driver)
        if inputElement != None:
            inputElement.click()
        else:
            print "Error - Menu Item is not found."
        driver.switch_to_default_content()

        ParentWindow = driver.current_window_handle
        time.sleep(5)
        driver.switch_to_window(Tools.GetWindowHandle('Site budget loading', driver))

        htmlElement = Tools.FindInFramesXP("//input[@id='ddlSiteNo_txtValue']", driver)
        if htmlElement != None:
            htmlElement.send_keys(keys.Keys.ARROW_DOWN)
            htmlElement.send_keys(keys.Keys.ENTER)
        else:
            print "Error - Dropdown is not found."
        driver.switch_to_default_content()

        htmlElement = Tools.FindInFramesXP("//input[@value='Load'][@type='submit']", driver)
        if htmlElement != None:
            htmlElement.click()
        else:
            print "Error - Button Load is not found."
        time.sleep(5)
        #driver.switch_to_default_content()
        driver.switch_to_window(ParentWindow)

        time.sleep(5)

        inputElement = Tools.FindInFramesXP("//a[contains(text(), 'Save Site Budget')]", driver)
        if inputElement != None:
            inputElement.click()
        else:
            print "Error - Menu Item is not found."
        driver.switch_to_default_content()

        time.sleep(5)

        htmlElement = Tools.FindInFramesXP("//input[@value='Finish'][@type='submit']", driver)
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
##------

        inputElement = Tools.FindInFramesXP("//input[@value='Edit'][@id='btnSummary4']", driver)
        if inputElement != None:
            inputElement.click()
        else:
            print "Error - Edit button (CRF) is not found."
        driver.switch_to_default_content()

        inputElement = Tools.FindInFramesXP("//a[contains(text(), 'Load Settings from other Payee')]", driver)
        if inputElement != None:
            inputElement.click()
        else:
            print "Error - Menu Item is not found."
        driver.switch_to_default_content()

        ParentWindow = driver.current_window_handle
        driver.switch_to_window(Tools.GetWindowHandle('Payee budget loading', driver))

        htmlElement = Tools.FindInFramesXP("//input[@id='ddlSiteNo_txtValue']", driver)
        if htmlElement != None:
            htmlElement.send_keys(keys.Keys.ARROW_DOWN)
            htmlElement.send_keys(keys.Keys.ENTER)
        else:
            print "Error - Dropdown is not found."
        driver.switch_to_default_content()

        htmlElement = Tools.FindInFramesXP("//input[@value='Load'][@type='submit']", driver)
        if htmlElement != None:
            htmlElement.click()
        else:
            print "Error - Button Load is not found."
        time.sleep(5)
        #driver.switch_to_default_content()
        driver.switch_to_window(ParentWindow)

        time.sleep(5)

        inputElement = Tools.FindInFramesXP("//a[contains(text(), 'Save Site Budget')]", driver)
        if inputElement != None:
            inputElement.click()
        else:
            print "Error - Menu Item is not found."
        driver.switch_to_default_content()

        time.sleep(5)

        htmlElement = Tools.FindInFramesXP("//input[@value='Finish'][@type='submit']", driver)
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
##------


        htmlElement = WebDriverWait(driver, 10).until(lambda driver : Tools.FindInFramesXP("//a[contains(text(), 'Deploy Payee')]", driver))
        if htmlElement != None:
            htmlElement.click()
        else:
            print "Error - Deploy action link is not found."
        driver.switch_to_default_content()

        element = WebDriverWait(driver, 600).until(lambda driver : Tools.FindInFramesXP("//input[@value='Change Search...']", driver))
        driver.switch_to_default_content()
    except Exception, e:
        print "Exception message: %s" % e
        print "Some error occurs for " + Payee[0] + "!"
        FailedPayees.append(Payee[0])
        try:
            driver.switch_to_alert().accept()
            time.sleep(4)
        except(WebDriverException):
            time.sleep(4)

f1.close
for FP in FailedPayees:
    print "\n" + str(FN)