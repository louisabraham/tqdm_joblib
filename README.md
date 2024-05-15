# `tqdm_joblib`

Simple snippet copied from https://stackoverflow.com/a/58936697/5133167 packaged for simple reuse.

# Usage

```py
from math import sqrt
from joblib import Parallel, delayed
from tqdm_joblib import tqdm_joblib
from tqdm_joblib import ParallelPbar

with tqdm_joblib(desc="My calculation", total=10) as progress_bar:
    Parallel(n_jobs=16)(delayed(sqrt)(i**2) for i in range(10))

# or

ParallelPbar("My calculation")(n_jobs=16)(
    delayed(sqrt)(i**2) for i in range(10)
)
```

Distributed under CC BY-SA 4.0.
