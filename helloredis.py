# python script to test redis connection
import redis
import cv2 as cv2
import time
from createimage import create_random_image
import numpy as np


def save_image_to_redis(redis_conn, key, image):
    # Convert the OpenCV image to a byte buffer
    success, img_buffer = cv2.imencode('.jpg', image)
    if success:
        # Save the image buffer to Redis
        redis_conn.set(key, img_buffer.tobytes())
        print(f"Image saved to Redis with key: {key}")
    else:
        print("Failed to encode the image.")

# function to read all images from redis server

def read_image_from_redis(redis_conn, key):
    # Retrieve the image data from Redis
    img_data = redis_conn.get(key)
    
    if img_data:
        # Convert the image data back to a NumPy array
        nparr = np.frombuffer(img_data, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        print(f"Image retrieved from Redis with key: {key}")
        return img_np
    else:
        print(f"No image found in Redis with key: {key}")
        return None

if __name__ == '__main__':
    r = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=False)
    folder_name = 'testdata'
    # images = read_images(folder_name)
    count = 500
    start = time.time()
    for i in range(count):
        random_img = create_random_image(1920, 1080)
        save_image_to_redis(r, f'image_{i}', random_img)
    print(f'Uploaded {count} images in {time.time() - start} seconds')
    start = time.time()
    for i in range(count):
        read_image_from_redis(r, f'image_{i}')
    print(f'Retrieved {count} images in {time.time() - start} seconds')