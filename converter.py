print("Mile to KM converter")

km_or_m = input("KM or Mile or Meter?")

value = int(input("Value: "))

if km_or_m == "km":
    print(f"Mile: {value / 1.6}")
    print(f"Meter: {value * 1000}")

elif km_or_m == "mile":
    print(f"Mile: {value * 1.6}")

elif km_or_m == "meter":
    print(f"KM: {value / 1000}")

print("Bye Bye")

