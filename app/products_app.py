import code
import csv
import os

products = []
my_path = os.path.abspath(os.path.dirname(__file__))
csv_file_path = os.path.join(my_path, "../data/products.csv")
#code.interact(local=locals())
#csv_file_path = "/Users/sanketwagle/Desktop/CurdAppClone/data/products.csv"
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    products = [dict(row) for row in reader]

def filterProducts(index):
    #return max identifer , list index and  required product
    prod = None # product
    count = 0 #List index
    maxProd = products[len(products)-1]
    maxId = int(maxProd["id"]) #max identifer
    if index == "max":
        return [maxId, None, None]
    for p in products:
        if int(p["id"]) == index:
            prod = p
            break
        count = count + 1
    if not prod:
        count = None
    return [maxId, count, prod]

def writeFile(prods):
    if not prods:
        return
    with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
        writer.writeheader()
        writer.writerows(prods)

def formatCheck(usr):
    try:
        usr = int(usr)
        return usr
    except ValueError:
        print("Please input a valid integer E.g. 1 for product identifier")
        return None

def listing():
    print ("There are {0} products in the database. Please select an operation".format(len(products)))
    for p in products:
        print ("+" + str(p))

def show():
        usr = input("OK. Please specify product's identifier: ")
        usr = formatCheck(usr)
        if not usr:
            return
        result = filterProducts(usr)
        if not result[2]:
            print ("Product not found. Please check the identifier")
            return
        print(str(result[2]))

def create():
    print("OK. Please specify product's information....")
    name = input("name: ")
    aisle = input("aisle: ")
    dept = input("department: ")
    price = input("price: ")
    print ("CREATING PRODUCT HERE!")
    result = filterProducts("max")
    ids = result[0] + 1 # Identifier index
    create = {"id":ids, "name":name, "aisle":aisle, "department":dept, "price":price}
    products.append(create)
    print ("CREATING A PRODUCT HERE!")
    print (str(create))
    writeFile(products)


def update():
    usr = input("OK. Please specify product's identifier....")
    usr = formatCheck(usr)
    if not usr:
        return
    result = filterProducts(usr)
    ids = result[1] # List index
    if not ids:
        print ("Please pick a proper identifier")
        return
    print("OK. Please specify product's information....")
    choice = products[ids]
    name = input("Change name from {0} to: ".format(choice["name"]))
    aisle = input("Change name from {0} to: ".format(choice["aisle"]))
    dept = input("Change name from {0} to: ".format(choice["department"]))
    price = input("Change name from {0} to: ".format(choice["price"]))
    update = {"id":usr, "name":name, "aisle":aisle, "department":dept, "price":price}
    products[ids] = update
    print ("UPDATING PRODUCT HERE!")
    print (str(update))
    writeFile(products)

def destroy():
    usr = input("OK. Please specify product's identifier....")
    usr = formatCheck(usr)
    if not usr:
        return
    result = filterProducts(usr)
    print ("DESTROYING PRODUCT HERE!")
    ids = result[1] # List index
    choice = products[ids]
    print (str(choice))
    products.pop(ids)
    writeFile(products)

def default():
    print ("Please make a proper selection")

msg = """
------------------------
PRODUCTS APPLICATION
------------------------
Welcome @SRW390!
"""

print(msg)
print ("There are {0} products in the database. Please select an operation:".format(len(products)))

menu = """
    operation | description
    --------- | -------------
    'List'    | Display a list of product identifiers and names.
    'Show'    | Show information about a product.
    'Create'  | Add a new product.
    'Update'  | Edit an existing product.
    'Destroy' | Delete an existing product.
"""

user = input(menu)

choices = {'List': listing,
            'Show': show,
            'Create': create,
            'Update': update,
            'Destroy': destroy,
            'Default': default
        }

try:
    choices.get(user.title())()
except TypeError:
    default()

#code.interact(local=locals())
