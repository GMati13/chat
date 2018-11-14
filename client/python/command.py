command_sign = '/'

def has_true(line):
    return len(line) > 0 and line[0] == command_sign

def pretty(line):
    cmd = line[1:].strip().split()
    return {
            'head': cmd[0],
            'args': cmd[1:]
            }
