<details>
    <summary>
        <b> Вопрос №1 </b>
    </summary>
    На языке Python написать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.
</details>

### Реализация

В файле [isEven.py](utils/is_even.py) реализована функция `is_even`, которая возвращает `True`, если число четное, и `False` в противном случае.
В качестве реализации представлено дерево отрезков, которое позволяет отвечать на запросы о четности числа за `O(log n)`.
В вершинах дерева хранится информации о количестве четных чисел на соответствующем отрезке. В листьях, соответственно, хранится информация о четности соответствующего числа.

### Плюсы и минусы

Очевидно, исходная реализация  `is_even` работает за `O(1)`, что является лучшим результатом, чем `O(log n)`. К тому же, в исходной реализации не используется дополнительная память, в то время как дерево отрезков требует `O(n)` памяти.
И читаемость исходной реализации лучше, чем у дерева отрезков.
Однако, в случае необходимости нахождения количества четных чисел на отрезке, дерево отрезков будет работать за `O(log n)`, в то время как исходная реализация будет работать за `O(n)`.
На этом плюсы приведённого решения заканчиваются 🙃 P.S. И на мой взгляд довольно креативненько

<details>
    <summary>
        Вопрос №2
    </summary>
    На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.
</details>

## Реализация

### Реализация на основе массива

В файле [array_impl.py](circular_buffer/array_impl.py) реализован класс `CircularBuffer`, который представляет собой циклический буфер FIFO на основе массива.

### Реализация на основе двусвязного списка
В файле [linked_list_impl.py](circular_buffer/linked_list_impl.py) реализован класс `CircularBuffer`, который представляет собой циклический буфер FIFO на основе двусвязного списка.


### Сравнение реализаций

В пакете utils создадим аннотацию `average_benchmark_decorator`, которая будет считать среднее время выполнения функции.
Посмотрим на результаты бенчмарков для каждой реализации на разных размерах буфера:

| Размер буфера | Реализация на основе массива | Реализация на основе двусвязного списка |
|:-------------:|:----------------------------:|:---------------------------------------:|
|     10000     |            0.012             |                  0.016                  |
|    1000000    |             1.14             |                  2.11                   |
|   10000000    |             11.4             |                  21.9                   |


Как видно из таблицы, реализация на основе массива работает быстрее, чем реализация на основе двусвязного списка.
Первая реализация использует массив для хранения элементов кольцевого буфера. У нее есть преимущество в эффективности доступа к элементам, так как операции enqueue и dequeue в этой реализации выполняются за время `O(1)`. Однако, когда размер буфера становится большим, может возникнуть необходимость копирования элементов, что может быть затратным по времени в случае изменения размера буфера.

Вторая реализация использует связанный список элементов. Она избегает копирования элементов при изменении размера буфера, но каждый элемент создается как отдельный объект, что может привести к большему расходу памяти и накладным расходам на создание и управление объектами.
<details>
    <summary>
        Вопрос №3
    </summary>
    На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). 
    Объяснить, почему вы считаете, что функция соответствует заданным критериям.
</details>

## Реализация

В файле [num_sort.py](utils/num_sort.py) реализована функция `num_sort`, которая использует встроенную функцию `sorted` для сортировки массива чисел.
Посмотрим на [имплементацию алгоритма](https://github.com/python/cpython/blob/5f665e99e0b8a52415f83c2416eaf28abaacc3ae/Objects/listobject.c#L2309) и поймём, почему для массива чисел лучше мы не напишем (в рамках текущей задачи):

Во-первых, ввиду того, что код написан на C, это даёт нам преимущество в скорости выполнения. (Спасибо си)

Во-вторых, если воспользоваться могуществом интернета, то можно понять, что стандартная сортировка под капотом использует
TimSort, который использует MergeSort и InsertionSort в зависимости от исходного массива. Поэтому, любые обёртки этих
сортировок будут явно не лучше TimSort'а. 
Конечно не забываем про QuickSort и вообще про все остальные сортировки, но в рамках текущей задачи, я считаю, что
встроенная сортировка ввиду того, что написана на си и не использует якобы существующей лучшей сортировки, будет
оптимальным решением.
