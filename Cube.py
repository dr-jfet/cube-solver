from Piece import Piece
from math3d import *
    

class Cube:
    """
    Coordinate system:
      - The middle of cube is [0, 0, 0]
      - Piece coordinates are [x, y, z]
      - x points from middle to F layer
      - y points from middle to R layer
      - z points from middle to U layer
    """
    def __init__(self):
        #self.COLOR_U = '\033[0;34mB\033[m'
        #self.COLOR_F = 'W'
        #self.COLOR_L = '\033[0;37mO\033[m'
        #self.COLOR_R = '\033[0;31mR\033[m'
        #self.COLOR_D = '\033[0;32mG\033[m'
        #self.COLOR_B = '\033[1;33mY\033[m'
        self.COLOR_U = 'W'
        self.COLOR_F = 'G'
        self.COLOR_L = 'O'
        self.COLOR_R = 'R'
        self.COLOR_D = 'Y'
        self.COLOR_B = 'B'
        self.pieces = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    if (i==0 and j==0) or (i==0 and k==0) or (j==0 and k==0):
                        continue
                    self.pieces.append(Piece([i, j, k], []))
        for i in self.pieces:
            if i.pos[2]==1:
                i.color_rotations.append([self.COLOR_U, [0, 0, 1]])
            if i.pos[0]==1:
                i.color_rotations.append([self.COLOR_F, [1, 0, 0]])
            if i.pos[1]==-1:
                i.color_rotations.append([self.COLOR_L, [0, -1, 0]])
            if i.pos[1]==1:
                i.color_rotations.append([self.COLOR_R, [0, 1, 0]])
            if i.pos[2]==-1:
                i.color_rotations.append([self.COLOR_D, [0, 0, -1]])
            if i.pos[0]==-1:
                i.color_rotations.append([self.COLOR_B, [-1, 0, 0]])

    def shuffle(self, moves=[]):
        if moves == []:
            pass
        moves = moves.split(" ")
        for i in moves:
            match i:
                case "F":
                    self.rotate_f()
                case "F2":
                    self.rotate_f()
                    self.rotate_f()
                case "F'":
                    self.rotate_f()
                    self.rotate_f()
                    self.rotate_f()
                case "L":
                    self.rotate_l()
                case "L2":
                    self.rotate_l()
                    self.rotate_l()
                case "L'":
                    self.rotate_l()
                    self.rotate_l()
                    self.rotate_l()
                case "R":
                    self.rotate_r()
                case "R2":
                    self.rotate_r()
                    self.rotate_r()
                case "R'":
                    self.rotate_r()
                    self.rotate_r()
                    self.rotate_r()
                case "U":
                    self.rotate_u()
                case "U2":
                    self.rotate_u()
                    self.rotate_u()
                case "U'":
                    self.rotate_u()
                    self.rotate_u()
                    self.rotate_u()
                case "D":
                    self.rotate_d()
                case "D2":
                    self.rotate_d()
                    self.rotate_d()
                case "D'":
                    self.rotate_d()
                    self.rotate_d()
                    self.rotate_d()
                case "B":
                    self.rotate_b()
                case "B2":
                    self.rotate_b()
                    self.rotate_b()
                case "B'":
                    self.rotate_b()
                    self.rotate_b()
                    self.rotate_b()

    def indexes_u(self):
        ret = []
        for i in range(len(self.pieces)):
            if self.pieces[i].pos[2] == 1:
                ret.append(i)
        return ret

    def indexes_f(self):
        ret = []
        for i in range(len(self.pieces)):
            if self.pieces[i].pos[0] == 1:
                ret.append(i)
        return ret

    def indexes_l(self):
        ret = []
        for i in range(len(self.pieces)):
            if self.pieces[i].pos[1] == -1:
                ret.append(i)
        return ret

    def indexes_r(self):
        ret = []
        for i in range(len(self.pieces)):
            if self.pieces[i].pos[1] == 1:
                ret.append(i)
        return ret

    def indexes_d(self):
        ret = []
        for i in range(len(self.pieces)):
            if self.pieces[i].pos[2] == -1:
                ret.append(i)
        return ret

    def indexes_b(self):
        ret = []
        for i in range(len(self.pieces)):
            if self.pieces[i].pos[0] == -1:
                ret.append(i)
        return ret


    def rotate_u(self):
        for i in self.indexes_u():
            self.pieces[i].pos = vec3_rotate_z(self.pieces[i].pos, 90, True)
            for j in range(len(self.pieces[i].color_rotations)):
                self.pieces[i].color_rotations[j][1] = vec3_rotate_z(self.pieces[i].color_rotations[j][1], 90, True)

    def rotate_f(self):
        for i in self.indexes_f():
            self.pieces[i].pos = vec3_rotate_x(self.pieces[i].pos, -90, True)
            for j in range(len(self.pieces[i].color_rotations)):
                self.pieces[i].color_rotations[j][1] = vec3_rotate_x(self.pieces[i].color_rotations[j][1], -90, True)

    def rotate_l(self):
        for i in self.indexes_l():
            self.pieces[i].pos = vec3_rotate_y(self.pieces[i].pos, 90, True)
            for j in range(len(self.pieces[i].color_rotations)):
                self.pieces[i].color_rotations[j][1] = vec3_rotate_y(self.pieces[i].color_rotations[j][1], 90, True)

    def rotate_r(self):
        for i in self.indexes_r():
            self.pieces[i].pos = vec3_rotate_y(self.pieces[i].pos, -90, True)
            for j in range(len(self.pieces[i].color_rotations)):
                self.pieces[i].color_rotations[j][1] = vec3_rotate_y(self.pieces[i].color_rotations[j][1], -90, True)

    def rotate_d(self):
        for i in self.indexes_d():
            self.pieces[i].pos = vec3_rotate_z(self.pieces[i].pos, -90, True)
            for j in range(len(self.pieces[i].color_rotations)):
                self.pieces[i].color_rotations[j][1] = vec3_rotate_z(self.pieces[i].color_rotations[j][1], -90, True)

    def rotate_b(self):
        for i in self.indexes_b():
            self.pieces[i].pos = vec3_rotate_x(self.pieces[i].pos, 90, True)
            for j in range(len(self.pieces[i].color_rotations)):
                self.pieces[i].color_rotations[j][1] = vec3_rotate_x(self.pieces[i].color_rotations[j][1], 90, True)

    def pos2color(self, pos, dir):
        piece = Piece(None, [])
        ret = None
        for i in self.pieces:
            if i.pos == pos:
                piece = i
                break
        for i in piece.color_rotations:
            if i[1] == dir:
                ret = i[0]
                break
        return ret


    def __str__(self):
        ret = ""
        # Up
        ret += f"        "
        ret += f"{self.pos2color([-1, -1, +1], [+0, +0, +1])} "
        ret += f"{self.pos2color([-1, +0, +1], [+0, +0, +1])} "
        ret += f"{self.pos2color([-1, +1, +1], [+0, +0, +1])} "
        ret += f"\n        "
        ret += f"{self.pos2color([+0, -1, +1], [+0, +0, +1])} "
        ret += f"{self.COLOR_U} "
        ret += f"{self.pos2color([+0, +1, +1], [+0, +0, +1])} "
        ret += f"\n        "
        ret += f"{self.pos2color([+1, -1, +1], [+0, +0, +1])} "
        ret += f"{self.pos2color([+1, +0, +1], [+0, +0, +1])} "
        ret += f"{self.pos2color([+1, +1, +1], [+0, +0, +1])} "
        ret += f"\n\n"

        # Left 1
        ret += f"{self.pos2color([-1, -1, +1], [+0, -1, +0])} "
        ret += f"{self.pos2color([+0, -1, +1], [+0, -1, +0])} "
        ret += f"{self.pos2color([+1, -1, +1], [+0, -1, +0])} "
        # Front 1
        ret += "  "
        ret += f"{self.pos2color([+1, -1, +1], [+1, +0, +0])} "
        ret += f"{self.pos2color([+1, +0, +1], [+1, +0, +0])} "
        ret += f"{self.pos2color([+1, +1, +1], [+1, +0, +0])} "
        # Right 1
        ret += "  "
        ret += f"{self.pos2color([+1, +1, +1], [+0, +1, +0])} "
        ret += f"{self.pos2color([+0, +1, +1], [+0, +1, +0])} "
        ret += f"{self.pos2color([-1, +1, +1], [+0, +1, +0])} "
        # Back 1
        ret += "  "
        ret += f"{self.pos2color([-1, +1, +1], [-1, +0, +0])} "
        ret += f"{self.pos2color([-1, +0, +1], [-1, +0, +0])} "
        ret += f"{self.pos2color([-1, -1, +1], [-1, +0, +0])} "

        ret += f"\n"
        # Left 2
        ret += f"{self.pos2color([-1, -1, +0], [+0, -1, +0])} "
        ret += f"{self.COLOR_L} "
        ret += f"{self.pos2color([+1, -1, +0], [+0, -1, +0])} "
        # Front 2
        ret += "  "
        ret += f"{self.pos2color([+1, -1, +0], [+1, +0, +0])} "
        ret += f"{self.COLOR_F} "
        ret += f"{self.pos2color([+1, +1, +0], [+1, +0, +0])} "
        # Right 2
        ret += "  "
        ret += f"{self.pos2color([+1, +1, +0], [+0, +1, +0])} "
        ret += f"{self.COLOR_R} "
        ret += f"{self.pos2color([-1, +1, +0], [+0, +1, +0])} "
        # Back 2
        ret += "  "
        ret += f"{self.pos2color([-1, +1, +0], [-1, +0, +0])} "
        ret += f"{self.COLOR_B} "
        ret += f"{self.pos2color([-1, -1, +0], [-1, +0, +0])} "

        ret += f"\n"
        # Left 3
        ret += f"{self.pos2color([-1, -1, -1], [+0, -1, +0])} "
        ret += f"{self.pos2color([+0, -1, -1], [+0, -1, +0])} "
        ret += f"{self.pos2color([+1, -1, -1], [+0, -1, +0])} "
        # Front 3
        ret += "  "
        ret += f"{self.pos2color([+1, -1, -1], [+1, +0, +0])} "
        ret += f"{self.pos2color([+1, +0, -1], [+1, +0, +0])} "
        ret += f"{self.pos2color([+1, +1, -1], [+1, +0, +0])} "
        # Right 3
        ret += "  "
        ret += f"{self.pos2color([+1, +1, -1], [+0, +1, +0])} "
        ret += f"{self.pos2color([+0, +1, -1], [+0, +1, +0])} "
        ret += f"{self.pos2color([-1, +1, -1], [+0, +1, +0])} "
        # Back 3
        ret += "  "
        ret += f"{self.pos2color([-1, +1, -1], [-1, +0, +0])} "
        ret += f"{self.pos2color([-1, +0, -1], [-1, +0, +0])} "
        ret += f"{self.pos2color([-1, -1, -1], [-1, +0, +0])} "

        # Down
        ret += f"\n\n"
        ret += f"        "
        ret += f"{self.pos2color([+1, -1, -1], [+0, +0, -1])} "
        ret += f"{self.pos2color([+1, +0, -1], [+0, +0, -1])} "
        ret += f"{self.pos2color([+1, +1, -1], [+0, +0, -1])} "
        ret += f"\n        "
        ret += f"{self.pos2color([+0, -1, -1], [+0, +0, -1])} "
        ret += f"{self.COLOR_D} "
        ret += f"{self.pos2color([+0, +1, -1], [+0, +0, -1])} "
        ret += f"\n        "
        ret += f"{self.pos2color([-1, -1, -1], [+0, +0, -1])} "
        ret += f"{self.pos2color([-1, +0, -1], [+0, +0, -1])} "
        ret += f"{self.pos2color([-1, +1, -1], [+0, +0, -1])} "

        return ret


