# Content Creation Workflow with CrewAI and OpenAI

This repository implements a content creation workflow using the `CrewAI` framework, which involves multiple agents working together to plan, write, and edit a blog post on a given topic. It uses OpenAI's GPT-3.5-turbo model to drive the agents' tasks. 

## Features
- **Content Planner**: Plans the structure of a blog post based on the topic.
- **Content Writer**: Crafts an engaging and insightful opinion piece based on the planner's work.
- **Editor**: Proofreads and edits the blog post to ensure it aligns with organizational style and best practices.
- **Task-Oriented Workflow**: Each agent is assigned specific tasks to complete, with input from others.

## Requirements

- Python 3.7+
- `crewai` library
- `openai` library
- `IPython` library
- Custom `utils` module for fetching OpenAI API keys

## Installation

To run this project, you need to install the required Python libraries.

```bash
pip install crewai openai ipython

