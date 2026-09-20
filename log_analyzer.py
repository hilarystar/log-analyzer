import sys
import json

if len(sys.argv) < 2:
    print("Usage: python log_analyzer.py <log.file>")
    sys.exit(1)

filename = sys.argv[1]
json_output = "--json" in sys.argv

try:
    with open(filename, "r") as file:
        contents = file.read()

except FileNotFoundError:
    print("Error: log file not found.")
    sys.exit(1)

def analyze_log(contents):
    counts = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
    }

    errors = {} 

    for line in contents.splitlines():
        line = line.strip()
        if line.startswith("INFO"):
            counts["INFO"] += 1

        elif line.startswith("WARNING"):
            counts["WARNING"] += 1      

        elif line.startswith("ERROR"):
            counts["ERROR"] += 1

        parts = line.split(" ", 1)

        if len(parts) > 1:
            error_message = parts[1].strip()
            errors[error_message] = errors.get(error_message, 0) + 1

    total_entries = len(contents.splitlines())

    if total_entries > 0:
        error_rate = (counts["ERROR"] / total_entries) * 100
    else:
        error_rate = 0

    return counts, error_rate, errors

def main():
    counts, error_rate, errors = analyze_log(contents)

    if json_output:
        result = {
    "total_entries": len(contents.splitlines()),
    "info": counts["INFO"],
    "warning": counts["WARNING"],
    "error": counts["ERROR"],
    "error_rate": round(error_rate, 2),
    "errors" : errors
    }

        print(json.dumps(result, indent=4))
        return


    print("\n==== LOG ANALYZER ====")
    print(f"File: {filename}")
    print("--------------------------")
    print(f"Total log entries: {len(contents.splitlines())}")
    print(f"INFO: {counts['INFO']}")
    print(f"WARNING: {counts['WARNING']}")   
    print(f"ERROR: {counts['ERROR']}")
    print(f"Error Rate: {error_rate:.2f}%")

    if errors:
        most_common_error = max(errors, key=errors.get)
        most_common_count = errors[most_common_error]
        print(f"Most Common Error: {most_common_error},({most_common_count} times)")

    print("\nError breakdown:")

    for error, count in errors.items():
        print(f"- {error}: {count}")

    print("======================")

if __name__ == "__main__":
    main()
    