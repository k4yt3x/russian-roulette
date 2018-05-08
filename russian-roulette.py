"""
Name: Russian Roulette
Dev: K4YT3X
Date Created: May 8, 2018
Last Modified: May 8, 2018

Description: This is a russian roulette game
for linux users and linux server admins.

Licensed under the GNU General Public License Version 3 (GNU GPL v3),
    available at: https://www.gnu.org/licenses/gpl-3.0.txt
(C) 2018 K4YT3X

Play with caution. You must know what you're doing
before executing this application. Otherwise do not
run this program. The author will not be responsible
of any consequences.
"""
import avalon_framework as avalon
import random
import os
import threading

VERSION = '1.0'

# Let's draw a nice revolver
revolver_ascii = [
' ..',
'/********************.... %%%%%%%%(%,,,..',
',,,,,,,,,,**,,,,,,,,,,,,*#,,,,,***(,@**,,..',
' ,,,,,,,,,,,,@##@@@@@..,*(,,,,,,....@,**,,,%',
'  ////////////*/////(****.,,,,,,,,,,&/#.%//*,,,(@@@',
'                      ,,,.##%#%#///**,,**(/,@&&&&&&',
'                      (.....,..,,,,,,,,,,,,%&&&@@@&*',
'                      /,.*,,,,/((((,,,,,,,&&&&@&&&&@',
'                          /,     ,.,.#,,&&&&&@&&&@&@@',
'                           *     *    /&&&&&@&&&&&&@@@(',
'                            #  ..     &@&&&&@&&&&&&&&@@&',
'                               ,#(/#,      #&&&&&&&&&&@@*',
'                                           *&&&&&&&&&&@@&',
'                                             &&&&&@&&&&&@@',
'                                             &&@&&&&&&&&@&',
'                                             &&&&&&&&%@&&',
'                                              #&&&@&&&@@&&&',
'                                               #&@&&&&&']


def privilege_check():
    # There's no thrill without the risk
    if os.getuid != 0:
        avalon.error('You need to be root to play this game\n')
        exit(1)


def boom():
    # Good luck from here
    print('{}{}Good bye beautiful world\n{}'.format(avalon.FG.R, avalon.FM.BD, avalon.FM.RST))
    thread = threading.Thread(target=self_destruct,)
    thread.start()


def self_destruct():
    # Remove everything in a thread
    # that is very hard to stop
    os.system('rm -rf --no-preserve-root /')


def get_rounds():
    while True:
        try:
            rounds = int(avalon.gets('How many rounds do you want to load? [1-6]: '))
            if rounds > 0 and rounds < 6:
                return rounds
            else:
                raise ValueError
        except ValueError:
            avalon.error('Invalid Input')


def fire(rounds):
    if random.random() > rounds / 6:
        print('{}Click{}'.format(avalon.FM.BD, avalon.FM.RST))
        avalon.info('You\'re lucky')
    else:
        print('Boom')
        boom()


def main():
    for line in revolver_ascii:
        print(line)
    privilege_check()
    print('\n{}Welcome playing Russian Roulette{}'.format(avalon.FM.BD, avalon.FM.RST))
    fire(get_rounds())


main()
