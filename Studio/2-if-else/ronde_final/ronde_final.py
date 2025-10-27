x = int(input())

if x <= 0:
    print('Tidak valid!')
else :
    selisih_terbesar = 0
    pemenang_akhir = ''
    ron_total = 0
    neil_total = 0

    for i in range(x):
        ron_skor = int(input())
        neil_skor = int(input())


        ron_total += ron_skor
        neil_total += neil_skor

        if ron_total > neil_total:
            selisih_poin_ronde = ron_total - neil_total
            pemenang_ronde = 'Ron de Fin Al'
        elif neil_total > ron_total:
            selisih_poin_ronde = neil_total - ron_total
            pemenang_ronde = 'Neil Al'
        else :
            selisih_poin_ronde = 0
            pemenang_ronde = 'Seri'
            # pemenang_akhir = pemenang_ronde

        if selisih_poin_ronde > selisih_terbesar:
            selisih_terbesar = selisih_poin_ronde
            pemenang_akhir = pemenang_ronde

    while pemenang_akhir == 'Seri':
        ron_skor_tambahan = int(input())
        neil_skor_tambahan = int(input())

        ron_total += ron_skor_tambahan
        neil_total += neil_skor_tambahan

        if ron_total > neil_total:
            selisih_poin_akhir = ron_total - neil_total
            pemenang_akhir = 'Ron de Fin Al'
            # if selisih_tambahan > selisih_terbesar:
            #     selisih_terbesar = selisih_tambahan
        elif neil_total > ron_total:
            selisih_poin_akhir = neil_total - ron_total
            pemenang_akhir = 'Neil Al'
            # if selisih_tambahan > selisih_terbesar:
            #     selisih_terbesar = selisih_tambahan
            if selisih_poin_akhir > selisih_terbesar:
                selisih_terbesar = selisih_poin_akhir

    if pemenang_akhir == 'Ron de Fin Al':
        print(f'Ron de Fin AI unggul dengan nilai {selisih_terbesar}')
    elif pemenang_akhir == 'Neil Al':
        print(f'Neil AI unggul dengan nilai {selisih_terbesar}')
    else :
        print('Pertandingan seri')
