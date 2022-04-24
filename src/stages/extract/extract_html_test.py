from src.drivers.http_requester import HttpRequester
from src.drivers.html_collector import HtmlCollector

from .extract_html import ExtractHtml

def test_extract_html():
    # Importing tested class
    http_requester = HttpRequester()
    html_extractor = HtmlCollector()

    # Object testing intancing (Dependency Injection)
    extract_html = ExtractHtml(http_requester,html_extractor)
    response = extract_html.extact()
    print()
    print(response)
