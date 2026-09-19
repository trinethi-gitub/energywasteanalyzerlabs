def calculate_energy(computers, fans, lights,
                     computer_power, fan_power, light_power,
                     hours, cost_per_unit):

    computer_energy = (computers * computer_power * hours) / 1000
    fan_energy = (fans * fan_power * hours) / 1000
    light_energy = (lights * light_power * hours) / 1000

    total_energy = computer_energy + fan_energy + light_energy

    total_cost = total_energy * cost_per_unit

    return {
        "computer_energy": computer_energy,
        "fan_energy": fan_energy,
        "light_energy": light_energy,
        "total_energy": total_energy,
        "total_cost": total_cost
    }