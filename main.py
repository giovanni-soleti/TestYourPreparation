import random
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

def total_question(ex):
    k = len(ex)
    while ex[k - 1] == '':
        k -= 1
    return k


def load():
    global num_questions, questions_done, question_list
    try:
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        path.set(askopenfilename())
        f = open(path.get())
        not_splitted_test.set(f.read())
        questions_list = not_splitted_test.get().split("\n")
        num_questions = total_question(questions_list)
        questions_done = []
        load_lab.set(path.get() + ' has been upload successfully')
        f.close()
    except:
        load_lab.set('.txt file has not been upload successfully')

def generate():
     try:
        global num_questions, questions_done
        questions_list = not_splitted_test.get().split("\n")
        question = random.randrange(num_questions)
        if len(questions_done) != num_questions:
            while question in questions_done:
                question = random.randrange(num_questions)
            current_quest.set(questions_list[question])
        else:
            current_quest.set("All questions are done")
        questions_done.append(question)


     except:
        current_quest.set("Problem is occured, try to reload .txt file")

def remove():
    try:
        f = open(path.get(), 'r+')
        txt_to_find = current_quest.get() + "\n"
        txt_to_replace = ''
        text = f.read()
        text = re.sub(txt_to_find, txt_to_replace, text)
        f.seek(0)
        f.write(text)
        f.truncate()
        f.close()
        rem_lab.set("Question has been removed from .txt file")
    except:
        rem_lab.set("Question hasn't been removed from .txt file, maybe you've to Load/Reload .txt file")

def substitute():
    try:
        f = open(path.get(), 'r+')
        txt_to_find = current_quest.get()
        txt_to_replace = replace.get()
        text = f.read()
        text = re.sub(txt_to_find, txt_to_replace, text)
        f.seek(0)
        f.write(text)
        f.truncate()
        f.close()
        rem_lab.set("Question has been changed in .txt file")
    except:
        rem_lab.set("Question hasn't been changed in .txt file, maybe you've to Load/Reload .txt file")
#This function has been implemented to kill the process when window is closed
def destroyer():
    root.quit()
    root.destroy()
    sys.exit()


root = Tk()
root.title('Test your preparation - 0.0.1')
#add a frame to the root with padding
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# After the frame is created, grid places it directly inside our main application window.
# The columnconfigure/rowconfigure bits tell Tk that the frame should expand to fill
# any extra space if the window is resized.
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#let's create the widget
#first element represent the parent of the widget (where it appears)

# StringVar global variables
current_quest = StringVar()
not_splitted_test = StringVar()
load_lab = StringVar()
path = StringVar()
replace = StringVar()
rem_lab = StringVar()
# Load label initialization
load_lab.set("To start your test click on Load Button and upload your .txt file")

#TEXT LABEL
label_tit = ttk.Label(mainframe, width= 110,text="Welcome in TestYourPrep, let's test your abilities:").grid(column=1, row=1, sticky=(S, E))
label_quest = ttk.Label(mainframe, width=110, textvariable=current_quest).grid(column=1, row=3)
label_load = ttk.Label(mainframe, width=110, textvariable=load_lab).grid(column=1, row=2)
label_rem = ttk.Label(mainframe, width=110, textvariable=rem_lab).grid(column=1, row=4)
feet_entry = ttk.Entry(mainframe, width=100, textvariable=replace).grid(column=1, row=5, sticky=(W))

#BUTTON LABEL
butt_load = ttk.Button(mainframe, width=18, text="Load",command=load).grid(column=2, row=2)
butt_generate = ttk.Button(mainframe, width=18, text="Generate Question", command=generate).grid(column=2, row=3)
butt_remove = ttk.Button(mainframe, width=18, text="Remove question", command=remove).grid(column=2, row=4)
butt_sub = ttk.Button(mainframe, width=18, text="Substitute question", command=substitute).grid(column=2, row=5)

#ADD PADDLING AT EACH WIDGET
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.protocol("WM_DELETE_WINDOW", destroyer)
root.mainloop()