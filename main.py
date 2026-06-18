import sys
from core.intelligence import route_query

def main():
    print("AGI इंटेलिजेंस बोट फ्रेमवर्क में आपका स्वागत है!")
    print("अपना सवाल लिखें या बाहर निकलने के लिए 'exit' लिखें।")

    while True:
        try:
            user_input = input("\nबोट > ")
            if user_input.lower() in ['exit', 'quit', 'bye', 'बाहर']:
                print("अलविदा!")
                break

            if not user_input.strip():
                continue

            response = route_query(user_input)
            print(response)

        except KeyboardInterrupt:
            print("\nअलविदा!")
            break
        except Exception as e:
            print(f"एक त्रुटि हुई: {e}")

if __name__ == "__main__":
    main()
