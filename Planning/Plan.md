# Task List for AI Chatbot Project

## Phase 1: Learn and Understand

- [ ] **Understanding the basics of an LLM**
  - Understand what is an LLM, explain this using basic brain anatomy (neuron, dendrites, cortex, etc...) such that a high school student can understand.
  - Explain how prompting works with LLM, how it can give LLM a "personality", explain what is a system prompt vs user message.
  - Explain at a high level the approach of building a LLM chatbot with "personality", list some interesting use cases for this.
  - Research and list examples of popular LLMs (e.g., GPT, Claude, Llama) and their unique features.
  - Create a simple analogy or story to explain how LLMs process information step-by-step.

- [ ] **Understand LangChain and LLMs**
  - Introduce LangChain and the concept of large language models (LLMs). Include resources for understanding how to host and use an LLM locally.
  - Explore how LangChain can be used to chain prompts together for more complex interactions.
  - Provide a simple example of using LangChain to create a chatbot flow.

- [ ] **Understand the purpose of a server and client in a web application**
  - Explain the difference between a server and a client using real-world analogies (e.g., a restaurant kitchen and a waiter).
  - Describe how data flows between the server and client in a web application.
  - Provide examples of common server-side and client-side tasks.

- [ ] **Understand how FastAPI and APIRouting works**
  - Provide resources and examples to understand API routing in FastAPI. Include creating endpoints and handling requests.
  - Create a simple diagram to show how a request flows through FastAPI.
  - Write a basic FastAPI example with one endpoint and explain each part of the code.

## Phase 2: Design

- [ ] **Define chatbot personality and behavior**
  - Outline the desired personality traits and conversational style for the chatbot.
  - Create example dialogues to guide development.
- [ ] **Plan backend architecture**
  - Design the structure of the FastAPI backend, including endpoints and data flow.
  - Decide how the LLM will be integrated and accessed.
- [ ] **Design frontend interface**
  - Sketch wireframes or mockups for the chatbot interface.
  - Plan user interactions and layout for the frontend.
- [ ] **Determine data handling and storage**
  - Decide how user inputs and chatbot responses will be stored, if needed.
  - Plan for any additional data requirements, such as logs or analytics.
- [ ] **Create a project timeline**
  - Break down the implementation phase into smaller milestones.
  - Assign deadlines or goals for each milestone.

## Phase 3: Implementation

- [ ] **Implement FastAPI backend**
  - Create a FastAPI backend with endpoints for chatbot functionality. Include integration with a locally hosted LLM using LangChain.
- [ ] **Develop frontend for chatbot**
  - Build a simple frontend to interact with the chatbot. Include basic HTML, CSS, and JavaScript for the interface.
- [ ] **Integrate frontend with backend**
  - Connect the frontend to the FastAPI backend using API calls. Ensure smooth communication between the two.

## Phase 4: Feature Build-Out

- [ ] **Add personality to chatbot**
  - Customize the chatbot's responses to reflect your son's personality. Include examples and techniques for fine-tuning the LLM.
- [ ] **Test and refine chatbot**
  - Test the chatbot thoroughly and refine its responses. Include debugging tips and iterative improvement strategies.
- [ ] **Explore advanced features**
  - Brainstorm and implement advanced features like memory, context retention, or voice interaction. Include resources for learning these concepts.
- [ ] **Context Storage and Retrieval**
  - Store context as graph, find relevant context data using LLM
