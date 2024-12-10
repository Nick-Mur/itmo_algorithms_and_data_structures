# Lab2/Task2/src/MergeSorterWithIndices.py

"""Модуль для сортировки слиянием с выводом индексов."""

class MergeSorterWithIndices:
    """
    Класс для сортировки слиянием с выводом индексов подмассивов.
    """

    @staticmethod
    def merge_with_indices(array, left, middle, right):
        left_subarray = array[left:middle+1] + [float('inf')]
        right_subarray = array[middle+1:right+1] + [float('inf')]

        print(f"Слияние: индексы {left+1}-{right+1}, значения: {array[left]}-{array[right]}")

        i=j=0
        for k in range(left, right+1):
            if left_subarray[i]<=right_subarray[j]:
                array[k]=left_subarray[i]
                i+=1
            else:
                array[k]=right_subarray[j]
                j+=1

    @staticmethod
    def merge_sort_with_indices(array, left, right):
        if left<0 or right>=len(array):
            raise ValueError("Некорректные индексы для сортировки.")
        if left>=right:
            return

        middle=(left+right)//2
        MergeSorterWithIndices.merge_sort_with_indices(array,left,middle)
        MergeSorterWithIndices.merge_sort_with_indices(array,middle+1,right)
        MergeSorterWithIndices.merge_with_indices(array,left,middle,right)
