<root>{
  let $areascientificas := "Ciências Sociais" (: areascientificas em especifico:)
  for $c in collection('CursosUA')//curso
  where $c/areascientificas = $areascientificas
  return
   ($c/nome)
}

</root>