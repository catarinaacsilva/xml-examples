for $c in collection('CursosUA')//curso
where $c[nome = 'curso novo']
return 
  replace node $c/grau/text() with 'Mestrado integrado'

