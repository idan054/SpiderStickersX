from time import sleep


def write_config():
    config = open("config.txt", "w", encoding='utf-8')
    config.write("לוקר ירוק: 0000")
    config.write("\n")
    config.write("לוקר כחול: 0000")
    config.write("\n")
    config.write("לוקר כתום: 0000")

def get_config():
    try:
        config = open("config.txt", "r", encoding='utf-8')
        print("CONFIG.TXT")
        print(config.read())
    except:
        print("config.txt not found! Start write_config()...")
        write_config()

    config = open("config.txt", "r", encoding='utf-8')
    read_config = config.read()

    config_list = read_config.splitlines()
    print("config_list")
    print(config_list)

    if len(config_list) == 0:
        print("config_list (Based config.txt) is Empty! Start write_config()")
        write_config()
        config = open("config.txt", "r", encoding='utf-8')
        read_config = config.read()

        config_list = read_config.splitlines()
        print("config_list update")
        print(*config_list)

    _locker_code_list = []
    for item in config_list:
        digit_item = ''.join(filter(str.isdigit, item))
        # print(digit_item)
        _locker_code_list.append(digit_item)
    print(_locker_code_list)
    return _locker_code_list
get_config()
print("Sleep...")
sleep(2)
get_config()
