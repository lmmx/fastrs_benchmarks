import subprocess
import time
from pathlib import Path

directories = ["10", "50"]
per_file = {}

# Pre-allocate the data structure
for directory in directories:
    for script_path in Path(directory).glob("*.py"):
        per_file.setdefault(script_path.stem, {d: [] for d in directories})

# Fill in the data structure
for directory in directories:
    for script_path in Path(directory).glob("*.py"):
        execution_times = []

        for _ in range(4):
            start_time = time.time()
            subprocess.run(["python", str(script_path)], stderr=subprocess.DEVNULL)
            end_time = time.time()
            execution_time = end_time - start_time
            execution_times.append(execution_time)

        average_time = sum(execution_times) / len(execution_times)
        per_file[script_path.stem][directory] = average_time

print("Benchmarked on:")
print("- 10 diffs x 12 lines each")
print("- 50 diffs x 12 lines each")
print()
print(
    "| Benchmark Script Name                      | 10 Diffs Execution Time (s)  | 50 Diffs Execution Time (s)  |"
)
print(
    "|--------------------------------------------|------------------------------|------------------------------|"
)

for script_name in per_file:
    row = f"| {script_name.ljust(42)} |"
    for directory, execution_time in per_file[script_name].items():
        row += f" {execution_time:.3f} ".ljust(30) + "|"
    print(row)
