import streamlit as st
from datetime import datetime

FILE_PATHS = {'data': r'data/to_do_list_data.txt',
              'history': r'data/to_do_list_history.txt'}


def get_to_do_list(file_path: str = FILE_PATHS['data']) -> list[str]:
    """ Loads and returns a to-do list from the specified file path.
    Ensures that the list does not contain duplicate trailing lines.
    """
    with open(file_path, mode='r', encoding='UTF-8') as file:
        to_do_list = file.readlines()
        # Remove the first line, if present
        if to_do_list and to_do_list[0] == '\n':
            to_do_list.pop(0)
        # Remove duplicate trailing lines, if present
        if len(to_do_list) > 1 and to_do_list[-2] == to_do_list[-1]:
            to_do_list.pop(-1)
    return to_do_list


def save_to_do_list(to_do_list: list[str], file_path: str = FILE_PATHS['data'], save_mode='w') -> None:
    """ Saves the to-do list to the specified file.
    - save_mode='w': Overwrites the file.
    - save_mode='a': Appends to the file (e.g., for history).
    """
    with open(file_path, mode=save_mode, encoding='UTF-8') as file:
        file.writelines(to_do_list)


def check_valid_input(new_to_dox: str) -> bool:
    """ Returns False if the input is empty or only contains whitespace. """
    return not new_to_dox.isspace()


def add_new_to_do_logic(to_do_list: list[str], new_to_do: str) -> list[str]:
    """ Add a new to-do item to the list and save it. """
    timestamped_to_do = f"{new_to_do} {datetime.now().strftime('%d. %m. %Y %H:%M')}\n"
    to_do_list.append(timestamped_to_do)
    save_to_do_list(to_do_list, file_path=FILE_PATHS['data'])
    return to_do_list


def export_data(data, file_path):
    with open(file_path, 'r') as file:
        st.download_button(label=f"Export {data} 💾",
                           data=file,
                           file_name=f"to_do_list_{data}.txt",
                           help=f"Export to-does {data} in plain text format.",
                           key=f"to_do_list_{data}.txt")


def show_to_do_history():
    """ Show the list with finished to-does. """
    to_do_list_history = get_to_do_list(file_path=FILE_PATHS['history'])
    form = st.form('History data', clear_on_submit=True)
    with form:
        for index, to_do in enumerate(to_do_list_history):
            st.write(f"{str(index + 1)}. {to_do}")
        form.form_submit_button('Hide History')


def delete_to_do_history():
    """ Delete the list with finished to-does. """
    clear_history = []
    save_to_do_list(clear_history, file_path=FILE_PATHS['history'])
    st.success('The history of your finished to-does was deleted.', icon="✅")
