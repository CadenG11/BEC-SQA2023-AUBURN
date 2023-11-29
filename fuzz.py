'''
Fuzz testing is commonly used in software quality assurance
to identify security vulnerabilities, stability issues, or 
other unexpected behaviors in software applications.
'''

from parser import checkIfWeirdYAML, checkIfValidK8SYaml, checkIfValidHelm, checkParseError, readYAMLAsStr

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
            result = checkIfValidK8SYaml(input)
        except Exception as e:
            print(f"Exception during testing for checkIfValidK8SYaml: {e}")

    print("\n")

    for input in inputs:
        try:
            result = checkIfValidHelm(input)
        except Exception as e:
            print(f"Exception during testing for checkIfValidHelm: {e}")

    print("\n")

    for input in inputs:
        try:
            result = checkParseError(input)
        except Exception as e:
            print(f"Exception during testing for checkParseError: {e}")

    print("\n")

    for input in inputs:
        try:
            result = readYAMLAsStr(input)

        except Exception as e:
            print(f"Exception during testing for readYAMLAsStr: {e}")

fuzzValues()