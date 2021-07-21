import autoit, time
# ждем 10 секунд и жмем кнопи из файла
time.sleep(10)
#autoit.send("hello world{!} чсч аыаы аааццукцец ецецун ссс")
f = open(f"zxc.txt", 'r', encoding="utf-8")

for word in f:
    autoit.send(word)
    time.sleep(5)