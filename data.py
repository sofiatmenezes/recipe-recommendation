class Recipe:
    def __init__(self,name):
        self.name=name
        self.instructions = []
        self.ingredients= []

    def __repr__(self):
        description="\n\n_________________________\n"+self.name + "\n\nIngredients:\n\n"
        for ing in self.ingredients:
            description += f"{ing[1]} ({ing[0]})\n"
        description += "\n\nDirections:\n\n"
        i=1
        for inst in self.instructions:
            description += f"{i}. {inst}\n"
            i += 1
        return description

    def add_instruction(self,instruction):
        #input is a single instruction str
        self.instructions.append(instruction)

    def add_ingredients(self,ingdts):
        #input is a list of ingredients, in which each ingredient is a list [quantity, name].
        self.ingredients += ingdts

        

classic_pancakes = Recipe("Classic Pancakes")
spaghetti_aglio_olio = Recipe("Spaghetti Aglio e Olio")
caprese_salad = Recipe("Caprese Salad")
chicken_stir_fry = Recipe("Chicken Stir-Fry")
veggie_tacos = Recipe("Veggie Tacos")
tomato_soup = Recipe("Tomato Soup")
garlic_butter_shrimp = Recipe("Garlic Butter Shrimp")
vegetable_curry = Recipe("Vegetable Curry")
grilled_cheese = Recipe("Grilled Cheese Sandwich")
chocolate_chip_cookies = Recipe("Chocolate Chip Cookies")



chocolate_chip_cookies.add_instruction("Preheat oven to 350°F (175°C).")
chocolate_chip_cookies.add_instruction("Cream butter and sugar together until light and fluffy.")
chocolate_chip_cookies.add_instruction("Add egg and mix well, then stir in dry ingredients (flour, baking soda, salt).")
chocolate_chip_cookies.add_instruction("Fold in chocolate chips.")
chocolate_chip_cookies.add_instruction("Drop spoonfuls of dough onto a baking sheet and bake for 10 minutes.")
chocolate_chip_cookies.add_instruction("Let cool on a wire rack before serving.")

vegetable_curry.add_instruction("Heat olive oil in a pot and sauté onions until translucent.")
vegetable_curry.add_instruction("Add mixed vegetables, curry powder, and a pinch of salt.")
vegetable_curry.add_instruction("Pour in coconut milk and bring to a simmer.")
vegetable_curry.add_instruction("Cook for 20 minutes or until vegetables are tender.")
vegetable_curry.add_instruction("Season with salt and pepper to taste, then serve hot over rice.")

garlic_butter_shrimp.add_instruction("Heat butter and olive oil in a skillet over medium heat.")
garlic_butter_shrimp.add_instruction("Add garlic and cook for 30 seconds until fragrant.")
garlic_butter_shrimp.add_instruction("Add shrimp and cook for 2-3 minutes on each side until pink.")
garlic_butter_shrimp.add_instruction("Drizzle lemon juice and toss shrimp to coat evenly.")
garlic_butter_shrimp.add_instruction("Season with salt and pepper, then garnish with parsley.")
garlic_butter_shrimp.add_instruction("Serve immediately with pasta or rice.")

tomato_soup.add_instruction("Heat olive oil in a pot over medium heat and sauté onion and garlic until soft.")
tomato_soup.add_instruction("Add crushed tomatoes and vegetable broth, bring to a simmer.")
tomato_soup.add_instruction("Season with salt and pepper, then simmer for 15 minutes.")
tomato_soup.add_instruction("Blend soup until smooth using an immersion blender or regular blender.")
tomato_soup.add_instruction("Serve hot with fresh basil leaves for garnish.")

veggie_tacos.add_instruction("Warm tortillas on a skillet for about 30 seconds on each side.")
veggie_tacos.add_instruction("Mash avocado with a pinch of salt and juice from half the lime.")
veggie_tacos.add_instruction("Heat black beans and corn in a pan until warmed through.")
veggie_tacos.add_instruction("Spread mashed avocado on the tortillas, then top with beans and corn.")
veggie_tacos.add_instruction("Add shredded lettuce and salsa on top.")
veggie_tacos.add_instruction("Squeeze lime juice over the tacos and serve immediately.")

