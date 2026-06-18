from core.llm_client import llm_client

def route_query(query):
    """
    Groq LLM का उपयोग करके उपयोगकर्ता की क्वेरी को प्रोसेस करता है।
    """
    system_prompt = """
    आप एक AGI इंटेलिजेंस बोट हैं जो 'क्रिप्टो', 'बग बाउंटी' और 'कोडिंग वर्कफ़्लो' में माहिर है।
    उपयोगकर्ता के सवाल का जवाब हिंदी में दें।
    अगर सवाल इन तीन क्षेत्रों से संबंधित है, तो विशेषज्ञ की तरह जवाब दें।
    अगर नहीं, तो विनम्रता से बताएं कि आप इनमें विशेषज्ञ हैं।
    हमेशा अपनी पहचान '[AGI Intelligence Bot]' के रूप में करें।
    """

    full_prompt = f"{system_prompt}\n\nUser Query: {query}"

    response = llm_client.get_response(full_prompt)
    return response
