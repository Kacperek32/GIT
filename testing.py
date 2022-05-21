shopping = {
    "piekarnia": ["bułki", "chleb", "pączek"],
    "warzywniak": ["marchew", "rukola", "seler"]
}
print(shopping)

shopping_dict = dict(shopping)

for shop, product in shopping_dict.items():
  print(f"Idę do {shop.capitalize()} i kupuję {product[0].capitalize()}, {product[1].capitalize()}, {product[2].capitalize()}")

print(f"W sumie kupueję {3*2} produktów")