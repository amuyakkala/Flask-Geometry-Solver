from flask import Flask, jsonify, request
import numpy as np
import math

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Geometry Engine!'

# Endpoint to calculate the smallest bounding box for an array of 3D points
@app.route('/smallest_bounding_box', methods=['POST'])
def smallest_bounding_box():
    points = request.get_json()['points']
    min_corner = [min(p[0] for p in points), min(p[1] for p in points), min(p[2] for p in points)]
    max_corner = [max(p[0] for p in points), max(p[1] for p in points), max(p[2] for p in points)]
    output = {
        'min_corner': min_corner,
        'max_corner': max_corner
    }
    return output

# Endpoint to rotate a 3D mesh by a specified angle along a specified axis
@app.route('/rotate_mesh', methods=['POST'])
def rotate_mesh():
    data = request.get_json()
    mesh = data['mesh']
    angle = data['angle']
    axis = data['axis']
    angle_radians = math.radians(angle)
    if axis == 'X':
        rotation_matrix = np.array([[1, 0, 0], [0, round(math.cos(angle_radians), 6), round(math.sin(angle_radians), 6)], [0, round(-math.sin(angle_radians), 6), round(math.cos(angle_radians), 6)]])
    elif axis == 'Y':
        rotation_matrix = np.array([[round(math.cos(angle_radians), 6), 0, round(-math.sin(angle_radians), 6)], [0, 1, 0], [round(math.sin(angle_radians), 6), 0, round(math.cos(angle_radians), 6)]])
    elif axis == 'Z':
        rotation_matrix = np.array([[round(math.cos(angle_radians), 6), round(math.sin(angle_radians), 6), 0], [round(-math.sin(angle_radians), 6), round(math.cos(angle_radians), 6), 0], [0, 0, 1]])
    else:
        raise ValueError("Invalid axis. Must be X, Y, or Z.")
    
    rotated_mesh = []
    for point in mesh:
        rotated_point = np.dot(point, rotation_matrix)
        rotated_mesh.append(rotated_point.tolist())
    
    return {'mesh': rotated_mesh}

# Endpoint to move a 3D mesh by specified units along X, Y, and Z axes
@app.route('/move_mesh', methods=['POST'])
def move_mesh():
    data = request.get_json()
    mesh = data['mesh']
    x = data['x']
    y = data['y']
    z = data['z']
    moved_mesh = [[point[0] + x, point[1] + y, point[2] + z] for point in mesh]
    return {'mesh': moved_mesh}

# Endpoint to check if a polygon represented by 3D points is convex
@app.route('/check_convex_polygon', methods=['POST'])
def check_convex_polygon():
    points = request.get_json()['points']
    if len(points) < 3:
        raise ValueError("Polygon must have at least 3 points.")
    
    for i in range(len(points)):
        p1 = np.array(points[i])
        p2 = np.array(points[(i + 1) % len(points)])
        p3 = np.array(points[(i + 2) % len(points)])
        edge1 = p2 - p1
        edge2 = p3 - p2
        cross_product = np.cross(edge1, edge2)
        if np.dot(cross_product, [0, 0, 1]) < 0:
            return {'is_convex': False}
    
    return {'is_convex': True}

if __name__ == '__main__':
    app.run(debug=True)
