# Rascunho (ciclo 40, 28/11): página /pernil-assado/. Publicar em 29/11 junto com /salpicao/ e /farofa-de-natal/ (3 de 3).
# Colar o dict na lista do build.py, opção no menu (<option value="pernil-assado/">Pernil assado</option>), links na ceia/farofa/salpicão e no sitemap.
# Conta conferida com python no ciclo 40: material (300+24+15)/2 = 169,50; tempo 3 h x 15 / 2 = 22,50; custo 192,00;
# preço 192,00/0,75 = 256,00 (pernil de ~6 kg cru, ~4,2 kg assado); kg assado 60,95; mínimo 192,00/0,95 = 202,11.
PAGINA = dict(slug="pernil-assado",title="Quanto cobrar por pernil assado: calculadora",
  desc="Vai vender pernil assado para o Natal? Calcule o preço do pernil inteiro e do quilo: carne, tempero, bandeja, gás do forno, seu tempo e taxas.",
  h1="Quanto cobrar por pernil assado?",
  sub="Pernil assado é um dos pratos mais encomendados para a ceia. Preencha os custos de <b>uma fornada</b> e quantos pernis ela rende. No exemplo, o pernil de ~6 kg sai por <b>R$ 256,00</b> (cerca de R$ 60,95 o quilo assado).",
  lab=["Ingredientes da fornada<small>pernil suíno com osso, alho, cebola, limão, laranja, sal, ervas, azeite</small>","Bandejas de alumínio, papel-alumínio e etiquetas","Gás do forno","Pernis que a fornada rende"],
  vals=[300,24,15,2,3,15,5,20],
  art="""<h2>Exemplo resolvido: 2 pernis de 6 kg</h2>
<p>Os números abaixo são os que já vêm preenchidos na calculadora. São um <b>exemplo</b> com preços de mercado comuns (estimativa nossa): troque pelos valores das suas notas.</p>
<ul>
<li><b>Ingredientes:</b> R$ 300,00 (2 pernis suínos com osso de 6 kg a R$ 22,00 o quilo = R$ 264,00; alho, cebola, limão, laranja, sal, ervas e azeite R$ 36,00).</li>
<li><b>Rendimento:</b> 2 pernis. Cada um perde cerca de 30% no forno: de 6 kg cru sai uns 4,2 kg assado.</li>
<li><b>Embalagem:</b> bandeja grande de alumínio, papel-alumínio e etiqueta a R$ 12,00 = R$ 24,00. <b>Gás:</b> forno ligado umas 4 a 5 horas, R$ 15,00.</li>
<li><b>Tempo:</b> 3 h de trabalho (temperar na véspera, assar, regar, desossar se o cliente pedir, embalar), a R$ 15 por hora = R$ 45,00.</li>
<li><b>Taxa da maquininha:</b> 5%. <b>Lucro do negócio:</b> 20%.</li>
</ul>
<p><b>A conta por pernil:</b> material = (300,00 + 24,00 + 15,00) ÷ 2 = R$ 169,50; tempo = 45,00 ÷ 2 = R$ 22,50; custo = R$ 192,00.<br>
Preço = 192,00 ÷ (1 − 0,05 − 0,20) = 192,00 ÷ 0,75 = <b>R$ 256,00 o pernil</b>, ou cerca de <b>R$ 60,95 o quilo assado</b> (256,00 ÷ 4,2).<br>
Abaixo de R$ 202,11 o pernil (192,00 ÷ 0,95) você não paga nem o material e as suas horas depois da taxa.</p>
<h2>Erros comuns</h2>
<p><b>Cobrar pelo peso cru.</b> O cliente recebe o pernil assado, que pesa uns 30% menos. Se vender por quilo, pese depois de assar.</p>
<p><b>Esquecer o gás do forno.</b> São horas de forno ligado: numa fornada grande isso pesa no custo.</p>
<p><b>Comprar a carne sem sinal.</b> O pernil é o item mais caro. Peça metade adiantada antes de ir ao açougue.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quanto pernil por pessoa na ceia?</b> Com outros pratos na mesa, uns 300 a 400 g de pernil cru (com osso) por pessoa: um pernil de 6 kg serve de 15 a 20 pessoas.</p>
<p><b>Vale vender pernil desossado ou fatiado?</b> Dá mais trabalho e o peso cai: some essas horas e cobre mais caro pelo pernil pronto para servir.</p>
<p><b>Quanto vale a minha hora?</b> Divida quanto quer ganhar no mês pelas horas que trabalha. Ex.: R$ 2.000 ÷ 120 h ≈ R$ 16,67 por hora.</p>
<h2>Outras calculadoras</h2>
<p><a href="/precifica/ceia-de-natal/">Quanto comprar para a ceia de Natal</a> · <a href="/precifica/farofa-de-natal/">Preço de farofa de Natal</a> · <a href="/precifica/salpicao/">Preço de salpicão</a></p>""")
