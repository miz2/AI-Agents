import csv 

def process_csv(file_path):
    total_salary=0
    engineering_count=0
    with open(file_path,newline='') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            if row['department']=='Engineering':
                engineering_count+=1
                total_salary+=float(row['salary'])
    print(f"Total Salary for Engineering: {total_salary}")
    print(f"Number of Employees in Engineering: {engineering_count}")

def main():
    file_path='data.csv'
    process_csv(file_path)

if __name__ == "__main__":    
    main()