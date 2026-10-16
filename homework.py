import pandas as pd
import numpy as np

import time

df_a = pd.DataFrame({
    'EmployeeID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Department': ['HR', 'Engineering', 'Marketing']
})

df_b = pd.DataFrame({
    'EmployeeID': [4, 5],
    'Name': ['David', 'Eva'],
    'Department': ['Finance', 'IT']
})

result_ind = pd.concat([df_a, df_b],axis=0, ignore_index=True)
result_keys = pd.concat([df_a, df_b], keys=['Group_A', 'Group_B']).reset_index()
print(result_ind,'\n')
print(result_keys,'\n')


orders_df = pd.DataFrame({
    'OrderID': [1001, 1002, 1003, 1004],
    'CustomerID': [1, 2, 1, 3],
    'ProductID': [501, 502, 503, 504],
    'Quantity': [2, 1, 5, 3]
})

customers_df = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David']
})

result = pd.merge(orders_df, customers_df, on='CustomerID', how='inner', indicator=True)
print(result)

np.random.seed(0)
transactions_df = pd.DataFrame({
    'TransactionID': range(1, 100001),
    'UserID': np.random.randint(1, 1001, size=100000),
    'ProductID': np.random.randint(501, 506, size=100000),
    'Date': pd.date_range(start='2023-01-01', periods=100000, freq='D'),
    'Amount': np.random.uniform(10.0, 1000.0, size=100000)
})

products_df = pd.DataFrame({
    'ProductID': [501, 502, 503, 504, 505],
    'ProductName': ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Printer'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Office Supplies'],
    'SupplierID': [201, 202, 203, 201, 204]
})


transactions_df['Amount'] = transactions_df['Amount'].astype('float32')
transactions_df_index = transactions_df.set_index(['UserID','ProductID'])
print(transactions_df.info(),'- перетворили тип стовпця Amount на float32\n' )

products_df_index = products_df.set_index('ProductID')

start_time = time.time()
result = pd.merge(transactions_df, products_df_index, left_on='ProductID', right_index=True, how='inner')
time_index = time.time() - start_time
print(f'Час виконання без індекса: {time_index:.4f} секунд')

start_time = time.time()
result = pd.merge(transactions_df_index, products_df_index, left_on='ProductID', right_index=True, how='inner')
time_index = time.time() - start_time
print(f'Час виконання з індексом: {time_index:.4f} секунд')
print(result)

df_sales = pd.DataFrame({
    'SaleID': [2001, 2002, 2003, 2004, 2005],
    'StoreID': [10, 20, 10, 30, 20],
    'ProductID': [301, 302, 303, 301, 304],
    'UnitsSold': [50, 60, 70, 80, 90]
})

df_suppliers = pd.DataFrame({
    'SupplierID': [401, 402, 403, 404],
    'ProductID': [301, 302, 303, 305],
    'SupplierName': ['Supplier A', 'Supplier B', 'Supplier C', 'Supplier D']
})

df_sales.set_index(['StoreID','ProductID'])

result = pd.merge(df_sales,df_suppliers, on='ProductID', validate='many_to_one')
print(result)