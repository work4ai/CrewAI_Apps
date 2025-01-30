import warnings
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
from IPython.display import Markdown

# Suppress warnings
warnings.filterwarnings('ignore')

# Groq API Key (Replace with your actual API key)
GROQ_API_KEY = "GROQ_API_KEY"    #Your GROQ API KEY

# Initialize LLM
llm = ChatGroq(
    model_name="llama3-70b-8192",
    groq_api_key=GROQ_API_KEY,
    verbose=True
)

# Event Planner Agent
event_planner = Agent(
    llm=llm,
    role="Event Planner",
    goal="Plan an event based on input: event type, number of people, and budget.",
    backstory="You are an expert event planner who selects the best venue and budget allocation.",
    allow_delegation=False,
    verbose=True
)

# Logistics Agent
logistics_manager = Agent(
    llm=llm,
    role="Logistics Manager",
    goal="Arrange all logistical requirements based on the event details.",
    backstory="You handle venue setup, catering, seating, and transportation.",
    allow_delegation=False,
    verbose=True
)

# Marketing Agent
marketing_expert = Agent(
    llm=llm,
    role="Marketing Expert",
    goal="Create marketing content for the event.",
    backstory="You are a creative marketer responsible for promotional content and branding.",
    allow_delegation=False,
    verbose=True
)

# Event Planning Task
event_planning = Task(
    description="Plan an event considering type: {event_type}, people: {num_people}, budget: {budget}.",
    expected_output="Provide event details including venue, estimated budget allocation, and key features.",
    agent=event_planner,
)

# Function to Get Human Feedback
def get_human_approval(event_details):
    print("\n💡 Event Plan Created: ")
    print(event_details)
    approval = input("\nDo you approve the event plan? (yes/no): ").strip().lower()
    return approval == "yes"

# Run Event Planner Task
crew = Crew(
    agents=[event_planner],
    tasks=[event_planning],
    verbose=1
)

inputs = {
    "event_type": "Corporate Seminar",
    "num_people": "150",
    "budget": "5000 USD"
}

event_plan = crew.kickoff(inputs=inputs)

# Get Human Approval
if get_human_approval(event_plan):
    print("\n✅ Event Approved! Proceeding with Logistics & Marketing...\n")

    # Logistics Task
    logistics_task = Task(
        description="Handle logistics for the event at {event_venue} with budget {budget}.",
        expected_output="Provide logistics details including venue setup, catering, transportation, and seating.",
        agent=logistics_manager,
    )

    # Marketing Task
    marketing_task = Task(
        description="Create a marketing campaign for the event titled {event_type}.",
        expected_output="A promotional strategy including social media posts, email campaigns, and branding.",
        agent=marketing_expert,
    )

    # Parallel Execution of Logistics & Marketing
    crew_parallel = Crew(
        agents=[logistics_manager, marketing_expert],
        tasks=[logistics_task, marketing_task],
        verbose=1
    )

    event_logistics, event_marketing = crew_parallel.kickoff(inputs={"event_venue": event_plan, "budget": inputs["budget"]})

    print("\n📦 Logistics Plan:\n", event_logistics)
    print("\n📢 Marketing Strategy:\n", event_marketing)

else:
    print("\n❌ Event Plan Rejected! Suggesting an alternative venue...\n")
