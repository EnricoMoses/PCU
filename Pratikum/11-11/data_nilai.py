def get_highest(data):
    nilai_tinggi = max(data.values())
    for nama, nilai in data.items():
        if nilai == nilai_tinggi:
            return nama, nilai
    return None


def get_lowest(data):
    nilai_rendah = min(data.values())
    for nama, nilai in data.items():
        if nilai == nilai_rendah:
            return nama, nilai
    return None


def get_average(data):
    return sum(data.values()) / len(data)


n = int(input())
data = {}
for i in range(n):
    input_data = input().split()
    nama = input_data[0]
    nilai = int(input_data[1])
    data[nama] = nilai

nama_tertinggi, nilai_tertinggi = get_highest(data)
nama_terendah, nilai_terendah = get_lowest(data)
rata_rata = get_average(data)
ascending_values = sorted(data.values())

print(f'Nilai tertinggi: {nama_tertinggi} dengan nilai {nilai_tertinggi}')
print(f'Nilai terendah: {nama_terendah} dengan nilai {nilai_terendah}')
print(f'Rata-rata nilai: {rata_rata:.1f}')
print(f'Daftar nilai (ascending): {ascending_values}')
