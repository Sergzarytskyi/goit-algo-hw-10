import numpy as np
import scipy.integrate as spi
from func_v2 import func as f,a, b


def monte_carlo_integration(f, a, b, num_points):
    
    x = np.random.uniform(a, b, num_points)
    max_x = max(f(x))
    y = np.random.uniform(0, max_x, num_points)
    under_curve = np.sum(y < f(x))
    print(f"Кількість точок під кривою: {under_curve} з {num_points}\n")
    area = (b - a) * max_x * (under_curve / num_points)
    return area


 
if __name__ == "__main__":
    result, error = spi.quad(f, a, b)
    mc_result = monte_carlo_integration(f, a, b, 1_000_000)
    print(f"Результат інтегрування функції за допомогою бібліотеки  SciPy: {result}  \nОцінка абсолютної помилки складає: {error}\n")
    print(f"Результат інтегрування методом Монте-Карло: {mc_result}\n")
    diff = abs(mc_result - result)
    print(f"Різниця: {diff:.4f} ({diff / result * 100:.2f}%)")