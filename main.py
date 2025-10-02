from logic.prep_engine import prep_instructions

product1 = {"type": "Fleece Bottoms", "category": "WOMENS", "size": "M"}
instructions1 = prep_instructions(product1["type"], product1["category"], product1["size"])
print(f"\nProduct: {product1['type']} ({product1['category']})")
print(instructions1)

product2 = {"type": "Hunting Pants", "category": "MENS", "size": "L"}
instructions2 = prep_instructions(product2["type"], product2["category"], product2["size"])
print(f"\nProduct: {product2['type']} ({product2['category']})")
print(instructions2)

product3 = {"type": "Life Jackets", "category": "YOUTH", "size": "S"}
instructions3 = prep_instructions(product3["type"], product3["category"], product3["size"])
print(f"\nProduct: {product3['type']} ({product3['category']})")
print(instructions3)