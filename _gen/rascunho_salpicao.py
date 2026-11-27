# Rascunho (ciclo 36, 27/11): página /salpicao/. Publicar em 29/11 (28/11 já tem 3: pão de mel, trufa, biscoito).
# Colar o dict na lista do build.py, opção no menu (<option value="salpicao/">Salpicão</option>), links na ceia/panetone e no sitemap.
# Conta conferida com python no ciclo 36: material (125+10+5)/10 = 14,00; tempo 45/10 = 4,50; custo 18,50;
# preço 18,50/0,75 = 24,67 (pote 500 g); kg 49,33; mínimo 18,50/0,95 = 19,47.
PAGINA = dict(slug="salpicao",title="Quanto cobrar por salpicão: calculadora grátis",
  desc="Vai vender salpicão para a ceia de Natal? Calcule o preço do pote e do quilo: frango, maionese, batata palha, pote, gás, seu tempo e taxas. Grátis.",
  h1="Quanto cobrar por salpicão de Natal?",
  sub="Salpicão é um dos pratos mais encomendados para a ceia. Preencha os custos de <b>uma leva</b> e quantos potes ela rende. No exemplo, o pote de 500 g sai por <b>R$ 24,67</b> (o quilo por R$ 49,33).",
  lab=["Ingredientes da leva<small>frango, maionese, batata palha, cenoura, milho, ervilha, uva passa, maçã, salsão</small>","Potes com tampa e etiquetas","Gás para cozinhar o frango","Potes que a leva rende"],
  vals=[125,10,5,10,3,15,5,20],
  art="""<h2>Exemplo resolvido: 5 kg de salpicão em 10 potes</h2>
<p>Os números abaixo são os que já vêm preenchidos na calculadora. São um <b>exemplo</b> com preços de mercado comuns (estimativa nossa): troque pelos valores das suas notas.</p>
<ul>
<li><b>Ingredientes:</b> R$ 125,00 (2 kg de peito de frango R$ 40,00; 1 kg de maionese R$ 20,00; 1 kg de batata palha R$ 30,00; legumes, frutas, uva passa e temperos R$ 35,00).</li>
<li><b>Rendimento:</b> 10 potes de 500 g (5 kg).</li>
<li><b>Embalagem:</b> pote de 500 ml com tampa e etiqueta a R$ 1,00 = R$ 10,00. <b>Gás:</b> R$ 5,00.</li>
<li><b>Tempo:</b> 3 h de trabalho (cozinhar e desfiar o frango, picar, misturar, embalar), a R$ 15 por hora = R$ 45,00.</li>
<li><b>Taxa da maquininha:</b> 5%. <b>Lucro do negócio:</b> 20%.</li>
</ul>
<p><b>A conta por pote:</b> material = (125,00 + 10,00 + 5,00) ÷ 10 = R$ 14,00; tempo = 45,00 ÷ 10 = R$ 4,50; custo = R$ 18,50.<br>
Preço = 18,50 ÷ (1 − 0,05 − 0,20) = 18,50 ÷ 0,75 = <b>R$ 24,67 o pote de 500 g</b>, ou <b>R$ 49,33 o quilo</b>.<br>
Abaixo de R$ 19,47 o pote (18,50 ÷ 0,95) você não paga nem o material e as suas horas depois da taxa.</p>
<h2>Batata palha à parte</h2>
<p>A batata palha murcha se ficar misturada muitas horas. Muita gente entrega num saquinho separado para o cliente pôr na hora: o saquinho entra no campo de embalagem.</p>
<h2>Erros comuns</h2>
<p><b>Contar o frango cru e esquecer que ele encolhe.</b> 2 kg de peito cru viram menos de 1,5 kg cozido e desfiado. Pese a leva pronta para saber o rendimento de verdade.</p>
<p><b>Cobrar o pote e esquecer a entrega.</b> Na véspera de Natal a entrega demora mais: cobre à parte ou some no preço.</p>
<p><b>Aceitar encomenda sem sinal.</b> Peça metade adiantada: se o cliente desistir em 24/12, você não fica com 5 kg de salpicão.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quanto salpicão por pessoa na ceia?</b> Como acompanhamento, uns 100 a 150 g por pessoa: um pote de 500 g serve de 3 a 5 pessoas.</p>
<p><b>Salpicão precisa de geladeira?</b> Sim, leva maionese. Entregue gelado e escreva na etiqueta a validade e "manter na geladeira".</p>
<p><b>Quanto vale a minha hora?</b> Divida quanto quer ganhar no mês pelas horas que trabalha. Ex.: R$ 2.000 ÷ 120 h ≈ R$ 16,67 por hora.</p>
<h2>Outras calculadoras</h2>
<p><a href="/precifica/ceia-de-natal/">Quanto comprar para a ceia de Natal</a> · <a href="/precifica/pave/">Preço de pavê</a> · <a href="/precifica/rabanada/">Preço de rabanada</a></p>""")
