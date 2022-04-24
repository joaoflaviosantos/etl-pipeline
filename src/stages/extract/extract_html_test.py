from src.drivers.http_requester import HttpRequester
from src.drivers.html_collector import HtmlCollector
from src.stages.contracts.extract_contract import ExtractContract
from src.errors.extract_error import ExtractError

from .extract_html import ExtractHtml

def test_extract():
    # Importing tested class
    http_requester = HttpRequester()
    html_extractor = HtmlCollector()

    # Object testing intancing (Dependency Injection)
    extract_html = ExtractHtml(http_requester,html_extractor)
    response = extract_html.extract()
    print()
    print(response)

    assert isinstance(response, ExtractContract)

def test_extract_error():
    # Importing tested class
    http_requester = 'This is error'
    html_extractor = HtmlCollector()

    # Object testing intancing (Dependency Injection)
    extract_html = ExtractHtml(http_requester,html_extractor)

    try:
        extract_html.extract()
    except Exception as exception: # pylint: disable=broad-except
        assert isinstance(exception, ExtractError)
