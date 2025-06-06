# HY_RU_XML
Библиотечка для генерации XML с морфологической разметкой из выровненного XLSX.

## Зачем это?
Эта библиотека предназначена для оборачивания выровненных текстов, в данном случае на восточноармянском и русском, в XML, поддерживаемый НКРЯ.

С помощью нашего форка библиотеки [razdel](https://github.com/natasha/razdel) предложения на восточноармянском разбиваются на токены, а с помощью [uniparser_eastern_armenian](https://bitbucket.org/timarkh/uniparser-grammar-eastern-armenian/src/master/analyzer/UniParser/) эти токены размечается морфологическими тегами, добавляется перевод и транслитерация. Предложения на русском остаются при этом "сырыми" и добавляются в XML как есть.

Обработку можно запускать из терминала. Достаточно запустить из папки проекта (структура описана ниже) команду:
```shell
python main.py --hye hy --rus ru
```
Здесь значение после `--hye` соответствует названию столбца с предложениями на восточноармянском, после `--rus` -- на русском.

По запуску скрипт итеративно обработает каждый файл в папке `input` (опять же, структура проекта описана ниже) и в результате генерируются XML файлы и txt-файл со статистикой, где для каждого текста будет указано количество предложений и суммарное количество слов на восточноармянском и русском языках.  

Чтобы воспользоваться библиотекой необходимо:

1) иметь выровненные тексты в формате XLSX, как на скрине ниже
<img src="readme_assets/xlsx_example.png" width="500">


2) положить эти тексты в папку `texts\input`. Структура проекта при этом следующая:
```
YOUR_PROJECT
|_texts
|    |_input # сюда класть выровненные XLSX
|    |_output # здесь появятся XML после обработки
|
|_main.py
|_classes.py
|_eanc2rnc_tag_converter.py
|_hy_translit.py
```

3) скачать наш форк библиотеки `razdel`, которая адаптирована под армянскую пунктуацию. Это можно сделать командой
`pip install git+https://github.com/RNC-Armenian-parallel-corpus/razdel_armenian.git`

Когда требования, перечисленные выше, выполнены, можно запускать программу из командной строки (пример команды см. в начале раздела).
