class Sprendimas:
  def maksimalus_kiekis( self, N: int ) :
    ats = []
    i = 1
    while i+1 <= N-i:
      ats.append( i )
      N -= i
      i += 1
    if 0 < N:
      ats.append( N )
    return ats

sprendimas = Sprendimas()
N = int( input() )
ats = sprendimas.maksimalus_kiekis( N )
print( len( ats ))
for x in ats:
 print( x, end=" " )
