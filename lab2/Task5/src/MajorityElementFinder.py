# Lab2/Task5/src/MajorityElementFinder.py

"""Модуль для поиска элемента, встречающегося более чем в половине случаев."""

class MajorityElementFinder:
    """
    Класс для нахождения элемента большинства в массиве.
    """

    @staticmethod
    def majority_element(array):
        if not isinstance(array,list):
            raise TypeError("Ожидается массив (list).")

        candidate=None
        count=0

        for num in array:
            if count==0:
                candidate=num
            count+= (1 if num==candidate else -1)

        if candidate is not None and array.count(candidate) > len(array)//2:
            return candidate
        return None
