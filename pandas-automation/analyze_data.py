import pandas as pd 

def analyze_data():
    df=pd.read_csv('employees.csv')
    print("\nFull Dataset\n")
    print(df)
    print("\nAverage Salary\n")
    print(df['salary'].mean())
    print("\nEngineering Employees\n")
    engineering=df[df['department']=='Engineering']
    print(engineering)
    print("\nFirst five records in Dataframe\n")
    print(df.head())
    print("\nLast five records in Dataframe\n")
    print(df.tail())
    print("Show Schema\n")
    print(df.info())
    high_salary=df[(df["salary"]>70000) & (df["experience"]>5)]
    print("\nEmployees with salary > 70000 and experience > 5 years\n")
    print(high_salary)
    print(df["salary"])
    print(df[["salary","department"]])
    print("Grouping by department and calculating average salary\n")
    print(df.groupby("department")["salary"].mean())
    print("adding columns")
    df["salary_inr"]=df["salary"]*80
    print(df["salary_inr"])
    print(df)
    print("\nCount of employees\n")
    print(df["name"].count())
    print("\nUnique departments\n")
    print(df["department"].unique())
    print(df["salary"].max())
    print("Employees with exp greater than 5 years")
    exp_gt_5=df[df["experience"]>5]
    print(exp_gt_5)
def main():
    analyze_data()

if __name__=="__main__":
    main()