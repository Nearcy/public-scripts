import json
import subprocess
import sys

def run_cmd(cmd, name):
    print(f"\n=== Running {name} ===")
    print(" ".join(cmd))

    result = subprocess.run(cmd)

    if result.returncode != 0:
        print(f"{name} failed with code {result.returncode}")
        sys.exit(result.returncode)

    print(f"{name} finished successfully")

# load profiles
with open("acc.json", encoding="utf-8") as f:
    profiles = json.load(f)["profiles"]

# RUN 1
cmd1 = [
    "uv", "run", "bing-rewards", "-b",
    "-d", "-c22",
    "--exe", "chrome",
    "--exit",
    "--profile",
    *profiles
]

# RUN 2
cmd2 = [
    "uv", "run", "bing-rewards", "-b",
    "--count=10",
    "--exe", "chrome",
    "--exit",
    "--profile",
    *profiles
]

# RUN 3
cmd3 = [
    "uv", "run", "bing-rewards", "-b",
    "-d", "-c3",
    "--exe", "chrome",
    "--exit",
    "--profile",
    *profiles
]


#1
#run_cmd(cmd2, "RUN 2 (Mobile)")
#2
#run_cmd(cmd2, "RUN 2 (Mobile)")
#3
#run_cmd(cmd2, "RUN 2 (Mobile)")
#4
#run_cmd(cmd2, "RUN 2 (Mobile)")
#5  
run_cmd(cmd1, "RUN 1 (Desktop)")
run_cmd(cmd3, "RUN 1 (Desktop)")
