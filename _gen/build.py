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
    h=re.sub(r'<script type="application/ld\+json">.*?</script>',lambda m:f'<script type="application/ld+json">{ld}</script>\n'+og,h,1,flags=re.S)
    return h

def write(slug,content):
    d=os.path.join(ROOT,slug) if slug else ROOT
    os.makedirs(d,exist_ok=True)
    open(os.path.join(d,"index.html"),"w",encoding="utf-8").write(content)

PAGES=[
 dict(slug="brigadeiro",title="Quanto cobrar por brigadeiro: calculadora grátis",
  desc="Calcule o preço do brigadeiro por unidade: ingredientes, forminha, gás, seu tempo e taxas. Grátis, direto no celular.",
  h1="Quanto cobrar por brigadeiro?",
  sub="Preencha os custos de <b>uma receita</b> (uma panela) e quantos brigadeiros ela rende. A conta mostra o preço por unidade.",
  lab=["Ingredientes da receita<small>leite condensado, chocolate, manteiga, granulado</small>","Forminhas, caixinha, etiqueta","Gás e luz (estimativa)","Brigadeiros que a receita rende"],
  vals=[22,6,3,25,1.5,15,5,30],
  art="""<h2>Passo a passo para precificar brigadeiro</h2>
<p><b>1. Custo da receita.</b> Some o que você pagou em tudo o que entra na panela. Se usou só meia lata de creme de leite, conte só a metade do preço.</p>
<p><b>2. Rendimento real.</b> Conte quantos brigadeiros saíram de verdade, no tamanho que você vende (ex.: 15 g ou 20 g). Os que você prova ou que quebram não entram.</p>
<p><b>3. Seu tempo vale dinheiro.</b> Enrolar dá trabalho. Marque no relógio quanto tempo leva do fogão até a caixinha fechada.</p>
<p><b>4. Taxas.</b> Maquininha, Pix com taxa, iFood ou marketplace: a taxa sai do preço, então ela já entra na conta.</p>
<p><b>5. Compare com a sua região.</b> A calculadora mostra o preço que paga tudo. Se o mercado da sua cidade cobra menos, veja onde dá para baixar custo (comprar no atacado, receita maior) antes de baixar o preço.</p>
<h2>Erro mais comum</h2>
<p>Multiplicar o custo dos ingredientes por 2 ou 3 e esquecer do tempo. Quem faz 100 brigadeiros por dia trabalha horas; se o preço não paga essas horas, o negócio só parece dar lucro.</p>"""),
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
    for i,v in zip(["mat","emb","ene","qtd","hrs","vh","taxa","luc"],p["vals"]):
        body=re.sub(rf'(id="{i}"[^>]*value=")[^"]*"',lambda m,v=v:f'{m.group(1)}{v}"',body,1)
    body=body.replace("<footer>",f"<article>{p['art']}</article>\n<footer>",1)
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
