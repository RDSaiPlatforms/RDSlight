from config import client

class SentimentAnalyzer:
    def analyze_sentiment(self, text):
        """
        Uses OpenAI's API to analyze the sentiment of the input text.
        Returns 'positive', 'negative', or 'neutral'.
        """
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that analyzes sentiment."},
                    {"role": "user", "content": f"Analyze the sentiment of the following text: '{text}'. Just return 'positive', 'negative', or 'neutral'. Return exactly one word."}
                ],
                max_tokens=5,
                temperature=0
            )
            sentiment = response.choices[0].message.content.strip().lower()
            return sentiment
        except Exception as e:
            print(f"Error during sentiment analysis: {e}")
            return "neutral"