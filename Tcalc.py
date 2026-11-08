
import sys
from collections import defaultdict

input_file = sys.argv[1]
output_file = sys.argv[2]

throughput = defaultdict(int)

# Read received packets
with open(input_file, "r") as file:
    for line in file:
        parts = line.split()

        if len(parts) == 3 and parts[0] == "Rx":
            time = float(parts[1])
            size = int(parts[2])

            second = int(time)
            throughput[second] += size

# Write throughput for every second
with open(output_file, "w") as file:
    file.write("# Time(s) Throughput(Mbps)\n")

    for second in range(1, 20):
        mbps = throughput[second] * 8 / 1_000_000
        file.write(f"{second}\t{mbps:.6f}\n")

print(f"Throughput saved to {output_file}")

