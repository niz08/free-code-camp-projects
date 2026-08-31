##Free Codecamp Project 2 - Discount Calculator

def apply_discount(price, discount):
    if type(price) != int and type(price) != float:
        msg="The price should be a number"
        return msg
    elif type(discount)!=int and type(discount)!=float:
        msg="The discount should be a number"
        return msg
    elif price <= 0:
        msg="The price should be greater than 0"
        return msg
    elif discount < 0 or discount > 100:
        msg="The discount should be between 0 and 100"
        return msg
    else:
        off=(price*discount)/100
        final=price-off
        return final
