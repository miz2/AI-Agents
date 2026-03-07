import argparse

def analyze_logs(file,keyword):
    count = 0
    with open(file,'r') as f:
        for line in f:
            if keyword in line:
                print(f"Match found: {line.strip()}")
                count += 1
    print(f"Total matches found: {count}")

def main():
    parser=argparse.ArgumentParser(description='Log Analyser CLI Tool')
    parser.add_argument(
        "--file",
        required=True,
        help="Path to the log file to analyze."
    )
    parser.add_argument(
        "--keyword",
        required=False,
        help="Keyword to search for in the log file."
    )
    args=parser.parse_args()
    analyze_logs(args.file,args.keyword)

if __name__ == "__main__":    main()

# to run python searchlog_tool.py --file logs.txt --keyword ERROR
# python searchlog_tool.py --file logs.txt --keyword INFO