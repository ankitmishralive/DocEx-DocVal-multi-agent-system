



from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
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
from utils.all_utils import load_json_file, append_to_file, save_final_output, serialize_output  # Import all_utils


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

OUTPUT_FILE = "extractions.json"
HUMAN_VALIDATION_FILE = "human_validations.json"
FINAL_OUTPUT_FILE = "final_output.json"

app = FastAPI()

@app.post("/process")
async def process_documents():
    """
    API endpoint to process claims from a PDF, perform validation, and return the combined results.
    """
    try:
        # Step 1: Load and chunk the PDF
        pdf_chunks = load_and_chunk_pdf(PDF_FILE_PATH, CHUNK_SIZE, CHUNK_OVERLAP)
        if not pdf_chunks:
            raise HTTPException(status_code=400, detail="Failed to load or chunk PDF.")

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

        logging.info(f"✅ All extracted claims saved to `{OUTPUT_FILE}`.")

   
        extracted_claims = load_json_file(OUTPUT_FILE)


        validation_task = create_validation_task(extracted_claims)
        human_validation_task = create_human_validation_task()


        validation_crew = Crew(
            agents=[create_data_validator_agent(), create_human_validation_agent()],
            tasks=[validation_task, human_validation_task],
            verbose=True
        )


        validation_crew.kickoff()
        

        save_final_output()
 
        final_result = load_json_file(FINAL_OUTPUT_FILE)

        return JSONResponse(content=final_result)

    except Exception as e:
        logging.exception(f"❌ An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))