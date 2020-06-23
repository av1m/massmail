# -*-coding= utf-8 -*-
import smtplib  # smtplib module send mail
import webbrowser # For redirige on website
from modules.fenSecurity import *
from modules.gmail_auth import * 
import sys
from pathlib import Path

def sendmail():
    """
    Function that allows to send emails according to the email address sent:
    nbMailAttack for 'Spam' the receiver(s)
    """
    nbMailAttack = int(unMailAttack.get())
    # Check if client_secret.json exist, if not we put smtp (and not use API)
    if Path("client_secret.json").is_file() and nbMailAttack <= 1:
        smtp = ""
    else:
        smtp = 'smtp.gmail.com'
    # Sign In
    mail_sender = str(unFROM.get()).lower()
    mail_passwd = str(unFROMmdp.get())
    # Recover email address and process to see which email it is in order to choose the corresponding smtp server
    mail_recup = str.split(unTO.get("1.0", "end-1c").replace(" ", ''), ";")
    ISP = mail_sender.split("@")
    ISP = ISP[1].split(".")
    ISP = ISP[0].lower()
    SUBJECT = str(unSUBJECT.get())
    TEXT = str(unTEXT.get("1.0", "end-1c"))
    for TO in mail_recup:
        i = 1
        TO = str(TO.strip()).lower()
        # We get the right address ismp with the right ports
        if ISP != 'gmail' or smtp == 'smtp.gmail.com':
            if ISP == 'live' or ISP == 'hotmail' or ISP == 'outlook':
                server = smtplib.SMTP("smtp.live.com", 25)
            if ISP == 'gmail':
                server = smtplib.SMTP("smtp.gmail.com", 587)
            elif ISP == 'free':
                server = smtplib.SMTP("smtp.free.fr", 587)
            elif ISP == 'orange':
                server = smtplib.SMTP("smtp.orange.fr", 587)
            elif ISP == 'sfr':
                server = smtplib.SMTP("smtp.sfr.fr", 587)
            elif ISP == 'wanadoo':
                server = smtplib.SMTP("smtp.wanadoo.fr", 587)
            elif ISP == 'yahoo':
                server = smtplib.SMTP("smtp.mail.yahoo.fr", 465)
            server.ehlo()
            server.starttls()
            try:
                server.login(mail_sender, mail_passwd)
            except smtplib.SMTPAuthenticationError:
                Label(fen, text="error 2FA is activated on your account", fg="red").pack()
            except:
                Label(fen, text="error while connecting : {}".format(sys.exc_info()[0]), fg="red").pack()
            BODY = '\r\n'.join(['To: %s' % TO,'From: %s' % mail_sender,'Subject: %s' % SUBJECT,'', TEXT])
            # We get the number for MailMassAttack
            while i <= nbMailAttack:
                try:
                    server.sendmail(mail_sender, [TO], BODY)
                    Label(fen, text="[!] Email sent ! {0}/{1}  TO  : {2}".format(i, nbMailAttack, TO), fg="green").pack()
                except:
                    Label(fen, text="error sending mail : {}".format(sys.exc_info()[0]), fg="red").pack()
                i+=1
            server.quit()
        if ISP == "gmail" and smtp != 'smtp.gmail.com':
            SCOPES = 'https://www.googleapis.com/auth/gmail.compose'
            store = file.Storage('credentials.json')
            creds = store.get()
            if not creds or creds.invalid:
                flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
                creds = tools.run_flow(flow, store)
            service = build('gmail', 'v1', http=creds.authorize(Http()))
            BODY = CreateMessage(mail_sender, TO, SUBJECT, TEXT)
            while i <= nbMailAttack:
                try:
                    SendMessage(service, 'me', BODY)
                    Label(fen, text="[!] Email sent ! {0}/{1}  TO  : {2}".format(i, nbMailAttack, TO), fg="green").pack()
                except:
                    Label(fen, text="error sending mail : {}".format(sys.exc_info()[0]), fg="red").pack()
                i+=1

def callback():
    """
    End programe
    """
    # Confirmation to quit the program
    if askyesno('Quit', 'Are you sure you want to leave ?'):
        # If the user clicks "yes"
        showwarning(
            'GOODBYE', 'Too bad...\nSee you soon\n\n@avimimoun\nhttps://www.github.com/av1m')
        fen.quit()
    else:
        # If the user clicks "no"
        showinfo('YES', 'Stay with us!')
        #showerror("Titre 4", "Aha")

def a_help_file():
    """
    This function opens a new window providing basic help on the application
    """
    tk_help_file = Tk()
    tk_help_file.title("Help massmail")
    tk_help_file.resizable(False, False)
    lb = LabelFrame(tk_help_file, text="Basic help", padx=20, pady=20)
    lb.pack(fill="both", expand="yes")
    Label(lb, fg='red', font=("Calibri 10 underline"),text='\nmassmail is under the ownership of @ av1m.\nFor more information click ').pack()
    help_link = Label(lb, text="here", fg="blue", cursor="hand2", font=("Calibri 9 underline"))
    help_link.pack()
	# If users click on "Click here"
    help_link.bind("<Button-1>", lambda event: webbrowser.open_new(r"https://github.com/av1m/massmail/blob/master/README.md"))
    # End
    help_quit = Button(tk_help_file, text='Quit', fg='red', command=lambda:tk_help_file.destroy())
    help_quit.pack()
    tk_help_file.mainloop()

