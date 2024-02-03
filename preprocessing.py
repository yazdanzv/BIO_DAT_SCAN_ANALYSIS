import numpy as np
import scipy.ndimage


class Preprocess:
    def __init__(self, images: list):
        self.normalized_volumes = list()
        self.images = images

    @staticmethod
    def resize(volume: np.array, target_size: tuple):
        resized_volume = scipy.ndimage.zoom(volume, np.array(target_size) / np.array(volume.shape),
                                            order=1)  # trilinear interpolation
        return resized_volume

    @staticmethod
    def normalize(volume):
        # Normalize the volume
        min_val = np.min(volume)
        max_val = np.max(volume)
        normalized_volume = (volume - min_val) / (max_val - min_val)
        return normalized_volume

    def start(self):
        preprocessed_volumes = [self.normalize(self.resize(volume)) for volume in self.images]
        return preprocessed_volumes