chicken_stir_fry.add_instruction("Heat oil in a pan over medium-high heat.")
chicken_stir_fry.add_instruction("Add chicken and cook until browned, then remove and set aside.")
chicken_stir_fry.add_instruction("In the same pan, sauté onions and bell pepper until tender.")
chicken_stir_fry.add_instruction("Return chicken to the pan and add soy sauce and oyster sauce.")
chicken_stir_fry.add_instruction("Mix cornstarch with a little water and add to the pan, stir until thickened.")
chicken_stir_fry.add_instruction("Serve hot with steamed rice.")

caprese_salad.add_instruction("Slice tomatoes and mozzarella into even rounds.")
caprese_salad.add_instruction("Arrange tomato and mozzarella slices alternately on a plate.")
caprese_salad.add_instruction("Tuck basil leaves between the slices.")
caprese_salad.add_instruction("Drizzle olive oil and balsamic vinegar over the salad.")
caprese_salad.add_instruction("Season with salt and pepper to taste.")
caprese_salad.add_instruction("Serve immediately as a refreshing side dish.")

spaghetti_aglio_olio.add_instruction("Boil spaghetti in salted water according to package instructions.")
spaghetti_aglio_olio.add_instruction("In a pan, heat olive oil over medium and sauté garlic until golden.")
spaghetti_aglio_olio.add_instruction("Add red pepper flakes and cook for another 30 seconds.")
spaghetti_aglio_olio.add_instruction("Drain spaghetti, reserving some pasta water, then toss with garlic oil.")
spaghetti_aglio_olio.add_instruction("Add parsley and some pasta water if needed for smooth consistency.")
spaghetti_aglio_olio.add_instruction("Serve with grated parmesan, if desired.")

classic_pancakes.add_instruction("In a bowl, mix flour, sugar, baking powder, and salt.")
classic_pancakes.add_instruction("In a separate bowl, whisk egg, milk, and melted butter.")
classic_pancakes.add_instruction("Combine wet and dry ingredients, stirring until smooth.")
classic_pancakes.add_instruction("Heat a pan on medium, pour batter, and cook until bubbles form.")
classic_pancakes.add_instruction("Flip the pancakes and cook for another 1-2 minutes.")
classic_pancakes.add_instruction("Serve with syrup or fruit.")


classic_pancakes.add_ingredients([["1 cup", "flour"], ["2 tbsp", "sugar"], ["1 tsp", "baking powder"], ["1/2 tsp", "salt"], ["1", "egg"], ["1 cup", "milk"], ["2 tbsp", "butter"]])
spaghetti_aglio_olio.add_ingredients([["200g", "spaghetti"], ["4 cloves", "garlic"], ["1/4 cup", "olive oil"], ["1 tsp", "red pepper flakes"], ["1/4 cup", "parsley"], ["salt", "to taste"], ["optional","parmesan"]])
caprese_salad.add_ingredients([["2", "tomatoes"], ["200g", "mozzarella"], ["fresh basil leaves", "as needed"], ["1 tbsp", "olive oil"], ["1 tbsp", "balsamic vinegar"], ["salt", "to taste"], ["pepper", "to taste"]])
chicken_stir_fry.add_ingredients([["2", "chicken breasts"], ["1", "bell pepper"], ["1", "onion"], ["2 tbsp", "soy sauce"], ["1 tbsp", "oyster sauce"], ["1 tbsp", "cornstarch"], ["1 tbsp", "vegetable oil"]])
veggie_tacos.add_ingredients([["2", "corn tortillas"], ["1/2 cup", "black beans"], ["1/2 cup", "corn kernels"], ["1", "avocado"], ["1/4 cup", "salsa"], ["1/4 cup", "shredded lettuce"], ["1", "lime"]])
tomato_soup.add_ingredients([["1 can", "crushed tomatoes"], ["1/2", "onion"], ["2 cloves", "garlic"], ["1 cup", "vegetable broth"], ["1 tbsp", "olive oil"], ["to taste", "salt"], ["to taste", "pepper"], ["for garnish","fresh basil"]])
garlic_butter_shrimp.add_ingredients([["500g", "shrimp"], ["4 cloves", "garlic"], ["3 tbsp", "butter"], ["1 tbsp", "olive oil"], ["1 tbsp", "lemon juice"], ["for garnish","parsley"], ["to taste", "salt"], ["to taste", "pepper"]])
vegetable_curry.add_ingredients([["1 cup", "coconut milk"], ["1 cup", "mixed vegetables"], ["1", "onion"], ["1 tbsp", "curry powder"], ["1 tbsp", "olive oil"], ["to taste", "salt"], ["to taste", "pepper"]])
grilled_cheese.add_ingredients([["2 slices", "bread"], ["2 slices", "cheese"], ["1 tbsp", "butter"]])
chocolate_chip_cookies.add_ingredients([["1 cup", "butter"], ["1 cup", "sugar"], ["2 cups", "flour"], ["1 tsp", "baking soda"], ["1/2 tsp", "salt"], ["1 cup", "chocolate chips"], ["1", "egg"]])

