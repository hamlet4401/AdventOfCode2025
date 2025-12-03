def run():
    file_path = 'input.txt'
    total_joltage = 0
    with open(file_path, 'r') as file:
        for line in file:
            bank = line.rstrip()
            total_joltage += find_max_joltage_from_bank(bank, 12)

    print(total_joltage)

def find_max_joltage_from_bank(bank, battery_target):
    battery_target_index = battery_target - 1

    max_v = 0
    index = 0

    for i in range(len(bank) - battery_target_index):
        int_v = int(bank[i])
        if int_v > max_v:
            max_v = int_v
            index = i

    other_value = (
        find_max_joltage_from_bank(bank[index + 1:], battery_target_index)
        if battery_target_index > 0
        else 0
    )

    return (max_v * 10**battery_target_index) + other_value

if __name__ == "__main__":
    run()