---
date: 2023-10-12
author:
А. Г. Маслова
title: Проект «Выпуклая оболочка»
---

### Постановка задачи

Необходимо написать программу, находящую выпуклую оболочку последовательно
поступающих точек плоскости и вычисляющую её периметр и площадь. Решение
должно быть индуктивным, что означает определение выпуклой оболочки и
вычисление её характеристик сразу после поступления очередной точки с
использованием методов теории индуктивных функций.

Задание на модификацию № 43:
Вычисляется количество вершин выпуклой оболочки, лежащих вне замкнутого заданного треугольника. Треугольник задаётся тремя его вершинами — произвольными точками плоскости.

### Краткий комментарий к решению

Для нахождения количества вершин выпуклой оболочки, находящихся вне заданного треугольника, в класс `R2Point` был добавлен метод `is_outside_triangle`, который определяет, находится ли точка вне треугольника. Это осуществляется путём сложения площащей трех треугольников, образующихся данной точкой и двумя вершинами заданного треугольника и сравнения этой суммы с площадью заданного треугольника. В этот же класс добавляется счетчик `counter`, который определяет количество нужных вершин для треугольника (те есть для только что инициализированного объекта класса `Polygon`). В дальнейшем для подсчета искомых вершин используется счетчик `vert_counter`. Он добавляется во все классы файла `convex` и пересчитывает количество вершин, которые расположены вне наперёд заданного треугольника. В файлы `tk_drawer` и `run_tk_convex` вносятся изменения направленные на то, чтобы заданный треугольник рисовался красным цветом на отдельно от остальных точек.

- Ключевое понятие проекта: *освещённость ребра из точки* 
- Вспомогательные классы:
    - `R2Point` — точка на плоскости
    - `Deq` — контейнер дек (double ended queue)
- Основные классы:
    - `Figure` — «абстрактная» фигура
    - `Void` — нульугольник
    - `Point` — одноугольник
    - `Segment` — двуугольник
    - `Polygon` — многоугольник
- Файлы проекта:
    - `README.md` — данный файл
    - `README.html` — полученный из файла `README.md` `html`-файл
    - `r2point.py` — реализация класса `R2Point`
    - `deq.py` —  реализация класса `Deq`
    - `convex.py` — реализация основных классов
    - `run_convex.py` — файл запуска
    - `tk_drawer.py` — интерфейс к графической библиотеке
    - `run_tk_convex.py` — файл запуска с использованием графики
    - `tests/test_r2point.py` — тесты к классу `R2Point`
    - `tests/test_convex.py` — тесты к основным классам

Файлы `run_tk_convex.py` и `run_tk_convex.py` являются исполняемыми (они имеют
бит `x`), в первой строке каждого из них используется [шебанг](https://ru.wikipedia.org/wiki/%D0%A8%D0%B5%D0%B1%D0%B0%D0%BD%D0%B3_(Unix)) и команда `env` с
опцией (ключом) `-S`. Это обеспечивает передачу интерпретатору языка Python
опции (ключа) `-B`, отменяющего генерацию `pyc`-файлов в директории
`__pycache__`.

### Описание идеи решения

Изначально для решения задачи необходимо понять, какие точки лежат вне
открытой 1-окрестности заданной прямой. Значит, что расстояние от некоторой
точки (вершины) до прямой должно быть больше 1. Для этого используем формулу
расстояния с использованием векторного произведения 

### Соблюдение соглашений о стиле программного кода

Для языка Python существуют [соглашения о стиле
кода](https://www.python.org/dev/peps/pep-0008/). Они являются лишь
рекомендациями (интерпретатор игнорирует их нарушение), но основную их
часть при написании программ целесообразно соблюдать. Существует простой
способ проверить соблюдение считающегося правильным
стиля записи кода с помощью утилиты (программы) `pycodestyle`. Утилита
`yapf` позволяет даже изменить код в соответствии с этими соглашениями.

Команда 

    pycodestyle r2point.py

позволяет, например, проверить соблюдение стиля для файла `r2point.py`.
С помощью очень мощной и часто используемой утилиты `find` проверить
корректность стиля всех файлов проекта можно так:

    find . -name '*.py' -exec pycodestyle {} \;

Эта команда находит все файлы с расширением `py` и запускает программу
`pycodestyle` последовательно для каждого из них.

### Запуск тестов

Уже известная нам команда (см. материал, посвящённый тестированию программ)

    python -B -m pytest -p no:cacheprovider tests

запускает pytest, выполняя все начинающиеся с `test` методы классов,
имена которых начинаются с `Test`, содержащиеся во всех файлах `test_*.py`
директории `tests`.

### Запуск программы

`./run_convex.py`

### Запуск программы с графическим интерфейсом

`./run_tk_convex.py`
