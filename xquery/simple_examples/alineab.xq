<root>{
  let $guid := "15" (: curso em especifico:)
  for $c in collection('CursosUA')//curso
  where $c/guid = $guid
  return
    ($c/nome, $c/codigo, $c/grau, $c/local)
}

</root>


(: Alternativa :)

(:<root>{
  let $c := collection("CursosUA")//curso[guid=$guid]
  return
 }
</root> :)
