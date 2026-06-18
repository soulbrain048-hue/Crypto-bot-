from core.intelligence import route_query
from unittest.mock import patch

@patch('core.llm_client.llm_client.get_response')
def test_route_crypto_hindi(mock_get_response):
    mock_get_response.return_value = "[AGI Intelligence Bot] [क्रिप्टो मॉड्यूल] विश्लेषण।"
    query = "क्रिप्टो चेक करो"
    response = route_query(query)
    assert "[क्रिप्टो मॉड्यूल]" in response

@patch('core.llm_client.llm_client.get_response')
def test_route_bounty_hindi(mock_get_response):
    mock_get_response.return_value = "[AGI Intelligence Bot] [बाउंटी मॉड्यूल] टोही शुरू।"
    query = "बग बाउंटी शुरू करो"
    response = route_query(query)
    assert "[बाउंटी मॉड्यूल]" in response

@patch('core.llm_client.llm_client.get_response')
def test_route_workflow_hindi(mock_get_response):
    mock_get_response.return_value = "[AGI Intelligence Bot] [वर्कफ़्लो मॉड्यूल] सुझाव।"
    query = "मेरा काम आसान करो"
    response = route_query(query)
    assert "[वर्कफ़्लो मॉड्यूल]" in response

@patch('core.llm_client.llm_client.get_response')
def test_route_unknown_hindi(mock_get_response):
    mock_get_response.return_value = "[AGI Intelligence Bot] क्षमा करें, मैं केवल क्रिप्टो, बग बाउंटी और वर्कफ़्लो में मदद कर सकता हूँ।"
    query = "आज का मौसम क्या है?"
    response = route_query(query)
    assert "क्षमा करें" in response

@patch('core.llm_client.llm_client.get_response')
def test_route_case_insensitive_crypto(mock_get_response):
    mock_get_response.return_value = "[AGI Intelligence Bot] [क्रिप्टो मॉड्यूल] CRYPTO analysis."
    query = "CRYPTO query"
    response = route_query(query)
    assert "[क्रिप्टो मॉड्यूल]" in response
