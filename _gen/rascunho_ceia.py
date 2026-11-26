# RASCUNHO (Sophia 1, ciclo 25, 26/11/2026) - publicar em 27/11 (limite de 3 páginas de 26/11 já usado).
# Como publicar: colar este bloco no build.py antes de "# --- Festa infantil", pôr CEIA_URL em urls (sitemap) e no print,
# pôr a opção "ceia-de-natal/" no <select> do menu e um link em "Outras calculadoras" de /festa-de-ano-novo/ e /panetone/.
# Exemplo padrão (12 pessoas) conferido à mão: total R$ 352,20, R$ 29,35 por pessoa (ver EXEMPLO abaixo e teste com node).
# Fontes das quantidades: TudoGostoso, IDEC, Valor Final (links na página). Panetone 8 fatias e vinho 1 garrafa/3 adultos: estimativa nossa.

CEIA_URL=BASE+"ceia-de-natal/"
CEIA_TITLE="Quanto comprar para a ceia de Natal: lista por pessoa e custo"
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
<p><b>Vai vender ceia ou pratos de Natal?</b> Use a <a href="/precifica/">calculadora de preço</a> para cobrar sem prejuízo, e a de <a href="/precifica/panetone/">preço de panetone</a> se for vender panetone.</p>
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
