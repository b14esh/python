import re

def pp():
    """" xxxx """
    print("#-----------------------------------------------")
pp()

mytext = "Vasia aaaaaaaa 1972, Koli - 1972 : Olesy 1981, aaaa@intel.com, " \
         "bbbbbb@intel.com, PPP hhhhh, 1982, ccccccccccccccccc@ya.ru, Olesya , " \
          "hgjgfjfyj@incte.com, vasya@yandex.net, hello hello, Misha #43 1984" \
          "Vladimir 1977, Irina, 2001, annnn@intel.com, eeeeee@yandex.com" \
          "oooooo@hotmail.gov, gggggggg@gov.gov, tutututut@giv.hot"

"""
\d = Any Digit 0-9 / Любая цифра
\D = Any non DIGIT / Любой символ но не цифра
\w = Any Alphabet simvol / Любая буква [A-Z a-z]
\W = Any non Alphabet simvol / Любой символ но не буквы
\s = breakespace  / пробел
\S = breakespace  / не пробел

[0-9][0-9][0-9][0-9] - четыре цифры подряд
[0-9][0-9][0-9] - три цыфры
[0-9]{3} -  три цыфры
[0-9]{4} -  четыри цыфры

\w{6} - любые слова из шести символов

[A-Z][a-z] - первый символ большой второй маленткий
[A-Z][a-z]+ - первый большой а далее мелких букв сколько угодно 

\. - точка

\w+\.\w+ - искать домены
\w+@\w+\.\w+ - искать почтовые адресса

"""

textlookfor = r"yandex" #шаблон
allresults = re.findall(textlookfor, mytext)
print(allresults)

pp()


textlookfor = r"\d\d\d" #шаблон
allresults = re.findall(textlookfor, mytext)
print(allresults)

pp()

textlookfor = r"[0-9][0-9][0-9]"
allresults = re.findall(textlookfor, mytext)
print(allresults)

pp()

textlookfor = r"[0-9]{3}"
allresults = re.findall(textlookfor, mytext)
print(allresults)

pp()

textlookfor = r"\w{6}"
allresults = re.findall(textlookfor, mytext)
print(allresults)

pp()

textlookfor = r"\w{6}\s"
allresults = re.findall(textlookfor, mytext)
print(allresults)

pp()

textlookfor = r"[A-Z][a-z]+"
allresults = re.findall(textlookfor, mytext)
print(allresults)

pp()

textlookfor = r"\w+\.\w+"
allresults = re.findall(textlookfor, mytext)
print(allresults)

pp()

textlookfor = r"@\w+\.\w+"
allresults = re.findall(textlookfor, mytext)
print(allresults)


pp()

textlookfor = r"\w+@\w+\.\w+"
allresults = re.findall(textlookfor, mytext)
print(allresults)




