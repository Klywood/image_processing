"""
Script to convert all images to specified format

input data: path to folder with folders that contains images
"""

import os

from PIL import Image

"""You can download images using Grabber of Pictures
URL - https://sourceforge.net/projects/grabber-of-pictures/
"""


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


def convert_images(path_to_folders, convert_to='jpg'):
    """Converts images from the specified folders to the specified
    format and saves to the appropriate folders with numbering in order

    :param path_to_folders: list with paths to folders with images
    :param convert_to: the format to which you want to convert (jpg - as default)
    """
    #  dict for saving img using pillow lib
    pil_dict = {'jpg': 'jpeg', 'png': 'png', 'webp': 'webp'}
    save_as = pil_dict[convert_to]
    #  go through list with paths to images
    for folder in path_to_folders:
        #  create the folder to save images
        fold_name = os.path.join('data', folder[folder.find('_', folder.find('_') + 1) + 1:])
        os.makedirs(fold_name, exist_ok=True)
        #  counter for naming the images in current folder
        count = 1
        #  walk through current folder
        for root, dirs, images in os.walk(folder):
            #  work with images
            for img in images:
                try:
                    im = Image.open(os.path.join(root, img)).convert('RGB')
                    #  creating full name to save the image
                    full_name = os.path.join(fold_name, str(count))
                    im.save(f"{full_name}.{convert_to}", save_as)
                    count += 1
                #  go to next if error occurred
                except Exception as err:
                    print(f"Error {err} occurred")
                    continue
        print(f"Folder '{fold_name}' done. Going to next")
    print("End of work")


if __name__ == '__main__':
    #  list with paths to folders with images
    folders = get_path_to_folders(r'C:\Users\User\Desktop\DataSets\from-ggl')
    #  convert and rename all images
    convert_images(folders)
