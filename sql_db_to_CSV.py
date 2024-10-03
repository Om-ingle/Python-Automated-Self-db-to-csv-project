import pandas as pd
import pyodbc as odbc
from datetime import datetime

# Establishing the connection
ConnectionString = odbc.connect(
    r'DRIVER={SQL Server Native Client 11.0};'
    r'Server=DESKTOP-OKP2NBN\SQLEXPRESS;'
    r'Database=AdventureWorks2019;'
    r'Trusted_Connection=yes;'
    r'TrustServerCertificate=yes;'
)

# Executing the query and reading the results into a DataFrame
query = pd.read_sql_query(
    '''
    SELECT BusinessEntityID, Passwordhash, rowguid
    FROM Person.Password
    ''',
    ConnectionString
)

# Generating the CSV file name with a timestamp
file_name = datetime.now().strftime("%Y-%m-%d_%I-%M-%S-%p") + '-SQL_User_Password_Data.csv'

# Saving the DataFrame to a CSV file
query.to_csv(file_name, index=False)

print(f"Data successfully saved to {file_name}")
