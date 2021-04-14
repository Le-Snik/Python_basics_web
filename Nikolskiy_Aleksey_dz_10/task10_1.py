class Matrix:
    def __init__(self, lst):
        self.y_len = len(lst)
        self.x_len = len(lst[0])
        for i in lst:
            if len(i) != self.x_len:
                raise IndexError("Размерность матрицы не должна меняться")
        con_lst = [list(map(int, x_line)) for x_line in lst]
        self.elements = con_lst

    def __str__(self):
        st_out = ''
        for i in self.elements:
            line = (" ".join(map(str, i)))
            st_out = f"{st_out}{line}\n"
        return st_out

    def __add__(self, other):
        if (self.x_len != other.x_len) or (self.y_len != other.y_len):
            raise IndexError("Складывать можно только матрицы одинаковых размерностей")
        total_lst = [list(map(lambda x, y: x + y, self.elements[i], other.elements[i])) for i in
                     range(0, len(self.elements))]
        new_mat = Matrix(total_lst)
        return new_mat


mat = Matrix([[1, -5, 3], [3, 4, 5], [6, 7, 8]])
mat2 = Matrix([['2', '3', '4'], ['5', ' 6', '+7'], [8, 9, 10]])

mat3 = mat + mat2
print(mat3)
