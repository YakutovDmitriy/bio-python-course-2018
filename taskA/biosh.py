import os
import sys

from filesystem import *


def main(args):
    cwd = Directory(os.getcwd())
    while True:
        cmdtokens = input('{path}$ '.format(path=cwd.path)).split()
        if not cmdtokens:
            continue
        cmd = cmdtokens[0]
        cmdargs = cmdtokens[1:]

        if cmd == 'ls':
            print()
            path = cwd.path if not cmdargs else cmdargs[0]
            directory = cwd.getsubdirectory(path)
            for item in directory.items():
                if item.isfile():
                    print('{name}\tFILE\t{size}'.format(name=item.getname(), size=len(item)))
                else:
                    print('{name}\tDIR'.format(name=item.getname()))
            print()
        elif cmd == 'cd':
            pass
        elif cmd == 'cat':
            pass
        elif cmd == 'head':
            pass
        elif cmd == 'tail':
            pass
        elif cmd == 'pwd':
            pass
        elif cmd == 'touch':
            pass
        elif cmd == 'find':
            pass
        elif cmd == 'exit':
            print("Bye bye!")
            break
        else:
            print('Unknown command: {cmd}'.format(cmd=cmd))


if __name__ == '__main__':
    main(sys.argv)
