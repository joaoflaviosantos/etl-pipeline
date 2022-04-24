from typing import List, Dict

class HtmlCollectorSpy:

    def __init__(self) -> None:
        self.collect_essential_information_attributes = {}

    def collect_essential_information(self, html: str) -> List[Dict[str,str]]: # pylint: disable=arguments-differ
        self.collect_essential_information_attributes["html"] = html
        return [{"name": 'SomeName', "link": 'https://something.com'}]
