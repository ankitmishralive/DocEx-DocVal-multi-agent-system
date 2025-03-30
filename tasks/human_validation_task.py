


# tasks/human_validation_task.py
from crewai import Task
from agents.human_validator import create_human_validation_agent
from prompts.human_validation_prompt import human_validation_format_instructions
from models.human_validation import HumanValidationsList

def create_human_validation_task():
    description = f"""Read the output of validation_report.txt and generate a JSON output 
    that summarizes the validation results in a structured format for human review.

    Return **only** a valid JSON object, without any markdown, triple backticks, or additional text.
    Ensure that the output is a valid JSON object conforming to the schema.
    {human_validation_format_instructions}
    
    Validation report:validation_report.txt
    """
    return Task(
        description=description,
        expected_output="A valid JSON object (without markdown formatting).",
        output_file="human_validations.json",
        agent=create_human_validation_agent(),
        output_json=HumanValidationsList
    )
