import numpy as np
            
#mengkodekan asam amino dari coding region
def asam_amino(coding_region):
    untai_asam_amino=[]
    for k in range(0, len(coding_region), 3):
        match coding_region[k:k+3]: 
            case 'AUG':
                untai_asam_amino.append('M') #Methionine
            case 'AUU' | 'AUC' | 'AUA':
                untai_asam_amino.append('I') #Isoleucine
            case 'ACU' | 'ACC' | 'ACA' | 'ACG':
                untai_asam_amino.append('T') #Threonine
            case 'AAU' | 'AAC':
                untai_asam_amino.append('N') #Asparagine
            case 'AAA' | 'AAG':
                untai_asam_amino.append('K') #Lysine
            case 'AGU' | 'AGC' | 'UCU' | 'UCC' | 'UCA' | 'UCG':
                untai_asam_amino.append('S') #Serine
            case 'AGA' | 'AGG' | 'CGU' | 'CGC' | 'CGA' | 'CGG':
                untai_asam_amino.append('R') #Arginine
            case 'GUU' | 'GUC' | 'GUA' | 'GUG':
                untai_asam_amino.append('V') #Valine
            case 'GCU' | 'GCC' | 'GCA' | 'GCG':
                untai_asam_amino.append('A') #Alanine
            case 'GAU' | 'GAC' | 'GAA' | 'GAG':
                untai_asam_amino.append('D') #Aspartic Acid
            case 'GGU' | 'GGC' | 'GGA' | 'GGG':
                untai_asam_amino.append('G') #Glycine
            case 'CUU' | 'CUC' | 'CUA' | 'CUG' | 'UUA' | 'UUG':
                untai_asam_amino.append('L') #Leucine
            case 'CCU' | 'CCC' | 'CCA' | 'CCG':
                untai_asam_amino.append('P') #Proline
            case 'CAU' | 'CAC':
                untai_asam_amino.append('H') #Histidine
            case 'CAA' | 'CAG':
                untai_asam_amino.append('Q') #Glutamine
            case 'UUU' | 'UUC':
                untai_asam_amino.append('F') #Phenylalanin
            case 'UAU' | 'UAC':
                untai_asam_amino.append('Y') #Tyrosine
            case 'UGU' | 'UGC':
                untai_asam_amino.append('C') #Cysteine
            case 'UGG':
                untai_asam_amino.append('W') #Tryptophan
            case 'UAA' | 'UAG' | 'UGA':
                untai_asam_amino.append('-') #stop codon
    return ''.join(untai_asam_amino)

#menentukan coding region
def five_utr(sekuen):
    #menemukan kodon start AUG setelah 5'UTR
    for i in range(len(sekuen)-2):
        if sekuen[i:i+3] == 'AUG':
            five_utr_region = sekuen[:i]
            coding_region = sekuen[i:]
            break
        else:
            i += 1
    #menemukan kodon stop UAA, UAG, UGA sebelum 3'UTR
    stop_codon = ['UAA', 'UAG', 'UGA']
    for j in range(len(coding_region)-2):
        if coding_region[j:j+3] in stop_codon:
            three_utr_region = coding_region[j-3:]
            coding_region = coding_region[0:j+3]
            break
        else:
            i += 1
    return five_utr_region, asam_amino(coding_region), three_utr_region

#transkripsi dari untai DNA ke mRNA
def transkripsi(DNA):
    sekuen = ""
    for l in DNA:
        if l == 'T':
            sekuen += 'U'
        else:
            sekuen += l
    return five_utr(sekuen)
