# **API Reference**

## **Overview**

The Reflective Dialogue System (RDS) is a modular AI framework designed to integrate with any pre-trained language model API (LLM). This system adds reflective thought, memory storage, emotion analysis, and context management to the LLM, enabling more dynamic and human-like conversations.

Developers can easily plug the RDS into an LLM API of their choice, such as OpenAI's GPT models, to create an AI that evolves over time, recalls past interactions, and adapts its behavior based on reflective analysis.

---

## **Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
  - [Initialization](#initialization)
- [Core Components](#core-components)
    - [Memory System](#memory-system)
    - [Thought Processor](#thought-processor)
    - [Context Manager](#context-manager)

---

## **Installation**

To get started, clone the repository and install the necessary dependencies.

### **Prerequisites**

Ensure you have `Python 3.7+` installed on your machine.

### **Install Dependencies**

After cloning the repository, install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

# Usage

## Initialization

To start using the Reflective Dialogue System (RDS), you need to initialize key components such as the MemorySystem, ContextManager, and ThoughtProcessor.

Each component can be customized, and the LLM API (e.g., OpenAI’s GPT-3/4) should be plugged into the ThoughtProcessor.

```python
from rds.memory_system import MemorySystem
from rds.thought_processor import ThoughtProcessor
from rds.context_manager import ContextManager
from rds.api_client import OpenAIClient  # Example for OpenAI

# Initialize key components
memory_system = MemorySystem()
context_manager = ContextManager()
openai_client = OpenAIClient(api_key="your-openai-api-key")

# Initialize ThoughtProcessor with memory and context systems
thought_processor = ThoughtProcessor(memory_system, openai_client, context_manager)
```

# Core Components

## Memory System
The `MemorySystem` stores, retrieves, and manages memories associated with user interactions. Memories are tagged with metadata (such as emotion, topic, and sentiment analysis).

**Method:** `store_interaction(user_input, ai_reflection, ai_response, metadata)`
**Description:** Stores user interactions, AI responses, and reflection into memory, along with emotion and topic metadata.
**Method:** `retrieve_relevant_memory(emotion=None, topic=None)`
**Description:** Retrieves past memories based on the provided emotion or topic.

```python
# Store a memory
memory_system.store_interaction(
    user_input="I’m worried about the math section.",
    ai_reflection="Reflecting on user's concern about math.",
    ai_response="Would you like to go over some math problems?",
    metadata={"emotion": "negative", "topic": "math"}
)

# Retrieve a memory
relevant_memory = memory_system.retrieve_relevant_memory(emotion="negative")
print(relevant_memory)
```

## Thought Processor
The `ThoughtProcessor` is responsible for simulating reflective thought by prompting the AI model (e.g., GPT) to reflect on past interactions and adapt its response.

**Method:** `process_thought(user_input, context)`
**Description:** Takes user input, retrieves relevant memory, prompts the AI to reflect, and generates an adaptive response.

```python
response = thought_processor.process_thought("I feel anxious about tomorrow's exam.")
print(response)
```

## Context Manager
The ContextManager keeps track of the recent conversation context (short-term memory) and integrates it with the ThoughtProcessor for continuity in conversations.
**Method:** `update_context(new_entry)`
**Description:** Adds the latest interaction to the context window.

**Method:** get_context()
**Description:** Retrieves the current context window.

```python
# Update context with new entry
context_manager.update_context("User: I am ready for the exam.")

# Retrieve context
current_context = context_manager.get_context()
print(current_context)
```


