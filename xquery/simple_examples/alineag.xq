<root>{
  let $local := "Campus Universitário de Santiago, Aveiro" (: local em especifico:)
  for $c in collection('CursosUA')//curso
  where $c/local = $local
  return
   ($c/nome)
}

</root>