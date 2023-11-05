# python script to test redis connection
import redis
import cv2 as cv2
import time
from createimage import create_random_image
from generatepcd import generate_random_point_cloud
import numpy as np

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
def save_image_to_redis(redis_conn, key, image):
    # Convert the OpenCV image to a byte buffer
    start = time.time()
    success, img_buffer = cv2.imencode('.jpg', image)
    print(f'Encoded image in {time.time() - start} seconds')
    if success:
        # Save the image buffer to Redis
        redis_conn.set(key, img_buffer.tobytes())
        # redis_conn.set(key, img_buffer)
        print(f"Image saved to Redis with key: {key}")
    else:
        print("Failed to encode the image.")

# function to read all images from redis server
@timer_func
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
    # start_ = time.time()
    # for i in range(count):
    #     random_img = create_random_image(1920, 1080)
    #     save_image_to_redis(r, f'image_{i}', random_img)
    # end_time_ = time.time()
    # start = time.time()
    # for i in range(count):
    #     read_image_from_redis(r, f'image_{i}')
    # end_time = time.time()
    # print(f'Uploaded {count} images in {end_time_ - start_} seconds')
    # print(f'Retrieved {count} images in {end_time - start} seconds')
    # generate pcd
    start_ = time.time()
    for i in range(count):
        random_pcd = generate_random_point_cloud(1000000)
        r.set(f'pcd_{i}', random_pcd.tobytes())
    end_time_ = time.time()
    start = time.time()
    for i in range(count):
        pcd = r.get(f'pcd_{i}')
        nparr = np.frombuffer(pcd, np.float64)
        pcd_np = nparr.reshape(-1, 3)
    end_time = time.time()
    print(f'Uploaded {count} pcds in {end_time_ - start_} seconds')
    print(f'Retrieved {count} pcds in {end_time - start} seconds')