# Lab2/Task6/src/SortPerformanceTester.py

"""Модуль для сравнения производительности сортировок: merge sort, insertion sort, selection sort."""

import time
from bisect import bisect_left

class Sorter:
    @staticmethod
    def merge_sort(arr):
        if not isinstance(arr,list):
            raise TypeError("Ожидается массив (list).")
        if len(arr)<=1:
            return arr
        mid=len(arr)//2
        left=Sorter.merge_sort(arr[:mid])
        right=Sorter.merge_sort(arr[mid:])
        return Sorter.merge(left,right)

    @staticmethod
    def merge(left,right):
        if left and right and left[-1]<=right[0]:
            return left+right
        merged=[]
        i=j=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                merged.append(left[i])
                i+=1
            else:
                merged.append(right[j])
                j+=1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    @staticmethod
    def insertion_sort(arr):
        if not isinstance(arr,list):
            raise TypeError("Ожидается массив (list).")
        arr=arr[:]
        for i in range(1,len(arr)):
            key=arr[i]
            j=i-1
            while j>=0 and arr[j]>key:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
        return arr

    @staticmethod
    def selection_sort(arr):
        if not isinstance(arr,list):
            raise TypeError("Ожидается массив (list).")
        arr=arr[:]
        n=len(arr)
        for i in range(n):
            min_idx=i
            for j in range(i+1,n):
                if arr[j]<arr[min_idx]:
                    min_idx=j
            arr[i],arr[min_idx]=arr[min_idx],arr[i]
        return arr

class SortPerformanceTester:
    """
    Класс для определения порога, начиная с которого merge sort быстрее вставок и выбора.
    """

    @staticmethod
    def measure_time(sort_func, arr):
        start=time.time()
        sort_func(arr)
        end=time.time()
        return end-start

    @staticmethod
    def find_threshold(max_size=1000):
        import random
        threshold_found=False
        for size in range(1,max_size+1):
            arr=[random.randint(-10**9,10**9) for _ in range(size)]
            t_merge=SortPerformanceTester.measure_time(Sorter.merge_sort,arr)
            t_insertion=SortPerformanceTester.measure_time(Sorter.insertion_sort,arr)
            t_selection=SortPerformanceTester.measure_time(Sorter.selection_sort,arr)
            print(f"Размер: {size} | Merge: {t_merge:.6f}s | Insertion: {t_insertion:.6f}s | Selection: {t_selection:.6f}s")

            if not threshold_found and t_merge<t_insertion and t_merge<t_selection:
                print(f"Merge Sort быстрее при размере: {size}")
                threshold_found=True
                break
        if not threshold_found:
            print(f"Порог не найден до {max_size}")
