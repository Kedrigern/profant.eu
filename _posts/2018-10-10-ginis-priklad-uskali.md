---
layout:     post
title:      "GINIS+ na MHMP: Příklad úskalí české digitalizace"
date:       2018-10-10 19:00:00 +0100
categories: Egovernment
comments:   true
tags:       [egovernment, digitalizace, informatika, veřejná správa]
img:        ginis.jpg
author:     Ondřej Profant
---

Správný přístup k přípravě a vypisování veřejných zakázek je pro státní správu a samosprávy důležitý nejen v oblasti digitalizace a egovernmentu. Veřejné zakázky na informační a komunikační technologie patří v ČR ale k nejvíce problematickým. V tomto článku podrobněji popíšu jeden konkrétní odstrašující příklad z nedávné minulosti, zároveň se pokusím nabídnout i pozitivní vizi možné alternativy.

<!--more-->

### Rámcová smlouva pro nákup rozvojových prací GINIS+

Zmíněný negativní příklad se týká veřejné zakázky Magistrátu hlavního města Prahy. Ten v červenci uzavřel smlouvu ([uveřejněnou v registru smluv dne 20. 7. 2018](https://www.hlidacstatu.cz/Detail/6205167)) o nákupu rozvojových prací na platformě GINIS+ v rozsahu až 30 milionů Kč ročně. Tato platforma se využívá pro provoz informačních systémů spisové služby (ESSS) a ekonomických systémů (ERP).

Celkem byly vybrány tyto tři společnosti s následujícími sazbami:

* PragoData a.s. (15 800 Kč za den, tedy **1 975 Kč za hod.** bez DPH)
* ADVICE.CZ Solutions s.r.o. (17 200 Kč za den, tedy **2 150 Kč za hod.** bez DPH)
* NESS Czech s.r.o. (17 500 Kč za den, tedy **2 187,50 Kč za hod.** bez DPH)

Všechny tři společnosti jsou partnery společnosti Gordic, která je výrobcem platformy GINIS+. Do výběrového řízení se tak mohli přihlásit pouze dodavatelé, kteří byli zároveň certifikováni jako GORDIC PARTNER. Už jen to představuje v případě tak velké zakázky problém, nicméně to v praxi není nic neobvyklého.

Dalším nedostatkem této zakázky jsou vyjednané licenční podmínky. Magistrát jako objednatel sice dle smlouvy získal výhradní licenci k užívání vzniklých autorských děl. Nicméně jde pouze o licenci k užívání, čili nikdo kromě certifikovaných dodavatelů nemůže dílo dále rozvíjet nebo upravovat. Jedná se proto o další pro Magistrát značně nevýhodnou smlouvu, která jej prohlubuje vendor lock-in. Gordic pak profituje skrze síť svých partnerů, takže se už ani nemusí o zakázky ucházet, protože jeho produkty používané ve veřejné správě za něj dodávají, spravují a rozvíjejí jeho partneři.

To ale není jediný problém s licenčními podmínkami této smlouvy. Další omezení představuje podmínka, že Praha získává výhradní licenci na veškeré výsledky rozvoje. Tímto způsobem tak Praha zavazuje dodavatele, že autorské dílo nesmí využít například v dalších krajských městech, která by měla podobné potřeby. Alarmující je také skutečnost, že Operátor ICT jako městská firma zřízená pro informační a komunikační potřeby hlavního města opět jen nečinně přihlížel.

### Jak to dělat lépe?

Konzervativní přístup veřejné správy, kdy se raději alibisticky nakupuje software a podpora pro něj od proprietárních dodavatelů, není pro dynamický rozvoj egovernmentu v ČR vhodný. Má však svou tradici, kterou je možné narušit pouze novým inovativním způsobem.

Varianty lepšího řešení pro příklad informačního systému pro ERP a ESSS agendy MHMP jsou následující:

* Magistrát by při svém rozpočtu mohl investovat do pořízení **informačního systému na míru**, který by pak mohl nabízet jako otevřený software ostatním krajským městům, a stále by proti současnému stavu ušetřil. Zvláště pak ve chvíli, kdy by se rozvoje chopila i ostatní města,
* případně by mohl Magistrát upustit od rozšiřování proprietárního systému, při jehož užívání je závislý na jeho jediném výrobci, a naopak jeho roli omezit a **rozvíjet vlastní nadstavby**, u kterých by bylo možné dodavatele skutečně volit na základě otevřené soutěže.

I kdybychom ale přistoupili na argumentaci aktuální potřeby určité systémové kontinuity, tedy že MHMP zkrátka z více či méně objektivních důvodů v současnosti musí používat právě platformu GINIS+, vykazuje tato veřejná zakázka výrazné prvky nehospodárnosti. Kupříkladu ve srovnání s podobnou zakázkou, kterou soutěžil Magistrát města Brna rovněž na údržbu a podporu software Ginis. V Brně dokázali vybrat dodavatele za jedenáctkrát nižší cenu, ve srovnání s Prahou tedy za čtyři roky ušetří zhruba 308 000 000,- korun. A to už nejsou zanedbatelné prostředky. Na tento problém jsem [upozornil již na zastupitelstvu 26. 1. 2017](https://github.com/pirati-byro/spisy-zk-pha-2016/blob/master/4382-gordic/2017-01-26-500M-zakazka/prezentace.pdf).

Pokud bychom pro srovnání vycházeli z [Přehledu obvyklých cen ICT prací](http://www.mvcr.cz/clanek/prehled-obvyklych-cen-ict-praci.aspx) prací k dnešnímu datu, dalo by se pouze za rozdíl mezi náklady Prahy a Brna pořídit například **10 000 člověkohodin administrátorů, 10 000 člověkohodin programátorů, 10 000 člověkohodin podpory a 10 000 člověkohodin specialistů v nejvyšší cenové hladině a stále by se ušetřilo téměř 100 000 000,- korun!** Tolik zbytečně promrhaných prostředků, které se daly využít daleko efektivněji. Když se ale podíváme do přehledu cen, zjistíme, kde vězí problém. Kupříkladu administrátor platformy Ginis je totiž v průměru dvojnásobně dražší než linuxový administrátor.

Veřejné zakázky na informační systémy a software obecně proto nadále zůstávají pro veřejnou správu značnou překážkou na cestě k efektivnímu egovernmentu. Aplikace stejných metod, které se pro rozvoj egovernmentu v ČR využívají od počátku devadesátých let, nás skutečně nikam neposune.
