from data import *

all_ingredients = []

for recipe in recipe_book:
    for ing in recipe.ingredients:
        if ing not in all_ingredients:
            all_ingredients.append(ing)


print("Welcome to the recipe recommendation program. \n The program will suggest recipies featuring a specific ingredient.")

while True:
    letter_choice = input("Please enter the first letter of the ingredient which you want to cook today: \n")
    letter_choice = letter_choice.lower().strip()
    available_ingredients=[]
    while True:
        for ing in all_ingredients:
            if ing[1][0]==letter_choice and ing[1] not in available_ingredients and (ing[1]+"s") not in available_ingredients and ing[1][:-1] not in available_ingredients:
                available_ingredients.append(ing[1])
        if len(available_ingredients) > 0:
            break
        else:
            letter_choice = input(f"Sorry, we don't have recipes with ingredients starting with {choice}. Please select another letter:")
    
    print("We have recipes with the following ingredients: \n")
    option = 1
    for ing in available_ingredients:
        print(str(option) + " " + ing)
        option += 1
    number_choice= input("\nPlease choose the number corresponding to your ingredient: \n")
    ingredient_choice = available_ingredients[int(number_choice)-1]

    print(f"\nWe have the following recipes using {ingredient_choice}: \n")
    for recipe in recipe_book:
        for recipe_ing in recipe.ingredients:
                if ingredient_choice == recipe_ing[1] or (ingredient_choice+"s") == recipe_ing[1] or ingredient_choice[:-1] == recipe_ing[1] :
                    print(recipe)
                    break
    
    next = input("Would you like to: \n 1- Search other recipes\n 2- Exit the program\nOption: ")
    if next == "2":
        print("\nBye!\n")
        break

        
    


