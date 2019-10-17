
  let $cs := collection('CursosUA')//cursos
  for $c in $cs
  return insert node <curso> <guid>5400</guid>
    <codigo>0300/9002</codigo>
    <nome>curso novo_3</nome>
    <nota/>
    <grau>Licenciatura</grau>
    <ciclo>1</ciclo>
    <departamentos>
      <departamento>Departamento de Ciências Sociais, Políticas e do Território</departamento>
    </departamentos>
    <areascientificas>
      <areacientifica>Ciências Sociais</areacientifica>
    </areascientificas>
    <areasformacao/>
    <regime>Diurno / laboral</regime>
    <local>Campus Universitário de Santiago, Aveiro</local>
    <provas>Uma das seguintes provas:<br/>17 Matemática Aplicada às Ciências Sociais<br/>16 Matemática<br/>18 Português<br/>
      <br/>
      <br/>
      <strong>O cálculo da nota de acesso considera:</strong>
      <ul>
        <li>60% da nota do ensino secundário</li>
        <li>40% da nota da prova de ingresso</li>
      </ul>
    </provas>
    <m23>True</m23>
    <abrecandidaturas>True</abrecandidaturas>
    <ultimaalteracao>03/06/2019 12:34:00</ultimaalteracao> </curso>
 into $c