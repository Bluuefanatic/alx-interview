#!/usr/bin/python3
import sys

# Initialize counters and storage variables
total_size = 0
status_code_count =
{200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_statistics():
    """Print the statistics of file size and status codes."""
    print(f"File size: {total_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")


try:
    for line in sys.stdin:
        # Split the line and check format
        parts = line.split()
    if len(parts) < 7 or not parts[-2].isdigit() or not parts[-1].isdigit():
            continue

        # Extract the file size and status code
     try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Update total file size and status code counts
            total_size += file_size
            if status_code in status_code_count:
                status_code_count[status_code] += 1
        except ValueError:
            continue

        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Print final stats on keyboard interruption
    print_statistics()
    raise

# Print final stats after EOF
print_statistics()
