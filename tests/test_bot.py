from core.intelligence import route_query

def test_route_crypto_hindi():
    query = "क्रिप्टो चेक करो"
    response = route_query(query)
    assert "[क्रिप्टो मॉड्यूल]" in response
    assert query in response

def test_route_bounty_hindi():
    query = "बग बाउंटी शुरू करो"
    response = route_query(query)
    assert "[बाउंटी मॉड्यूल]" in response
    assert query in response

def test_route_workflow_hindi():
    query = "मेरा काम आसान करो"
    response = route_query(query)
    assert "[वर्कफ़्लो मॉड्यूल]" in response
    assert query in response

def test_route_unknown_hindi():
    query = "आज का मौसम क्या है?"
    response = route_query(query)
    assert "क्षमा करें, मैं यह नहीं समझ पा रहा हूँ" in response

def test_route_case_insensitive_crypto():
    query = "CRYPTO query"
    response = route_query(query)
    assert "[क्रिप्टो मॉड्यूल]" in response
