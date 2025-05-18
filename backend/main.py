from fastapi import FastAPI, HTTPException
from backend.schemas.prompt import PromptRequest
from backend.llm.engine import generate_manim_code
from backend.manim_engine.runner import save_code, render_manim_file
from backend.manim_engine.utils import extract_scene_name

app = FastAPI(title="2D Animation Generator API")

@app.post("/generate")
def generate_animation(request: PromptRequest):
    try:
        code = generate_manim_code(request.user_input)
        scene_name = extract_scene_name(code)
        file_path = save_code(code)
        video_path = render_manim_file(file_path, scene_name)
        return {
            "status": "success",
            "video_path": video_path,
            "scene_name": scene_name
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
