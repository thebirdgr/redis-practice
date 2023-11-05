import numpy as np
import open3d as o3d
import time

def generate_random_point_cloud(num_points):
    # Generating random points within a cube
    points = np.random.rand(num_points, 3)  # Generating points in the range [0, 1) for x, y, z

    # Scale the points to a larger volume or specific dimensions
    # For example, scale points to be in the range [0, 10) for x, y, z
    points = points * 10.0

    return points


# point_cloud = generate_random_point_cloud(num_points)

# Create an Open3D point cloud
# pcd = o3d.geometry.PointCloud()
# pcd.points = o3d.utility.Vector3dVector(point_cloud)

# Save the point cloud as a PCD file
# o3d.io.write_point_cloud("random_point_cloud.pcd", pcd)

# Visualizing the point cloud
# o3d.visualization.draw_geometries([pcd])
# Created point cloud 499 in 18.059847831726074 seconds
if __name__ == '__main__':
    folder_name = 'testdata'
    # Generate a random dense point cloud with 10,000 points
    num_points = 1000000
    start = time.time()
    for i in range(500):
        random_pcd = generate_random_point_cloud(num_points)
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(random_pcd)
        o3d.io.write_point_cloud('testdata/pcd_' + str(i) + '.pcd', pcd)
    print(f'Created point cloud {i} in {time.time() - start} seconds')
