import numpy as np
from PIL import Image
import os
import imghdr
# import cv2


def get_avg_rgb(image):      # gets avg RGB value for each input image as a numpy array
    img = np.array(image)
    width, height, depth = img.shape
    # print(width, height, depth,'\n')
    return tuple(np.average(img.reshape(width * height, depth), axis=0))   # returns avg rgb value of image 3 x 1 format


def split_image(image, size):       # splits an image into smaller images according to size tuple ( rows, cols)
    org_width, org_height = image.size[0], image.size[1]
    rows, cols = size
    new_width, new_height = int(org_width / cols), int(org_height / rows)
    print(org_width, org_height, '\n', rows, cols, '\n', new_width, new_height)

    imgs = []
    for j in range(rows):
        for i in range(cols):
            # image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_NEAREST)
            # image = image.resize((new_width, new_height), Image.ANTIALIAS)
            imgs.append(image.crop((i * new_width, j * new_height, (i + 1) * new_width, (j + 1) * new_height)))

    return imgs


def get_images(image_dir):      # given a directory of images, returns list of images to insert
    files = os.listdir(image_dir)
    images = []

    for file in files:
        file_path = os.path.abspath(os.path.join(image_dir, file))    # creates directory string
        try:
            with open(file_path, 'rb') as f_path:
                im = Image.open(file_path)
                im.load()               # force loading of image data from file
                images.append(im)
        except FileNotFoundError:
             print("Invalid image: {0}".format(file_path, ))

    return images


def get_image_file_names(image_dir):        # returns list of image file names from given directory
    files = os.listdir(image_dir)
    file_names = []

    for file in files:
        file_path = os.path.abspath(os.path.join(image_dir, file))
        try:
            img_type = imghdr.what(file_path)      # determines image type (i.e. extension type)
            if img_type:
                file_names.append(file_path)
        except FileNotFoundError:
            print("Invalid image: {0}".format(file_path, ))

    return file_names


def get_best_match_index(input_avg, avgs):   # returns index of best image match based on average RGB value distances

    avg = input_avg

    index, min_index = 0, 0
    min_dist = float('inf')

    for val in avgs:
        dist = 0
        for i in range(3):
            dist += (val[i] - avg[i]) ** 2
        if dist < min_dist:
            min_dist = dist
            min_index = index
        index += 1

    return min_index


def create_img_grid(images, dimensions):      # given a list of images and grid size (x, y), a grid of images is created
    x, y = dimensions

    assert x * y == len(images)         # checks if images will fill grid
    # max image dimensions found as all images may not be of same size.
    # images smaller than max will have the empty space filled with a black background, making it less visible
    img_width = max([img.size[0] for img in images])
    img_height = max([img.size[1] for img in images])

    result_image = Image.new('RGB', (y * img_width, x * img_height))

    for index in range(len(images)):
        row = int(index / y)
        column = index - y * row
        result_image.paste(images[index], (column * img_width, row * img_height))

    return result_image


def create_photomosaic(target_image, input_images, grid_size, reverse, reuse_images=True):
    # main function that creates the Photomosaic

    print('Splitting input images.')
    target_images = split_image(target_image, grid_size)

    print("Finding image matches.")
    output_images = []     # array of output images used in the resulting mosaic
    count = 0
    batch_size = int(len(target_images) / 10)   # creates batches to speed up execution

    averages = []
    for img in input_images:
        averages.append(get_avg_rgb(img))

    for img in target_images:
        avg = get_avg_rgb(img)
        match_index = get_best_match_index(avg, averages)
        output_images.append(input_images[match_index])

        if count > 0 and batch_size > 10 and count % batch_size == 0:
            print("Processed {0} of {1} images".format(count, len(target_images)))
        count += 1

        if not reuse_images:
            input_images.remove(match_index)

    print('Creating mosaic')
    if reverse:
        mosaic_image = create_img_grid(output_images[::-1], grid_size)
    else:
        mosaic_image = create_img_grid(output_images, grid_size)

    return mosaic_image

"""
x = get_image_file_names('img_data')
print(x)
"""