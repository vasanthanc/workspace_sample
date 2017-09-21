import urllib3
import os
from internal_utils.log_utils import Logger as logger
# from bs4 import BeautifulSoup
from selenium import webdriver
# import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from lxml import html
from pyparsing import makeHTMLTags, withAttribute, SkipTo


class UltraProxyList(object):
    def __init__(self):
        # chrome_service = service.Service('http://127.0.0.1:9515')
        # chrome_service.start()
        # capabilities = {'chrome.binary': '/usr/bin/google-chrome-stable'}
        # driver = webdriver.Remote(chrome_service.service_url, capabilities)
        # self.driver = webdriver.Chrome('/home/vasanthan/Downloads/chromedriver')
        # self.driver = webdriver.Chrome('/usr/bin/google-chrome-stable')
        self.log_utils = logger()
        self.url = "http://www.ultraproxies.com/"
        self.http = urllib3.PoolManager(retries=urllib3.Retry(3, redirect=2))

    def fetch_html_page(self):
        response = None
        try:
            self.log_utils.info(self.driver)
            self.driver.get(self.url)
            time.sleep(5)
            htmlSource = self.driver.page_source
            # response = self.http.request('GET', self.url)
        except Exception as e:
            self.log_utils.error(e)
        return response

    def parse_response_data_to_page_dom(self):
        response = self.fetch_html_page()
        page_source = response.data
        # html_dom = BeautifulSoup(page_source, 'html.parser')
        html_dom = html.fromstring(page_source)
        return html_dom

    def get_proxy_list_with_information(self):
        html_dom = self.parse_response_data_to_page_dom()
        proxy_table = html_dom.xpath("//table[contains(@class,'proxy') and .//tr[contains(@align,'top')]]")
        if proxy_table:
            table_rows = proxy_table[0].xpath(".//tr[position()>1]")
            for table_row in table_rows:
                ip_address_node = table_row.xpath("./td[contains(@class ,'ip')]/text()")[0] if table_row.xpath("./td[contains(@class ,'ip')]/text()") else None
                port_number_node = table_row.xpath("./td[contains(@class,'port')]/text()")[0] if table_row.xpath("./td[contains(@class,'port')]/text()") else None
                country_name_node = table_row.xpath("./td[position()=6]/text()")[0] if table_row.xpath("./td[position()=6]/text()") else None
                ip_address_value = self.get_value_from_node(ip_address_node)
                port_number_value = self.get_value_from_node(port_number_node)
                country_name_value = self.get_value_from_node(country_name_node)
                self.log_utils.info("IP : {}".format(ip_address_value) + "\n")
                self.log_utils.info("PoRT : {}".format(port_number_value) + "\n")
                self.log_utils.info("COUNTRY : {}".format(country_name_value) + "\n")

    def get_value_from_node(self,node):
        string_value = None
        if node:
            # self.log_utils.info(node)
            string_value = str(node)
        return string_value

if __name__ == "__main__":
    ultra_proxy = UltraProxyList()
    ultra_proxy.get_proxy_list_with_information()