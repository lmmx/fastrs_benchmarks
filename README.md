# String colouring speed optimisation benchmarking

Executed with

```sh
for x in *.py; do echo $x; time python $x 2>/dev/null; echo; done 2>&1 | grep -v "user" | grep -v "sys"
```

10 diffs x 12 lines each

```
benchmark_apply_colouring_fastrs_join_strings.py                                    

real    0m0.020s                          

benchmark_apply_colouring_fastrs_join_strings_regex.py                              

real    0m0.021s                          

benchmark_apply_colouring_str_join.py     

real    0m0.028s                          

benchmark_fastrs_join_strings.py          

real    0m0.020s        
```

50 diffs x 12 lines each

```
benchmark_apply_colouring_fastrs_join_strings.py

real    0m0.060s

benchmark_apply_colouring_fastrs_join_strings_regex.py

real    0m0.021s

benchmark_apply_colouring_str_join.py

real    0m0.029s

benchmark_fastrs_join_strings.py

real    0m0.019s
```
