'''
Fuzz testing is commonly used in software quality assurance
to identify security vulnerabilities, stability issues, or 
other unexpected behaviors in software applications.
'''

from parser import checkIfWeirdYAML, checkIfValidHelm, update_json_paths, getSingleDict4MultiDocs
from graphtaint import getValidTaints

def fuzzValues():
    inputs = [
        "invalidString",
        True,
        2024
    ]
    
    for input in inputs:
        try:
            result = checkIfWeirdYAML(input)
        except Exception as e:
            print(f"Exception during testing for checkIfWeirdYAML: {e}")

    print("\n")

    for input in inputs:
        try:
            result = checkIfValidHelm(input)
        except Exception as e:
            print(f"Exception during testing for checkIfValidHelm: {e}")

    print("\n")

    for input in inputs:
        try:
            result = update_json_paths(input)
        except Exception as e:
            print(f"Exception during testing for update_json_paths : {e}")

    print("\n")

    for input in inputs:
        try:
            result = getSingleDict4MultiDocs(input)
        except Exception as e:
            print(f"Exception during testing for getSingleDict4MultiDocs: {e}")

    print("\n")

    for input in inputs:
        try:
            result = getValidTaints(input)
        except Exception as e:
            print(f"Exception during testing for getValidTaints: {e}")

if __name__ == "__main__":
    fuzzValues()