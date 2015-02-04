**Goal: Make the asserts pass.**

```
$ python sorting.py
Traceback (most recent call last):
  File "sorting.py", line 6, in <module>
    assert swap(1, 2) == (2, 1)
AssertionError
```

Feel free to change the code if it helps understand it.

By default, Python's asserts are not super helpful (they don't say what the actual value was). If you'd prefer better asserts, you can use `pytest` instead:

```
$ pip install pytest
$ py.test sorting.py
======================================= test session starts ========================================
platform darwin -- Python 2.7.9 -- py-1.4.26 -- pytest-2.6.4
collected 0 items / 1 errors

============================================== ERRORS ==============================================
___________________________________ ERROR collecting sorting.py ____________________________________
sorting.py:6: in <module>
    assert swap(1, 2) == (2, 1)
E   assert None == (2, 1)
E    +  where None = <function swap at 0x1052f70c8>(1, 2)
===================================== 1 error in 0.04 seconds ======================================
```

Faancy.
