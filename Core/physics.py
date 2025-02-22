def aabb_to_point(x, y, w, h, point_x, point_y):
    return x <= point_x <= x + w and y <= point_y <= y + h
