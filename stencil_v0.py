# ==========================================================================
def dot(mat: "float[:,:,:,:,:,:]", x: "float[:,:,:]", out: "float[:,:,:]",
        n1: int, n2: int, n3: int,
        p1: int, p2: int, p3: int):

    for i1 in range(0, n1, 1):
        for i2 in range(0, n2, 1):
            for i3 in range(0, n3, 1):
                v = 0.0
                for k1 in range(0, 2*p1+1, 1):
                    for k2 in range(0, 2*p2+1, 1):
                        for k3 in range(0, 2*p3+1, 1):
                            v += mat[p1 + i1,p2 + i2,p3 + i3,k1,k2,k3]*x[i1 + k1,i2 + k2,i3 + k3]
                out[p1 + i1,p2 + i2,p3 + i3] = v
