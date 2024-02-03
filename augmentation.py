import copy

import numpy as np
import scipy.ndimage


class Augmentation:
    def __init__(self, images: list):
        self.images = images
        self.augmented_images = list()

    @staticmethod
    def rotate(volume, angle):
        # Rotate the volume
        rotated_volume = scipy.ndimage.rotate(volume, angle, reshape=False)
        return rotated_volume

    @staticmethod
    def flip(volume, axis):
        # Flip the volume along a specified axis
        flipped_volume = np.flip(volume, axis=axis)
        return flipped_volume

    @staticmethod
    def add_noise(volume, mean=0, std=0.1):
        # Add Gaussian noise to the volume
        noise = np.random.normal(mean, std, volume.shape)
        noisy_volume = volume + noise
        return noisy_volume

    def generate(self):
        for image in self.images:
            augmented_volume = self.rotate(image, angle=30)  # Rotate by 30 degrees
            augmented_volume = self.flip(augmented_volume, axis=0)  # Flip along the first axis
            augmented_volume = self.add_noise(augmented_volume)  # Add Gaussian noise
            self.augmented_images.append(copy.deepcopy(augmented_volume))
