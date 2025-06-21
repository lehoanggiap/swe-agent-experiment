from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="Calculator API", description="A simple calculator with basic operations")

class CalculationRequest(BaseModel):
    a: float
    b: float
    operation: str

class CalculationResult(BaseModel):
    result: float
    operation: str
    inputs: dict

# Store calculation history
calculation_history: List[CalculationResult] = []

@app.get("/")
async def root():
    return {"message": "Welcome to Calculator API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/calculate", response_model=CalculationResult)
async def calculate(request: CalculationRequest):
    """
    Perform basic mathematical operations.
    
    BUG: This function has a division by zero issue when b=0 and operation="divide"
    This is intentionally left unfixed for SWE Agent to detect and fix automatically.
    """
    a = request.a
    b = request.b
    operation = request.operation.lower()
    
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        # BUG: No check for division by zero!
        result = a / b  # This will raise ZeroDivisionError when b=0
    else:
        raise HTTPException(status_code=400, detail=f"Unsupported operation: {operation}")
    
    # Store in history
    calc_result = CalculationResult(
        result=result,
        operation=operation,
        inputs={"a": a, "b": b}
    )
    calculation_history.append(calc_result)
    
    return calc_result

@app.get("/history")
async def get_history():
    """Get calculation history."""
    return {"history": calculation_history}

@app.get("/history/clear")
async def clear_history():
    """Clear calculation history."""
    global calculation_history
    calculation_history = []
    return {"message": "History cleared", "total_cleared": len(calculation_history)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)