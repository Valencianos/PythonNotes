from datetime import datetime, date, time

navi_but = ['list', 'add', 'show', 'edit', 'del', 'exit']

def input_choice():
    keyword = input('Enter command: ')
    for data in navi_but:
        if keyword == data:
            return keyword
    else:
        print('Enter correct command!')


# def show_contact(book: list[dict[str, str]], message: str):
#     if book:
#         print('\n' + '=' * 55)
#         for i, contact in enumerate(book, 1):
#             print(f'{i:<3} | {contact["name"]:<30} | {contact["phone"]:<15}')
#         print('=' * 55 + '\n')
#     else:
#         print(message)

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

