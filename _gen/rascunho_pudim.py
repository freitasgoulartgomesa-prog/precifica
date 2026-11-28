# Rascunho (ciclo 38, 28/11): página /pudim/. Publicar em 30/11: colar o dict na lista do build.py (depois do biscoito),
# opção no menu (<option value="pudim/">Pudim</option>), link no pavê/ceia; sitemap sai do build.
# Conta conferida com python no ciclo 38: material (50+8+6)/2 = 32,00; tempo 30/2 = 15,00; custo 47,00;
# preço 47/0,75 = 62,6667 (R$ 62,67); fatia 62,67/12 = 5,22; mínimo 47/0,95 = 49,4737 (R$ 49,47).
PAGINA = dict(slug="pudim",title="Quanto cobrar por pudim: calculadora grátis",
  desc="Vai vender pudim no Natal ou por encomenda? Calcule o preço do pudim inteiro e da fatia: leite condensado, ovos, embalagem, gás, seu tempo e taxas.",
  h1="Quanto cobrar por pudim?",
  sub="Pudim é sobremesa de ceia e de encomenda o ano todo. Preencha os custos de <b>uma fornada</b> e quantos pudins ela rende. No exemplo, cada pudim de 1 kg sai por <b>R$ 62,67</b> (cerca de R$ 5,22 a fatia, cortado em 12).",
  lab=["Ingredientes da fornada<small>leite condensado, leite, ovos, açúcar da calda</small>","Embalagens com tampa e etiquetas","Gás do forno (banho-maria)","Pudins que a fornada rende"],
  vals=[50,8,6,2,2,15,5,20],
  art="""<h2>Exemplo resolvido: 2 pudins de leite condensado de 1 kg</h2>
<p>Os números abaixo são os que já vêm preenchidos na calculadora. São um <b>exemplo</b> com preços de mercado comuns (estimativa nossa): troque pelos valores das suas notas.</p>
<ul>
<li><b>Ingredientes:</b> R$ 50,00 (por pudim: 2 latas de leite condensado R$ 14,00, leite R$ 4,00, ovos R$ 5,00, açúcar da calda R$ 2,00 = R$ 25,00).</li>
<li><b>Rendimento:</b> 2 pudins de cerca de 1 kg (forma de 22 cm), 12 fatias cada.</li>
<li><b>Embalagem:</b> 2 bases com tampa e etiqueta a R$ 4,00 = R$ 8,00. <b>Gás:</b> cerca de 1 h de forno em banho-maria, R$ 6,00.</li>
<li><b>Tempo:</b> 2 h de trabalho (calda, massa, assar, esfriar, desenformar e embalar), a R$ 15 por hora = R$ 30,00.</li>
<li><b>Taxa da maquininha:</b> 5%. <b>Lucro do negócio:</b> 20%.</li>
</ul>
<p><b>A conta por pudim:</b> material = (50,00 + 8,00 + 6,00) ÷ 2 = R$ 32,00; tempo = 30,00 ÷ 2 = R$ 15,00; custo = R$ 47,00.<br>
Preço = 47,00 ÷ (1 − 0,05 − 0,20) = 47,00 ÷ 0,75 = <b>R$ 62,67 o pudim</b>.<br>
Abaixo de R$ 49,47 (47,00 ÷ 0,95) você não paga nem o material e as suas horas depois da taxa.</p>
<h2>Preço da fatia</h2>
<p>Dividindo o pudim em 12, a fatia sai por cerca de <b>R$ 5,22</b>. Se vender em fatias, some o pote ou a embalagem individual de cada uma no campo de embalagem e troque o rendimento para o número de fatias.</p>
<h2>Erros comuns</h2>
<p><b>Esquecer o gás do banho-maria.</b> Pudim fica muito tempo no forno: o gás pesa mais que em outros doces.</p>
<p><b>Cobrar a fatia como 1/12 do pudim sem a embalagem.</b> Cada fatia vai num pote com tampa e colher: isso é custo.</p>
<p><b>Não contar o pudim que racha ou gruda.</b> Se de vez em quando um não sai perfeito, some uma pequena margem nos ingredientes.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quanto cobrar por um pudim de 1 kg?</b> Faça a conta com os seus custos. No exemplo, R$ 62,67; com ingredientes mais baratos ou mais pudins por fornada, o preço cai.</p>
<p><b>Pudim dura quanto tempo?</b> Na geladeira, bem tampado, costuma durar poucos dias. Combine a entrega perto do dia da ceia e escreva a validade na etiqueta.</p>
<p><b>Quanto vale a minha hora?</b> Divida quanto quer ganhar no mês pelas horas que trabalha. Ex.: R$ 2.000 ÷ 120 h ≈ R$ 16,67 por hora.</p>
<h2>Outras calculadoras</h2>
<p><a href="/precifica/pave/">Preço de pavê de Natal</a> · <a href="/precifica/ceia-de-natal/">Quanto comprar para a ceia de Natal</a> · <a href="/precifica/trufa/">Preço de trufa</a></p>""")
