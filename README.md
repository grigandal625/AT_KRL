# Конвертор языка представления знаний инструментального комплекса АТ-ТЕХНОЛОГИЯ

Данный проект предоставляет python-пакет для парсинга и конвертации базового и расширенного языка представления знаний комплекса АТ-ТЕХНОЛОГИЯ.

Для создания парсера используется стандарт [antlr](https://www.antlr.org/), предоставляющий язык описания синтаксических грамматик, на основе которых генерируются runtime-модули парсера для выбранного языка программирования (список поддерживаемых языков [здесь](https://github.com/antlr/antlr4/blob/dev/doc/targets.md)).

Текущая версия синтаксиса находится в файле [src/at_krl/grammar/at_krl.g4](./src/at_krl/grammar/at_krl.g4)

*Пакет функционирует в режиме разработки*

## 1. Установка

1. Установить python версии от 3.10
2. Установть пакет следующей командой:

```bash
pip install git+https://github.com/grigandal625/AT_KRL.git@master
```

В более ранних версиях pip установка осуществляется следующей командой:

```bash
pip install git+https://github.com/grigandal625/AT_KRL.git#egg=at-krl
```

Для систем типа `linux` может потребоваться напрямую указать версию python:

```bash
python3.10 -m pip install git+https://github.com/grigandal625/AT_KRL.git#egg=at-krl
```


Также можно использовать пакетный менеджер pipenv, poetry

Пакет установлен и готов к работе.

## 2. Простой пример использования

### 2.1. Исполняемый модуль

В папке [example](./example/) есть файл БЗ на ЯПЗ `test.kbs`, для описания примеров будет использован этот файл.

*Обратите внимание! Текущая реализация грамматики и парсера не чувствительна к переносам и отступам.*

Можно сконвертировать формат ЯПЗ в XML, воспринимаемый текущими версиями АТ-РЕШАТЕЛЯ и темпорального решателя следующим образом:

```bash
python -m at_krl atkrl-xml -i ./example/test.kbs
```

В этой команде мы вызываем сполняемый модуль пакета `at_krl`, указывая следующие параметры:

- `atkrl-xml` - позиционный параметр, указывающий на то, что входной формат будет формат ЯПЗ, а выходной формат требуется XML
- `-i` - позиционный параметр (также возможно указывать `--input`) - файл, из которого брать текст входного формата

После выполнения данной команды XML-представление БЗ выведется на экране. Чтобы сохранить его в отдельный файл, необходимо добавить параметр `-o` или `--output`.

```bash
python -m at_krl atkrl-xml -i ./example/test.kbs -o TKBNew.xml
```

Также следует учесть, что на момент разработки данного пакета, темпоральный решатель считывает темпоральные объекты (интервалы и события) из отдельного файла. Для того, чтобы выгрузить темпоральные объекты в отдельный файл, можно добавить параметр `-a` (или `--allen`)

```bash
python -m at_krl atkrl-xml -i ./example/test.kbs -o TKBNew.xml -a Allen2.xml
```

### 2.2. Использование режиме runtime

Загрузить БЗ из формата ЯПЗ можно следующим образом:

```python
from antlr4 import CommonTokenStream, InputStream
from at_krl.grammar.at_krlLexer import at_krlLexer
from at_krl.grammar.at_krlParser import at_krlParser
from at_krl.utils.listener import ATKRLListener
from at_krl.utils.error_listener import ATKRLErrorListener

input = 'example/test.kbs' # Входной файл на япз

with open(input, 'r') as krl_file:
    krl_text = krl_file.read() # считываем текст БЗ
    input_stream = InputStream(krl_text)
    lexer = at_krlLexer(input_stream) # создаем лексер
    stream = CommonTokenStream(lexer)
    parser = at_krlParser(stream) # создаем парсер

    listener = ATKRLListener()
    parser.addParseListener(listener) # добавляем лисенер

    error_listener = ATKRLErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.knowledge_base() # даем команду распарсить БЗ

    # После этого в объекте listener в свойсте KB будет загруженная бз

    kb = listener.KB

    for t in kb.types: # пеатаем все типы
        print(t.id)

    for p in kb.world.properties: # печатаем все объекты
        print(p.id, p.type_or_class_id)

    for i in kb.classes.intervals: # печатаем все интервалы
        print(i.id)

    for e in kb.classes.events: # печатаем все события
        print(e.id)

    for r in kb.world.rules: # печатаем все правила
        print(r.id)
```

## 3. Разработка

### 3.1. Локальная установка

1. Клонировать репозиторий командой `git clone https://github.com/grigandal625/AT_KRL.git`
2. Установить python версии 3.10 и пакетный менеджер poetry
3. Перейти в директорию склонированного проекта
4. Установить зависимости командой `poetry install`

### 3.2. Генерация парсера

При возникновении необходимости модифицировать грамматику, также нужно перегенерировать модули парсера. Для этого проще всего будет выполнить следующие действия:

1. Подготовка
    - 1.1. Установить docker
    - 1.2. Выполнить в свобоной директории команды для сборки docker-образа antlr (раздел [build](https://github.com/antlr/antlr4/tree/dev/docker#build))
2. Перегенерировать модули парсера следующей командой:

```bash
docker run -it --rm -v $$(pwd)/at_krl/grammar:/app antlr/antlr4 -Dlanguage=Python3 /app/at_krl.g4
```

**Действия из пункта "1. Подготовка" нужно выполнить только один раз, дальше можно всегда пользоваться этим образом**

Если необходимо сгенерировать модули парсера на языке не python3, а другом из поддерживающихся, измените параметр `-Dlanguage` в команде
