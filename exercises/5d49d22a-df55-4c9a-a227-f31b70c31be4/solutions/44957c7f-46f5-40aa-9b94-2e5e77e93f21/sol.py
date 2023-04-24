def kuro_uzpildymas(atstumas,kilometrai,n,benzino_koloneles):
  
    kiek_pildyta, dabart_pildymas, riba = 0,0,kilometrai
    while riba < atstumas:  
        # Kol su dabartiniais degalais neįmanoma pasiekti kelionės tikslo
        if dabart_pildymas >= n or benzino_koloneles[dabart_pildymas] > riba:
            # Negalima pasiekti nei kelionės tikslo, nei artimiausios degalinės
            return -1
          
        # Ieškoti tolimiausios degalinės, kurią galime pasiekti
        while dabart_pildymas < n-1 and benzino_koloneles[dabart_pildymas+1] <= riba:
            dabart_pildymas += 1
            
        kiek_pildyta += 1  # Sustoti įsipilti kuro
        riba = benzino_koloneles[dabart_pildymas] + kilometrai  # Pripildyti baką 
        dabart_pildymas += 1
        
    return kiek_pildyta

print(kuro_uzpildymas(10, 3, 4, [1,2,5,9]))

