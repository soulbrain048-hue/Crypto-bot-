import pytest
from unittest.mock import MagicMock, patch
from core.intelligence import route_query

@patch('core.llm_client.llm_client.get_response')
def test_route_query_mocked(mock_get_response):
    # Setup mock response
    mock_get_response.return_value = "[AGI Intelligence Bot] यह एक क्रिप्टो विश्लेषण है।"

    query = "क्रिप्टो के बारे में बताओ"
    response = route_query(query)

    assert "[AGI Intelligence Bot]" in response
    assert "क्रिप्टो" in response
    mock_get_response.assert_called_once()

@patch('core.llm_client.llm_client.get_response')
def test_route_query_bounty_mocked(mock_get_response):
    mock_get_response.return_value = "[AGI Intelligence Bot] बग बाउंटी टोही शुरू।"

    query = "bug bounty tips"
    response = route_query(query)

    assert "[AGI Intelligence Bot]" in response
    assert "बग बाउंटी" in response
