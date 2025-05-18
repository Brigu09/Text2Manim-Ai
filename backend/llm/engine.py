## LLM INTEGRATION LOGIC

import re
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


## load environment variables from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model_name = "deepseek-r1-distill-llama-70b", api_key = GROQ_API_KEY)
prompt = PromptTemplate(
    input_variables = ["user_input"],
    template = """

    You are a professional Python developer using the Manim library.
    Write a full Python script that renders a 2D animation based on the following instruction:
    {user_input}

    Ensure it includes:
    1. All necessary imports (especially 'from manim import *')
    2. A class that inherits from Scene
    3. A construct method with proper indentation
    4. Valid Manim syntax for creating and animating objects
    5. Use readable colors and appropriate positioning of objects
    6. Add appropriate labels and explanations where needed

    Return ONLY Python code, Do NOT include any explanations, comments, or descriptions before the code.
    
    """
)

chain = prompt | llm


## FUNCTION - 1

def extract_code_from_response(response: str) -> str:
    # If the response is wrapped in code blocks (```python ... ```), extract that
    code_blocks = re.findall(r"```(?:python)?(.*?)```", response, re.DOTALL)
    if code_blocks:
        return code_blocks[0].strip()

    # Try to find the first line with 'from manim import *' and return from there
    match = re.search(r"(from manim import \*.*)", response, re.DOTALL)
    if match:
        return match.group(1).strip()

    # As a last resort, return the full response
    return response.strip()

## FUNCTION - 2 --> MAIN FUNCTION

def generate_manim_code(user_input: str) -> str:
    
    """Generate Manim code based on user input using the LLM chain."""

    response = chain.invoke({"user_input": user_input})

    cleaned_response = extract_code_from_response(response)

    return cleaned_response