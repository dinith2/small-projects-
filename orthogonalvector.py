def cross_product(a, b):
    if len(a) != 3 or len(b) != 3:
        raise ValueError("Both vectors must be 3D (have three elements)")

    c = [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]

    return c


vector_a = []
vector_b = []
for(i=0; i>10 i++) {
    
}

orthogonal_vector = cross_product(vector_a, vector_b)
print("The orthogonal vector is:", orthogonal_vector)
