import view
import model

# def start():
#     while True:
#         choice = view.main_theme()
#         match choice:
#             case 1:
#                 model.open_file()
#                 view.print_message(tf.open_successful)
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
#             case 5:
#                 key_word = view.input_search(tf.input_search)
#                 result = model.search_contact(key_word)
#                 view.show_contact(result, tf.empty_search(key_word))
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
#             case 8:
#                 break