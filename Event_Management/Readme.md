## **📌 README: Multi-Agent Event Planning with CrewAI & Groq**  

### **🚀 Overview**  
This Python program demonstrates **multi-agent collaboration** using **CrewAI** and **Groq** to plan, organize, and market an event efficiently. The system consists of **three AI agents**, each responsible for a different aspect of event management:  

1. **Event Planner Agent** → Plans the event based on input (event type, number of attendees, budget).  
2. **Logistics Manager Agent** → Determines the logistics requirements (venue, catering, seating, etc.).  
3. **Marketing Specialist Agent** → Creates promotional content for the event.  

👉 **Parallel Execution**: The **Logistics Manager** and **Marketing Specialist** agents run **in parallel** after the event is planned.  

👉 **Human-in-the-Loop**: Before proceeding, a human user confirms the venue and budget. If rejected, the **Event Planner** suggests alternatives.  

---

### **🛠️ Tech Stack**  
- **CrewAI** → Multi-agent framework for AI-driven task execution.  
- **Groq (Llama 3-70B)** → Large Language Model (LLM) for intelligent decision-making.  
- **Python** → Core programming language.  
- **LiteLLM** → Integrates Groq with CrewAI.  
- **Parallel Task Execution** → Logistics & Marketing agents work simultaneously.  

---

### **📌 Installation**  

```bash
# 1️⃣ Install required dependencies  
pip install crewai litellm langchain_groq  

# 2️⃣ Set up environment variables (for Groq API Key)  
export GROQ_API_KEY="your-groq-api-key"

# 3️⃣ Run the program  
python event_planner.py
```

---

### **⚙️ Program Workflow**  

#### **Step 1: Event Planning (Agent 1 - Event Planner)**  
- Takes **event type, number of attendees, and budget** as input.  
- Suggests **venue, estimated cost, and basic event details**.  
- **Requires human approval** before proceeding.  

#### **Step 2: Logistics & Marketing (Agents 2 & 3 - Parallel Execution)**  
✅ **Logistics Manager** → Determines **venue setup, seating, food, and other requirements**.  
✅ **Marketing Specialist** → Generates **event promotion content** (social media, email campaigns, etc.).  

#### **Step 3: Finalizing the Event**  
- If the human feedback is **positive**, the logistics and marketing execution proceeds.  
- If **negative**, the **Event Planner suggests a new venue/budget**, and the process restarts.  

---

### **📜 Example Input & Execution**  

#### **User Input**  
```python
inputs = {
    "event_type": "Tech Conference",
    "num_attendees": 500,
    "budget": 20000
}
```

#### **AI-Generated Output**  
```
📅 Event Planned: Tech Conference  
🏢 Suggested Venue: Grand Hall, XYZ Convention Center  
💰 Estimated Cost: $18,500  

👤 Human Approval Needed...
✅ Approved! Proceeding with logistics & marketing.

📦 Logistics:
✔️ Venue booked
✔️ Catering arranged
✔️ Seating & AV setup completed

📢 Marketing:
✔️ Social media post drafted
✔️ Email campaign content created
✔️ Press release finalized

🎉 Event Successfully Planned & Marketed!
```

---

### **🔗 Future Enhancements**  
- 🧠 **More AI Agents** → Adding Finance, Sponsorship, or Ticketing agents.  
- 🔄 **Dynamic Budget Adjustments** → Auto-adjust logistics based on real-time approval.  
- 🎯 **AI-driven Personalization** → Customizing event promotions for different audiences.  

---

### **📌 Contributing**  
Want to enhance this multi-agent system? Feel free to fork the repository and submit a **Pull Request (PR)**! 🚀  

---

### **📧 Contact**  
For any questions or improvements, reach out via **GitHub Issues**. 🚀
