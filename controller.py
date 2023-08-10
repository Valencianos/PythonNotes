import view
import model

my_notes = model.Notes('notes.json')

def start():

    while True:
        print('Main menu:\n',
        'list - show all notes\n',
        'add  - add new note\n',
        'show - show note\n',
        'edit - edit note\n',
        'del  - delete note\n',
        'exit - save & exit\n')

        choice = view.input_choice()

        match choice:
            case 'list':
                notes = my_notes.get_notes()
                view.print_notes(notes)
                print('What u gonna do?')
            case 'add':
                note = view.input_notes(my_notes.get_id())
                title = my_notes.add_note(note)
                print('Note "' + title + '" successfully added')
            case 'show':
                pass
            case 'edit':
                pass
            case 'del':
                pass
            case 'exit':
                my_notes.save_note()
                print('Notes successfully saved')
                break

#             case 2:
#                 model.save_file()
#                 view.print_message(tf.save_successful)
#             case 3:
#                 pb = model.get_pb()
#                 view.show_contact(pb, tf.empty_phone_book)
#             case 4:
#                 new_contact = view.input_contact(tf.new_contact)
#                 name = model.add_contact(new_contact)
#                 view.print_message(tf.add_contact_successful(name))
#             case 6:
#                 pb = model.phone_book
#                 view.show_contact(pb, '')
#                 choice = view.input_choice(len(pb), tf.change_choice) - 1
#                 change_contact = view.input_contact(tf.change_contact)
#                 res = model.change(choice, change_contact)
#                 view.print_message(tf.changed(res['name']))
#             case 7:
#                 pb = model.get_pb()
#                 index = view.input_index(tf.index_del_contact, pb)
#                 name = model.del_contact(index)
#                 view.print_message(tf.del_contact(name))
