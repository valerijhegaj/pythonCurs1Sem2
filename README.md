Специализация команд
1.exit - завершает работу программы
2.caesar [-e | -d | -h] pathToRead pathToWrite [shift]
    -e - шифрование шифром
    -d - дешифрование
    -h - взлом шифра цезаря (shift не надо вводить)
    shift - сдвиг шифрования
3.vigener [-e | -d] pathToRead pathToWrite key
    -e - шифрование
    -d - дешифрование
    keyWord - ключевое слово
4.vernam [-e | -eg | -d] pathToRead pathToKey pathToWrite
    -e - шифрование
    -eg - шифрование с генерацией ключа 
    -d - дешифрование
    path - путь к файлу
    pathToKey - путь к ключу (должен совпадать по длине с файлом)

запуск:
	python3 src/main/main.py
запуск тестов, перейти в test/
	python3 testing.py