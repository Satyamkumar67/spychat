# Importing spy details
from spy_details import spy, Spy, ChatMessage, friends

# Importing Steganography to encode and decode images
from steganography.steganography import Steganography

# For printing in color in terminal
from termcolor import colored, cprint

import colorama

from colorama import Fore

STATUS_MSG = ["Shashwat Gupta", "gupta ji ka ladka hai yeh to", "**some cool stuff**", "hakuna matata"]

urgent = ["SOS", "SAVE", "URGENT", "DANGER", "HELP", "STALKING", "GUN", "HOSPITAL", "ACCIDENT",
          "SUICIDE", "STALKED", "KILL", "BLOOD", ]


# Welcoming the spy
def welcome_spy():
    if spy.rating > 4.5:

        print "those are some pretty nice numbers"

    elif 3.5 <= spy.rating <= 4.5:

        print "looks just fine"

    elif 2.5 <= spy.rating <= 3.5:

        print "definitely need inprovement "

    else:

        print "beta tmse na ho payega ... hume tmhsre num bilkul theek nahi lag rhe hai .. tmse na ho payega"

    print "Welcome. You are now online!"

    # print "Your name is " + spy.name + "\nYour age is " + str(spy.age) + "\nYour rating is " + str(spy.rating)

    print "Your name is %s\nYour age is %d\nYour rating is %f" % (spy.name, spy.age, spy.rating)


# StartChat method to display and call menu option methods
def start_chat():
    show_menu = True

    while show_menu:

        menu_choices = "hey there! wanna do something ? select one of 5. NO .. select the lsst one. \n1. Add a status update.\n2. Add a friend.\n3. Send a secret message." \
                       "\n4. Read a secret message.\n5. Read chats from a user.\n6. Close application.\n"

        menu_choice = int(raw_input(menu_choices))

        if menu_choice == 1:

            # Updating the spy's status
            new_status = add_status()

            print "Status updated to :-\n" + new_status

        elif menu_choice == 2:

            # Adding a spy friend
            friend_count = add_friend()

            print "You currently have %d spy friends." % friend_count

        elif menu_choice == 3:

            send_a_message()

        elif menu_choice == 4:

            read_a_message()

        elif menu_choice == 5:

            read_chat()

        elif menu_choice == 6:

            # Close application
            show_menu = False

        else:

            print "Wrong choice"


def add_status():
    # Displaying the current status
    print spy.current_status

    default = (raw_input("wanna  select from the old statuses (Y/N)?:\n")).upper()

    if default.upper() == "N":

        new_status_msg = raw_input("enter new status\n")

        if len(new_status_msg) > 0:

            spy.current_status = new_status_msg

            # Appending new status to status list
            STATUS_MSG.append(new_status_msg)

        else:

            print "all okay ? try again..!"

    elif default.upper() == "Y":

        item_pos = 1

        # Displaying default statuses
        for status in STATUS_MSG:
            print "%d. %s" % (item_pos, status)

            item_pos = item_pos + 1

        msg_choice = int(raw_input("Enter the status index of you choice :\n"))

        # Updating current status
        spy.current_status = STATUS_MSG[msg_choice - 1]

    else:

        print "Wrong choice!"

        quit()

    return spy.current_status


# Adding a new friend to the friends list
def add_friend():
    new_friend = Spy("", "", 0, 0)

    new_friend.name = raw_input("what is your friend's name :\n")

    new_friend.salutation = raw_input("Is your friend Mr. or Ms. :\n")



    new_friend.age = int(raw_input("whats your friend's age :\n"))

    new_friend.rating = float(raw_input("whats your friend's rating :\n"))
    if new_friend.rating > 4:

        print "kuch seekho inse ... nalayak kahin k"

    elif 3<= new_friend.rating <= 4:

        print "just like you... loser -_-"

    elif 2 <= new_friend.rating <= 3:

        print "nihayati nalayak dost hai tmhare "

    else:

        print "beta tmse na ho payega ... hume tmhsre num bilkul theek nahi lag rhe hai .. tmse na ho payega"

    # Checking eligibility of new friend
    # The criteria that his spy_rating should be greater than mine seems to be a bit wonky :-(
    if len(new_friend.name) > 0 and 12 < new_friend.age < 50 and spy.rating <= new_friend.rating <= 5.0:

        # Adding a new friend to my friends list
        friends.append(new_friend)

        print new_friend.salutation + " " + new_friend.name + " is now your friend"

    else:

        print "yeh banda sahi nahi hai tere liye... bigad k rakh dega tujhe"

    # Returning the no of friends
    return len(friends)


