from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window=Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score=0
    # ASK A QUESTION AND CHECK THE ANSWER
    user=simpledialog.askstring(title=None,prompt="the capital of France is London")
    if(user =="false"):
        score+=1
    #      // 2.  Ask the user a question 
    question=simpledialog.askstring(title=None,prompt="tomatoes are a vegtable")
    #      // 3.  Use an if statement to check if their answer is correct
    if(question =="false"):
          score+=1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    then=simpledialog.askstring(title=None,prompt="Dolphins are fish")
    if(then =="false"):
        score+=1
    next=simpledialog.askstring(title=None,prompt="Humans can't live without oxygen")
    if(next =="true"):
        score+=1
    last=simpledialog.askstring(title=None,prompt="the Turritopsis dohrnii jellyfish is immortal")
    if(last=="true"):
        score+=1
    # After all the questions have been asked, tell the user their final score
    messagebox.showinfo(message=score)
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
    window.mainloop()
