## PYDANTIC REQUEST MODEL

from pydantic import BaseModel

class PromptRequest(BaseModel):

    """Structure of data --> expecting from the user"""

    user_input: str