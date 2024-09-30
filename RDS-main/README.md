# Reflective Dialogue System (RDS)

## **Overview of RDS**

The **Reflective Dialogue System (RDS)** is a modular AI architecture designed to work with pre-trained Large Language Models (LLMs), like GPT-3 or GPT-4, to simulate human-like reflective thought, memory, and contextual adaptation. The RDS enhances traditional LLMs by introducing a dynamic system that allows AI to reflect on previous interactions, learn over time, and respond based on memory and emotional cues, creating more natural and engaging conversations.

This system aims to bridge the gap between static, isolated responses and dynamic, evolving dialogue that better simulates human conversation.
Currently this system is still in development


## **Overview of RDS Light**

# RDS Light

RDS Light is a simplified version of the Reflective Dialogue System (RDS), designed for lightweight use while retaining core functionalities such as sentiment analysis, memory retrieval, and thoughtful response generation. This system uses OpenAI's GPT-3.5-turbo model to generate responses and analyze sentiment based on user input.
<img width="2992" alt="RDS" src="https://github.com/user-attachments/assets/041f220b-3e07-44c9-927c-282eb70176a1">


## Features
- **Sentiment Analysis**: Determines if the user's input has a positive, negative, or neutral sentiment.
- **Memory System**: Stores and retrieves relevant memories based on user input and previous interactions.
- **Reflective Dialogue**: Generates internal thoughts based on retrieved memory and sentiment.
- **Adaptive Response**: The system reflects on its strategy and provides a thoughtful response tailored to the user's mood and input.

## How It Works
1. **User Input**: The user provides a prompt.
2. **Sentiment Analysis**: RDS Light analyzes the sentiment of the input (positive, negative, or neutral).
3. **Memory Retrieval**: The system searches for relevant past memories based on the sentiment or topic.
4. **Internal Reflection**: RDS Light generates an internal prompt based on the memory and user input.
5. **Response Strategy**: The AI generates a strategy to determine how to respond (empathetically, positively, or neutrally).
6. **Final Response**: Based on the response strategy, RDS Light generates a final response to the user.
7. **Memory Update**: The system stores the interaction for future retrieval.

## Comparison to GPT-4
<img width="2208" alt="comp" src="https://github.com/user-attachments/assets/43ab2e4b-d29d-4a81-b317-03e5373a46f4">
In comparing a modified GPT-4 vs unmodified GPT-4, we can see that GPT-4 with RDS significantly outperforms the unmodified version in empathy and context awareness. GPT with RDS falls behind on task-based prompts, but this can be easily fixed with a higher max token limit. Overall, adding RDS to GPT-4 significantly improves contextual awareness and emotional intelligence.



## Getting Started

### Prerequisites
- Python 3.6+
- OpenAI API Key (stored in an environment variable)


---

## **Key Features**

- **Memory System**: Stores and retrieves past interactions based on emotion, topics, and context, allowing the AI to recall and use previous memories in future conversations.
- **Reflective Thought Processor**: The AI self-prompts and reflects on previous interactions before generating responses, simulating the way humans think and recall past conversations.
- **Context Manager**: Tracks the conversation's immediate context to maintain coherent, continuous dialogue across multiple exchanges.
- **Sentiment and Emotion Analyzer**: Detects emotional tone and adjusts the AI’s response accordingly, allowing for more empathetic interactions.
- **Modular Design**: Easily integrates with any LLM API, making it simple to scale, customize, and deploy.

---

## **Getting Started**

To get started with the Reflective Dialogue System, follow the steps below to install and run the system.

### **Prerequisites**

Make sure you have the following installed:
- **Python 3.7+**
- API Key from an LLM provider (e.g., OpenAI)