banana_bread = Recipe("Banana Bread")
banana_bread.add_instruction("Preheat the oven to 350°F (175°C) and grease a loaf pan.")
banana_bread.add_instruction("In a bowl, mash the ripe bananas until smooth.")
banana_bread.add_instruction("Add sugar, egg, melted butter, and vanilla extract to the bananas and mix.")
banana_bread.add_instruction("In another bowl, combine flour, baking soda, and salt.")
banana_bread.add_instruction("Gradually mix the dry ingredients into the wet ingredients until just combined.")
banana_bread.add_instruction("Pour the batter into the loaf pan and bake for 60-65 minutes.")
banana_bread.add_instruction("Let the bread cool before slicing and serving.")
banana_bread.add_ingredients([["2", "bananas"], ["1 cup", "sugar"], ["1", "egg"], ["1/2 cup", "butter"], ["1 tsp", "vanilla extract"], ["2 cups", "flour"], ["1 tsp", "baking soda"], ["1/2 tsp", "salt"]])

vegetable_fried_rice = Recipe("Vegetable Fried Rice")
vegetable_fried_rice.add_instruction("Cook rice according to package directions and let it cool.")
vegetable_fried_rice.add_instruction("Heat oil in a wok and sauté diced carrots, peas, and onions until tender.")
vegetable_fried_rice.add_instruction("Add garlic and ginger, cook for another 30 seconds.")
vegetable_fried_rice.add_instruction("Push vegetables to one side of the wok and scramble eggs on the other side.")
vegetable_fried_rice.add_instruction("Add cooled rice to the wok, then pour in soy sauce and sesame oil.")
vegetable_fried_rice.add_instruction("Mix everything together and cook for 2-3 minutes.")
vegetable_fried_rice.add_instruction("Garnish with green onions and serve hot.")
vegetable_fried_rice.add_ingredients([["2 cups", "cooked rice"], ["1/2 cup", "peas"], ["1/2 cup", "carrots"], ["1/2", "onion"], ["2 cloves", "garlic"], ["1 tbsp", "ginger"], ["2", "eggs"], ["2 tbsp", "soy sauce"], ["1 tbsp", "sesame oil"], ["green onions", "for garnish"]])

caesar_salad = Recipe("Caesar Salad")
caesar_salad.add_instruction("Wash and chop romaine lettuce, then place it in a large bowl.")
caesar_salad.add_instruction("In a separate bowl, mix mayonnaise, garlic, lemon juice, Dijon mustard, and anchovy paste.")
caesar_salad.add_instruction("Toss the lettuce with the dressing until well-coated.")
caesar_salad.add_instruction("Add croutons and parmesan cheese to the salad.")
caesar_salad.add_instruction("Serve immediately, topped with extra parmesan if desired.")
caesar_salad.add_ingredients([["1 head", "romaine lettuce"], ["1/2 cup", "mayonnaise"], ["2 cloves", "garlic"], ["1 tbsp", "lemon juice"], ["1 tsp", "Dijon mustard"], ["1 tsp", "anchovy paste"], ["1/2 cup", "parmesan"], ["to taste", "croutons"]])

