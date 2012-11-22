#coding: utf-8
import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
import time

# Create a new instance of the Firefox driver
driver = webdriver.Ie()

# go to the google home page
driver.get("http://ts-host-3/ctpm")
driver.get("http://ts-host-3/ctpm/StudySetup/StudyList.aspx")

# find the element that's name attribute is q (the google search box)
#inputElement = driver.find_element_by_name("_ctl0$_ctl0$ContentPlaceHolder$InnerContentPlaceHolder$StudyListCtrl$psc$btnChange")

inputElement = driver.find_element_by_xpath("//input[@value='Change Search...']")
inputElement.click()
#driver.switch_to_window("mainFrame")
Handles = driver.window_handles
ParentWindow = driver.current_window_handle
#popup = webdriver.Ie()
for Handle in Handles:
    driver.switch_to_window(Handle)
    if 'Change Search' in driver.title:
        print driver.title
        break
#inputElement = driver.find_element_by_xpath("//input[@value='Reset']")
driver.switch_to_frame('frmWindow')
inputElement = driver.find_element_by_xpath("//input[@value='Reset'][@type='submit']")
inputElement.click()
inputElement = driver.find_element_by_xpath("//input[@value='Search'][@type='submit']")
inputElement.click()
driver.switch_to_window(ParentWindow)
# type in the search
#inputElement.send_keys("Cheese!")

# submit the form (although google automatically searches now without submitting)
#inputElement.submit()

# the page is ajaxy so the title is originally this:
print driver.title

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(lambda driver : driver.title.lower().startswith("cheese!"))

    # You should see "cheese! - Google Search"
    print driver.title

finally:
    driver.quit()