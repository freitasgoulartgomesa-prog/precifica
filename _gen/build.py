# Gera páginas de nicho e /sobre/ a partir de index.html (rodar com: python -I build.py)
import os, re, html, json
BASE="https://freitasgoulartgomesa-prog.github.io/precifica/"
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src=open(os.path.join(ROOT,"index.html"),encoding="utf-8").read()
HEAD=src[:src.index("<body>")]
BODY=src[src.index("<body>"):]
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
  vals=[22,6,3,25,1.5,15,5,30],
  art="""<h2>Exemplo resolvido: 25 brigadeiros de 20 g</h2>
<p>Os números abaixo são os que já vêm preenchidos na calculadora. São um <b>exemplo</b>: troque pelos valores das suas notas e do seu mercado.</p>
<ul>
<li><b>Ingredientes da panela:</b> R$ 22,00 (leite condensado, chocolate em pó, manteiga e granulado).</li>
<li><b>Forminhas e caixinha:</b> R$ 6,00. <b>Gás e luz:</b> R$ 3,00.</li>
<li><b>Rendimento:</b> a massa pronta pesou 500 g; 500 ÷ 20 g = 25 brigadeiros.</li>
<li><b>Tempo:</b> 1 h 30 min do fogão até a caixinha fechada, a R$ 15 por hora = R$ 22,50.</li>
<li><b>Taxa da maquininha:</b> 5%. <b>Lucro do negócio:</b> 30%.</li>
</ul>
<p><b>A conta:</b> custo por unidade = (22 + 6 + 3) ÷ 25 = R$ 1,24. Tempo por unidade = 22,50 ÷ 25 = R$ 0,90. Total = R$ 2,14.<br>
Preço = 2,14 ÷ (1 − 0,05 − 0,30) = 2,14 ÷ 0,65 = <b>R$ 3,29 por brigadeiro</b>.<br>
Abaixo de R$ 2,25 (2,14 ÷ 0,95) você não paga nem o material e as suas horas depois da taxa.</p>
<h2>Onde está o custo do brigadeiro</h2>
<p><b>Leite condensado e chocolate</b> são quase todo o custo da massa. Trocar o chocolate em pó comum por cacau 50% ou chocolate nobre muda bastante o preço: faça uma conta para cada versão.</p>
<p><b>Cobertura:</b> granulado comum, granulado belga, castanha ou confeito colorido têm custos bem diferentes. Pese quanto vai em cada lote.</p>
<p><b>Forminha:</b> parece pouco, mas no exemplo R$ 6,00 ÷ 25 = R$ 0,24 por unidade, mais que o gás.</p>
<p><b>Rendimento:</b> o jeito mais exato é pesar a massa pronta e dividir pelo peso de cada bolinha. Brigadeiro de 15 g rende mais unidades que o de 20 g com a mesma panela.</p>
<h2>Erros comuns</h2>
<p><b>Multiplicar o custo por 2 ou 3.</b> Essa regra ignora o seu tempo. Enrolar 100 brigadeiros leva horas, e elas precisam estar no preço.</p>
<p><b>Dar desconto grande no cento.</b> Se o desconto for maior que o lucro, você paga para trabalhar. No exemplo, o lucro é 30%; um desconto de 10% no cento ainda deixa margem, um de 35% não.</p>
<p><b>Contar os que você prova ou que quebram.</b> No rendimento entram só os que vão para a caixa.</p>
<p><b>Esquecer a taxa.</b> Cartão, Pix com taxa ou app de entrega ficam com uma parte do preço. Coloque a taxa no campo certo.</p>
<h2>Perguntas frequentes</h2>
<p><b>Quanto cobrar pelo cento de brigadeiro?</b> Multiplique o preço por unidade por 100. No exemplo, 100 × R$ 3,29 = R$ 329. Se quiser dar desconto para festa, veja a regra acima.</p>
<p><b>Brigadeiro gourmet deve custar mais?</b> Sim, porque o ingrediente é mais caro e costuma levar mais tempo para decorar. Preencha a calculadora com os custos da versão gourmet.</p>
<p><b>E a taxa de entrega?</b> Cobre à parte. A calculadora mostra o preço do produto; o frete muda conforme a distância.</p>
<p><b>Quanto vale a minha hora?</b> Divida quanto quer ganhar no mês pelas horas que trabalha. Ex.: R$ 2.000 ÷ 120 h ≈ R$ 16,67 por hora.</p>"""),
 dict(slug="bolo-de-pote",title="Quanto cobrar por bolo de pote: calculadora grátis",
  desc="Calcule o preço do bolo de pote: massa, recheio, pote, colher, gás, seu tempo e taxas. Grátis e sem cadastro.",
  h1="Quanto cobrar por bolo de pote?",
  sub="Preencha os custos de <b>uma fornada</b> (massa + recheios) e quantos potes ela enche.",
  lab=["Massa e recheios<small>farinha, ovos, leite condensado, chocolate, frutas</small>","Potes, tampas, colherzinhas, etiquetas","Gás e luz (estimativa)","Potes que a fornada enche"],
  vals=[45,15,5,12,3,15,5,25],
  art="""<h2>Como fazer a conta do bolo de pote</h2>
<p><b>1. Uma fornada inteira.</b> Some massa e todos os recheios usados. É mais fácil acertar o custo de uma fornada do que de um pote.</p>
<p><b>2. Embalagem pesa.</b> No bolo de pote, pote + tampa + colher pode custar quase tanto quanto o recheio. Não esqueça de nada.</p>
<p><b>3. Tempo:</b> assar, fazer recheio, montar camadas e limpar a cozinha. Tudo isso é trabalho.</p>
<p><b>4. Perdas.</b> Se costuma sobrar pote no fim do dia, conte só os que você vende de fato nas unidades.</p>
<p><b>5. Sabores diferentes, custos diferentes.</b> Ninho com Nutella custa mais que brigadeiro simples. Faça uma conta para cada sabor.</p>
<h2>Quantos potes para ter um salário?</h2>
<p>Olhe o campo "Sobra para você" e divida o quanto quer tirar no mês por esse valor. É uma conta simples que mostra se a meta é possível.</p>"""),
 dict(slug="croche",title="Quanto cobrar por peça de crochê: calculadora grátis",
  desc="Calcule o preço da sua peça de crochê: linha, acessórios, embalagem, horas de trabalho e taxas. Grátis, direto no celular.",
  h1="Quanto cobrar por uma peça de crochê?",
  sub="Preencha os custos de <b>uma peça</b> (ou de um lote, dizendo quantas peças saem).",
  lab=["Linhas e fios<small>conte só a parte do novelo que a peça usa</small>","Acessórios e embalagem<small>enchimento, olhos, botões, saquinho, tag</small>","Luz e outros gastos (estimativa)","Peças feitas com esses materiais"],
  vals=[25,8,1,1,6,12,5,20],
  art="""<h2>Como precificar crochê sem trabalhar no prejuízo</h2>
<p><b>1. Linha usada, não novelo comprado.</b> Se a peça gasta meio novelo de R$ 20, o custo de linha é R$ 10.</p>
<p><b>2. Cronometre.</b> Crochê leva horas. Marque o tempo das primeiras peças de cada modelo; é o número mais importante da conta.</p>
<p><b>3. Valor da sua hora.</b> Uma forma simples: divida quanto quer ganhar no mês pelas horas que pode trabalhar. Ex.: R$ 1.500 ÷ 130 h ≈ R$ 11,50 por hora.</p>
<p><b>4. Acabamento e embalagem contam.</b> Tag, saquinho e enchimento são custo.</p>
<p><b>5. Se o preço assustar,</b> é sinal de que a peça leva muitas horas. Opções: modelos mais rápidos, peças menores, ou vender o diferencial (exclusiva, sob medida) para quem paga mais.</p>
<h2>Sobre a conta</h2>
<p>Esta calculadora tira a taxa e o lucro do preço final (preço = custo ÷ (1 − taxa − lucro)). É o jeito que garante que, depois de pagar a taxa, sobra o lucro que você escolheu.</p>"""),
 dict(slug="bijuteria",title="Quanto cobrar por bijuteria artesanal: calculadora grátis",
  desc="Calcule o preço da sua bijuteria: miçangas, fecho, fio, embalagem, seu tempo e taxas. Grátis, direto no celular.",
  h1="Quanto cobrar por bijuteria artesanal?",
  sub="Preencha os custos de <b>um lote</b> de peças iguais (ex.: 10 pulseiras) e quantas peças saem dele.",
  lab=["Materiais do lote<small>miçangas, pedras, fio, fechos, argolas</small>","Embalagem<small>saquinho, cartela, tag</small>","Outros gastos (estimativa)","Peças que o lote rende"],
  vals=[30,8,2,10,2,12,5,25],
  art="""<h2>Como precificar bijuteria</h2>
<p><b>1. Conte por lote.</b> Comprar miçanga em pacote e usar um pouco em cada peça confunde. Faça 10 peças iguais e divida o custo total por 10.</p>
<p><b>2. Fecho e argola custam.</b> Peças pequenas somam: fecho, terminal, argola e fio podem custar mais que as miçangas.</p>
<p><b>3. Cronometre a montagem.</b> Uma pulseira simples leva minutos; um colar bordado leva horas. O tempo muda tudo.</p>
<p><b>4. Cartela e embalagem vendem.</b> Elas entram no custo, mas ajudam a cobrar mais.</p>
<p><b>5. Feira, loja ou internet?</b> Em loja consignada a loja fica com uma parte; coloque essa parte no campo de taxa.</p>
<h2>Bijuteria x semijoia</h2>
<p>Semijoia tem banho de metal e custo maior por peça. A conta é a mesma: some o custo da peça pronta (incluindo o banho) no campo de materiais.</p>"""),
]

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
    body=body.replace("<footer>",f"<article>{p['art']}</article>\n<footer>",1)
    if p.get("extra"): body=body.replace('<label><span>Taxa da maquininha',p["extra"]+'\n<label><span>Taxa da maquininha',1)
    if p.get("script"): body=body.replace("<script>",p["script"]+"\n<script>",1)
    write(p["slug"],head_for(p["title"],p["desc"],url)+body)

SOBRE_DESC="O que é o Precifica, como o cálculo funciona e por que seus números ficam só no seu navegador."
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
<section>
<h2>Sugestões</h2>
<p>Achou um erro ou tem uma ideia? <a href="https://github.com/freitasgoulartgomesa-prog/precifica/issues">Abra uma sugestão no GitHub</a>.</p>
</section>
</article>
{FOOTER}
</main>
</body>
</html>
"""
write("sobre",head_for("Sobre o Precifica",SOBRE_DESC,BASE+"sobre/")+SOBRE_BODY)

urls=[BASE]+[BASE+p["slug"]+"/" for p in PAGES]+[BASE+"sobre/"]
open(os.path.join(ROOT,"sitemap.xml"),"w",encoding="utf-8").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{u}</loc><lastmod>2026-11-24</lastmod></url>\n" for u in urls)+"</urlset>\n")
open(os.path.join(ROOT,"robots.txt"),"w",encoding="utf-8").write("User-agent: *\nAllow: /\nSitemap: "+BASE+"sitemap.xml\n")
print("ok",[p["slug"] for p in PAGES]+["sobre"])
