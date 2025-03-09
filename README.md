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

*Обратите внимание! Текущая реализация грамматики и парсера не чувствительна к отступам.*

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

### 2.2. Использование в режиме runtime

#### 2.2.1. Построение конструкций ЯПЗ из кода

Типы:

```python
# Символьный тип
from at_krl.core.kb_type import KBSymbolicType

my_symbolic_type = KBSymbolicType(
    id="СИМВ_ТИП_1",
    desc="Символьный тестовый тип",
    values=["Значение 1", "Значение 2"]
)
print(my_symbolic_type.krl) # напечаниется представление типа в формате ЯПЗ

# Числовой тип
from at_krl.core.kb_type import KBNumericType

my_numeric_type = KBNumericType(
    id="ЧИСЛО_ТИП_1",
    desc="Числовой тестовый тип",
    from_=0,
    to_=10
)
print(my_numeric_type.krl) # напечаниется представление типа в формате ЯПЗ

# Нечеткий тип
from at_krl.core.fuzzy.membership_function import MFPoint
from at_krl.core.fuzzy.membership_function import MembershipFunction
from at_krl.core.kb_type import KBFuzzyType

mf1 = MembershipFunction(
    name="Высокая",
    min=0,
    max=100,
    points=[
        MFPoint(x=0, y=0),
        MFPoint(x=60, y=0.7),
        MFPoint(x=100, y=1)
    ]
)
mf2 = MembershipFunction(
    name="Низкая",
    min=0,
    max=100,
    points=[
        MFPoint(x=0, y=1),
        MFPoint(x=30, y=0.6),
        MFPoint(x=100, y=0)
    ]
)

my_fuzzy_type = KBFuzzyType(
    id="СКОРОСТЬ",
    desc="Нечеткий тестовый тип для описания лингвистической переменной Скорость",
    membership_functions=[mf1, mf2]
)
print(my_fuzzy_type.krl) # напечаниется представление типа в формате ЯПЗ
```

Объекты (базовые, события, интервалы)

```python
# Базовый объект
from at_krl.core.kb_class import TypeOrClassReference
from at_krl.core.kb_class import PropertyDefinition
from at_krl.core.kb_class import KBClass

my_base_object = KBClass(
    id="МОЙ_ОБЪЕКТ",
    desc="Базовый объект",
    properties=[
        PropertyDefinition(id="Скорость", type=TypeOrClassReference(id="СКОРОСТЬ")),
        PropertyDefinition(id="Атрибут2", type=TypeOrClassReference(id="СИМВ_ТИП_1")),
        PropertyDefinition(id="Атрибут3", type=TypeOrClassReference(id="ЧИСЛО_ТИП_1"))
    ]
)

# дополнительно можно явно указать, на какие типы ссылаются атрибуты объекта

my_base_object.properties[0].type.target = my_fuzzy_type
my_base_object.properties[1].type.target = my_symbolic_type
my_base_object.properties[2].type.target = my_numeric_type

print(my_base_object.krl) # напечаниется представление объекта в формате ЯПЗ

# События

from at_krl.core.simple.simple_reference import SimpleReference
from at_krl.core.simple.simple_value import SimpleValue
from at_krl.core.simple.simple_operation import SimpleOperation
from at_krl.core.temporal.allen_event import KBEvent

my_event = KBEvent(
    id="МОЕ_СОБЫТИЕ",
    desc="Темпоральный объект - событие",
    occurance_condition=SimpleOperation(
        sign=">",
        left=SimpleReference(
            id="МОЙ_ОБЪЕКТ",
            ref=SimpleReference(id="Атрибут3")
        ),
        right=SimpleValue(content=5)
    )
)

print(my_event.krl) # напечаниется представление события в формате ЯПЗ

from at_krl.core.temporal.allen_interval import KBInterval

my_interval = KBInterval(
    id="МОЙ_ИНТЕРВАЛ",
    desc="Темпоральный объект - интервал",
    open=SimpleOperation(
        sign="<=",
        left=SimpleReference(
            id="МОЙ_ОБЪЕКТ",
            ref=SimpleReference(id="Атрибут3")
        ),
        right=SimpleValue(content=10)
    ),
    close=SimpleOperation(
        sign=">",
        left=SimpleReference(
            id="МОЙ_ОБЪЕКТ",
            ref=SimpleReference(id="Атрибут3")
        ),
        right=SimpleValue(content=15)
    )
)

print(my_interval.krl) # напечаниется представление интервала в формате ЯПЗ
```

