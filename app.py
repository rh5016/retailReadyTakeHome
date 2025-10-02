from logic.prep_engine import prep_instructions
from logic.shipping_engine import shipping_method


shipment_products = [
    {"id": 1, "type": "Fleece Bottoms", "category": "WOMENS", "size": "M"},
    {"id": 2, "type": "Hunting Pants", "category": "MENS", "size": "L"},
    {"id": 3, "type": "Life Jackets", "category": "YOUTH", "size": "S"},
]

shipment_cartons = [
    {"carton_id": "C101", "actual_weight": 15, "length": 12, "width": 12, "height": 12, "contents": [1]},
    {"carton_id": "C102", "actual_weight": 20, "length": 14, "width": 14, "height": 10, "contents": [2, 3]}
]


def process_shipment(products, cartons):
    print("NEW SHIPMENT")


    print("\nSTEP 1: PREPARATION INSTRUCTIONS\n")

    for product in products:
        instructions = prep_instructions(product["type"], product["category"], product["size"])
        print(f"  -> For Product: {product['type']} ({product['category']} / {product['size']})")
        print(f"     - Hanger Code: {instructions['hanger_code']}")
        print(f"     - Presentation: {instructions['presentation']}")
        print(f"     - Sizer Required: {instructions['sizer_required']}")
        if instructions['special_note'] != "None":
            print(f"     - NOTE: {instructions['special_note']}")

    print("\nSTEP 2: SHIPPING METHOD\n")

    shipping_method = shipping_method(cartons)
    print(f"The required shipping method is -> [ {shipping_method} ]")


    if shipping_method == "PARCEL COLLECT":
        print("\n[ACTION]: Ship via PARCEL.")
        print("1. Log in to the TMS Portal.")
        print("2. Create a routing request for a PARCEL shipment.")
        print("3. Use the FedEx account number provided by TMS.")
    else:
        print("\n[ACTION]: Ship via LTL.")
        print("1. Palletize and shrink-wrap all cartons.")
        print("2. Log in to the TMS Portal.")
        print("3. Create a routing request for an LTL shipment.")
        print("4. Call the assigned LTL carrier to schedule pickup.")
    


if __name__ == "__main__":
    process_shipment(shipment_products, shipment_cartons)
