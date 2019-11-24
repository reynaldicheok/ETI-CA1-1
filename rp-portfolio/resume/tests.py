from django.test import TestCase

# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("localhost:8000/blog")

link = driver.find_element_by_link_text('Testing Blog')
link.click()

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)

driver.find_element_by_id('id_author').send_keys('Reynaldi')

driver.find_element_by_id('id_body').send_keys('Hello there')

driver.find_element_by_class_name('btn btn-primary')
        
