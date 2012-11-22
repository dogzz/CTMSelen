#coding: utf-8
import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
import time, unittest

class CTMDriver(webdriver.Ie):
    CTMUrl = ""
    StudyList = ""
    ContactList = ""
    PayeeList = ""
    SiteList = ""
    ParentWindow = ""
    CurrentWindow = ""
    def __init__(self, CTMUrl):
        self.CTMUrl = CTMUrl
        self.StudyList = "http://"+CTMUrl+"/StudySetup/StudyList.aspx"
        self.ContactList = "http://"+CTMUrl+"/ContactManagement/ContactList.aspx"
        self.PayeeList = "http://"+CTMUrl+"/Payment/PayeeList/PayeeList.aspx"
        self.SiteList = "http://"+CTMUrl+"/CTMS/SiteManagement/SiteList.aspx"
        webdriver.Ie.__init__(self)
        self.CurrentWindow = self.current_window_handle

    def WinAuthLogin(self):
        self.get("http://"+self.CTMUrl)
        try:
            self.switch_to_alert().accept()
            time.sleep(4)
        except(WebDriverException):
            time.sleep(4)

    def IsExistsXP(self, xpath):
        flag = False
        obj = self.find_elements_by_xpath(xpath)
        if obj is not None:
                flag = len(obj) != 0
        else:
                flag = False
        return flag


    def FindInFramesXP(self, xpath):
        element = None
        iframes = self.find_elements_by_tag_name('iframe')
        self.implicitly_wait(2)
        flag = self.IsExistsXP(xpath)
        for iframe in iframes:
            if flag:
                break
            try:
                self.switch_to_frame(iframe)
            except StaleElementReferenceException, e:
                print "FindInFramesXP failed for frame %s: %s" % (iframe, e)
            obj = self.find_elements_by_xpath(xpath)
        self.implicitly_wait(2)
        element = self.find_element_by_xpath(xpath)
        return element


    def FindInFramesXPRec(self, xpath):
        element = None
        self.implicitly_wait(2)
        flag = self.IsExistsXP(xpath)
        if not flag:
            iframes = []
            iframes = self.find_elements_by_tag_name('iframe')
            if iframes != []:
                for iframe in iframes:
                    try:
                        self.switch_to_frame(iframe)
                        element = self.FindInFramesXPRec(xpath)
                    except StaleElementReferenceException, e:
                        print "FindInFramesXPRec failed for frame %s: %s" % (iframe, e)
                    if element == None:
                        if self.IsExistsXP(".."):
                            self = self.find_element_by_xpath("..")
                    else:
                        break
        self.implicitly_wait(2)
        if flag and element == None:
            element = self.find_element_by_xpath(xpath)
        return element

    def ClickElement(self, xpath):
        flag = False
        inputElement = self.FindInFramesXPRec(xpath)
        if inputElement != None:
            inputElement.click()
            flag = True
        else:
            print "Error - Element with xpath '%s' is not found." % xpath
        self.switch_to_default_content()
        return flag

    def GetWindowHandle(self, Title):
        CorrectWindow = ''
        Handles = self.window_handles
        self.ParentWindow = self.current_window_handle
        for Handle in Handles:
            self.switch_to_window(Handle)
            try:
                if Title in self.title:
                    self.switch_to_window(self.ParentWindow)
                    CorrectWindow = Handle
                    break
            except Exception, e:
                print "GetWindowHandle failed for window %s: %s" % (Handle, e)
        return CorrectWindow

    def SwitchToWindowTitle(self, Title):
        flag = False
        Handle = self.GetWindowHandle(Title)
        if Handle != '':
            self.switch_to_window(Handle)
            self.CurrentWindow = self.current_window_handle
            flag = True
        else:
            flaf = False
        return flag

    def SwitchToParentWindow(self):
        self.switch_to_window(self.ParentWindow)

    def SelectDDItem(self, ImgExpandId, ItemName):
        flag = False
        if self.ClickElement("//img[@id='%s']" % ImgExpandId):
            if self.ClickElement("//td[contains(@class, 'ddlExItem')][contains(text(), '%s')]" % ItemName):
                flag = True
        return flag

    def ClickButtonVl(self, Value):
        flag = False
        if self.ClickElement("//input[@value='%s'][@type='button' or @type='submit']" % Value):
            flag = True
        return flag



##Test Part
##driver = CTMDriver("ts-test/ctpm")
##driver.WinAuthLogin()
##driver.get(driver.SiteList)
##driver.ClickElement("//input[@value='Change Search...']")
##if driver.SwitchToWindowTitle('Change Search'):
##    driver.SelectDDItem("_ctl7_ddlStudyNo_imgExpand", "SDY-005")
##    driver.ClickElement("//input[@value='Search'][@type='button']")
##    driver.SwitchToParentWindow()
##else:
##    print "Unable to switch to 'Change Search' window"