import os
import google.generativeai as genai

# Retrieve the API key from environment variables
api_key = os.environ.get("API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set the API_KEY environment variable.")

# Configure the Google Generative AI client with the API key
genai.configure(api_key=api_key)

# Client interface for making requests
class GeminiClient:
    def create(self, model, messages, max_tokens=1000):
        """
        Sends a chat request to Google Gemini API and retrieves the response.

        Args:
            model (str): The name of the Gemini model to use.
            messages (list): A list of message objects (role: 'system', 'user', etc.).
            max_tokens (int): The maximum number of tokens to generate.

        Returns:
            dict: The response from the API.
        """
        try:
            response = genai.GenerativeModel(model).generate_content(
                prompt=messages[-1]["content"] if messages else ""
                max_tokens=max_tokens
            )
            return {
                'choices': [
                    {'message': {'content': response.text}}
                ]
            }
        except Exception as e:
            print(f"Error in GeminiClient.create: {e}")
            return None

# Instantiate the client
gemini_client = GeminiClient()
