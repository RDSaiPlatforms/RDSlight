import json
import os

class MemorySystem:
    def __init__(self, memory_file="memory.json"):
        self.memory_file = memory_file
        self.memory_storage = self.load_memory()

    def load_memory(self):
        """
        Load memory from the memory file if it exists.
        """
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        else:
            return []

    def save_memory(self):

        """
        Save the current state of memory to the memory file.
        """

        with open(self.memory_file, 'w') as f:
            json.dump(self.memory_storage, f, indent=4)

    def store_interaction(self, user_input, ai_reflection, ai_response, metadata):

        """
        Store a new interaction in memory, ensuring no duplicate entries.
        """

        memory_entry = {
            'user_input': user_input,
            'ai_reflection': ai_reflection,
            'ai_response': ai_response,
            'metadata': {
                'sentiment': metadata.get('sentiment'),
                'category': metadata.get('category'),
                'strategy': metadata.get('strategy')
            }
        }

        if not self.memory_storage or self.memory_storage[-1] != memory_entry:
            self.memory_storage.append(memory_entry)
            self.save_memory()

    def retrieve_relevant_memory(self, emotion=None, category=None):
        """
        Retrieve the most relevant memory based on emotion or category.
        It searches in reverse order (most recent first).
        """
        for memory in reversed(self.memory_storage):
            emotion_match = (emotion and memory['metadata'].get('sentiment') == emotion)
            category_match = (category and memory['metadata'].get('category') == category)

            if emotion_match or category_match:
                return memory
        return None