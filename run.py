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
    profiles_data = json.load(f)["profiles"]

profiles = [p["name"] for p in profiles_data]

# RUN 1
cmd1 = [
    "uv", "run", "bing-rewards", "-b",
    "-d", "-c22",
    "--exe", "chrome",
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

run_cmd(cmd1, "RUN 1 (Desktop)")
run_cmd(cmd3, "RUN 1 (Desktop)")
