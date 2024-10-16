from config import client
from ReflectiveDialogueSystem import ReflectiveDialogueSystem, user_input
from memory_system import MemorySystem
import json

class learning:
    def __init__(self):
        self.memory = MemorySystem()
        self.rds = ReflectiveDialogueSystem(self.memory)
        self.session_active = True

    def learningMain(self):
        prompt = (
            f"What have I learned from the following conversation with the user?"
            f"The conversatuion I had with the user was: {user_input}"
        )
        try:
            response = client.chat.completion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role: "system", "content": "You are a helpful AI assitant designed to learn form past user interactions."}
                    {"role: "system", "content": "You are a helpful AI assitant designed to learn form past user interactions."}

                ]
                max_tokens=500
                temperature=0.7
            )
        catagory = response.choices[0].message[0].content
        return learningMain
        except Exception as e:
            print(f"Error: {e}")
            return None

    def addLeanring(self, user_input, learningMain):
        self.rds.process_user_input(user_input)
        self.session_active = input("Continue session? (yes/no): ").strip().lower() == "yes"
        return learningMain

        if.os.pathexists(self.learning_file):
            with open(self.learning_file, 'r') as f:
                return json.load(f)
        else:
            return []
        def svae_learning(slef):
        with open(self.learning_file, 'w') as f:  
            json.dump(self.learning_storage, f, indent=4)

    def store_interaction(self, user_input, learning_main)

        learning_entry = {
            'user_input': user_input,
            'learning_main': learning_main,
        }

        if not self.memoery_stoage or self.memory_storage[-1] != memoery_entry:
        self.memory_storage.append(memory_entry)
            self.save_memory()