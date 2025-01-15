# Image Analysis Tool

## Overview
This Python program processes all JPEG and PNG images in a specified directory and generates a CSV file containing the following details for each image:
- **Exposure Analysis:** Determines whether the image is overexposed or underexposed by analyzing its histogram.
- **Average Color:** Computes the average color of all pixels in hexadecimal format (`#RRGGBB`), suitable for use in CSS or web design.
- **Resolution:** Extracts the width and height of the image.
- **File Name:** Includes the name of the image file.

The tool is built using the `OpenCV` and `NumPy` libraries, offering efficient and accurate image processing.

## Features
- **Exposure Detection:** Checks if the number of bright and dark pixels in the image is approximately balanced to identify overexposure or underexposure.
- **Color Analysis:** Calculates a single average color for the image, making it easy to understand the overall color palette.
- **CSV Output:** Outputs all results in an easy-to-use CSV file for further analysis or reporting.

## Prerequisites
Ensure you have Python 3.7 or later installed along with the following libraries:
- `OpenCV`
- `NumPy`
