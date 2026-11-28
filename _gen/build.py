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
  desc="Calcule o preço do brigadeiro por unidade: ingredientes, forminha, gás, seu tempo e taxas. Grátis, no celular.",
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
<p><b>Vai vender pavê também?</b> Veja a <a href="/precifica/pave/">calculadora de preço de pavê</a>. Para a ceia da sua casa, use <a href="/precifica/ceia-de-natal/">quanto comprar para a ceia de Natal</a>.</p>
<p><b>Quanto vale a minha hora?</b> Divida quanto quer ganhar no mês pelas horas que trabalha. Ex.: R$ 2.000 ÷ 120 h ≈ R$ 16,67 por hora.</p>"""),
 dict(slug="cesta-de-natal",title="Quanto cobrar por cesta de Natal: calculadora grátis",
  desc="Vai montar cestas de Natal para vender? Calcule o preço de cada cesta: itens, cesta e embalagem, ida ao mercado, seu tempo e taxas. Grátis, no celular.",
  h1="Quanto cobrar por cesta de Natal?",
  sub="Renda extra no Natal montando cestas. Preencha o custo de <b>um lote</b> de cestas iguais e quantas você monta. A conta mostra o preço de cada uma.",
  lab=["Itens de todas as cestas do lote<small>panetone, chocolates, biscoitos, geleia, castanhas, suco</small>","Cestas ou caixas, papel, laço e etiqueta","Ida ao mercado e entrega (estimativa)","Cestas do lote"],
  vals=[290,80,15,5,2.5,15,5,20],
  art="""<h2>Exemplo resolvido: 5 cestas de Natal iguais</h2>
<p>Os números abaixo são os que já vêm preenchidos na calculadora. São um <b>exemplo</b>: troque pelos preços que você pagou.</p>
<ul>
<li><b>Itens de cada cesta:</b> panetone de 500 g R$ 15,00, suco de uva integral R$ 12,00, caixa de bombons R$ 10,00, biscoitos R$ 6,00, geleia R$ 8,00 e 100 g de castanhas R$ 7,00 = R$ 58,00. Para 5 cestas: <b>R$ 290,00</b>.</li>
<li><b>Embalagem:</b> cesta ou caixa R$ 12,00 + papel celofane, laço e etiqueta R$ 4,00 = R$ 16,00 por cesta; 5 cestas = <b>R$ 80,00</b>.</li>
<li><b>Ida ao mercado e entrega:</b> R$ 15,00 para o lote.</li>
<li><b>Tempo:</b> 2,5 h para comprar, montar e embalar as 5, a R$ 15 por hora = R$ 37,50.</li>
<li><b>Taxa da maquininha:</b> 5%. <b>Lucro do negócio:</b> 20%.</li>
</ul>
<p><b>A conta:</b> material por cesta = (290 + 80 + 15) ÷ 5 = R$ 77,00. Tempo por cesta = 37,50 ÷ 5 = R$ 7,50. Total = R$ 84,50.<br>
Preço = 84,50 ÷ (1 − 0,05 − 0,20) = 84,50 ÷ 0,75 = <b>R$ 112,67 por cesta</b> (pode arredondar para R$ 112,90).<br>
Abaixo de R$ 88,95 (84,50 ÷ 0,95) você não paga nem os itens e as suas horas depois da taxa.</p>
<h2>Cesta com itens caseiros</h2>
<p>Se a cesta leva panetone, brigadeiro ou geleia feitos por você, calcule primeiro o custo de cada um (por exemplo na <a href="/precifica/panetone/">calculadora de panetone</a> ou na de <a href="/precifica/brigadeiro/">brigadeiro</a>) e coloque esse custo nos itens. Use o <b>custo</b>, não o preço de venda: o lucro entra uma vez só, no fim.</p>
<h2>Três tamanhos para três bolsos</h2>
<p>No fim de ano muita gente quer presentear, mas com pouco dinheiro. Monte uma cesta pequena, uma média e uma grande e faça uma conta para cada uma. A pequena atrai quem tem pouco para gastar; a grande dá mais lucro por cesta.</p>
<h2>Erros comuns</h2>
<p><b>Somar só o preço dos itens.</b> No exemplo, a embalagem é R$ 16 por cesta, mais de 1/4 do valor dos itens. Cesta, papel e laço precisam estar no preço.</p>
<p><b>Esquecer o seu tempo de compra.</b> Rodar mercados atrás de preço bom leva horas: elas fazem parte do trabalho.</p>
<p><b>Comprar tudo antes de fechar as encomendas.</b> Peça um sinal (por exemplo, metade) na encomenda e compre depois. Assim você não fica com cestas paradas no dia 26.</p>
<p><b>Comprar no varejo quando dá para comprar no atacado.</b> Para 10 cestas ou mais, cote os itens em atacarejo e mude os valores na calculadora: o preço final cai.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quanto cobrar por uma cesta de Natal?</b> Faça a sua conta: no exemplo, uma cesta com 6 itens sai por R$ 112,67. O preço muda muito com os itens; o que não muda é a regra de somar itens, embalagem, tempo e taxa e só depois o lucro.</p>
<p><b>E para empresas?</b> Encomenda grande pede preço por lote. Calcule o lote inteiro aqui (por exemplo, 30 cestas) e ofereça um desconto menor que o seu lucro.</p>
<p><b>Posso colocar bebida alcoólica?</b> Só se o comprador e quem recebe forem maiores de 18, e confira as regras de onde você vende. Suco de uva integral é uma opção para todos.</p>
<p><b>Quanto vale a minha hora?</b> Divida quanto quer ganhar no mês pelas horas que trabalha. Ex.: R$ 2.000 ÷ 120 h ≈ R$ 16,67 por hora.</p>"""),
 dict(slug="pave",title="Quanto cobrar por pavê de Natal: calculadora grátis",
  desc="Vai vender pavê no Natal, em travessa ou pote? Calcule o preço: ingredientes, embalagem, gás, seu tempo e taxas. Exemplo resolvido. Grátis, sem cadastro.",
  h1="Quanto cobrar por pavê de Natal?",
  sub="Pavê é uma das sobremesas mais pedidas na ceia. Preencha os custos de <b>uma receita</b> e quantas unidades ela rende (1 travessa ou vários potes). No exemplo, a travessa de 2 L sai por <b>R$ 105,33</b>.",
  lab=["Ingredientes da receita<small>leite condensado, creme de leite, biscoito, leite, ovos, chocolate</small>","Travessa ou potes, tampa e etiqueta","Gás do fogão (estimativa)","Unidades que a receita rende<small>1 travessa ou número de potes</small>"],
  vals=[48,6.5,2,1,1.5,15,5,20],
  art="""<h2>Exemplo resolvido: pavê de chocolate em travessa de 2 L (12 porções)</h2>
