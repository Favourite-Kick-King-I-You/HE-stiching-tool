
import cv2
import glob
import numpy as np
import os
import argparse

def stitch_folder(folder_path, output_dir):
    folder_name = os.path.basename(folder_path)
    print(f"Processing: {folder_name}")

    image_files = sorted(glob.glob(os.path.join(folder_path, "*.tif")))

    if len(image_files) < 2:
        print(f"Skipped: {folder_name} (fewer than 2 images)")
        return

    images = [cv2.imread(img) for img in image_files]

    stitcher = cv2.Stitcher_create(cv2.Stitcher_SCANS)
    status, stitched = stitcher.stitch(images)

    if status == cv2.Stitcher_OK:
        stitched_rgba = cv2.cvtColor(stitched, cv2.COLOR_BGR2BGRA)
        black_mask = np.all(stitched[:, :] == [0, 0, 0], axis=-1)
        stitched_rgba[black_mask, 3] = 0
        stitched_rgba[~black_mask, 3] = 255

        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{folder_name}_stitched.png")
        cv2.imwrite(output_path, stitched_rgba)

        print(f"Saved: {output_path}")
    else:
        print(f"Stitching failed: {folder_name} (status: {status})")

def main():
    parser = argparse.ArgumentParser(description="Stitch HE-stained images in subfolders")
    parser.add_argument("--input", required=True, help="Path to input directory containing subfolders")
    parser.add_argument("--output", required=True, help="Path to save stitched images")
    args = parser.parse_args()

    subfolders = [f.path for f in os.scandir(args.input) if f.is_dir()]
    for folder in subfolders:
        stitch_folder(folder, args.output)

if __name__ == "__main__":
    main()
