<root>{
  let $guid := "15" (: curso em especifico:)
  for $c in collection('CursosUA')//curso
  where $c/guid = $guid
  return
    ($c/areascientificas)
}

</root>