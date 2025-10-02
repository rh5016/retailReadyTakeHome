import math

def shipping_method(cartons):
    total_cartons = len(cartons)
    total_actual_weight = 0
    total_dimensional_weight = 0

    for carton in cartons:
        total_actual_weight += carton["actual_weight"]
        
        # calculate dimensional weight per carton (14.2.7)
        dim_weight = math.ceil((carton["length"] * carton["width"] * carton["height"]) / 350)
        total_dimensional_weight += dim_weight

    # billable weight is the greater of the two
    billable_weight = max(total_actual_weight, total_dimensional_weight)

    # Rules from 14.2.7

    # Check total shipment limits
    if billable_weight > 110 or total_cartons > 16:
        return "LTL / TRUCKLOAD"

    # Check individual carton limits
    for carton in cartons:
        girth = (2 * carton["width"]) + (2 * carton["height"])
        if (
            carton["actual_weight"] > 150 or
            (carton["length"] + girth) > 130 or
            carton["length"] > 96
        ):
            # if even one carton is oversized, the entire shipment is ineligible for parcel
            return "LTL / TRUCKLOAD"
            
    return "PARCEL COLLECT"