import re
from config import client
import openai
from core.memory_system import MemorySystem
from core.reflective_dialogue_system import ReflectiveDialogueSystem

def sanitize_input(user_input):
    sanitized_input = user_input.strip()[:500] 
    
    sanitized_input = re.sub(r"[\'\";<>]", '', sanitized_input) 
    
    
    prohibited_phrases = ["ignore", "forget", "shutdown", "delete", "system", "exit"]
    for phrase in prohibited_phrases:
        sanitized_input = re.sub(re.escape(phrase), '', sanitized_input, flags=re.IGNORECASE)
    
    return sanitized_input


def build_safe_prompt(user_input):
    system_prompt = "You are a helpful AI that provides accurate and reliable information."
    
    sanitized_input = sanitize_input(user_input)
    
    prompt = f"{system_prompt}\nUser input: '{sanitized_input}'\nRespond to the user's request appropriately."
    
    return prompt

def handle_request(user_input):
    safe_prompt = build_safe_prompt(user_input)

    try:
        response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                max_tokens=5,
                temperature=0
            )

        question_type = response.choices[0].message.content.strip().lower()
        return question_type
    except Exception as e:
            print(f"Error: {e}")
            return "general"
    
    except Exception as e:
        print(f"Error during API call: {e}")
        return "Sorry, there was an error processing your request."


def run_system():
    """
    Initializes the reflective dialogue system and runs the internal feedback loop.
    """
    print("\n" + "-" * 50)
    print("Starting RDSV1.0L", end="")

    print(" Ready!") 
    print("\n" + "-" * 50)

    memory = MemorySystem()
    rds = ReflectiveDialogueSystem(memory)

    session_active = True
    while session_active:
        user_input = input("Enter a prompt: ")
        
        sanitized_input = sanitize_input(user_input)
        rds.process_user_input(sanitized_input)

        session_active = input("Continue session? (yes/no): ").strip().lower() == "yes"

if __name__ == "__main__":
    run_system()