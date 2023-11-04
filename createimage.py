import numpy as np
import time
import cv2 as cv2

def create_random_image(width, height):
    # Create a random array of pixels
    random_array = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
    # Convert the array to an image
    random_image = cv2.cvtColor(random_array, cv2.COLOR_RGB2BGR)
    return random_image

# function to read all images from a folder
def read_images(folder_name):
    images = []
    for i in range(500):
        img = cv2.imread(f'{folder_name}/{i}.png')
        print(f'Image {i} read')
        images.append(img)
    return images

# Define the image size
image_width = 1920
image_height = 1080


if __name__ == '__main__':
    start = time.time()
    folder_name = 'testdata'
    # for i in range(500):
        # random_img = create_random_image(image_width, image_height)
        # cv2.imwrite(f'{folder_name}/{i}.png', random_img)
    read_images(folder_name)
    print(f'Created {500} images in {time.time() - start} seconds')