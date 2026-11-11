# BIO_DAT_SCAN_ANALYSIS

## Code guide

`main.ipynb` ties together the DICOM image workflow. `loading_data.py` defines `LoadData` for reading image data, `preprocessing.py` defines `Preprocess` for image preparation, and `augmentation.py` defines `Augmentation` for transformations. The Python modules use `pydicom`, NumPy, and SciPy. Open the notebook from the repository root so its local imports resolve, and supply the image data expected by its loading cells.
