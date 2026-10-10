#include <stdio.h>

int main() {
    char nama[50];

    // Menampilkan teks ke layar
    printf("Halo! Selamat datang di pemrograman C.\n");
    
    // Meminta input dari pengguna
    printf("Masukkan nama Anda: ");
    scanf("%s", nama);

    // Menampilkan kembali hasil input
    printf("Senang berkenalan dengan Anda, %s!\n", nama);

    return 0;
}
