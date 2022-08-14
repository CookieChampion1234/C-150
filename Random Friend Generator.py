from tkinter import*
import random

root=Tk()
root.geometry("500x500")
root.title("Random Friend Generator")

add_friend = Entry(root)
add_friend.place(relx=0.5, rely=0.2, anchor=CENTER)

friend_list = Label(root)
random_number_list = Label(root)
random_friend = Label(root)

list1 = []

def addFriend():
    new_friend = add_friend.get()
    list1.append(new_friend)
    friend_list['text'] = "Your friend list is : " + str(list1)
    
def randomFriend():
    length = len(list1)
    random_number = random.randint(0, length-1)
    random_number_list['text'] = str(random_number)
    random_person = list1[random_number]
    random_friend['text'] = "Your random friend is : " + str(random_person)
    
btn = Button(text="Add Friend", command=addFriend)
btn.place(relx=0.5, rely=0.3, anchor=CENTER)

btn2 = Button(text="Pick Random Friend", command=randomFriend)
btn2.place(relx=0.5, rely=0.5, anchor=CENTER)

friend_list.place(relx=0.5, rely=0.4, anchor=CENTER)
random_number_list.place(relx=0.5, rely=0.6, anchor=CENTER)
random_friend.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()



