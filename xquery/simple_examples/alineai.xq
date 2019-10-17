<root>{
  for $c in  distinct-values(collection('CursosUA')//areascientificas)
   return 
   <elem>
      {$c}
    </elem>
   
}

</root>