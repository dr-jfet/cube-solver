from math import sqrt
from math import pi
from math import sin
from math import cos


def vec3_len(vec3):
    return sqrt(vec3[0]**2 + vec3[1]**2 + vec3[2]**2)

def vec3_add(a, b):
    return [a[0]+b[0], a[1]+b[1], a[2]+b[2]]

def vec3_mul(c, vec3):
    return [c*vec3[0], c*vec3[1], c*vec3[2]]

def vec3_dist(a, b):
    return vec3_len(vec3_add(a, vec3_mul(-1, b)))

def add_mat3(a, b):
    ret = []
    for i in range(3):
        ret.append([])
        for j in range(3):
            ret[i].append([])
            ret[i][j] = a[i][j] + b[i][j]
    return ret

def mat3_row(mat3x3, row_index):
    return mat3x3[row_index]

def mat3_col(mat3x3, col_index):
    return [mat3x3[0][col_index], mat3x3[1][col_index], mat3x3[2][col_index]]

def dot3(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def mat_vec_mul3(mat3x3, vec3, round_answer=False):
    ret = []
    for i in range(3):
        if round_answer:
            ret.append(round(dot3(mat3_row(mat3x3, i), vec3)))
        else:
            ret.append(dot3(mat3_row(mat3x3, i), vec3))
    return ret

def vec3_rotate_x(vec3, deg, round_answer=False):
    rad = deg/180*pi
    rot_mat_x = [[1, 0, 0], [0, cos(rad), -sin(rad)], [0, sin(rad), cos(rad)]]
    if round_answer:
        return mat_vec_mul3(rot_mat_x, vec3, True)
    else:
        return mat_vec_mul3(rot_mat_x, vec3)

def vec3_rotate_y(vec3, deg, round_answer=False):
    rad = deg/180*pi
    rot_mat_x = [[cos(rad), 0, sin(rad)], [0, 1, 0], [-sin(rad), 0, cos(rad)]]
    if round_answer:
        return mat_vec_mul3(rot_mat_x, vec3, True)
    else:
        return mat_vec_mul3(rot_mat_x, vec3)


def vec3_rotate_z(vec3, deg, round_answer=False):
    rad = deg/180*pi
    rot_mat_x = [[cos(rad), -sin(rad), 0], [sin(rad), cos(rad), 0], [0, 0, 1]]
    if round_answer:
        return mat_vec_mul3(rot_mat_x, vec3, True)
    else:
        return mat_vec_mul3(rot_mat_x, vec3)


