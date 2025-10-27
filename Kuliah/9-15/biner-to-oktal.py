biner = 0b110110

biner1 = biner & 0b111
biner2 = (biner >> 3) & 0b111
print(biner2, biner1, sep='')

