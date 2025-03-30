

# crew.py
from crewai import Crew
from tasks.extraction_task import create_extraction_task
from tasks.validation_task import create_validation_task
from tasks.human_validation_task import create_human_validation_task

def create_crew(pdf_chunks):
    extraction_task = create_extraction_task(pdf_chunks)
    validation_task = create_validation_task()
    human_validation_task = create_human_validation_task()

    return Crew(
        agents=[extraction_task.agent, validation_task.agent, human_validation_task.agent],
        tasks=[extraction_task, validation_task, human_validation_task],
        verbose=True
    )


# crew.py
# from crewai import Crew
# from tasks.extraction_task import create_extraction_task
# from tasks.validation_task import create_validation_task
# from tasks.human_validation_task import create_human_validation_task

# def create_crew(pdf_chunks):
#     # Define file names for intermediate outputs
#     extracted_claims_file = "extracted_claims.json"
#     validation_report_file = "validation_report.txt"
#     human_validation_report_file = "human_validation_report.json"

#     extraction_task = create_extraction_task(pdf_chunks, extracted_claims_file)
#     validation_task = create_validation_task(extracted_claims_file, validation_report_file, pdf_chunks)
#     human_validation_task = create_human_validation_task(extracted_claims_file, validation_report_file, human_validation_report_file)

#     return Crew(
#         agents=[extraction_task.agent, validation_task.agent, human_validation_task.agent],
#         tasks=[extraction_task, validation_task, human_validation_task],
#         verbose=True
#     )


# crew.py
# from crewai import Crew
# from tasks.extraction_task import create_extraction_task
# from tasks.validation_task import create_validation_task
# from tasks.human_validation_task import create_human_validation_task
# from agents.data_extractor import create_data_extractor_agent
# from agents.data_validator import create_data_validator_agent
# from agents.human_validation_agent import create_human_validation_agent

# def create_crew(pdf_chunks):
#     # Define file names for intermediate outputs
#     extracted_claims_file = "extracted_claims.json"
#     validation_report_file = "validation_report.txt"
#     human_validation_report_file = "human_validation_report.json"

#     #Creating agent to send it!
#     data_extraction_agent = create_data_extractor_agent()
#     data_validation_agent = create_data_validator_agent()
#     human_validation_agent = create_human_validation_agent()

#     extraction_task = create_extraction_task(pdf_chunks, data_extraction_agent)
#     validation_task = create_validation_task(extracted_claims_file, validation_report_file, pdf_chunks, data_validation_agent)
#     human_validation_task = create_human_validation_task(extracted_claims_file, validation_report_file, human_validation_report_file, human_validation_agent)

#     return Crew(
#         agents=[data_extraction_agent, data_validation_agent, human_validation_agent],
#         tasks=[extraction_task, validation_task, human_validation_task],
#         verbose=True
#     )