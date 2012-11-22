#coding: utf-8
import sys, unittest
from CTMDriver import CTMDriver

class TestSuite1(unittest.TestCase):
    def setUp(self):
        self.driver = CTMDriver("ts-test/ctpm")
        self.driver.WinAuthLogin()

    def testChangeSearchCriteria(self):
        try:
            driver = self.driver
            driver.get(driver.SiteList)
            #driver.ClickElement("//input[@value='Change Search...']")
            driver.ClickButtonVl('Change Search...')
            if driver.SwitchToWindowTitle('Change Search'):
                driver.SelectDDItem("_ctl7_ddlStudyNo_imgExpand", "SDY-005")
                #driver.ClickElement("//input[@value='Search'][@type='button']")
                driver.ClickButtonVl('Search123')
                driver.SwitchToParentWindow()
            else:
                print "Unable to switch to 'Change Search' window"
        except Exception, e:
            self.fail(msg="Test ChangeSearchCriteria failed with message: %s" % e)
        self.assertEqual(driver.FindInFramesXPRec("//*[@class = 'criteriaValue']").text, "SDY-005")

    def tearDown(self):
        self.driver.close()

#code to run from command string:
##if __name__ == "__main__":
##    unittest.main()

#code to run from any place:
suite = unittest.TestLoader().loadTestsFromTestCase(TestSuite1)
unittest.TextTestRunner(verbosity=2).run(suite)