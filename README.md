# HE Image Stitcher 🧵🩸

This repository contains a simple tool for stitching together Hematoxylin and Eosin (HE)-stained histological images into a single composite image.

## 🔧 Features

- Merge multiple HE-stained image tiles into one composite image
- Designed for histological section scanning (e.g., partial field captures)
- Supports image input in PNG, JPEG, or TIFF formats
- Adjustable output resolution and layout
- Minimal dependencies, ready to run

## 📂 Files

| File | Description |
|------|-------------|
| `he_stitcher.py` | Main script to perform horizontal/vertical stitching of HE images |
| `example_input/` | Sample image tiles (optional) |
| `stitched_output/` | Output folder for composite images |

## 🚀 How to Use

1. Place your HE-stained image tiles into a folder (e.g., `./input_images`)
2. Run the script:
   ```bash
   python he_stitcher.py --input ./input_images --output ./stitched_output
