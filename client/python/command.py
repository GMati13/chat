command_sign = ':'

def pretty(line):
    cmd = line.strip().split()
    if len(line) == 0:
        cmd = ['','']
    return {
            'head': cmd[0],
            'args': cmd[1:],
            'tail': ' '.join(cmd[1:])
            }

exit         = ('q', 'quit', 'exit')
connect      = ('c', 'conn', 'connect')
send_message = ('s', 'send')
multiline    = ('ml', 'multiline')
set_name     = ('n', 'name')
