from datetime import datetime, date, time

navi_but = ['list', 'add', 'show', 'edit', 'del', 'exit']

def input_choice():
    keyword = input('Enter command: ')
    for data in navi_but:
        if keyword == data:
            return keyword
    else:
        print('Enter correct command!')

def print_notes(book: list[dict[str, str]]):
    if book:
        print('-' * 122)
        for i, contact in enumerate(book, 1):
            print(f'{i:<3} | {contact["title"]:<30} | {contact["note"]:<60} | {contact["date"]:<20}')
        print('-' * 122)
    else:
        print('Something went wrong')

# def print_message(message: str):
#     print('\n' + '=' * len(message))
#     print(message)
#     print('=' * len(message) + '\n')

def input_notes(new_id: int):
    note = {}
    print('Welcome friend! Enter new note: ')
    note['id'] = str(new_id)
    note['date'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    note['title'] = input('Enter your title: ')
    note['note'] = input('Enter your thoughts: ')
    return note

# def input_search(message) -> str:
#     return input(message)

