

def get_co_from_file(infile):
    with open(infile) as temp:
        for line in temp:
            line = line.rstrip('\n')
            line_list = line.split('\t')
    pass
