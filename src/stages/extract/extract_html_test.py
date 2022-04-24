from src.drivers.tests.http_requester import HttpRequesterSpy
from src.drivers.tests.html_collector import HtmlCollectorSpy
from src.stages.contracts.extract_contract import ExtractContract
from src.errors.extract_error import ExtractError

from .extract_html import ExtractHtml

def test_extract():
    # Importing tested class
    http_requester = HttpRequesterSpy()
    #print()
    print(http_requester.__dict__)
    html_collector = HtmlCollectorSpy()

    # Object testing intancing (Dependency Injection)
    extract_html = ExtractHtml(http_requester,html_collector)
    response = extract_html.extract()
    #print()
    print(response)

    assert isinstance(response, ExtractContract)
    assert http_requester.request_from_page_count == 1
    assert 'html' in html_collector.collect_essential_information_attributes

def test_extract_error():
    # Importing tested class
    http_requester = 'This is error'
    html_collector = HtmlCollectorSpy()

    # Object testing intancing (Dependency Injection)
    extract_html = ExtractHtml(http_requester,html_collector)

    try:
        extract_html.extract()
    except Exception as exception: # pylint: disable=broad-except
        print(exception)
        assert isinstance(exception, ExtractError)
