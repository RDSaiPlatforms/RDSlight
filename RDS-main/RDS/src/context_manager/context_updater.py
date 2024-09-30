class ContextManager:
    def __init__(self, window_size=5):
        self.context_window = []
        self.window_size = window_size  

    def update_context(self, new_entry):
        # Add the new entry to the context window
        self.context_window.append(new_entry)

        # If the window exceeds the size, remove the oldest entry
        if len(self.context_window) > self.window_size:
            self.context_window.pop(0)

    def get_context(self):
        # Return the current context window
        return self.context_window

    def clear_context(self):
        # Clear the context window
        self.context_window = []
