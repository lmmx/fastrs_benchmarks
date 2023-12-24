# String colouring speed optimisation benchmarking

Benchmarked on:
- 10 diffs x 12 lines each
- 50 diffs x 12 lines each

| Benchmark Script Name                      | 10 Diffs Execution Time (s)  | 50 Diffs Execution Time (s)  |
|--------------------------------------------|------------------------------|------------------------------|
| fastrs_join_strings                        | 0.020                        | 0.020                        |
| apply_colouring_fastrs_join_strings        | 0.020                        | 0.021                        |
| apply_colouring_fastrs_join_strings_regex  | 0.020                        | 0.021                        |
| apply_colouring_str_join                   | 0.027                        | 0.028                        |


## Reproduction

Run `python run_bench.py` to reproduce the table above
