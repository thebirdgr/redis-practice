import numpy as np
import time
import cv2 as cv2

def timer_func(func): 
    # This function shows the execution time of  
    # the function object passed 
    def wrap_func(*args, **kwargs): 
        t1 = time.time() 
        result = func(*args, **kwargs) 
        t2 = time.time() 
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s') 
        return result 
    return wrap_func

@timer_func
def create_random_image(width, height):
    # Create a random array of pixels
    random_array = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
    # Convert the array to an image
    random_image = cv2.cvtColor(random_array, cv2.COLOR_RGB2BGR)
    return random_image

# function to read all images from a folder
@timer_func
def read_images(folder_name):
    images = []
    for i in range(500):
        img = cv2.imread(f'{folder_name}/{i}.png')
        # print(f'Image {i} read')
        images.append(img)
    return images

# Define the image size
image_width = 1920
image_height = 1080


if __name__ == '__main__':
    folder_name = 'testdata'
    for i in range(500):
        random_img = create_random_image(image_width, image_height)
        start = time.time()
        cv2.imwrite(f'{folder_name}/{i}.png', random_img)
        print(f'Created image in {time.time() - start} seconds')
    read_images(folder_name)