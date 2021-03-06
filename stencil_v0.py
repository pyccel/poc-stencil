# ==========================================================================
def dot_1(mat: "float[:,:,:,:,:,:]", x: "float[:,:,:]", out: "float[:,:,:]",
        n1: int, n2: int, n3: int,
        p1: int, p2: int, p3: int):

    #$ omp parallel default(private) shared(mat,x,out) firstprivate( n1, n2, n3)

    #$ omp for schedule(static) collapse(3) nowait
    for i1 in range(0, n1, 1):
        for i2 in range(0, n2, 1):
            for i3 in range(0, n3, 1):
                v = 0.0
                for k1 in range(0, 3, 1):
                    for k2 in range(0, 3, 1):
                        for k3 in range(0, 3, 1):
                            v += mat[1 + i1,1 + i2,1 + i3,k1,k2,k3]*x[i1 + k1,i2 + k2,i3 + k3]
                out[1 + i1,1 + i2,1 + i3] = v

    #$ omp end parallel
    return
def dot_2(mat: "float[:,:,:,:,:,:]", x: "float[:,:,:]", out: "float[:,:,:]",
        n1: int, n2: int, n3: int,
        p1: int, p2: int, p3: int):

    #$ omp parallel default(private) shared(mat,x,out) firstprivate( n1, n2, n3)

    #$ omp for schedule(static) collapse(3) nowait
    for i1 in range(0, n1, 1):
        for i2 in range(0, n2, 1):
            for i3 in range(0, n3, 1):
                v = 0.0
                for k1 in range(0, 5, 1):
                    for k2 in range(0, 5, 1):
                        for k3 in range(0, 5, 1):
                            v += mat[2 + i1,2 + i2,2 + i3,k1,k2,k3]*x[i1 + k1,i2 + k2,i3 + k3]
                out[2 + i1,2 + i2,2 + i3] = v

    #$ omp end parallel
    return

def dot_3(mat: "float[:,:,:,:,:,:]", x: "float[:,:,:]", out: "float[:,:,:]",
        n1: int, n2: int, n3: int,
        p1: int, p2: int, p3: int):

    #$ omp parallel default(private) shared(mat,x,out) firstprivate( n1, n2, n3)

    #$ omp for schedule(static) collapse(3) nowait
    for i1 in range(0, n1, 1):
        for i2 in range(0, n2, 1):
            for i3 in range(0, n3, 1):
                v = 0.0
                for k1 in range(0, 7, 1):
                    for k2 in range(0, 7, 1):
                        for k3 in range(0, 7, 1):
                            v += mat[3 + i1,3 + i2,3 + i3,k1,k2,k3]*x[i1 + k1,i2 + k2,i3 + k3]
                out[3 + i1,3 + i2,3 + i3] = v

    #$ omp end parallel
    return

def dot_4(mat: "float[:,:,:,:,:,:]", x: "float[:,:,:]", out: "float[:,:,:]",
        n1: int, n2: int, n3: int,
        p1: int, p2: int, p3: int):

    #$ omp parallel default(private) shared(mat,x,out) firstprivate( n1, n2, n3)

    #$ omp for schedule(static) collapse(3) nowait
    for i1 in range(0, n1, 1):
        for i2 in range(0, n2, 1):
            for i3 in range(0, n3, 1):
                v = 0.0
                for k1 in range(0, 9, 1):
                    for k2 in range(0, 9, 1):
                        for k3 in range(0, 9, 1):
                            v += mat[4 + i1,4 + i2,4 + i3,k1,k2,k3]*x[i1 + k1,i2 + k2,i3 + k3]
                out[4 + i1,4 + i2,4 + i3] = v

    #$ omp end parallel
    return

def dot_5(mat: "float[:,:,:,:,:,:]", x: "float[:,:,:]", out: "float[:,:,:]",
        n1: int, n2: int, n3: int,
        p1: int, p2: int, p3: int):

    #$ omp parallel default(private) shared(mat,x,out) firstprivate( n1, n2, n3)

    #$ omp for schedule(static) collapse(3) nowait
    for i1 in range(0, n1, 1):
        for i2 in range(0, n2, 1):
            for i3 in range(0, n3, 1):
                v = 0.0
                for k1 in range(0, 11, 1):
                    for k2 in range(0, 11, 1):
                        for k3 in range(0, 11, 1):
                            v += mat[5 + i1,5 + i2,5 + i3,k1,k2,k3]*x[i1 + k1,i2 + k2,i3 + k3]
                out[5 + i1,5 + i2,5 + i3] = v
    #$ omp end parallel
    return
