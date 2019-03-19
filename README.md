# Framework to generate a bug in LassoLarsCV

```
cd autofeat
python3.6 -m pip install .
python3.6 generate_error.py
```

This will cause LassoLarsCV to fail:

```
During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "generate_error.py", line 19, in <module>
    reg.fit(X, target)
  File "/home/felix/Software/fork_autofeat/venv/lib/python3.6/site-packages/sklearn/linear_model/least_angle.py", line 1187, in fit
    Xy=None, fit_path=True)
  File "/home/felix/Software/fork_autofeat/venv/lib/python3.6/site-packages/sklearn/linear_model/least_angle.py", line 647, in _fit
    return_n_iter=True, positive=self.positive)
  File "/home/felix/Software/fork_autofeat/venv/lib/python3.6/site-packages/sklearn/linear_model/least_angle.py", line 380, in lars_path
    g1 = arrayfuncs.min_pos((C - Cov) / (AA - corr_eq_dir + tiny32))
ValueError: operands could not be broadcast together with shapes (37,) (36,) 
```
