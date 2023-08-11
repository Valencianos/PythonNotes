from datetime import datetime

navi_but = ['list', 'add', 'show', 'edit', 'del', 'exit', 'save', 'open']

def input_choice():
    keyword = input('Enter command: ')
    for data in navi_but:
        if keyword == data:
            return keyword
    else:
        print('Enter correct command!')

def print_notes(notes: list[dict[str, str]]):
    if notes:
        print('-' * 122)
        for id, data in enumerate(notes, 1):
            print(f'{id:<3} | {data["title"]:<30} | {data["note"]:<60} | {data["date"]:<20}')
        print('-' * 122)
    else:
        print_message('Something went wrong or notes is empty')

def print_message(message: str):
    print('-' * len(message))
    print(message)
    print('-' * len(message))

def input_notes(new_id: int):
    temp_note = {}
    print('Welcome friend! Enter new note: ')
    temp_note['id'] = str(new_id)
    temp_note['date'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    temp_note['title'] = input('Enter title: ')
    temp_note['note'] = input('Enter notes: ')
    return temp_note

def input_search(message) -> str:
    return input(message)

def input_index(message: str, notes: list) -> int:
    print_notes(notes)
    while True:
        index = input(message)
        if index.isdigit() and 0 < int(index) < len(notes) + 1:
            return int(index)