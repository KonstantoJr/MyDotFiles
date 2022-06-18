#! /usr/bin/python3
# Script to sync current computer dirs with a given remote
# The path files need to be at the home directory of the user 
# named .dirsToSync (default) 
import os
import argparse
DEFAULT_PATH = os.path.expanduser("~") + "/.dirsToSync"

def main(args):
    paths = []
    try:
        with open(DEFAULT_PATH , "r") as file:
            for row in file:
                if row == "\n":
                    print("You forgot a white line at the end of the dirs file")
                    print("Which means it will sync the home dirs of the two machines")
                    print("If that what you want to do, write ~/ in the dirs file")
                    return -1
                paths.append(row.strip())
    except FileNotFoundError:
        print("File containing paths to sync not found")
        print(f"Make sure it is located at {DEFAULT_PATH}")
        return -1
    if args.remote == None:
        print("No remote host given")
        print("Run script with -remote REMOTE")
        return 1
    for path in paths:
        print(path)
    print(args.remote)
    for path in paths:
        command = f"rsync -avzP {path} {args.remote}:{path[:-1]}"
        os.system(command)
        print(command)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-remote" , type=str)
    #parser.add_argument("-password", type=str)
    args = parser.parse_args()
    main(args)
