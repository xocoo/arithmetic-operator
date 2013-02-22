import argparse

def sum(args):
    '''
    Summarize 2 numbers
    '''
    print int(args.f) + int(args.s)

def div(args):
    '''
    Divide input first number to second
    '''
    print float(args.f) / float(args.s)

def mult(args):
    '''
    Multiple input numbers
    '''
    print int(args.f) * int(args.s)

def sub(args):
    '''
    Subtraction input first number to second
    '''
    print int(args.f) - int(args.s)

def prints(args):
    '''
    Print input values
    '''
    print "%s %s" % (args.f, args.s)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    operator =[sum, div, mult, sub, prints]
    for x in operator:
        b = subparsers.add_parser(x.__name__, help=x.__doc__)
        b.set_defaults(func=x)
        b.add_argument('f')
        b.add_argument('s')
    args = parser.parse_args()
    args.func(args)
