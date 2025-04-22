def sum_first_numbers(file_path, index):
    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            numbers = line.strip().split(',')
            #print(numbers)
            if numbers:
                total += float(numbers[index].strip())
    return total

# Beispielpfad zur Datei
file_path = "/home/user/Desktop/Uni_tmp/PP_tmp/angle_files/cat.txt"  # Passe den Pfad entsprechend an
result_ms = sum_first_numbers(file_path, 0)
result_s = result_ms / 1000
result_min = result_s / 60
result_motorA = sum_first_numbers(file_path, 1)
result_motorB = sum_first_numbers(file_path, 2)

print(f"Reading '{file_path}'...")
print(f"Time total: {result_ms}ms (ca {result_s:.2f}s bzw. {result_min:.2f}min)")
print(f"MotorA total: {result_motorA} Degrees")
print(f"MotorB total: {result_motorB} Degrees")
