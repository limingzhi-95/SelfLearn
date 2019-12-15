from fysom import Fysom

fsm = Fysom({'initial': 'green',
              'events': [
                  {'name': 'warn', 'src': 'green', 'dst': 'yellow'},
                  {'name': 'panic', 'src': 'yellow', 'dst': 'red'},
                  {'name': 'calm', 'src': 'red', 'dst': 'yellow'},
                  {'name': 'clear', 'src': 'yellow', 'dst': 'green'}]})

if __name__ == '__main__':
    fsm.warn()
    print(fsm.current)
    fsm.calm()
    print(fsm.current)

