Import csv
#Open the CSV file 
with open('data.csv', 'r') as file:
    #Create a CSV reader 
    object reader csv.reader(file)
    #Iterate over the rows in the csv file
    for row in reader:
        print(row)
        import pandas as pd
#Read the CSV file into a Dataframe 
df pd.read_csv('data.csv')
#Display the first few rows
print(df.head())
#Filter the Dataframe to only include rows where the 'age' column is greater than 30
filtered_df = df[df['age'] > 30]
print(filtered_df) 
#Group the Dataframe by the department column and calculate the average salary
grouped_df = df.groupby('department')['salary'].mean()
print(grouped_df) 
#Sort the Dataframe by the "name" column in ascending order 
sorted_df = df.sort_values('name')
print(sorted_df)
