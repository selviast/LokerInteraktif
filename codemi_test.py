class LokerInteraktif(object):

    def __init__(self):
        self.jumlah_loker = 0
        self.isi_loker = [""]

    def init(self, jumlah_loker):
        try:
            self.jumlah_loker = jumlah_loker
            for i in range (1, int(self.jumlah_loker)+1):
                self.isi_loker.append("KOSONG KOSONG")
            # print (self.isi_loker)
            print("Berhasil membuat loker dengan jumlah", jumlah_loker)
        except ValueError:
            print("\nError: Perintah tidak dikenali")

    def status(self):

        isi_loker = self.isi_loker
        print("No. Loker    Tipe Identitas         No. Identitas")
        for i in range (1, int(self.jumlah_loker)+1 ):
            print(i,"          ",isi_loker[i].split()[0].upper(),"                  ",isi_loker[i].split()[1].upper())


    def input(self,input_isi):
        try:
            if len(input_isi.split()) == 2:
                isi_loker = self.isi_loker
                #validasi loker penuh belum
                input_isi = input_isi.upper()
                isi_loker[isi_loker.index("KOSONG KOSONG")]= input_isi

                print("Kartu identitas disimpan di loker nomor",isi_loker.index(input_isi))
            else:
                print("Perintah salah")
        except ValueError:
            print("\nError: Perintah tidak dikenali")

    def leave(self, no_loker):
        try:
            isi_loker = self.isi_loker
            # isi_loker.pop(int(no_loker))
            isi_loker[int(no_loker)] = "KOSONG KOSONG"
            print("Loker nomor",no_loker,"berhasil dikosongkan")
            # print(self.isi_loker)
        except IndexError:
            print("\nError: Tidak ada nomor loker tersebut")

    def find(self, no_id):
        isi_loker = self.isi_loker
        for i in isi_loker:
            if no_id in i:
                index_loker = isi_loker.index(i)
                print("Kartu identitas tersebut berada di loker nomor",index_loker)

    def search(self, tipe_id):
        tipe_id = tipe_id.upper()
        try:
            isi_loker = self.isi_loker
            for i in isi_loker:
                if tipe_id in i:
                    # print(i.split(tipe_id)[1])
                    print(i)
            else:
                print("Jenis Kartu identitas tidak ditemukan.")

        except ValueError:
            print("\nError: Perintah tidak dikenali")

obj = LokerInteraktif()

def Interaktif():

    perintah = str(input('')).lower()
    if perintah.split()[0] == "init":
        obj.init(perintah.split()[1])
            # print("tahap init paling awal")

        while True:
            perintah = str(input('')).lower()
            # print("perintah berhasil di input")
            if perintah.split()[0] == "init":
                print("Perintah init sudah dilakukan.")
                continue

            elif perintah.split()[0]== "input" :
                obj.input(str(perintah.split("input")[1]))
            elif perintah == "status":
                obj.status()
            elif perintah.split()[0] == "leave":
                obj.leave(perintah.split("leave")[1])
            elif perintah.split()[0] == "find":
                obj.find(perintah.split("find")[1])
            elif perintah.split()[0] == "search":
                obj.search(perintah.split("search")[1])
            elif perintah == "exit":
                quit()
            else:
                print("Perintah tidak dikenali.")
    elif perintah == "exit":
        quit()


    elif perintah.split()[0] not in ["input", "leave", "find", "search", "status"]:
        print("Perintah tidak dikenali.")
        Interaktif()
    else:
        # print("Lakukan init terlebih dahulu")

        kumpulan_perintah = ["input", "leave", "find", "search", "status"]

        for i in kumpulan_perintah:
            if i == perintah.split()[0].lower():
                print("Silahkan menentukan jumlah loker terlebih dahulu")



        Interaktif()



Interaktif()




