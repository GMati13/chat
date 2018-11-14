command_sign = ':'

def has_true(line):
    return len(line) > 0 and line[0] == command_sign

def pretty(line):
    cmd = line.strip().split()
    if len(line) == 0:
        cmd = ['','']
    return {
            'head': cmd[0],
            'args': cmd[1:],
            'tail': ' '.join(cmd[1:])
            }

exit    = ('q', 'quit', 'exit')
connect = ('c', 'conn', 'connect')
