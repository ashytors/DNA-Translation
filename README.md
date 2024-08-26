Nuhita Aunillah (21/481196/TK/53114)
Tugas Komputasi Genomik - Translasi sekuen RNA menjadi sekuen asam amino

terdapat 2 file, file uji coba yaitu tugas1.ipynb serta dna-translation-clean.py yang berisi fungsi yang sudah clean dan siap diimport. 
Isi dari dna-translation-clean.py:

fungsi asam_amino() adalah fungsi utama untuk melakukan translasi. fungsi ini menggunakan for loop untuk membaca sekuens dalam range 3 karakter dan menggunakan match-case untuk mentranslasikan sekuens.

fungsi five_utr() adalah fungsi tambahan untuk memisahkan 5' untranslated region yang ada sebelum coding region dan 3'untranslated region yang ada setelah coding region. 
fungsi ini menggunakan array splicing untuk memisahkan daerah pada sebelum dan setelah kodon start AUG, dan juga daerah sebelum dan sesudah kodon stop UAA, UAG, dan UGA untuk kemudian daerah di antara kodon stop dan kodon start dijadikan string input untuk fungsi asam_amino().
pada fungsi ini diasumsikan seluruh area coding region adalah exon karena menurut literatur diperlukan machine learning untuk dapat mengenali intron di antara coding region.

//jika ternyata pemahaman saya salah, saya sangat mengharapkan donor ilmu dari pembaca sekalian :D
