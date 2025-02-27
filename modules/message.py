from termcolor import colored

fs_msg_storage = {
    "create_file": {
        True: colored("The file was successfully created.", "green"),
        False:f"{colored('Error!', 'red')} There is already a file with the same name in this directory or you specified an incorrect path."
    },
    "remove_file": {
        True: colored("File deleted successfully.", "green"),
        False: f"{colored('Error!', 'red')} Invalid file path specified or file does not exist"
    },
    "write_to_file": {
        True: colored("The data was successfully written to the file.", "green"),
        False: f"{colored('Error!', 'red')} The file could not be opened, the path specified is incorrect, or the file does not exist."
    },
    "read_from_file": {
        True: colored("Data was successfully read from the file.", "green"),
        False: f"{colored('Error!', 'red')} The file could not be opened, the path specified is incorrect, or the file does not exist."
    },
    "copy_file": {
        True: colored("The file was copied successfully.", "green"),
        False: f"{colored('Error!', 'red')} The file could not be copied, the path specified is invalid, or the file does not exist."
    },
    "rename_file": {
        True: colored("The file has been successfully renamed.", "green"),
        False: f"{colored('Error!', 'red')} The file could not be renamed, the path specified is invalid, or the file does not exist."
    }
}

winreg_msg_storage = {
    "create_key": {
        True: colored("The key was successfully created.", "green"),
        False: {
            FileNotFoundError: f"{colored('Error!', 'red')} The specified path is invalid.",
            PermissionError: f"{colored('Error!', 'red')} Permission denied.",
            OSError: f"{colored('Error!', 'red')} It is impossible to write a key using this path."
        }
    },
    "delete_key": {
        True: colored("The key was successfully deleted.", "green"),
        False: {
            FileNotFoundError: f"{colored('Error!', 'red')} The specified path is invalid.",
            PermissionError: f"{colored('Error!', 'red')} Permission denied.",
            OSError: f"{colored('Error!', 'red')} It is impossible to delete a key using this path."
        }
    },
    "set_value_to_key": {
        True: colored("The data was successfully written to the key.", "green"),
        False: {
            FileNotFoundError: f"{colored('Error!', 'red')} The specified key could not be found.",
            PermissionError: f"{colored('Error!', 'red')} Permission denied.",
            OSError: f"{colored('Error!', 'red')} Cannot write data to this key.",
            ValueError: f"{colored('Error!', 'red')} Invalid value specified."
        }
    }
}
