#!/usr/bin/python3
""" Doc string"""
from pandas import DataFrame

Employees = {'Name of Employee': ['Jon', 'Mark', 'Tina', 'Maria', 'Bill', 'Jon', 'Mark', 'Tina',
                                  'Maria', 'Bill', 'Jon', 'Mark', 'Tina', 'Maria', 'Bill', 'Jon',
                                  'Mark', 'Tina', 'Maria', 'Bill'],
             'Sales': [1000, 300, 400, 500, 800, 1000, 500, 700, 50, 60, 1000, 900, 750, 200, 300,
                       1000, 900, 250, 750, 50],
             'Quarter': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4],
             'Country': ['US', 'Japan', 'Brazil', 'UK', 'US', 'Brazil', 'Japan', 'Brazil', 'US', 'US',
                         'US', 'Japan', 'Brazil', 'UK', 'Brazil', 'Japan', 'Japan', 'Brazil', 'UK', 'US']
            }

df = DataFrame(Employees, columns=['Name of Employee', 'Sales', 'Quarter', 'Country'])

print(df)
