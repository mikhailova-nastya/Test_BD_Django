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


# Общие комментарии

Лишние элементы не стоит добавлять в приложение. В данном случае это Django и непосредственно база данных db.sqlite3.
Для игнорирования локальных файлов в git есть .gitignore. Типовой .gitignore для Python - https://github.com/github/gitignore/blob/main/Python.gitignore
Обычно стоит добавлять его в проект и в него уже накидывать дополнительные файлы, которые нужны только локально

* Нейминг обычно очень важен. Например, приложение называется
