import sys
from core.intelligence import route_query

def main():
    print("Welcome to the AGI Intelligence Bot Framework!")
    print("Type your query or 'exit' to quit.")

    while True:
        try:
            user_input = input("\nBot > ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("Goodbye!")
                break

            if not user_input.strip():
                continue

            response = route_query(user_input)
            print(response)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
