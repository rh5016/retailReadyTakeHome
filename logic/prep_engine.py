import json
import os

script_dir = os.path.dirname(__file__)
rules_path = os.path.join(script_dir, '..', 'data', 'hanger_rules.json')

with open(rules_path, 'r') as f:
    rules = json.load(f)

def prep_instructions(product_type, category, size):
    # defaults
    instructions = {
        "hanger_code": None,
        "presentation": "CLOSED",
        "sizer_required": True,
        "special_note": "None"
    }

    # hanger lookup
    if product_type in rules["hanger_map"] and category in rules["hanger_map"][product_type]:
        instructions["hanger_code"] = rules["hanger_map"][product_type][category]

    if product_type in rules["exceptions"]["open_presentation"]:
        instructions["presentation"] = "OPEN"

    if product_type in rules["exceptions"]["no_sizer"]:
        instructions["sizer_required"] = False

    if product_type in rules["exceptions"]["special_notes"]:
        instructions["special_note"] = rules["exceptions"]["special_notes"][product_type]

    if product_type == "Youth Bottoms" and category == "YOUTH" and size == "XXS":
        instructions["special_note"] = "Acceptable hangers are 6008 or 6010."
        instructions["hanger_code"] = "6008/6010"

    if not instructions["hanger_code"]:
        instructions["special_note"] = "Hanger code not found for this product/category combination."

    return instructions