
# def input_choice(size: int, message: str):
#     while True:
#         number = input(message)
#         if number.isdigit() and 0 < int(number) < size + 1:
#             return int(number)
#         else:
#             print(tf.wrong_choice(size))

# def main_theme() -> int:
#     print(*tf.menu, sep='\n')
#     return input_choice(len(tf.menu) -1, tf.input_choice)

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

# def input_contact(message: list[str]) -> dict[str, str]:
#     contact = {}
#     name = input(message[0])
#     phone = input(message[1])
#     if name:
#         contact['name'] = name
#     if phone:
#         contact['phone'] = phone
#     return contact

# def input_index(message: str, pb: list) -> int:

#     while True:
#         index = input(message)
#         if index.isdigit() and 0 < int(index) < len(pb) + 1:
#             return int(index)

# def input_search(message) -> str:
#     return input(message)

# menu = ['Main menu:',
#     '\t1. Open file',
#     '\t2. Save file',
#     '\t3. Show all contacts',
#     '\t4. Add contact',
#     '\t5. Find contact',
#     '\t6. Change contact',
#     '\t7. Delete contact',
#     '\t8. Exit\n']

# input_choice = 'Choose a point from menu: '

# def wrong_choice(limit: int) -> str:
#     return f'Incorrect point. Please enter point from 1 to {limit}'

# empty_phone_book = 'Phone book is empty or not open!'

# open_successful = 'Phone book successfully open'
# add_successful = 'Contact successfully added'
# save_successful = 'PhoneBook successfully saved'

# def change_sucessful(name: str) -> str:
#     return f'Contact {name} successfully changed'

# new_contact = ['Enter Name: ', 'Enter Phone: ']
# change_contact = ['Enter Name or press Enter to skip: ', 'Enter Phone or press Enter to skip: ']
# change_choice = 'Choose contact to change: '
# def add_contact_successful(name: str) -> str:
#     return f'Contact {name} successfully added'

# def changed(name: str) -> str:
#     return f'Contact {name} was changed'

# index_del_contact = 'Enter index of contact which you want to delete: '

# def del_contact(name: str):
#     return f'Contact {name} successfully deleted'

# input_search = 'What you looking for: '

# def empty_search(word) -> str:
#     return f'Contacts with "{word}" not found'