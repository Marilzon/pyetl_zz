from .http_request import HttpRequest

def test_request_from_page(requests_mock):
    url = "https://www.databricks.com/br/blog"
    response_context = "<h1>Databricks Blog Works!</h1>"
    requests_mock.get(url, status_code=200, text=response_context)

    http_request = HttpRequest()
    request_response = http_request.request_from_page()

    assert "status_code" in request_response
    assert "html" in request_response
    assert request_response["status_code"] == 200
    assert request_response["html"] == response_context
