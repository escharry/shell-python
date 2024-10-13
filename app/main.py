import sys
import os

def main():
    paths = os.getenv("PATH").split(":")
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        args = command.split(" ")
        commands = ['exit', 'echo', 'type', 'pwd', 'cd']
        if args[0] == commands[0]:
            if len(args) > 1 and args[1] == '0':
                break
            else:
                sys.stdout.write(f'{args[0]}: command not found\n')
        elif args[0] == commands[1]:
            sys.stdout.write(" ".join(args[1:]) + '\n')
        elif args[0] == commands[2]:
            cmd_path = None
            for path in paths:
                if os.path.exists(f'{path}/{args[1]}'):
                    cmd_path = f'{path}/{args[1]}'
            if len(args) == 2 and args[1] in commands:
                sys.stdout.write(f'{args[1]} is a shell builtin\n')
            elif len(args) == 2 and args[1] not in commands and not cmd_path:
                sys.stdout.write(f'{args[1]}: not found\n')
            elif len(args) == 1:
                sys.stdout.write(f'{args[0]} error: missing input\n')
            elif len(args) > 2:
                sys.stdout.write(f'{args[0]} error: too many inputs\n')
            elif cmd_path:
                sys.stdout.write(f'{args[1]} is {cmd_path}\n')
        elif args[0] == commands[3]:
            sys.stdout.write(f'{os.getcwd()}\n')
        elif args[0] == commands[4]:
            if len(args) > 1:
                directory = os.getcwd()
                if args[1].startswith('~'):
                    target_directory = os.path.expanduser(args[1])
                else:
                    target_directory = os.path.join(directory, args[1])
                
                try:
                    os.chdir(target_directory)
                except OSError:
                    sys.stdout.write(f'{args[0]}: {args[1]}: No such file or directory\n')
            else:
                sys.stdout.write(f'{args[0]} error: missing input\n')
        else:
            found = False
            for path in paths:
                if os.path.exists(f'{path}/{args[0]}'):
                    os.system(command)
                    found = True
            if not found:
                sys.stdout.write(f'{command}: command not found\n')

if __name__ == "__main__":
    main()
