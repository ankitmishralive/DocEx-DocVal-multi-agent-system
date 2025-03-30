

# prompts/human_validation_prompt.py
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain.output_parsers import PydanticOutputParser
from models.human_validation import HumanValidationsList

human_validation_parser = PydanticOutputParser(pydantic_object=HumanValidationsList)
human_validation_format_instructions = human_validation_parser.get_format_instructions()

human_validation_system_template = """
You are an expert in processing validation reports and structuring data for human review.
Your task is to read the validation_report.txt and the extracted_claims.json, and generate a JSON output
that summarizes the validation results in a structured format.

Here's how you should process the information:

1.  **Read the validation_report.txt**: This file contains a summary of errors found during the validation process.
    Each error specifies the row number, claim number, field, expected value, and extracted value.
2.  **Read the extracted_claims.json**: This file contains the original extracted data for each claim.
3.  **Combine the information**: For each claim in the extracted_claims.json, create a validation entry in the output JSON.
    The validation entry should include the claim number and a list of validations.
    Each validation should include the attribute, extracted value, validated value, validation status, confidence score, and remarks.
4.  **Populate the validation details**:
    -   **attribute**: The field name from the extracted_claims.json (e.g., "date_of_loss", "claim_status").
    -   **extracted_value**: The value extracted from the document for the attribute.
    -   **validated_value**: If the validation_report.txt indicates an error for this attribute, use the "Expected" value from the report.
        Otherwise, use the same value as the extracted_value.
    -   **validation_status**: If the validation_report.txt indicates an error for this attribute, set the status to "Invalid".
        Otherwise, set the status to "Valid".
    -   **confidence_score**: Assign a confidence score of 95 for all validations.
    -   **remarks**: If the validation_report.txt indicates an error, provide a remark like "Incorrect extraction, used validated value".
        Otherwise, provide a remark like "Correct extraction".
5.  **Format the output**: The output should be a JSON object conforming to the structure defined in HumanValidationsList.

Remember to handle cases where the validation_report.txt is empty (no errors found) and to process all claims in the extracted_claims.json.

Format the output as a JSON object conforming to the following structure:
{human_validation_format_instructions}

validation_report.txt: {validation_report}
extracted_claims.json: {extracted_claims}
"""

human_validation_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(human_validation_system_template),
    HumanMessagePromptTemplate.from_template(
        "validation_report.txt: {validation_report}\nextracted_claims.json: {extracted_claims}"
    )
])