'''
Created on 19.11.2012

@author: florian
'''

import sqlobject
from database.connection import conn

class policy(sqlobject.SQLObject):
    _connection = conn
    url = sqlobject.StringCol(length=14, unique=True)
    name = sqlobject.StringCol(length=255)
    date = sqlobject.DateTimeCol(default=None)
    text = sqlobject.StringCol()
    
policy.createTable(ifNotExists=True)
