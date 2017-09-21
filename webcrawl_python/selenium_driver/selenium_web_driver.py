from selenium import webdriver

from internal_utils.log_utils import Logger as logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SeleniumWebDriver:

    def __init__(self,url,**kwargs):
        self.log_utils = logger()