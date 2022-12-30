#!/usr/bin/env python3
from Cube import Cube

def main():
    cube = Cube()
    cube.shuffle("F' L' B' L2 D2 R F' D2 R' F2 R F2 R2 B2 D2 R D2 L2")
    print(cube)

if __name__ == "__main__":
    main()

