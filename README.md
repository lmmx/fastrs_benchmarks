# String colouring speed optimisation benchmarking

Benchmarked on:
- 10 diffs x 12 lines each
- 50 diffs x 12 lines each

1.1 GHz CPU:

| Benchmark Script Name                      | 10 Diffs Execution Time (s)  | 50 Diffs Execution Time (s)  |
|--------------------------------------------|------------------------------|------------------------------|
| fastrs_join_strings                        | 0.020                        | 0.020                        |
| apply_colouring_fastrs_join_strings        | 0.020                        | 0.021                        |
| apply_colouring_fastrs_join_strings_regex  | 0.020                        | 0.021                        |
| apply_colouring_str_join                   | 0.027                        | 0.028                        |

3.7 GHz CPU:

| Benchmark Script Name                      | 10 Diffs Execution Time (s)  | 50 Diffs Execution Time (s)  |
|--------------------------------------------|------------------------------|------------------------------|
| apply_colouring_fastrs_join_strings_regex  | 0.011                        | 0.010                        |
| fastrs_join_strings                        | 0.011                        | 0.010                        |
| apply_colouring_fastrs_join_strings        | 0.011                        | 0.010                        |
| apply_colouring_str_join                   | 0.012                        | 0.012                        |

## Reproduction

Run `python run_bench.py` to reproduce the table above
