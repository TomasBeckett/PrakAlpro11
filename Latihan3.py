# LATIHAN 10.3
nama_file = input("Masukkan nama file: ")

try:
    file = open(nama_file, 'r')
except:
    print("File tidak dapat dibuka:", nama_file)
    exit()

pesan_masuk = dict()

for line in file:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        pesan_masuk[email] = pesan_masuk.get(email, 0) + 1

file.close()

print(pesan_masuk)