beef_tacos = Recipe("Beef Tacos")
beef_tacos.add_instruction("In a pan, brown the ground beef over medium heat.")
beef_tacos.add_instruction("Drain any excess fat, then add taco seasoning and water.")
beef_tacos.add_instruction("Simmer the beef mixture for 5-7 minutes until thickened.")
beef_tacos.add_instruction("Warm the taco shells and fill with the beef mixture.")
beef_tacos.add_instruction("Top with shredded cheese, lettuce, salsa, and sour cream.")
beef_tacos.add_ingredients([["500g", "ground beef"], ["1 packet", "taco seasoning"], ["1/4 cup", "water"], ["8", "taco shells"], ["1/2 cup", "shredded cheese"], ["1/2 cup", "shredded lettuce"], ["1/4 cup", "salsa"], ["2 tbsp", "sour cream"]])

lemonade = Recipe("Lemonade")
lemonade.add_instruction("In a saucepan, make a simple syrup by combining water and sugar. Heat until sugar is dissolved.")
lemonade.add_instruction("Juice the lemons until you have about 1 cup of lemon juice.")
lemonade.add_instruction("Mix the lemon juice, simple syrup, and cold water in a large pitcher.")
lemonade.add_instruction("Stir well and refrigerate until chilled.")
lemonade.add_instruction("Serve over ice with lemon slices for garnish.")
lemonade.add_ingredients([["1 cup", "sugar"], ["1 cup", "water"], ["1 cup", "fresh lemon juice"], ["4 cups", "cold water"], ["lemon slices", "for garnish"]])

chicken_alfredo = Recipe("Chicken Alfredo")
chicken_alfredo.add_instruction("Cook pasta according to package instructions, then drain and set aside.")
chicken_alfredo.add_instruction("Season chicken breasts with salt and pepper, then cook in a skillet over medium heat until golden brown.")
chicken_alfredo.add_instruction("Remove chicken, slice, and set aside.")
chicken_alfredo.add_instruction("In the same pan, melt butter and add garlic, cooking for 1-2 minutes.")
chicken_alfredo.add_instruction("Add heavy cream and bring to a simmer, then stir in parmesan cheese until smooth.")
chicken_alfredo.add_instruction("Add cooked pasta and chicken to the sauce, toss to coat.")
chicken_alfredo.add_instruction("Serve with extra parmesan and parsley.")
chicken_alfredo.add_ingredients([["2", "chicken breasts"], ["200g", "pasta"], ["1/2 cup", "butter"], ["2 cloves", "garlic"], ["1 cup", "heavy cream"], ["1/2 cup", "parmesan"], ["to taste","salt"], ["to taste","pepper"], ["for garnish","parsley"]])

pineapple_smoothie = Recipe("Pineapple Smoothie")
pineapple_smoothie.add_instruction("In a blender, combine frozen pineapple chunks, banana, and yogurt.")
pineapple_smoothie.add_instruction("Add coconut water or milk for a smoother consistency.")
pineapple_smoothie.add_instruction("Blend until smooth and creamy.")
pineapple_smoothie.add_instruction("Pour into glasses and serve immediately.")
pineapple_smoothie.add_ingredients([["1 cup", "frozen pineapple chunks"], ["1", "banana"], ["1/2 cup", "yogurt"], ["1/2 cup", "coconut water or milk"]])

chicken_caesar_wrap = Recipe("Chicken Caesar Wrap")
chicken_caesar_wrap.add_instruction("Cook the chicken breasts, then slice into strips.")
chicken_caesar_wrap.add_instruction("In a bowl, combine lettuce, chicken, Caesar dressing, and parmesan cheese.")
chicken_caesar_wrap.add_instruction("Place the mixture in a wrap and roll tightly.")
chicken_caesar_wrap.add_instruction("Serve immediately, optionally with extra dressing on the side.")
chicken_caesar_wrap.add_ingredients([["2", "chicken breasts"], ["1 head", "romaine lettuce"], ["1/4 cup", "Caesar dressing"], ["1/4 cup", "parmesan"], ["2", "wraps"]])

