"""
Дан массив чисел, состоящий из некоторого количества подряд идущих единиц, за которыми следует какое-то количество подряд идущих нулей: 111111111111111111111111100000000.
Найти индекс первого нуля (то есть найти такое место, где заканчиваются единицы, и начинаются нули)
def task(array):
    pass

print(task("111111111110000000000000000"))
# >> OUT: 11
…
"""


def task(array: str) -> int:
    for count, elem in enumerate(array):
        if elem == "0":
            return count

array1 = "111111111110000000000000000"
array2 = "10"
array3 = "111000"

if __name__ == '__main__':
    assert task(array1) == 11, "First test failed!"
    assert task(array2) == 1, "Second test failed!"
    assert task(array3) == 3, "Third test failed!"
    print("Test passed!")