# A method to select a friend from friend's list
def select_a_friend():
    item_no = 1

    space = " "

    print "Friend's List :-\nS.no \t Name " + space * 26 + " Age \t Rating\t Online status"

    for friend in friends:
        print "%d. \t %s" % (item_no, friend.salutation + " " + friend.name) + space * (
            30 - len(friend.name) - 3) + " %d \t %.2f \t %s" % (friend.age, friend.rating, friend.spy_is_online)

        item_no += 1

    friend_choice = int(raw_input("Select a friend :-\n"))

    friend_pos = friend_choice - 1

    if friend_pos + 1 > len(friends):

        print "Imaginary friend found Send him/her an imaginary telepathic message"

        quit()

    else:

        # Returning the chosen friend's index
        return friend_pos


# Method to encode and ready the message to be sent
def send_a_message():
    recipient = select_a_friend()

    input_img = raw_input("Enter the name(\"Path\") of the image :\n")

    secret_msg = raw_input("Enter the secret message :-\n")

    output_img = "Output.jpg"

    Steganography.encode(input_img, output_img, secret_msg)

    # Making a chat message object
    new_chat = ChatMessage(secret_msg, True)

    # Adding the new chat to chats list
    friends[recipient].chats.append(new_chat)

    print "Your secret message is ready to be sent!"


# Reading the secret message received from your friend.
def read_a_message():
    sender = select_a_friend()

    output_img = raw_input("Enter the name of the received image :\n")

    secret_text = Steganography.decode(output_img)

    if len(secret_text) > 0:

        new_chat = ChatMessage(secret_text, False)

        # Adding the received message to the chats list
        friends[sender].chats.append(new_chat)

        text = secret_text.split()

        # Keeping record of the no of words spoken by friend to calculate average words per chat
        friends[sender].word_count += len(text)

        colorama.init()

        temp = (secret_text.upper()).split()

        count = 0

        for special in urgent:

            if special in temp:
                count += 1

        if count > 0:

            cprint("RED ALERT ! \nYour spy_friend " + friends[sender].salutation + friends[sender].name + " needs you",
                   'red')

            print "%s said : %s" % (friends[sender].salutation + friends[sender].name, secret_text)

        else:

            print "%s said : %s" % (friends[sender].salutation + friends[sender].name, secret_text)

        print "\n"

        print "Average  words said by %s is %d" % (friends[sender].name, friends[sender].word_count / sum(
            1 for chat in friends[sender].chats if chat.sent_by_me is False))

        # Removing your friend from friends list if he/she is a bit too chatty
        if (len(secret_text.split())) > 100:
            print "%s removed from friends list due to humongous messages." % friends[sender].name

            friends.remove(friends[sender])

    else:

        print "There was no message present in the file!"


# Reading the chat history with any friend
def read_chat():
    friend_choice = select_a_friend()

    colorama.init()

    for chat in friends[friend_choice].chats:

        if chat.sent_by_me:

            cprint("At " + colored(chat.time.strftime("%d %B %Y"), 'blue') + " : " + colored('You',
                                                                                             'red')
                   + " said :- " + Fore.BLACK + chat.message)

        else:

            cprint(
                "At " + colored(chat.time.strftime("%d %B %Y"), 'blue') + " : " + colored(friends[friend_choice].name,
                                                                                          'red')
                + ' said :- ' + Fore.BLACK + chat.message)


print("Hello Mr.Spy")

existing = (raw_input(
    "Continue with default spy or would you like to create a new identity\nPress Y for default and N for new ")).upper()

if existing == 'N':

    spy.name = raw_input("What is your name?\n")

    spy.age = 0

    spy.rating = 0.0

    spy.spy_is_online = False

    # Calculating the length of the name

    string_length = len(spy.name)

    # Check if name is given

    if string_length > 0:

        spy.salutation = raw_input("Should I call you Mr. or Ms.\n")

        spy.name = spy.salutation + " " + spy.name

        print "Hello " + spy.name + "!"

    else:

        print "Sorry you didn't enter your name \n Please run the program again !"

    spy.age = int(raw_input("Please enter your age\n"))

    spy.rating = float(raw_input("Please enter your spy rating.\n"))

    if 12 < spy.age < 50 and 0.0 <= spy.rating <= 5.0:

        print "Welcome to the SpyNet!"

        welcome_spy()

        start_chat()

    else:

        print "You're not eligible according to the information provided. Please try again!"



else:

    welcome_spy()

    start_chat()