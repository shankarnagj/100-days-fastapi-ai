from fastapi import APIRouter
from schemas import PromptRequest, PromptResponse
from services import process_prompt

router = APIRouter()

@router.post("/prompt", response_model=PromptResponse)
def prompt_api(request: PromptRequest):
    result = process_prompt(request.prompt)

    return PromptResponse(
        response=result
    )