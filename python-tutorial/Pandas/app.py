
import pandas as pd
# pip install pandas openpyxl

# df stands for Data Frame and it is a variable
df = pd.read_excel(r"C:\Users\iaman\OneDrive\Desktop\dataset.xlsx")
# df = pd.read_excel("C:/Users/iaman/OneDrive/Desktop/dataset.xlsx")

print(df)

# average salary
avg_salary = df['Salary'].mean()
print(f"\n Average Salary: {avg_salary}")

# add a new columns
df['Experience'] = ['Junior', 'Mid', 'Senior', 'Mid']
print("\n Added Experience Column:")
print(df)

# filter IT department
it_employees = df[df['Department'] == 'IT']
print("\n IT Employees:")
print(it_employees)
