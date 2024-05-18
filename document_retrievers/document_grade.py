from langchain_core.pydantic_v1 import BaseModel, Field


class DocumentGrade(BaseModel):
    """Letter grade to determine relevancy of a document"""

    grade: str = Field(
        description="Document grade for relevancy, 'A', 'B', 'C', 'D', or 'F'",
    )
