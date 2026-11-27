# Rascunho (ciclo 32, 27/11): página /pao-de-mel/. Publicar em 28/11: colar o dict na lista de páginas do build.py,
# pôr a opção no menu (<option value="pao-de-mel/">Pão de mel</option>), links no panetone/rabanada e no sitemap.
# Conta conferida com python no ciclo 32: material 78,00/30 = 2,60; tempo 45/30 = 1,50; custo 4,10;
# preço 4,10/0,75 = 5,4667 (R$ 5,47); kit 6 = 32,80; mínimo 4,10/0,95 = 4,3158 (R$ 4,32).
PAGINA = dict(slug="pao-de-mel",title="Quanto cobrar por pão de mel: calculadora grátis",
  desc="Vai vender pão de mel no Natal? Calcule o preço por unidade e por kit: massa, recheio, chocolate, embalagem, gás, seu tempo e taxas. Grátis.",
  h1="Quanto cobrar por pão de mel?",
  sub="Pão de mel é um dos doces que mais vendem no Natal, avulso ou em kit de presente. Preencha os custos de <b>uma fornada</b> e quantos pães ela rende. No exemplo, cada um sai por <b>R$ 5,47</b> (kit com 6 por R$ 32,80).",
  lab=["Ingredientes da fornada<small>farinha, mel, açúcar mascavo, cacau, especiarias, recheio, chocolate para banhar</small>","Saquinhos, fitas e etiquetas","Gás do forno e do banho-maria","Pães de mel que a fornada rende"],
  vals=[62,12,4,30,3,15,5,20],
  art="""<h2>Exemplo resolvido: 30 pães de mel recheados e banhados</h2>
<p>Os números abaixo são os que já vêm preenchidos na calculadora. São um <b>exemplo</b> com preços de mercado comuns (estimativa nossa): troque pelos valores das suas notas.</p>
<ul>
<li><b>Ingredientes:</b> R$ 62,00 (massa com farinha, mel, açúcar mascavo, cacau, especiarias, leite e ovos R$ 25,00; doce de leite para rechear R$ 9,00; 800 g de chocolate fracionado para banhar R$ 28,00).</li>
<li><b>Rendimento:</b> 30 pães de mel médios.</li>
<li><b>Embalagem:</b> 30 saquinhos com fita e etiqueta a R$ 0,40 = R$ 12,00. <b>Gás:</b> R$ 4,00.</li>
<li><b>Tempo:</b> 3 h de trabalho (massa, assar, cortar, rechear, banhar, secar e embalar), a R$ 15 por hora = R$ 45,00.</li>
<li><b>Taxa da maquininha:</b> 5%. <b>Lucro do negócio:</b> 20%.</li>
</ul>
<p><b>A conta por unidade:</b> material = (62,00 + 12,00 + 4,00) ÷ 30 = R$ 2,60; tempo = 45,00 ÷ 30 = R$ 1,50; custo = R$ 4,10.<br>
Preço = 4,10 ÷ (1 − 0,05 − 0,20) = 4,10 ÷ 0,75 = <b>R$ 5,47 cada</b>, ou <b>R$ 32,80 o kit com 6</b>.<br>
Abaixo de R$ 4,32 cada (4,10 ÷ 0,95) você não paga nem o material e as suas horas depois da taxa.</p>
<h2>Kit de presente de Natal</h2>
<p>Caixa, laço e cartão do kit são custo à parte: some no campo de embalagem e divida pelo número de pães do kit. Ex.: caixa para 6 com laço a R$ 4,00 acrescenta R$ 0,67 em cada pão.</p>
<h2>Erros comuns</h2>
<p><b>Usar o preço da barra de chocolate da promoção.</b> O chocolate é o item mais caro: use o preço que você paga de verdade e conte o que sobra na tigela.</p>
<p><b>Não contar o tempo de banhar e secar.</b> Banhar um por um e esperar secar leva horas. É o seu trabalho e entra no preço.</p>
<p><b>Cobrar o mesmo no avulso e no kit.</b> O kit tem caixa e laço: some esse custo ou cobre mais no kit.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quanto cobrar pelo kit de pão de mel?</b> Faça a conta por unidade e multiplique: no exemplo, o kit com 6 dá R$ 32,80, mais a caixa se tiver.</p>
<p><b>Pão de mel dura quanto tempo?</b> Bem banhado e fechado no saquinho, costuma durar alguns dias fora da geladeira; por isso dá para produzir antes do Natal. Escreva a validade na etiqueta.</p>
<p><b>Quanto vale a minha hora?</b> Divida quanto quer ganhar no mês pelas horas que trabalha. Ex.: R$ 2.000 ÷ 120 h ≈ R$ 16,67 por hora.</p>
<h2>Outras calculadoras</h2>
<p><a href="/precifica/panetone/">Preço de panetone caseiro</a> · <a href="/precifica/rabanada/">Preço de rabanada</a> · <a href="/precifica/cesta-de-natal/">Preço de cesta de Natal</a></p>""")
