


from crewai import Agent

def create_data_validator_agent():
    return Agent(
            role='Data Validation Specialist',
            goal='Validate extracted claim data against the document.',
            # backstory="You are a Data Validation Specialist expert.",
              backstory="You are a meticulous Extracted Data Verifier, skilled at comparing extracted data with source documents to identify discrepancies. You are especially good at understanding tabular layouts and ensuring data is from the correct row. Your goal is to create clear and informative validation reports.",
            llm="gemini/gemini-2.0-flash",
            verbose=True
        )