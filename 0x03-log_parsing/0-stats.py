#!/usr/bin/python3
"""
Module to process log entries, track file size and
status codes. This script reads log entries from
standard input, calculates the total file size, and
counts various HTTP status codes. It prints statistics
periodically and upon interrupt signals.
"""

import sys
import re
import signal

# Initialize variables
total_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

# Regular expression to match the log line format
log_pattern = re.compile(
    r'(\S+) - \[(.+?)\] "GET (/projects/260) HTTP/1.1" (\d{3}) (\d+)'
)


# Signal handler for CTRL + C
def signal_handler(sig, frame):
    """
    Signal handler for graceful shutdown on CTRL + C.
    It prints the current statistics before exiting the program.
    """
    print_stats()
    sys.exit(0)


# Function to print stats
def print_stats():
    """
    Print the current statistics including total file size
    and counts of HTTP status codes.
    """
    global total_size, status_codes_count

    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Read input line by line from stdin
try:
    for line in sys.stdin:
        line_count += 1

        # Try to match the log pattern
        match = log_pattern.match(line)

        if match:
            ip = match.group(1)
            date = match.group(2)
            url = match.group(3)
            status_code = match.group(4)
            file_size = match.group(5)

            # Update total file size
            total_size += int(file_size)

            # Update status code count if valid
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1
        else:
            # Line format doesn't match
            continue

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # If interrupted by CTRL + C, print stats
    print_stats()
    sys.exit(0)