tom_yum_soup = Recipe("Tom Yum Soup")
tom_yum_soup.add_instruction("Bring water and vegetable broth to a boil in a pot.")
tom_yum_soup.add_instruction("Add lemongrass, kaffir lime leaves, and galangal, and simmer for 5 minutes.")
tom_yum_soup.add_instruction("Add mushrooms, shrimp, and chili paste, then cook until shrimp are done.")
tom_yum_soup.add_instruction("Stir in fish sauce, lime juice, and cilantro.")
tom_yum_soup.add_instruction("Serve hot with a side of steamed rice.")
tom_yum_soup.add_ingredients([["4 cups", "water"], ["2 cups", "vegetable broth"], ["2 stalks", "lemongrass"], ["4", "kaffir lime leaves"], ["2 tbsp", "chili paste"], ["200g", "shrimp"], ["1 cup", "mushrooms"], ["1 tbsp", "fish sauce"], ["1 tbsp", "lime juice"], ["1/4 cup", "cilantro"]])

mango_salsa = Recipe("Mango Salsa")
mango_salsa.add_instruction("Dice mangoes, red onion, and bell peppers.")
mango_salsa.add_instruction("Chop cilantro and jalapeño, then combine all ingredients in a bowl.")
mango_salsa.add_instruction("Add lime juice, salt, and pepper, and mix well.")
mango_salsa.add_instruction("Serve with tortilla chips or as a topping for grilled meats.")
mango_salsa.add_ingredients([["2", "mangoes"], ["1/2", "red onion"], ["1", "bell pepper"], ["1/4 cup", "cilantro"], ["1", "jalapeño"], ["1 tbsp", "lime juice"], ["to taste", "salt"], ["to taste", "pepper"]])

bacalhau_a_bras = Recipe("Bacalhau à Brás")
bacalhau_a_bras.add_instruction("Soak the salted cod in water overnight, then drain and shred it.")
bacalhau_a_bras.add_instruction("In a pan, sauté onions and garlic in olive oil until golden.")
bacalhau_a_bras.add_instruction("Add the shredded cod and cook for 5 minutes.")
bacalhau_a_bras.add_instruction("Add the potatoes and stir until they begin to crisp.")
bacalhau_a_bras.add_instruction("In a bowl, beat eggs and pour over the cod mixture.")
bacalhau_a_bras.add_instruction("Stir gently until eggs are cooked but still soft.")
bacalhau_a_bras.add_instruction("Garnish with parsley and black olives. Serve hot.")
bacalhau_a_bras.add_ingredients([["400g", "salted codfish"], ["2", "onions"], ["2 cloves", "garlic"], ["2 tbsp", "olive oil"], ["3", "potatoes"], ["4", "eggs"], ["for garnish","parsley"], ["for garnish","black olives"]])

caldo_verde = Recipe("Caldo Verde")
caldo_verde.add_instruction("In a pot, sauté onions and garlic in olive oil until soft.")
caldo_verde.add_instruction("Add the potatoes and cook for 5 minutes.")
caldo_verde.add_instruction("Add water and simmer until the potatoes are tender.")
caldo_verde.add_instruction("Mash the potatoes until smooth, then return to the pot.")
caldo_verde.add_instruction("Add the kale and chorizo slices, and cook for another 10 minutes.")
caldo_verde.add_instruction("Season with salt and pepper, then serve hot with crusty bread.")
caldo_verde.add_ingredients([["1", "onion"], ["2 cloves", "garlic"], ["4", "potatoes"], ["200g", "kale"], ["150g", "chorizo"], ["1 tbsp", "olive oil"], ["salt", "to taste"], ["pepper", "to taste"], ["as needed", "water"]])

