# Lab1/Task4/src/LinearSearcher.py

"""Модуль для линейного поиска элемента в массиве."""

class LinearSearcher:
    """
    Класс для линейного поиска.
    """

    @staticmethod
    def linear_search(arr,v):
        result=[]
        for i,num in enumerate(arr):
            if num==v:
                result.append(str(i+1))
        return result if result else ['-1']
