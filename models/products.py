#! /usr/bin/env python3
# coding: utf-8
"""
Jean-Pierre [Prototype]
A Raspberry Pi robot helping people to build groceries list.
Matteo Cargnelutti - github.com/matteocargnelutti

scanner/models/products.py
"""
#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
from utils import Database

#-----------------------------------------------------------------------------
# Products Table class
#-----------------------------------------------------------------------------
class Products:
    """
    This class handles :
    - Add / Get items from the Products table, which is a cache for products info
    Usage :
    - products = Products()
    - product = products.get_one(barcode)
    """
    def __init__(self):
        """
        Constructor
        :rtype: ProductsTable
        """
        # Is the database connexion initialized ?
        if not Database.is_ready():
            Database.on()

    def create_table(self):
        """
        Creates the Products table
        :rtype: bool
        """
        query = """
                CREATE TABLE IF NOT EXISTS Products (
                    barcode CHAR (13) PRIMARY KEY,
                    name    TEXT,
                    pic     TEXT
                )
                WITHOUT ROWID;
                """
        Database.LINK.execute(query)
        Database.LINK.commit()
        return True

    def get_item(self, barcode):
        """
        Get a product from its barcode
        :param barcode: barcode to lookup for
        :type barcode: string
        :rtype: tuple
        """
        query = "SELECT * FROM Products WHERE barcode = ?;"
        params = (barcode,)

        Database.CURSOR.execute(query, params)
        product = Database.CURSOR.fetchone()

        if product:
            return {'barcode': product['barcode'],
                    'name': product['name'],
                    'pic': product['pic']}
        else:
            return False

    def add_item(self, barcode, name, pic=''):
        """
        Adds a product
        :param barcode: barcode to lookup for
        :param name: name of the product
        :param pic: blob of the thumbnail pic
        :type name: string
        :type barcode: string
        :type pic: binary
        :rtype: bool
        """
        query = "INSERT INTO Products VALUES (?, ?, ?);"
        params = (barcode, name, pic)

        Database.CURSOR.execute(query, params)
        Database.LINK.commit()

        return True

    def __del__(self):
        """
        Closes database connexion on delete
        """
        Database.off()
