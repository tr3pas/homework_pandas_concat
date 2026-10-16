# import pandas as pd

# df_courses = pd.DataFrame({
#     'CourseID': [101, 102, 103],
#     'CourseName': ['Quantum Mechanics', 'Organic Chemistry', 'Calculus']
# }, index=[1, 2, 3])

# df_instructors = pd.DataFrame({
#     'Instructor': ['Dr. Smith', 'Dr. Johnson', 'Dr. Lee']
# }, index=[1, 2, 4])

# result = pd.merge(df_courses, df_instructors, left_index=True, right_index=True, how='outer').fillna('Unknown')


# print(result)


import pandas as pd

sales_df = pd.DataFrame({
    'SaleID': [1001, 1002, 1003, 1004, 1005, 1006],
    'StoreID': [1, 2, 1, 3, 2, 3],
    'ProductID': [501, 502, 503, 501, 502, 504],
    'Date': ['2023-01-15', '2023-01-17', '2023-02-20', '2023-02-25', '2023-03-05', '2023-03-10'],
    'UnitsSold': [20, 35, 15, 40, 25, 30],
    'Revenue': [2000, 3500, 1500, 4000, 2500, 3000]
})

products_df = pd.DataFrame({
    'ProductID': [501, 502, 503, 504, 505],
    'ProductName': ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Printer'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Office Supplies'],
    'SupplierID': [201, 202, 203, 201, 204]
})  