print("Lista zakupów")

shopping = {
    "piekarnia": ["bułki", "chleb", "pączek"],
    "warzywniak": ["marchew", "rukola", "seler"]
}

#iter test

shopping_dict = dict(shopping)

for shop, product in shopping_dict.items():
  print(f"Idę do {shop.capitalize()} i kupuję {product[0].capitalize()}, {product[1].capitalize()}, {product[2].capitalize()}")

print(f"W sumie kupuję {3*2} produktów")

# blue is my favorite colour

print("Wpadł facet do kanału i koniec kawału :)")