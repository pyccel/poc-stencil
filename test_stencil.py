import time
import numpy as np

from stencil_v0 import dot as dot_v0

# ==============================================================
def test_1(n1=100, n2=100, n3=100, p1=4, p2=4, p3=4):
    ps = (p1, p2, p3)
    ns = (n1, n2, n3)
    mat = np.random.random((n1+2*p1,n2+2*p2,n3+2*p3 , 2*p1+1, 2*p2+1, 2*p3+1))
    x   = np.random.random((n1+2*p1,n2+2*p2,n3+2*p3))

    # ... version 0
    out = np.zeros_like(x)

    t1 = time.time()
    dot_v0(mat, x, out, *ns, *ps)
    t2 = time.time()

    print('[v0] CPU Time :', t2-t1)
    # ...

################################################################
if __name__ == '__main__':
    test_1()
