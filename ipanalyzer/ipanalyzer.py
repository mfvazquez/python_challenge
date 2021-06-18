from . import IpFinder, GeoIP, Rdap
import json


def ip_analysis(input_filename, output_filename):
    """ Searchs IPS in the `input_filename` and 
    store Geo IP and RDAP lookups in the `output_filename`. 

    Args:
        input_filename (str): The input filename.
        output_filename (str): The output filename.
    """

    parser = IpFinder()
    pipes = (GeoIP(), Rdap())
    keys = ('GeoIP', 'RDAP')
    ip_processor = Processor(pipes, keys)

    print(f"Reading input file {input_filename}...")
    ips = parser.find(input_filename)
    output = {}

    print("Analyzing IP addresses...")
    for i, ip in enumerate(ips):
        print(f"{(i/len(ips) * 100):.2f} % ", end="\r")
        output[ip] = ip_processor.process(ip)

    print(f"Writing output in file {output_filename}...")
    with open(output_filename, 'w') as fp:
        json.dump(output, fp)


class Processor:

    def __init__(self, processes_obj, keys):
        self.processes = processes_obj
        self.keys = keys

    def process(self, input_data):
        """ Process the input data through the pipeline.

        Args:
            input_data (object): Data required by the `get` methods of the objects.

        Returns:
            [dict]: A dictionary with the keys provided and the output of each
            process as value 
        """

        output = {}
        for i in range(len(self.processes)):
            output[self.keys[i]] = self.processes[i].get(input_data)

        return output
