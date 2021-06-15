---
layout:     post
title:      "Digitální COVID certifikát EU"
date:       2021-06-09
categories: Soukromí
comments:   true
tags:       [soukromí, digitalizace]
img:        covidpass.jpg
author:     Ondřej Profant
---

Vláda sama uznala, že její [první legislativní předklad](https://www.psp.cz/sqw/text/tiskt.sqw?O=8&CT=1225&CT1=0) covid pasu je špatný, a tak ho raději stáhla. Ani 2. verze vládního návrhu zákona nebyla o mnoho lepší, proto jsme ji 9. června na půdě sněmovny nepodpořili. Podle nás není takový návrh totiž vůbec potřebný.

<!--more-->

----------------------------------------------------------------------------------

## Oficiální stanovisko Pirátů a Starostů a koalice SPOLU

*K tématu se sešla dne 8. 6. 2021 naše koalice Pirátů a Starostů se zástupci koalice Spolu a shodli jsme se na následujícím podrobnějším shrnutí situace ve složení Ondřej Profant, Olga Richterová, Vít Rakušan, Marek Benda, Martin Kupka, Vlastimil Válek, Vít Kaňkovský:*

Evropská unie vydala [nařízení](https://data.consilium.europa.eu/doc/document/ST-9038-2021-INIT/en/pdf) o covid pasu, který opravňuje k bezproblémovému cestování napříč Evropou. Cílem je zabránit chaosu, kdy by na hranicích s různými zeměmi platila různorodá pravidla a bylo by obtížné se vyznat v tom, jaký dokument mám jako cestující kde ukázat a jaký dokument mám jako úředník uznat.

**Co certifikát zvaný covid pas osvědčuje?**   
Evropské nařízení specifikuje tyto důvody k vydání certifikátu:
- očkování proti Covid-19
- test prokazující bezinfekčnost
- prodělaná nemoc v určitém časovém intervalu (u prodělané nemoci není specifikované, jak se má prokazovat - může to být PCR testem, který byl pozitivní, nebo to může být z logiky věci protilátkami, které ukazují imunitní odpověď na setkání s patogenem)

Prakticky jde o omezený výpis ze zdravotní dokumentace, který pokrývá pouze oblast spojenou s jednou nemocí - Covid 19 - a prokazování bezinfekčnosti. Ve zdravotní dokumentaci každého člověka jsou zanesena i jiná očkování či prodělané nemoci, tyto ale v covidpasu nijak uvedeny nebudou

**Co je cílem tohoto certifikátu?**  
Cílem je jednoduše prokazovat bezinfekčnost na hranicích. Na základě tohoto certifikátu budete moci překročit hranice v rámci Schengenu a dalších přidružených států a nedělat si např. speciální testy kvůli cestování. Má to tedy být služba státu pro občany, kteří chtějí snadno cestovat.

**Jaká má být podoba certifikátu?**  
Prakticky se jedná o dokument s QR kódem, který může mít digitální i listinnou podobu. Jelikož tento výpis je osvědčením o bezinfekčnosti, může se opírat o různé způsoby jejího prokázání (očkováním, proděláním nemoci a protilátkami, či negativním testem). Srozumitelným usnadněním je jednotná zelená
barva prokazující bezinfekčnost.

**Jak má v souladu se zákonem tento certifikát fungovat v ČR? Toto chceme:**  
- Díky zákonu o právu na digitální službu mají lidé už dnes právo na přístup ke službám státu v digitální i listinné podobě.
- Výpis ze zdravotní dokumentace, což covid certifikát je, je takovou službou.
- Aby byla dostupná i občanům, co nemají možnost si certifikát sami stáhnout z webu [ocko.uzis.cz](https://ocko.uzis.cz/), je třeba ji nařízením vlády zařadit do katalogu služeb, které poskytuje Czech POINT.
- Technické řešení na Czech pointech je implementovatelné v řádu jednoho měsíce, protože se jedná o standardní a otestovanou formu publikace dat v rámci veřejné správy.
- Další možností, jak covid certifikát získat, je samozřejmě výpis ze zdravotnické dokumentace od praktického lékaře či zdravotnického zařízení (očkovacího místa), ale je nadbytečné je zatěžovat touto úřední činností.

**Jak budeme ČR bránit před epidemií?**  
Epidemie tu s námi stále je, mutace viru nás stále mohou ohrozit. Zvláště pak mutace Delta. Proto je třeba zaměřit se na efektivní boj s nebezpečnými mutacemi. Je potřeba rychle a přesně trasovat a v případě prokázání nákazy se nebát izolovat ohniska. V momentě, kdy virus zastavíme v počátku, minimalizujeme škody. Preventivně je třeba zachovat dostatečnou testovací kapacitu (pro případ mutací) a kapacitu na sekvenování (tedy záchyt mutací viru).

----------------------------------------------------------------------------------

## Technicky

Technicky na tom není nic složitého. Veškerá potřebná data jsou zašifrována v QR kódu. Ten může být v listinné podobě (papír), anebo digitálně. Aplikace na mobilu ověřovatele pak snadno zjistí, zda daný člověk splnil, či nesplnil podmínky (ale nic víc). Co stát musí udělat proto, aby to vše fungovalo:

- legislativní podklad (aby i soukromý subjekt, třeba pořadatel koncertu, měl právo kontrolovat účastníky)
- proces vydávání QR kódů
  - ČR zvolila zcela centralizovaný způsob, kdy všechny certifikáty vydává přímo ministerstvo zdravotnictví (prostřednictvím ÚZIS)
  - Nabízí se robustnější možnost derivovat podpisové certifikáty a ty vydávat jednotlivým lékařským zařízením.
- jednoduchá aplikace, která řekne ANO/NE při přečtený daného QR kódu, v kterém je zašifrovaná informace
- vše se provádí offline lokálně (stát ani nikdo jiný nemůže sledovat na jakou akci zrovna jdu)

Specifikaci [nalezneme na Githubu](https://github.com/eu-digital-green-certificates/dgc-overview).


## Co nám vláda předložila

Vláda nám předložila novou, již druhou, verzi covid pasu jako [sněmovní tisk 1231](https://www.psp.cz/sqw/text/tiskt.sqw?O=8&CT=1231&CT1=0). Jenže tato úprava legislativy vlastně jen rozšiřuje informační systém infekčních nemocí, [tzv. ISIN provozovaný ÚZIS](https://www.zakonyprolidi.cz/cs/2000-258#p75a). Ani tato verze nebyla dostatečně odůvodněna, zejména v oblasti sběru dalších osobních údajů. Zejména zmocnění pro sběr rodných čísel v novele tohoto zákona je zarážející - cožpak tento fungující systém rodná čísla již dávno nesbírá?

Největším problémem je, že návrh vůbec neřeší kdy a jak by se měl covid pas použít. Přitom to je zcela klíčové.  Musí dojít k vyvážení zájmů občanů, ochrany zdraví a zájmů podnikatelů. Každé konkrétní použití covid pasu, jakožto prostředku pro prokázání bezinfekčnosti, musí být dobře odůvodněné. O této problematice má rozhodovat ministerstvo zdravotnictví. To samé ministerstvo, které rozpustilo MeSES a není ochotno své kroky odborně odůvodnit. Po takových krocích je již důvěra ve vládu nulová, proto požadujeme jasné vymezení možného použití přímo v zákoně. Obáváme se např. situace, kdy ministerstvo bude opětovně zakazovat vstup do lesa (a podmíní vstup certifikátem). Piráti si myslí, že by měl být používán pouze pro **epidemiologicky významné události**, např. pro velké koncerty. V současné době ale nedává smysl ho používat na místech, kde není velké nebezpečí, třeba ve službách, kde se setkávají najednou jen 2 lidé (kadeřník). Je důležité, aby případná opatření byla dostatečně odůvodněná - jinak opět hrozí shození Nejvyšším správním soudem jako se to opakovaně stalo v případě epidemiologických opatření ministerstva zdravotnictví.

Národní covid pas, tedy použití certifikátu pro různá omezení života v Česku, by měl mít jasná a předem vymezená pravidla, včetně omezené doby platnosti pouze na následující rok.
