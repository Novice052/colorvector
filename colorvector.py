# Generate n colors along a vector

def get_vector(a, b):
    """Given two points (3D), Returns the common vector"""
    vector = ((b[0] - a[0]), (b[1] - a[1]), (b[2] - a[2]))
    return vector


def get_t(n):
    if n <= 2:
        return [0, 1]
    else:
        t = []
        for i in range(n):
            if i == 0:
                t.append(0)
                i += 1
            elif i < n - 1:
                t.append(1/(n - 1) * i)
                i += 1
            else:
                t.append(1)
                i += 1
        return t


def get_palette(a, b, n):
    vector = get_vector(a, b)
    t = get_t(n)
    palette = []
    for i in range(n):
        scalar = ((t[i] * vector[0]), (t[i] * vector[1]), (t[i] * vector[2]))
        palette.append((round(scalar[0] + a[0]), round(scalar[1] + a[1]), round(scalar[2] + a[2])))
    return palette


print(get_palette((0, 0, 0), (239, 107, 252), 5))
