def valid_segment(seg):
    if len(seg) == 0 or len(seg) > 3:
        return False
    if seg[0] == '0' and len(seg) > 1:
        return False
    if int(seg) > 255:
        return False
    return True


def restore_ip_address(s):
    n = len(s)
    hasil = []

    if n < 4 or n > 12:
        return hasil

    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                if i + j + k >= n:
                    continue
                l = n - (i + j + k)
                if l < 1 or l > 3:
                    continue

                seg1 = s[0:i]
                seg2 = s[i:i+j]
                seg3 = s[i+j:i+j+k]
                seg4 = s[i+j+k:]

                if (valid_segment(seg1) and valid_segment(seg2) and
                    valid_segment(seg3) and valid_segment(seg4)):
                    hasil.append(seg1 + "." + seg2 + "." + seg3 + "." + seg4)

    return hasil


s = input("s = ").strip()
ips = restore_ip_address(s)
print(ips)
