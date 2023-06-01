# Definisi kelas Mahasiswa yang memiliki atribut nama, nim, dan jurusan
class Mahasiswa:

# Method konstruktor yang menginisialisasi atribut nama, nim, dan jurusan dari objek mahasiswa
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
# Method ini dipanggil ketika sebuah objek Mahasiswa baru dibuat. Method ini menerima tiga argumen: 
# nama, nim, dan jurusan. Argumen nama adalah nama mahasiswa, argumen nim adalah nomor identitas mahasiswa, 
# dan argumen jurusan adalah jurusan mahasiswa. Method ini menyimpan nilai-nilai tersebut dalam atribut nama, 
# nim, dan jurusan dari objek Mahasiswa

# Method yang menampilkan informasi nama, nim, dan nama jurusan dari objek mahasiswa
    def tampilkan_info(self):
        print("Nama: ", self.nama)
        print("NIM: ", self.nim)
        print("Jurusan: ", self.jurusan.nama_jurusan)
# Method ini menampilkan informasi nama, nim, dan jurusan dari objek Mahasiswa. Hal ini dilakukan dengan 
# mencetak nilai-nilai atribut nama, nim, dan jurusan

# Definisi kelas Jurusan yang memiliki atribut nama_jurusan dan daftar_mahasiswa
class Jurusan:

# Method konstruktor yang menginisialisasi atribut nama_jurusan dan daftar_mahasiswa dari objek jurusan
    def __init__(self, nama_jurusan):
        self.nama_jurusan = nama_jurusan
        self.daftar_mahasiswa = []
# Method ini menampilkan informasi nama, nim, dan jurusan (major) dari objek Mahasiswa. Hal ini dilakukan
# dengan mencetak nilai-nilai atribut nama, nim, dan jurusan

# Method yang menambahkan objek mahasiswa ke dalam atribut daftar_mahasiswa dari objek jurusan
    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)
# Method ini menambahkan objek Mahasiswa ke dalam atribut daftar_mahasiswa dari objek Jurusan. Method ini
# menerima satu argumen: mahasiswa. Argumen mahasiswa adalah objek Mahasiswa yang akan ditambahkan. 
# Method ini menambahkan objek mahasiswa ke dalam atribut daftar_mahasiswa dari objek Jurusan

# Method yang menampilkan daftar nama mahasiswa yang terdaftar di objek jurusan
    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa", self.nama_jurusan)
        for mahasiswa in self.daftar_mahasiswa:
            print("- ", mahasiswa.nama)
# Method ini menampilkan daftar nama mahasiswa yang terdaftar di objek Jurusan. Hal ini dilakukan
# dengan melakukan perulangan melalui atribut daftar_mahasiswa dari objek Jurusan dan mencetak
# nama dari setiap objek Mahasiswa

# Definisi kelas Universitas yang memiliki atribut nama_universitas dan daftar_jurusan
class Universitas:

# Method konstruktor yang menginisialisasi atribut nama_universitas dan daftar_jurusan dari objek universitas
    def __init__(self, nama_universitas):
        self.nama_universitas = nama_universitas
        self.daftar_jurusan = []
# Method ini dipanggil ketika sebuah objek Universitas baru dibuat. Method ini menerima satu argumen: 
# university_name. Argumen university_name adalah nama universitas. Method ini menyimpan nilai ini dalam
# atribut university_name dari objek Universitas

# Method yang menambahkan objek jurusan ke dalam atribut daftar_jurusan dari objek universitas
    def tambah_jurusan(self, jurusan):
        self.daftar_jurusan.append(jurusan)
# Method ini menambahkan objek Jurusan ke dalam atribut daftar_jurusan dari objek Universitas 
# Method ini menerima satu argumen: jurusan. Argumen jurusan adalah objek Jurusan yang akan ditambahkan
# Method ini menambahkan objek jurusan ke dalam atribut daftar_jurusan dari objek Universitas

# Method yang menambahkan objek jurusan ke dalam atribut daftar_jurusan dari objek universitas
    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di", self.nama_universitas)
        for jurusan in self.daftar_jurusan:
            print("- ", jurusan.nama_jurusan)
# Method ini menampilkan daftar jurusan di objek Universitas. Hal ini dilakukan dengan melakukan
# perulangan melalui atribut daftar_jurusan dari objek Universitas dan mencetak nama dari setiap 
# objek Jurusan


# 2. Membuat objek Universitas dengan nama "XYZ University"
universitas_xyz = Universitas("XYZ University")

# 3. Membuat objek Jurusan dengan nama "Teknik Informatika" dan menambahkannya ke dalam Universitas XYZ
jurusan_ti = Jurusan("Teknik Informatika")
universitas_xyz.tambah_jurusan(jurusan_ti)

# 4. Membuat objek Mahasiswa dengan nama "Kalian masing" dan NIM "Kalian masing",
#    lalu memasukkannya ke dalam Jurusan Teknik Informatika di Universitas XYZ
mahasiswa_kalian = Mahasiswa("Yebi Depriansyah", "G1A022063", jurusan_ti)
jurusan_ti.tambah_mahasiswa(mahasiswa_kalian)

# 5. Menampilkan daftar jurusan yang ada di Universitas XYZ
universitas_xyz.tampilkan_daftar_jurusan()

# 6. Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ
jurusan_ti.tampilkan_daftar_mahasiswa()
