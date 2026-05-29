# AI App Compiler

## 1. Project Overview
This project is an AI-powered app compiler built using FastAPI. It takes a natural language prompt from the user and converts it into a full application blueprint including intent, architecture, UI schema, database schema, API schema, and runtime simulation. It also includes validation and automatic repair mechanisms to improve output quality.

---

## 2. Architecture
The system is modular and pipeline-based.

Modules:
- Intent Extractor
- Architecture Generator
- UI Schema Generator
- Database Schema Generator
- API Schema Generator
- Validator
- Repair Engine
- Runtime Simulator

Flow:
User Prompt → Intent Extraction → Architecture Generation → Schema Generation (UI/DB/API) → Validation → Repair (if needed) → Runtime Simulation → Final Output

---

## 3. Pipeline
Step-by-step execution:

1. User sends a prompt via `/generate`
2. Intent is extracted using `extract_intent()`
3. System architecture is generated
4. UI schema is created
5. Database schema is created
6. API schema is created
7. Runtime simulation is executed
8. Validation checks are applied
9. Errors (if any) are collected
10. Repair engine fixes issues if errors exist
11. Final structured response is returned

---

## 4. Validation
Validation ensures correctness of generated schemas.

Two levels:
- Schema validation → `validate_schema(result)`
- Architecture validation → `validate_architecture(api_schema, db_schema)`

Errors are collected in a single list for repair processing.

---

## 5. Repair Engine
If validation fails, the system activates the repair engine:

Function:
- `repair_schema(result, errors, db_schema)`

Responsibilities:
- Fix incorrect or missing fields
- Align schemas with architecture rules
- Improve consistency across outputs

---

## 6. Runtime Simulation
The runtime simulator tests execution behavior using:

Function:
- `simulate_runtime(ui_schema)`

It simulates how the generated UI/schema behaves in real execution conditions.

---

## 7. Metrics
(Current system can be extended to track these)

- Requests processed
- Validation errors
- Repair actions triggered
- Runtime simulation outputs
- Success/failure rate

---

## 8. Tradeoffs
- Rule-based generation is fast but not always fully accurate
- Repair engine improves correctness but adds latency
- Modular design improves scalability but increases complexity
- Runtime simulation improves reliability but increases processing time