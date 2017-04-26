# coding=utf-8
__author__ = 'eharcil'

import variables
import resources
import os
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import unittest
import logging
import logging.config
import linkGrabber

class Project21Residence(unittest.TestCase):

    logging.config.dictConfig(variables.LOGGING)
    logger = logging.getLogger(__name__)

    # def setUpClass(cls):
    #     pass

    # def tearDownClass(cls):
    #     cls.driver = variables.driver
    #     cls.driver.quit()

    def setUp(self):
        self.driver = variables.driver
        self.driver.get(variables.url)
        self.driver.maximize_window()
        if not os.path.exists(variables.daily_directory_for_screenshots+'\\'+variables.today):
            os.makedirs(variables.daily_directory_for_screenshots+'\\'+variables.today)


    def tearDown(self):
        self.driver.close()


    def test_TestCase_001_check_homepage_menu_is_present(self):
        # This test checks that the menu is present in the homepage
        # It also creates a daily folder and saves screenshots in it
        self.TC_ID = 'TC_ID_001'
        self.logger.info(self.TC_ID+'   check_homepage_menu_is_present   Starting')
        driver = self.driver
        sleep(2)
        #Check for the menu element
        assert driver.find_element_by_id("sp-menu").is_displayed() == True
        #Take screenshots with timestamp
        driver.find_element_by_id("sp-menu").screenshot\
            (variables.daily_directory_for_screenshots+variables.today+'\\'+self.TC_ID+' Homepage-Menu %s.jpg' % variables.now)
        self.logger.info(self.TC_ID+'   homepage menu is present in the page')
        self.logger.info(self.TC_ID+'   check_homepage_menu_is_present   Finished')


    def test_TestCase_002_check_1_2_3_4_rooms_apartment_images_are_enabled(self):
        # This test checks that the images for 1, 2, 3, 4 rooms apartments are enabled in the homepage
        self.TC_ID = 'TC_ID_002'
        self.logger.info(self.TC_ID+'   check_1_2_3_4_rooms_apartment_images_are_enabled   Starting')
        driver = self.driver
        sleep(2)
        assert driver.find_element_by_xpath("//img[@src='/images/grafica/slide/slide.jpg']").is_enabled() == True
        assert driver.find_element_by_xpath("//img[@src='/images/grafica/ap/gars1.jpg']").is_enabled() == True
        assert driver.find_element_by_xpath("//img[@src='/images/grafica/ap/2cam1.jpg']").is_enabled() == True
        assert driver.find_element_by_xpath("//img[@src='/images/grafica/ap/3cam1.jpg']").is_enabled() == True
        assert driver.find_element_by_xpath("//img[@src='/images/grafica/ap/4cam1.jpg']").is_enabled() == True
        driver.get_screenshot_as_file\
            (variables.daily_directory_for_screenshots+variables.today+'\\'+self.TC_ID+' Homepage %s.jpg' % variables.now)
        self.logger.info(self.TC_ID+'   1, 2, 3, 4 rooms apartment images are enabled')
        self.logger.info(self.TC_ID+'   check_1_2_3_4_rooms_apartment_images_are_enabled   Finished')

    def test_TestCase_003_check_contact_page(self):
        # This test checks the presence and validity of Contact page
        self.TC_ID = 'TC_ID_003'
        self.logger.info(self.TC_ID+'   check_contact_page   Starting')
        driver = self.driver
        sleep(2)
        driver.find_element_by_xpath("//a[@href='/index.php/contact']").click()
        sleep(5)
        # Check validity elements on the page
        assert driver.find_element_by_xpath("//img[@src='http://maps.gstatic.com/mapfiles/api-3/images/google4.png']").is_enabled() == True
        assert driver.find_element_by_xpath("//button[@class='btn btn-danger jsn-form-submit']").is_enabled() == True
        assert driver.find_element_by_xpath("//a[@href='mailto:andrei.cretu@21residence.ro']").is_enabled() == True
        assert driver.find_element_by_xpath("//a[@href='mailto:anamaria.muntean@21residence.ro']").text == 'anamaria.muntean@21residence.ro'
        assert driver.find_element_by_xpath("//a[@href='mailto:bogdan.mihai@21residence.ro']").text == 'bogdan.mihai@21residence.ro'
        # Take screenshots with timestamp
        driver.get_screenshot_as_file\
            (variables.daily_directory_for_screenshots+variables.today+'\\'+self.TC_ID+' Contact page %s.jpg' % variables.now)
        self.logger.info(self.TC_ID+'   Validity elements on the page are enabled')
        self.logger.info(self.TC_ID+'   check_contact_page   Finished')


if __name__=='__main__':
    unittest.main(exit=False)