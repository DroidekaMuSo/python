def convert(*args) -> None:
    if len(args) == 1:
        output1 = 0
        output2 = 0

        for arg in args:
            output1 = arg / 1000
            output2 = arg / 100

            print(f"Converting mm to m: {output1}")
            print(f"Converting mm to cm: {output2}")
        # convert mm to m
        # convert mm to cm

        return None

    if len(args) == 3:
        output1 = 0
        output2 = 0

        for arg in args:
            output1 = arg * 1000
            output2 = arg * 100

            print(f"Converting mm to m: {output1}")
            print(f"Converting mm to cm: {output2}")

        # convert m to cm
        # convert m to mm
        return None


