# список контактів
user_phone = {}

def main():

    def hello_handler():
        return "How can I help you?"
    
    def exit_handler():
        return "Good bye!"
    
    def show_all_handler():
        global user_phone
        return user_phone
    
       
    def input_error(func):
        def inner(args):
            try:
                result = func(args)
                return func(args)
            except KeyError:
                return "No user with this name"
            except ValueError:
                return "Give me name and phone please"
            except IndexError:
                return "Enter user name"
        return inner


    @input_error
    def add_handler(args):
        new_str = args.strip().split(" ")
        global user_phone
        user_phone[str(new_str[0])] = int(new_str[1])
        return f"The contact <{new_str[0]}> with the number <{new_str[1]}> is added to the list"

    @input_error
    def change_handler(args):
        global user_phone
        new_str = args.strip().split(" ")
        if new_str[0] in user_phone.keys():
            user_phone[new_str[0]] = int(new_str[1])
            return f"The <{new_str[0]}> contact number has been changed to <{new_str[1]}>"
        else:
            raise KeyError
        
    @input_error
    def phone_handler(args):
        new_str = args.strip()
        global user_phone
        if new_str in user_phone.keys():
            return f"Contact {new_str}: {user_phone[new_str]}"
        else:
            raise KeyError
        
       
    while True:
        enter_phrase = input("... ")
        if enter_phrase.lower() in "hello":
            print(hello_handler())
              
        elif enter_phrase.lower().startswith("add "):
            print(add_handler(enter_phrase[3:]))

        elif enter_phrase.lower().startswith("change "):
            print(change_handler(enter_phrase[6:]))

        elif enter_phrase.lower().startswith("phone "):
            print(phone_handler(enter_phrase[5:]))

        elif enter_phrase.lower().startswith("show all"):
            print(show_all_handler())

        elif enter_phrase.lower() in ".goodbyecloseexit":
            print(exit_handler())
            break

        else:
            print("None of the coommands have been entered")

        
main()
print(user_phone)