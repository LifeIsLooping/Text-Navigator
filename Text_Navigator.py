class TextNavigator:
    def __init__(self, text_list):
        self.text_list = text_list
        self.current_index = 0

    def show_current_text(self):
        print(self.text_list[self.current_index])

    def next_text(self):
        if self.current_index < len(self.text_list) - 1:
            self.current_index += 1
            self.show_current_text()
        else:
            print("Anda sudah mencapai akhir teks.")

    def prev_text(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_current_text()
        else:
            print("Anda sudah berada di awal teks.")

# Contoh penggunaan
my_list = [
    "Kalimat1",
    "Kalimat2",
    "Kalimat3",
    "Kalimat4"
]

navigator = TextNavigator(my_list)

# Tampilkan kalimat saat ini
navigator.show_current_text()

while True:
    print("\nMenu:")
    print("1. Next")
    print("2. Previous")
    print("3. Keluar")

    choice = input("Masukkan pilihan: ")

    if choice == '1':
        navigator.next_text()
    elif choice == '2':
        navigator.prev_text()
    elif choice == '3':
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")