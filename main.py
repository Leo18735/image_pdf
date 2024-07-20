import argparse
import os
import sys
import shutil
import glob
from pdf2image import convert_from_path
from PIL import Image


def convert_images_to_pdf(folder: str, file: str) -> int:
    try:
        images = [Image.open(x) for x in glob.glob(f"{folder}/*")]
        images[0].save(file, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
    except Exception as e:
        print(f"Error in convert_images_to_pdf: {e}")
        return 2
    return 0


def convert_pdf_to_images(size: int, folder: str, file: str) -> int:
    try:
        shutil.rmtree(folder, ignore_errors=True)
        os.makedirs(folder, exist_ok=True)
        pages = convert_from_path(file, size)
        for count, page in enumerate(pages):
            page.save(f'{folder}/{count}.jpeg', 'JPEG')
    except Exception as e:
        print(f"Error in convert_pdf_to_images: {e}")
        return 1
    return 0


def main(pdf_to_image: bool, image_to_pdf: bool, size: int, folder: str, file: str) -> int:
    if image_to_pdf:
        return convert_images_to_pdf(folder, file)
    elif pdf_to_image:
        return convert_pdf_to_images(size, folder, file)
    else:
        print("One argument must be true!")
    return 3


def parse_arguments() -> dict:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--pdf_to_image', action="store_true")
    group.add_argument('--image_to_pdf', action="store_true")
    parser.add_argument('--size', type=int, default=500)
    parser.add_argument('--folder', type=str, required=True)
    parser.add_argument('--file', type=str, required=True)
    return vars(parser.parse_args())


if __name__ == '__main__':
    sys.exit(main(**parse_arguments()))
