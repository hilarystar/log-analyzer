import sys
if len(sys.argv) < 2:
    print("Usage: python log_analyzer.py <log.file>")
    sys.exit(1)
filename = sys.argv[1]
try:
    with open(filename, "r") as file:
        contents = file.read()
except FileNotFoundError:
    print("Error: log file not found.")

def analyze_log(contents):
    counts = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
    }

    errors = {} 

    for line in contents.splitlines():
        if line.startswith("INFO"):
            counts["INFO"] += 1
        elif line.startswith("WARNING"):
            counts["WARNING"] += 1      
        elif line.startswith("ERROR"):
            counts["ERROR"] += 1
        error_message = line.split(" ", 1)[1]
        errors[error_message] = errors.get(error_message, 0) + 1
        most_common_error = max(errors, key=errors.get)
        most_common_count = errors[most_common_error]

    total_entries = len(contents.splitlines())
    if total_entries > 0:
        error_rate = (counts["ERROR"] / total_entries) * 100
    else:
        error_rate = 0

    print("\n==== LOG ANALYZER ====")
    print(f"File: {filename}")
    print("--------------------------")
    print(f"Total log entries: {total_entries}")
    print(f"INFO: {counts['INFO']}")
    print(f"WARNING: {counts['WARNING']}")
    print(f"ERROR: {counts['ERROR']}")
    print(f"Error Rate: {error_rate:.2f}%")
    print(f"Most Common Error: {most_common_error},({most_common_count} times)")

    print("\nError breakdown:")

    for error, count in errors.items():
        print(f"- {error}: {count}")

    print("======================")

analyze_log(contents)