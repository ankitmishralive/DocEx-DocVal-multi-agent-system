

from crewai import Agent


def create_data_extractor_agent():
    return Agent(
        role='Data Extraction Specialist',
        goal='Extract claim data from documents and return a JSON object, paying careful attention to layout.',
        backstory="You are an expert data extraction specialist with a knack for accurately pulling information from complex documents. You pay close attention to detail, the layout of the document, and are skilled at identifying key data points.",
        # llm=create_extraction_llm(),
        llm="gemini/gemini-2.0-flash",
        verbose=True
    )

