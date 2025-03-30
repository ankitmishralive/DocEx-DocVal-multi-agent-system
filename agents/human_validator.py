


# agents/human_validation_agent.py
from crewai import Agent
# from llm import create_human_validation_llm



def create_human_validation_agent():
    return Agent(
            role='Human Validation Report Generator',
            goal='Read the validation_report.txt and extracted_claims.json, and generate a structured JSON output for human review.',
            backstory="You are an expert in processing validation reports and structuring data for human review.",
          llm="gemini/gemini-2.0-flash",
            verbose=True
        )
