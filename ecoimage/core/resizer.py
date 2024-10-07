from pathlib import Path

from PIL import Image


def resize_image(img_path: Path | str, scale_factor: float) -> Path:
    img_path = Path(img_path)
    img = Image.open(img_path)

    original_width, original_height = img.size
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)

    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    new_path = img_path.with_name(
        f"{img_path.stem}_{new_width}_{new_height}{img_path.suffix}"
    )
    resized_img.save(new_path, format=img.format)

    return new_path
