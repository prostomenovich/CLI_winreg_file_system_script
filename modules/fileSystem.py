import os
import shutil
from modules.message import fs_msg_storage
from termcolor import colored


def create_file(path_to_file: str, create_mode: str = "x") -> str:
    """
        Выполняет создание нового файла.

        :param path: абсолютный путь до нового файла [если указано только имя нового файла, то он будет создан в директории, из которой запускается скрипт]
        :param create_mode: режим создания файла, "w" или "x" [опционально, значение по умолчанию = "x", при наличии в директории по пути path файла с именем name, файл не будет перезаписан и операция завершится ошибкой. Если указано значение "w", файл будет перезаписан]
        :return: строка с результатом операции
    """

    #Попытка создать файл
    try: 
        with open(file=path_to_file, mode=create_mode) as file:
            pass
        return  fs_msg_storage["create_file"][True]
    except:
        return fs_msg_storage["create_file"][False]


def remove_file(path_to_file: str) -> str:
    """
        Выполняет удаление заданного файла.

        :param path_to_file: абсолютный путь до файла, который необходимо удалить [если указано только имя файла, то поиск будет производиться в директории, из которой был запущен скрипт]
        :param name: имя удаляемого файла [можно не указывать, если был задан параметр path_to_file и обязательно указывать, если происходит поиск в директории скрипта]
        :return: строка с результатом операции
    """
    
    #Попытка удалить файл по указанному пути
    try:
        os.remove(path=path_to_file)   
        return fs_msg_storage["remove_file"][True]
    except:
        return fs_msg_storage["remove_file"][False]


def write_to_file(path_to_file: str, data: str) -> str:
    """
        Осуществляет попытку записи в файл, переданных данных.

        :param path_to_file: абсолютный путь до файла, в который необходимо записать данные [если указано только имя, то поиск файла будет производиться в директории, из которой был запущен скрипт. Если указанный файл не найден, то будет создан новый файл и в него запишутся данные из параметра data]
        :param data: Данные, которые требуется записать в файл
        :return: строка с результатом операции
    """

    #Попытка записать данные в файл
    try:
        with open(file=path_to_file, mode="a", encoding="utf-8") as file:
            file.write(data)
        return fs_msg_storage["write_to_file"][True]
    except:
        return fs_msg_storage["write_to_file"][False]


def read_from_file(path_to_file: str) -> str:
    """
        Осуществляет попытку прочитать данные из файла и в случае успеха выводит их в консоль

        :param path_to_file: абсолютный путь до файла, который необходимо прочитать[если указано только имя файла, то поиск будет производиться в директории, из которой был запущен скрипт]
        :return: строка с результатом операции
    """
    
    #Попытка прочитать данные из файла
    try:
        with open(file=path_to_file, mode="r", encoding="utf-8") as file:
            print(f"{colored('File Contents', 'grey')}:\n{file.read()}")
        return fs_msg_storage["read_from_file"][True]
    except:
        return fs_msg_storage["read_from_file"][False]


def copy_file(source_path: str, destination_path: str) -> str:
    """
        Копирует файл из source_path в destination_path

        :param source_path: абослютный путь до файла, который необходимо скопировать [если путь не полный, то поиск будет производиться в директории, из которой запущен скрипт]
        :param destination_path: абсолютный путь до места, куда необходимо скопировать файл из source_path [после пути можно укахать новое имя файла, если этого не сделать, то файл будет скопирован с первоначальным названием]
        :return: строка с результатом операции    """
    try:
        shutil.copy(src=source_path, dst=destination_path)
        return fs_msg_storage["copy_file"][True]
    except:
        return fs_msg_storage["copy_file"][False]


def rename_file(path_to_file: str, new_name: str) -> str:
    """
        Переименование файла

        :param path_to_file: абсолютный путь до файла, который необходимо переименовать [если путь не полный, то поиск будет производиться в директории, из которой запущен скрипт]
        :param new_name: новое имя файла
        :return: строка с результатом операции

    """

    #Формирование пути до файла с изменённым именем
    new_name_path = path_to_file[:path_to_file.rfind("\\") + 1] + new_name if path_to_file.rfind("\\") != -1 else new_name
    
    #Попытка переименовать файл
    try:
        os.rename(path_to_file, new_name_path)
        return fs_msg_storage["rename_file"][True]
    except:
        return fs_msg_storage["rename_file"][False]