<p>Os números abaixo são os que já vêm preenchidos na calculadora. São um <b>exemplo</b> com preços de mercado comuns: troque pelos valores das suas notas.</p>
<ul>
<li><b>Ingredientes:</b> R$ 48,00 (2 latas de leite condensado R$ 14,00, 2 caixas de creme de leite R$ 7,00, 2 pacotes de biscoito maisena R$ 9,00, 500 ml de leite R$ 2,50, 3 ovos R$ 2,40, 100 g de chocolate em pó R$ 6,00, amido de milho R$ 0,60 e 100 g de chocolate para cobrir R$ 6,50).</li>
<li><b>Embalagem:</b> travessa descartável de 2 L com tampa R$ 6,00 e etiqueta R$ 0,50 = R$ 6,50. <b>Gás:</b> R$ 2,00.</li>
<li><b>Tempo:</b> 1,5 h de trabalho (cremes, montar as camadas, cobrir e embalar), a R$ 15 por hora = R$ 22,50. As horas na geladeira não entram.</li>
<li><b>Taxa da maquininha:</b> 5%. <b>Lucro do negócio:</b> 20%.</li>
</ul>
<p><b>A conta:</b> custo = 48,00 + 6,50 + 2,00 + 22,50 = R$ 79,00.<br>
Preço = 79,00 ÷ (1 − 0,05 − 0,20) = 79,00 ÷ 0,75 = <b>R$ 105,33 a travessa</b>, cerca de R$ 8,78 por porção.<br>
Abaixo de R$ 83,16 (79,00 ÷ 0,95) você não paga nem o material e as suas horas depois da taxa.</p>
<h2>Pavê em pote para vender</h2>
<p>A mesma receita rende uns <b>10 potes de 200 ml</b>. Troque a embalagem por 10 potes com tampa (R$ 1,20 cada) e etiquetas (R$ 2,00) = R$ 14,00, ponha 2 h de trabalho e 10 unidades. A conta: (48 + 14 + 2 + 30) ÷ 10 = R$ 9,40 de custo por pote, preço <b>R$ 12,53 o pote</b>.</p>
<h2>Erros comuns</h2>
<p><b>Esquecer a travessa.</b> Travessa com tampa para entregar custa quase o mesmo que um pacote de biscoito. Se a cliente devolve a travessa de vidro, não cobre; se é descartável, cobre sempre.</p>
<p><b>Cobrar a porção pelo preço do mercado.</b> Pavê de padaria é feito em grande quantidade. O seu é sob encomenda: venda o sabor caseiro e a entrega no dia da ceia.</p>
<p><b>Aceitar encomenda para o dia 24 sem contar a geladeira.</b> Cada travessa precisa de espaço gelado por horas. Veja quantas cabem antes de fechar pedidos.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quanto cobrar por um pavê de travessa?</b> Faça a sua conta: no exemplo, a travessa de 2 L dá R$ 105,33. Sabores com morango, nozes ou chocolate nobre custam mais: some nos ingredientes.</p>
<p><b>Dá para vender pavê como renda extra no Natal?</b> Sim, desde que o preço pague o material, o seu tempo e a taxa. Peça as encomendas com antecedência e um sinal para garantir.</p>
<p><b>Quanto vale a minha hora?</b> Divida quanto quer ganhar no mês pelas horas que trabalha. Ex.: R$ 2.000 ÷ 120 h ≈ R$ 16,67 por hora.</p>
<h2>Outras calculadoras</h2>
<p><a href="/precifica/panetone/">Preço de panetone caseiro</a> · <a href="/precifica/ceia-de-natal/">Quanto comprar para a ceia de Natal</a> · <a href="/precifica/rabanada/">Preço de rabanada</a></p>"""),
 dict(slug="rabanada",title="Quanto cobrar por rabanada: calculadora grátis",
  desc="Vai vender rabanada no Natal? Calcule o preço por unidade e por caixa: pão, leite, ovos, óleo, embalagem, gás, seu tempo e taxas. Grátis.",
  h1="Quanto cobrar por rabanada?",
  sub="Rabanada é doce de Natal fácil de vender por unidade ou em caixa. Preencha os custos de <b>uma fornada</b> e quantas rabanadas ela rende. No exemplo, cada uma sai por <b>R$ 2,36</b> (caixa com 10 por R$ 23,57).",
  lab=["Ingredientes da fornada<small>pão amanhecido, leite, leite condensado, ovos, açúcar, canela, óleo</small>","Bandejas ou caixas, filme e etiqueta","Gás do fogão (fritura)","Rabanadas que a fornada rende"],
  vals=[31.7,6,3,40,2,15,5,20],
  art="""<h2>Exemplo resolvido: 40 rabanadas fritas (4 caixas de 10)</h2>