def a_help_smtp():
    """
    This function opens a new window providing help on sender's emails
    """
    tk_help_smtp = Tk()
    tk_help_smtp.title("Help massmail")
    tk_help_smtp.resizable(False, False)
    lb = LabelFrame(tk_help_smtp, text="Information about the sender's email", padx=20, pady=20)
    lb.pack(fill="both", expand="yes")
    Label(lb, fg='black', text='\nThe sending of mails is done via the SMTP protocol and in API for the Gmail addresses\n(if the file clients_secrets.json is provided, otherwise it is SMTP).\n').pack()
    Label(lb, fg='red', font="Calibri 10 underline", text='SMTP protocol included in the app').pack()
    Label(lb, fg='black', text='Gmail, Yahoo, Hotmail, Outlook, Live, Free, Sfr, Wanadoo, orange\nFor more SMTP, please contact me : ').pack()
    help_link = Label(lb, text="here", fg="blue", cursor="hand2", font=("Calibri 9 underline"))
    help_link.pack()
    help_link.bind("<Button-1>", lambda event: webbrowser.open_new(r"https://github.com/av1m/"))
    help_quit = Button(tk_help_smtp, text='Quit', fg='red', command=lambda:tk_help_smtp.destroy())
    help_quit.pack()
    tk_help_smtp.mainloop()

if __name__ == '__main__':
    # Calling security fen 
    security = fenCode()
    if security.verification != True:
        del security
        # if the user closes the security window, the program stops
        sys.exit(0)

    # Graphic window creation
    from tkinter import *
    from tkinter.messagebox import *  # Import module for message management
    fen = Tk()
    # Window size adjustment
    fen.geometry("555x555+300+0")
    fen.title("massmail")
    # Blocking the window
    fen.resizable(width=True, height=True)

    # Display of the welcome message in the program
    bienvenue = Label(fen, text="Welcome, send an mail", fg="red")
    bienvenue.pack()
    bienvenue.config(font=("Courier 25 bold"))

    # Label and input display for sender
    Label(fen, fg="black", text="Sender's email address").pack()
    Label(fen, fg="gray", font="Calibri 8", text="For more information : Help >> Sender's mail").pack()
    unFROM = Entry(fen, width=40)
    unFROM.pack()

    # Display of the label and the entry for the sender password
    Label(fen, fg="black", text="Sender's password").pack()
    unFROMmdp = Entry(fen, width=40, show="*")
    unFROMmdp.pack()

    # Label and input display for the recipient
    Label(fen, fg="black", text="Recipient's email address (can put ; for send many) ").pack()
    unTO = Text(fen, width=40, height=3)
    unTO.pack()

    # Display of the label and the entry for the mail subject
    Label(fen, fg="black", text="Object").pack()
    unSUBJECT = Entry(fen, width=40)
    unSUBJECT.pack()

    # Label and input display for the mail body
    Label(fen, fg="black", text="Enter your text").pack()
    unTEXT = Text(fen, height=5, width=300)
    unTEXT.pack()

    # Label and input display for the number of sendings
    Label(fen, fg="black", text="Number of sending ? (email attack)").pack()
    nbMailAttack = IntVar()
    nbMailAttack.set(1)
    unMailAttack = Entry(fen, text=nbMailAttack)
    unMailAttack.pack()

    buttonSendMail = Button(fen, text="SEND", fg="green", command=sendmail, width=10)
    buttonSendMail.pack()

    # Redirect to github using the webbrowser module
    githubLink = Label(fen, text="\n\nProject on Github", fg="blue", cursor="hand2", font=("Calibri 9 underline"))
    githubLink.pack()
        # If the user clicks on the labels
    githubLink.bind("<Button-1>", lambda event: webbrowser.open_new(r"https://www.github.com/av1m/massmail"))

    # Creating Menu
    menubar = Menu(fen)
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Quit", command=mainloop)
    menubar.add_cascade(label="File", menu=menu1)
    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label="File help", command=a_help_file)
    menu2.add_command(label="Sender's email", command=a_help_smtp)
    menu2.add_command(label="Change Log's", command=lambda: webbrowser.open_new(r"https://github.com/av1m/massmail/blob/master/changelog.md"))
    menu2.add_command(label="about massmail...", command=lambda: webbrowser.open_new(r"https://www.github.com/av1m/massmail"))
    menubar.add_cascade(label="Help", menu=menu2)
    fen.config(menu=menubar)

    # Button end Program
    Label(fen, text="\n").pack()
    bouton_quitter = Button(fen, text="Quit", command=callback, fg="red", font=("Calibri 12 bold"))
    bouton_quitter.pack(side=BOTTOM, anchor=SE)

    fen.mainloop()