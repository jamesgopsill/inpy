from io import TextIOWrapper
from typing import TypedDict


class InpFile(TypedDict):
    nodes: list[int, float, float, float]


def read_inp_file(fpath: str):
    inp_file: InpFile = {"nodes": []}

    with open(fpath, "rt") as f:
        pidx = f.tell()
        while True:
            line = f.readline()
            # has the buffer pointer moved?
            # If not then we have reached EOF.
            if f.tell() == pidx:
                print("EOF")
                break
            # Checking for regions to parse
            if line.startswith("*Node"):
                # Go back a line
                f.seek(pidx)
                inp_file["nodes"] = read_nodes_list(f)
                # Note. fcn f.seek(0) so we need to return
                # to our reading position
                f.seek(pidx)
            # Update our position in the file
            pidx = f.tell()

    return inp_file


def read_nodes_list(f: TextIOWrapper):
    print("Reading Nodes List")
    nodes: list[int, float, float, float] = []
    flag = False
    pidx = f.tell()
    while True:
        line = f.readline()
        if f.tell() == pidx:
            print("EOF")
            break
        if flag:
            if line.startswith("*"):
                break
            elements = line.split(",")
            node = [
                int(elements[0].strip()),
                float(elements[1].strip()),
                float(elements[2].strip()),
                float(elements[3].strip()),
            ]
            nodes.append(node)
        else:
            if line.startswith("*Node"):
                flag = True
        pidx = f.tell()
    # Return the pointer back to the start
    # in case the user wants to read something
    # else
    f.seek(0)
    print(nodes)
    return nodes
