# poc-stencil
Investigating performances of Stencil Matrix Operations

In order to run these tests, you need 
- compile the core file (stencil_vx.py) with pyccel
- run the test_stencil.py file

## Compiling the core file with pyccel

run

```shell
pyccel stencil_v0.py --flags="-O3 -march=native -mtune=native -mavx -ffast-math" 
```

## Adding new versions
Whenever you add a new version (**vx**), put it in a new file **stencil_vx.py** then following the same steps as before.
The test_stencil.py file will be unique and should provide an output as a table, for the different versions, flags etc
