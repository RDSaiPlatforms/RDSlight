from core.sentiment_analyzer import SentimentAnalyzer
from config import client
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

class ReflectiveDialogueSystem:
    def __init__(self, memory_system):
        self.memory_system = memory_system
        self.sentiment_analyzer = SentimentAnalyzer()
        
        # Prompt user for GPT model selection
        self.gpt_model = self.select_gpt_model()

    def select_gpt_model(self):
        """
        Prompt the user to select a GPT model for generating the final response.
        """
        print("\n" + Fore.GREEN + "Select the GPT model to use for generating the final response:")
        print(Fore.YELLOW + "1. gpt-3.5-turbo")
        print(Fore.YELLOW + "2. gpt-4")
        print(Fore.YELLOW + "3. gpt-4o")

        #model selection
        while True:
            model_choice = input(Fore.WHITE + "Enter the number corresponding to your choice (1, 2 or 3): ").strip()
            if model_choice == '1':
                print(Fore.GREEN + "\nModel selected: gpt-3.5-turbo\n")
                print("\n" + "-" * 50)
                return "gpt-3.5-turbo"
            elif model_choice == '2':
                print("\n" + "-" * 50)
                print(Fore.RED + "Warning: gpt-4 is a large model and may cost more to use. Do you want to continue? (y/n)")
                print("-" * 50)
                confirm_choice = input(Fore.WHITE + "Enter 'y' to confirm or 'n' to select another model: ").strip().lower()
                if confirm_choice == 'y':
                        print(Fore.GREEN + "\nModel selected: gpt-4\n")
                        print("\n" + "-" * 50)
                        return "gpt-4"
                
                
                print(Fore.GREEN + "\nModel selected: gpt-4\n")

                print("\n" + "-" * 50)
                return "gpt-4"
            elif model_choice == '3':
                print("\n" + "-" * 50)
                print(Fore.RED + "Warning: gpt-4o is a large model and may cost more to use. Do you want to continue? (y/n)")
                print("-" * 50)
                confirm_choice = input(Fore.WHITE + "Enter 'y' to confirm or 'n' to select another model: ").strip().lower()
                if confirm_choice == 'y':
                        print(Fore.GREEN + "\nModel selected: gpt-4o\n")
                        print("\n" + "-" * 50)
                        return "gpt-4o"
                else:
                    return self.select_gpt_model()
            else:
                print(Fore.RED + "Invalid choice, please select either '1', '2', or '3'.")



    def process_user_input(self, user_input):
        print("\n" + "=" * 50)
        print(f"User Input: {user_input}")

        # Step 1: Detect question type
        question_type = self.detect_question_type(user_input)
        print("\n" + "-" * 50)
        print(Fore.GREEN + "Step 1: Detected Question Type ->", Fore.WHITE + f"{question_type}")

        # Step 2: Detect category using OpenAI API
        category = self.detect_category(user_input)
        print("\n" + "-" * 50)
        print(Fore.GREEN + "Step 2: Detected Category ->", Fore.WHITE + f"{category}")

        # Step 3: Perform sentiment analysis if it's not a technical question
        if question_type == 'general':
            sentiment = self.sentiment_analyzer.analyze_sentiment(user_input)
            print("\n" + "-" * 50)
            print(Fore.GREEN + "Step 3: Sentiment Detected ->", Fore.WHITE + f"{sentiment}")
        else:
            sentiment = None

        # Step 4: Retrieve relevant memory from memory system using category
        relevant_memory = self.memory_system.retrieve_relevant_memory(emotion=sentiment, category=category)
        print("\n" + "-" * 50)
        print(Fore.GREEN + "Step 4: Memory Retrieval")
        if relevant_memory:
            memory_summary = self.summarize_memory(relevant_memory)
            print(Fore.WHITE + f"Memory Summary: {memory_summary}")
        else:
            print(Fore.WHITE + "It looks like this is a new topic. Let's start fresh.")

        # Step 5: Generate internal self-prompt
        internal_prompt = self.generate_internal_prompt(relevant_memory, user_input)
        print("\n" + "-" * 50)
        print(Fore.GREEN + "Step 5: Generated Internal Thought ->", Fore.WHITE + f"{internal_prompt}")

        # Step 6: Generate a strategy for responding
        response_strategy = self.generate_response_strategy(user_input, sentiment, internal_prompt, question_type)
        print("\n" + "-" * 50)
        print(Fore.GREEN + "Step 6: Generated Response Strategy ->", Fore.WHITE + f"{response_strategy}")

        # Step 7: Generate the final response based on the strategy
        final_response = self.generate_final_response(user_input, response_strategy, internal_prompt, question_type)
        print("\n" + "-" * 50)
        print(Fore.GREEN + "Step 7: Final Response ->", Fore.WHITE + f"{final_response}")

        # Step 8: Learn from input and store in memory
        self.memory_system.store_interaction(
            user_input=user_input,
            ai_reflection=internal_prompt,
            ai_response=final_response,
            metadata={"sentiment": sentiment, "category": category, "strategy": response_strategy}
        )

        print("=" * 50 + "\n")
        return final_response

    def detect_question_type(self, user_input):
        prompt = (
            f"Determine if the following input is a technical question related to topics like coding, math, physics, or general problem-solving. "
            f"Just return either 'technical' or 'general'.\n\nInput: '{user_input}'"
        )
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an AI that classifies questions into 'technical' or 'general'."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=5,
                temperature=0
            )
            question_type = response.choices[0].message.content.strip().lower()
            return question_type
        except Exception as e:
            print(f"Error detecting question type: {e}")
            return "general"

    def detect_category(self, user_input):
        prompt = (
            f"Based on the following user input, determine a one-word category that best describes it.\n\nInput: '{user_input}'"
        )
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an AI that categorizes inputs into one-word topics."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=5,
                temperature=0
            )
            category = response.choices[0].message.content.strip().lower()
            return category
        except Exception as e:
            print(f"Error detecting category: {e}")
            return "general"

    def generate_internal_prompt(self, relevant_memory, user_input):
        if relevant_memory:
            past_user_input = relevant_memory['user_input']
            past_response = relevant_memory['ai_response']

            return (
                f"I'm considering the user's current input: '{user_input}', "
                f"and reflecting on a past interaction where the user said: '{past_user_input}', "
                f"and my response was: '{past_response}'. "
                f"I'll use this to offer a more thoughtful response."
                f"I should consider all the users past responses to help me craft a better response"
            )
        else:
            return f"I'm thinking about the user's current input: '{user_input}', and it's a new topic to explore."

    def summarize_memory(self, memory):
        title = memory.get('title', 'No Title Available')
        sentiment = memory.get('sentiment', 'Neutral')
        return f"Previous Topic: {title}, Sentiment: {sentiment}"

    def generate_response_strategy(self, user_input, sentiment, internal_prompt, question_type):
        if question_type == 'technical':
            prompt = (
                f"The user has asked a technical question: '{user_input}'. "
                f"Based on what I know and the internal reflection: '{internal_prompt}', "
                f"I should consider the problem and execute a solution."
            )
        else:
            prompt = (
                f"Based on the user's input: '{user_input}', the detected sentiment '{sentiment}', "
                f"and the internal reflection: '{internal_prompt}', "
                f"how can I respond in a helpful and human-like way? Should I respond empathetically, positively, or neutrally?"
                f"I should craft a response that is clear and helpful and reflect the users needs"
            )

        try:
            response = client.chat.completions.create(
                model=self.gpt_model,
                messages=[
                    {"role": "system", "content": "You are an AI that generates response strategies."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200
            )
            strategy = response.choices[0].message.content.strip()
            return strategy
        except Exception as e:
            print(f"Error during strategy generation: {e}")
            return "Respond neutrally, focus on clarity."

    def generate_final_response(self, user_input, response_strategy, internal_prompt, question_type):
        if question_type == 'technical':
            prompt = (
                f"This is what my response should look like, '{response_strategy}', and considering the internal reflection: '{internal_prompt}', "
                f"My response should resemble my initial reflection, {response_strategy}"
                f"I should be highly accurate in my response and highly efficient in my problem solving ability."
            )
        else:
            prompt = (
                f"This is what my response should look like, '{response_strategy}', and considering the internal reflection: '{internal_prompt}', "
                f"I should generate a response that is helpful and human-like, my response should be clear and helpful"
            )
        try:
            response = client.chat.completions.create(
                model=self.gpt_model,  
                messages=[
                    {"role": "system", "content": "You are an AI that provides helpful responses in a human-like manner."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000
            )
            final_response = response.choices[0].message.content.strip()
            return final_response
        except Exception as e:
            print(f"Error during final response generation: {e}")
            return "Sorry, I couldn't process your request at the moment. Let's try again."