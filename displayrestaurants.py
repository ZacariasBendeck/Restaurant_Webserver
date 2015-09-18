# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 22:06:11 2015

@author: Z
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, MenuItem
##from restaurantmenu.db import MenuItem, Restaurant
#from flask.ext.sqlalchemy import SQLAlchemy
##from random import randint
#import datetime
#import random


engine = create_engine('sqlite:///restaurantmenu.db')

##Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()






