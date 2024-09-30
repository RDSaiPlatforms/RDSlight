class EmotionResponse:
    def __init__(self, sentiment_analysis, memory_query):
        self.sentiment_analysis = sentiment_analysis
        self.memory_query = memory_query

    def generate_response(self, user_input):
        sentiment = self.sentiment_analysis.analyze(user_input)
        relevant_memory = self.memory_query.query_memory(emotion_filter=sentiment)

        if sentiment == "positive":
            response = "I'm glad to hear that! "
        elif sentiment == "negative":
            response = "I'm sorry you're feeling that way. "
        else:
            response = "Thank you for sharing that. "

        if relevant_memory:
            response += f"I remember you once mentioned: '{relevant_memory['interaction']}'."
        
        return response

