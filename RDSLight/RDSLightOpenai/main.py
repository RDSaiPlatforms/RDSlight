from core.memory_system import MemorySystem
from core.reflective_dialogue_system import ReflectiveDialogueSystem


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
        rds.process_user_input(user_input)

        session_active = input("Continue session? (yes/no): ").strip().lower() == "yes"

if __name__ == "__main__":
    run_system()

