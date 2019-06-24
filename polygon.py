def calculate_size(sides):
    if sides == 'Icosahedron':
        return 20
    if sides == 'Cube':
        return 6
    if sides == 'Tetrahedron':
        return 4
    if sides == 'Octahedron':
        return 8
    if sides == 'Dodecahedron':
        return 12
    else:
        return 0


if __name__ == '__main__':
    num = 0
    n = int(input())
    for i in range(n):
        sides = input()
        num += calculate_size(sides)
    print(num)
