import argparse
def analyze_logs(file,keyword,output=None,count_only=False):
    count=0;
    matches=[]
    with open(file,'r') as f:
        for line in f:
            if keyword in line:
                count+=1
                matches.append(line.strip())
                if not count_only:
                    print(f"Match found: {line.strip()}")
    print(f"Total {keyword} matches found: {count}")       
    
    # save results to output file if specified
    if output:
        with open(output,'w') as out_file:
            for match in matches:
                out_file.write(match+'\n')
        print(f"Results saved to {output}")

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
    parser.add_argument(
        "--output",
        required=False,
        help="Path to save the matched results."
    )
    parser.add_argument(
        "--count-only",
        action='store_true',
        help="Only display the count of matches without showing each match."
    )
    args=parser.parse_args()
    analyze_logs(args.file,args.keyword,args.output,args.count_only) 

if __name__ == "__main__":    main()

# sample run cases 
# python log_outputtool.py --file logs.txt --keyword ERROR --output results.txt
# python log_outputtool.py --file logs.txt --keyword ERROR --count-only  