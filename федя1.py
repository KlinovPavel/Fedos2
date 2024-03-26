import numpy as np
import matplotlib.pyplot as plt

# Функция для расчета звукового давления
def calculate_sound_pressure(frequencies, distances):
    L_values = []
    for d in distances:
        for f in frequencies:
            L = 32.4 + 20*np.log10(f) + 20*np.log10(d)
            L_values.append(L)
    return L_values

# Параметры формулы
frequencies = np.linspace(20, 20000, 100)  # диапазон частот от 20 Гц до 20 кГц
distances = np.arange(1, 501, 100)  # диапазон расстояний от 1 до 500 м с шагом 10 метров

# Рассчитываем значения звукового давления
L_values = calculate_sound_pressure(frequencies, distances)

# Разбиваем значения на подграфики
fig, ax = plt.subplots()
for i in range(len(distances)):
    ax.plot(frequencies, L_values[i*len(frequencies):(i+1)*len(frequencies)])

# Настройка графика
ax.set(xlabel='Частота (Гц)', ylabel='Уровень звукового давления (дБ)',
       title='График звукового давления в зависимости от частоты и расстояния (до 500 м)')
ax.grid()

# Сохраняем изображение с прозрачным фоном
plt.savefig('sound_pressure_chart.png', transparent=True)

# Показываем график
plt.show()