feijoada = Recipe("Feijoada")
feijoada.add_instruction("Soak the beans overnight, then drain and set aside.")
feijoada.add_instruction("In a large pot, sauté onions, garlic, and chorizo in olive oil.")
feijoada.add_instruction("Add the beans, bay leaves, and enough water to cover. Simmer for 1-2 hours.")
feijoada.add_instruction("Add the pork ribs and sausages, and cook until the meat is tender.")
feijoada.add_instruction("Season with salt, pepper, and paprika to taste.")
feijoada.add_instruction("Serve with rice and orange slices.")
feijoada.add_ingredients([["500g", "beans"], ["1", "onion"], ["2 cloves", "garlic"], ["2", "chorizos"], ["300g", "pork ribs"], ["2", "sausages"], ["2", "bay leaves"], ["1 tbsp", "olive oil"], ["to taste", "salt"], ["to taste", "pepper"], ["to taste","paprika"], ["for garnish","orange slices"], ["for serving","rice"]])

bacalhau_com_natas = Recipe("Bacalhau com Natas")
bacalhau_com_natas.add_instruction("Soak and shred the salted cod.")
bacalhau_com_natas.add_instruction("In a pan, sauté onions and garlic in olive oil until soft.")
bacalhau_com_natas.add_instruction("Add the cod and cook for 5 minutes.")
bacalhau_com_natas.add_instruction("In a bowl, mix the cream with eggs, nutmeg, salt, and pepper.")
bacalhau_com_natas.add_instruction("Layer the cod mixture and the cream mixture in a baking dish.")
bacalhau_com_natas.add_instruction("Bake at 180°C for 25-30 minutes until golden and bubbly.")
bacalhau_com_natas.add_ingredients([["400g", "salted codfish"], ["1", "onion"], ["2 cloves", "garlic"], ["1 tbsp", "olive oil"], ["1 cup", "heavy cream"], ["2", "eggs"], ["1/2 tsp", "nutmeg"], ["to taste", "salt"], ["to taste", "pepper"]])

arroz_de_marisco = Recipe("Arroz de Marisco")
arroz_de_marisco.add_instruction("In a large pan, sauté onions, garlic, and bell peppers in olive oil.")
arroz_de_marisco.add_instruction("Add the rice and cook for 2 minutes, stirring frequently.")
arroz_de_marisco.add_instruction("Add the tomatoes, seafood stock, and water, and bring to a boil.")
arroz_de_marisco.add_instruction("Add shrimp, mussels, and clams, then simmer for 15-20 minutes until the rice is tender.")
arroz_de_marisco.add_instruction("Season with salt, pepper, and parsley, and serve hot.")
arroz_de_marisco.add_ingredients([["1", "onion"], ["2 cloves", "garlic"], ["1", "bell pepper"], ["2 tbsp", "olive oil"], ["2 cups", "rice"], ["2 cups", "seafood stock"], ["1 cup", "water"], ["200g", "shrimp"], ["200g", "mussels"], ["200g", "clams"], ["2", "tomatoes"], ["to taste", "salt"], ["to taste", "pepper"], ["for garnish","parsley"]])

pasteis_de_nata = Recipe("Pastéis de Nata")
pasteis_de_nata.add_instruction("Preheat the oven to 220°C and grease muffin tins.")
pasteis_de_nata.add_instruction("Roll out puff pastry and cut into circles to fit the muffin cups.")
pasteis_de_nata.add_instruction("In a saucepan, combine sugar, milk, and flour, and heat until thickened.")
pasteis_de_nata.add_instruction("Whisk the egg yolks and add to the mixture, stirring constantly.")
pasteis_de_nata.add_instruction("Pour the custard into the pastry shells and bake for 10-15 minutes until golden.")
pasteis_de_nata.add_instruction("Let the tarts cool slightly before serving.")
pasteis_de_nata.add_ingredients([["1 sheet", "puff pastry"], ["1 cup", "sugar"], ["1 cup", "milk"], ["2 tbsp", "flour"], ["6", "egg yolks"], ["1 tsp", "vanilla extract"]])

