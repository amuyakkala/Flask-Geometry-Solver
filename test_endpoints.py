import unittest
import requests

base_url = 'http://127.0.0.1:5000'  # Assuming the service is running locally

class EndpointTests(unittest.TestCase):
    def test_smallest_bounding_box_endpoint(self):
        # Test case for /smallest_bounding_box endpoint
        points = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
        response = requests.post(f'{base_url}/smallest_bounding_box', json={'points': points})
        data = response.json()
        # print(data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['min_corner'], [0, 0, 0])
        self.assertEqual(data['max_corner'], [2, 2, 2])

    def test_rotate_mesh_endpoint(self):
        # Test case for /rotate_mesh endpoint
        mesh = [[0, 0, 0], [1, 0, 0], [1, 1, 0]]
        response = requests.post(f'{base_url}/rotate_mesh', json={'mesh': mesh, 'angle': 90, 'axis': 'Z'})
        data = response.json()
        expected_rotated_mesh = [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [-1.0, 1.0, 0.0]]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['mesh'], expected_rotated_mesh)

    def test_move_mesh_endpoint(self):
        # Test case for /move_mesh endpoint
        mesh = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
        response = requests.post(f'{base_url}/move_mesh', json={'mesh': mesh, 'x': 2, 'y': -1, 'z': 3})
        data = response.json()
        expected_rotated_mesh = [[3, 1, 6],
                                [6, 4, 9],
                                [9, 7, 12]]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['mesh'], expected_rotated_mesh)
    
    def test_check_convex_polygon_endpoint(self):
        # Test case for /check_convex_polygon endpoint
        mesh = [[0, 0, 0],
                [2, 0, 0],
                [3, 1, 0],
                [2, 2, 0],
                [0, 2, 0]]
        response = requests.post(f'{base_url}/check_convex_polygon', json={'points': mesh})
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['is_convex'], True)

if __name__ == '__main__':
    unittest.main()
