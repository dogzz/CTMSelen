#coding: utf-8
import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
import time

def GetWindowHandle(Title, driver1):
    CorrectWindow = ''
    Handles = driver1.window_handles
    ParentWindow = driver1.current_window_handle
    print Handles
    for Handle in Handles:
        driver1.switch_to_window(Handle)
        print Handle
        try:
            if Title in driver1.title:
                #print driver.title
                driver1.switch_to_window(ParentWindow)
                CorrectWindow = Handle
                break
        except Exception, e:
            print "GetWindowHandle failed for window %s: %s" % (Handle, e)
    return CorrectWindow

def FindInFramesXP(xpath, driver):
    element = None
    iframes = driver.find_elements_by_tag_name('iframe')
    driver.implicitly_wait(2)
    obj = driver.find_elements_by_xpath(xpath)
    for iframe in iframes:
        #print type(obj)
        if obj is not None:
            flag = len(obj) != 0
        else:
            flag = False
        if flag:
            break
        try:
            driver.switch_to_frame(iframe)
        except StaleElementReferenceException, e:
            print "FindInFramesXP failed for frame %s: %s" % (iframe, e)
        obj = driver.find_elements_by_xpath(xpath)
    driver.implicitly_wait(2)
    element = driver.find_element_by_xpath(xpath)
    return element


def FindInFramesXPRec(xpath, driver):
    element = None
    driver.implicitly_wait(2)
    flag = len(driver.find_elements_by_xpath(xpath)) != 0
    if not flag:
        iframes = []
        iframes = driver.find_elements_by_tag_name('iframe')
        if iframes != []:
            for iframe in iframes:
                driver.switch_to_frame(iframe)
                element = FindInFramesXPRec(xpath, driver)
                if element == None:
                    if len(driver.find_elements_by_xpath("..")) > 0:
                        driver = driver.find_element_by_xpath("..")
                else:
                    break
    ##            flag = len(driver.find_elements_by_xpath(xpath)) != 0
    ##            if flag:
    ##                break
    driver.implicitly_wait(2)
    if flag and element == None:
        element = driver.find_element_by_xpath(xpath)
    return element


def WinAuthLogin(CTMUrl, driver):
    driver.get("http://"+CTMUrl)
    try:
        driver.switch_to_alert().accept()
        time.sleep(4)
        #driver.get("http://ts-host-3/ctpm/StudySetup/StudyList.aspx")
    except(WebDriverException):
        time.sleep(4)
        #driver.get("http://ts-host-3/ctpm/StudySetup/StudyList.aspx")


def NavigateToScreen(ScreenUrl, driver):
    driver.get(ScreenUrl)
