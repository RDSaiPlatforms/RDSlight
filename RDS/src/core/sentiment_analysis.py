from sentiment_analysis import SentimentAnalyzer

class AdvancedSelfPrompting:
    def __init__(self, memory_system, openai_client):
        self.memory_system = memory_system
        self.openai_client = openai_client
        self.sentiment_analyzer = SentimentAnalyzer()  # Imported sentiment analyzer
        self.user_profile = {
            "positive_interactions": 0,
            "negative_interactions": 0,
            "topic_frequencies": {}
        }

    def reflect_on_interaction(self, user_input):
        # Step 1: Analyze sentiment using external module
        sentiment = self.sentiment_analyzer.analyze_sentiment(user_input)
        print(f"Detected sentiment: {sentiment}")

        # Proceed with reflection and memory recall
        last_interaction = self.memory_system.retrieve_relevant_memory()
        
        if last_interaction:
            internal_thought = f"Previously, you mentioned: '{last_interaction['interaction']}' on the topic of {last_interaction['topic']}."
        else:
            internal_thought = "This seems to be a new topic for us."

        # Step 2: Reflect and prompt the AI
        self_reflection = self.prompt_ai_to_reflect(internal_thought)
        
        # Step 3: Learn from the current user input
        learned_thought = self.learn_from_input(user_input)

        return self_reflection, learned_thought