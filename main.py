
def not_implemented(cmd):
    print(cmd.upper()+' no implementado')

PROMPT='sql>'

if __name__ == '__main__':
    while True:
        print(PROMPT, end='');
        cmd = input();

        if cmd.strip() == '':
            continue
        elif 'select' == cmd.lower():
            not_implemented(cmd)
        elif 'insert' == cmd.lower():
            not_implemented(cmd)
        elif '.exit' == cmd:
            print('Terminado')
            break
        else:
            print("Comando no reconocido: '{cmd}'".format(cmd=cmd))
