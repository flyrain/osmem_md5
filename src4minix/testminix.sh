# Time-stamp: <2013-06-13 17:09:34 cs3612>
#rm outData
#rm outTime
./signa -g ~/qemu/mem/mem-minix3.1.5 0 0xf94e000 > ../md5/Minix-3.1.5
echo './signa -g ~/qemu/mem-minix3.1.5-a'
./signa -g ~/qemu/mem/mem-minix3.1.7 0 0xfee3000 > ../md5/Minix-3.1.7
echo " ./signa -g ~/qemu/mem-minix3.1.7"
./signa -g ~/qemu/mem/mem-minix3.1.8 0 0xf6c8000  > ../md5/Minix-3.1.8
echo " ./signa -g ~/qemu/mem-minix3.1.8"
./signa -g ~/qemu/mem/mem-minix3.2.0 0 0xfee1000  > ../md5/Minix-3.2.0
echo "./signa -g ~/qemu/mem-minix3.2.0"
./signa -g ~/qemu/mem/mem-minix3.2.1 0 0x4d2000 > ../md5/Minix-3.2.1
echo "./signa -g ~/qemu/mem-minix3.2.1"
