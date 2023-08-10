import json
import datetime

class Notes:

    def __init__(self, path: str = '') -> None:
        self.notes: list[dict[str,str]] = []
        self.path = path

    def open_note(self):
        try:
            with open(self.path, 'r') as file:
                return json.load(file)
        except FileNotFoundError: 
            return -1
        
    def save_note(self):
        with open(self.path, 'w') as file:
            json.dump(self.notes, file)

    def get_id(self) -> int:
        if self.notes:
            id = max(int(value['id']) for value in self.notes) + 1
        else:
            id = 1
        return id

    # def print_list_notes(notes):
    #     count = 0
    #     for note in notes['id']:
    #         count += 1
    #         print(f"id: {note['id']} {note['date']} '{note['title']}' ")
    #     print(f"Total notes - {count}\n")

    def add_note(self, note: dict[str, str]):
        self.notes.append(note)
        return note.get('title')

    def get_notes(self) -> list(dict[str,str]):
        return self.notes

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


