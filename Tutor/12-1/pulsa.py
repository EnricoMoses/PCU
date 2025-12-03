import random
#pulsa awalnya di random
pulsa= random.randint(100_000,200_000)
isLanjut=True
while isLanjut:

    print("Hello! Transaksi apa yang mau dilakukan?")
    print("1. Cek Pulsa")
    print("2. Top Up Pulsa")
    print("3. Beli Paket Data")
    print("0. Keluar")
    pilihan= int(input("Pilihan: "))
    if pilihan == 1:
        print("Pulsa anda sekarang adalah Rp. ", pulsa)

    elif pilihan == 2:
        topUp=int(input("Masukkan nominal Top Up Pulsa: Rp. "))
        total=pulsa+topUp
        print("Transaksi berhasil dilakukan! Top Up Pulsa senilai Rp.",total )
    elif pilihan==3:
        isBenar=True
        while isBenar:
            print("Beli Paket Data:")
            print("1. Super Seru")
            print("2. Surprise Deal")
            print("3. 5G Promo")
            print("0. Back")
            pilihan2=int(input("Pilihan: "))
            isCorrect=True
            while isCorrect:
                if pilihan2 == 1:
                    print("Detail Paket Super Seru:")
                    print("1. 7Gb/7hr/20rb")
                    print("2. 45Gb/28hr/70rb")
                    print("3. 50Gb/28hr/90rb")
                    print("4. 60Gb/28hr/130rb")
                    print("0. Back")
                    pilihan3=int(input("Pilihan: "))
                    if pilihan3 == 1:
                        print("Konfirmasi Pembelian:")
                        print("7Gb/7hr/20rb:")
                        print("1. Beli")
                        print("2. Batal")
                        pilihan4=int(input("Pilihan: "))
                        if pilihan4==1:
                            total2=pulsa-20_000
                            if pulsa<20_000:
                                print("Saldo tidak mencukupi untuk melakukan transaksi. Silahkan isi pulsa terlebih dahulu")
                                break #masih nda tau
                            else:
                                print("Paket berhasil dibeli dengan harga Rp. 20000. Saldo Pulsa tersisa Rp. ", total2)
                        elif pilihan4 == 2:
                            print("Transaksi paket [Super Seru] [7Gb/7hr/20rb] telah dibatalkan”")
                            continue
                    elif pilihan3 == 2:
                        print("Konfirmasi Pembelian:")
                        print("45Gb/28hr/70rb")
                        print("1. Beli")
                        print("2. Batal")
                        pilihan4=int(input("Pilihan: "))
                        if pilihan4==1:
                            total2=pulsa-70_000
                            if pulsa<70_000:
                                print("Saldo tidak mencukupi untuk melakukan transaksi. Silahkan isi pulsa terlebih dahulu")
                                break #masih nda tau
                            else:
                                print("Paket berhasil dibeli dengan harga Rp. 70000. Saldo Pulsa tersisa Rp. ", total2)
                        elif pilihan4 == 2:
                            print("Transaksi paket [Super Seru] [45Gb/28hr/70rb] telah dibatalkan”")
                            continue
                    elif pilihan3 == 3:
                        print("Konfirmasi Pembelian:")
                        print("50Gb/28hr/90rb")
                        print("1. Beli")
                        print("2. Batal")
                        pilihan4=int(input("Pilihan: "))
                        if pilihan4==1:
                            total2=pulsa-90_000
                            if pulsa<90_000:
                                print("Saldo tidak mencukupi untuk melakukan transaksi. Silahkan isi pulsa terlebih dahulu")
                                break #masih nda tau
                            else:
                                print("Paket berhasil dibeli dengan harga Rp. 90000. Saldo Pulsa tersisa Rp. ", total2)
                        elif pilihan4 == 2:
                            print("Transaksi paket [Super Seru] [50Gb/28hr/90rb] telah dibatalkan”")
                            continue
                    elif pilihan3 == 4:
                        print("Konfirmasi Pembelian:")
                        print("60Gb/28hr/130rb")
                        print("1. Beli")
                        print("2. Batal")
                        pilihan4=int(input("Pilihan: "))
                        if pilihan4==1:
                            total2=pulsa-130_000
                            if pulsa<130_000:
                                print("Saldo tidak mencukupi untuk melakukan transaksi. Silahkan isi pulsa terlebih dahulu")
                                break #masih nda tau
                            else:
                                print("Paket berhasil dibeli dengan harga Rp. 130000. Saldo Pulsa tersisa Rp. ", total2)
                        elif pilihan4 == 2:
                            print("Transaksi paket [Super Seru] [60Gb/28hr/130rb] telah dibatalkan”")
                            continue
                    elif pilihan3 == 0:
                            isCorrect=False
                if pilihan2 == 2:
                    print("Detail Paket Suprise Deal:")
                    print("1. 30Gb/30hr/60rb (bonus Youtube Premium 30hr)")
                    print("2. 45Gb/30hr/90rb (bonus BlockBlast No ad 30hr)")
                    print("3. 80Gb/30hr/100rb (bonus WeTV VIP 30hr)")
                    print("4. 180Gb/30hr/200rb (bonus Netflix 30hr)")
                    print("0. Back")
                    pilihan3=int(input("Pilihan: "))
                    if pilihan3 == 1:
                        print("Konfirmasi Pembelian:")
                        print("30Gb/30hr/60rb (bonus Youtube Premium 30hr):")
                        print("1. Beli")
                        print("2. Batal")
                        pilihan4=int(input("Pilihan: "))
                        if pilihan4==1:
                            total2=pulsa-60_000
                            if pulsa<60_000:
                                print("Saldo tidak mencukupi untuk melakukan transaksi. Silahkan isi pulsa terlebih dahulu")
                                break #masih nda tau
                            else:
                                print("Paket berhasil dibeli dengan harga Rp. 60000. Saldo Pulsa tersisa Rp. ", total2)
                        elif pilihan4 == 2:
                            print("Transaksi paket [Suprise Deal] [30Gb/30hr/60rb (bonus Youtube Premium 30hr)] telah dibatalkan”")
                            continue
                    elif pilihan3 == 2:
                        print("Konfirmasi Pembelian:")
                        print("45Gb/30hr/90rb (bonus BlockBlast No ad 30hr)")
                        print("1. Beli")
                        print("2. Batal")
                        pilihan4=int(input("Pilihan: "))
                        if pilihan4==1:
                            total2=pulsa-90_000
                            if pulsa<90_000:
                                print("Saldo tidak mencukupi untuk melakukan transaksi. Silahkan isi pulsa terlebih dahulu")
                                break #masih nda tau
                            else:
                                print("Paket berhasil dibeli dengan harga Rp. 90000. Saldo Pulsa tersisa Rp. ", total2)
                        elif pilihan4 == 2:
                            print("Transaksi paket [Suprise Deal] [45Gb/30hr/90rb (bonus BlockBlast No ad 30hr)] telah dibatalkan”")
                            continue
                    elif pilihan3 == 3:
                        print("Konfirmasi Pembelian:")
                        print("80Gb/30hr/100rb (bonus WeTV VIP 30hr)")
                        print("1. Beli")
                        print("2. Batal")
                        pilihan4=int(input("Pilihan: "))
                        if pilihan4==1:
                            total2=pulsa-100_000
                            if pulsa<100_000:
                                print("Saldo tidak mencukupi untuk melakukan transaksi. Silahkan isi pulsa terlebih dahulu")
                                break #masih nda tau
                            else:
                                print("Paket berhasil dibeli dengan harga Rp. 100000. Saldo Pulsa tersisa Rp. ", total2)
                        elif pilihan4 == 2:
                            print("Transaksi paket [Suprise Deal] [80Gb/30hr/100rb (bonus WeTV VIP 30hr)] telah dibatalkan”")
                            continue
                    elif pilihan3 == 4:
                        print("Konfirmasi Pembelian:")
                        print("180Gb/30hr/200rb (bonus Netflix 30hr)")
                        print("1. Beli")
                        print("2. Batal")
                        pilihan4=int(input("Pilihan: "))
                        if pilihan4==1:
                            total2=pulsa-200_000
                            if pulsa<200_000:
                                print("Saldo tidak mencukupi untuk melakukan transaksi. Silahkan isi pulsa terlebih dahulu")
                                break #masih nda tau
                            else:
                                print("Paket berhasil dibeli dengan harga Rp. 200000. Saldo Pulsa tersisa Rp. ", total2)
                        elif pilihan4 == 2:
                            print("Transaksi paket [Suprise Deal] [180Gb/30hr/200rb (bonus Netflix 30hr)] telah dibatalkan”")
                            continue
                    elif pilihan3 == 0:
                            isCorrect=False
                if pilihan2 == 3:
                    print("Detail Paket 5G Promo:")
                    print("1. 22Gb/28hr/60rb")
                    print("2. 30Gb/28hr/75rb")
                    print("3. 40Gb/28hr/90rb")
                    print("4. 55Gb/28hr/110rb")
                    print("0. Back")
                    pilihan3=int(input("Pilihan: "))
                    if pilihan3 == 1:
                        print("Konfirmasi Pembelian:")
                        print("22Gb/28hr/60rb")
                        print("1. Beli")
                        print("2. Batal")
                        pilihan4=int(input("Pilihan: "))
                        if pilihan4==1:
                            total2=pulsa-60_000
                            if pulsa<60_000:
                                print("Saldo tidak mencukupi untuk melakukan transaksi. Silahkan isi pulsa terlebih dahulu")
                                break #masih nda tau
                            else:
                                print("Paket berhasil dibeli dengan harga Rp. 60000. Saldo Pulsa tersisa Rp. ", total2)
                        elif pilihan4 == 2:
                            print("Transaksi paket [5G Promo] [22Gb/28hr/60rb] telah dibatalkan”")
                            continue
                    elif pilihan3 == 2:
                        print("Konfirmasi Pembelian:")
                        print("30Gb/28hr/75rb")
                        print("1. Beli")
                        print("2. Batal")
                        pilihan4=int(input("Pilihan: "))
                        if pilihan4==1:
                            total2=pulsa-75_000
                            if pulsa<75_000:
                                print("Saldo tidak mencukupi untuk melakukan transaksi. Silahkan isi pulsa terlebih dahulu")
                                break #masih nda tau
                            else:
                                print("Paket berhasil dibeli dengan harga Rp. 75000. Saldo Pulsa tersisa Rp. ", total2)
                        elif pilihan4 == 2:
                            print("Transaksi paket [5G Promo] [30Gb/28hr/75rb] telah dibatalkan”")
                            continue
                    elif pilihan3 == 3:
                        print("Konfirmasi Pembelian:")
                        print("40Gb/28hr/90rb")
                        print("1. Beli")
                        print("2. Batal")
                        pilihan4=int(input("Pilihan: "))
                        if pilihan4==1:
                            total2=pulsa-90_000
                            if pulsa<90_000:
                                print("Saldo tidak mencukupi untuk melakukan transaksi. Silahkan isi pulsa terlebih dahulu")
                                break #masih nda tau
                            else:
                                print("Paket berhasil dibeli dengan harga Rp. 90000. Saldo Pulsa tersisa Rp. ", total2)
                        elif pilihan4 == 2:
                            print("Transaksi paket [5G Promo] [40Gb/28hr/90rb] telah dibatalkan”")
                            continue
                    elif pilihan3 == 4:
                        print("Konfirmasi Pembelian:")
                        print("55Gb/28hr/110rb")
                        print("1. Beli")
                        print("2. Batal")
                        pilihan4=int(input("Pilihan: "))
                        if pilihan4==1:
                            total2=pulsa-110_000
                            if pulsa<110_000:
                                print("Saldo tidak mencukupi untuk melakukan transaksi. Silahkan isi pulsa terlebih dahulu")
                                break #masih nda tau
                            else:
                                print("Paket berhasil dibeli dengan harga Rp. 110000. Saldo Pulsa tersisa Rp. ", total2)
                        elif pilihan4 == 2:
                            print("Transaksi paket [5G Promo] [55Gb/28hr/110rb] telah dibatalkan”")
                            isBenar=False
                    elif pilihan3 == 0:
                            continue

                elif pilihan2==0:
                    print("Masuk")
                    isCorrect=False
                    isBenar=False
    elif pilihan==0:
        isLanjut=False