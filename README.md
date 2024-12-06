# Recipe Recommendation Program

This program helps combat food waste by recommending recipes based on an ingredient you need to cook before it goes bad. It's perfect for when you have a perishable ingredient at home and are unsure of what recipes to make with it. Simply choose the desired ingredient, and the program will provide a list of recipes featuring it!

## How It Works

1. **Ingredient Selection**: You input the first letter of the ingredient you have, and the program filters through a list of all available ingredients that start with that letter.
2. **Recipe Suggestions**: After selecting an ingredient, the program suggests recipes that use that ingredient.
3. **Interactive**: You can continue searching for recipes with other ingredients or exit the program whenever you like.

## Features

- Suggests recipes based on a specific ingredient you need to use.
- Helps reduce food waste by making use of perishable ingredients.
- Simple and user-friendly command-line interface.
- Allows you to search for ingredients by their first letter.

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/sofiatmenezes/recipe-recommendation.git
    ```
2. Navigate to the project folder:
    ```bash
    cd recipe-recommendation
    ```
3. Make sure you have Python installed.
4. The program uses a `data.py` file to store recipes and ingredients. Ensure you have the appropriate `data.py` file with recipe and ingredient data.

## Usage

1. Run the program:
    ```bash
    python3 recipe_recommendation.py
    ```
2. The program will prompt you to enter the first letter of the ingredient you want to use.
3. After selecting an ingredient, it will show you a list of recipes that contain that ingredient.
4. Choose a recipe and the program will display the full recipe for you.
5. You can continue searching for other ingredients or exit the program by choosing the corresponding option.

## Example

```plaintext
Welcome to the recipe recommendation program. 
The program will suggest recipes featuring a specific ingredient.

Please enter the first letter of the ingredient which you want to cook today: 
p
We have recipes with the following ingredients:

1 potatoes
2 parsley
3 pork ribs
4 pepper
5 paprika
6 puff pastry
7 pork
8 parmesan
9 peas
10 pasta

Please choose the number corresponding to your ingredient:
8

We have the following recipes using parmesan:

_________________________
Spaghetti Aglio e Olio

Ingredients:

spaghetti (200g)
garlic (4 cloves)
olive oil (1/4 cup)
red pepper flakes (1 tsp)
parsley (1/4 cup)
to taste (salt)
parmesan (optional)


Directions:

1. Boil spaghetti in salted water according to package instructions.
2. In a pan, heat olive oil over medium and sauté garlic until golden.
3. Add red pepper flakes and cook for another 30 seconds.
4. Drain spaghetti, reserving some pasta water, then toss with garlic oil.
5. Add parsley and some pasta water if needed for smooth consistency.
6. Serve with grated parmesan, if desired.



_________________________
Caesar Salad

Ingredients:

romaine lettuce (1 head)
mayonnaise (1/2 cup)
garlic (2 cloves)
lemon juice (1 tbsp)
Dijon mustard (1 tsp)
anchovy paste (1 tsp)
parmesan (1/2 cup)
croutons (to taste)


Directions:

1. Wash and chop romaine lettuce, then place it in a large bowl.
2. In a separate bowl, mix mayonnaise, garlic, lemon juice, Dijon mustard, and anchovy paste.
3. Toss the lettuce with the dressing until well-coated.
4. Add croutons and parmesan cheese to the salad.
5. Serve immediately, topped with extra parmesan if desired.



_________________________
Chicken Caesar Wrap

Ingredients:

chicken breasts (2)
romaine lettuce (1 head)
Caesar dressing (1/4 cup)
parmesan (1/4 cup)
wraps (2)


Directions:

1. Cook the chicken breasts, then slice into strips.
2. In a bowl, combine lettuce, chicken, Caesar dressing, and parmesan cheese.
3. Place the mixture in a wrap and roll tightly.
4. Serve immediately, optionally with extra dressing on the side.



_________________________
Chicken Alfredo

Ingredients:

chicken breasts (2)
pasta (200g)
butter (1/2 cup)
garlic (2 cloves)
heavy cream (1 cup)
parmesan (1/2 cup)
salt (to taste)
pepper (to taste)
parsley (for garnish)


Directions:

1. Cook pasta according to package instructions, then drain and set aside.
2. Season chicken breasts with salt and pepper, then cook in a skillet over medium heat until golden brown.
3. Remove chicken, slice, and set aside.
4. In the same pan, melt butter and add garlic, cooking for 1-2 minutes.
5. Add heavy cream and bring to a simmer, then stir in parmesan cheese until smooth.
6. Add cooked pasta and chicken to the sauce, toss to coat.
7. Serve with extra parmesan and parsley.

Would you like to:
1- Search other recipes
2- Exit the program
Option: 2

Bye!
