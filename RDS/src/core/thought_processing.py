class ThoughtProcessor:
    def __init__(self, memory_system, openai_client):
        self.memory_system = memory_system 
        self.openai_client = openai_client  

    def process_thought(self, user_input):
        # Step 1: Retrieve relevant memories
        relevant_memory = self.memory_system.retrieve_relevant_memory()

        # Step 2: Prompt the AI for internal reflection on this memory
        if relevant_memory:
            internal_thought = f"Previously, the user said: '{relevant_memory['interaction']}', which had a tone of {relevant_memory['emotion']}."
        else:
            internal_thought = "I don't recall any past conversations about this topic."

        # Reflect on internal thought using LLM(OpenAI in htis case) API
        reflection = self.self_reflect(internal_thought)

        # Step 3: Generate a final thought based on user input and reflection
        final_thought = self.generate_final_thought(user_input, reflection, relevant_memory)

        return final_thought

    def self_reflect(self, internal_thought):
        # OpenAI is called to simulate AI reflection on past memory
        prompt = f"As an AI, reflect on this: '{internal_thought}'. What should I consider before responding to the user?"
        response = self.openai_client.get_completion(prompt, max_tokens=150)
        return response

    def generate_final_thought(self, user_input, reflection, relevant_memory):
        # Generate a comprehensive thought combining the reflection and user input

        if relevant_memory:
            final_thought = (
                f"{reflection} Considering you previously mentioned '{relevant_memory['interaction']}' "
                f"which had a tone of {relevant_memory['emotion']}, how can we apply this now? "
                f"In response to your current input: '{user_input}', here's what I've learned."
            )
        else:
            final_thought = (
                f"{reflection} Since this is a new topic for us based on '{user_input}', "
                f"I'm considering how this fits into our broader conversations."
            )

        return final_thought
