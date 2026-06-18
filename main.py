import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from core.intelligence import route_query

def main():
    print("AGI इंटेलिजेंस बोट फ्रेमवर्क में आपका स्वागत है! (Groq AI द्वारा संचालित)")
    print("अपना सवाल लिखें या बाहर निकलने के लिए 'exit' लिखें।")

    # Check if API Key is set
    if not os.getenv("GROQ_API_KEY"):
        print("\nचेतावनी: GROQ_API_KEY सेट नहीं है। कृपया .env फ़ाइल चेक करें।")

    while True:
        try:
            user_input = input("\nबोट > ")
            if user_input.lower() in ['exit', 'quit', 'bye', 'बाहर']:
                print("अलविदा!")
                break

            if not user_input.strip():
                continue

            response = route_query(user_input)
            print(f"\n{response}")

        except KeyboardInterrupt:
            print("\nअलविदा!")
            break
        except Exception as e:
            print(f"एक त्रुटि हुई: {e}")

if __name__ == "__main__":
    main()
