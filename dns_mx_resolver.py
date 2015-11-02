#!/usr/bin/env python
import dns.resolver
import argparse
import os
import csv

#def dns_mx_resolver():
#   pass

def ArgsParser():
    # Initialize argparse    
    cmd_parser = argparse.ArgumentParser(description='Process input [output] file(s).')
    # Define command-line arguments
    cmd_parser.add_argument('input_file', nargs=1, help = 'input csv file')
    cmd_parser.add_argument('output_file', nargs='?', help = 'output file')
    args = cmd_parser.parse_args()
    return args
   

if __name__ == "__main__":
    # Get command-line parameters
    args = ArgsParser()
    # Open input and output files
    try:
        in_file = open(args.input_file[0], 'rb')
    except IOError, e:
        print "Couldn't open input file", os.getcwd()+args.input_file[0], e   
    if args.output_file is None:
        args.output_file = []
        args.output_file.append(args.input_file[0].split('.csv')[0]+'_processed.csv')
    try:
        out_file = open(args.output_file[0], 'w') 
    except IOError, e:
        print "Couldn't open output file.", os.getcwd()+args.output_file[0], e 
    csv_in = csv.reader(in_file, delimiter=';')
    #
    # Get MX records for e-mail domain in list. List in an input file.
    #
    csv.register_dialect('csv_mx_record', delimiter=';',quoting = csv.QUOTE_MINIMAL, quotechar='"')
    for in_row in csv_in:
        out_row = in_row
        email_address = in_row[0].split('@')
        print out_row
        mx = []
        for mx_record in dns.resolver.query(email_address[1].strip(),'MX'):
            mx.append(mx_record.to_text().split(' ')[1][:-1])
        mx_records_row = ','.join(sorted(mx))
        out_row.append(mx_records_row)
        print out_row
        csv_out = csv.writer(out_file, 'csv_mx_record')
        csv_out.writerow(out_row)
    in_file.close()
    out_file.close()
    
