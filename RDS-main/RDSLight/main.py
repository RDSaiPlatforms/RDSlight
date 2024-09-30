from core.memory_system import MemorySystem
from core.reflective_dialogue_system import ReflectiveDialogueSystem
import time
import threading

def loading_animation(stop_event):
    """
    Displays a loading animation with repeating dots until stop_event is set.
    """
    while not stop_event.is_set():
        for _ in range(3):
            if stop_event.is_set():
                break
            print(".", end="", flush=True)
            time.sleep(0.5)
        if not stop_event.is_set():
            print("\b\b\b   \b\b\b", end="", flush=True) 

def run_system():
    """
    Initializes the reflective dialogue system and runs the internal feedback loop.
    """
    print("\n" + "-" * 50)
    print("Starting RDSV1.0L", end="")


    stop_event = threading.Event()
    loading_thread = threading.Thread(target=loading_animation, args=(stop_event,))
    loading_thread.start()

    time.sleep(5) 

    stop_event.set()
    loading_thread.join()

    print(" Ready!") 
    print("\n" + "-" * 50)

    memory = MemorySystem()
    rds = ReflectiveDialogueSystem(memory)

    # Activate the session loop
    session_active = True
    while session_active:
        user_input = input("Enter a prompt: ")
        rds.process_user_input(user_input)

        # Prompt to continue or end the session
        session_active = input("Continue session? (yes/no): ").strip().lower() == "yes"

if __name__ == "__main__":
    run_system()