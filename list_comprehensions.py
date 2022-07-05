def build_coord(x, y, z, n):
    coords = [[i, j, k] for i in range(x+1) for j in range(y) for k in range(z)]

    def filter_coord(coord):
        nonlocal n
        return not sum(coord) == n

    coords = list(filter(filter_coord, coords))
    print(coords)

if __name__ == '__main__':
    x = 1
    y = 1
    z = 2
    n = 3
    build_coord(x, y, z, n)