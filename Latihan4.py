# LATIHAN 10.4
nama_file = input("Masukkan nama file: ")

try:
    file = open(nama_file, 'r')
except:
    print("File tidak dapat dibuka:", nama_file)
    exit()

pesan_per_domain = dict()

for line in file:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        domain = email.split('@')[1]
        pesan_per_domain[domain] = pesan_per_domain.get(domain, 0) + 1

file.close()

print(pesan_per_domain)

