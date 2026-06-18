from core.intelligence import route_query

def test_route_crypto():
    query = "Check crypto prices"
    response = route_query(query)
    assert "[Crypto Module]" in response
    assert query in response

def test_route_bounty():
    query = "Start a bounty hunt"
    response = route_query(query)
    assert "[Bounty Module]" in response
    assert query in response

def test_route_workflow():
    query = "Improve my workflow"
    response = route_query(query)
    assert "[Workflow Module]" in response
    assert query in response

def test_route_unknown():
    query = "What is the weather?"
    response = route_query(query)
    assert "I'm sorry, I couldn't determine" in response

def test_route_case_insensitive():
    query = "CRYPTO query"
    response = route_query(query)
    assert "[Crypto Module]" in response
