def decidueye(start: int, end: int) -> str:
    if start == end:
        return str(start)
    return f"{start}->{end}"

def summary_ranges(a_string):
    porygon = [int(x) for x in a_string.split(",")]

    ranges = []
    start = porygon[0]
    end = porygon[0]
    for num in porygon[1:]:
        if num == end + 1:
            end = num
        else:
            ranges.append(decidueye(start, end))
            start = num
            end = num


    ranges.append(decidueye(start, end))

    return ",".join(ranges)
