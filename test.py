STATUS_MSG = ["Kumar! Rahul Kumar!", "Licensed to kill", "Just a guy on holiday!"]

def add_status(current_status_message):

    default = raw_input("Do you want to select from the old statuses (Y/N)?");

    if default.upper() == "N":

        new_status_msg = raw_input("Set a new status message");

        if len(new_status_msg) > 0:

            STATUS_MSG.append(new_status_msg)

        else:

            item_pos = 1

            for status in STATUS_MSG:

                print item_pos + ". " + status

                item_pos = item_pos + 1

            msg_choice = int(raw_input("Enter the status index of you choice"))

            print STATUS_MSG[msg_choice-1]

        return STATUS_MSG

add_status("test")

def add_friend():