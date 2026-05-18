# Программа-конвертер температур
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32
temp_c = float(input('Введите градусы Цельсия: '))
print(f'{temp_c}°C = {celsius_to_fahrenheit(temp_c)}°F')
