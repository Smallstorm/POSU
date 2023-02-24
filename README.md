# POSU


## Задание 1.

Разработать программу, которая читает JSON-документ input.json из текущего
каталога, модифицирует этот документ и выводит результат в терминал. Можно
считать, что элементом верхнего уровня в документе всегда является массив.
Внутри массива могут находиться любые элементы (числа, строки, массивы,
объекты, и т.д.). Программа должна модифицировать эти элементы по следующим
правилам.
1. Из массива удаляются все элементы с четным индексом.
2. Все ключи словаря переводятся в верхний регистр.
3. Из каждой строки удаляется вторая половина символов.
4. Остальные элементы остаются без изменений.

Пример.
Исходный input.json:
```
[
	[2,3,4,5],
	{
		"key1" : 34534,
		"key2" : "text for key1",
		"key3" : [234, 345, 345]
	},
	{
		"key1" : 34534,
		"key2" : "text for key2",
		"key3" : [234, 345, 345]
	},
	3453,
	"some text, some more text",
	true
]

Ожидаемый результат:
[
	[
		3,
		5
	],
	{
		"KEY1": 34534,
		"KEY2": "text for key1",
		"KEY3": [
			234,
			345,
			345
		]
	},
	{
		"KEY1": 34534,
		"KEY2": "text for key2",
		"KEY3": [
			234,
			345,
			345
		]
	},
	3453,
	"some text, s",
	true
]
```