import os
import readchar
import time
import sys

home_folder = os.path.expanduser("~")
file_path = home_folder + "/Desktop/custom-lang-rus.astro"

while True:
    print("\n" * 100)
    print("""
    Добро пожаловать в: 
    🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
    🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
    🟩🟩🟩\033[1m\033[32m&#$* > Джон\033[32m\033[1m🟩🟩🟩
    🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
    🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩

    СОЗДАТЕЛЬ СЕКРЕТНОГО ЯЗЫКА
     \033[0mОт \033[95mAstroVoid24""")

    choice1 = input("""\033[0mЧто вы хотите сделать?
        ПОЛЬЗОВАТЕЛЬСКИЙ ЯЗЫК → Русский - \"1\"
        Русский → ПОЛЬЗОВАТЕЛЬСКИЙ ЯЗЫК - \"2\"
        СОЗДАТЬ ПОЛЬЗОВАТЕЛЬСКИЙ ЯЗЫК - \"3\"
        Автоматическое создание (не рекомендуется!) - \"4\"
        Ответ: """)

    if choice1 == "3":
        FullLanguage = []
        print(f"""Инструкция:
        Введите символ вашего языка, а затем русскую букву
        и нажмите Enter для перехода к следующей букве.
        Пример: &а *Нажать Enter*
                 %б *Нажать Enter*
        Требуется 50 пар, но в алфавите всего 33 буквы?
        Верно, но есть и другие важные символы, а главное – ЦИФРЫ!
        Дополнительные символы: 1234567890,.=+-%?
        Не используйте \\q, это сломает программу.
        Рекомендуется вводить русские буквы по алфавиту, затем цифры, затем остальные символы.
        Чтобы отправить язык другу, передайте ему файл \"custom-lang-rus.astro\" с рабочего стола,
        он должен поместить его на свой рабочий стол.""")

        for LineLetter in range(50):   # 33 буквы + 10 цифр + 7 знаков = 50
            pair = input(f"Доп. символы: 1234567890,.=+-%? | Пара {LineLetter + 1}:")
            FullLanguage.append(pair)

        with open(file_path, "w") as f:
            for pair in FullLanguage:
                f.write(pair + "\n")

        with open(file_path, "r") as file:
            Review = file.read()
            print("Всё готово!\nПроверьте свой перевод!:")
            time.sleep(1)
            print(Review + "\nНажмите любую клавишу для продолжения")
            key = readchar.readkey()

    if choice1 == "4":
        # Автоматическое создание русского языка (50 пар)
        with open(file_path, "w") as f:
            f.write("""!а
@б
#в
$г
%д
^е
&ё
*ж
(з
)и
_й
-к
+л
=м
[н
]о
{п
}р
|с
:т
;у
'ф
\"х
<ц
>ч
.ш
,щ
/ъ
\\ы
`ь
~э
@ю
#я
A0
B1
C2
D3
E4
F5
G6
H7
I8
J9
K,
L.
M=
N+
O-
P%
Q?""")
        print("Готово! Нажмите любую клавишу для продолжения")
        key = readchar.readkey()

    elif choice1 == "2":
        # Русский → Пользовательский язык
        Translation = {}
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if line:  # пропускаем пустые строки
                    symbol = line[:-1]
                    letter = line[-1]
                    Translation[letter] = symbol

        FromRussian = input("Текст (русский): ")
        result = ""
        for char in FromRussian:
            if char in Translation:
                result += Translation[char]
            else:
                print("Не буду переводить! Не смог найти одну из букв, попробуйте писать строчными буквами, хорошо? Я не буду продолжать,\nпотому что если я продолжу, вы сможете прочитать всё целиком, просто без одного или двух букв и\nя не знаю, кто за этим компьютером!")
                result = ""
                break
        print(f"{FromRussian} -> {result}\nНажмите любую клавишу для продолжения")
        key = readchar.readkey()

    elif choice1 == "1":
        # Пользовательский язык → Русский
        TranslationToRus = {}
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if line:  # пропускаем пустые строки
                    symbol = line[:-1]
                    letter = line[-1]
                    TranslationToRus[symbol] = letter

        ToRussian = input("Текст (на секретном языке): ")
        result = ""
        for char in ToRussian:
            if char in TranslationToRus:
                result += TranslationToRus[char]
            else:
                print("Не буду переводить! Не смог найти одну из букв, попробуйте писать строчными буквами, хорошо? Я не буду продолжать,\nпотому что если я продолжу, вы сможете прочитать всё целиком, просто без одного или двух букв и\nя не знаю, кто за этим компьютером!")
                result = ""
                break
        print(f"{ToRussian} -> {result}\nНажмите любую клавишу для продолжения")
        key = readchar.readkey()

    else:
        print(f"Неправильно написано: {choice1}\n2-секундная пауза")
        time.sleep(2)