import random

def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


battery = 50
BATTERY_MAX = 100

for tick in range(1, 21):
    print(f"\nTick {tick}")

    generator_output = random.randint(5, 15)
    energy_use = random.randint(6, 12)

    battery += generator_output
    print(f"Generator produced {generator_output} energy")

    battery -= energy_use
    print(f"System used {energy_use} energy")

    battery = clamp(battery, 0, BATTERY_MAX)

    print(f"Battery level: {battery}")
