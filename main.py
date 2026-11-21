# 1. Импортировать numpy и matplotlib.pyplot.
# 2. Написать функцию plot_basis_and_square(A, title):
#    - Задать точки квадрата по периметру: xs = [0,1,1,0,0], ys = [0,0,1,1,0]
#    - Создать матрицу точек: square = np.array([xs, ys]) (форма 2x5)
#    - Умножить: transformed = A @ square
#    - plt.fill(xs, ys, alpha=0.3, color='blue', label='Before')
#    - plt.fill(transformed[0], transformed[1], alpha=0.3, color='red', label='After')
#    - (Опционально) Нарисовать базисные векторы i и j через quiver до и после.
#    - Зафиксировать оси: plt.xlim(-3, 3), plt.ylim(-3, 3)
#    - plt.title(title), plt.legend(), plt.show()
# 3. В __main__ создать 3 матрицы: scaling, rotation, shear.
# 4. Вызвать plot_basis_and_square для каждой.
import numpy as np
import matplotlib.pyplot as plt
def plot_basis_and_square(A, title):
    ''' Visualizes matrix transformation
    Args: A (np.array), title (string)
    Returns: None
    '''
    xs = [0,1,1,0,0]
    ys = [0,0,1,1,0]
    square = np.array([xs, ys])
    transformed = A @ square
    fig, ax = plt.subplots()
    ax.fill(xs, ys, alpha=0.3, color='blue', label='Before')
    ax.fill(transformed[0], transformed[1], alpha=0.3, color='red', label='After')
    ax.quiver(0, 0, xs[1], ys[1], angles='xy', scale_units='xy', scale=1, color='black', label='column x before')
    ax.quiver(0, 0, xs[3], ys[3], angles='xy', scale_units='xy', scale=1, color='purple', label='column y before')
    ax.quiver(0, 0, transformed[0][1], transformed[1][1], angles='xy', scale_units='xy', scale=1, color='green', label='column x after')
    ax.quiver(0, 0, transformed[0][3], transformed[1][3], angles='xy', scale_units='xy', scale=1, color='orange', label='column y after')
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_title(title)
    ax.grid(True)
    ax.legend()
    plt.show()
if __name__ == "__main__":
    A = np.array([[1, 1], [0, 1]])
    plot_basis_and_square(A, 'Shear')
    B = np.array([[2,0],[0,1]])
    plot_basis_and_square(B, 'Scaling')
    C = np.array([[0,-1],[1,0]])
    plot_basis_and_square(C, 'Rotation')