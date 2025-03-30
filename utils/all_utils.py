



import logging
import json
import os






def serialize_output(data):
    """Convert CrewOutput or TaskOutput to JSON-serializable format."""
    if isinstance(data, list):
        return [serialize_output(item) for item in data]
    elif isinstance(data, dict):
        return data  # Return directly if already a dictionary
    elif hasattr(data, "model_dump"):
        return data.model_dump()  # Convert to dict if it's a Pydantic model
    else:
        return str(data)  # Ensure it's serializable
    
def load_json_file(file_path):
    """Load a JSON file and return its content as a list."""
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
                return data if isinstance(data, list) else [data]
        except json.JSONDecodeError:
            logging.warning(f"⚠️ {file_path} is corrupted. Resetting...")
            return []
    return []

def append_to_file(data, file_path):
    """Append new data to a JSON file, ensuring existing data is retained."""
    existing_data = load_json_file(file_path)
    if isinstance(data, dict):
        existing_data.append(data)
    elif isinstance(data, list):
        existing_data.extend(data)
    
    with open(file_path, "w") as f:
        json.dump(existing_data, f, indent=2)
        f.flush()
    
    logging.info(f"✅ Data appended to `{file_path}` (Total: {len(existing_data)} entries)")



OUTPUT_FILE = "extractions.json"
HUMAN_VALIDATION_FILE = "human_validations.json"
FINAL_OUTPUT_FILE = "final_output.json"
def save_final_output():
    """Merge extracted and human validated data and save the final output."""
    growing_data = load_json_file(OUTPUT_FILE)
    human_validation = load_json_file(HUMAN_VALIDATION_FILE)
    
    final_data = {
        "results": growing_data,
        "human_validations": human_validation
    }

    with open(FINAL_OUTPUT_FILE, "w") as f:
        json.dump(final_data, f, indent=2)
        f.flush()

    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
    # if os.path.exists(HUMAN_VALIDATION_FILE):
    #     os.remove(HUMAN_VALIDATION_FILE) 
    
    logging.info(f"✅ Final combined data saved to `{FINAL_OUTPUT_FILE}`")