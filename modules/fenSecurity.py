from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import pathlib
import os
from bcrypt import hashpw, gensalt

class fenCode:
    """
    Class that creates an authentication window
    Sample Call and Check in Main Program

    securityFen = fenCode() # We open the security window
    if securityFen.verification==False: # If the user closes we leave the program
        del securityFen # We delete the object 
        sys.exit(0) 
    else: # Otherwise we get the code of the user and we delete the object
        codeUtilisateur = securityFen.code
        del securityFen
    """

    def __init__(self):
        """
        Builder fenCode
        """
        self.verification = False
        self.fenPass = Tk()
        self.fenPass.title("SECURITY")
        self.fenPass.geometry("250x85+100+0")
        self.fenPass.resizable(width=False, height=False)
        self.typePassword = Label(self.fenPass, text="PASSWORD :", font=("Arial 12 bold"))
        self.typePassword.pack()
        self.uneVar = StringVar
        self.uneEntre = Entry(self.fenPass, textvariable=self.uneVar, show="*")
        self.uneEntre.pack()
        self.fenPass.bind('<Return>', self.recupPass)
        self.bouton_valider = Button(self.fenPass, text="Next", command=lambda: self.recupPass(), fg="green", font=("Calibri 12 bold"))
        self.bouton_valider.pack(side="right")
        self.bouton_quitter = Button(self.fenPass, text="Quit", command=quit, fg="red", font=("Calibri 12 bold"))
        self.bouton_quitter.pack(side="left")
        if os.path.isfile("{}\client.aes".format(os.path.dirname(os.path.realpath(__file__)))):
            self.bouton_changePass = Button(self.fenPass, text="Change", command=lambda: self.recupNewPass(), font=("Calibri 12 bold"))
            self.bouton_changePass.pack(side="top")
        self.fenPass.mainloop()  # END fenPass windows

    def recupPass(self, *event):
        """
        Function that serves to retrieve the user's code
        """
        self.code = self.uneEntre.get()
        # We look if the user has already created a code
        if os.path.isfile("{}\client.aes".format(os.path.dirname(os.path.realpath(__file__)))):
            with open("{}\client.aes".format(os.path.dirname(os.path.realpath(__file__))), 'rb') as outfile:
                aCode = outfile.read() # need update switch application. For example on heroku put os.environ["code"]
        else: 
            key = hashpw(self.code.encode(), gensalt()) # It is important to save it because the gensalt generates a random key
            with open("{}\client.aes".format(os.path.dirname(os.path.realpath(__file__))), 'wb') as outfile:
                outfile.write(key)
            showinfo("Password register", "Your password has been saved", icon="info")
            aCode = key
        try:
            if hashpw(self.code.encode(), aCode) == aCode:
                self.fenPass.destroy()
                self.verification = True
            else: 
                showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")
        except:
            showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")
    
    def recupNewPass(self):
        """
        Function that serves to get the new password (if exist)
        """
        self.code = self.uneEntre.get()
        with open("{}\client.aes".format(os.path.dirname(os.path.realpath(__file__))), 'rb') as outfile:
                aCode = outfile.read() # need update switch application. For example on heroku put os.environ["code"]
        if hashpw(self.code.encode(), aCode) == aCode:
            self.fenPass.title("New password")
            self.typePassword.destroy()
            self.typePassword = Label(self.fenPass, text="Update password", font=("Arial 12 bold"))
            self.typePassword.pack(side="top")
            #self.bouton_newPass = Button(self.fenChange, fg='green', text="Confirm", command = lambda: showinfo("-- ERROR --", "Your password has been updated!", icon="info"))
            self.bouton_newPass = Button(self.fenPass, fg='green', text="Confirm", command = lambda: self.updatePassword())
            self.bouton_newPass.pack()
            self.bouton_changePass.destroy()
        else:
            showinfo("-- ERROR --", "Please enter the old password before!", icon="warning")
    
    def updatePassword(self):
        """
        Function that serves to change the password in file client.aes
        """
        with open("{}\client.aes".format(os.path.dirname(os.path.realpath(__file__))), 'wb') as outfile:
            outfile.write(hashpw(self.uneEntre.get().encode(), gensalt()))
        showinfo("Password updated", "Your password has been updated!")
        self.fenPass.destroy()
        self.verification = True