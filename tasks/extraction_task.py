

# tasks/extraction_task.py
from crewai import Task
from prompts.extraction_prompt import format_instructions,extraction_system_template
from agents.data_extractor import create_data_extractor_agent

from models.claim_details import ClaimsList


def create_extraction_task(pdf_chunks):
    return Task(
        description=f"""Extract all claim details accurately from the provided document content and generate a valid JSON output. 
        
        - Ensure extracted data aligns with the correct column headers and rows.
        - Validate that values are mapped correctly based on their respective rows.
        - Strictly return **only** a valid JSON object without markdown, triple backticks, or extra formatting.
        - The output **must** conform to the defined schema for claim extraction.
        
        Document content:
        {pdf_chunks}
        
        {extraction_system_template}
        """,

        agent=create_data_extractor_agent(),
        expected_output="A valid JSON object (without markdown formatting).",
        output_json=ClaimsList,
        # output_file='extractions.json',
    )

