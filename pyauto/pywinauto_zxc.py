# pywinauto - модуль для работы с gui, нажимает клавиши
# Русский язык поддерживается
# https://github.com/pywinauto/pywinauto/tree/master/examples - примеры


# Пример открываем блокнот и наченаем печатать
from pywinauto import Application

app = Application().start('notepad.exe')
app.UntitledNotepad.Edit.send_chars('Hello World!') # не нужен GUI context
app.UntitledNotepad.Edit.type_keys('\nTyping to the active window...', with_newlines=True) # нужен GUI context