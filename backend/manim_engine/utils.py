## HELPERS --> SCENE NAME EXTRACTOR
import re


def extract_scene_name(code: str) -> str:
    match = re.search(r'class\s+(\w+)\s*\(Scene\)', code)
    return match.group(1) if match else "UnknownScene"

