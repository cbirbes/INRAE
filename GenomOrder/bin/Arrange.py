#!/usr/bin/env python3

import os
import re
from collections import OrderedDict
from Bio import SeqIO
from paf import Paf
from numpy import mean
import argparse
from sort_paf import Sorter

parser = argparse.ArgumentParser(description='Arrange assembly according to reference')
parser.add_argument('--paf', help = "input paf file", required=True)
parser.add_argument('--queryIdx', help = "input query index", required=True)
parser.add_argument('--refIdx', help = "input reference index", required=True)
parser.add_argument('--inputFasta', help = 'input fasta file', required=True)
args = vars(parser.parse_args())
InputPaf = args['paf']
InputQIdx = args['queryIdx']
InputTIdx = args['refIdx']
inputFasta = args['inputFasta']

def uncompress(filename):
        """
        Uncompress a gzipped file

        :param filename: gzipped file
        :type filename: str
        :return: path of the uncompressed file
        :rtype: str
        """
        try:
            uncompressed = filename.rsplit('.', 1)[0]
            parts = uncompressed.rsplit("/", 1)
            file_path = parts[0]
            basename = parts[1]
            n = 2
            while os.path.exists(uncompressed):
                uncompressed = "%s/%d_%s" % (file_path, n, basename)
                n += 1
            with open(filename, "rb") as infile, open(uncompressed, "wb") as outfile:
                outfile.write(gzip.decompress(infile.read()))
            return uncompressed
        except Exception as e:
            print(traceback.format_exc())
            return None

def read_index(index_file):
        """
        Load index of query or target

        :param index_file: index file path
        :type index_file: str
        :return:
            * [0] index (size of each chromosome) {dict}
            * [1] sample name {str}
        :rtype: (dict, str)
        """
        index = OrderedDict()
        with open(index_file, "r") as index_f:
            # Sample name without special chars:
            sample_name = re.sub('[^A-Za-z0-9_\-.]+', '', index_f.readline().strip("\n").replace(" ", "_"))
            for line in index_f:
                if line != "":
                    parts = line.strip("\n").split("\t")
                    name = parts[0]
                    lenght = int(parts[1])
                    to_reverse = parts[2] == "1" if len(parts) >= 3 else False
                    index[name] = {
                        "length": lenght,
                        "to_reverse": to_reverse
                    }
        return index, sample_name

def build_query_as_reference():
    """
    Build fasta of query with contigs order like reference

    :param id_res: job id
    :type id_res: str
    """
    sorter = Sorter(InputPaf, "map.paf")
    sorter.sort()
    paf_file = os.path.join("map.paf")
    idx1 = os.path.join(InputQIdx)
    idx2 = os.path.join(InputTIdx)
    paf = Paf(paf_file, idx1, idx2, inputFasta)
    return paf.build_query_chr_as_reference()

build_query_as_reference()
