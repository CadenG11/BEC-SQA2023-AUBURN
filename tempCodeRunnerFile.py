    for input in inputs:
        try:
            result = getValuesRecursively(input)
        except Exception as e:
            print(f"Exception during testing: {e}")