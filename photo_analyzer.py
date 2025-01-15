import numpy as np
import cv2
import os
import argparse

parser = argparse.ArgumentParser(
    prog="photo_analyzer",
    description="A program to analyze JPEG and PNG images. It detects exposure (overexposed/underexposed), \
    calculates the average color in hexadecimal format, extracts image resolution, and stores these details in a CSV file.",
)

parser.add_argument(
    "photo_directory",
    type=str,
    help="Path to the directory containing the images to analyze.",
)

args = parser.parse_args()

DIR_PATH = args.photo_directory

class AnalyzePhotoException(Exception):
    pass


def get_filenames_from_dir(path=DIR_PATH):
    files = os.listdir(path)
    image_files = [f for f in files if f.endswith((".JPG", ".jpeg", ".png"))]
    if not image_files:
        raise AnalyzePhotoException("Directory contains no compatible images.")
    return image_files


def get_image_from_filename(filename):
    image_path = os.path.join(DIR_PATH, filename)
    return cv2.imread(image_path)


def check_exposure(image, tol=0.3):
    histogram_bins_borders = [0, 128, 255]

    mean_values = image.mean(axis=2).flatten()
    (dark_pixels, bright_pixels), _ = np.histogram(mean_values, histogram_bins_borders)
    half_pixels = (dark_pixels + bright_pixels) / 2

    if bright_pixels > half_pixels + half_pixels * tol:
        return "overexposed"

    elif dark_pixels > half_pixels + half_pixels * tol:
        return "underexposed"

    else:
        return "correct exposure"


def get_color_hex_mean(image):
    B_mean, G_mean, R_mean, _ = cv2.mean(image)
    RGB_hex_mean = f"#{int(R_mean):x}{int(G_mean):x}{int(B_mean):x}"
    return RGB_hex_mean


def get_resolution(image):
    height, width, _ = image.shape
    return f"{height}x{width}"


def create_row(*args):
    return ",".join(map(str, args))


def write_to_csv(rows_array, filename="results.csv", overwrite=True):
    header = "Exposure,Mean Color Hex,Resolution,Filename"
    mode = "w" if overwrite else "a"

    if not filename.endswith(".csv"):
        raise Exception("File should be save as csv file")

    with open(filename, mode) as file:
        if overwrite:
            file.write (f"{header}\n")
        file.write("\n".join(map(str, rows_array)))
        file.write("\n")


image_filenames = get_filenames_from_dir()
rows_array = []

for image_filename in image_filenames:
    image = get_image_from_filename(image_filename)
    new_row = create_row(
        check_exposure(image),
        get_color_hex_mean(image),
        get_resolution(image),
        image_filename,
    )
    rows_array.append(new_row)

write_to_csv(rows_array)
