# Test_DB_Django
<b>Django version: </b>Django==4.1.dev20211206065911


<b>DB Structure: </b>

Category: category. 

Product: item, description, category(ref. to Category), price

Customer: email, name

Discount: disc_title, disc_value, category(ref. to Category)

Sell: customer(ref. to Customer), time_of_purchase, product(ref. to Product), amount_of_items, disc(ref. to Discount)

<p>

Links to the reports are located in index.html
