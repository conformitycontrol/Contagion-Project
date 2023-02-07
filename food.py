"""Many foods are recursive"""

class Food:

    def count_calories(self) -> int:   #abstract base class
        raise NotImplementedError("Must specify type of food")

class BaseIngredient(Food):

    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def count_calories(self) -> int:
        return self.calories

class CompositeFood(Food):

    def __init__(self, ingredients: list):
        self.ingredients = ingredients

    def count_calories(self) -> int:
        totcal = 0
        for ingredient in self.ingredients:
            totcal += ingredient.count_calories()
        return totcal

flour = BaseIngredient("Flour", 48)
salt = BaseIngredient("Salt", 0)
yeast = BaseIngredient("Sugar", 18)
crust = CompositeFood("Crusty",[flour,salt,yeast,sugar])

tomato = BaseIngredient("Tomato", 50)
oregano = BaseIngredient("Oregano", 1)
basil = BaseIngredient("Basil", 1)
sauce = CompositeFood("Saucey Shawty",[tomato, oregano, basil, salt])

moz = BaseIngredient("Mozzarella", 120)
pine = BaseIngredient("Pineapple", 80)
anchovies = BaseIngredient("Ancho", 45)
toppings = CompositeFood("Toppings", [moz,pine, anchovies])

pizza = CompositeFood("Pizza", [sauce, crust, toppings])

print(f"This pizza has {pizza.count_calories()}")