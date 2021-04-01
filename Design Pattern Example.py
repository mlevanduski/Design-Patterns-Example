# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:47:26 2020

Design Patterns Lab 7

@author: MLevanduski
"""
from time import sleep

#Part I Singleton Class

class Restaurant(object):
    
    def __init__(self, *args):
        print(f"Restaurant.__init__ {args}")
    
    def __new__(cls, *args, **kwargs):
        print(f"Restaurant.__new__ {args}")
        if not hasattr(cls, '_instance'):
            print("Creating new Restaurant")
            cls._instance = super(Restaurant, cls).__new__(cls, *args, **kwargs)
        else:
            print("Using existing Restaurant")
            
        #Initializing Extra Credit Variables
        _orders = 0
        _total_sales = 0
        
        return cls._instance
        
    def __str__(self):
        pass
    
    def order_food(self, food_type):
        Food.order_food(food_type) # Not sure if I need a self instance member to access static method in Food class
        #alter _orders and _total_sales variables for extra credit
        
#Part II Food factory base class

class Food():
    
    def __init__(self):
        print("Currently in Food.__init__ base class")
    
    def price(self):
        return 0 # Not sure how this works yet since derivative classes need to access here
    
    def prepare(self):
        pass
    
    @staticmethod #Factory design pattern in order_food method
    def order_food(food_type):
        if type(food_type) is str:
            food_type.lower()
            food_type = food_type.strip()
        else:
            print("Please enter a string type")
        if food_type == "cheeseburger":
            item_1 = Cheeseburger()
            item_1.prepare() 
        elif food_type == "pasta":
            item_2 = Pasta()
            item_2.prepare()
        elif food_type == "pizza":
            item_3 = Pizza()
            item_3.prepare()
        else:
            print("Item does not exist on the menu")
            
class Cheeseburger(Food):
    
    def __init__(self):
        #print("In derivative __init__ Cheeseburger() class")
        pass
    
    def __str__(self):
        return f"{__class__.__name__}: {Cheeseburger.price(self)}"
    
    def price(self):
        cost = 10.00 
        self.cost = cost
        return self.cost
    
    # Fascade design pattern in prepare method
    def prepare(self):
        print("*Hamburger* Grabbing hamburger patties from freezer")
        sleep(2)
        print("*Hamburger* Heating grill")
        sleep(2)
        print("*Hamburger* Placing patty on grill")
        sleep(2)
        print("*Hamburger* Cutting vegetables and preparing order extras")
        sleep(2)
        print("*Hamburger* Dropping side of fries in the fryer")
        sleep(2)
        print("*Hamburger* Plating burger with fries")
        sleep(2)
        print("*Hamburger* Placing order in staging for waiter")
        sleep(2)
        print("*Hamburger* Order complete")
        print(Cheeseburger())
        
class Pasta(Food):
    
    def __init__(self):
        #print("In derivative __init__ Pasta() class")
        pass
    
    def __str__(self):
        return f"{__class__.__name__}: {Pasta.price(self)}"
    
    def price(self):
        cost = 15.00
        self.cost = cost
        return self.cost
    
    # Fascade design pattern in prepare method
    def prepare(self):
        print("<Pasta> Grabbing Pasta from inventory")
        sleep(2)
        print("<Pasta> Boiling water")
        sleep(2)
        print("<Pasta> Placing pasta in water")
        sleep(2)
        print("<Pasta> Preparing meat sauce in separate pan")
        sleep(2)
        print("<Pasta> Straining pasta")
        sleep(2)
        print("<Pasta> Adding meat sauce to pasta and mixing")
        sleep(2)
        print("<Pasta> Garnishing, and placing order in staging for waiter")
        sleep(2)
        print("<Pasta> Order complete")

class Pizza(Food):
    
    def __init__(self):
        #print("In derivative __init__ Pizza() class")
        pass
    
    def __str__(self):
        return f"{__class__.__name__}: {Pizza.price(self)}"
    
    def price(self):
        cost = 20.00
        self.cost = cost
        return self.cost
    
    # Fascade design pattern
    def prepare(self):
        print("Preheating oven")
        sleep(2)
        print("[Pizza] Kneading raw dough into shape")
        sleep(2)
        print("[Pizza] Placing oils, herbs, and sauces")
        sleep(2)
        print("[Pizza] Placing toppings onto pizza")
        sleep(2)
        print("[Pizza] Placing pizza into oven")
        sleep(2)
        print("[Pizza] Extracting pizza from oven")
        sleep(2)
        print("[Pizza] Placing order in staging for waiter")
    
def main():
    r = Restaurant()
    
    food = r.order_food("cheeseburger")
    if food:
        print(food)
    
    food = r.order_food("pasta")
    if food:
        print(food)
    
    food = r.order_food("pizza")
    if food:
        print(food)
        
    food = r.order_food("salad")
    if food:
        print(food)
        
        
    
    