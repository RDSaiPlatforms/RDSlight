import json
import os

class MemorySystem:
    def __init__(self, memory_file="memory.json"):
        self.memory_file = memory_file
        self.memory_storage = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        else:
            return []

    def save_memory(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory_storage, f, indent=4)

    def store_interaction(self, user_input, ai_reflection, ai_response, metadata):
        """
        Store each interaction including the user's input, the AI's reflection, 
        final response, and any additional metadata like sentiment or topic.
        """
        memory_entry = {
            'user_input': user_input,
            'ai_reflection': ai_reflection,
            'ai_response': ai_response,
            'metadata': metadata 
        }
        self.memory_storage.append(memory_entry)
        self.save_memory()

    def retrieve_relevant_memory(self, emotion=None, topic=None):
        """
        Retrieve the most relevant memory based on emotion or topic.
        Memory is stored as a list and retrieved in reverse order (most recent first).
        """
        for memory in reversed(self.memory_storage):
            if emotion and memory['metadata'].get('emotion') == emotion:
                return memory
            if topic and memory['metadata'].get('topic') == topic:
                return memory
        return None

    def retrieve_latest_memory(self):
        """
        Retrieve the latest memory if no specific emotion or topic is needed.
        """
        if self.memory_storage:
            return self.memory_storage[-1]  
        return None