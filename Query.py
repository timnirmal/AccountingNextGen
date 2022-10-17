import pandas as pd
import numpy as np

# show all columns in dataframe
pd.set_option('display.max_columns', None)

# Create Users
# user_id, name, email, password, created_at, updated_at, role_id,
users = pd.DataFrame({'user_id': [1, 2, 3, 4, 5, 6, 7],
                      'user_name': ['John', 'Paul', 'George', 'Ringo', 'Pete', 'Mike', 'Dave'],
                      'email': ['John@gmail.com', 'Paul@gmail.com', 'George@gmail.com', 'Ringo@gmail.com',
                                'Pete@gmail.com', 'Mike@gmail.com', 'Dave@gmail.com'],
                      'password': ['John123', 'Paul123', 'George123', 'Ringo123', 'Pete123', 'Mike123', 'Dave123'],
                      'created_at': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05', '2020-01-06',
                                     '2020-01-07'],
                      'updated_at': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05', '2020-01-06',
                                     '2020-01-07'],
                      'role_id': [1, 2, 3, 1, 2, 3, 1]
                      })

# Create Roles
# role_id, name
roles = pd.DataFrame({'role_id': [1, 2, 3],
                      'name': ['Admin', 'Manager', 'Employee']
                      })

# Create User_Roles
# user_id, role_id
# user_roles = pd.DataFrame({'user_id': [1, 2, 3, 4, 5, 6, 7],
#                             'role_id': [1, 2, 3, 1, 2, 3, 1]
#                             })

# Create Products
# product_id, name, price, created_at, updated_at
products = pd.DataFrame({'product_id': [1, 2, 3, 4, 5, 6, 7],
                            'name': ['Apple', 'Orange', 'Banana', 'Peach', 'Pear', 'Grape', 'Watermelon'],
                            'price': [1.99, 2.99, 3.99, 4.99, 5.99, 6.99, 7.99],
                            'created_at': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05',
                                             '2020-01-06', '2020-01-07'],
                            'updated_at': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05',
                                                '2020-01-06', '2020-01-07']
                            })

# Create Orders
# order_id, user_id, product_id, quantity, created_at, updated_at
orders = pd.DataFrame({'order_id': [1, 2, 3, 4, 5, 6, 7],
                            'user_id': [1, 2, 3, 4, 5, 6, 7],
                            'product_id': [1, 2, 3, 4, 5, 6, 7],
                            'quantity': [1, 2, 3, 4, 5, 6, 7],
                            'created_at': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05',
                                                '2020-01-06', '2020-01-07'],
                            'updated_at': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05',
                                                '2020-01-06', '2020-01-07']
                            })

# Create Order_Details (4 products per order)
# order_id, product_id, quantity, price, created_at, updated_at
order_details = pd.DataFrame({'order_id': [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7],
                              'product_id': [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],
                              'quantity': [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],
                              'price': [1.99, 2.99, 3.99, 4.99, 1.99, 2.99, 3.99, 4.99, 1.99, 2.99, 3.99, 4.99, 1.99, 2.99, 3.99, 4.99, 1.99, 2.99, 3.99, 4.99, 1.99, 2.99, 3.99, 4.99, 1.99, 2.99, 3.99, 4.99],
                              'created_at': ['2020-01-01', '2020-01-01', '2020-01-01', '2020-01-01', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02',
                                             '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04',
                                             '2020-01-05', '2020-01-05', '2020-01-05', '2020-01-05', '2020-01-06', '2020-01-06', '2020-01-06', '2020-01-06',
                                             '2020-01-07', '2020-01-07', '2020-01-07', '2020-01-07'],
                              'updated_at': ['2020-01-01', '2020-01-01', '2020-01-01', '2020-01-01', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02',
                                             '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04',
                                             '2020-01-05', '2020-01-05', '2020-01-05', '2020-01-05', '2020-01-06', '2020-01-06', '2020-01-06', '2020-01-06',
                                             '2020-01-07', '2020-01-07', '2020-01-07', '2020-01-07']
                              })



# Create Sales
# sale_id, user_id, sale_date, sale_amount
sales = pd.DataFrame({'sale_id': [1, 2, 3, 4, 5, 6, 7],
                      'user_id': [1, 2, 3, 4, 5, 6, 7],
                      'sale_date': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05', '2020-01-06',
                                    '2020-01-07'],
                      'sale_amount': [100, 200, 300, 400, 500, 600, 700]
                      })

# Create Purchases
# purchase_id, user_id, purchase_date, purchase_amount
purchases = pd.DataFrame({'purchase_id': [1, 2, 3, 4, 5, 6, 7],
                          'user_id': [1, 2, 3, 4, 5, 6, 7],
                          'purchase_date': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05',
                                            '2020-01-06',
                                            '2020-01-07'],
                          'purchase_amount': [100, 200, 300, 400, 500, 600, 700]
                          })


# save to csv
users.to_csv('Database/users.csv', index=False)
products.to_csv('Database/products.csv', index=False)
orders.to_csv('Database/orders.csv', index=False)
order_details.to_csv('Database/order_details.csv', index=False)
sales.to_csv('Database/sales.csv', index=False)
purchases.to_csv('Database/purchases.csv', index=False)
