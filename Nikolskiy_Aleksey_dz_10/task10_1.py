class Matrix:
    def __init__(self, lst):
        self.y_len = len(lst)
        self.x_len = len(lst[0])
        for i in lst:
            if len(i) != self.x_len:
                raise IndexError("Размерность матрицы не должна меняться")

        self.elements = lst

    def __str__(self):
        stout = ''
        for i in self.elements:
            line = (" ".join(map(str, i)))
            stout = f"{stout}{line}\n"
        return stout

    def __add__(self, other):
        total_lst = []
        if (self.x_len != other.x_len) or (self.y_len != other.y_len):
            raise IndexError("Складывать можно только матрицы одинаковых размерностей")

        for i in range(0, len(self.elements)):
            buff_lst = [self.elements[i][j] + other.elements[i][j] for j in range(0, len(self.elements[i]))]
            total_lst.append(buff_lst)

        new_mat = Matrix(total_lst)
        return new_mat


mat = Matrix([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
mat2 = Matrix([[1, 2, 3], [3, 4, 5], [6, 7, 8]])

mat3 = mat + mat2
print(mat3)
