# CT Scan Texture Analysis with Heightmap Generation

This project extracts texture features from CT scan images in DICOM format and visualizes them as 2D heightmaps. It aims to assist in medical image analysis by enhancing visual representation of tissue density and texture through spatial surface plots.

## Project Objective

- Load CT scan DICOM files using `pydicom`
- Extract texture features (e.g., contrast, entropy, homogeneity) using `scikit-image`
- Convert those features into 2D heightmaps for visual and spatial interpretation

## Tools & Libraries Used

- `pydicom` – Read CT DICOM files
- `numpy` – Matrix and array manipulation
- `matplotlib` – Heightmap plotting (3D surface)
- `scikit-image` – GLCM texture feature extraction
- `pandas` – Store extracted features for future ML use

## 📁 Project Structure
<pre> ct-texture-dicom/ ├── dicom_texture_extractor.py # Main script for processing CT scans ├── requirements.txt # Python dependencies ├── README.md # Project description and instructions ├── LICENSE # Open-source license ├── example_heightmap.png # Sample visualization of a heightmap ├── features.csv # Optional: texture features as table ├── /dicom_samples/ # Sample DICOM CT images (optional) └── /heightmaps/ # Output: generated heightmap plots </pre>
