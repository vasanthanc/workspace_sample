import time
import eventlet
import socket
from retrying import retry
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.remote_connection import RemoteConnection


class SeleniumWebdriverV1:

    __driver = None

    def __init__(self,**kwargs):
        pass

    def init_selenium(self, **kwargs):
        done = False
        eventlet.monkey_patch()
        max_counter = 3
        while not done:
            print("inside while")
            try:
                with eventlet.Timeout(10):
                    self.__driver = webdriver.Remote(
                        command_executor='http://127.0.0.1:4444/wd/hub',
                        desired_capabilities=DesiredCapabilities.CHROME)
            except eventlet.timeout.Timeout as e:
                max_counter -= 1
                print("Unexpected timeout error, Error {}".format(str(e)))
                if max_counter <= 0:
                    break
            else:
                done = True
        return self.__driver

    def get_driver(self):
        if self.__driver:
            return self.__driver
        else:
            return self.init_selenium()

    def close_driver(self):
        if self.is_session_alive:
            self.__driver.quit()
            self.__driver.stop_client()
            self.__driver = None
        else:
            self.__driver = None

    def load_page(self,url,**kwargs):
        if self.__driver:
            xpath_to_wait_for_element = kwargs.get('xpath_to_wait_for_element', None)
            try:
                self.__driver.get(url)
                if xpath_to_wait_for_element:
                    print("Going to wait for element")
                    WebDriverWait(self.__driver, 30).until(
                        EC.presence_of_element_located((By.XPATH, xpath_to_wait_for_element))
                    )
                    print("Page is ready!")
            except Exception as e:
                print("{}".format(str(e)))
            except TimeoutException:
                print("Loading took too much time!")

    def is_session_alive(self):
        try:
            self.__driver.find_element_by_xpath("//*")
            return True
        except (socket.error, Exception) as e:
            print(str(e))
            return False
        

    def find_element_by_xpath(self,xpath):
        element = None
        if self.is_session_alive:
            element = self.__driver.find_element_by_xpath(xpath)
        return element

    def find_elements_by_xpath(self,xpath):
        elements = None
        if self.is_session_alive:
            elements = self.__driver.find_elements_by_xpath(xpath)
        return elements

sele = SeleniumWebdriverV1()
# sele.init_selenium()
driver = sele.get_driver()
sele.load_page("https://www.expedia.co.in/Chennai-Hotels-ITC-Grand-Chola.h4942760.Hotel-Information?chkin=22%2F09%2F2017&chkout=23%2F09%2F2017&rm1=a2&regionId=0&hwrqCacheKey=ca60dd38-3488-4bb6-b591-003cf25bb326HWRQ1505355958016&vip=false&c=d87992be-9ff5-49a5-be06-f65fd1892ead&&exp_dp=9299&exp_ts=1505355958770&exp_curr=INR&swpToggleOn=false&exp_pg=HSR",xpath_to_wait_for_element="//span[contains(@class,'recommend-percentage')]")
time.sleep(10)
print(sele.is_session_alive())
percentage = sele.find_element_by_xpath("//span[contains(@class,'recommend-percentage')]")
print(percentage.text)
sele.close_driver()
# time.sleep(5)