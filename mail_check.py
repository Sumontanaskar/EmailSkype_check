import imaplib
import email
from playsound import playsound
import time, timeit
import Skype4Py

def play_sound_skype():
    try:
        playsound('alarmclock.mp3')
        playsound('beepclocka.mp3')
    except KeyboardInterrupt:
        print 'bye!'

def play_sound():
    try:
        print 'Sound Start'
        playsound('alarmclock.mp3')
        #playsound('beepclocka.mp3')
        print 'Sound Played'
        print 'Sound End'
    except KeyboardInterrupt:
        print 'bye!'
def func_check():
    skype = Skype4Py.Skype()
    skype.Attach()

    user_status = skype.CurrentUserStatus  # returns a string
    missed_messages = skype.MissedMessages  # object type=message collection
    missed_calls = skype.MissedCalls  # object type=call collection

    print 'user_status:', user_status
    if user_status != 'ONLINE':
        #playsound('beep-01a.mp3')
        pass

    for list in missed_messages:
        print 'missed_messages:', list
        play_sound_skype()
    for list in missed_calls:
        print 'missed_calls:', list
        play_sound_skype()

def mail_ck(uname, pw):
    print "Checking mail"
    mail = imaplib.IMAP4_SSL('secure.emailsrvr.com')
    (retcode, capabilities) = mail.login(uname, pw)
    mail.select("inbox") # connect to inbox.
    n = 0
    (retcode, messages) = mail.search(None, '(UNSEEN)')
    if retcode == 'OK':
        for num in messages[0].split():
            print 'Processing '
            n = n + 1
            typ, data = mail.fetch(num, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    original = email.message_from_string(response_part[1])
                    print original['From']
                    print original['Subject']
                    typ, data = mail.store(num, '+FLAGS', '\\Seen')

    print uname + " has " + str(n) + " no of unread emails."
    return n
if __name__ == '__main__':
    while True:
        func_check()
        buf1 = mail_ck('xx@xx.com','xx')
        buf2 = mail_ck('xx@xx.com','xx')
        time.sleep(10)
        buf = buf1+buf2
        print "buf:", buf
        try:
            while buf:
               start = timeit.timeit()
               play_sound()
               end = timeit.timeit()
               time.sleep(2)
               print end - start
        except KeyboardInterrupt:
            print 'bye!'
        
