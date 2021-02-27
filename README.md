# Опис програми
Програма створює сервер, на якому можна ввести ім'я користувача твітеру та отримати карту з локаціями декількох людей, на яких він підписаний.

# Опис модулів
* get_json.py :
    модуль містить функцію, яка надсилає запит до twitter api та повертає обєкт з відповідною інформацією про юзера.
* get.location.py :
    модуль містить функції, які генерують список з інформацією про юзерів (ім'я, локація) шукають координати по локації та додають їх у список (ім'я, локація, координати).
* put_users_on_map.py :
    містить функцію, яка генерує карту з маркерами у відповідних координатах.
* server.py :
    створює сервер.
    
# Опис фрагменту з opening_page.html

Html-сторінка "opening_page.html" містить форму для введення імені користувача. Локації декілької із підписок цього користувача будуть згодом відображатись на мапі.
```
<form action="/create_map" autocomplete="off" method="POST">
      <label for="user_name">User name:</label><br>
      <input type="text" id="user_name" name="user_name"><br>
      <input type="submit" value="Submit">
</form>
```
В даному фрагменті коду, ми user_name, яке ввід користувач у форму, передаємо в post запит "/create_map".

# Приклад роботи програми
* Запускаємо модуль server.py, переходимо за посиланням:
![Без імені](https://user-images.githubusercontent.com/73783964/109386011-71bb6700-7900-11eb-8bf1-f087b7c582b9.png)

* Вводио ім'я користувача:
![Без імені1](https://user-images.githubusercontent.com/73783964/109386071-d8408500-7900-11eb-9c49-fc79e404b142.png)

* Дивимось локації декількох друзів користувача на карті:
![Без імені2](https://user-images.githubusercontent.com/73783964/109386072-daa2df00-7900-11eb-9e41-de37a250414d.png)
