# This file only has to be ran once. If the database and tables are created, this can be omitted
# NapCorps Inc., User - dsantos date - 04/29/2015


class CreateItem():

    def __init__(self, name, quantity, brand,
                 model, description, unit_cost,
                 selling_price, picture):
        self.name = name
        self.brand = brand
        self.model = model
        self.description = description
        self.quantity = quantity
        self.unit_cost = unit_cost
        self.selling_price = selling_price
        self.picture = picture


# class UpdateItem():
#
#     def __init__(self, name, quantity, brand, model, description, unit_cost, selling_price, picture):
#         self.name = name
#         self.brand = brand
#         self.model = model
#         self.description = description
#         self.quantity = quantity
#         self.unit_cost = unit_cost
#         self.selling_price = selling_price
#         self.picture = picture