import os
import pydicom
import numpy as np
import cv2
from skimage import feature, exposure
from PIL import Image
# --- Config ---
dicom_dir = r"C:\Users\samra\mltheory\Anonymized_20250524\series-00003"
output_texture_map = r"C:\Users\samra\mltheory\bone_texture_heightmap.png"
slice_index = None  # None = middle slice

# --- Load DICOM Series ---
slices = [pydicom.dcmread(os.path.join(dicom_dir, f)) 
          for f in os.listdir(dicom_dir) if f.endswith(".dcm")]
slices.sort(key=lambda s: float(s.ImagePositionPatient[2]))
print(f"Loaded {len(slices)} slices.")

if slice_index is None:
    slice_index = len(slices) // 2
img = slices[slice_index].pixel_array.astype(np.float32)
# --- Normalize & Enhance ---
img -= img.min()
img /= img.max()
img *= 255
img = img.astype(np.uint8)
# --- CLAHE to enhance porous contrast ---
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
enhanced = clahe.apply(img)

# --- Local Binary Pattern (LBP) Texture Feature ---
radius = 3
n_points = 8 * radius
lbp = feature.local_binary_pattern(enhanced, n_points, radius, method="uniform")
lbp_normalized = (lbp - lbp.min()) / (lbp.max() - lbp.min()) * 255

# --- Save Texture Map ---
Image.fromarray(lbp_normalized.astype(np.uint8)).save(output_texture_map)
print(f"✅ Saved texture heightmap to:\n{output_texture_map}")
