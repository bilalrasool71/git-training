from collections import namedtuple
product = namedtuple('Product',['id', 'name', 'category', 'price'])
products = [product(1, 'iphone', 'mobile', '90000')]
print('Welcome to Inventory Management System')
print('1. Add product')
print('2. View product')
print('3. Search Product')
print('4. Delete Product')
print('5. Modify Product')
print('6. Exit')

while True:
  type = int(input('Please Select an Option: '))
  if type == 1:
    id = int(input('Enter Product ID: '))
    name = input('Enter Product Name: ')
    category = input('Enter Product Category: ')
    price = int(input('Enter Product Price:'))
    products.append(product(id, name, category, price))
    print('Added Successfully')
  elif type == 2:
    for index in range(len(products)):
      print('-------------------------------------------------------------------------\n',
      products[index].id, '\t', '|', '\t', products[index].name, '\t','|', '\t', products[index].category, '\t','|','\t',products[index].price,'\n',
      '------------------------------------------------------------------------')
  elif type == 3:
    id = int(input('Enter Id to Search: '))
    product = None
    for index in range(len(products)):
      if(products[index].id == id):
        product = products[index]
        break
    if (product):
      print('ID: ', product.id)
      print('Name: ', product.name)
      print('Category: ', product.category)
      print('Price: ', product.price)
    else:
      print('No Product Found!')
  elif type == 4:
    id = int(input('Enter Product ID to Delete Product:'))
    deleted = False
    for index in range (len(products)):
      if(products[index].id == id):
          del products[index]
          deleted = True
          break
    if deleted:
      print('Product Deleted')
    else:
      print('No Product Found!')     
  elif type == 5:
    id = int(input('Enter Product ID to Modify Product:'))
    updated = False
    for index in range(len(products)):
      if(products[index].id == id):
        id = int(input('Enter Product ID: '))
        name = input('Enter Product Name: ')
        category = input('Enter Product Category: ')
        price = int(input('Enter Product Price:'))
        products[index]=product(id, name, category, price)
    if updated:
      print('Product Updated')
    else:
      print('Not found!')
  elif type == 6:
    print('Exit')
    break
  else:
    print('Invalid Input!')