# Multi-Agent Customer Support Automation with CrewAI

## Overview
This project demonstrates the use of **CrewAI** to automate customer support interactions using multi-agent cooperation. The example focuses on handling customer inquiries with a structured workflow, ensuring high-quality responses through an **AI-powered support team**.

In this lesson, we explore **six key elements** that enhance AI Agents' performance:
1. **Role Playing** – Assigning well-defined roles to agents.
2. **Focus** – Ensuring each agent has a clear objective.
3. **Tools** – Enhancing agent capabilities with external tools.
4. **Cooperation** – Structuring task delegation and collaboration.
5. **Guardrails** – Setting constraints for agent behavior.
6. **Memory** – Enabling agents to recall context across interactions.

---

## Features
- **Automated Support Handling**: A support agent answers customer inquiries with accuracy.
- **Quality Assurance Review**: A second agent ensures the response meets high-quality standards.
- **Web Scraping for Documentation**: Agents use external resources for reference.
- **Multi-Agent Collaboration**: Ensures thorough and well-researched responses.
- **Memory Persistence**: Enhances follow-up interactions with context retention.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/multi-agent-support-automation.git
   cd multi-agent-support-automation
   ```
2. Install dependencies:
   ```bash
   pip install crewai crewai_tools langchain_groq ipython
   ```
3. Set up API keys (Replace with your actual credentials):
   ```python
   GROQ_API_KEY = "your_groq_api_key"
   ```

---

## Agents & Tasks

### 1. **Senior Support Representative**
- **Goal**: Provide friendly and complete support to customers.
- **Responsibilities**:
  - Process customer inquiries.
  - Use available tools and references.
  - Ensure responses are comprehensive and helpful.

### 2. **Support Quality Assurance Specialist**
- **Goal**: Maintain high standards in support responses.
- **Responsibilities**:
  - Review responses for accuracy and completeness.
  - Ensure responses follow company guidelines.
  - Provide improvements where necessary.

### 3. **Tasks**
- **Inquiry Resolution**: The support representative formulates a detailed response.
- **Quality Assurance Review**: The response is reviewed before finalizing it for the customer.

---

## Usage

1. Define your inputs:
   ```python
   inputs = {
       "customer": "DeepLearningAI",
       "person": "Rahul Nanavaty",
       "inquiry": "I need help with setting up a Crew and kicking it off, specifically how can I add memory to my crew? Can you provide guidance?"
   }
   ```
2. Run the script:
   ```python
   result = crew.kickoff(inputs=inputs)
   ```
3. View the response:
   ```python
   from IPython.display import Markdown
   Markdown(result)
   ```

---

## Key Takeaways
- **Role-playing** helps structure AI behavior.
- **Task specialization** improves efficiency.
- **Memory and context-awareness** enhance user experience.
- **Quality assurance mechanisms** ensure response reliability.

This project serves as a **learning resource** for **CrewAI-based multi-agent collaboration** in customer support automation.

---

## Contributing
Feel free to submit issues or pull requests for improvements.

---

## License
This project is licensed under the MIT License.


