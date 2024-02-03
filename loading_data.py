import copy
import os
import pydicom
import numpy as np

# File path
PATH_BIG = 'DATASET/NEW/BIG/PPMI/'
PATH_SMALL = 'DATASET/NEW/SMALL/PPMI/'


class LoadData:
    def __init__(self):
        self.images_big = list()
        self.images_small = list()

    def load_data(self):
        # BIG folder
        for root, folders, files in os.walk(PATH_BIG):
            temp_img = np.array([])
            if len(list(files)) != 0:
                for file in list(files):
                    if ".dcm" in file.lower():
                        dicom_file = pydicom.read_file(os.path.join(root, file), force=True)
                        dicom_file.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian
                        temp = dicom_file.pixel_array
                        temp = np.array(temp)
                        temp_img = np.append(temp_img, copy.deepcopy(temp))
                self.images_big.append(copy.deepcopy(temp_img))

        # SMALL folders
        for root, folders, files in os.walk(PATH_SMALL):
            temp_img = np.array([])
            if len(list(files)) != 0:
                for file in list(files):
                    if ".dcm" in file.lower():
                        dicom_file = pydicom.read_file(os.path.join(root, file), force=True)
                        dicom_file.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian
                        temp = dicom_file.pixel_array
                        temp = np.array(temp)
                        temp_img = np.append(temp_img, copy.deepcopy(temp))
                self.images_small.append(copy.deepcopy(temp_img))