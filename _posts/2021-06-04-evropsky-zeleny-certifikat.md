---
layout:     post
title:      "Evropský zelený certifikát"
date:       2021-06-04
categories: Soukromí
comments:   true
tags:       [soukromí, digitalizace]
img:        covidpass.jpg
author:     Ondřej Profant
---

Vláda připravila už druhou verzi zákona k tzv. covidpassům. Ani ta však nevyvrátila pochybnosti o tom, zda je takový zákon vůbec nutný a zda nastavuje podmínky pro používání tohoto certifikátu správně.

<!--more-->

Vláda sama uznala, že její první legislativní předklad covidpassu je špatný, a tak ho stáhla. Je důležité, aby nová verze i z ní plynoucí opatření byly dostatečně odůvodněné - jinak opět hrozí shození Nejvyšším správním soudem jako se to opakovaně stalo v případě epidemiologických opatření ministerstva zdravotnictví.

Evropský zelený certifikát je v pořádku. Sjednocuje pravidla přeshraničního prokazování, a díky tomu zjednodušuje občanům cestování po EU. Zachovává paralelně možnost testování, očkování i období immunity po prodělání nemoci. Jediná škoda je, že nedovoluje použít naměřené protilátky. Navíc ho lze snadno použít v digitální i listinné podobě.

Národní covidpass, tedy použití certifikátu pro různá omezení života v Česku, by měl mít jasná a předem vymezená pravidla. Musí dojít k vyvážení zájmů občanů, ochrany zdraví a zájmů podnikatelů. Každé konkrétní použití covidpassu, jakožto prostředku pro prokázání bezinfekčnosti, musí být dobře odůvodněné.

Existuje mnoho provozů a situací, kde rozhodně není potřeba. Piráti si myslí, že by měl být používán pouze pro **epidemiologicky významné události**, např. pro velké koncerty. V současné době ale nedává smysl ho používat na místech, kde není velké nebezpečí, třeba ve službách, kde se setkávají najednou jen 2 lidé (kadeřník).

Schválení takového mimořádného prostředku musí být časově omezené, proto navrhujeme platnost zákona omezit pouze na následující rok.

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

Vláda nám předložila novou, již druhou, verzi covidpassu jako [sněmovní tisk 1225](https://www.psp.cz/sqw/text/tiskt.sqw?O=8&CT=1225&CT1=0) a [ST 1231](https://www.psp.cz/sqw/text/tiskt.sqw?O=8&CT=1231&CT1=0). Jenže tato úprava legislativy vlastně jen rozšiřuje informační systém infekčních nemocí, tzv. ISIN provozovaný ÚZIS. Ani tato verze nebyla dostatečně odůvodněna, zejména v oblasti sběru dalších osobních údajů. Zejména zmocnění pro sběr rodných čísel v novele tohoto zákona je zarážející - cožpak tento fungující systém rodná čísla již dávno nesbírá?

Největším problémem je, že návrh vůbec neřeší kdy a jak by se měl covidpass použít. Přitom to je zcela klíčové. O této problematice má rozhodovat ministerstvo zdravotnictví. To samé ministerstvo, které rozpustilo MeSES a není ochotno své kroky odborně odůvodnit. Po takových krocích je již důvěra ve vládu nulová, proto požadujeme jasné vymezení možného použití přímo v zákoně. Obáváme se např. situace, kdy ministerstvo bude opětovně zakazovat vstup do lesa (a podmíní vstup certifikátem).

## Aktuální situace

Zákon měl být původně projednán v legislativní nouzi, ale vláda na takový postup neměla dostatek hlasů ve sněmovně. Čeká se tedy na řádné projednání, případně předložení další verze.

Ministerstvo zdravotnictví začalo vydávat certifikáty 1. června na adrese [ocko.uzis.cz](https://ocko.uzis.cz). Tato služba vyvolala velký nápor na Základní registry, které nejsou v dobré kondici a které jsou potřeba pro ověření totožnosti.
