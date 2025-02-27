import winreg as wrg
from modules.message import winreg_msg_storage


def create_key(hkey: str, path_to_new_key:str) -> str:
    """
        Создаёт новый ключ в реестре.
        
        :param hkey: конрневой ключ в сокращённом формате (например, HKEY_CURRENT_USER == cu).
        :param path_to_new_key: путь до ключа, который необходимо создать, включая его имя.
        :return: строку с результатом операции.
    """

    main_key_location = None

    if hkey == "cr":
        main_key_location = wrg.HKEY_CLASSES_ROOT
    elif hkey == "cu":
        main_key_location = wrg.HKEY_CURRENT_USER
    elif hkey == "lm":
        main_key_location = wrg.HKEY_LOCAL_MACHINE
    elif hkey == "u":
        main_key_location = wrg.HKEY_USERS
    elif hkey == "cc":
        main_key_location = wrg.HKEY_CURRENT_CONFIG
    

    #Попытка создать новый ключ
    try:
        new_key = wrg.CreateKeyEx(main_key_location, path_to_new_key, 0, wrg.KEY_ALL_ACCESS)
        wrg.CloseKey(new_key)
        return winreg_msg_storage["create_key"][True]
    except PermissionError:
        return winreg_msg_storage["create_key"][False][PermissionError]
    except FileNotFoundError:
        return winreg_msg_storage["create_key"][False][FileNotFoundError]
    except OSError:
        return winreg_msg_storage["create_key"][False][OSError]



def delete_key(hkey: str, path_to_key: str) -> str:
    """
        Удаляет ключ из реестра.

        :param hkey: конрневой ключ в сокращённом формате (например, HKEY_CURRENT_USER == cu)
        :param path_to_key: путь до ключа, который необходимо удалить
        :return: строку с результатом операции.
    """

    main_key_location = None

    if hkey == "cr":
        main_key_location = wrg.HKEY_CLASSES_ROOT
    elif hkey == "cu":
        main_key_location = wrg.HKEY_CURRENT_USER
    elif hkey == "lm":
        main_key_location = wrg.HKEY_LOCAL_MACHINE
    elif hkey == "u":
        main_key_location = wrg.HKEY_USERS
    elif hkey == "cc":
        main_key_location = wrg.HKEY_CURRENT_CONFIG


    #Попытка удалить ключ
    try:
        wrg.DeleteKeyEx(main_key_location, path_to_key, wrg.KEY_ALL_ACCESS, 0)
    except PermissionError:
        return winreg_msg_storage["delete_key"][False][PermissionError]
    except FileNotFoundError:
        return winreg_msg_storage["delete_key"][False][FileNotFoundError]
    except OSError:
        return winreg_msg_storage["delete_key"][False][OSError]



def set_value_to_key(hkey: str, path_to_key: str, type, value_name: str ,value:str) -> str:
    """
        Добавляет данные в ключ.

        :param hkey: конрневой ключ в сокращённом формате (например, HKEY_CURRENT_USER == cu)
        :param path_to_key: путь до ключа, в который необходимо записать данные.
        :param type: типа записываемых данных.
        :param value_name: имя, записываемого значения.
        :param value: значение, которое необходимо записать.
        :return: строку с результатом операции
    """

    main_key_location = None

    if hkey == "cr":
        main_key_location = wrg.HKEY_CLASSES_ROOT
    elif hkey == "cu":
        main_key_location = wrg.HKEY_CURRENT_USER
    elif hkey == "lm":
        main_key_location = wrg.HKEY_LOCAL_MACHINE
    elif hkey == "u":
        main_key_location = wrg.HKEY_USERS
    elif hkey == "cc":
        main_key_location = wrg.HKEY_CURRENT_CONFIG

    #Попытка записать данные в ключ
    try:
        key = wrg.OpenKeyEx(main_key_location, path_to_key, 0, wrg.KEY_ALL_ACCESS)

        if type == wrg.REG_SZ:
            wrg.SetValueEx(key,value_name, 0, wrg.REG_SZ, value)
        elif type == wrg.REG_DWORD:
            wrg.SetValueEx(key,value_name, 0, wrg.REG_DWORD, int(value))
        return winreg_msg_storage["set_value_to_key"][True]
    except PermissionError:
        return winreg_msg_storage["set_value_to_key"][False][PermissionError]
    except FileNotFoundError:
        return winreg_msg_storage["set_value_to_key"][False][FileNotFoundError]
    except OSError:
        return winreg_msg_storage["set_value_to_key"][False][OSError]
    except ValueError:
        return winreg_msg_storage["set_value_to_key"][False][ValueError]

