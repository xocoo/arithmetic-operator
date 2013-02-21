import argparse

def do(args):
    if args.n=='sum': print int(args.f) + int(args.s)
    if args.n=='div': print int(args.f) / int(args.s)
    if args.n=='mult': print int(args.f) * int(args.s)
    if args.n=='sub': print int(args.f) - int(args.s)
    if args.n=='print': print args.f + ' ' + args.s

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    operator =['sum', 'div', 'mult', 'sub', 'print']
    for x in operator:
        b = subparsers.add_parser(x)
        b.set_defaults(func=do)
        b.add_argument('f')
        b.add_argument('s')
        b.add_argument('--n', default=x)
    args = parser.parse_args()
    args.func(args)
