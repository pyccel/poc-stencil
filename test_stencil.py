import time
import numpy as np

from stencil_v0 import dot_1 as dot_1_v0, dot_2 as dot_2_v0, dot_3 as dot_3_v0, dot_4 as dot_4_v0, dot_5 as dot_5_v0
from stencil_v1 import dot_1 as dot_1_v1, dot_2 as dot_2_v1, dot_3 as dot_3_v1, dot_4 as dot_4_v1, dot_5 as dot_5_v1
from stencil_v2 import dot_1 as dot_1_v2, dot_2 as dot_2_v2, dot_3 as dot_3_v2, dot_4 as dot_4_v2, dot_5 as dot_5_v2

def select_dot_v0(p):
    if p==1:
        return dot_1_v0
    elif p==2:
        return dot_2_v0
    elif p==3:
        return dot_3_v0
    elif p==4:
        return dot_4_v0
    elif p==5:
        return dot_5_v0
    else:
        raise ValueError("not available")

def select_dot_v1(p):
    if p==1:
        return dot_1_v1
    elif p==2:
        return dot_2_v1
    elif p==3:
        return dot_3_v1
    elif p==4:
        return dot_4_v1
    elif p==5:
        return dot_5_v1
    else:
        raise ValueError("not available")

def select_dot_v2(p):
    if p==1:
        return dot_1_v2
    elif p==2:
        return dot_2_v2
    elif p==3:
        return dot_3_v2
    elif p==4:
        return dot_4_v2
    elif p==5:
        return dot_5_v2
    else:
        raise ValueError("not available")
# ==============================================================
def test_1(n, p):
    dot_v0 = select_dot_v0(p)
    dot_v1 = select_dot_v1(p)
    dot_v2 = select_dot_v2(p)

    p1, p2, p3 = p, p, p
    n1, n2, n3 = n, n, n

    ps = (p1, p2, p3)
    ns = (n1, n2, n3)
    mat = np.random.random((n1+2*p1,n2+2*p2,n3+2*p3 , 2*p1+1, 2*p2+1, 2*p3+1))
    x   = np.random.random((n1+2*p1,n2+2*p2,n3+2*p3))

    # ... version 0
    out = np.zeros_like(x)

    t1 = time.time()
    dot_v0(mat, x, out, *ns, *ps)
    t2 = time.time()

    time_dot_v0 = t2-t1
    # ...

    # ... version 1
    out1 = np.zeros_like(x)

    t1 = time.time()
    dot_v1(mat, x, out1, *ns, *ps)
    t2 = time.time()

    time_dot_v1 = t2-t1
    # ...

    # ... version 2
    out2        = np.zeros_like(x)
    time_dot_v2 = 1000
    block_len   = -1
    for bls in range(1, min(20,n)):
        if abs(n//bls-n/bls)>1e-10:continue

        out2[:,:,:] = 0.
        t1 = time.time()
        dot_v2(mat, x, out2, *ns, *ps, bls)
        t2 = time.time()
        T = t2-t1

        if not abs(out-out2).max()<1e-11:
            print(abs(out-out2).max())
            raise ValueError("wrong result")

        if T<time_dot_v2:
            time_dot_v2 = T
            block_len   = bls

    # ...

#    print('[v0] CPU Time :', time_dot_v0)
#    print('[v1] CPU Time :', time_dot_v1)
#    print('[v2] CPU Time :', time_dot_v2)

    return time_dot_v0, time_dot_v1, time_dot_v2

################################################################
if __name__ == '__main__':
    ps           = [1,2,3,4,5]
    ns           = [10,20,30,40,50,60,70,80,90]
    nversions    = 3
    times = [np.zeros((len(ps),len(ns))) for i in range(nversions)]

    for i,p in enumerate(ps):
        for j,n in enumerate(ns):
            timmings = test_1(n,p)
            for k,T in enumerate(timmings):
                times[k][i,j] = T

    from tabulate import tabulate
    headers = [""] + ["{}**3".format(ni) for ni in ns]

    for i,T in enumerate(times):
        T = T.tolist()
        T = [["p={}".format(pi)] + ti for pi,ti in zip(ps,T)]
        print("="*45,"Timings of dot product version {}".format(i), "="*45)
        print(tabulate(T, headers=headers, tablefmt="grid"))
        print("\n")

    for i,T in enumerate(times):
        if i==0:continue
        T = (times[0]/T).tolist()
        T = [["p={}".format(pi)] + ti for pi,ti in zip(ps,T)]
        print("="*34," Speedup of dot product version {} ".format(i), "="*34)
        print(tabulate(T, headers=headers, tablefmt="grid"))
        print("\n")
