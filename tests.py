
# config = open("config.txt", "w")
# config.write("לוקר ירוק: 1478")
# config.write("\n")
# config.write("לוקר ירוק: 2580")
# config.write("\n")
# config.write("לוקר ירוק: 2356")

config = open("config.txt", "r")
read_config = config.read()
print(type(read_config))

config_list = read_config.splitlines()
print(config_list)

locker_code_list = []
for item in config_list:
    digit_item = ''.join(filter(str.isdigit, item))
    print(digit_item)
    locker_code_list.append(digit_item)
print(locker_code_list)

