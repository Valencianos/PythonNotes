# PATH = 'phonebook.txt'

# phone_book: list[dict[str, str]] = []

# def open_file():
#     global phone_book, PATH
#     with open(PATH, 'r', encoding='UTF-8') as file:
#         data = file.readlines()
#     for contact in data:
#         contact = contact.strip().split(';')
#         contact = {'name': contact[0], 'phone': contact[1]}
#         phone_book.append(contact)

# def get_pb() -> list[dict[str,str]]:
#     global phone_book
#     return phone_book
# def add_contact(contact: dict[str, str]):
#     global phone_book
#     phone_book.append(contact)
#     return contact.get('name')

# def change(ind: int, contact: dict[str, str]) -> dict[str, str]:
#     cur_contact = phone_book[ind]
#     cur_contact.update(contact)
#     result = phone_book.pop(ind)
#     phone_book.insert(ind, cur_contact)
#     return result

# def save_file():
#     global phone_book, PATH
#     data = []
#     for contact in phone_book:
#         contact = ';'.join([value for value in contact.values()])
#         data.append(contact)
#     with open(PATH, 'w', encoding='UTF-8') as file:
#         file.write('\n'.join(data))

# def del_contact(index: int):
#     return phone_book.pop(index-1).get('name')

# def search_contact(word: str) -> list[dict[str, str]]:
#     result: list[dict[str, str]] = []
#     for contact in phone_book:
#         for field in contact.values():
#             if word.lower() in field.lower():
#                 result.append(contact)
#                 break
#     return result
