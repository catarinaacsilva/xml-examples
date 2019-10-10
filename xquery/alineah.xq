<root>{
  for $c in  distinct-values(collection('CursosUA')//departamento)
   return 
   <elem>
      {$c}
    </elem>
   
}

</root>