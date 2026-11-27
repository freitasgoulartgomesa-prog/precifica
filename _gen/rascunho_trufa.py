# Rascunho (ciclo 33, 27/11): página /trufa/. Publicar em 28/11 junto com /pao-de-mel/: colar o dict na lista do build.py,
# opção no menu (<option value="trufa/">Trufa</option>), links no pão de mel/panetone e no sitemap.
# Conta conferida com python no ciclo 33: material (75+10+2)/50 = 1,74; tempo 45/50 = 0,90; custo 2,64;
# preço 2,64/0,75 = 3,52; caixa 6 = 21,12; mínimo 2,64/0,95 = 2,7789 (R$ 2,78).
PAGINA = dict(slug="trufa",title="Quanto cobrar por trufa: calculadora grátis",
  desc="Vai vender trufa no Natal? Calcule o preço por unidade e por caixa: chocolate, recheio, papel, forminha, gás, seu tempo e taxas. Grátis.",
  h1="Quanto cobrar por trufa de chocolate?",
  sub="Trufa vende o ano todo e dispara no Natal, avulsa ou em caixa de presente. Preencha os custos de <b>uma leva</b> e quantas trufas ela rende. No exemplo, cada uma sai por <b>R$ 3,52</b> (caixa com 6 por R$ 21,12).",
  lab=["Ingredientes da leva<small>chocolate da casca, chocolate e creme de leite do recheio, essência ou licor</small>","Papel chumbo, forminhas e etiquetas","Gás do banho-maria","Trufas que a leva rende"],
  vals=[75,10,2,50,3,15,5,20],
  art="""<h2>Exemplo resolvido: 50 trufas recheadas</h2>
<p>Os números abaixo são os que já vêm preenchidos na calculadora. São um <b>exemplo</b> com preços de mercado comuns (estimativa nossa): troque pelos valores das suas notas.</p>
<ul>
<li><b>Ingredientes:</b> R$ 75,00 (1 kg de chocolate fracionado para a casca R$ 55,00; recheio de ganache com chocolate e creme de leite R$ 20,00).</li>
<li><b>Rendimento:</b> 50 trufas de uns 20 g.</li>
<li><b>Embalagem:</b> papel chumbo e forminha a R$ 0,20 cada = R$ 10,00. <b>Gás:</b> R$ 2,00.</li>
<li><b>Tempo:</b> 3 h de trabalho (derreter e temperar, fazer a casca, rechear, fechar, embrulhar), a R$ 15 por hora = R$ 45,00.</li>
<li><b>Taxa da maquininha:</b> 5%. <b>Lucro do negócio:</b> 20%.</li>
</ul>
<p><b>A conta por unidade:</b> material = (75,00 + 10,00 + 2,00) ÷ 50 = R$ 1,74; tempo = 45,00 ÷ 50 = R$ 0,90; custo = R$ 2,64.<br>
Preço = 2,64 ÷ (1 − 0,05 − 0,20) = 2,64 ÷ 0,75 = <b>R$ 3,52 cada</b>, ou <b>R$ 21,12 a caixa com 6</b>.<br>
Abaixo de R$ 2,78 cada (2,64 ÷ 0,95) você não paga nem o material e as suas horas depois da taxa.</p>
<h2>Caixa de presente de Natal</h2>
<p>A caixa, o laço e o cartão são custo à parte: some no campo de embalagem e divida pelo número de trufas da caixa. Ex.: caixa para 6 com laço a R$ 3,00 acrescenta R$ 0,50 em cada trufa.</p>
<h2>Erros comuns</h2>
<p><b>Esquecer o chocolate que fica na tigela e nas formas.</b> Sempre sobra chocolate que não vira trufa: use o pacote inteiro na conta.</p>
<p><b>Cobrar o mesmo por recheios diferentes.</b> Recheio com castanha, licor ou frutas custa mais: faça uma conta para cada sabor.</p>
<p><b>Não contar o tempo de embrulhar.</b> Papel chumbo um por um leva tempo. É o seu trabalho e entra no preço.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quanto cobrar pela caixa de trufas?</b> Faça a conta por unidade e multiplique: no exemplo, a caixa com 6 dá R$ 21,12, mais a caixa de presente se tiver.</p>
<p><b>Trufa precisa de geladeira?</b> Depende do recheio. Recheio com creme de leite fresco dura menos: escreva a validade e como guardar na etiqueta.</p>
<p><b>Quanto vale a minha hora?</b> Divida quanto quer ganhar no mês pelas horas que trabalha. Ex.: R$ 2.000 ÷ 120 h ≈ R$ 16,67 por hora.</p>
<h2>Outras calculadoras</h2>
<p><a href="/precifica/pao-de-mel/">Preço de pão de mel</a> · <a href="/precifica/brigadeiro/">Preço de brigadeiro</a> · <a href="/precifica/cesta-de-natal/">Preço de cesta de Natal</a></p>""")
