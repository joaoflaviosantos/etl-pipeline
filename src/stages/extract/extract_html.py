from typing import Type
from src.drivers.interfaces.http_requester import HttpRequesterInterface
from src.drivers.interfaces.html_collector import HtmlCollectorInterface

class ExtractHtml:

    def __init__(self, http_requester: Type[HttpRequesterInterface], html_collector: Type[HtmlCollectorInterface]) -> None:
        self.__http_requester = http_requester
        self.__html_collector = html_collector

    def extact(self):
        html_information = self.__http_requester.request_from_page()
        essential_information = self.__html_collector.collect_essential_information(html_information["html"])
        return essential_information
