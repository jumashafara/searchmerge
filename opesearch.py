import re
import pandas as pd


"""
©LearningTool

This is a simple application which allows a user to search for a product
from one particular store. I have created a search function which allows this.
(You can improve the search function where you see fit). 

The search function takes in products in a string form, example "milk,bread,coffee,potatoes"
and takes in one store and returns the full names of the products in a list. 
Try for example: Store =  pnp , product = milk,jacobs

The task is to allow a user to input more than one store and return all products from the 
stores that the user has specified.
Example store = pnp,spar  products = milk 
returns [['Milk 1L Spar],['Milk 1L Pnp]]
        
Our goal after this is to be able to create a single table with both products from both shops so keep this in mind

Issues you might face
There arent many products that match as yet so scan the csv files for what matches and use those for test
example: Spar, pnp and game all have Jacobs coffee
"""


#Read files from "database", we have 4 South African stores here
#Please your own path to the project to read the files
spar = pd.read_csv(r' \Data\spar\SparMainTable.csv')
pnp = pd.read_csv(r' \Data\pnp\PnpMainTable.csv')
makro = pd.read_csv(r' \Data\makro\MakroMainTable.csv')
game = pd.read_csv(r' \Data\game\GameMainTable.csv')


def searching_product_list_of_prods(user_search_name, store_name):
        if store_name == 'pnp':
            prod_name_list = pnp['Product Name'].tolist()
        elif store_name == 'spar':
            prod_name_list = spar['Product Name'].tolist()
        elif store_name == 'makro':
            prod_name_list = makro['Product Name'].tolist()
        elif store_name == 'game':
            prod_name_list = game['Product Name'].tolist()
        prod_lis = [x.lower() for x in prod_name_list]
        user_search_name = user_search_name.lower()
        words = user_search_name.split(',')
        # This returns a list of searched objects 
        # This is to make our searches robust
        products_lists = []
        for j in words:
            for i in prod_lis:
                # Checks for pattern matches for starting in co
                if re.search(r'{}'.format(j), i):
                    products_lists.append(i)               
        print(products_lists)
        return products_lists

store_name = input("Please enter store name:")
product_name = input("Please enter product name:")

searching_product_list_of_prods(product_name, store_name)