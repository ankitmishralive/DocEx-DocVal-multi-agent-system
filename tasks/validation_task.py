


# tasks/validation_task.py
from crewai import Task
from agents.data_validator import create_data_validator_agent
from models.claim_details import ClaimsList

# def create_validation_task():
#     return Task(
#         description="""As a Extracted Data Verifier, compare the extracted claim data (extracted_claim.json) against the Real Loss Document Report.
#         Identify incorrect values and generate a detailed validation_report.txt specifying the row number (if available), accurate claim number,
#         the field with incorrect data, and the expected vs. extracted value.

#         Before flagging an error, VERIFY that the extracted value is actually incorrect based on the ROW it's in.  Do NOT flag errors if the extracted value is correct for its row, even if it's vertically close to the 'expected' value.
#          """,
#         agent=create_data_validator_agent(),
#         expected_output="A detailed validation_report.txt file summarizing all incorrect values with row number, claim number, field, expected value, and extracted value, taking layout and row alignment into account.",
#    output_file='validation_report.txt',

#     )


def create_validation_task(extracted_json):
    description=f"""As a Extracted Data Verifier, compare the extracted claim data against the Real Loss Document Report.
    Identify incorrect values and generate a detailed validation_report.txt specifying the row number (if available), accurate claim number, the field with incorrect data, and the expected vs. extracted value.

    Before flagging an error, VERIFY that the extracted value is actually incorrect based on the ROW it's in.  Do NOT flag errors if the extracted value is correct for its row, even if it's vertically close to the 'expected' value.
            
    Extracted Data : {extracted_json}
    """
    return Task(
            description=description,
            expected_output="A detailed validation_report.txt file summarizing all incorrect values.",
               output_file='validation_report.txt',

               agent=create_data_validator_agent()

        )