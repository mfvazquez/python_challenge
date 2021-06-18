import sys
from ipanalyzer import ipanalyzer


if __name__ == "__main__":

    try:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
    except IndexError:
        print("No input or output filename provided")
        sys.exit(1)
        
    ipanalyzer.ip_analysis(input_filename, output_filename)
