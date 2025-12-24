def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))





energy = 50
MAX_ENERGY = 100
MIN_ENERGY = 0

for tick in range(1,21):
    print(f"\nTick {tick}")

    action = input("Charge (c) or Use (u)? ").lower()

    if action == "c":
        energy += 10
        print("Charging...")
    elif action == ("u"):
        energy -= 15
        print("Using energy...")
    else:
        print("No action taken.")

    energy = clamp(energy, MIN_ENERGY, MAX_ENERGY)

    print(f"Energy level: {energy}")