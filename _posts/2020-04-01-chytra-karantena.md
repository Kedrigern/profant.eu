---
layout:     post
title:      "Chytrá karanténa"
date:       2020-04-01
categories: Bezpečnost
comments:   true
tags:       [Bezpečnost, Zdraví]
img:        chytra-karantena.jpg
author:     Ondřej Profant
---

Chytrá karanténa je skloňována ve všech mediích a denně o ní slyšíme od náměstka ministra zdravotnictví a bývalého předsedy ústřeního krizového štábu Romana Prymuly. Pojďme si říct, co to doopravdy je, s čím nám pomůže a jaká má naopak úskalí. Zvláště se zaměříme na ochranu soukromí.

<!--more-->

## O co se jedná?

Situaci nejlépe popíšeme na ukázkovém příkladu. 

1. Vezměme si fiktivního Jana Nováka. Projeví se u něj symptomy (horečka, kašel) a nechá se otestovat. 
2. Jeho test vyjde pozitivní, je tedy nakažen onemocněním Covid-19. O tom je informován pomocí SMS.
3. Od momentu, kdy to Novák zjistí, je v klasické **domácí karanténě**.
4. Janu Novákovi závolají z call centra hygieniků, které připravila skupina [Covid19CZ](https://covid19cz.cz). Ta si dala za cíl bojovat daty a informačními technologiemi proti pandemii.
5. Vyškolený pracovník se Nováka zeptá, zda chce (dává informovaný souhlas) vytvořit **vzpomínkovou mapu pohybu**. Je třeba zkoumat cca 5 dní zpětně.
6. Pokud pan Novák **souhlasí**, pracovník hygieny dostane data od mobilního operátora (triangulace na základě BTS) a data od bank. Díky tomu uvidí, kde se pohyboval s mobilem a kde platil. Díky těmto informací bude snazší sestavit mapu pohybu nakaženého pana Nováka a identifikovat, kde mohl koho nakazit.
7. Pokud pan Novák **neudělí souhlas**, tak se pracovník hygieny bude ptát "kde jste byl včera", "s kým jste přišel do styku" apod. a nebude mít žádné vodítko. Vědomé lhaní o nakažlivých nemocech je postižitelné.
8. Hygiena takto sestaví mapu pohybu a kontaktů nakaženého. Následně se pokusí kontaktovat ohrožené jedince (napříkald člověk, s kterým byl pan Novák 4h v jedné místnosti apod.). K tomuto kontaktovní hygiena nedostane žádná data od mobilních operátorů, v případě souhlasu je k dispozici jen vzpomínková mapa.

Tohle je základní a nejdůležitější proces. Vidíme z něj, že Chytrá karanténa se opírá o běžnou domácí karanténu. Sama o sobě nám pouze usnadňuje hledání nakažených. Další informace naleznete na [oficiálním webu](https://covid19cz.cz/covid19-cz/manifest/chytra-karantena).

### Další aplikace

Dílčí součastí Chytré karantény jsou také mobilní aplikace **Mapy.cz** a eRouška. První jmenovaná je dobře známá a má v ČR mnoho uživatelů. Ta vám opět nabídne možnost dobrovolně sledovat polohu. Tu sleduje na základě GPS a Wifi. 

Aplikace **eRouška** funguje na základě technologie bluetooth. Skrze bluetooth zkoumá, zda jsou po okolí další přístroje s touto aplikací. V případě, že držitel zjistí, že je roznašeč, následuje proces vyhodnocení, s kým vším se potkal a zda to setkání mělo vyšší pravděpodobnost přenosu (byli spolu déle). Samozřejmě aplikace opět není povinná a funguje jen, když máte zapnutý bluetooth. Skvělé na této aplikaci je, že se nejedná o black box. Její [**zdrojový kód je zveřejněn**](https://github.com/covid19cz/).

### Kdo to vše provozuje?

Vzpomínkovou mapu provozuje Ministertsvo zdravotnictví, v call centru jsou hygienici a vyškolení medici a software vyvinula skupina [Covid19CZ](hhttps://covid19cz.cz). Vše audituje PWC. Osobně doufám, že vše ještě zkontroluje i ÚOOÚ.

Aplikace Mapy.cz je od společnosti Seznam.cz. Aplikace eRouška teprve vzniká.

### Role armády

V mediích často slyšíme, že pomáhá armáda. To může znít jako velmi děsivé sdělení. Nicméně armáda slouží hlavně jako logistická pomoc. Jezdí odebírat vzorky od potenciálních nakažených, staví odběrová místa a dalšími způsoby pomáhá v postižené oblasti. U případů, kde to jinak nejde, může vozit nákup lidem v karanténě. 

Též pomáháhá ve vnitřní logistice státu, kterou nevidíme.

## Výhrady Pirátů

Současnou verzi Chytré karantény podporujeme, protože je založena na dobrovolnosti a respektu k soukromí jednotlivce. Avšak je třeba varovat před neopatrným rozšiřováním či zasahováním do současného systému. Další problémy jsou:

- **Efektivnost**: Je třeba si uvědomit, že nás ochrání jen důsledné dodržování hygienických pravidel. Chytrá karanténa nám pomůže rychleji odhalit kontakty, které by mohly vést k nákaze. Ale rozhodně nám nepomůže například proti nákaze od infikované kliky či tlačítka výtahu.
- **Reakce vlády**: Pokud opravdu Chytrá karanténa nezabrání opětovnému masovému šíření, vláda bude muset reagovat. My se bojíme, aby nešla cestou likvidace soukromí občanů.
- **Black box**: Aplikace vzpomínkové mapy ani další aplikace nejsou opensource. Jedná se o blackbox, u kterého odborná veřejnost nemůže ověřit, zda opravdu dělá jen to, co nám říkají tvůrci. Další problém může být, co se stane, až situace pomine. Toto je třeba hlídat. Jedinou výjimkou je aplikace eRouška.
- **Ostrakizace**: Nezanedbatelné riziko jsou útoky proti lidem, kteří souhlas nedají. Je třeba si uvědomit, že tito lidé nic špatného nedělají a nemoc nešíří vědomě. Špatné je, pokud někdo nedodržuje hygienická pravidla (kašle bez zakrytí obličeje, nenosí roušku) či odmítne spolupracovat s hygienikem - to však může i bez šmírování.
- **Kontrola**: Celý systém musí být pod důslednou kontrolou. Audit PWC je nezbytné minimum. Jak už jsem zmínil, je jistě důležité, aby se k věci vyjádřil i ÚOOÚ. Piráti budou požadovat i kontrolu ze strany sněmovní komise.

Stejně jako omezení pohybu jsou zásahy do soukromí velmi nebezpečný precedent. Musíme k nim přistupovat po velmi pečlivé úvaze a vždy jen na jasně omezenou dobu. Naštěstí u nás je vše na dobrovolné bázi narozdíl od mnoha jiných zemí. Podrobnější rozepsání obav naleznete v článku [Daniela Dočekala](https://www.lupa.cz/clanky/inteligentni-karantena-vzdavame-se-kvuli-koronaviru-soukromi/).
