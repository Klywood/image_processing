
"""Script for saving augmented images"""

import os

from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img


def get_path_to_folders(root_folder):
    """Finding paths to folders with images

    :param root_folder: path to folder that contains folders with images
    :return: list with abs paths to folders with images
    """
    path_to_folders = []
    for root, dirs, files in os.walk(root_folder):
        for dir in dirs:
            path_to_folders.append(os.path.join(root_folder, dir))
    return path_to_folders


def image_augmentation(folders, samples=4):
    """Creates augmentations for images
    :param folders: list - paths to folders with images
    :param samples: number of augmented samples
    """
    #  create image generator
    aug_gen = ImageDataGenerator(rescale=1. / 255,
                                 rotation_range=15,
                                 width_shift_range=0.2,
                                 height_shift_range=0.2,
                                 shear_range=0.2,
                                 zoom_range=0.2,
                                 horizontal_flip=True,
                                 fill_mode='nearest',
                                 brightness_range=[0.5, 1.5]
                                 )

    for path in folders:
        #  creating new folder to store augmented images
        fold_name = path.split('\\')[-1]
        new_folder = f"augmented_{fold_name}"
        os.makedirs(new_folder, exist_ok=True)

        filenames = os.listdir(path)
        l = len(filenames)
        i = 1
        for file in filenames:
            print(f"file {i} of {l} in '{fold_name}' folder")
            i += 1
            aug_count = 0
            #  read image and convert it to np.array
            img = load_img(os.path.join(path, file))
            img_array = image.img_to_array(img)
            img_arr = img_array.reshape((1,) + img_array.shape)
            #  creating generator with augmented images
            aug_images = aug_gen.flow(img_arr, batch_size=1, save_to_dir=new_folder, save_prefix='aug')
            for batch in aug_images:
                image.array_to_img(batch[0])
                aug_count += 1
                if aug_count == samples:
                    aug_count = 0
                    break


if __name__ == '__main__':
    paths = get_path_to_folders('data')
    image_augmentation(paths)


