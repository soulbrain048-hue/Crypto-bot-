from modules.crypto import handle_crypto
from modules.bounty import handle_bounty
from modules.workflow import handle_workflow

def route_query(query):
    """
    Routes the user query to the appropriate module based on keywords.
    """
    query_lower = query.lower()

    if "crypto" in query_lower:
        return handle_crypto(query)
    elif "bounty" in query_lower:
        return handle_bounty(query)
    elif "workflow" in query_lower:
        return handle_workflow(query)
    else:
        return "I'm sorry, I couldn't determine which module to route your query to. Try using keywords like 'crypto', 'bounty', or 'workflow'."
