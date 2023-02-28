from tkinter import *
import random
root=Tk()
root.title("Random Word Generator")
root.geometry("500x500")

label1 = Label(root)

def generate_random_word():
    alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    random1 = random.randint(1,26)
    random2 = random.randint(1,26)
    random3 = random.randint(1,26)
    random4 = random.randint(1,26)
    random5 = random.randint(1,26)
    
    randomalpha1 = alphalist[random1]
    randomalpha2 = alphalist[random2]
    randomalpha3 = alphalist[random3]
    randomalpha4 = alphalist[random4]
    randomalpha5 = alphalist[random5]
    
    label1["text"] = randomalpha1 + randomalpha2 + randomalpha3 + randomalpha4 + randomalpha5

btn = Button(root, text="Generate Word", command = generate_random_word)
btn.place(relx = 0.5, rely = 0.4, anchor = CENTER)
label1.place(relx = 0.5, rely = 0.5, anchor = CENTER)
root.mainloop()