#!/usr/bin/env python3

from pargs import parse
import sys


if __name__ == "__main__":
    def main():
        print(sys.argv)
        args, opt = parse(['a|all', 'n', 'l|list|1', 't|target|2',
                           's', 'u|user|1', 'p|pass|1', 'h|ip|1'])

        print(args, opt)

    main()
