temp =40
print("Ustaw zakres temperatury min/max")
min = input()
max = input()
temp_min = int(min)
temp_max = int(max)

too_low = temp < temp_min
too_high = temp > temp_max
while too_low or too_high:
    print(f"Tempeatura jest poza zakresem: {temp}")
    if too_high:
        temp = temp - 5
        print(f"obniżono temperaturę{temp}")
    if too_low:
        temp = temp + 5
        print(f"podniesiono temperaturę{temp}")

    print("ponowny pomiar")
    too_low = temp < temp_min
    too_high = temp > temp_max