import os
from groq import Groq

class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            # Fallback for testing or when key is missing
            self.client = None
        else:
            self.client = Groq(api_key=self.api_key)

    def get_response(self, prompt, model="llama3-8b-8192"):
        if not self.client:
            return "Error: GROQ_API_KEY not found in environment. Please check your .env file."

        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=model,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Error connecting to Groq API: {e}"

llm_client = LLMClient()
