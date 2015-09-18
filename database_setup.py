# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 02:57:39 2015

@author: Z
"""

####### CONFIGURATION CODE #############
import sys
from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship\

from sqlalchemy import create_engine

Base = declarative_base()



### CLASS Code ###
class Restaurant(Base):
    ### TABLE INFORMATION ###
    __tablename__ = 'restaurant'

    ### MAPPERS ###
    name = Column(String(80), nullable = False)
    id =  Column(Integer, primary_key = True)

### CLASS CODE ##
class MenuItem(Base):  ### classes in camelcase
    ### TABLE INFORMATION
    __tablename__ = 'menu_item'  ## table names in lowercase

    ###  MAPPER CODE
    name = Column(String(90), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))

    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)






########insert at the end of the file  ###############
#####
engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
