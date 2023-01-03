def lokasi() :
    print("="*5,"Selamat datang di XXV","="*5)
    tanggal=int(input("Masukkan tanggal hari ini :"))
    if(tanggal<13) :
        print("== Berikut genre film yang tersedia ==")
        print("1. Horror")
        print("2. Action") 
    film=int(input("Silahkan pilih mau nonton film bergenre apa :"))   
    if(film == 1) :
        print("== Berikut pilihan film yang sedang tayang")
        print("1. The Devil's Light")
        print("2. Pengabdi Setan")
        film=int(input("Silahkan pilih mau nonton film apa :"))
        film=int(input("Mau memesan tiket sebanyak :"))
        print("Total yang harus dibayar adalah",film*25000)
    
lokasi()