<p>Os números abaixo são os que já vêm preenchidos na calculadora. São um <b>exemplo</b> com preços de mercado comuns (estimativa nossa): troque pelos valores das suas notas.</p>
<ul>
<li><b>Ingredientes:</b> R$ 31,70 (10 pães franceses amanhecidos R$ 8,00, 1 L de leite R$ 5,00, 1 lata de leite condensado R$ 7,00, 4 ovos R$ 3,20, açúcar e canela R$ 2,50 e a parte do óleo de fritura que se perde R$ 6,00).</li>
<li><b>Rendimento:</b> cada pão cortado em 4 fatias = 40 rabanadas.</li>
<li><b>Embalagem:</b> 4 bandejas com filme e etiqueta a R$ 1,50 = R$ 6,00. <b>Gás:</b> R$ 3,00 (fritura gasta mais que forno).</li>
<li><b>Tempo:</b> 2 h de trabalho (cortar, molhar, fritar, escorrer, passar no açúcar e embalar), a R$ 15 por hora = R$ 30,00.</li>
<li><b>Taxa da maquininha:</b> 5%. <b>Lucro do negócio:</b> 20%.</li>
</ul>
<p><b>A conta por unidade:</b> material = (31,70 + 6,00 + 3,00) ÷ 40 = R$ 1,02; tempo = 30,00 ÷ 40 = R$ 0,75; custo = R$ 1,77.<br>
Preço = 1,7675 ÷ (1 − 0,05 − 0,20) = 1,7675 ÷ 0,75 = <b>R$ 2,36 cada</b>, ou <b>R$ 23,57 a caixa com 10</b>.<br>
Abaixo de R$ 1,86 cada (1,7675 ÷ 0,95) você não paga nem o material e as suas horas depois da taxa.</p>
<h2>Rabanada de forno ou na air fryer</h2>
<p>Sem fritura, quase todo o óleo sai da conta: tire os R$ 6,00 de óleo dos ingredientes e ponha um pouco de manteiga para pincelar (uns R$ 2,00). O gás ou a energia do forno pode subir, porque assa em várias levas. Mude os campos e a calculadora refaz o preço.</p>
<h2>Erros comuns</h2>
<p><b>Esquecer o óleo.</b> O óleo que fica na panela ou é jogado fora é custo da fornada. Em fritura, é um dos itens mais caros depois do leite condensado.</p>
<p><b>Não contar o tempo de fritar.</b> Fritar 40 fatias leva tempo de verdade em pé no fogão: é o seu trabalho e entra no preço.</p>
<p><b>Vender por unidade o mesmo que na caixa.</b> Unidade avulsa pede embalagem própria (saquinho, guardanapo). Some esse custo ou cobre um pouco mais na avulsa.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quanto cobrar pela caixa de rabanada?</b> Faça a conta por unidade e multiplique: no exemplo, a caixa com 10 dá R$ 23,57. Com recheio (doce de leite, creme) ou calda, some nos ingredientes.</p>
<p><b>Dá para vender rabanada como renda extra no Natal?</b> Sim, desde que o preço pague o material, o seu tempo e a taxa. Rabanada é melhor no dia: combine as encomendas para 23 e 24 de dezembro e peça um sinal.</p>
<p><b>Quanto vale a minha hora?</b> Divida quanto quer ganhar no mês pelas horas que trabalha. Ex.: R$ 2.000 ÷ 120 h ≈ R$ 16,67 por hora.</p>
<h2>Outras calculadoras</h2>
<p><a href="/precifica/pave/">Preço de pavê de Natal</a> · <a href="/precifica/panetone/">Preço de panetone caseiro</a> · <a href="/precifica/ceia-de-natal/">Quanto comprar para a ceia de Natal</a> · <a href="/precifica/pao-de-mel/">Preço de pão de mel</a> · <a href="/precifica/trufa/">Preço de trufa</a></p>"""),
 dict(slug="pao-de-mel",title="Quanto cobrar por pão de mel: calculadora grátis",
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
<p><a href="/precifica/panetone/">Preço de panetone caseiro</a> · <a href="/precifica/rabanada/">Preço de rabanada</a> · <a href="/precifica/cesta-de-natal/">Preço de cesta de Natal</a></p>"""),
 dict(slug="trufa",title="Quanto cobrar por trufa: calculadora grátis",
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
<p><a href="/precifica/pao-de-mel/">Preço de pão de mel</a> · <a href="/precifica/brigadeiro/">Preço de brigadeiro</a> · <a href="/precifica/cesta-de-natal/">Preço de cesta de Natal</a></p>"""),
 dict(slug="biscoito-de-natal",title="Preço de biscoito de Natal: calculadora grátis",
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
<p><a href="/precifica/pao-de-mel/">Preço de pão de mel</a> · <a href="/precifica/trufa/">Preço de trufa</a> · <a href="/precifica/cesta-de-natal/">Preço de cesta de Natal</a></p>"""),
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
  desc="Calcule o preço da sua peça de crochê: linha, acessórios, embalagem, horas de trabalho e taxas. Grátis, no celular.",
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
  desc="Calcule o preço da sua bijuteria: miçangas, fecho, fio, embalagem, seu tempo e taxas. Grátis, no celular.",
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
 dict(slug="ifood", title="Calculadora de preço iFood 2026: quanto cobrar com a taxa",
  desc="Quanto cobrar no iFood para não vender no prejuízo: comissão do Plano Básico ou Entrega, taxa de pagamento online, seus custos e lucro. Grátis.",
  h1="Quanto cobrar no iFood?",
  sub="No iFood a comissão é de cerca de <b>12% no Plano Básico</b> (você entrega) ou <b>23% no Plano Entrega</b>, mais cerca de <b>3,2%</b> do pagamento online. Com custo de R$ 14,60 por marmita e 20% de lucro, cobre <b>R$ 27,14</b> no Plano Entrega. Preencha os seus custos.",
  lab=["Ingredientes do lote<small>arroz, feijão, carne, legumes, temperos</small>","Embalagens do lote<small>marmita, tampa, saco, talher, etiqueta</small>","Gás e luz (estimativa)","Porções que o lote rende"],
  vals=[80,15,6,10,3,15,26.2,20],
  art="""<h2>Exemplo resolvido: 10 marmitas no iFood</h2>
<p>Os números abaixo são os que já vêm preenchidos na calculadora. São um <b>exemplo</b>: troque pelos valores das suas notas.</p>
<ul>
<li><b>Ingredientes:</b> R$ 80,00 para 10 marmitas. <b>Embalagens:</b> 10 × R$ 1,50 = R$ 15,00. <b>Gás e luz:</b> R$ 6,00.</li>
<li><b>Tempo:</b> 3 horas de cozinha e montagem a R$ 15 por hora = R$ 45,00.</li>
<li><b>Taxa:</b> 26,2% (23% do Plano Entrega + 3,2% do pagamento online). <b>Lucro:</b> 20%.</li>
</ul>
<p><b>A conta:</b> custo por marmita = (80 + 15 + 6 + 45) ÷ 10 = R$ 14,60.<br>
Preço = 14,60 ÷ (1 − 0,262 − 0,20) = 14,60 ÷ 0,538 = <b>R$ 27,14 por marmita</b>.</p>
<h2>Plano Básico, Plano Entrega ou venda direta?</h2>
<table><tr><th>Onde vende</th><th>Taxa usada</th><th>Preço da mesma marmita</th></tr>
<tr><td>iFood Plano Entrega (o iFood entrega)</td><td>23% + 3,2%</td><td>R$ 27,14</td></tr>
<tr><td>iFood Plano Básico (você entrega)</td><td>12% + 3,2%</td><td>R$ 22,53</td></tr>
<tr><td>WhatsApp com Pix</td><td>0%</td><td>R$ 18,25</td></tr></table>
<p>No Plano Básico a entrega é sua: some o custo do entregador ou da sua moto nos gastos, senão o preço sai baixo demais.</p>
<h2>Erros comuns</h2>
<p><b>Usar no iFood o mesmo preço do balcão.</b> No exemplo, a mesma marmita de R$ 18,25 no Pix precisa custar R$ 27,14 no Plano Entrega para sobrar o mesmo lucro.</p>
<p><b>Somar a taxa no custo em vez de dividir.</b> 14,60 + 46,2% = R$ 21,35 parece certo, mas depois da taxa e do lucro não paga o custo. A conta certa divide.</p>
<p><b>Esquecer a mensalidade.</b> Quem vende mais de R$ 1.800 por mês no iFood paga mensalidade (cerca de R$ 110 no Plano Básico e R$ 150 no Plano Entrega, conforme a fonte). Divida pelo número de pedidos do mês e some no custo.</p>
<h2>Perguntas frequentes</h2>
<p><b>Qual a taxa do iFood em 2026?</b> Cerca de 12% no Plano Básico e 23% no Plano Entrega, mais cerca de 3,2% de pagamento online (algumas fontes dizem 3,5%). Pedido pago em dinheiro na entrega não tem a taxa online. Fontes: <a href="https://www.serasa.com.br/blog/abrir-loja-no-ifood/" rel="nofollow">Serasa</a>, <a href="https://saipos.com/integracoes/ifood/taxa-ifood" rel="nofollow">Saipos</a> e <a href="https://blog.bling.com.br/?p=19386" rel="nofollow">Bling</a>. Confira no Portal do Parceiro antes de fechar o preço.</p>
<p><b>Posso cobrar mais caro no iFood do que no balcão?</b> Muitos restaurantes fazem isso justamente por causa da taxa. Deixe o seu preço de balcão e o do iFood cada um com a sua conta.</p>
<p><b>Quanto vale a minha hora?</b> Divida quanto quer ganhar no mês pelas horas que trabalha. Ex.: R$ 2.000 ÷ 120 h ≈ R$ 16,67 por hora.</p>"""),
 dict(slug="mercado-livre", title="Calculadora de preço Mercado Livre 2026: Clássico ou Premium",
  desc="Quanto cobrar no Mercado Livre com a tarifa do anúncio Clássico ou Premium e o custo fixo de item barato. Seus custos, seu lucro. Grátis.",
  h1="Quanto cobrar no Mercado Livre?",
  sub="No Mercado Livre a tarifa é de <b>10% a 14% no Clássico</b> e de <b>15% a 19% no Premium</b>, conforme a categoria, e item barato paga um <b>custo fixo por unidade</b>. Com custo de R$ 14 por peça e 20% de lucro, cobre <b>R$ 30,15</b> no Clássico. Preencha os seus custos.",
  lab=["Materiais do lote<small>tecido, linha, miçanga, base, tinta</small>","Embalagem de envio<small>saquinho, plástico-bolha, etiqueta, fita</small>","Luz e outros gastos (estimativa)","Peças que o lote rende"],
  vals=[60,15,5,10,5,12,12,20,6.5],
  art="""<p><small>Atualizado em 25/11/2026. A tarifa muda por categoria e o custo fixo de item barato mudou em 2026 (segundo blogs de vendedores, desde março/2026: no Envios Flex e no envio próprio, item abaixo de R$ 79 paga um custo fixo de cerca de R$ 6,25 a R$ 7,75 por unidade; no Full, Coleta e Agência ele virou custo de envio por peso e preço, a partir de cerca de R$ 5,65). O exemplo usa R$ 6,50. Confira no anúncio, na tela "Tarifas", e troque os campos de taxa e taxa fixa.</small></p>
<h2>Exemplo resolvido: 10 peças no anúncio Clássico</h2>
<p>Os números abaixo são os que já vêm preenchidos na calculadora. São um <b>exemplo</b>: troque pelos valores das suas notas.</p>
<ul>
<li><b>Materiais:</b> R$ 60,00 para 10 peças. <b>Embalagem:</b> R$ 15,00. <b>Luz e outros:</b> R$ 5,00.</li>
<li><b>Tempo:</b> 5 horas a R$ 12 por hora = R$ 60,00.</li>
<li><b>Tarifa:</b> 12% (Clássico, meio da faixa) + R$ 6,50 por unidade. <b>Lucro:</b> 20%.</li>
</ul>
<p><b>A conta:</b> custo por peça = (60 + 15 + 5 + 60) ÷ 10 = R$ 14,00.<br>
Preço = (14,00 + 6,50) ÷ (1 − 0,12 − 0,20) = 20,50 ÷ 0,68 = <b>R$ 30,15 por peça</b>.</p>
<h2>A mesma peça em cada canal</h2>
<table><tr><th>Onde vende</th><th>Taxa usada</th><th>Preço da mesma peça</th></tr>
<tr><td>Mercado Livre Clássico</td><td>12% + R$ 6,50</td><td>R$ 30,15</td></tr>
<tr><td>Mercado Livre Premium (parcela sem juros)</td><td>17% + R$ 6,50</td><td>R$ 32,54</td></tr>
<tr><td><a href="/precifica/shopee/">Shopee</a></td><td>20% + R$ 4,50</td><td>R$ 30,83</td></tr>
<tr><td>Venda direta no Pix</td><td>0%</td><td>R$ 17,50</td></tr></table>
<p>O Premium custa mais, mas deixa o cliente parcelar sem juros. Vale para peça cara, em que parcelar decide a compra. Para peça barata, o Clássico costuma bastar.</p>
<h2>Erros comuns</h2>
<p><b>Esquecer o custo fixo em item barato.</b> Numa peça de R$ 30, R$ 6,50 são mais de 20% do preço, além da tarifa.</p>
<p><b>Usar o mesmo preço do Premium e do Clássico.</b> Se anunciar nos dois, cada um precisa da sua conta.</p>
<p><b>Somar a taxa no custo em vez de dividir.</b> A conta certa divide: preço = (custo + taxa fixa) ÷ (1 − taxa − lucro).</p>
<h2>Perguntas frequentes</h2>
<p><b>Qual a tarifa do Mercado Livre em 2026?</b> De 10% a 14% no Clássico e de 15% a 19% no Premium, conforme a categoria, mais um custo fixo ou de envio para itens baratos. Fontes: <a href="https://ecommercenapratica.com/quanto-custa-vender-no-mercado-livre/" rel="nofollow">E-commerce na Prática</a>, <a href="https://viniensina.com.br/?p=4617" rel="nofollow">Vini Ensina</a> e <a href="https://jaguarsheet.com/pt/blog/costo-fijo-mercado-livre" rel="nofollow">Jaguar Sheet</a>. Confira na tela de tarifas do seu anúncio.</p>
<p><b>Vale vender kit?</b> Muitas vezes sim: o custo fixo é por unidade vendida, então um kit de 3 peças paga um só. No exemplo, o kit de 3 sai a (42 + 6,50) ÷ 0,68 = <b>R$ 71,32</b>, ou R$ 23,77 por peça, contra R$ 30,15 avulsa.</p>
<p><b>Quanto vale a minha hora?</b> Divida quanto quer ganhar no mês pelas horas que trabalha. Ex.: R$ 2.000 ÷ 120 h ≈ R$ 16,67 por hora.</p>""")
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
<option value="">Calculadora geral de preço</option><option value="brigadeiro/">Brigadeiro</option><option value="bolo-de-pote/">Bolo de pote</option><option value="panetone/">Panetone</option><option value="cesta-de-natal/">Cesta de Natal</option><option value="croche/">Crochê</option><option value="bijuteria/">Bijuteria</option><option value="shopee/">Shopee</option><option value="quantos-salgados/">Salgados para festa</option><option value="docinhos-e-bolo/">Doces e bolo para festa</option><option value="festa-de-ano-novo/">Festa de Ano Novo</option><option value="ceia-de-natal/">Ceia de Natal</option><option value="pave/">Pavê de Natal</option><option value="rabanada/">Rabanada</option><option value="pao-de-mel/">Pão de mel</option><option value="trufa/">Trufa</option><option value="biscoito-de-natal/">Biscoito de Natal</option>
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
ANO_TITLE="Festa de Ano Novo: quanto comprar de comida, bebida e custo"
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
<p><a href="/precifica/quantos-salgados/">Quantos salgados por pessoa</a> · <a href="/precifica/docinhos-e-bolo/">Quantos docinhos e quanto bolo</a> · <a href="/precifica/panetone/">Preço de panetone caseiro</a> · <a href="/precifica/ceia-de-natal/">Quanto comprar para a ceia de Natal</a></p>
</article>
{FOOTER}
</main>
"""+ANO_SCRIPT+"""
</body>
</html>
"""
write("festa-de-ano-novo",head_for(ANO_TITLE,ANO_DESC,ANO_URL)+ANO_BODY)

# --- Ceia de Natal (Sophia 1, ciclo 30, 27/11/2026) ---
CEIA_URL=BASE+"ceia-de-natal/"
CEIA_TITLE="Quanto comprar para a ceia de Natal: lista e custo"
CEIA_DESC="Calcule quanta carne, arroz, farofa, salada, bebida e panetone comprar para a ceia de Natal e quanto vai gastar por pessoa. Grátis, sem cadastro."
CEIA_SCRIPT="""<script>
const $=id=>document.getElementById(id);
const n=id=>Math.max(0,parseFloat($(id).value)||0);
const R=v=>'R$ '+v.toLocaleString('pt-BR',{minimumFractionDigits:2,maximumFractionDigits:2});
const D=(v,c)=>v.toLocaleString('pt-BR',{maximumFractionDigits:c});
let txtWa=null;
function conta(){
  const ab=Math.round(n('ab')),an=Math.round(n('an')),cr=Math.round(n('cr')),ad=ab+an,tot=ad+cr;
  const carne=Math.ceil((ad*n('ca')+cr*n('ca')*n('cf')/100)/100-1e-9)/10;
  const arroz=Math.ceil(tot*n('ar')/100-1e-9)/10;
  const farofa=Math.ceil(tot/Math.max(1,n('fa'))*10-1e-9)/10;
  const salada=Math.ceil(tot*n('sa')/100-1e-9)/10;
  const garRef=Math.ceil(((an+cr)*n('rf')+ab*n('rfb'))/2-1e-9);
  const vinho=Math.ceil(ab/Math.max(1,n('vg'))-1e-9);
  const pan=Math.ceil(tot/Math.max(1,n('pf'))-1e-9);
  const it=[['Carnes (pernil, tender, peru ou chester)',D(carne,1)+' kg',carne*n('pca')],
    ['Arroz (cru)',D(arroz,1)+' kg',arroz*n('par')],
    ['Farofa pronta',D(farofa,1)+' kg',farofa*n('pfa')],
    ['Salada',D(salada,1)+' kg',salada*n('psa')],
    ['Refrigerante ou suco',garRef+' garrafas de 2 L',garRef*n('prf')],
    ['Vinho ou espumante (só maiores de 18)',vinho+' garrafas de 750 ml',vinho*n('pvi')],
    ['Panetone ou chocotone (500 g)',pan+' unidades',pan*n('ppa')],
    ['Sobremesa (rabanada, pavê)',tot+' pessoas',tot*n('pso')],
    ['Frutas e castanhas',tot+' pessoas',tot*n('pfr')]];
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
  txtWa='Lista da ceia de Natal ('+r.tot+' pessoas):\\n'+r.it.map(x=>'- '+x[0]+': '+x[1]+' ('+R(x[2])+')').join('\\n')+'\\nTotal: '+R(r.total)+' ('+R(r.total/r.tot)+' por pessoa). Calculei no Precifica: '+document.querySelector('link[rel=canonical]').href;
  $('btnWa').disabled=false;
}
function enviarWa(){if(txtWa)window.open('https://wa.me/?text='+encodeURIComponent(txtWa),'_blank','noopener');}
document.querySelectorAll('input').forEach(i=>i.addEventListener('input',calc));calc();
</script>"""
CEIA_BODY=f"""<body>
<main>
{NAV}
<h1>Quanto comprar para a ceia de Natal?</h1>
<p class="sub">Diga quantas pessoas vão e veja a lista de compras da ceia (carnes, arroz, farofa, salada, bebida, panetone e sobremesa) com o gasto total e por pessoa. Para 12 pessoas, a conta dá cerca de <b>R$ 352, uns R$ 29 por pessoa</b>. Troque os preços pelos do seu mercado.</p>
<section>
<h2>1. Convidados</h2>
<label><span>Adultos que bebem álcool<small>só maiores de 18</small></span>{_inp("ab",6)}</label>
<label><span>Adultos que não bebem álcool</span>{_inp("an",3)}</label>
<label><span>Crianças</span>{_inp("cr",3)}</label>
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
<label><span>Carnes por adulto, somando todas (g)<small>fontes: 150 a 250 g</small></span>{_inp("ca",250,"10")}</label>
<label><span>Criança come quanto de um adulto (%)</span>{_inp("cf",50,"5")}</label>
<label><span>Arroz cru por pessoa (g)<small>fonte: 50 g</small></span>{_inp("ar",50,"5")}</label>
<label><span>Pessoas por kg de farofa pronta<small>fonte: 1 kg serve 15</small></span>{_inp("fa",15)}</label>
<label><span>Salada por pessoa (g)<small>fonte: 100 g</small></span>{_inp("sa",100,"10")}</label>
<label><span>Refrigerante ou suco por criança ou adulto que não bebe (L)</span>{_inp("rf",0.6,"0.1")}</label>
<label><span>Refrigerante ou suco por adulto que bebe (L)</span>{_inp("rfb",0.3,"0.1")}</label>
<label><span>Adultos que bebem por garrafa de vinho ou espumante<small>estimativa nossa: 2 taças por pessoa</small></span>{_inp("vg",3)}</label>
<label><span>Pessoas por panetone de 500 g<small>estimativa nossa: 8 fatias</small></span>{_inp("pf",8)}</label>
</section>
<section>
<h2>3. Preços do seu mercado (R$)</h2>
<label><span>Carnes, por kg</span>{_inp("pca",30,"0.01")}</label>
<label><span>Arroz, por kg</span>{_inp("par",6,"0.01")}</label>
<label><span>Farofa pronta, por kg</span>{_inp("pfa",14,"0.01")}</label>
<label><span>Salada, por kg</span>{_inp("psa",12,"0.01")}</label>
<label><span>Refrigerante ou suco, por garrafa de 2 L</span>{_inp("prf",8,"0.01")}</label>
<label><span>Vinho ou espumante, por garrafa</span>{_inp("pvi",30,"0.01")}</label>
<label><span>Panetone de 500 g</span>{_inp("ppa",25,"0.01")}</label>
<label><span>Sobremesa, por pessoa</span>{_inp("pso",5,"0.01")}</label>
<label><span>Frutas e castanhas, por pessoa</span>{_inp("pfr",4,"0.01")}</label>
</section>
<article>
<p><small>Atualizado em 27/11/2026. Não existe regra oficial: as quantidades são as faixas de guias de ceia como <a href="https://www.tudogostoso.com.br/noticias/como-calcular-quantidade-de-comida-a2215.htm" rel="nofollow">TudoGostoso</a>, <a href="https://idec.org.br/consultas/dicas-e-direitos/confira-as-dicas-do-idec-e-economize-nas-compras-para-a-ceia-de-natal" rel="nofollow">Idec</a> e <a href="https://valorfinal.com.br/guia/cardapio-ceia-de-natal" rel="nofollow">Valor Final</a>. Panetone e vinho por pessoa são estimativa nossa. Os preços são um exemplo: troque pelos do seu mercado. Bebida alcoólica só para maiores de 18 anos.</small></p>
<h2>Exemplo resolvido: 12 pessoas</h2>
<p>São os números que já vêm preenchidos: 6 adultos que bebem, 3 adultos que não bebem e 3 crianças.</p>
<ul>
<li><b>Carnes:</b> 9 adultos × 250 g + 3 crianças × 125 g = 2,625 kg, arredondando 2,7 kg × R$ 30 = R$ 81,00.</li>
<li><b>Arroz:</b> 12 × 50 g = 0,6 kg × R$ 6 = R$ 3,60.</li>
<li><b>Farofa:</b> 12 ÷ 15 = 0,8 kg × R$ 14 = R$ 11,20.</li>
<li><b>Salada:</b> 12 × 100 g = 1,2 kg × R$ 12 = R$ 14,40.</li>
<li><b>Refrigerante ou suco:</b> 6 × 0,6 L + 6 × 0,3 L = 5,4 L = 3 garrafas de 2 L × R$ 8 = R$ 24,00.</li>
<li><b>Vinho ou espumante:</b> 6 adultos ÷ 3 = 2 garrafas × R$ 30 = R$ 60,00.</li>
<li><b>Panetone:</b> 12 ÷ 8 = 1,5, arredondando 2 × R$ 25 = R$ 50,00.</li>
<li><b>Sobremesa:</b> 12 × R$ 5 = R$ 60,00. <b>Frutas e castanhas:</b> 12 × R$ 4 = R$ 48,00.</li>
</ul>
<p><b>Total: R$ 352,20</b>, ou <b>R$ 29,35 por pessoa</b> se todos dividirem igual.</p>
<h2>Peru e chester inteiros: compre mais</h2>
<p>As gramas acima são de carne servida. Ave inteira tem osso: um peru de 4 kg serve cerca de 6 pessoas, segundo o TudoGostoso. Se a carne for só peru ou chester, coloque o preço por kg e aumente a quantidade por adulto para uns 600 g.</p>
<h2>Como economizar sem faltar nada</h2>
<p><b>Mais pratos, porção menor.</b> Com duas carnes, a soma das duas fica nos mesmos 250 g por adulto, não 250 g de cada.</p>
<p><b>Divida a conta antes.</b> Mande a lista no WhatsApp com o valor por pessoa e combine quem leva o quê.</p>
<p><b>Compre cedo o que não estraga</b> (arroz, farofa, castanhas, bebida) e deixe carne e salada para os últimos dias.</p>
<h2>Erros comuns</h2>
<p><b>Contar criança como adulto.</b> Criança come cerca da metade: a calculadora já desconta.</p>
<p><b>Somar a porção cheia de cada carne.</b> É o erro que mais sobra comida na ceia.</p>
<p><b>Esquecer a sobremesa e o panetone na conta.</b> Juntos, no exemplo, passam de R$ 100.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quanto de carne por pessoa na ceia de Natal?</b> De 150 a 250 g de carne servida por adulto, somando todas as carnes. Ave inteira com osso pede mais.</p>
<p><b>Quanto de arroz para 20 pessoas?</b> 20 × 50 g = 1 kg de arroz cru.</p>
<p><b>Quanto custa uma ceia de Natal por pessoa?</b> No exemplo, cerca de R$ 29 por pessoa. Muda muito com a carne e a bebida: troque os preços e veja na hora.</p>
<p><b>Vai vender doces ou pratos de Natal?</b> Use a <a href="/precifica/">calculadora de preço</a> para cobrar sem prejuízo, ou as de <a href="/precifica/panetone/">panetone</a>, <a href="/precifica/pave/">pavê</a> e <a href="/precifica/rabanada/">rabanada</a>.</p>
<h2>Outras calculadoras</h2>
<p><a href="/precifica/festa-de-ano-novo/">Festa de Ano Novo</a> · <a href="/precifica/cesta-de-natal/">Preço de cesta de Natal</a> · <a href="/precifica/panetone/">Preço de panetone caseiro</a></p>
</article>
{FOOTER}
</main>
"""+CEIA_SCRIPT+"""
</body>
</html>
"""
write("ceia-de-natal",head_for(CEIA_TITLE,CEIA_DESC,CEIA_URL)+CEIA_BODY)

# --- Festa infantil (Sophia 1, ciclo 23, 26/11/2026) ---
INF_URL=BASE+"festa-infantil/"
INF_TITLE="Festa infantil: quanto comprar por criança e quanto custa"
INF_DESC="Calcule salgados, docinhos, bolo, refrigerante, água e lembrancinhas para a festa infantil, com o gasto total e por criança. Grátis, sem cadastro."
INF_SCRIPT="""<script>
const $=id=>document.getElementById(id);
const n=id=>Math.max(0,parseFloat($(id).value)||0);
const R=v=>'R$ '+v.toLocaleString('pt-BR',{minimumFractionDigits:2,maximumFractionDigits:2});
const D=(v,c)=>v.toLocaleString('pt-BR',{maximumFractionDigits:c});
let txtWa=null;
function conta(){
  const cr=Math.round(n('cr')),ad=Math.round(n('ad')),tot=cr+ad;
  const ext=1+n('hx')/100*Math.max(0,n('dur')-4);
  const salg=Math.ceil((cr*n('sc')+ad*n('sa'))*ext-1e-9);
  const doce=Math.ceil(cr*n('dc')+ad*n('da')-1e-9);
  const bolo=Math.round((cr*n('bc')+ad*n('ba'))/100)/10;
  const garRef=Math.ceil(tot*n('rf')*ext/2-1e-9);
  const litAg=Math.ceil(tot*n('ag')*ext-1e-9);
  const it=[['Salgados',salg+' unidades ('+D(salg/100,1)+' centos)',salg*n('psa')/100],
    ['Docinhos',doce+' unidades ('+D(doce/100,1)+' centos)',doce*n('pdo')/100],
    ['Bolo',D(bolo,1)+' kg',bolo*n('pbo')],
    ['Refrigerante ou suco',garRef+' garrafas de 2 L',garRef*n('prf')],
    ['Água',litAg+' L',litAg*n('pag')],
    ['Lembrancinhas',cr+' unidades',cr*n('ple')],
    ['Descartáveis (prato, copo, guardanapo)',tot+' pessoas',tot*n('pds')]];
  const total=it.reduce((s,x)=>s+x[2],0);
  return {cr,tot,it,total};
}
function calc(){
  const r=conta();txtWa=null;$('btnWa').disabled=true;
  if(r.tot===0){$('lista').innerHTML='';['rTot','rPc','rResumo'].forEach(i=>$(i).textContent='—');return;}
  $('lista').innerHTML=r.it.map(x=>'<tr><td>'+x[0]+'</td><td>'+x[1]+'</td><td>'+R(x[2])+'</td></tr>').join('');
  $('rTot').textContent=R(r.total);
  $('rPc').textContent=(r.cr>0?R(r.total/r.cr)+' por criança · ':'')+R(r.total/r.tot)+' por pessoa';
  $('rResumo').textContent='Resumo: '+r.tot+' convidados ('+r.cr+' crianças), gasto de cerca de '+R(r.total)+'. Lista completa abaixo.';
  txtWa='Lista da festa infantil ('+r.cr+' crianças e '+(r.tot-r.cr)+' adultos):\\n'+r.it.map(x=>'- '+x[0]+': '+x[1]+' ('+R(x[2])+')').join('\\n')+'\\nTotal: '+R(r.total)+'. Calculei no Precifica: '+document.querySelector('link[rel=canonical]').href;
  $('btnWa').disabled=false;
}
function enviarWa(){if(txtWa)window.open('https://wa.me/?text='+encodeURIComponent(txtWa),'_blank','noopener');}
document.querySelectorAll('input').forEach(i=>i.addEventListener('input',calc));calc();
</script>"""
INF_BODY=f"""<body>
<main>
{NAV}
<h1>Quanto comprar para festa infantil?</h1>
<p class="sub">Diga quantas crianças e quantos adultos vão e veja quanto comprar de salgados, docinhos, bolo, bebida e lembrancinhas, com o gasto total. Para 20 crianças e 15 adultos numa festa de 3 horas: <b>270 salgados, 180 docinhos e 3,1 kg de bolo</b>, cerca de <b>R$ 755</b>. Troque os preços pelos da sua região.</p>
<section>
<h2>1. Convidados</h2>
<label><span>Crianças</span>{_inp("cr",20)}</label>
<label><span>Adultos</span>{_inp("ad",15)}</label>
<label><span>Duração da festa (horas)</span>{_inp("dur",3,"0.5")}</label>
</section>
<p class="box good" id="rResumo" aria-live="polite">—</p>
<section>
<h2>Lista de compras</h2>
<table><thead><tr><th>O quê</th><th>Quanto</th><th>Custo</th></tr></thead><tbody id="lista"></tbody></table>
<div class="res" aria-live="polite">
<div class="box big"><small>Gasto total</small><b id="rTot">—</b></div>
<div class="box"><small>Dividindo</small><b id="rPc" style="font-size:1.05rem">—</b></div>
</div>
<div class="btns">
<button type="button" id="btnWa" disabled onclick="enviarWa()">Enviar a lista no WhatsApp</button>
<button type="button" class="sec" onclick="window.print()">Imprimir</button>
</div>
</section>
<section>
<h2>2. Quantidades por pessoa (ajuste se quiser)</h2>
<label><span>Salgados por criança<small>fontes: 5 a 8</small></span>{_inp("sc",6)}</label>
<label><span>Salgados por adulto<small>fontes: 10 a 15</small></span>{_inp("sa",10)}</label>
<label><span>Docinhos por criança<small>fontes: 5 a 7</small></span>{_inp("dc",6)}</label>
<label><span>Docinhos por adulto<small>fontes: 4 a 5</small></span>{_inp("da",4)}</label>
<label><span>Bolo por criança (g)<small>estimativa nossa: fatia menor</small></span>{_inp("bc",80,"10")}</label>
<label><span>Bolo por adulto (g)<small>fontes: cerca de 100 g</small></span>{_inp("ba",100,"10")}</label>
<label><span>Refrigerante ou suco por pessoa (L)<small>fontes: 0,4 a 0,5 L</small></span>{_inp("rf",0.5,"0.1")}</label>
<label><span>Água por pessoa (L)</span>{_inp("ag",0.3,"0.1")}</label>
<label><span>Aumento por hora acima de 4 h (%)<small>salgados e bebidas; fonte: cerca de 10%</small></span>{_inp("hx",10)}</label>
</section>
<section>
<h2>3. Preços da sua região (R$)</h2>
<label><span>Salgados, o cento</span>{_inp("psa",60,"0.01")}</label>
<label><span>Docinhos, o cento</span>{_inp("pdo",100,"0.01")}</label>
<label><span>Bolo, por kg</span>{_inp("pbo",60,"0.01")}</label>
<label><span>Refrigerante ou suco, garrafa de 2 L</span>{_inp("prf",8,"0.01")}</label>
<label><span>Água, por litro</span>{_inp("pag",2,"0.01")}</label>
<label><span>Lembrancinha, cada</span>{_inp("ple",4,"0.01")}</label>
<label><span>Descartáveis, por pessoa</span>{_inp("pds",1.5,"0.01")}</label>
</section>
<article>
<p><small>Atualizado em 26/11/2026. Não existe regra oficial: as quantidades são faixas de guias de festa como <a href="https://www.receiteria.com.br/dicas/calculadora-de-docinhos-festa/" rel="nofollow">Receiteria</a>, <a href="https://valorfinal.com.br/calculadora-festa" rel="nofollow">Valor Final</a> e <a href="https://www.decorfacil.com/quantidade-de-salgados-para-festa" rel="nofollow">Decor Fácil</a>. Os preços são um exemplo: troque pelos da sua região.</small></p>
<h2>Exemplo resolvido: 20 crianças e 15 adultos, 3 horas</h2>
<p>São os números que já vêm preenchidos.</p>
<ul>
<li><b>Salgados:</b> 20 × 6 + 15 × 10 = 270 salgados (2,7 centos) × R$ 60 o cento = R$ 162,00.</li>
<li><b>Docinhos:</b> 20 × 6 + 15 × 4 = 180 docinhos (1,8 cento) × R$ 100 o cento = R$ 180,00.</li>
<li><b>Bolo:</b> 20 × 80 g + 15 × 100 g = 3,1 kg × R$ 60 = R$ 186,00.</li>
<li><b>Refrigerante ou suco:</b> 35 × 0,5 L = 17,5 L = 9 garrafas de 2 L (arredondando para cima) × R$ 8 = R$ 72,00.</li>
<li><b>Água:</b> 35 × 0,3 L = 10,5 L, arredondando 11 L × R$ 2 = R$ 22,00.</li>
<li><b>Lembrancinhas:</b> 20 × R$ 4 = R$ 80,00. <b>Descartáveis:</b> 35 × R$ 1,50 = R$ 52,50.</li>
</ul>
<p><b>Total: R$ 754,50</b>, ou R$ 37,73 por criança convidada (R$ 21,56 por pessoa).</p>
<h2>Como economizar sem faltar nada</h2>
<p><b>Encomende por cento, mas some antes.</b> A conta dá o número exato; arredonde para o cento de cima só se a doceira vender assim.</p>
<p><b>Festa curta no meio da tarde</b> pede menos comida que festa perto do almoço ou do jantar. Se for perto da refeição, aumente os salgados.</p>
<p><b>Lembrancinha feita em casa</b> sai mais barata: troque o preço na calculadora e veja o total mudar na hora.</p>
<h2>Erros comuns</h2>
<p><b>Contar criança como adulto.</b> Criança pequena come bem menos: 20 crianças a 10 salgados dariam 80 salgados a mais que o necessário no exemplo.</p>
<p><b>Esquecer os adultos.</b> Pais e tios que levam as crianças também comem, e costumam comer mais salgado que doce.</p>
<p><b>Comprar só refrigerante.</b> Com calor e criança correndo, a água acaba primeiro. Deixe água à vontade.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quantos salgados por criança?</b> De 5 a 8 numa festa de 2 a 3 horas, conforme a idade. Adolescentes comem como adultos.</p>
<p><b>Quantos docinhos para 30 crianças?</b> Com 6 por criança, 180 docinhos. Some os dos adultos.</p>
<p><b>Quanto bolo para 50 pessoas?</b> Com cerca de 100 g por pessoa, 5 kg. Se metade for criança, cerca de 4,5 kg.</p>
<p><b>Vai fazer os doces para vender?</b> Use a <a href="/precifica/brigadeiro/">calculadora de preço do brigadeiro</a> e a de <a href="/precifica/bolo-de-pote/">bolo de pote</a> para cobrar sem prejuízo.</p>
<h2>Outras calculadoras</h2>
<p><a href="/precifica/quantos-salgados/">Quantos salgados por pessoa</a> · <a href="/precifica/docinhos-e-bolo/">Quantos docinhos e quanto bolo</a> · <a href="/precifica/festa-de-ano-novo/">Festa de Ano Novo</a></p>
</article>
{FOOTER}
</main>
"""+INF_SCRIPT+"""
</body>
</html>
"""
write("festa-infantil",head_for(INF_TITLE,INF_DESC,INF_URL)+INF_BODY)

urls=[BASE]+[BASE+p["slug"]+"/" for p in PAGES]+[SALG_URL,DOCE_URL,ANO_URL,CEIA_URL,INF_URL,BASE+"sobre/"]
open(os.path.join(ROOT,"sitemap.xml"),"w",encoding="utf-8").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{u}</loc><lastmod>2026-11-24</lastmod></url>\n" for u in urls)+"</urlset>\n")
open(os.path.join(ROOT,"robots.txt"),"w",encoding="utf-8").write("User-agent: *\nAllow: /\nSitemap: "+BASE+"sitemap.xml\n")
print("ok",[p["slug"] for p in PAGES]+["quantos-salgados","docinhos-e-bolo","festa-de-ano-novo","ceia-de-natal","festa-infantil","sobre"])
