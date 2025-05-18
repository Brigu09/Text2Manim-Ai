import subprocess
import os
import uuid

# Create output folder (for generated .py files)
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_code(code: str) -> str:
    file_id = uuid.uuid4().hex[:8]
    file_path = os.path.join(OUTPUT_DIR, f"scene_{file_id}.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)
    return file_path


def render_manim_file(file_path: str, scene_name: str, resolution: str = "1920x1080", fps: int = 30) -> str:
    try:
        result = subprocess.run([
            "manim",
            file_path,
            scene_name,
            "--format", "mp4",
            "--resolution", resolution,
            "--fps", str(fps)
        ], check=True, capture_output=True, text=True)

        print("STDOUT:\n", result.stdout)
        print("STDERR:\n", result.stderr)

    except subprocess.CalledProcessError as e:
        print("STDOUT:\n", e.stdout)
        print("STDERR:\n", e.stderr)
        raise RuntimeError("Manim rendering failed") from e

    # Try to auto-detect output path from the file structure
    media_root = os.path.join(os.path.dirname(file_path), "..", "media", "videos")
    possible_output_dir = os.path.join(media_root, scene_name)
    video_file = ""

    for root, _, files in os.walk(possible_output_dir):
        for file in files:
            if file.endswith(".mp4"):
                video_file = os.path.join(root, file)
                break

    if not video_file:
        raise FileNotFoundError("Rendered video file not found.")

    return video_file
