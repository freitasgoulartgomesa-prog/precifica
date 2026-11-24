# Gera páginas de nicho a partir de um modelo (rodar com: python -I build.py)
import os, re, html
BASE="https://freitasgoulartgomesa-prog.github.io/precifica/"
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src=open(os.path.join(ROOT,"index.html"),encoding="utf-8").read()
css=re.search(r"<style>(.*?)</style>",src,re.S).group(1)
js=re.search(r"<script>(.*?)</script>",src,re.S).group(1)
css+="nav{font-size:.9rem;margin-bottom:8px}nav a{color:var(--accent);margin-right:12px}article h2{margin-top:20px}article{line-height:1.6}"
NAV='<nav><a href="../">Calculadora geral</a><a href="../brigadeiro/">Brigadeiro</a><a href="../bolo-de-pote/">Bolo de pote</a><a href="../croche/">Crochê</a></nav>'
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
<p>Multiplicar o custo dos ingredientes por 2 ou 3 e esquecer do tempo. Quem enrola 100 brigadeiros por dia trabalha horas; se o preço não paga essas horas, o negócio só parece dar lucro.</p>"""),
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
<p>Olhe o campo "Você recebe limpo por unidade" e divida o quanto quer tirar no mês por esse valor. É uma conta simples que mostra se a meta é possível.</p>"""),
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
]
ids=["mat","emb","ene","qtd","hrs","vh","taxa","luc"]
for p in PAGES:
    body=src.split("<body>",1)[1].split("<script>",1)[0]
    body=body.replace("<main>","<main>\n"+NAV,1)
    body=re.sub(r"<h1>.*?</h1>",f"<h1>{p['h1']}</h1>",body,1,re.S)
    body=re.sub(r'<p class="sub">.*?</p>',f'<p class="sub">{p["sub"]}</p>',body,1,re.S)
    labs=re.findall(r'<label><span>(.*?)</span><input id="(mat|emb|ene|qtd)"',body)
    for (old,i),new in zip(labs,p["lab"]):
        body=body.replace(f'<label><span>{old}</span><input id="{i}"',f'<label><span>{new}</span><input id="{i}"',1)
    for i,v in zip(ids,p["vals"]):
        body=re.sub(rf'(id="{i}"[^>]*value=")[^"]*"',rf'\g<1>{v}"',body,1)
    body=body.replace("<footer>",f"<article>{p['art']}</article>\n<footer>",1)
    url=BASE+p["slug"]+"/"
    out=f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p['title']}</title>
<meta name="description" content="{html.escape(p['desc'])}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{html.escape(p['title'])}">
<meta property="og:description" content="{html.escape(p['desc'])}">
<meta property="og:url" content="{url}">
<style>{css}</style>
</head>
<body>{body}<script>{js}</script>
</body>
</html>
'''
    d=os.path.join(ROOT,p["slug"]); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,"index.html"),"w",encoding="utf-8").write(out)
urls=[BASE]+[BASE+p["slug"]+"/" for p in PAGES]
open(os.path.join(ROOT,"sitemap.xml"),"w",encoding="utf-8").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{u}</loc><lastmod>2026-11-23</lastmod></url>\n" for u in urls)+"</urlset>\n")
open(os.path.join(ROOT,"robots.txt"),"w",encoding="utf-8").write("User-agent: *\nAllow: /\nSitemap: "+BASE+"sitemap.xml\n")
print("ok",[p["slug"] for p in PAGES])
