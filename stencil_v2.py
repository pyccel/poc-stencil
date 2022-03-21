from numpy import empty

def dot_1(mat: "float[:,:,:,:,:,:]", x: "float[:,:,:]", out: "float[:,:,:]",
        n1: int, n2: int, n3: int,
        p1: int, p2: int, p3: int, bls:int):

    #$ omp parallel default(private) shared(mat,x,out) firstprivate( n1, n2, n3, bls)
    xx     = empty((2+bls,2+bls,2+bls))
    v      = empty((bls,bls,bls))

    #$ omp for schedule(static) collapse(3) nowait
    for i_outer_1 in range(0, n1//bls, 1):
        for i_outer_2 in range(0, n2//bls, 1):
            for i_outer_3 in range(0, n3//bls, 1):
                xx[:,:,:]  = x[i_outer_1*bls:i_outer_1*bls+2+bls,i_outer_2*bls:i_outer_2*bls+2+bls,i_outer_3*bls:i_outer_3*bls+2+bls]
                v[:,:,:]   = 0.
                for i_inner_1 in range(0, bls, 1):
                    i1 = i_outer_1*bls + i_inner_1
                    for i_inner_2 in range(0, bls, 1):
                        i2 = i_outer_2*bls + i_inner_2
                        for i_inner_3 in range(0, bls, 1):
                            i3 = i_outer_3*bls + i_inner_3
                            for k1 in range(0, 3, 1):
                                for k2 in range(0, 3, 1):
                                    for k3 in range(0, 3, 1):
                                        v[i_inner_1, i_inner_2, i_inner_3] += mat[1+i1,1+i2, 1+i3,k1,k2,k3]*xx[i_inner_1+k1,i_inner_2+k2,i_inner_3+k3]

                out[1 + i_outer_1*bls:1+i_outer_1*bls+bls,1 + i_outer_2*bls:1+i_outer_2*bls+bls,1 + i_outer_3*bls:1+i_outer_3*bls+bls] = v[:,:,:]

#    #$ omp for schedule(static) collapse(3) nowait
#    for i1 in range((n1//bls)*bls, n1, 1):
#        for i2 in range(0, n2, 1):
#            for i3 in range(0, n3, 1):
#                vv   = 0.
#                for k1 in range(0, 3, 1):
#                    for k2 in range(0, 3, 1):
#                        for k3 in range(0, 3, 1):
#                            vv += mat[1+i1,1+i2, 1+i3,k1,k2,k3]*x[i1+k1,i2+k2,i3+k3]

#                out[1+i1,1+i2,1+i3] = vv

#    #$ omp for schedule(static) collapse(3) nowait
#    for i1 in range(0, (n1//bls)*bls, 1):
#        for i2 in range((n2//bls)*bls, n2, 1):
#            for i3 in range(0, n3, 1):
#                vv   = 0.
#                for k1 in range(0, 3, 1):
#                    for k2 in range(0, 3, 1):
#                        for k3 in range(0, 3, 1):
#                            vv += mat[1+i1,1+i2, 1+i3,k1,k2,k3]*x[i1+k1,i2+k2,i3+k3]

#                out[1+i1,1+i2,1+i3] = vv

#    #$ omp for schedule(static) collapse(3) nowait
#    for i1 in range(0, (n1//bls)*bls, 1):
#        for i2 in range(0, (n2//bls)*bls, 1):
#            for i3 in range((n3//bls)*bls, n3, 1):
#                vv   = 0.
#                for k1 in range(0, 3, 1):
#                    for k2 in range(0, 3, 1):
#                        for k3 in range(0, 3, 1):
#                            vv += mat[1+i1,1+i2, 1+i3,k1,k2,k3]*x[i1+k1,i2+k2,i3+k3]

#                out[1+i1,1+i2,1+i3] = vv

    #$ omp end parallel
    return
def dot_2(mat: "float[:,:,:,:,:,:]", x: "float[:,:,:]", out: "float[:,:,:]",
        n1: int, n2: int, n3: int,
        p1: int, p2: int, p3: int, bls:int):

    #$ omp parallel default(private) shared(mat,x,out) firstprivate( n1, n2, n3, bls)

    xx     = empty((4+bls,4+bls,4+bls))
    v      = empty((bls,bls,bls))

    #$ omp for schedule(static) collapse(3) nowait
    for i_outer_1 in range(0, n1//bls, 1):
        for i_outer_2 in range(0, n2//bls, 1):
            for i_outer_3 in range(0, n3//bls, 1):
                xx[:,:,:]  = x[i_outer_1*bls:i_outer_1*bls+4+bls,i_outer_2*bls:i_outer_2*bls+4+bls,i_outer_3*bls:i_outer_3*bls+4+bls]
                v[:,:,:]   = 0.
                for i_inner_1 in range(0, bls, 1):
                    i1 = i_outer_1*bls + i_inner_1
                    for i_inner_2 in range(0, bls, 1):
                        i2 = i_outer_2*bls + i_inner_2
                        for i_inner_3 in range(0, bls, 1):
                            i3 = i_outer_3*bls + i_inner_3
                            for k1 in range(0, 5, 1):
                                for k2 in range(0, 5, 1):
                                    for k3 in range(0, 5, 1):
                                        v[i_inner_1, i_inner_2, i_inner_3] += mat[2+i1,2+i2,2+i3,k1,k2,k3]*xx[i_inner_1+k1,i_inner_2+k2,i_inner_3+k3]

                out[2 + i_outer_1*bls:2+i_outer_1*bls+bls,2 + i_outer_2*bls:2+i_outer_2*bls+bls,2 + i_outer_3*bls:2+i_outer_3*bls+bls] = v[:,:,:]

#    #$ omp for schedule(static) collapse(3) nowait
#    for i1 in range((n1//bls)*bls, n1, 1):
#        for i2 in range(0, n2, 1):
#            for i3 in range(0, n3, 1):
#                vv   = 0.
#                for k1 in range(0, 5, 1):
#                    for k2 in range(0, 5, 1):
#                        for k3 in range(0, 5, 1):
#                            vv += mat[2+i1,2+i2,2+i3,k1,k2,k3]*x[i1+k1,i2+k2,i3+k3]

#                out[2+i1,2+i2,2+i3] = vv

#    #$ omp for schedule(static) collapse(3) nowait
#    for i1 in range(0, (n1//bls)*bls, 1):
#        for i2 in range((n2//bls)*bls, n2, 1):
#            for i3 in range(0, n3, 1):
#                vv   = 0.
#                for k1 in range(0, 5, 1):
#                    for k2 in range(0, 5, 1):
#                        for k3 in range(0, 5, 1):
#                            vv += mat[2+i1,2+i2,2+i3,k1,k2,k3]*x[i1+k1,i2+k2,i3+k3]

#                out[2+i1,2+i2,2+i3] = vv

#    #$ omp for schedule(static) collapse(3) nowait
#    for i1 in range(0, (n1//bls)*bls, 1):
#        for i2 in range(0, (n2//bls)*bls, 1):
#            for i3 in range((n3//bls)*bls, n3, 1):
#                vv   = 0.
#                for k1 in range(0, 5, 1):
#                    for k2 in range(0, 5, 1):
#                        for k3 in range(0, 5, 1):
#                            vv += mat[2+i1,2+i2,2+i3,k1,k2,k3]*x[i1+k1,i2+k2,i3+k3]

#                out[2+i1,2+i2,2+i3] = vv

    #$ omp end parallel
    return

@stack_array("xx, v")
def dot_3(mat: "float[:,:,:,:,:,:]", x: "float[:,:,:]", out: "float[:,:,:]",
        n1: int, n2: int, n3: int,
        p1: int, p2: int, p3: int, bls:int):

    #$ omp parallel default(private) shared(mat,x,out) firstprivate( n1, n2, n3, bls)
    xx     = empty((6+bls,6+bls,6+bls))
    v      = empty((bls,bls,bls))
    xx2    = empty((7,n2+7,n3+7))

    #$ omp for schedule(static) collapse(3) nowait
    for i_outer_1 in range(0, n1//bls, 1):
        for i_outer_2 in range(0, n2//bls, 1):
            for i_outer_3 in range(0, n3//bls, 1):
                xx[:,:,:]  = x[i_outer_1*bls:i_outer_1*bls+6+bls,i_outer_2*bls:i_outer_2*bls+6+bls,i_outer_3*bls:i_outer_3*bls+6+bls]
                v[:,:,:]   = 0.
                for i_inner_1 in range(0, bls, 1):
                    i1 = i_outer_1*bls + i_inner_1
                    for i_inner_2 in range(0, bls, 1):
                        i2 = i_outer_2*bls + i_inner_2
                        for i_inner_3 in range(0, bls, 1):
                            i3 = i_outer_3*bls + i_inner_3
                            for k1 in range(0, 7, 1):
                                for k2 in range(0, 7, 1):
                                    for k3 in range(0, 7, 1):
                                        v[i_inner_1, i_inner_2, i_inner_3] += mat[3+i1,3+i2,3+i3,k1,k2,k3]*xx[i_inner_1+k1,i_inner_2+k2,i_inner_3+k3]

                out[3 + i_outer_1*bls:3+i_outer_1*bls+bls,3 + i_outer_2*bls:3+i_outer_2*bls+bls,3 + i_outer_3*bls:3+i_outer_3*bls+bls] = v[:,:,:]

#    #$ omp for schedule(static) nowait
#    for i1 in range((n1//bls)*bls, n1, 1):
#        xx2[:,:,:] = x[i1:i1+7,:,:]
#        for i2 in range(0, n2, 1):
#            for i3 in range(0, n3, 1):
#                vv   = 0.
#                for k1 in range(0, 7, 1):
#                    for k2 in range(0, 7, 1):
#                        for k3 in range(0, 7, 1):
#                            vv += mat[3+i1,3+i2,3+i3,k1,k2,k3]*xx2[k1,i2+k2,i3+k3]

#                out[3+i1,3+i2,3+i3] = vv

#    #$ omp for schedule(static) nowait
#    for i1 in range(0, (n1//bls)*bls, 1):
#        xx2[:,:,:] = x[i1:i1+7,:,:]
#        for i2 in range((n2//bls)*bls, n2, 1):
#            for i3 in range(0, n3, 1):
#                vv   = 0.
#                for k1 in range(0, 7, 1):
#                    for k2 in range(0, 7, 1):
#                        for k3 in range(0, 7, 1):
#                            vv += mat[3+i1,3+i2,3+i3,k1,k2,k3]*xx2[k1,i2+k2,i3+k3]

#                out[3+i1,3+i2,3+i3] = vv

#    #$ omp for schedule(static) nowait
#    for i1 in range(0, (n1//bls)*bls, 1):
#        xx2[:,:,:] = x[i1:i1+7,:,:]
#        for i2 in range(0, (n2//bls)*bls, 1):
#            for i3 in range((n3//bls)*bls, n3, 1):
#                vv   = 0.
#                for k1 in range(0, 7, 1):
#                    for k2 in range(0, 7, 1):
#                        for k3 in range(0, 7, 1):
#                            vv += mat[3+i1,3+i2,3+i3,k1,k2,k3]*xx2[k1,i2+k2,i3+k3]

#                out[3+i1,3+i2,3+i3] = vv

    #$ omp end parallel
    return

def dot_4(mat: "float[:,:,:,:,:,:]", x: "float[:,:,:]", out: "float[:,:,:]",
        n1: int, n2: int, n3: int,
        p1: int, p2: int, p3: int, bls:int):

    #$ omp parallel default(private) shared(mat,x,out) firstprivate( n1, n2, n3, bls)
    xx     = empty((8+bls,8+bls,8+bls))
    v      = empty((bls,bls,bls))

    #$ omp for schedule(static) collapse(3) nowait
    for i_outer_1 in range(0, n1//bls, 1):
        for i_outer_2 in range(0, n2//bls, 1):
            for i_outer_3 in range(0, n3//bls, 1):
                xx[:,:,:]  = x[i_outer_1*bls:i_outer_1*bls+8+bls,i_outer_2*bls:i_outer_2*bls+8+bls,i_outer_3*bls:i_outer_3*bls+8+bls]
                v[:,:,:]   = 0.
                for i_inner_1 in range(0, bls, 1):
                    i1 = i_outer_1*bls + i_inner_1
                    for i_inner_2 in range(0, bls, 1):
                        i2 = i_outer_2*bls + i_inner_2
                        for i_inner_3 in range(0, bls, 1):
                            i3 = i_outer_3*bls + i_inner_3
                            for k1 in range(0, 9, 1):
                                for k2 in range(0, 9, 1):
                                    for k3 in range(0, 9, 1):
                                        v[i_inner_1, i_inner_2, i_inner_3] += mat[4+i1,4+i2,4+i3,k1,k2,k3]*xx[i_inner_1+k1,i_inner_2+k2,i_inner_3+k3]

                out[4 + i_outer_1*bls:4+i_outer_1*bls+bls,4 + i_outer_2*bls:4+i_outer_2*bls+bls,4 + i_outer_3*bls:4+i_outer_3*bls+bls] = v[:,:,:]

#    #$ omp for schedule(static) collapse(3) nowait
#    for i1 in range((n1//bls)*bls, n1, 1):
#        for i2 in range(0, n2, 1):
#            for i3 in range(0, n3, 1):
#                vv   = 0.
#                for k1 in range(0, 9, 1):
#                    for k2 in range(0, 9, 1):
#                        for k3 in range(0, 9, 1):
#                            vv += mat[4+i1,4+i2, 4+i3,k1,k2,k3]*x[i1+k1,i2+k2,i3+k3]

#                out[4+i1,4+i2,4+i3] = vv

#    #$ omp for schedule(static) collapse(3) nowait
#    for i1 in range(0, (n1//bls)*bls, 1):
#        for i2 in range((n2//bls)*bls, n2, 1):
#            for i3 in range(0, n3, 1):
#                vv   = 0.
#                for k1 in range(0, 9, 1):
#                    for k2 in range(0, 9, 1):
#                        for k3 in range(0, 9, 1):
#                            vv += mat[4+i1,4+i2, 4+i3,k1,k2,k3]*x[i1+k1,i2+k2,i3+k3]

#                out[4+i1,4+i2,4+i3] = vv

#    #$ omp for schedule(static) collapse(3) nowait
#    for i1 in range(0, (n1//bls)*bls, 1):
#        for i2 in range(0, (n2//bls)*bls, 1):
#            for i3 in range((n3//bls)*bls, n3, 1):
#                vv   = 0.
#                for k1 in range(0, 9, 1):
#                    for k2 in range(0, 9, 1):
#                        for k3 in range(0, 9, 1):
#                            vv += mat[4+i1,4+i2, 4+i3,k1,k2,k3]*x[i1+k1,i2+k2,i3+k3]

#                out[4+i1,4+i2,4+i3] = vv

    #$ omp end parallel
    return
def dot_5(mat: "float[:,:,:,:,:,:]", x: "float[:,:,:]", out: "float[:,:,:]",
        n1: int, n2: int, n3: int,
        p1: int, p2: int, p3: int, bls:int):

    #$ omp parallel default(private) shared(mat,x,out) firstprivate( n1, n2, n3, bls)
    xx     = empty((10+bls,10+bls,10+bls))
    v      = empty((bls,bls,bls))

    #$ omp for schedule(static) collapse(3) nowait
    for i_outer_1 in range(0, n1//bls, 1):
        for i_outer_2 in range(0, n2//bls, 1):
            for i_outer_3 in range(0, n3//bls, 1):
                xx[:,:,:]  = x[i_outer_1*bls:i_outer_1*bls+10+bls,i_outer_2*bls:i_outer_2*bls+10+bls,i_outer_3*bls:i_outer_3*bls+10+bls]
                v[:,:,:]   = 0.
                for i_inner_1 in range(0, bls, 1):
                    i1 = i_outer_1*bls + i_inner_1
                    for i_inner_2 in range(0, bls, 1):
                        i2 = i_outer_2*bls + i_inner_2
                        for i_inner_3 in range(0, bls, 1):
                            i3 = i_outer_3*bls + i_inner_3
                            for k1 in range(0, 11, 1):
                                for k2 in range(0, 11, 1):
                                    for k3 in range(0, 11, 1):
                                        v[i_inner_1, i_inner_2, i_inner_3] += mat[5+i1,5+i2,5+i3,k1,k2,k3]*xx[i_inner_1+k1,i_inner_2+k2,i_inner_3+k3]

                out[5 + i_outer_1*bls:5+i_outer_1*bls+bls,5 + i_outer_2*bls:5+i_outer_2*bls+bls,5 + i_outer_3*bls:5+i_outer_3*bls+bls] = v[:,:,:]

#    #$ omp for schedule(static) collapse(3) nowait
#    for i1 in range((n1//bls)*bls, n1, 1):
#        for i2 in range(0, n2, 1):
#            for i3 in range(0, n3, 1):
#                vv   = 0.
#                for k1 in range(0, 11, 1):
#                    for k2 in range(0, 11, 1):
#                        for k3 in range(0, 11, 1):
#                            vv += mat[5+i1,5+i2,5+i3,k1,k2,k3]*x[i1+k1,i2+k2,i3+k3]

#                out[5+i1,5+i2,5+i3] = vv

#    #$ omp for schedule(static) collapse(3) nowait
#    for i1 in range(0, (n1//bls)*bls, 1):
#        for i2 in range((n2//bls)*bls, n2, 1):
#            for i3 in range(0, n3, 1):
#                vv   = 0.
#                for k1 in range(0, 11, 1):
#                    for k2 in range(0, 11, 1):
#                        for k3 in range(0, 11, 1):
#                            vv += mat[5+i1,5+i2,5+i3,k1,k2,k3]*x[i1+k1,i2+k2,i3+k3]

#                out[5+i1,5+i2,5+i3] = vv

#    #$ omp for schedule(static) collapse(3) nowait
#    for i1 in range(0, (n1//bls)*bls, 1):
#        for i2 in range(0, (n2//bls)*bls, 1):
#            for i3 in range((n3//bls)*bls, n3, 1):
#                vv   = 0.
#                for k1 in range(0, 11, 1):
#                    for k2 in range(0, 11, 1):
#                        for k3 in range(0, 11, 1):
#                            vv += mat[5+i1,5+i2,5+i3,k1,k2,k3]*x[i1+k1,i2+k2,i3+k3]

#                out[5+i1,5+i2,5+i3] = vv
    #$ omp end parallel
    return
