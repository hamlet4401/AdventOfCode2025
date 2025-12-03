def run():
    file_path = 'input.txt'
    total_joltage = 0
    with open(file_path, 'r') as file:
        for line in file:
            bank = line.rstrip()
            total_joltage += find_max_joltage_from_bank(bank, 11)

    print(total_joltage)

def find_max_joltage_from_bank(bank, battery_amount):
    max_v = 0
    index = 0

    for i in range(len(bank) - battery_amount):
        int_v = int(bank[i])
        if int_v > max_v:
            max_v = int_v
            index = i

    other_value = (
        find_max_joltage_from_bank(bank[index + 1:], battery_amount - 1)
        if battery_amount > 0
        else 0
    )

    return (max_v * 10**battery_amount) + other_value

if __name__ == "__main__":
    run()