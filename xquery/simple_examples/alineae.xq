<root>{
  let $departamentos := "Departamento de Ciências Sociais, Políticas e do Território" (: curso em especifico:)
  for $c in collection('CursosUA')//curso
  where $c/departamentos = $departamentos
  return
   ($c/nome, $c/codigo, $c/grau, $c/local)
}

</root>