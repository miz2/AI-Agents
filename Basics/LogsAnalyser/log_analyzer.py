import os

def analyze_log(filepath):
    error_count = 0
    warning_count = 0

    if not os.path.exists(filepath):
        print(f"Log file not found: {filepath}")
        return

    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()

            if 'ERROR' in line:
                error_count += 1
                print(f"[ERROR] {line}")

            elif 'WARNING' in line:
                warning_count += 1
                print(f"[WARNING] {line}")

    print("\nSummary")
    print("--------")
    print(f"Total Errors: {error_count}")
    print(f"Total Warnings: {warning_count}")

def main():
    log_path = "/Users/mac/Desktop/Python-AI/Basics/LogsAnalyser/logs.txt"
    analyze_log(log_path)


if __name__ == "__main__":
    main()