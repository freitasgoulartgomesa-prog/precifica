# Rascunho (ciclo 39, 28/11): página /brownie/. Publicar em 30/11 com /pudim/: colar o dict na lista do build.py,
# opção no menu (<option value="brownie/">Brownie</option>), link na trufa/pudim; sitemap sai do build.
# Conta conferida com python no ciclo 39: material (48+16+3)/20 = 3,35; tempo 30/20 = 1,50; custo 4,85;
# preço 4,85/0,75 = 6,4667 (R$ 6,47); caixa de 4 = 25,88; mínimo 4,85/0,95 = 5,1053 (R$ 5,11).
PAGINA = dict(slug="brownie",title="Quanto cobrar por brownie: calculadora grátis",
  desc="Vai vender brownie para o Natal, em festa ou por encomenda? Calcule o preço de cada pedaço: chocolate, manteiga, embalagem, gás, seu tempo e taxas.",
  h1="Quanto cobrar por brownie?",
  sub="Brownie vende bem como lembrancinha de Natal e o ano todo. Preencha os custos de <b>uma assadeira</b> e quantos pedaços ela rende. No exemplo, cada pedaço sai por <b>R$ 6,47</b> (caixa com 4 por R$ 25,88).",
  lab=["Ingredientes da assadeira<small>chocolate, manteiga, açúcar, ovos, farinha e cacau</small>","Embalagens (saquinho ou caixinha) e etiquetas","Gás do forno","Pedaços que a assadeira rende"],
  vals=[48,16,3,20,2,15,5,20],
  art="""<h2>Exemplo resolvido: 1 assadeira de 20 x 30 cm, 20 pedaços</h2>
<p>Os números abaixo são os que já vêm preenchidos na calculadora. São um <b>exemplo</b> com preços de mercado comuns (estimativa nossa): troque pelos valores das suas notas.</p>
<ul>
<li><b>Ingredientes:</b> R$ 48,00 (chocolate meio amargo 400 g R$ 24,00, manteiga 200 g R$ 12,00, 4 ovos R$ 4,00, açúcar R$ 3,00, farinha e cacau R$ 5,00).</li>
<li><b>Rendimento:</b> 20 pedaços de cerca de 6 x 5 cm.</li>
<li><b>Embalagem:</b> 20 saquinhos ou caixinhas com etiqueta a R$ 0,80 = R$ 16,00. <b>Gás:</b> cerca de 35 min de forno, R$ 3,00.</li>
<li><b>Tempo:</b> 2 h de trabalho (derreter, misturar, assar, esfriar, cortar e embalar), a R$ 15 por hora = R$ 30,00.</li>
<li><b>Taxa da maquininha:</b> 5%. <b>Lucro do negócio:</b> 20%.</li>
</ul>
<p><b>A conta por pedaço:</b> material = (48,00 + 16,00 + 3,00) ÷ 20 = R$ 3,35; tempo = 30,00 ÷ 20 = R$ 1,50; custo = R$ 4,85.<br>
Preço = 4,85 ÷ (1 − 0,05 − 0,20) = 4,85 ÷ 0,75 = <b>R$ 6,47 o pedaço</b>.<br>
Abaixo de R$ 5,11 (4,85 ÷ 0,95) você não paga nem o material e as suas horas depois da taxa.</p>
<h2>Caixa de presente</h2>
<p>Uma caixa com 4 pedaços sai por cerca de <b>R$ 25,88</b>. Se a caixa de presente custa mais que os saquinhos, some a diferença no campo de embalagem e troque o rendimento para o número de caixas.</p>
<h2>Erros comuns</h2>
<p><b>Usar o preço do chocolate em promoção como se fosse sempre.</b> Faça a conta com o preço que você paga normalmente; promoção vira lucro extra.</p>
<p><b>Esquecer as beiradas.</b> Se você corta as bordas e não vende, a assadeira rende menos pedaços: ponha no rendimento o que sobra para vender.</p>
<p><b>Cobrar o mesmo por pedaços de tamanhos diferentes.</b> Defina o tamanho (ex.: 6 x 5 cm) e corte sempre igual.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quanto cobrar por um brownie?</b> Faça a conta com os seus custos. No exemplo, R$ 6,47 o pedaço; com chocolate mais barato ou pedaços menores, o preço cai.</p>
<p><b>Brownie dura quanto tempo?</b> Bem embalado e longe do calor, costuma durar alguns dias. Escreva a data de fabricação na etiqueta.</p>
<p><b>Quanto vale a minha hora?</b> Divida quanto quer ganhar no mês pelas horas que trabalha. Ex.: R$ 2.000 ÷ 120 h ≈ R$ 16,67 por hora.</p>
<h2>Outras calculadoras</h2>
<p><a href="/precifica/trufa/">Preço de trufa</a> · <a href="/precifica/pao-de-mel/">Preço de pão de mel</a> · <a href="/precifica/pudim/">Preço de pudim</a></p>""")
