products = [{'id':1, 'name':'iphone', 'category':'mobile','price':90000}]
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
    products.append({'id' : id, 'name' : name, 'category' : category, 'price' : price})
    print('Added Successfully')
  elif type == 2:
    for index in range(len(products)):
      print('-------------------------------------------------------------------------\n',
      products[index].get('id'), '\t', '|', '\t', products[index].get('name'), '\t','|', '\t', products[index].get('category'), '\t','|','\t',products[index].get('price'),'\n',
      '------------------------------------------------------------------------')
  elif type == 3:
    id = int(input('Enter Id to Search: '))
    product = None
    for index in range(len(products)):
      if(products[index].get('id') == id):
        product = products[index]
        break
    if (product):
      print('ID: ', product.get('id'))
      print('Name: ', product.get('name'))
      print('Category: ', product.get('category'))
      print('Price: ', product.get('price'))
    else:
      print('No Product Found!')
  elif type == 4:
    id = int(input('Enter Product ID to Delete Product:'))
    deleted = False
    for index in range (len(products)):
      if(products[index].get('id') == id):
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
      if(products[index].get('id') == id):
        id = int(input('Enter Product ID: '))
        name = input('Enter Product Name: ')
        category = input('Enter Product Category: ')
        price = int(input('Enter Product Price:'))
        products[index]={'id' : id, 'name' : name, 'category' : category, 'price' : price}
      32
      if updated:
        print('Product Updated')
      else:
        print('Not found!')
  elif type == 6:
    print('Exit')
    break
  else:
    print('Invalid Input!')