we break it up into two parts:
1. product preparation
2. shipment


inputs needed: list of porducts.
for each product, we need product_type, gender, size
for each carton: actual_weight, length, width, height

from section 5.3:
determines the VAS requirements for each piece of apparel.
output: set of instructions for the worker on how to pack.

function 1: get_prep_instructions:
    1. we need default instructions
    2. hanger lookup from table
    3. handel exceptions

function 2: shipping_method:
    1. calculate the total shipment metrics
    2. check parcel 
    3. pick method