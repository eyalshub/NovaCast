# app/agents/types.py
from pydantic import BaseModel, Field
from typing import Optional
from typing import List
from typing import TypedDict

class IdeationAgentOutput(TypedDict):
    idea: str
class IdeationAgentInput(BaseModel):
    topic: str = Field(..., description="The main topic or subject of the video idea")
    tone: str = Field(default="neutral", description="The desired tone of the idea, e.g., 'funny', 'serious'")
    audience: Optional[str] = Field(default=None, description="Who the content is for")
    goal: Optional[str] = Field(default=None, description="What the video aims to achieve, e.g., 'educate', 'entertain'")
    platform: Optional[str] = Field(default="YouTube Shorts", description="Where the video will be published")
    style: Optional[str] = Field(default=None, description="Preferred structure or format, e.g., 'listicle', 'story'")
    max_words: Optional[int] = Field(default=25, description="Maximum number of words in the output idea")
    language: Optional[str] = Field(default="en", description="Language code (en/he/es/etc)")

    class Config:
        schema_extra = {
            "example": {
                "topic": "How AI helps teachers",
                "tone": "funny",
                "audience": "burnt-out high school teachers",
                "goal": "make them laugh and feel seen",
                "platform": "TikTok",
                "style": "relatable pain point + twist",
                "max_words": 25,
                "language": "en"
            }
        }


class OutlineSection(BaseModel):
    heading: str = Field(..., description="Section heading")
    bullets: List[str] = Field(..., min_items=1, description="Bulleted talking points")


class OutlineAgentInput(BaseModel):
    topic: str
    idea: str
    tone: str = "neutral"
    audience: str = "general"
    goal: str = "inform"
    platform: str = "youtube_short"
    style: str = "concise"
    max_sections: int = 5
    language: str = "en"


class OutlineAgentResult(BaseModel):
    title: str
    language: str
    audience: str
    platform: str
    sections: List[OutlineSection]
    cta: str