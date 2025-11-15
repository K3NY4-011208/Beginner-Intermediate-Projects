temps_c = [18, 20, 25, 22, 19, 30]

temps_f = [(c * 9/5) + 32 for c in temps_c]

average_c = sum(temps_c) / len(temps_c)
average_f = sum(temps_f) / len(temps_f)

print("Celsius:", temps_c)
print("Fahrenheit:", temps_f)
print(f"Average C: {average_c:.2f}")
print(f"Average F: {average_f:.2f}")
