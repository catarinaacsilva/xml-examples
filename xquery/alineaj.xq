<root>{
  for $c in  distinct-values(collection('CursosUA')//local)
   return 
   <elem>
      {$c}
    </elem>
   
}

</root>