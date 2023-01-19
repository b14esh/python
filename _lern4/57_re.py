# Мы можем не только искать строки, но и заменять их чем-то другим. 
# Например, давай попробуем удалить из HTML-кода все теги. Для этого используется команда re.sub(pattern,'чем заменять',string)


import re
string = 'Вы можете посмотреть карту сайта <a href="map.php">тут</a>. Посетите также <a href="best.php"раздел</a>'
pattern = r'<(.+?)>'
result = re.sub(pattern,'',string)
print(result)
