"""
AI Inference endpoints for clinical documentation
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from app.services.note_generator import NoteGenerator
from app.services.code_suggester import CodeSuggester
from app.services.summarizer import DocumentSummarizer

router = APIRouter()


class NoteGenerationRequest(BaseModel):
    """Request to generate clinical note"""
    patient_id: str
    encounter_data: Dict[str, Any]
    document_type: str  # progress_note, discharge_summary, etc.
    style: Optional[str] = "professional"
    include_sections: Optional[List[str]] = None


class NoteGenerationResponse(BaseModel):
    """Response with generated note"""
    note_content: str
    sections: Dict[str, str]
    confidence: float
    model_used: str
    tokens_generated: int


class CodeSuggestionRequest(BaseModel):
    """Request for code suggestions"""
    text: str
    code_type: str  # ICD-10, CPT, or both
    max_results: int = 10


class CodeSuggestion(BaseModel):
    """Single code suggestion"""
    code: str
    description: str
    category: str
    confidence: float
    rationale: str


class CodeSuggestionResponse(BaseModel):
    """Response with code suggestions"""
    suggestions: List[CodeSuggestion]
    total_count: int
    model_used: str


class SummarizationRequest(BaseModel):
    """Request to summarize document"""
    document: str
    max_length: Optional[int] = 300
    min_length: Optional[int] = 100
    focus_areas: Optional[List[str]] = None


class SummarizationResponse(BaseModel):
    """Response with summary"""
    summary: str
    key_points: List[str]
    word_count: int
    compression_ratio: float
    model_used: str


@router.post("/generate-note", response_model=NoteGenerationResponse)
async def generate_clinical_note(request: NoteGenerationRequest):
    """
    Generate clinical note using AI

    - **patient_id**: Patient identifier
    - **encounter_data**: Raw encounter data (notes, vitals, labs, etc.)
    - **document_type**: Type of note to generate
    - **style**: Writing style (professional, concise, detailed)
    - **include_sections**: Specific sections to include
    """
    try:
        generator = NoteGenerator()
        result = await generator.generate(
            patient_id=request.patient_id,
            encounter_data=request.encounter_data,
            document_type=request.document_type,
            style=request.style,
            include_sections=request.include_sections
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/suggest-codes", response_model=CodeSuggestionResponse)
async def suggest_medical_codes(request: CodeSuggestionRequest):
    """
    Get AI-powered medical code suggestions

    - **text**: Clinical text to analyze
    - **code_type**: Type of codes (ICD-10, CPT, or both)
    - **max_results**: Maximum number of suggestions
    """
    try:
        suggester = CodeSuggester()
        result = await suggester.suggest(
            text=request.text,
            code_type=request.code_type,
            max_results=request.max_results
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/summarize", response_model=SummarizationResponse)
async def summarize_document(request: SummarizationRequest):
    """
    Generate AI summary of clinical document

    - **document**: Document text to summarize
    - **max_length**: Maximum summary length
    - **min_length**: Minimum summary length
    - **focus_areas**: Specific areas to focus on
    """
    try:
        summarizer = DocumentSummarizer()
        result = await summarizer.summarize(
            document=request.document,
            max_length=request.max_length,
            min_length=request.min_length,
            focus_areas=request.focus_areas
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/extract-entities")
async def extract_entities(text: str):
    """
    Extract medical entities from text

    - **text**: Clinical text to analyze
    """
    try:
        from app.services.entity_extractor import EntityExtractor
        extractor = EntityExtractor()
        entities = await extractor.extract(text)
        return {"entities": entities}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
