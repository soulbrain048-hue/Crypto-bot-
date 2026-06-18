from modules.crypto import handle_crypto
from modules.bounty import handle_bounty
from modules.workflow import handle_workflow

def route_query(query):
    """
    कीवर्ड के आधार पर उपयोगकर्ता की क्वेरी को उचित मॉड्यूल पर रूट करता है।
    """
    query_lower = query.lower()

    # English and Hindi keywords
    if any(kw in query_lower for kw in ["crypto", "क्रिप्टो"]):
        return handle_crypto(query)
    elif any(kw in query_lower for kw in ["bounty", "बाउंटी", "बग"]):
        return handle_bounty(query)
    elif any(kw in query_lower for kw in ["workflow", "वर्कफ़्लो", "काम"]):
        return handle_workflow(query)
    else:
        return "क्षमा करें, मैं यह नहीं समझ पा रहा हूँ कि आपकी क्वेरी को किस मॉड्यूल पर भेजा जाए। कृपया 'क्रिप्टो', 'बाउंटी', या 'वर्कफ़्लो' जैसे कीवर्ड का उपयोग करें।"
