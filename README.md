При запуску Parser/Parse_and_save_to_db.py данні про компанії скачуються і в БД створюються відповідні таблиці з назвами компанії. Потім в ці таблиці імопртуються csv файли цих компаній.
Далі створюється проект Django для REST сервіса.
Командою python manage.py inspectdb > models.py таблиці з нашої бази імпортуються в моделі джанго для подальшої роботи з ними.