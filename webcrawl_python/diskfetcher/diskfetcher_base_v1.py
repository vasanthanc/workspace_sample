import urllib.request

import logging


FORMAT = "%(asctime)-15s %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

logger = logging.getLogger(__name__)

class DiskfetcherBaseV1(object):
    def __init__(self, url, **kwargs):
        self.request_type_and_its_equivalent_function_name = {
            "urllib" : self.get_page_content_using_urllib,
            "POST" : self.get_page_content_using_post,
            "GET" : self.get_page_content_using_get
        }
        self.version = "v1.0"
        self.url= url
        self.request_type = kwargs.get("request_type", "urllib")
        if self.request_type == "POST":
            self.payload = kwargs.get("payload", None)
        self.request_header = kwargs.get("request_header", {})
        self.page_content_hash = None

    def get_page_content_hash(self):
        current_request_type_function = self.request_type_and_its_equivalent_function_name.get(self.request_type)
        if current_request_type_function:
            current_request_type_function()

        #if self.request_type == "urllib":
        #    self.page_content_hash = self.get_page_content_using_urllib()
        #elif self.request_type == "GET":
        #    self.page_content_hash = self.get_page_content_using_get()
        #elif self.request_type == "POST":
        #    self.page_content_hash = self.get_page_content_using_post()
        #else:
        #    self.page_content_hash = None

    def get_page_content_using_urllib(self):
        response_page_hash = {}
        response_hash = ""
        response_code = 0
        try:
            req = urllib.request.Request(url, None, self.request_header)
            with urllib.request.urlopen(req) as response:
                response_hash = response.read()
                response_code = response.getcode()
        except Exception as e:
            logging.info("{0}{1}{2}{3}{4}".format(dir(e), e.reason, e.filename, e.with_traceback, e.strerror))
        response_page_hash.update({'response_source': response_hash})
        response_page_hash.update({'response_code': response_code})
        logging.info(response_page_hash)
        return response_page_hash
        #pass

    def get_page_content_using_get(self):
        pass

    def get_page_content_using_post(self):
        pass


if __name__ == "__main__":
    url = "https://www.google.dd"
    #args_hash = {'request_type':'urllib'}
    args_hash = {}
    args_hash.update({'request_header' : {'User-Agent' : 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}})
    diskfetcher = DiskfetcherBaseV1(url,**args_hash)
    diskfetcher.get_page_content_hash()