# Lab2/Task3/src/InversionsCounter.py

"""Модуль для подсчёта инверсий с помощью сортировки слиянием."""

class InversionsCounter:
    """
    Класс для подсчёта количества инверсий в массиве.
    """

    @staticmethod
    def merge_and_count(array, temp_array, left, middle, right):
        i=left
        j=middle+1
        k=left
        inv_count=0

        while i<=middle and j<=right:
            if array[i]<=array[j]:
                temp_array[k]=array[i]
                i+=1
            else:
                temp_array[k]=array[j]
                inv_count+=(middle - i +1)
                j+=1
            k+=1

        while i<=middle:
            temp_array[k]=array[i]
            i+=1
            k+=1

        while j<=right:
            temp_array[k]=array[j]
            j+=1
            k+=1

        for idx in range(left,right+1):
            array[idx]=temp_array[idx]

        return inv_count

    @staticmethod
    def merge_sort_and_count(array, temp_array, left, right):
        if not isinstance(array,list) or not isinstance(temp_array,list):
            raise TypeError("Ожидается массив (list).")

        if len(temp_array)<len(array):
            raise ValueError("Временный массив слишком мал.")

        inv_count=0
        if left<right:
            middle=(left+right)//2
            inv_count+=InversionsCounter.merge_sort_and_count(array,temp_array,left,middle)
            inv_count+=InversionsCounter.merge_sort_and_count(array,temp_array,middle+1,right)
            inv_count+=InversionsCounter.merge_and_count(array,temp_array,left,middle,right)
        return inv_count
