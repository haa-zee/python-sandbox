#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mailbox
import sys,os


def processMailbox(mailboxPath):
    mb=mailbox.mbox(mailboxPath)
    for nextMessage in mb:
#        print nextMessage.get_params()
        print nextMessage.get_all('Return-Path')
        print nextMessage.get_all('Received')[-1]
        print nextMessage.get_all('From')
        print nextMessage.get_all('Reply-to')
        print nextMessage.get_all('List-Unsubscribe')
        
        print "----------------------------\n"
        
#    print x.get_all('Return-path')
#    print x.as_string()
#    for mailContent in mb:
#        print mailContent.is_multipart()
#        print mailContent.__class__.__name__
# mboxMessage
#        print mailContent.get_flags()

def main():
    if len(sys.argv)<2:
        mailboxPath='/var/mail/'+os.getlogin()
    else:
        mailboxPath=sys.argv[1]

    try:
        processMailbox(mailboxPath)
    except Exception,arg:
        print "An error occured."
        print arg
        sys.exit(-1)



if __name__ == "__main__":
    main()



