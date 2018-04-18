#contoh peta 
peta =  {'gnpt':set(['cep','kandri','rand']),
         'cep':set(['sampokong','kandri','gnpt']),
         'kandri':set(['gnpt','rand','pongangan','cep']),
         'rand':set(['pongangan','rand','sekaran','kandri']),
         'pongangan':set(['sampokong','kandri','sadeng','rand']),
         'sampokong':set(['greenwood','cep','pongangan']),
         'greenwood':set(['sampokong','sadeng','mrjeng']),
         'mrjeng':set(['greenwood']),
         'sadeng':set(['sekaran','greenwood','pongangan']),
         'sekaran':set(['rand','sadeng']),
       }
   

def dfs(graf, mulai, tujuan):
    stack = [[mulai]]
    visited = set()

    while stack:
        #hitung panjang tumpukan dan masukkan ke variabel panjang_tumpukan
        panjang_tumpukan = len(stack)-1
        
        # masukkan tumpukan palinif state == tujuan:g atas ke variabel jalur
        jalur = stack.pop(panjang_tumpukan)

        # simpan node yang dipilih ke variabel state, misal jalur = C,B maka simpan B ke variabel state
        state = jalur[-1]

        # cek state apakah sama dengan tujuan, jika ya maka return jalur
        if state == tujuan:
            return jalur
        # jika state tidak sama dengan tujuan, maka cek apakah state tidak ada di visited
        elif state not in visited:
            # jika state tidak ada di visited maka cek cabang
            for cabang in graf.get(state, []): #cek semua cabang dari state
                jalur_baru = list(jalur) #masukkan isi dari variabel jalur ke variabel jalur_baru
                jalur_baru.append(cabang) #update/tambah isi jalur_baru dengan cabang
                stack.append(jalur_baru) #update/tambah queue dengan jalur_baru

            # tandai state yang sudah dikunjungi sebagai visited
            visited.add(state)


        #cek isi tumpukan
        isi = len(stack)
        if isi == 0:
            print("Tidak ditemukan")

print(dfs(peta,'gnpt','mrjeng'))
