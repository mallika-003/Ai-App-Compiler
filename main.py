from fastapi import FastAPI
from pydantic import BaseModel

from intent_extractor import extract_intent
from architecture_generator import generate_architecture
from ui_schema_generator import generate_ui_schema
from db_schema_generator import generate_db_schema
from api_schema_generator import generate_api_schema
from validator import validate_schema, validate_architecture
from repair_engine import repair_schema
from runtime_simulator import simulate_runtime

app = FastAPI()


class UserPrompt(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {"message": "AI App Compiler Running"}


@app.post("/generate")
def generate_app(data: UserPrompt):

    prompt = data.prompt

    # STEP 1 — Intent Extraction
    result = extract_intent(prompt)

    # STEP 2 — Architecture Generation
    architecture = generate_architecture(result)

    # STEP 3 — UI Schema
    ui_schema = generate_ui_schema(architecture)

    # STEP 4 — Database Schema
    db_schema = generate_db_schema(architecture)

    # STEP 5 — API Schema
    api_schema = generate_api_schema(architecture)

    # STEP 6 — Runtime Simulation
    runtime_output = simulate_runtime(ui_schema)

    # STEP 7 — Validation
    errors = validate_schema(result)

    architecture_errors = validate_architecture(
        api_schema,
        db_schema
    )

    errors.extend(architecture_errors)

    # STEP 8 — Repair Engine
    if errors:
        result = repair_schema(
            result,
            errors,
            db_schema
        )

    # FINAL OUTPUT
    return {
        "intent": result,
        "architecture": architecture,
        "ui_schema": ui_schema,
        "db_schema": db_schema,
        "api_schema": api_schema,
        "runtime_output": runtime_output,
        "errors": errors
    }