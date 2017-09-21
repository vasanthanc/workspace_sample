from urllib3 import util as urllib3_utls
from validators import url as url_validator
from validators import utils as validators_utls

from internal_utils.log_utils import Logger as logger

class UrlUtls(object):
    def __init__(self,url):
        self.url = url
        self.logging = logger(object)

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, uri):
        if not uri: raise Exception("description cannot be empty")
        self._url = uri

    def url_validation(self):
        is_valid = False
        try:
            is_valid = url_validator(self.url)
            if isinstance(is_valid,validators_utls.ValidationFailure):
                raise ValidationFailure(is_valid)
        except ValidationFailure as e:
            is_valid = False
            self.logging.error(e)
        return is_valid

    def get_host_name_from_url(self):
        host_name = None
        if self.url_validation():
            parsed_url = urllib3_utls.parse_url(self.url)
            logger.info(parsed_url.query)
            scheme = parsed_url.scheme
            host = parsed_url.host
            port = parsed_url.port
            host_name = scheme + "://" + host if not port else scheme + "://" + str(host) + ":" + str(port)
        return host_name

class ValidationFailure(Exception):
    pass

if __name__ == "__main__":
    url_val = UrlUtls("http://google.com?res=true&gender=male")
    hostname = url_val.get_host_name_from_url()
    print(hostname)