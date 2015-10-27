#!/usr/bin/env python
import dns.resolver
import argparse
import os

def dns_mx_resolver():
    pass

def ArgsParser():
    cmd_parser = argparse.ArgumentParser(description='Process input [output] file(s).')
    cmd_parser.add_argument('input_file', nargs=1, help = 'input csv file')
    cmd_parser.add_argument('output_file', nargs='?', help = 'output file')
    args = cmd_parser.parse_args()
    print args.input_file
    print args.output_file
    try:
        in_file = open(args.input_file[0],'r')
    except IOError, e:
        print e
    try:
        out_file = open(args.output_file[0],'w+') 
    except IOError, e:
        print e
    print args
    return args

if __name__ == "__main__":
    print os.getcwd()
    ArgsParser()
