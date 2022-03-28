import pandas as pd 

data = pd.read_csv('dataset.csv')

def product(query):
    """
    Working: Find the top five product with any given query.
    Args:
        query: The query requested by user.
    Output:
        A list of top five product tile with the given query.
    """
    pt = data['Product Title'].values
    pt = pt.astype(str)
    found = []
    mx = 0
    for i in pt:
        temp = query.lower()
        curr = i.lower()
        if temp in curr:
            mx += 1
            found.append(i)
        if mx == 5:
            break
    return found

def idx(title):
    """
    Working: Get the index of the product in the dataset.
    Args:
        title: Product Title.
    Output: Returns the index of the product in the dataset. Returns `-1` if the product not found in the dataset.
    """
    pt = data['Product Title'].values
    pt = pt.astype(str)
    curr = -1
    for i in pt:
        curr += 1
        temp = title.lower()
        item = i.lower()
        if temp in item:
            return curr
    return -1

def detail(title):
    """
    Working: Get the product detail of the given product title.
    Args:
        title: Product Title.
    Output: Returns the detail.
    """
    dt = data['Product Description'].values
    try:
        # get the index of the product inside the dataset 
        curr = idx(title)
        if curr != -1:
            d = dt[curr]
            return d
        else:
            error = 'Product not found. Please enter the Product title. To find the product using \"Product < search query >\"'
            return error
    except Exception as e:
        error = 'Product not found. Please enter the Product title. To find the product using \"Product < search query >\"'
        return error

def price(title):
    """
    Working: Get the product price.
    Args:
        title: Product title.
    Output: Get the price of the product.
    """
    p = data['Price'].values
    try:
        # get the index of the product inside the dataset 
        curr = idx(title)
        if curr != -1:
            p = p[curr]
            return p
        else:
            error = 'Product not found. Please enter the Product title. To find the product using \"Product < search query >\"'
            return error
    except Exception as e:
        error = 'Product not found. Please enter the Product title. To find the product using \"Product < search query >\"'
        return error  

def help():
    """
    Working: Building on fire, help!
    Args:
        No args.
    Output: Get the help.
    """
    query = 'Enter : \"product < search query >\" to get top five product with the given keyword, \"detail < search query >\" to get the detail of the particular product, \"price < search query >\" to get the price of the product.'
    return query