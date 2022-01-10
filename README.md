# Test_DB_Django
<b>Django version: </b>Django==4.1.dev20211206065911


<b>DB Structure: </b>

Category: category. 

Product: name, description, category(ref. to Category), price

Customer: email, name

Discount: title, value, category(ref. to Category)


Sell: customer(ref. to Customer), time_of_purchase, product(ref. to Product), amount_of_items, discount(ref. to Discount)




