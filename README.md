# String colouring speed optimisation benchmarking

Benchmarked on:
- 10 diffs x 12 lines each
- 50 diffs x 12 lines each

| Benchmark Script Name                     | 10 Diffs Execution Time (s) | 50 Diffs Execution Time (s) |
|-------------------------------------------|-----------------------------|-----------------------------|
| apply_colouring_fastrs_join_strings       |           0.020             |           0.060             |
| apply_colouring_fastrs_join_strings_regex |           0.021             |           0.021             |
| apply_colouring_str_join                  |           0.028             |           0.029             |
| fastrs_join_strings                       |           0.020             |           0.019             |

## Reproduction

Executed in the `10` and `50` subdirectories with:

```sh
for x in *.py; do echo $x; time python $x 2>/dev/null; echo; done 2>&1 | grep -v "user" | grep -v "sys"
```

