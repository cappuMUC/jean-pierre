#! /usr/bin/env python3
# coding: utf-8
"""
Jean-Pierre [Prototype]
A Raspberry Pi robot helping people to build groceries list.
Matteo Cargnelutti - github.com/matteocargnelutti

jeanpierre.py - Main script
"""
#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
import logging
import argparse
import os

import controllers
from controllers.web import webapp # Gunicorn hook for Flask

#-----------------------------------------------------------------------------
# Main : routing
#-----------------------------------------------------------------------------
def main():
    """
    Routing from the console line arguments to the appropriate controller.
    Options :
    --do config/scanner/web
    """
    # Get arguments
    arguments = argparse.ArgumentParser()
    arguments.add_argument("-d", "--do",
                           help="Jean-Pierre's process to launch: config/scanner/web/key")
    arguments.add_argument("-l", "--lang",
                           help="Language for the web app and config assistant. Default: en")
    arguments = arguments.parse_args()

    # If no arguments
    if not arguments or not hasattr(arguments, 'do') or not arguments.do:
        message = "Jean-Pierre understands:\n"
        message += "--do config : launch the configuration assistant"
        message += "--do scanner : launch the scanner process"
        message += "--do web : launch the web server"
        message += "--do key : generates a secret key for Flask"
        print(message)
        return

    # If invalid arguments
    if arguments.do not in ['config', 'scanner', 'web', 'key']:
        message = 'Invalid option --do "{}"'.format(arguments.do)
        print(message)
        return

    # Check that the program has been configured
    if arguments.do != 'config' and not os.path.isfile('database.db'):
        message = "Jean-Pierre is not configured. Please launch jeanpierre.py --do config"
        print(message)
        return

    # Config
    if arguments.do == 'config':
        controllers.Config.execute(str(arguments.lang))
    # Scanner
    elif arguments.do == 'scanner':
        controllers.Scanner.execute()
    # Web debug
    elif arguments.do == 'web':
        webapp.run(debug=True, host='0.0.0.0')
        print("Flask launched in DEBUG mode.")
        print("For production, please use : gunicorn --bind 0.0.0.0 jeanpierre:webapp")
    # Flask secret key
    elif arguments.key == 'key':
        newkey = "".join([random.choice(string.printable) for _ in range(24)])
        keyfile = open('flask_secret_key', 'w')
        keyfile.write(newkey)
        keyfile.close()
        print("New secret key generated for Flask.")

# Execution
if __name__ == "__main__":
    try:
        main()
    except Warning as trace:
        logging.warning(trace, exc_info=True)
    except Exception as trace:
        logging.error(trace, exc_info=True)
