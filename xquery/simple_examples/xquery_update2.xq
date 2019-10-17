for $d in collection('CursosUA')//curso
where $d[nome = 'curso novo']
return delete node $d