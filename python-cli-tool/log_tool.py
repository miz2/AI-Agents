import argparse

def analyze_logs(file):
    error_count = 0
    with open(file, 'r') as f:
        for line in f:
            if 'ERROR' in line:
                print(f'Error found: {line.strip()}')
                error_count += 1
    print(f'Total errors found: {error_count}')

def main():
    parser=argparse.ArgumentParser(description='Analyze log files for errors.')
    parser.add_argument(
        "--file",
        required=True,
        help="Path to the log file to analyze."
    )
    args=parser.parse_args()
    analyze_logs(args.file)

if __name__ == "__main__":    main()