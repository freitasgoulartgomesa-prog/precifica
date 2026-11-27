# Rascunho (ciclo 33, 27/11): página /biscoito-de-natal/. Publicar em 28/11 junto com /pao-de-mel/ e /trufa/: colar o dict no build.py,
# opção no menu (<option value="biscoito-de-natal/">Biscoito de Natal</option>), links no pão de mel/cesta e no sitemap.
# Conta conferida com python no ciclo 33: material (40+6+4)/60 = 0,8333; tempo 60/60 = 1,00; custo 1,8333;
# preço 1,8333/0,75 = 2,4444 (R$ 2,44); saquinho 6 = 14,67; mínimo 1,8333/0,95 = 1,9298 (R$ 1,93).
PAGINA = dict(slug="biscoito-de-natal",title="Preço de biscoito de Natal: calculadora grátis",
  desc="Vai vender biscoito amanteigado ou decorado no Natal? Calcule o preço por unidade e por saquinho: ingredientes, glacê, embalagem, gás e seu tempo.",
  h1="Quanto cobrar por biscoito de Natal?",
  sub="Biscoito amanteigado decorado é presente barato e muito procurado no Natal. Preencha os custos de <b>uma fornada</b> e quantos biscoitos ela rende. No exemplo, cada um sai por <b>R$ 2,44</b> (saquinho com 6 por R$ 14,67).",
  lab=["Ingredientes da fornada<small>farinha, manteiga, açúcar, ovos, essência, glacê e corantes para decorar</small>","Saquinhos, fitas e etiquetas","Gás do forno","Biscoitos que a fornada rende"],
  vals=[40,6,4,60,4,15,5,20],
  art="""<h2>Exemplo resolvido: 60 biscoitos decorados (10 saquinhos de 6)</h2>
<p>Os números abaixo são os que já vêm preenchidos na calculadora. São um <b>exemplo</b> com preços de mercado comuns (estimativa nossa): troque pelos valores das suas notas.</p>
<ul>
<li><b>Ingredientes:</b> R$ 40,00 (massa amanteigada com farinha, manteiga, açúcar, ovos e essência R$ 30,00; glacê real e corantes R$ 10,00).</li>
<li><b>Rendimento:</b> 60 biscoitos médios cortados com forminha.</li>
<li><b>Embalagem:</b> 10 saquinhos com fita e etiqueta a R$ 0,60 = R$ 6,00. <b>Gás:</b> R$ 4,00.</li>
<li><b>Tempo:</b> 4 h de trabalho (massa, descanso, cortar, assar, decorar, secar e embalar), a R$ 15 por hora = R$ 60,00.</li>
<li><b>Taxa da maquininha:</b> 5%. <b>Lucro do negócio:</b> 20%.</li>
</ul>
<p><b>A conta por unidade:</b> material = (40,00 + 6,00 + 4,00) ÷ 60 = R$ 0,83; tempo = 60,00 ÷ 60 = R$ 1,00; custo = R$ 1,83.<br>
Preço = custo ÷ (1 − 0,05 − 0,20) = 1,8333 ÷ 0,75 = <b>R$ 2,44 cada</b>, ou <b>R$ 14,67 o saquinho com 6</b>.<br>
Abaixo de R$ 1,93 cada (custo ÷ 0,95) você não paga nem o material e as suas horas depois da taxa.</p>
<h2>Decorado ou simples?</h2>
<p>Decorar com glacê pode dobrar o tempo. Biscoito simples (sem glacê) leva menos horas: troque o tempo na calculadora e veja o preço cair. Cobre à parte se o cliente pedir nome ou desenho.</p>
<h2>Erros comuns</h2>
<p><b>Não contar o tempo de secar o glacê.</b> O biscoito decorado precisa secar horas antes de embalar; o tempo de decorar é o seu trabalho.</p>
<p><b>Contar os biscoitos que quebraram.</b> Sempre quebram alguns: use no rendimento só os que dá para vender.</p>
<p><b>Usar o preço da margarina numa receita de manteiga.</b> A manteiga é o item que mais pesa: use o preço dela.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quanto cobrar pelo saquinho de biscoito?</b> Faça a conta por unidade e multiplique: no exemplo, o saquinho com 6 dá R$ 14,67.</p>
<p><b>Biscoito amanteigado dura quanto tempo?</b> Bem fechado, costuma durar algumas semanas: dá para produzir antes do Natal. Escreva a validade na etiqueta.</p>
<p><b>Quanto vale a minha hora?</b> Divida quanto quer ganhar no mês pelas horas que trabalha. Ex.: R$ 2.000 ÷ 120 h ≈ R$ 16,67 por hora.</p>
<h2>Outras calculadoras</h2>
<p><a href="/precifica/pao-de-mel/">Preço de pão de mel</a> · <a href="/precifica/trufa/">Preço de trufa</a> · <a href="/precifica/cesta-de-natal/">Preço de cesta de Natal</a></p>""")
