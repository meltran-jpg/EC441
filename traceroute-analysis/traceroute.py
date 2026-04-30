# basic traceroute using system command

import subprocess

target = "google.com"

result = subprocess.run(["traceroute", target], capture_output=True, text=True)

print(result.stdout)
