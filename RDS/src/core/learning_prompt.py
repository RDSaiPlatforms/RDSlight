class LearningPrompt:
    def __init__(self, memory_system):
        self.memory_system = memory_system

    def generate_learning_prompt(self, user_input, reflection):
        # Generate a learning prompt based on user input and AI's reflection
        prompt = f"What did I learn from this interaction? User said: '{user_input}'. AI reflected: '{reflection}'."
        return prompt

    def store_learning(self, user_input, reflection, memory):
        learning_prompt = self.generate_learning_prompt(user_input, reflection)
        # Store the learning as a new memory entry
        self.memory_system.store_interaction(user_input, reflection, memory)