polvo_a_lagareiro = Recipe("Polvo à Lagareiro")
polvo_a_lagareiro.add_instruction("Boil the octopus in salted water for 45-60 minutes until tender.")
polvo_a_lagareiro.add_instruction("Drain and cut the octopus into pieces.")
polvo_a_lagareiro.add_instruction("Place the octopus in a baking dish and drizzle with olive oil, garlic, and herbs.")
polvo_a_lagareiro.add_instruction("Roast in the oven at 200°C for 15-20 minutes.")
polvo_a_lagareiro.add_instruction("Serve with roasted potatoes and a drizzle of olive oil.")
polvo_a_lagareiro.add_ingredients([["1kg", "octopus"], ["1 cup", "olive oil"], ["3 cloves", "garlic"], ["1 tbsp", "oregano"], ["1 tbsp", "parsley"], ["500g", "potatoes"]])

alheira = Recipe("Alheira")
alheira.add_instruction("In a pan, sauté onions and garlic in olive oil until translucent.")
alheira.add_instruction("Add minced chicken and pork, and cook until browned.")
alheira.add_instruction("Add bread crumbs and season with salt, pepper, and paprika.")
alheira.add_instruction("Stuff the mixture into sausage casings and tie them off.")
alheira.add_instruction("Simmer the sausages in water for 45 minutes.")
alheira.add_instruction("Grill or pan-fry the sausages before serving.")
alheira.add_ingredients([["500g", "chicken"], ["500g", "pork"], ["1", "onion"], ["2 cloves", "garlic"], ["1 cup", "bread crumbs"], ["1 tbsp", "paprika"], ["salt", "to taste"], ["pepper", "to taste"], ["sausage casings", "as needed"]])

ameijoas_a_bulhao_pato = Recipe("Amêijoas à Bulhão Pato")
ameijoas_a_bulhao_pato.add_instruction("In a pan, sauté garlic in olive oil until fragrant.")
ameijoas_a_bulhao_pato.add_instruction("Add the clams and cook until they begin to open.")
ameijoas_a_bulhao_pato.add_instruction("Add white wine, lemon juice, and chopped cilantro, and cook for 5 more minutes.")
ameijoas_a_bulhao_pato.add_instruction("Season with salt and pepper and serve with crusty bread.")
ameijoas_a_bulhao_pato.add_ingredients([["1kg", "clams"], ["2 cloves", "garlic"], ["2 tbsp", "olive oil"], ["1/2 cup", "white wine"], ["1 tbsp", "lemon juice"], ["1/4 cup", "cilantro"], ["to taste","salt"], ["totaste","pepper"]])

sardinhas_assadas = Recipe("Sardinhas Assadas")
sardinhas_assadas.add_instruction("Clean and gut the sardines, then season with salt and olive oil.")
sardinhas_assadas.add_instruction("Preheat the grill and cook the sardines for 4-5 minutes on each side.")
sardinhas_assadas.add_instruction("Serve with lemon wedges and a drizzle of olive oil.")
sardinhas_assadas.add_ingredients([["10", "sardines"], ["2 tbsp", "olive oil"], ["to taste","salt"], ["1", "lemon"]])


recipe_book = [
    bacalhau_a_bras,
    caldo_verde,
    feijoada,
    bacalhau_com_natas,
    arroz_de_marisco,
    pasteis_de_nata,
    polvo_a_lagareiro,
    alheira,
    ameijoas_a_bulhao_pato,
    sardinhas_assadas,
    classic_pancakes,
    spaghetti_aglio_olio,
    caprese_salad,
    chicken_stir_fry,
    veggie_tacos,
    tomato_soup,
    garlic_butter_shrimp,
    vegetable_curry,
    grilled_cheese,
    chocolate_chip_cookies,
    caesar_salad,
    vegetable_fried_rice,
    banana_bread,
    mango_salsa,
    tom_yum_soup,
    chicken_caesar_wrap,
    pineapple_smoothie,
    chicken_alfredo,
    lemonade,
    beef_tacos]