Правила

```python
# Простое правило с темпоральным отношением в условии
from at_krl.core.non_factor import NonFactor
from at_krl.core.kb_value import KBValue
from at_krl.core.kb_reference import KBReference
from at_krl.core.kb_operation import KBOperation
from at_krl.core.kb_instruction import AssignInstruction
from at_krl.core.temporal.allen_reference import AllenReference
from at_krl.core.temporal.allen_operation import AllenOperation
from at_krl.core.kb_rule import KBRule

event_reference = AllenReference(id="МОЕ_СОБЫТИЕ")
interval_reference = AllenReference(id="МОЙ_ИНТЕРВАЛ")

event_reference.target = my_event
interval_reference.target = my_interval

# Операция логики аллена, которая утверждает, что событие произошло до интервала
allen_operation = AllenOperation(
    sign="b",
    left=event_reference,
    right=interval_reference
)

# для выражения условия правила задаим простую
# логическую операцию с НЕ-фактором, включающую алленовскую

rule_condition = KBOperation(
    sign="&",
    left=allen_operation,
    right=KBOperation(
        sign=">",
        left=KBReference(
            id="МОЙ_ОБЪЕКТ",
            ref=KBReference(id="Атрибут3"),
            non_factor=NonFactor(belief=70, probability=100, accuracy=0)
        ),
        right=KBValue(content=5, non_factor=NonFactor(belief=80, probability=90, accuracy=0)),
        non_factor=NonFactor(belief=40, probability=50, accuracy=0)
    )
)

my_rule = KBRule(
    id="МОЕ_ПРАВИЛО",
    desc="Тестовое правило",
    condition=rule_condition,
    instructions=[
        AssignInstruction(
            ref=KBReference.parse("МОЙ_ОБЪЕКТ.АТРИБУТ2"),
            value=KBValue(content="Значение 2"),
            non_factor=NonFactor(belief=90, probability=95, accuracy=0)
        ),
    ]
)

print(my_rule.krl) # напечаниется представление правила в формате ЯПЗ
```

#### 2.2.2. Считывание текста на ЯПЗ и конвертация в объекты

Загрузить БЗ из формата ЯПЗ можно следующим образом:

```python
from antlr4 import CommonTokenStream, InputStream
from at_krl.grammar.at_krl_lexer import at_krl_lexer
from at_krl.grammar.at_krl_parser import at_krl_parser
from at_krl.utils.listener import ATKRLListener
from at_krl.utils.error_listener import ATKRLErrorListener

input = 'example/test.kbs' # Входной файл на япз

with open(input, 'r') as krl_file:
    krl_text = krl_file.read() # считываем текст БЗ

    # Создаем поток ввода для текста ЯПЗ
    input_stream = InputStream(krl_text)

    # Создаем лексер
    lexer = at_krl_lexer(input_stream)

    # Создаем кастомный поток токенов, который пропускает скрытые токены
    stream = CommonTokenStream(lexer)
    stream.fill()  # Заполняем поток токенов

    # Создаем парсер
    parser = at_krl_parser(stream)

    listener = ATKRLListener()
    parser.addParseListener(listener)

    # Настраиваем обработчик ошибок
    error_listener = ATKRLErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    # Парсим входной текст
    parser.knowledge_base() # даем команду распарсить БЗ

    # После этого в объекте listener в свойсте KB будет загруженная бз

    kb = listener.KB

    for t in kb.types: # пеатаем все типы
        print(t.id)

    for p in kb.world.properties: # печатаем все объекты
        print(p.id, p.type.target.id)

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
docker run -it --rm -v $$(pwd)/at_krl/grammar:/app antlr/antlr4 -Dlanguage=Python3 /app/at_krl_lexer.g4 /app/at_krl_parser.g4
```

**Действия из пункта "1. Подготовка" нужно выполнить только один раз, дальше можно всегда пользоваться этим образом**

Если необходимо сгенерировать модули парсера на языке не python3, а другом из поддерживающихся, измените параметр `-Dlanguage` в команде
