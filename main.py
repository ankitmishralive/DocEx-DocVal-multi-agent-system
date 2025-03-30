


import logging
from crewai import Crew
from agents.data_extractor import create_data_extractor_agent
from agents.data_validator import create_data_validator_agent
from agents.human_validator import create_human_validation_agent
from tasks.extraction_task import create_extraction_task
from tasks.validation_task import create_validation_task
from tasks.human_validation_task import create_human_validation_task
from tools.pdf_loader import load_and_chunk_pdf
from config import CHUNK_SIZE, CHUNK_OVERLAP, PDF_FILE_PATH

from utils.all_utils import *

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

OUTPUT_FILE = "extractions.json"
HUMAN_VALIDATION_FILE = "human_validations.json"
FINAL_OUTPUT_FILE = "final_output.json"

def main():
    try:
        # Step 1: Load and chunk the PDF
        pdf_chunks = load_and_chunk_pdf(PDF_FILE_PATH, CHUNK_SIZE, CHUNK_OVERLAP)
        if not pdf_chunks:
            print("❌ Failed to load or chunk PDF.")
            return
        
        # Step 2: Process each chunk dynamically
        for chunk in pdf_chunks:
            extraction_task = create_extraction_task(chunk)

            # Create an Extraction Crew
            extraction_crew = Crew(
                agents=[create_data_extractor_agent()],
                tasks=[extraction_task],
                verbose=True
            )

            # Run extraction for the chunk
            extraction_crew.kickoff()
            extraction_task_output = extraction_task.output
            data = extraction_task_output.json_dict.get('claims', None)
            append_to_file(data, OUTPUT_FILE)

        print(f"✅ All extracted claims saved to `{OUTPUT_FILE}`.")

        # Step 3: Load full extracted data for validation
        extracted_claims = load_json_file(OUTPUT_FILE)

        # Step 4: Pass extracted data to validation & human validation
        validation_task = create_validation_task(extracted_claims)
        human_validation_task = create_human_validation_task()

        # Step 5: Create Validation Crew
        validation_crew = Crew(
            agents=[create_data_validator_agent(), create_human_validation_agent()],
            tasks=[validation_task, human_validation_task],
            verbose=True
        )

        # Step 6: Run validation & human validation
        validation_crew.kickoff()
        # serialize_output(validation_crew_output)

        # Step 7: Merge and save final output
        save_final_output()
        print("✅ Final processed data saved.")

    except Exception as e:
        logging.error(f"❌ An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()
