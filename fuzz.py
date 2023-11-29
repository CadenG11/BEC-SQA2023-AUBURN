'''
Fuzz testing is commonly used in software quality assurance
to identify security vulnerabilities, stability issues, or 
other unexpected behaviors in software applications.
'''

from parser import checkIfWeirdYAML, checkIfValidHelm, checkIfValidK8SYaml

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
            result = checkIfValidK8SYaml(input)
        except Exception as e:
            print(f"Exception during testing for checkIfValidK8SYaml: {e}")

    print("\n")

if __name__ == "__main__":
    fuzzValues()