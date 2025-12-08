def valid_segment(seg):
    if len(seg) == 0 or len(seg) > 3:
        return False
    if seg[0] == '0' and len(seg) > 1:
        return False
    if int(seg) > 255:
        return False
    return True

def backtrack_ip(s, index, segments, result):
    if len(segments) == 4:
        if index == len(s):
            result.append('.'.join(segments))

        return

    for length in range(1, 4):
        if index + length > len(s):
            break

        seg = s[index:index + length]
        if valid_segment(seg):
            segments.append(seg)
            backtrack_ip(s, index + length, segments, result)
            segments.pop()

def restore_ip_address(s):
    result = []
    backtrack_ip(s, 0, [], result)
    return result

s = input('s = ')
ips = restore_ip_address(s)
print(ips)