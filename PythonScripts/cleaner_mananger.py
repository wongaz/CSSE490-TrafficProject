import argparse
import cleaner
parser = argparse.ArgumentParser()
parser.add_argument('--f')
parser.add_argument('--d')
args = parser.parse_args()
if args.d!=None:
    cleaner.clean(args.d)
else:
    import os
    x = [os.path.join(r, file) for r, d, f in os.walk(args.f) for file in f]
    for k in x:
        cleaner.clean(k)