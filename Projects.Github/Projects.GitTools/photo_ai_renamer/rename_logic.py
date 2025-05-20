import os
from PIL import Image
from PIL.ExifTags import TAGS
import datetime
import shutil

def get_exif_timestamp(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if exif_data:
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == 'DateTimeOriginal':
                    return value.replace(":", "-").replace(" ", "_")
    except Exception:
        pass
    # Fallback: use file modification time
    mtime = os.path.getmtime(image_path)
    return datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d_%H-%M-%S")

def get_placeholder_label(image_path):
    # Placeholder: replace with AI later
    return "image"

def process_images(source_folder, output_folder, log_fn):
    for file in os.listdir(source_folder):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            src = os.path.join(source_folder, file)
            timestamp = get_exif_timestamp(src)
            label = get_placeholder_label(src)
            new_name = f"{timestamp}_{label}{os.path.splitext(file)[1]}"
            dst = os.path.join(output_folder, new_name)
            shutil.copy2(src, dst)
            log_fn(f"Renamed '{file}' to '{new_name}'")
