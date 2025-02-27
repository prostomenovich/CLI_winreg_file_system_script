import argparse
import modules.fileSystem as fs
import modules.winregistry as wrg
from winreg import REG_DWORD, REG_SZ
from termcolor import colored
import os


def main() -> None:
    #Параметр для отображения цвета текста в терминале
    os.system('color')

    parser = argparse.ArgumentParser(description="A utility for interacting with the file system and registry.")
    parser.add_argument("operations_set", choices=["fs", "reg"], help="Use the fs flag if you want to execute filesystem commands or the reg flag to manipulate registers")

    #Создание группы ключей для взаимодействия с файловой системой
    fs_group = parser.add_argument_group(title="File System Commands", description="This block describes commands that allow you to interact with the file system.")
    
    #Добавление опциональных флагов, на которые не должно распространяться взаимоисключение
    fs_group.add_argument("-rw", "--rewrite", action="store_true", help=argparse.SUPPRESS)

    #Создание подгруппы взаимоисключающих ключей для взаимодействия с операционной системой (за один раз выполняется одна операция)
    fs_mutual_exclusive_group = fs_group.add_mutually_exclusive_group()
    fs_mutual_exclusive_group.add_argument("-cf", "--create_file",
                                           metavar="path", 
                                           help="Creates a new file at the specified path. [Use the additional flag -rw/--rewrite to overwrite to allow overwriting if a file with the specified name is already in the directory]")
    fs_mutual_exclusive_group.add_argument("-rf", "--remove_file",
                                           metavar="path", 
                                           help="Deletes a file at the specified path.")
    fs_mutual_exclusive_group.add_argument("-wtf", "--write_to_file",
                                           nargs=2,
                                           action="extend", 
                                           metavar=("path", "data"), 
                                           help="Writes data to a file at the specified path.")
    fs_mutual_exclusive_group.add_argument("-rff", "--read_from_file",
                                           metavar="path", 
                                           help="Reads data from a file at the specified path and outputs it to the console.")
    fs_mutual_exclusive_group.add_argument("-cpf", "--copy_file", 
                                           nargs=2,
                                           action="extend",
                                           metavar=("src_path", "dst_path"), 
                                           help="Copies a file from src to dst. You can change the name of the copied file in dst_path.")
    fs_mutual_exclusive_group.add_argument("-rnf", "--rename_file",
                                            nargs=2,
                                            action="extend",
                                            metavar=("path", "new_name"), 
                                            help="Renames the file to new_name at the specified path.")
    

    #Создание подгруппы ключей необходимых для взаимодействия с реестром
    wr_group = parser.add_argument_group(title="Windwos Registry Commands", 
                                         description="This block describes commands that allow you to interact with the windows registry.To perform any operation with the registry, you must specify ONE of the following flags: -cr, -cu, -lm, -u, -cc.")
    
    #Группа взаимоисключающих ключей для указания корневого ключа
    wr_hkey_mutual_exclusive_group = wr_group.add_mutually_exclusive_group()
    wr_hkey_mutual_exclusive_group.add_argument("-cr", "--classes_root", action="store_true", help="HKEY_CLASSES_ROOT")
    wr_hkey_mutual_exclusive_group.add_argument("-cu", "--current_user", action="store_true", help="HKEY_CURRENT_USER")
    wr_hkey_mutual_exclusive_group.add_argument("-lm", "--local_machine", action="store_true", help="HKEY_LOCAL_MACHINE")
    wr_hkey_mutual_exclusive_group.add_argument("-u", "--users", action="store_true", help="HKEY_USERS")
    wr_hkey_mutual_exclusive_group.add_argument("-cc", "--classes_config", action="store_true", help="HKEY_CURRENT_CONFIG")

    #Группа взаимоисключающих ключей для указания типа записываемых в ключ данных
    wr_type_mutual_exclusive_group = wr_group.add_mutually_exclusive_group()
    wr_type_mutual_exclusive_group.add_argument("-rsz", "--reg_sz", action="store_true", help="REG_SZ key value type.")
    wr_type_mutual_exclusive_group.add_argument("-rdw", "--reg_dword", action="store_true", help="REG_DWORD key value type.")

    #Группа взаимоисключающих ключей для операций с реестром
    wr_operations_mutual_exclusive_group = wr_group.add_mutually_exclusive_group()
    wr_operations_mutual_exclusive_group.add_argument("-ck", "--create_key", 
                                                      metavar="path_to_key", 
                                                      help="Creates a new key in the registry.")
    wr_operations_mutual_exclusive_group.add_argument("-dk", "--delete_key", 
                                                      metavar="path_to_key", 
                                                      help="Removes a key from the registry at a given path.")
    wr_operations_mutual_exclusive_group.add_argument("-avtk", "--add_value_to_key", 
                                                      nargs=3, metavar=("path_to_key", "value_name", "value"), 
                                                      action="extend", 
                                                      help="Writes data to the key. It is necessary to use flags indicating the type of data being written: -rsz/--reg_sz, -rdw/--reg_dword.")

    #Парсинг заданных аргументов
    args = parser.parse_args()
    
    operation_result_str = colored('Operation result:', 'grey')
    if args.operations_set == "fs":
        #Обработка операций
        if args.create_file:
            print(f"{operation_result_str} {fs.create_file(args.create_file, create_mode='w') if args.rewrite else fs.create_file(args.create_file)}")
        elif args.remove_file:
            print(f"{operation_result_str} {fs.remove_file(args.remove_file)}")
        elif args.write_to_file:
            print(f"{operation_result_str} {fs.write_to_file(args.write_to_file[0], args.write_to_file[1])}")
        elif args.read_from_file:
            print(f"{operation_result_str} {fs.read_from_file(args.read_from_file)}")
        elif args.copy_file:
            print(f"{operation_result_str} {fs.copy_file(args.copy_file[0], args.copy_file[1])}")
        elif args.rename_file:
            print(f"{operation_result_str} {fs.rename_file(args.rename_file[0], args.rename_file[1])}")
    else:
        main_hkey = None
        #Если не указан ни один из флагов, указывающих на корневой ключ, то необходимо вернуть ошибку
        if args.current_user:
            main_hkey = "cu"
        elif args.classes_root:
            main_hkey = "cr"
        elif args.local_machine:
            main_hkey = "lm"
        elif args.users:
            main_hkey = "u"
        elif args.users:
            main_hkey = "cc"
        else:
            print(f"{colored('Error!', 'red')} None of the flags corresponding to the root key are specified [-cr, -cu, -lm, -u, -cc].")
            return

        #Обработка операций
        if args.create_key:
            print(f"{operation_result_str} {wrg.create_key(main_hkey, args.create_key)}")
        elif args.delete_key:
            print(f"{operation_result_str} {wrg.create_key(main_hkey, args.delete_key)}")
        elif args.add_value_to_key:
            if args.reg_sz:
                print(f"{operation_result_str} {wrg.set_value_to_key(main_hkey, args.add_value_to_key[0], REG_SZ, args.add_value_to_key[1], args.add_value_to_key[2])}")
            elif args.reg_dword:
                print(f"{operation_result_str} {wrg.set_value_to_key(main_hkey, args.add_value_to_key[0], REG_DWORD, args.add_value_to_key[1], args.add_value_to_key[2])}")
            else:
                print(f"{colored('Error!', 'red')} You must specify the data type flag. [-rs/--reg_sz, -rfw/--reg_dword]")


if __name__ == "__main__":
    main()