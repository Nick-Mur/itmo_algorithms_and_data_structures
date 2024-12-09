"""Модуль для вычисления высоты дерева по списку родителей."""

class TreeHeightCalculator:
    """
    Класс для вычисления высоты дерева.
    Считается, что -1 в списке родителей обозначает корень дерева.
    """

    def tree_height(self, n, parents):
        """
        Вычисляет высоту дерева.

        :param n: Количество узлов.
        :param parents: Список родителей для каждого узла (индекс = узел, значение = родитель).
        :return: Высота дерева.
        """
        tree = [[] for _ in range(n)]
        root = -1

        for i in range(n):
            if parents[i] == -1:
                root = i
            else:
                tree[parents[i]].append(i)

        def height(node):
            if not tree[node]:
                return 1
            max_h = 0
            for child in tree[node]:
                max_h = max(max_h, height(child))
            return max_h + 1

        return height(root)
