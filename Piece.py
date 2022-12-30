

# class Piece:
#     def __init__(self, pos_init):
#         ORIENTATION_INIT_ = [1, 0, 0]
#         self.pos_init = pos_init
#         self.orientation_init = ORIENTATION_INIT_
# 
#         self.pos = pos_init
#         self.orientation = ORIENTATION_INIT_


class Piece:
    """
    self.pos:               3d position vector
    self.color_rotations:   Array of arrays, where tuple's first
                            item is a char that represents color
                            and second item is vec3 pointing to
                            the side that corresponding color is
                            located, example:
                                [['R', [1, 0, 0]], ['Y', [0, 1, 0]]]
    """
    def __init__(self, pos, color_rotations):
        self.pos = pos
        self.color_rotations = color_rotations
        




