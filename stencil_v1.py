from numpy import empty
# ==========================================================================
def dot_1(mat: "float[:,:,:,:,:,:]", x: "float[:,:,:]", out: "float[:,:,:]",
        n1: int, n2: int, n3: int,
        p1: int, p2: int, p3: int):

    #$ omp parallel default(private) shared(mat,x,out) firstprivate( n1, n2, n3)
    xx = empty((3,n2+3,n3+3))

    #$ omp for schedule(static) nowait
    for i1 in range(0, n1, 1):
        xx[:,:,:] = x[i1:i1+3,:,:]
        for i2 in range(0, n2, 1):
            for i3 in range(0, n3, 1):
                v = 0.0
                for k1 in range(0, 3, 1):
                    for k2 in range(0, 3, 1):
                        for k3 in range(0, 3, 1):
                            v += mat[p1 + i1,p2 + i2,p3 + i3,k1,k2,k3]*xx[k1,i2+k2,i3+k3]
                out[p1 + i1,p2 + i2,p3 + i3] = v

    #$ omp end parallel
    return
def dot_2(mat: "float[:,:,:,:,:,:]", x: "float[:,:,:]", out: "float[:,:,:]",
        n1: int, n2: int, n3: int,
        p1: int, p2: int, p3: int):

    #$ omp parallel default(private) shared(mat,x,out) firstprivate( n1, n2, n3)
    xx = empty((5,n2+5,n3+5))

    #$ omp for schedule(static) nowait
    for i1 in range(0, n1, 1):
        xx[:,:,:] = x[i1:i1+5,:,:]
        for i2 in range(0, n2, 1):
            for i3 in range(0, n3, 1):
                v = 0.0
                for k1 in range(0, 5, 1):
                    for k2 in range(0, 5, 1):
                        for k3 in range(0, 5, 1):
                            v += mat[p1 + i1,p2 + i2,p3 + i3,k1,k2,k3]*xx[k1,i2+k2,i3+k3]
                out[p1 + i1,p2 + i2,p3 + i3] = v

    #$ omp end parallel
    return
def dot_3(mat: "float[:,:,:,:,:,:]", x: "float[:,:,:]", out: "float[:,:,:]",
        n1: int, n2: int, n3: int,
        p1: int, p2: int, p3: int):

    #$ omp parallel default(private) shared(mat,x,out) firstprivate( n1, n2, n3)
    xx = empty((7,n2+7,n3+7))

    #$ omp for schedule(static) nowait
    for i1 in range(0, n1, 1):
        xx[:,:,:] = x[i1:i1+7,:,:]
        for i2 in range(0, n2, 1):
            for i3 in range(0, n3, 1):
                v = 0.0
                for k1 in range(0, 7, 1):
                    for k2 in range(0, 7, 1):
                        for k3 in range(0, 7, 1):
                            v += mat[p1 + i1,p2 + i2,p3 + i3,k1,k2,k3]*xx[k1,i2+k2,i3+k3]
                out[p1 + i1,p2 + i2,p3 + i3] = v

    #$ omp end parallel
    return
def dot_4(mat: "float[:,:,:,:,:,:]", x: "float[:,:,:]", out: "float[:,:,:]",
        n1: int, n2: int, n3: int,
        p1: int, p2: int, p3: int):

    #$ omp parallel default(private) shared(mat,x,out) firstprivate( n1, n2, n3)
    xx = empty((9,n2+9,n3+9))

    #$ omp for schedule(static) nowait
    for i1 in range(0, n1, 1):
        xx[:,:,:] = x[i1:i1+9,:,:]
        for i2 in range(0, n2, 1):
            for i3 in range(0, n3, 1):
                v = 0.0
                for k1 in range(0, 9, 1):
                    for k2 in range(0, 9, 1):
                        for k3 in range(0, 9, 1):
                            v += mat[p1 + i1,p2 + i2,p3 + i3,k1,k2,k3]*xx[k1,i2+k2,i3+k3]
                out[p1 + i1,p2 + i2,p3 + i3] = v

    #$ omp end parallel
    return
def dot_5(mat: "float[:,:,:,:,:,:]", x: "float[:,:,:]", out: "float[:,:,:]",
        n1: int, n2: int, n3: int,
        p1: int, p2: int, p3: int):

    #$ omp parallel default(private) shared(mat,x,out) firstprivate( n1, n2, n3)
    xx = empty((11,n2+11,n3+11))

    #$ omp for schedule(static) nowait
    for i1 in range(0, n1, 1):
        xx[:,:,:] = x[i1:i1+11,:,:]
        for i2 in range(0, n2, 1):
            for i3 in range(0, n3, 1):
                v = 0.0
                for k1 in range(0, 11, 1):
                    for k2 in range(0, 11, 1):
                        for k3 in range(0, 11, 1):
                            v += mat[p1 + i1,p2 + i2,p3 + i3,k1,k2,k3]*xx[k1,i2+k2,i3+k3]
                out[p1 + i1,p2 + i2,p3 + i3] = v
    #$ omp end parallel
    return
