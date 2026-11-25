# Gera páginas de nicho e /sobre/ a partir de index.html (rodar com: python -I build.py)
import os, re, html, json
BASE="https://freitasgoulartgomesa-prog.github.io/precifica/"
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src=open(os.path.join(ROOT,"index.html"),encoding="utf-8").read()
HEAD=src[:src.index("<body>")]
BODY=src[src.index("<body>"):]
BODY=re.sub(r"<!--HOME-->.*?<!--/HOME-->\n?","",BODY,flags=re.S)  # artigo só da página inicial
NAV=re.search(r'<nav aria-label="Calculadoras">.*?</nav>',src,re.S).group(0)
FOOTER=re.search(r"<footer>.*?</footer>",src,re.S).group(0)

def head_for(title,desc,url):
    h=HEAD
    h=re.sub(r"<title>.*?</title>",lambda m:f"<title>{html.escape(title)}</title>",h,1,flags=re.S)
    h=re.sub(r'<meta name="description" content="[^"]*">',lambda m:f'<meta name="description" content="{html.escape(desc)}">',h,1)
    h=re.sub(r'<link rel="canonical" href="[^"]*">',lambda m:f'<link rel="canonical" href="{url}">',h,1)
    ld=json.dumps({"@context":"https://schema.org","@type":"WebApplication","name":"Precifica","url":url,
        "description":desc,"applicationCategory":"BusinessApplication","operatingSystem":"Any",
        "inLanguage":"pt-BR","offers":{"@type":"Offer","price":"0","priceCurrency":"BRL"}},ensure_ascii=False)
    og=(f'<meta property="og:title" content="{html.escape(title)}">\n'
        f'<meta property="og:description" content="{html.escape(desc)}">\n'
        f'<meta property="og:url" content="{url}">\n')
    bc={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Precifica","item":BASE}]}
    if url!=BASE: bc["itemListElement"].append({"@type":"ListItem","position":2,"name":title.split(":")[0],"item":url})
    ld+='</script>\n<script type="application/ld+json">'+json.dumps(bc,ensure_ascii=False)
    h=re.sub(r'<script type="application/ld\+json">.*?</script>',lambda m:f'<script type="application/ld+json">{ld}</script>\n'+og,h,1,flags=re.S)
    return h

def write(slug,content):
    d=os.path.join(ROOT,slug) if slug else ROOT
    os.makedirs(d,exist_ok=True)
    open(os.path.join(d,"index.html"),"w",encoding="utf-8").write(content)

PAGES=[
 dict(slug="shopee",title="Calculadora de preço Shopee 2026: taxa e lucro",
  desc="Calcule quanto cobrar na Shopee com a comissão e a taxa fixa por item de out/2026. A conta escolhe a faixa certa sozinha. Grátis.",
  h1="Calculadora de preço para vender na Shopee",
  sub="Na Shopee (taxas de out/2026), produto até R$ 79,99 paga <b>20% + R$ 4,50 por item</b>. Com custo de R$ 14 por peça e 20% de lucro, cobre <b>R$ 30,83</b>. Preencha os seus custos: a calculadora escolhe a faixa de comissão que fecha com o preço final.",
  lab=["Materiais do lote<small>tecido, linha, miçanga, base, tinta</small>","Embalagem de envio<small>saquinho, plástico-bolha, etiqueta, fita</small>","Luz e outros gastos (estimativa)","Peças que o lote rende"],
  vals=[60,15,5,10,5,12,20,20,4.5],
  extra='<label style="display:flex;gap:8px;align-items:center"><input id="auto" type="checkbox" checked style="width:auto"> Usar as faixas da Shopee (out/2026) automaticamente</label>\n<label style="display:flex;gap:8px;align-items:center"><input id="mais450" type="checkbox" style="width:auto"> Vendo como CPF e tive mais de 450 pedidos em 90 dias (+R$ 3 por item)</label>',
  script='<script>window.FAIXAS=[{nome:"até R$ 79,99",de:0,ate:79.99,t:0.20,fixa:4.5},{nome:"R$ 80 a R$ 99,99",de:80,ate:99.99,t:0.14,fixa:16},{nome:"R$ 100 a R$ 199,99",de:100,ate:199.99,t:0.14,fixa:20},{nome:"a partir de R$ 200",de:200,ate:1e9,t:0.14,fixa:26}];</script>',
  art="""<p><small>Atualizado em 24/11/2026. Taxas vigentes desde 1º/10/2026 segundo <a href="https://ecommercenapratica.com/blog/taxa-shopee/">E-commerce na Prática</a> e <a href="https://viniensina.com.br/?p=4619">Vini Ensina</a>. A Shopee muda as taxas com frequência: confira na Central do Vendedor. Para usar outros valores, desmarque "Usar as faixas da Shopee" e digite a taxa e a taxa fixa.</small></p>
<h2>Taxas da Shopee por faixa de preço (out/2026)</h2>
<table>
<tr><th>Preço de venda do item</th><th>Comissão</th><th>Taxa fixa por item</th></tr>
<tr><td>até R$ 79,99</td><td>20%</td><td>R$ 4,50</td></tr>
<tr><td>R$ 80 a R$ 99,99</td><td>14%</td><td>R$ 16,00</td></tr>
<tr><td>R$ 100 a R$ 199,99</td><td>14%</td><td>R$ 20,00</td></tr>
<tr><td>a partir de R$ 200</td><td>14%</td><td>R$ 26,00</td></tr>
</table>
<p>Vale para CPF e CNPJ. Quem vende como pessoa física e passou de 450 pedidos em 90 dias paga R$ 3 a mais por item (marque a opção na calculadora).</p>
<h2>Exemplo resolvido: lote de 10 peças artesanais</h2>
<p>São os números que já vêm preenchidos. Troque pelos seus.</p>
<ul>
<li><b>Materiais:</b> R$ 60. <b>Embalagem de envio:</b> R$ 15. <b>Luz e outros:</b> R$ 5. Total R$ 80 ÷ 10 peças = R$ 8,00 por peça.</li>
<li><b>Tempo:</b> 5 horas a R$ 12 = R$ 60 ÷ 10 = R$ 6,00 por peça. Custo total: R$ 14,00.</li>
<li><b>Lucro do negócio:</b> 20%.</li>
</ul>
<p><b>A conta na primeira faixa:</b> (14,00 + 4,50) ÷ (1 − 0,20 − 0,20) = 18,50 ÷ 0,60 = <b>R$ 30,83</b>. Como R$ 30,83 está abaixo de R$ 79,99, a faixa fecha.<br>
Preço mínimo (sem lucro): 18,50 ÷ 0,80 = R$ 23,13. Abaixo disso você paga para vender.</p>
<h2>Quando o preço muda de faixa</h2>
<p>Peça com custo total de R$ 45 e 20% de lucro: na primeira faixa daria (45 + 4,50) ÷ 0,60 = R$ 82,50, que já passa de R$ 79,99. Então a faixa não fecha. Na segunda: (45 + 16) ÷ (1 − 0,14 − 0,20) = 61 ÷ 0,66 = <b>R$ 92,42</b>, dentro de R$ 80 a R$ 99,99. A calculadora faz esse teste sozinha e mostra qual faixa usou.</p>
<p>Às vezes a conta cai num "buraco" entre faixas. Aí a calculadora sugere o menor preço da faixa seguinte (ex.: R$ 80,00), que já cobre o lucro que você pediu.</p>
<h2>Erros comuns</h2>
<p><b>Esquecer a taxa fixa.</b> Em produto barato ela pesa muito: num chaveiro de R$ 15, R$ 4,50 são 30% do preço, além dos 20% de comissão.</p>
<p><b>Usar o mesmo preço da feira.</b> Na feira não há comissão. Na Shopee, a mesma peça precisa de preço maior ou você perde o lucro.</p>
<p><b>Somar a porcentagem em cima do custo.</b> Custo × 1,20 não paga a comissão de 20%, porque ela é tirada do preço final. Use a divisão, como a calculadora faz.</p>
<p><b>Não contar a embalagem de envio.</b> Plástico-bolha, saquinho e etiqueta entram em toda venda.</p>
<h2>Perguntas frequentes</h2>
<p><b>Vale a pena vender kit em vez de peça avulsa?</b> Muitas vezes sim: a taxa fixa é cobrada por item, então um kit de 3 peças paga uma taxa fixa só. Faça a conta do kit como se fosse uma peça.</p>
<p><b>O frete entra na conta?</b> Não. Esta calculadora mostra o preço do produto. Programas de frete da Shopee podem ter regras e custos próprios: confira no painel.</p>
<p><b>Preciso de CNPJ?</b> Não para vender; segundo as fontes, a tabela de out/2026 é a mesma para CPF e CNPJ.</p>
<p><b>Por que meu preço deu exatamente R$ 80,00 ou R$ 100,00?</b> É o caso do "buraco" entre faixas explicado acima.</p>
<h2>Outras calculadoras</h2>
<p><a href="/precifica/">Calculadora geral de preço</a> · <a href="/precifica/croche/">Preço de peça de crochê</a> · <a href="/precifica/bijuteria/">Preço de bijuteria</a></p>"""),
 dict(slug="brigadeiro",title="Quanto cobrar por brigadeiro: calculadora grátis",
  desc="Calcule o preço do brigadeiro por unidade: ingredientes, forminha, gás, seu tempo e taxas. Grátis, direto no celular.",
  h1="Quanto cobrar por brigadeiro?",
  sub="Preencha os custos de <b>uma receita</b> (uma panela) e quantos brigadeiros ela rende. A conta mostra o preço por unidade.",
  lab=["Ingredientes da receita<small>leite condensado, chocolate, manteiga, granulado</small>","Forminhas, caixinha, etiqueta","Gás e luz (estimativa)","Brigadeiros que a receita rende"],
  vals=[11.02,1.8,1.5,30,1,15,5,20],
  art="""<h2>Exemplo resolvido: 30 brigadeiros de 15 g</h2>
<p>Os números abaixo são os que já vêm preenchidos na calculadora. São um <b>exemplo</b>: troque pelos valores das suas notas e do seu mercado.</p>
<ul>
<li><b>Ingredientes da panela:</b> R$ 11,02 (1 lata de leite condensado R$ 7,00, 30 g de chocolate em pó R$ 1,35, 15 g de manteiga R$ 0,75 e 80 g de granulado R$ 1,92).</li>
<li><b>Forminhas:</b> 30 a R$ 0,06 = R$ 1,80. <b>Gás e luz:</b> R$ 1,50.</li>
<li><b>Rendimento:</b> a massa pronta pesou 450 g; 450 ÷ 15 g = 30 brigadeiros.</li>
<li><b>Tempo:</b> 1 h do fogão até as forminhas, a R$ 15 por hora = R$ 15,00.</li>
<li><b>Taxa da maquininha:</b> 5%. <b>Lucro do negócio:</b> 20%.</li>
</ul>
<p><b>A conta:</b> material por unidade = (11,02 + 1,80 + 1,50) ÷ 30 = R$ 0,48. Tempo por unidade = 15,00 ÷ 30 = R$ 0,50. Total = R$ 0,98.<br>
Preço = 0,977 ÷ (1 − 0,05 − 0,20) = 0,977 ÷ 0,75 = <b>R$ 1,30 por brigadeiro</b> (R$ 130 o cento).<br>
Abaixo de R$ 1,03 (0,977 ÷ 0,95) você não paga nem o material e as suas horas depois da taxa.</p>
<h2>Onde está o custo do brigadeiro</h2>
<p><b>Leite condensado e chocolate</b> são quase todo o custo da massa. Trocar o chocolate em pó comum por cacau 50% ou chocolate nobre muda bastante o preço: faça uma conta para cada versão.</p>
<p><b>Cobertura:</b> granulado comum, granulado belga, castanha ou confeito colorido têm custos bem diferentes. Pese quanto vai em cada lote.</p>
<p><b>Forminha:</b> parece pouco, mas no exemplo R$ 1,80 ÷ 30 = R$ 0,06 por unidade, mais que o gás (R$ 0,05). Caixinha e etiqueta somam ainda mais.</p>
<p><b>Rendimento:</b> o jeito mais exato é pesar a massa pronta e dividir pelo peso de cada bolinha. Brigadeiro de 15 g rende mais unidades que o de 20 g com a mesma panela.</p>
<h2>Erros comuns</h2>
<p><b>Multiplicar o custo por 2 ou 3.</b> Essa regra ignora o seu tempo. Enrolar 100 brigadeiros leva horas, e elas precisam estar no preço.</p>
<p><b>Dar desconto grande no cento.</b> Se o desconto for maior que o lucro, você paga para trabalhar. No exemplo, o lucro é 20%; um desconto de 10% no cento ainda deixa margem, um de 35% não.</p>
<p><b>Copiar o preço da vizinha.</b> No exemplo, vendendo a R$ 0,80: 30 × 0,80 = R$ 24,00, menos 5% de taxa = R$ 22,80, menos R$ 14,32 de material = R$ 8,48 pela 1 h de trabalho, sem lucro nenhum. Faça a sua conta antes de baixar o preço.</p>
<p><b>Contar os que você prova ou que quebram.</b> No rendimento entram só os que vão para a caixa.</p>
<p><b>Esquecer a taxa.</b> Cartão, Pix com taxa ou app de entrega ficam com uma parte do preço. Coloque a taxa no campo certo.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quanto cobrar pelo cento de brigadeiro?</b> Multiplique o preço por unidade por 100. No exemplo, 100 × R$ 1,30 = R$ 130. Para comparar: em 2026 o cento tradicional costuma sair entre R$ 80 e R$ 160, mais barato no Nordeste e mais caro nas capitais do Sudeste (referências: <a href="https://engrenou.com.br/precificacao/cento-de-brigadeiro" rel="nofollow">Engrenou</a> e <a href="https://receitorio.app/guia/quanto-cobrar-por-brigadeiro/" rel="nofollow">Receitório</a>). Brigadeiro gourmet passa disso. Se quiser dar desconto para festa, veja a regra acima.</p>
<p><b>Brigadeiro gourmet deve custar mais?</b> Sim, porque o ingrediente é mais caro e costuma levar mais tempo para decorar. Preencha a calculadora com os custos da versão gourmet.</p>
<p><b>E a taxa de entrega?</b> Cobre à parte. A calculadora mostra o preço do produto; o frete muda conforme a distância.</p>
<p><b>Quanto vale a minha hora?</b> Divida quanto quer ganhar no mês pelas horas que trabalha. Ex.: R$ 2.000 ÷ 120 h ≈ R$ 16,67 por hora.</p>"""),
 dict(slug="panetone",title="Quanto cobrar por panetone caseiro: calculadora grátis",
  desc="Vai vender panetone ou chocotone no Natal? Calcule o preço do panetone caseiro de 500 g: ingredientes, forma, embalagem, forno, seu tempo e taxas. Grátis.",
  h1="Quanto cobrar por panetone caseiro?",
  sub="Renda extra no Natal sem vender no prejuízo. Preencha os custos de <b>uma fornada</b> e quantos panetones ela rende. A conta mostra o preço de cada um.",
  lab=["Ingredientes da fornada<small>farinha, manteiga, ovos, açúcar, fermento, frutas ou gotas de chocolate</small>","Formas de papel, saco, fita e etiqueta","Gás ou luz do forno (estimativa)","Panetones que a fornada rende"],
  vals=[28.9,7,4,2,1.5,15,5,20],
  art="""<h2>Exemplo resolvido: 2 panetones caseiros de 500 g</h2>
<p>Os números abaixo são os que já vêm preenchidos na calculadora. São um <b>exemplo</b> com preços de mercado comuns: troque pelos valores das suas notas.</p>
<ul>
<li><b>Ingredientes da fornada:</b> R$ 28,90 (500 g de farinha R$ 2,75, 150 g de açúcar R$ 0,75, 150 g de manteiga R$ 9,00, 4 ovos R$ 3,20, 200 ml de leite R$ 1,20, 10 g de fermento biológico seco R$ 1,00, 200 g de frutas cristalizadas R$ 6,00, 100 g de uva-passa R$ 3,50 e essência e raspas de laranja R$ 1,50).</li>
<li><b>Embalagem:</b> 2 formas de papel de 500 g (R$ 1,50 cada) e 2 sacos com fita e etiqueta (R$ 2,00 cada) = R$ 7,00. <b>Forno:</b> R$ 4,00.</li>
<li><b>Tempo:</b> 1,5 h de trabalho de verdade (sovar, modelar, assar e embalar), a R$ 15 por hora = R$ 22,50. As horas de crescimento da massa não entram, porque você pode fazer outra coisa.</li>
<li><b>Taxa da maquininha:</b> 5%. <b>Lucro do negócio:</b> 20%.</li>
</ul>
<p><b>A conta:</b> material por panetone = (28,90 + 7,00 + 4,00) ÷ 2 = R$ 19,95. Tempo por panetone = 22,50 ÷ 2 = R$ 11,25. Total = R$ 31,20.<br>
Preço = 31,20 ÷ (1 − 0,05 − 0,20) = 31,20 ÷ 0,75 = <b>R$ 41,60 por panetone de 500 g</b>.<br>
Abaixo de R$ 32,84 (31,20 ÷ 0,95) você não paga nem o material e as suas horas depois da taxa.</p>
<h2>Chocotone e panetone recheado</h2>
<p><b>Chocotone:</b> troque as frutas e a passa (R$ 9,50 no exemplo) por 200 g de gotas de chocolate próprias para forno e coloque o preço que você pagou. Faça uma conta para cada sabor: o recheio muda o custo.</p>
<p><b>Trufado ou com recheio de brigadeiro, doce de leite ou Nutella:</b> o recheio pode custar mais que a massa. Some o recheio nos ingredientes e conte o tempo a mais para rechear.</p>
<p><b>Tamanhos:</b> o de 500 g é o mais procurado para presente. Um mini de 100 g sai com a mesma massa: divida a fornada por mais unidades e inclua uma forma e um saco para cada uma.</p>
<h2>Erros comuns</h2>
<p><b>Comparar com o panetone de mercado em promoção.</b> O industrial compra em toneladas. O seu é feito à mão, com manteiga e sem conservante: venda isso, não o preço mais baixo.</p>
<p><b>Esquecer a embalagem.</b> No exemplo, a embalagem é R$ 3,50 por panetone, quase 1/5 do material. Para presente, caixa e laço custam mais: coloque no campo certo.</p>
<p><b>Contar as horas de crescimento como trabalho, ou esquecer o seu tempo de verdade.</b> Só entra o tempo em que você está trabalhando. Mas ele precisa entrar.</p>
<p><b>Aceitar encomenda grande sem conta.</b> 20 panetones são 10 fornadas no exemplo, cerca de 15 horas de trabalho. Veja se o forno e a sua agenda dão conta antes de fechar o preço.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quanto cobrar por um panetone caseiro de 500 g?</b> Faça a sua conta: no exemplo dá R$ 41,60. Para comparar, panetones industriais gourmet de 500 g saíram por R$ 70 a R$ 90 em 2025 (<a href="https://www.guiadasemana.com.br/gastronomia/galeria/lancamentos-panetones-chocotones-2025" rel="nofollow">Guia da Semana</a>). O seu caseiro pode ficar entre o de supermercado e o gourmet.</p>
<p><b>Dá para vender panetone como renda extra no Natal?</b> Sim, desde que o preço pague o material, o seu tempo e a taxa. Comece com encomendas de conhecidos e anote quanto tempo cada fornada leva de verdade.</p>
<p><b>E para vender em cesta de Natal?</b> Calcule o panetone aqui e some o preço de cada item da cesta. A cesta inteira também precisa de lucro e da sua hora para montar.</p>
<p><b>Quanto vale a minha hora?</b> Divida quanto quer ganhar no mês pelas horas que trabalha. Ex.: R$ 2.000 ÷ 120 h ≈ R$ 16,67 por hora.</p>"""),
 dict(slug="bolo-de-pote",title="Quanto cobrar por bolo de pote: calculadora grátis",
  desc="Calcule o preço do bolo de pote: massa, recheio, pote, colher, gás, seu tempo e taxas. Grátis e sem cadastro.",
  h1="Quanto cobrar por bolo de pote?",
  sub="Com R$ 65 de material e embalagem para 12 potes, 3 horas de trabalho, 5% de taxa e 25% de lucro, o bolo de pote sai a <b>R$ 13,10</b>. Preencha os custos de <b>uma fornada</b> (massa + recheios) e quantos potes ela enche.",
  lab=["Massa e recheios<small>farinha, ovos, leite condensado, chocolate, frutas</small>","Potes, tampas, colherzinhas, etiquetas","Gás e luz (estimativa)","Potes que a fornada enche"],
  vals=[45,15,5,12,3,15,5,25],
  art="""<h2>Exemplo resolvido: fornada de 12 potes de 250 ml</h2>
<p>Os números abaixo são os que já vêm preenchidos na calculadora. São um <b>exemplo</b>: troque pelos valores das suas notas e do seu mercado.</p>
<ul>
<li><b>Massa e recheios:</b> R$ 45,00 (massa de chocolate, dois recheios cremosos e cobertura para 12 potes).</li>
<li><b>Potes com tampa, colherzinhas e etiquetas:</b> R$ 15,00. <b>Gás e luz:</b> R$ 5,00 (forno ligado cerca de 40 minutos, mais o fogão dos recheios).</li>
<li><b>Tempo:</b> 3 horas entre assar, fazer os recheios, montar as camadas e lavar a louça, a R$ 15 por hora = R$ 45,00.</li>
<li><b>Taxa da maquininha:</b> 5%. <b>Lucro do negócio:</b> 25%.</li>
</ul>
<p><b>A conta:</b> custo por pote = (45 + 15 + 5) ÷ 12 = R$ 5,42. Tempo por pote = 45 ÷ 12 = R$ 3,75. Total = R$ 9,17.<br>
Preço = 9,17 ÷ (1 − 0,05 − 0,25) = 9,17 ÷ 0,70 = <b>R$ 13,10 por pote</b>.<br>
Abaixo de R$ 9,65 (9,17 ÷ 0,95) você não paga nem o material e as suas horas depois da taxa.</p>
<h2>Onde está o custo do bolo de pote</h2>
<p><b>Embalagem:</b> no exemplo, pote, tampa, colher e etiqueta somam R$ 1,25 por unidade, quase um quarto do custo de material. Comprar potes em caixa fechada costuma baixar esse valor.</p>
<p><b>Recheio:</b> é o que mais muda entre sabores. Creme de leite ninho, creme de avelã e frutas vermelhas custam bem mais que um brigadeiro simples. Faça uma conta por sabor e não um preço único para todos.</p>
<p><b>Tamanho do pote:</b> pote de 250 ml e pote de 350 ml levam quantidades diferentes de massa e recheio. Se vende os dois, faça duas contas.</p>
<p><b>Rendimento:</b> conte quantos potes cheios saem de verdade da fornada. Sobra de massa que vira lanche não entra.</p>
<h2>Erros comuns</h2>
<p><b>Copiar o preço da concorrente.</b> Ela pode ter custos, tamanho de pote e recheios diferentes dos seus. Use o preço dela só para comparar depois de fazer a sua conta.</p>
<p><b>Esquecer a perda do dia.</b> Se você leva 20 potes para vender e costuma voltar com 3, o custo dos 3 precisa estar no preço dos 17 vendidos. Coloque 17 no campo de potes.</p>
<p><b>Não contar a geladeira e a bolsa térmica.</b> Gelo, bolsa térmica e a geladeira ligada a mais também são custo. Some uma estimativa no campo de gás e luz.</p>
<p><b>Dar desconto maior que o lucro.</b> Com 25% de lucro, um "leve 3, pague 2" (33% de desconto) faz você trabalhar no prejuízo.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quanto cobrar por bolo de pote de 250 ml?</b> Depende dos seus custos. No exemplo desta página, com R$ 65 de material e embalagem para 12 potes e 3 horas de trabalho, o preço sai R$ 13,10.</p>
<p><b>Vale a pena vender pelo iFood?</b> Só se o preço no app for maior. A comissão sai do preço final: coloque a porcentagem do app no campo de taxa e veja o novo preço.</p>
<p><b>Quantos potes preciso vender por mês?</b> No exemplo, sobram R$ 7,02 por pote para pagar as suas horas e o lucro. Para tirar R$ 1.500 no mês: 1.500 ÷ 7,02 ≈ 214 potes, cerca de 18 fornadas.</p>
<p><b>Bolo de pote precisa de rótulo?</b> Para vender, é boa prática ter etiqueta com nome do produto, ingredientes e data de validade. As regras de rotulagem e de vigilância sanitária mudam conforme a cidade e o tipo de venda: confira na prefeitura.</p>
<h2>Outras calculadoras</h2>
<p><a href="/precifica/brigadeiro/">Quanto cobrar por brigadeiro</a> · <a href="/precifica/docinhos-e-bolo/">Quantos docinhos e quanto bolo para festa</a> · <a href="/precifica/">Calculadora geral de preço</a></p>"""),
 dict(slug="croche",title="Quanto cobrar por peça de crochê: calculadora grátis",
  desc="Calcule o preço da sua peça de crochê: linha, acessórios, embalagem, horas de trabalho e taxas. Grátis, direto no celular.",
  h1="Quanto cobrar por uma peça de crochê?",
  sub="Um amigurumi de 20 cm com R$ 34 de material e 6 horas de trabalho a R$ 12 por hora sai a <b>R$ 141,33</b> (5% de taxa e 20% de lucro). Preencha os custos de <b>uma peça</b> (ou de um lote, dizendo quantas peças saem).",
  lab=["Linhas e fios<small>conte só a parte do novelo que a peça usa</small>","Acessórios e embalagem<small>enchimento, olhos, botões, saquinho, tag</small>","Luz e outros gastos (estimativa)","Peças feitas com esses materiais"],
  vals=[25,8,1,1,6,12,5,20],
  art="""<h2>Exemplo resolvido: amigurumi de 20 cm</h2>
<p>Os números abaixo são os que já vêm preenchidos na calculadora. São um <b>exemplo</b>: troque pelos seus.</p>
<ul>
<li><b>Linha:</b> R$ 25,00 (a parte dos novelos que a peça usou, não os novelos inteiros).</li>
<li><b>Enchimento, olhos de segurança, tag e saquinho:</b> R$ 8,00. <b>Luz:</b> R$ 1,00.</li>
<li><b>Tempo:</b> 6 horas, do primeiro ponto até a costura das partes, a R$ 12 por hora = R$ 72,00.</li>
<li><b>Taxa da maquininha:</b> 5%. <b>Lucro do negócio:</b> 20%.</li>
</ul>
<p><b>A conta:</b> material = 25 + 8 + 1 = R$ 34,00. Tempo = R$ 72,00. Total = R$ 106,00.<br>
Preço = 106 ÷ (1 − 0,05 − 0,20) = 106 ÷ 0,75 = <b>R$ 141,33</b>.<br>
Abaixo de R$ 111,58 (106 ÷ 0,95) você não paga o material e as suas horas depois da taxa.</p>
<p>Repare: o tempo é <b>dois terços</b> do custo. Se a mesma peça levar 4 horas em vez de 6, o preço cai para R$ 109,33. Por isso cronometrar é o passo mais importante.</p>
<h2>Onde está o custo do crochê</h2>
<p><b>Horas de trabalho:</b> quase sempre a maior parte. Anote o tempo das primeiras peças de cada modelo; com a prática ele cai, e o preço pode cair junto.</p>
<p><b>Linha usada:</b> pese a peça pronta e compare com o peso do novelo. Ex.: peça de 50 g feita com novelo de 100 g que custou R$ 20 usa R$ 10 de linha.</p>
<p><b>Acabamento:</b> olhos de segurança, enchimento, botões, forro, tag e embalagem. São pequenos, mas somam.</p>
<p><b>Peças em série:</b> se fizer 5 peças iguais, preencha os materiais e as horas do lote e coloque 5 em "Peças feitas". O custo por peça costuma cair, porque você fica mais rápida.</p>
<h2>Erros comuns</h2>
<p><b>Cobrar só a linha em dobro.</b> No exemplo, R$ 25 × 2 = R$ 50 deixaria de fora mais da metade do custo real (as horas).</p>
<p><b>Usar o valor do novelo inteiro.</b> Se sobra meio novelo para outra peça, só a metade entra nesta conta.</p>
<p><b>Comparar com peça industrial.</b> Peça de fábrica é feita em máquina, em escala. O cliente de crochê paga pelo feito à mão: mostre isso na foto e na descrição.</p>
<p><b>Esquecer a taxa.</b> Cartão, loja de artesanato consignada ou marketplace ficam com uma parte do preço. Ponha a porcentagem no campo de taxa; para Shopee, use a <a href="/precifica/shopee/">calculadora da Shopee</a>.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quanto vale a hora de trabalho no crochê?</b> Uma forma simples: divida quanto quer ganhar no mês pelas horas que pode trabalhar. Ex.: R$ 1.500 ÷ 130 h ≈ R$ 11,50 por hora. A referência do salário mínimo de 2026 é cerca de R$ 7,37 por hora.</p>
<p><b>E se o preço ficar alto demais?</b> É sinal de que a peça leva muitas horas. Opções: modelos mais rápidos, peças menores, ou vender o diferencial (exclusiva, sob encomenda, com nome) para quem paga mais.</p>
<p><b>Como cobrar encomenda personalizada?</b> Faça a conta como uma peça nova, com o tempo estimado a mais para criar o modelo. Peça um sinal (por exemplo, metade) antes de começar.</p>
<p><b>Receita (gráfico) comprada entra no custo?</b> Pode entrar dividida pelas peças que você pretende vender com ela. Ex.: receita de R$ 30 para 10 peças = R$ 3 por peça no campo de materiais.</p>
<h2>Outras calculadoras</h2>
<p><a href="/precifica/bijuteria/">Preço de bijuteria</a> · <a href="/precifica/shopee/">Preço para vender na Shopee</a> · <a href="/precifica/">Calculadora geral de preço</a></p>"""),
 dict(slug="bijuteria",title="Quanto cobrar por bijuteria artesanal: calculadora grátis",
  desc="Calcule o preço da sua bijuteria: miçangas, fecho, fio, embalagem, seu tempo e taxas. Grátis, direto no celular.",
  h1="Quanto cobrar por bijuteria artesanal?",
  sub="Num lote de 10 pulseiras de miçanga com R$ 40 de material, embalagem e outros gastos e 2 horas de trabalho, cada pulseira sai a <b>R$ 9,14</b> (5% de taxa e 25% de lucro). Preencha os custos de <b>um lote</b> de peças iguais e quantas peças saem dele.",
  lab=["Materiais do lote<small>miçangas, pedras, fio, fechos, argolas</small>","Embalagem<small>saquinho, cartela, tag</small>","Outros gastos (estimativa)","Peças que o lote rende"],
  vals=[30,8,2,10,2,12,5,25],
  art="""<h2>Exemplo resolvido: lote de 10 pulseiras de miçanga</h2>
<p>Os números abaixo são os que já vêm preenchidos na calculadora. São um <b>exemplo</b>: troque pelos seus.</p>
<ul>
<li><b>Materiais do lote:</b> R$ 30,00 (miçangas, fio elástico ou de silicone, fechos, terminais e argolas para 10 pulseiras).</li>
<li><b>Cartelas, saquinhos e tags:</b> R$ 8,00. <b>Outros gastos:</b> R$ 2,00 (cola, luz).</li>
<li><b>Tempo:</b> 2 horas para montar as 10, a R$ 12 por hora = R$ 24,00.</li>
<li><b>Taxa da maquininha:</b> 5%. <b>Lucro do negócio:</b> 25%.</li>
</ul>
<p><b>A conta:</b> custo por pulseira = (30 + 8 + 2) ÷ 10 = R$ 4,00. Tempo por pulseira = 24 ÷ 10 = R$ 2,40. Total = R$ 6,40.<br>
Preço = 6,40 ÷ (1 − 0,05 − 0,25) = 6,40 ÷ 0,70 = <b>R$ 9,14 por pulseira</b>.<br>
Abaixo de R$ 6,74 (6,40 ÷ 0,95) você não paga o material e as suas horas depois da taxa.</p>
<h2>Loja consignada: a mesma pulseira com 30% para a loja</h2>
<p>Se uma loja vende as suas peças e fica com 30%, coloque 30 no campo de taxa: 6,40 ÷ (1 − 0,30 − 0,25) = 6,40 ÷ 0,45 = <b>R$ 14,22</b>. É o preço de etiqueta na loja para você receber o mesmo que na venda direta. Para a Shopee, use a <a href="/precifica/shopee/">calculadora da Shopee</a>, que já tem a taxa fixa por item.</p>
<h2>Onde está o custo da bijuteria</h2>
<p><b>Peças de metal:</b> fecho, terminal, argola, pino e corrente costumam custar mais que as miçangas. Conte cada uma.</p>
<p><b>Pedras e cristais:</b> pedra natural, cristal e pérola mudam muito o custo. Faça uma conta para cada linha de produto.</p>
<p><b>Apresentação:</b> cartela, saquinho de organza e tag entram no custo, mas ajudam a cobrar mais e a vender como presente.</p>
<p><b>Perdas:</b> miçanga que quebra, fio que sobra e fecho que entorta. Se perde muito, aumente um pouco o valor dos materiais.</p>
<h2>Erros comuns</h2>
<p><b>Dividir o pacote de miçanga pelo número errado de peças.</b> Monte o lote inteiro e divida o custo pelas peças que saíram de verdade.</p>
<p><b>Cobrar o mesmo preço na feira e na loja.</b> Na loja consignada ou no marketplace, a taxa sai do preço. Veja o exemplo acima.</p>
<p><b>Não contar o tempo porque "é rápido".</b> 12 minutos por pulseira parecem pouco, mas em 10 pulseiras são 2 horas de trabalho.</p>
<p><b>Desconto no atacado maior que o lucro.</b> Para revendedora, dê desconto menor que o seu lucro, ou faça a conta com o lucro menor e veja se ainda vale.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quanto cobrar por uma pulseira de miçanga?</b> Depende dos materiais e do tempo. No exemplo desta página, R$ 9,14 na venda direta e R$ 14,22 numa loja que fica com 30%.</p>
<p><b>E a semijoia?</b> A conta é a mesma. Some o custo da peça pronta, incluindo o banho de metal, no campo de materiais.</p>
<p><b>Quanto cobrar de revendedora?</b> Uma forma: faça a conta com o lucro que quer manter (por exemplo, 10%) e use esse preço para a revendedora; ela define o preço final dela.</p>
<p><b>Preciso de nota fiscal?</b> Para vender pouco, como pessoa física, em geral não. Se as vendas crescerem, o MEI é o caminho mais simples; confira as regras no Portal do Empreendedor (gov.br).</p>
<h2>Outras calculadoras</h2>
<p><a href="/precifica/croche/">Preço de peça de crochê</a> · <a href="/precifica/shopee/">Preço para vender na Shopee</a> · <a href="/precifica/">Calculadora geral de preço</a></p>"""),
]

# Oferta da planilha paga (S1-5). Fica desligada até o Arthur mandar o link de venda da Kiwify: cole o link aqui e rode o build.
PLANILHA_URL="https://pay.kiwify.com.br/HS40mXy"
PLANILHA_HTML=(f'<aside class="oferta"><h2>Planilha Ficha técnica e preço (R$ 12,90)</h2>'
 '<p><b>Vai vender no Natal?</b> Panetone, brigadeiro, bolo de pote ou cesta: monte a ficha de cada produto antes de aceitar as encomendas.</p>'
 '<p>Anote o preço dos ingredientes ou materiais, monte até 5 receitas e veja o custo por unidade, o preço mínimo e o preço de venda, '
 'já com a sua hora, a taxa da maquininha e o lucro. Arquivo .xlsx para Excel ou Google Planilhas, com guia de uso. A calculadora desta página continua grátis.</p>'
 f'<p><a href="{PLANILHA_URL}" rel="nofollow">Comprar a planilha</a></p></aside>'+chr(10)) if PLANILHA_URL else ""

for p in PAGES:
    url=BASE+p["slug"]+"/"
    body=BODY
    body=re.sub(r"<h1>.*?</h1>",lambda m:f"<h1>{p['h1']}</h1>",body,1,flags=re.S)
    body=re.sub(r'<p class="sub">.*?</p>',lambda m:f'<p class="sub">{p["sub"]}</p>',body,1,flags=re.S)
    labs=re.findall(r'<label><span>(.*?)</span><input id="(mat|emb|ene|qtd)"',body,flags=re.S)
    for (old,i),new in zip(labs,p["lab"]):
        body=body.replace(f'<label><span>{old}</span><input id="{i}"',f'<label><span>{new}</span><input id="{i}"',1)
    for i,v in zip(["mat","emb","ene","qtd","hrs","vh","taxa","luc","fixa"],p["vals"]):
        body=re.sub(rf'(id="{i}"[^>]*value=")[^"]*"',lambda m,v=v:f'{m.group(1)}{v}"',body,1)
    body=body.replace("<footer>",f"<article>{p['art']}</article>\n{PLANILHA_HTML}<footer>",1)
    if p.get("extra"): body=body.replace('<label><span>Taxa da maquininha',p["extra"]+'\n<label><span>Taxa da maquininha',1)
    if p.get("script"): body=body.replace("<script>",p["script"]+"\n<script>",1)
    write(p["slug"],head_for(p["title"],p["desc"],url)+body)

SOBRE_DESC="O que é o Precifica, como o cálculo funciona, privacidade e como colocar uma calculadora grátis no seu site ou blog."
EMB_JS=r"""<script>
function codEmb(){const u="https://freitasgoulartgomesa-prog.github.io/precifica/"+document.getElementById("embSel").value;
document.getElementById("embCod").value='<iframe src="'+u+'" width="100%" height="900" style="border:0;max-width:720px" loading="lazy" title="Calculadora Precifica"></iframe>\n<p><a href="'+u+'">Calculadora grátis do Precifica</a></p>';}
function ok(){document.getElementById("embOk").textContent="Copiado!";}
function copiarEmb(){const t=document.getElementById("embCod");t.select();try{navigator.clipboard.writeText(t.value).then(ok,()=>{document.execCommand("copy");ok();});}catch(e){document.execCommand("copy");ok();}}
document.getElementById("embSel").addEventListener("change",codEmb);codEmb();
</script>"""
SOBRE_BODY=f"""<body>
<main>
{NAV}
<h1>Sobre o Precifica</h1>
<article>
<section>
<h2>O que é</h2>
<p>O Precifica reúne calculadoras grátis para quem vende o que faz: doces, bolo de pote, crochê, bijuteria, artesanato e costura. Você preenche os custos, o seu tempo e as taxas, e vê quanto cobrar por unidade.</p>
</section>
<section>
<h2>Como o cálculo funciona</h2>
<p>Primeiro somamos o custo por unidade (material, embalagem e energia) ao valor das suas horas. Esse total é dividido por 1 − taxa − lucro. Assim, a taxa da maquininha e o lucro que você escolheu saem do preço de venda, e não do que sobra para você.</p>
<p>Preço = (custo + horas × valor da hora) ÷ (1 − taxa% − lucro%).</p>
</section>
<section>
<h2>Privacidade</h2>
<p>O site não usa cookies, não tem cadastro e não coleta dados pessoais. Os números que você digita ficam só no seu navegador. Só é aberto um link externo se você clicar em "Enviar no WhatsApp".</p>
</section>
<section>
<h2>Projeto</h2>
<p>Projeto pessoal mantido com ajuda de inteligência artificial e revisado.</p>
</section>
<section id="use-no-seu-site">
<h2>Use no seu site ou blog</h2>
<p>Tem um blog de receitas, uma loja ou um site de artesanato? Pode colocar uma calculadora do Precifica nele, de graça. Escolha a calculadora, copie o código e cole no seu site (no WordPress, use o bloco "HTML personalizado").</p>
<label><span>Calculadora</span><select id="embSel" style="padding:8px;border:1px solid var(--line);border-radius:8px;background:var(--bg);color:var(--ink);font-size:1rem;max-width:200px">
<option value="">Calculadora geral de preço</option><option value="brigadeiro/">Brigadeiro</option><option value="bolo-de-pote/">Bolo de pote</option><option value="panetone/">Panetone</option><option value="croche/">Crochê</option><option value="bijuteria/">Bijuteria</option><option value="shopee/">Shopee</option><option value="quantos-salgados/">Salgados para festa</option><option value="docinhos-e-bolo/">Doces e bolo para festa</option><option value="festa-de-ano-novo/">Festa de Ano Novo</option>
</select></label>
<textarea id="embCod" readonly rows="5" style="width:100%;margin-top:8px;padding:8px;border:1px solid var(--line);border-radius:8px;background:var(--bg);color:var(--ink);font:13px/1.4 ui-monospace,Consolas,monospace"></textarea>
<div class="btns"><button type="button" onclick="copiarEmb()">Copiar código</button><span id="embOk" class="good" style="align-self:center"></span></div>
<p><small>O código mostra a calculadora dentro de uma moldura e mantém um link para o Precifica. Ela continua sem cookies e sem coletar dados.</small></p>
</section>
<section>
<h2>Sugestões</h2>
<p>Achou um erro ou tem uma ideia? <a href="https://github.com/freitasgoulartgomesa-prog/precifica/issues">Abra uma sugestão no GitHub</a>.</p>
</section>
</article>
{FOOTER}
</main>
{EMB_JS}
</body>
</html>
"""
write("sobre",head_for("Sobre o Precifica",SOBRE_DESC,BASE+"sobre/")+SOBRE_BODY)

# ---- Frente 2 (festa): quantos salgados por pessoa ----
SALG_URL=BASE+"quantos-salgados/"
SALG_TITLE="Quantos salgados por pessoa: calculadora para festa"
SALG_DESC="Calcule quantos salgados pedir para a festa: adultos, crianças, duração e horário de refeição. Mostra o total e quantos centos encomendar. Grátis."
SALG_SCRIPT="""<script>
const $=id=>document.getElementById(id);
const n=id=>Math.max(0,parseFloat($(id).value)||0);
let txtWa=null;
function calc(){
  const a=Math.round(n('ad')),c=Math.round(n('cr'));
  const base=a*n('sa')+c*n('sc');
  const fator=1+n('hx')/100*Math.max(0,n('dur')-3)+($('ref').checked?n('rx')/100:0);
  const total=Math.ceil(base*fator-1e-9);
  const pedido=Math.ceil(total/50)*50;
  txtWa=null;$('btnWa').disabled=true;
  if(a+c===0){['rTot','rPed','rPp','rResumo'].forEach(i=>$(i).textContent='—');$('rNota').textContent='Preencha quantos convidados.';return;}
  $('rTot').textContent=total.toLocaleString('pt-BR')+' salgados';
  $('rPed').textContent=pedido.toLocaleString('pt-BR')+' ('+(pedido/100).toLocaleString('pt-BR')+' centos)';
  $('rPp').textContent=(a?(n('sa')*fator).toLocaleString('pt-BR',{maximumFractionDigits:1})+' por adulto':'')+(a&&c?' · ':'')+(c?(n('sc')*fator).toLocaleString('pt-BR',{maximumFractionDigits:1})+' por criança':'');
  $('rNota').textContent=fator>1?'Inclui aumento de '+Math.round((fator-1)*100)+'% pela duração ou pelo horário.':'';
  $('rResumo').textContent='Resumo: '+total.toLocaleString('pt-BR')+' salgados; encomendar '+$('rPed').textContent+'. Detalhes no Resultado, abaixo.';
  txtWa='Festa com '+a+' adultos e '+c+' crianças: '+total+' salgados (encomendar '+pedido+', '+(pedido/100).toLocaleString('pt-BR')+' centos). Calculei no Precifica: '+document.querySelector('link[rel=canonical]').href;
  $('btnWa').disabled=false;
}
function enviarWa(){if(txtWa)window.open('https://wa.me/?text='+encodeURIComponent(txtWa),'_blank','noopener');}
document.querySelectorAll('input').forEach(i=>i.addEventListener('input',calc));calc();
</script>"""
def _inp(i,v,step="1",mn="0"): return f'<input id="{i}" type="number" inputmode="decimal" min="{mn}" step="{step}" value="{v}">'
SALG_BODY=f"""<body>
<main>
{NAV}
<h1>Quantos salgados por pessoa?</h1>
<p class="sub">Numa festa de 2 a 3 horas, conte de <b>10 a 15 salgados por adulto</b> e de <b>5 a 8 por criança</b>. Para 30 adultos e 10 crianças, são cerca de <b>420 salgados: encomende 450</b>. Mude os números abaixo para a sua festa.</p>
<section>
<h2>1. Convidados</h2>
<label><span>Adultos<small>conte adolescentes como adultos</small></span>{_inp("ad",30)}</label>
<label><span>Crianças<small>até uns 10 anos</small></span>{_inp("cr",10)}</label>
<label><span>Duração da festa (horas)</span>{_inp("dur",3,"0.5")}</label>
<label style="display:flex;gap:8px;align-items:center;justify-content:flex-start"><input id="ref" type="checkbox" style="width:auto"> A festa cai no horário de almoço ou jantar e os salgados são a comida principal</label>
</section>
<p class="box good" id="rResumo" aria-live="polite">—</p>
<section>
<h2>2. Premissas (ajuste se quiser)</h2>
<label><span>Salgados por adulto<small>faixa usada pelas fontes: 10 a 15</small></span>{_inp("sa",12)}</label>
<label><span>Salgados por criança<small>faixa usada pelas fontes: 5 a 8</small></span>{_inp("sc",6)}</label>
<label><span>Aumento por hora acima de 3 h (%)<small>estimativa nossa</small></span>{_inp("hx",25)}</label>
<label><span>Aumento no horário de refeição (%)<small>estimativa nossa</small></span>{_inp("rx",20)}</label>
</section>
<section>
<h2>Resultado</h2>
<div class="res" aria-live="polite">
<div class="box big"><small>Salgados para a festa</small><b id="rTot">—</b><span id="rNota"></span></div>
<div class="box"><small>Para encomendar (arredondado para 50)</small><b id="rPed">—</b></div>
<div class="box"><small>Média por pessoa</small><b id="rPp" style="font-size:1.05rem">—</b></div>
</div>
<div class="btns">
<button type="button" id="btnWa" disabled onclick="enviarWa()">Enviar no WhatsApp</button>
<button type="button" class="sec" onclick="window.print()">Imprimir</button>
</div>
<p><small>Faz salgados para vender? <a href="/precifica/">Calcule o preço do cento</a> com ingredientes, embalagem, gás, seu tempo e taxas.</small></p>
</section>
<article>
<p><small>Atualizado em 24/11/2026. Não existe uma regra oficial: as faixas abaixo são as que aparecem em guias de festa como <a href="https://www.decorfacil.com/quantidade-de-salgados-para-festa">Decor Fácil</a>, <a href="https://valorfinal.com.br/calculadora-festa">Valor Final</a> e <a href="https://www.receiteria.com.br/dicas/calculadora-de-docinhos-festa/">Receiteria</a>. Os aumentos por duração e por horário são uma estimativa nossa, que você pode mudar.</small></p>
<h2>Exemplo resolvido: 30 adultos e 10 crianças, 3 horas</h2>
<p>São os números que já vêm preenchidos.</p>
<ul>
<li><b>Adultos:</b> 30 × 12 = 360 salgados.</li>
<li><b>Crianças:</b> 10 × 6 = 60 salgados.</li>
<li><b>Total:</b> 420. Festa de 3 horas fora do horário de refeição: sem aumento.</li>
<li><b>Encomenda:</b> salgado costuma ser vendido por cento, então arredonde para cima: <b>450 (4,5 centos)</b>.</li>
</ul>
<h2>Exemplo 2: almoço de 40 adultos, 4 horas</h2>
<p>Base: 40 × 12 = 480. Aumento: 25% pela hora a mais + 20% pelo horário de almoço = 45%. Total: 480 × 1,45 = <b>696 salgados</b>; encomende <b>700 (7 centos)</b>. Dá cerca de 17 por pessoa, porque nesse caso o salgado é a refeição.</p>
<h2>Tabela de referência para festa</h2>
<table>
<tr><th>O quê</th><th>Por pessoa</th></tr>
<tr><td>Salgados, adulto (festa de 2 a 3 h)</td><td>10 a 15</td></tr>
<tr><td>Salgados, criança</td><td>5 a 8</td></tr>
<tr><td>Docinhos (<a href="/precifica/docinhos-e-bolo/">calcular</a>)</td><td>5 a 7 (cerca de 5 se houver outra sobremesa)</td></tr>
<tr><td>Bolo</td><td>cerca de 100 g (80 a 100 g com outras opções no cardápio)</td></tr>
</table>
<h2>O que faz a conta subir ou descer</h2>
<p><b>Sobe:</b> festa mais longa, perto do almoço ou do jantar, muitos adolescentes, salgados como única comida, convidados que chegam com fome depois do trabalho.</p>
<p><b>Desce:</b> festa curta, muitas crianças pequenas, outras comidas na mesa (cachorro-quente, pizza, churrasco). Nesses casos use o começo da faixa (10 por adulto).</p>
<h2>Erros comuns</h2>
<p><b>Contar criança como adulto.</b> Criança pequena come bem menos; em festa infantil isso muda muito o total.</p>
<p><b>Esquecer quem não confirmou.</b> Some uma margem para quem aparece sem avisar, ou use o fim da faixa.</p>
<p><b>Pedir tudo frito.</b> Misturar fritos e assados agrada mais e ajuda quem não come fritura. A quantidade total é a mesma.</p>
<p><b>Encomendar em cima da hora.</b> Quem faz salgados costuma fechar a agenda do fim de semana com antecedência; peça o orçamento cedo.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quantos salgados para 50 pessoas?</b> Com 50 adultos numa festa de 3 horas: 50 × 12 = 600 salgados (6 centos). Se forem 40 adultos e 10 crianças: 480 + 60 = 540; encomende 550.</p>
<p><b>Quantos salgados para 100 pessoas?</b> Com 100 adultos e 12 por pessoa: 1.200 salgados (12 centos). Use a calculadora se houver crianças ou se a festa for longa.</p>
<p><b>E se o salgado for grande?</b> O salgado de festa costuma ser pequeno, de uma ou duas mordidas. Se for maior (tamanho de lanchonete), conte menos por pessoa.</p>
<p><b>Quanto cobrar pelo cento de salgado?</b> Depende dos seus custos. A <a href="/precifica/">calculadora de preço</a> soma ingredientes, óleo, embalagem, gás, o seu tempo e a taxa, e mostra o preço por unidade; multiplique por 100.</p>
<h2>Outras calculadoras</h2>
<p><a href="/precifica/docinhos-e-bolo/">Quantos docinhos e quanto bolo</a> · <a href="/precifica/">Preço do cento de salgado</a> · <a href="/precifica/brigadeiro/">Quanto cobrar por brigadeiro</a> · <a href="/precifica/bolo-de-pote/">Preço de bolo de pote</a></p>
</article>
{FOOTER}
</main>
"""+SALG_SCRIPT+"""
</body>
</html>
"""
write("quantos-salgados",head_for(SALG_TITLE,SALG_DESC,SALG_URL)+SALG_BODY)

# ---- Frente 2 (festa): docinhos e bolo por pessoa ----
DOCE_URL=BASE+"docinhos-e-bolo/"
DOCE_TITLE="Quantos docinhos e quanto bolo por pessoa: calculadora"
DOCE_DESC="Calcule quantos docinhos encomendar e quantos quilos de bolo pedir para a festa, com ou sem outra sobremesa. Grátis, direto no celular."
DOCE_SCRIPT="""<script>
const $=id=>document.getElementById(id);
const n=id=>Math.max(0,parseFloat($(id).value)||0);
let txtWa=null;
function trocar(){const o=$('outra').checked;$('dp').value=o?5:6;$('gb').value=o?80:100;calc();}
function calc(){
  const p=Math.round(n('pes'));
  const doces=Math.ceil(p*n('dp')-1e-9),pedido=Math.ceil(doces/50)*50;
  const kg=p*n('gb')/1000,kgPed=Math.ceil(kg*2-1e-9)/2;
  const f=v=>v.toLocaleString('pt-BR',{maximumFractionDigits:2});
  txtWa=null;$('btnWa').disabled=true;
  if(p===0){['rDoc','rDocP','rBolo','rBoloP','rResumo'].forEach(i=>$(i).textContent='—');return;}
  $('rDoc').textContent=doces.toLocaleString('pt-BR')+' docinhos';
  $('rDocP').textContent=pedido.toLocaleString('pt-BR')+' ('+f(pedido/100)+' centos)';
  $('rBolo').textContent=f(kg)+' kg';
  $('rBoloP').textContent=f(kgPed)+' kg';
  $('rResumo').textContent='Resumo: encomendar '+pedido.toLocaleString('pt-BR')+' docinhos e '+f(kgPed)+' kg de bolo. Detalhes no Resultado, abaixo.';
  txtWa='Festa com '+p+' convidados: '+pedido+' docinhos ('+f(pedido/100)+' centos) e bolo de '+f(kgPed)+' kg. Calculei no Precifica: '+document.querySelector('link[rel=canonical]').href;
  $('btnWa').disabled=false;
}
function enviarWa(){if(txtWa)window.open('https://wa.me/?text='+encodeURIComponent(txtWa),'_blank','noopener');}
document.querySelectorAll('input').forEach(i=>i.addEventListener('input',i.id==='outra'?trocar:calc));calc();
</script>"""
DOCE_BODY=f"""<body>
<main>
{NAV}
<h1>Quantos docinhos e quanto bolo por pessoa?</h1>
<p class="sub">Conte de <b>5 a 7 docinhos por convidado</b> (6 quando o doce é a única sobremesa) e cerca de <b>100 g de bolo por pessoa</b>. Para 40 convidados: <b>250 docinhos e um bolo de 4 kg</b>. Mude os números para a sua festa.</p>
<section>
<h2>1. Convidados</h2>
<label><span>Total de convidados<small>adultos e crianças: criança também come doce e bolo</small></span>{_inp("pes",40)}</label>
<label style="display:flex;gap:8px;align-items:center;justify-content:flex-start"><input id="outra" type="checkbox" style="width:auto"> Vai ter outra sobremesa (pudim, torta, mesa de frutas)</label>
</section>
<p class="box good" id="rResumo" aria-live="polite">—</p>
<section>
<h2>2. Premissas (ajuste se quiser)</h2>
<label><span>Docinhos por pessoa<small>faixa usada pelas fontes: 5 a 7</small></span>{_inp("dp",6,"0.5")}</label>
<label><span>Bolo por pessoa (gramas)<small>faixa usada pelas fontes: 80 a 100 g</small></span>{_inp("gb",100,"5")}</label>
</section>
<section>
<h2>Resultado</h2>
<div class="res" aria-live="polite">
<div class="box"><small>Docinhos</small><b id="rDoc">—</b></div>
<div class="box"><small>Para encomendar (arredondado para 50)</small><b id="rDocP">—</b></div>
<div class="box"><small>Bolo (conta exata)</small><b id="rBolo">—</b></div>
<div class="box big"><small>Bolo para encomendar (arredondado para meio quilo)</small><b id="rBoloP">—</b></div>
</div>
<div class="btns">
<button type="button" id="btnWa" disabled onclick="enviarWa()">Enviar no WhatsApp</button>
<button type="button" class="sec" onclick="window.print()">Imprimir</button>
</div>
<p><small>Faz doces para vender? <a href="/precifica/brigadeiro/">Calcule o preço do brigadeiro</a> ou o <a href="/precifica/">preço do quilo de bolo</a> com os seus custos.</small></p>
</section>
<article>
<p><small>Atualizado em 24/11/2026. Não existe uma regra oficial: as faixas são as que aparecem em guias de festa como <a href="https://www.receiteria.com.br/dicas/calculadora-de-docinhos-festa/">Receiteria</a>, <a href="https://www.casamentos.com.br/artigos/como-calcular-a-quantidade-de-doces-do-meu-casamento--c5265">Casamentos.com.br</a> e <a href="https://valorfinal.com.br/calculadora-festa">Valor Final</a>. Ao marcar "outra sobremesa", a calculadora usa 5 docinhos e 80 g de bolo por pessoa.</small></p>
<h2>Exemplo resolvido: 40 convidados, só doces e bolo de sobremesa</h2>
<p>São os números que já vêm preenchidos.</p>
<ul>
<li><b>Docinhos:</b> 40 × 6 = 240. Docinho é vendido por cento, então arredonde para cima: <b>250 (2,5 centos)</b>.</li>
<li><b>Bolo:</b> 40 × 100 g = 4.000 g = <b>4 kg</b>.</li>
</ul>
<h2>Exemplo 2: 40 convidados com pudim na mesa</h2>
<p>Com outra sobremesa: 40 × 5 = 200 docinhos (2 centos) e 40 × 80 g = 3,2 kg de bolo. Arredondando para meio quilo: <b>bolo de 3,5 kg</b>.</p>
<h2>Tabela rápida</h2>
<table>
<tr><th>Convidados</th><th>Docinhos (6 por pessoa)</th><th>Bolo (100 g por pessoa)</th></tr>
<tr><td>20</td><td>120 → encomende 150</td><td>2 kg</td></tr>
<tr><td>30</td><td>180 → encomende 200</td><td>3 kg</td></tr>
<tr><td>50</td><td>300</td><td>5 kg</td></tr>
<tr><td>80</td><td>480 → encomende 500</td><td>8 kg</td></tr>
<tr><td>100</td><td>600</td><td>10 kg</td></tr>
</table>
<p>Vai servir salgados também? Veja <a href="/precifica/quantos-salgados/">quantos salgados por pessoa</a>.</p>
<h2>O que faz a conta mudar</h2>
<p><b>Mais doces:</b> festa longa, mesa de doces como atração principal, casamento com doces finos para levar.</p>
<p><b>Menos doces:</b> outra sobremesa, festa curta, muitos convidados que não comem doce.</p>
<p><b>Bolo:</b> bolo com muitas camadas ou recheio pesado rende mais fatias por quilo; bolo só de enfeite (cenográfico) não entra na conta.</p>
<h2>Erros comuns</h2>
<p><b>Somar bolo e docinho como se fossem a mesma coisa.</b> São duas contas: docinho por unidade e bolo por peso.</p>
<p><b>Esquecer as forminhas e as caixas.</b> Para quem encomenda, pergunte se o preço do cento já inclui forminha. Para quem vende, ela entra no custo.</p>
<p><b>Arredondar para baixo.</b> Faltar doce é pior do que sobrar alguns: arredonde a encomenda para cima.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quantos docinhos para 50 pessoas?</b> Com 6 por pessoa, 300 docinhos (3 centos). Com outra sobremesa, 250.</p>
<p><b>Quantos quilos de bolo para 50 pessoas?</b> Cerca de 5 kg, com 100 g por pessoa. Com outras sobremesas, 4 kg.</p>
<p><b>Criança conta como adulto?</b> Para doce e bolo, sim: criança costuma comer tanto quanto adulto.</p>
<p><b>Quantas fatias tem um bolo de 1 kg?</b> Com fatias de 100 g, cerca de 10. É a conta que esta página usa.</p>
<h2>Outras calculadoras</h2>
<p><a href="/precifica/quantos-salgados/">Quantos salgados por pessoa</a> · <a href="/precifica/brigadeiro/">Quanto cobrar por brigadeiro</a> · <a href="/precifica/bolo-de-pote/">Preço de bolo de pote</a></p>
</article>
{FOOTER}
</main>
"""+DOCE_SCRIPT+"""
</body>
</html>
"""
write("docinhos-e-bolo",head_for(DOCE_TITLE,DOCE_DESC,DOCE_URL)+DOCE_BODY)

# ---- Época (Ano Novo): quanto comprar de comida e bebida ----
ANO_URL=BASE+"festa-de-ano-novo/"
ANO_TITLE="Quanto comprar para a festa de Ano Novo: comida, bebida e custo"
ANO_DESC="Calcule quanta carne, cerveja, espumante, refrigerante, água e gelo comprar para a festa de Ano Novo e quanto vai gastar por pessoa. Grátis, sem cadastro."
ANO_SCRIPT="""<script>
const $=id=>document.getElementById(id);
const n=id=>Math.max(0,parseFloat($(id).value)||0);
const R=v=>'R$ '+v.toLocaleString('pt-BR',{minimumFractionDigits:2,maximumFractionDigits:2});
const D=(v,c)=>v.toLocaleString('pt-BR',{maximumFractionDigits:c});
let txtWa=null;
function conta(){
  const ab=Math.round(n('ab')),an=Math.round(n('an')),cr=Math.round(n('cr')),tot=ab+an+cr;
  const ext=1+n('hx')/100*Math.max(0,n('dur')-5);
  const carne=Math.round(((ab+an)*n('ca')+cr*n('cc'))/100)/10;
  const litCerv=ab*n('ce')*ext, latas=Math.ceil(litCerv/0.35-1e-9);
  const garr=Math.ceil(ab/Math.max(1,n('eg'))-1e-9);
  const litRef=((an+cr)*n('rf')+ab*n('rfb'))*ext, garRef=Math.ceil(litRef/2-1e-9);
  const litAg=Math.ceil(tot*n('ag')*ext-1e-9);
  const gelo=Math.ceil((latas*0.35+garRef*2)*n('gl')-1e-9);
  const it=[['Carne ou prato principal',D(carne,1)+' kg',carne*n('pca')],
    ['Cerveja (só maiores de 18)',latas+' latas de 350 ml',latas*n('pce')],
    ['Espumante para o brinde (só maiores de 18)',garr+' garrafas de 750 ml',garr*n('pes')],
    ['Refrigerante ou suco',garRef+' garrafas de 2 L',garRef*n('prf')],
    ['Água',litAg+' L',litAg*n('pag')],
    ['Gelo',gelo+' kg',gelo*n('pgl')],
    ['Acompanhamentos (arroz, farofa, salada, pão)',tot+' pessoas',tot*n('pac')]];
  const total=it.reduce((s,x)=>s+x[2],0);
  return {tot,it,total};
}
function calc(){
  const r=conta();txtWa=null;$('btnWa').disabled=true;
  if(r.tot===0){$('lista').innerHTML='';['rTot','rPp','rResumo'].forEach(i=>$(i).textContent='—');return;}
  $('lista').innerHTML=r.it.map(x=>'<tr><td>'+x[0]+'</td><td>'+x[1]+'</td><td>'+R(x[2])+'</td></tr>').join('');
  $('rTot').textContent=R(r.total);
  $('rPp').textContent=R(r.total/r.tot)+' por pessoa';
  $('rResumo').textContent='Resumo: '+r.tot+' pessoas, gasto de cerca de '+R(r.total)+' ('+R(r.total/r.tot)+' por pessoa). Lista completa abaixo.';
  txtWa='Lista da festa de Ano Novo ('+r.tot+' pessoas):\\n'+r.it.map(x=>'- '+x[0]+': '+x[1]+' ('+R(x[2])+')').join('\\n')+'\\nTotal: '+R(r.total)+' ('+R(r.total/r.tot)+' por pessoa). Calculei no Precifica: '+document.querySelector('link[rel=canonical]').href;
  $('btnWa').disabled=false;
}
function enviarWa(){if(txtWa)window.open('https://wa.me/?text='+encodeURIComponent(txtWa),'_blank','noopener');}
document.querySelectorAll('input').forEach(i=>i.addEventListener('input',calc));calc();
</script>"""
ANO_BODY=f"""<body>
<main>
{NAV}
<h1>Quanto comprar para a festa de Ano Novo?</h1>
<p class="sub">Diga quantas pessoas vão e veja a lista de compras da virada (carne, cerveja, espumante, refrigerante, água e gelo) com o gasto total e por pessoa. Para 18 pessoas, a conta dá cerca de <b>R$ 750, uns R$ 42 por pessoa</b>. Troque os preços pelos do seu mercado.</p>
<section>
<h2>1. Convidados</h2>
<label><span>Adultos que bebem álcool<small>só maiores de 18</small></span>{_inp("ab",10)}</label>
<label><span>Adultos que não bebem álcool</span>{_inp("an",4)}</label>
<label><span>Crianças</span>{_inp("cr",4)}</label>
<label><span>Duração da festa (horas)</span>{_inp("dur",5,"0.5")}</label>
</section>
<p class="box good" id="rResumo" aria-live="polite">—</p>
<section>
<h2>Lista de compras</h2>
<table><thead><tr><th>O quê</th><th>Quanto</th><th>Custo</th></tr></thead><tbody id="lista"></tbody></table>
<div class="res" aria-live="polite">
<div class="box big"><small>Gasto total</small><b id="rTot">—</b></div>
<div class="box"><small>Dividindo por todos</small><b id="rPp" style="font-size:1.05rem">—</b></div>
</div>
<div class="btns">
<button type="button" id="btnWa" disabled onclick="enviarWa()">Enviar a lista no WhatsApp</button>
<button type="button" class="sec" onclick="window.print()">Imprimir</button>
</div>
</section>
<section>
<h2>2. Quantidades por pessoa (ajuste se quiser)</h2>
<label><span>Carne por adulto (g)<small>fontes: 350 a 500 g com acompanhamentos</small></span>{_inp("ca",400,"50")}</label>
<label><span>Carne por criança (g)</span>{_inp("cc",200,"50")}</label>
<label><span>Cerveja por adulto que bebe (L)<small>fontes: 1 a 1,5 L numa festa de 4 a 5 h</small></span>{_inp("ce",1.5,"0.1")}</label>
<label><span>Adultos que bebem por garrafa de espumante<small>1 garrafa dá 5 a 6 taças; 2 taças por pessoa</small></span>{_inp("eg",3)}</label>
<label><span>Refrigerante ou suco por criança ou adulto que não bebe (L)<small>fontes: 0,6 a 1 L</small></span>{_inp("rf",0.6,"0.1")}</label>
<label><span>Refrigerante ou suco por adulto que bebe (L)</span>{_inp("rfb",0.3,"0.1")}</label>
<label><span>Água por pessoa (L)</span>{_inp("ag",0.5,"0.1")}</label>
<label><span>Gelo por litro de bebida (kg)<small>fonte: cerca de 0,5 kg</small></span>{_inp("gl",0.5,"0.1")}</label>
<label><span>Aumento de bebida por hora acima de 5 h (%)<small>estimativa nossa</small></span>{_inp("hx",20)}</label>
</section>
<section>
<h2>3. Preços do seu mercado (R$)</h2>
<label><span>Carne, por kg</span>{_inp("pca",45,"0.01")}</label>
<label><span>Cerveja, por lata de 350 ml</span>{_inp("pce",3.5,"0.01")}</label>
<label><span>Espumante, por garrafa</span>{_inp("pes",30,"0.01")}</label>
<label><span>Refrigerante ou suco, por garrafa de 2 L</span>{_inp("prf",8,"0.01")}</label>
<label><span>Água, por litro</span>{_inp("pag",2,"0.01")}</label>
<label><span>Gelo, por kg</span>{_inp("pgl",3,"0.01")}</label>
<label><span>Acompanhamentos, por pessoa</span>{_inp("pac",6,"0.01")}</label>
</section>
<article>
<p><small>Atualizado em 25/11/2026. Não existe regra oficial: as quantidades são as faixas de guias de festa e churrasco como <a href="https://www.tendaatacado.com.br/dicas/bebidas-para-o-ano-novo/" rel="nofollow">Tenda Atacado</a>, <a href="https://valorfinal.com.br/calculadora-bebidas-festa" rel="nofollow">Valor Final</a> e <a href="https://www.guiadasemana.com.br/restaurantes/noticia/veja-como-calcular-a-quantidade-de-comida-e-bebida-para-um-churrasco" rel="nofollow">Guia da Semana</a>. Os preços são um exemplo: troque pelos do seu mercado. Bebida alcoólica só para maiores de 18 anos. Se beber, não dirija.</small></p>
<h2>Exemplo resolvido: 18 pessoas, 5 horas</h2>
<p>São os números que já vêm preenchidos: 10 adultos que bebem, 4 adultos que não bebem e 4 crianças.</p>
<ul>
<li><b>Carne:</b> 14 adultos × 400 g + 4 crianças × 200 g = 6,4 kg × R$ 45 = R$ 288,00.</li>
<li><b>Cerveja:</b> 10 × 1,5 L = 15 L ÷ 0,35 L = 43 latas (arredondando para cima) × R$ 3,50 = R$ 150,50.</li>
<li><b>Espumante:</b> 10 adultos ÷ 3 = 4 garrafas (arredondando para cima) × R$ 30 = R$ 120,00.</li>
<li><b>Refrigerante ou suco:</b> 8 × 0,6 L + 10 × 0,3 L = 7,8 L = 4 garrafas de 2 L × R$ 8 = R$ 32,00.</li>
<li><b>Água:</b> 18 × 0,5 L = 9 L × R$ 2 = R$ 18,00.</li>
<li><b>Gelo:</b> (43 latas × 0,35 L + 4 garrafas × 2 L) × 0,5 kg = 11,5 kg, arredondando 12 kg × R$ 3 = R$ 36,00.</li>
<li><b>Acompanhamentos:</b> 18 × R$ 6 = R$ 108,00.</li>
</ul>
<p><b>Total: R$ 752,50</b>, ou <b>R$ 41,81 por pessoa</b> se todos dividirem igual.</p>
<h2>Como economizar sem faltar nada</h2>
<p><b>Divida a conta antes da festa.</b> Mande a lista no WhatsApp com o valor por pessoa: cada um sabe quanto vai dar, e ninguém leva o mesmo item duas vezes.</p>
<p><b>Compre gelo e bebida no dia 30.</b> No dia 31 os mercados lotam e o gelo acaba cedo.</p>
<p><b>Troque a carne cara por uma mais barata</b> (frango, linguiça, pernil) e mude o preço por kg na calculadora: o total muda na hora.</p>
<p><b>Quem não bebe álcool</b> costuma tomar mais refrigerante ou suco: por isso a calculadora separa os dois grupos.</p>
<h2>Erros comuns</h2>
<p><b>Comprar espumante para todo mundo.</b> Conte só os adultos que bebem; para as crianças, suco de uva ou sidra sem álcool.</p>
<p><b>Esquecer o gelo.</b> Sem gelo a cerveja e o refrigerante não gelam a tempo. Em dia quente, use o fim da faixa.</p>
<p><b>Comprar para uma festa curta quando ela vai varar a noite.</b> Se a virada passar de 5 horas, coloque a duração real: a bebida aumenta 20% por hora a mais.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quanto de cerveja por pessoa no Ano Novo?</b> Numa festa de 4 a 5 horas, de 1 a 1,5 L por adulto que bebe, cerca de 3 a 4 latas. Festa mais longa ou mais quente pede mais.</p>
<p><b>Quantas garrafas de espumante para 20 pessoas?</b> Se as 20 forem adultos que bebem, com 2 taças cada: 20 ÷ 3 = 6,7, ou seja, 7 garrafas.</p>
<p><b>Quanto de carne por pessoa?</b> De 350 a 500 g por adulto quando há acompanhamentos; criança come cerca da metade.</p>
<p><b>Vai vender comida para o Ano Novo?</b> Use a <a href="/precifica/">calculadora de preço</a> para cobrar a encomenda sem prejuízo, e a de <a href="/precifica/quantos-salgados/">salgados por pessoa</a> para saber quanto fazer.</p>
<h2>Outras calculadoras</h2>
<p><a href="/precifica/quantos-salgados/">Quantos salgados por pessoa</a> · <a href="/precifica/docinhos-e-bolo/">Quantos docinhos e quanto bolo</a> · <a href="/precifica/panetone/">Preço de panetone caseiro</a></p>
</article>
{FOOTER}
</main>
"""+ANO_SCRIPT+"""
</body>
</html>
"""
write("festa-de-ano-novo",head_for(ANO_TITLE,ANO_DESC,ANO_URL)+ANO_BODY)

urls=[BASE]+[BASE+p["slug"]+"/" for p in PAGES]+[SALG_URL,DOCE_URL,ANO_URL,BASE+"sobre/"]
open(os.path.join(ROOT,"sitemap.xml"),"w",encoding="utf-8").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{u}</loc><lastmod>2026-11-24</lastmod></url>\n" for u in urls)+"</urlset>\n")
open(os.path.join(ROOT,"robots.txt"),"w",encoding="utf-8").write("User-agent: *\nAllow: /\nSitemap: "+BASE+"sitemap.xml\n")
print("ok",[p["slug"] for p in PAGES]+["quantos-salgados","docinhos-e-bolo","festa-de-ano-novo","sobre"])
