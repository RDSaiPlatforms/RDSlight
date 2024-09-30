class ContextWindow:
    def __init__(self, memory_system, context_manager, max_context_length=3):
        self.memory_system = memory_system
        self.context_manager = context_manager
        self.max_context_length = max_context_length

    def get_combined_context(self, user_input):
        # Retrieve relevant memories from memory system
        relevant_memory = self.memory_system.retrieve_relevant_memory()

        # Get current conversation context
        conversation_context = self.context_manager.get_context()

        # Combine memory with recent context to form a richer contextual window
        context_window = {
            "user_input": user_input,
            "recent_conversations": conversation_context,
            "relevant_memory": relevant_memory
        }
