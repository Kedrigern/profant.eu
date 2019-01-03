---
layout:     post
title:      "Otevřený hardware jako součást kybernetické bezpečnosti"
date:       2019-01-01 17:00:00 +0100
categories: Bezpečnost
comments:   true
tags:       [bezpečnost, egovernment]
img:        otevreny_hardware.jpg
author:     Ondřej Profant
---

Skandál okolo čínských společností Huawei a ZTE poukázal na další citlivou oblast kybernetické bezpečnosti, přičemž příčinou je využívání uzavřených technologií. Obavy o bezpečnost státních informačních systémů jsou zcela určitě na místě. Vyhazováním telefonů Huawei a ZTE a zákazem jejich používání se ale nic nevyřeší, problém je jako vždy daleko hlubší a složitější.

<!--more-->

Národní úřad pro kybernetickou a informační bezpečnost (NÚKIB) vydal 17. 12. 2018 varování před používáním technických a programových prostředků společností Huawei Technologies a ZTE Corporation. Toto varování vyvolalo značný mediální ohlas, v určitých politických kruzích by se dalo téměř až hovořit o panice (zbrklé chování premiéra v souvislosti s touto kauzou jsem popsal již v předchozím [článku](https://www.profant.eu/2018/nahy-premier.html)). Pro odborníky v oblasti informačních technologií se ale nejedná o žádnou novinku. Rizika spojená s proprietárním hardware využívajícím uzavřené technologie jsou odborné komunitě známy již desítky let.

Je samozřejmě dobře, že se o těchto problémech začíná ve veřejném prostoru více uvažovat a diskutovat. Koneckonců v případě informační infrastruktury státu se skutečně jedná o záležitosti národní a potažmo i unijní bezpečnosti, které mohou mít v krizových scénářích fatální dopady pro naši republiku a naše spojence. Stačí si jen například představit, že backdoor v hardware využívaném pro zabezpečování chodu jaderné elektrárny způsobí v kritický moment selhání. A nemusí jít o katastrofickou vizi zakončenou výbuchem celého areálu elektrárny, obyčejná sabotáž s následným výpadkem a nucenou odstávkou produkce elektřiny může sama o sobě napáchat až miliardové škody.

Není zároveň možné uvažovat v přísně geopolitických intencích, čili na jedné straně se vyhýbat čínským výrobkům, ale zároveň upřednostňovat ty americké. Základní principy kontroly hardware by měly být mnohem více systémové, aby bylo možné jakékoliv pochyby o používaných zařízeních snadno rozptýlit, nebo naopak potvrdit a vyvodit patřičné důsledky.

### Správná výrobní praxe pro hardware

Rozumným přístupem by bylo zavedení jasných a striktních principů při kontrole procesů výroby produktu. Podobně jako se například ve farmaceutickém průmyslu nebo potravinářství uplatňuje takzvaná správná výrobní praxe.

Hardwarové produkty by tak například musely mít svůj “rodný list”, který by spotřebitele informoval o veškerých náležitostech, které by regulátor potřeboval. Výrobci a dodavatelé rizikových součástek pro kritickou infrastrukturu by museli mít certifikovaný provoz, na který by dohlížel státní kontrolní orgán. Jistě by se dalo vymyslet dostatek dalších kontrolních a ochranných opatření.

Tato forma regulace a kontroly výrobků se může na první pohled zdát jako poněkud přehnaná. Je však nutné si uvědomit, že stát nemůže pro svůj kritický provoz pořizovat potenciálně nebezpečný hardware. Stejně tak státní orgány chrání trh před jinými závadnými výrobky, ať už to jsou vadné elektrospotřebiče, nebezpečné hračky nebo jedovaté léky. A v případě hardware, který je součástí širší sítě kritických informačních systémů státu, je zapotřebí postupovat se srovnatelnou opatrností.

### Otevřený hardware jako bezpečné řešení

**Co je otevřený hardware?** [Otevřený hardware](https://en.wikipedia.org/wiki/Open-source_hardware) nebo open source hardware jsou technické prostředky založené na otevřeném designu. Koncový spotřebitel tak může důkladně prozkoumat schémata daného výrobku a případně je upravit pro své potřeby. Svobodná licence otevřeného hardware umožňuje snadné a rychlé sdílení technologií. Vzhledem k rozmachu 3D tisku se pojem otevřený hardware nevztahuje pouze k elektronice, ale například i k předmětům běžné potřeby, které si může uživatel na základě designu uvolněného pod svobodnou licencí stáhnout a vytisknout. Velkou výhodou otevřeného hardware je přístup k jeho kompletní dokumentaci. To velmi usnadňuje práci s výrobkem i jeho případný bezpečnostní audit. 
{: .article-note}

Dobrým řešením by také mohlo být využívání otevřeného hardware od certifikovaného regionálního výrobce. Do otevřeného hardware by pak mohlo investovat více států, případně by se z toho mohl stát společný projekt na úrovni EU či NATO. Tím by se jednak blíže propojoval průmysl s vědou, aniž by při tom docházelo ke zvýhodňování konkrétních výrobců a s tím spojené korupci, ale zároveň by se jednalo o formu investice do společné infrastruktury kybernetické obrany.

Otevřený hardware aktuálně využívá například Facebook při výstavbě svých datových center. Své zkušenosti převedl na nadaci [Open Compute Project (OCP)](https://www.opencompute.org)[^1], která certifikuje otevřený hardware. Dávno se tedy nejedná (stejně jako v případě otevřeného software) o “zábavu v garáži”, nýbrž o plnohodnotnou funkční alternativu, do které investují nadnárodní korporace. Státy by neměly zůstat stranou, jinak budou opět na korporacích zcela závislé.

Širší využívání otevřeného hardware v rámci informačních infrastruktur členských států EU by jednotlivým státům mohlo pomoci získat větší kontrolu a tím posílit jejich bezpečnost. Zároveň se tak může významně podpořit pokrok v oblasti vývoje nového hardware, který by byl vyroben čistě v zemích EU. Příslušnými legislativními opatřeními by se pak dalo velmi snadno předejít podobným problémům, jako jsou nyní se společnostmi Huawei a ZTE. Taková strategie ale může fungovat pouze za předpokladu, že se na ní členské státy EU shodnou.

---

[^1]: OCP není jediná obdobná organizce. Za zmínku jistě stojí i [Open Hardware Repository](https://www.ohwr.org) od CERNu.