def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0

try:
    fahrenheit_input = int(input("Введіть температуру у Фаренгейтах: "))
    celsius = fahrenheit_to_celsius(fahrenheit_input)
    celsius_rounded = round(celsius, 1)
    print(f"{fahrenheit_input} °F дорівнює {celsius_rounded} °C")
except ValueError:
    print("Будь ласка, введіть ціле число.")

