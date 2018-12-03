---
layout:     post
title:      "Strategie pro Egovernment cloud v ČR"
date:       2018-12-02 19:00:00 +0100
categories: Egovernment
comments:   true
tags:       [Egovernment, Digitalizace]
img:        egov-cloud.jpg
author:     Ondřej Profant
---

V předchozím [článku o využití cloudových technologií](https://www.profant.eu/2018/vlada-v-oblacich.html) pro český egovernment jsem popsal základní vlastnosti těchto technologií. V tomto článku se podrobněji zaměřím na chystanou vládní implementaci.

<!--more-->

### Co vláda chystá

Vláda 14. 11. schválila strategický rámec pro Egovernment cloud (eGC). Aplikace v cloudu budou rozděleny do čtyř úrovní kritičnosti (nízká, střední, vysoká, kritická). Samotný eGC se má v budoucnu skládat z komerčního cloud (KeGC), který bude skupinou poskytovatelů komerčních cloudových služeb, kteří splnili patřičné podmínky. Služby poskytované v KeGC se budou nakupovat formou dynamického nákupního systému. Proces nákupu služeb by pak měl v praxi umožňovat snadné objednání a nákup požadované služby.

Další částí eGC je státní cloud (SeGC), který bude využíván pro nejkritičtější systémy a aplikace, tedy například základní registry, datové schránky nebo ADIS (daňový systém).

Pro orgány státní moci má být zapojení do cloudu povinné do dvou let od spuštění eGC. Pokud by se některý orgán nechtěl připojit, musel byl dostatečně prokázat, že jeho vlastní řešení je úspornější. Dále vládní materiál navrhuje zavedení řídícího orgánu eGC složeného ze zástupců Ministerstva vnitra, Ministerstva financí, Národního úřadu pro kybernetickou a informační bezpečnost, zpravodajských služeb, ústředních orgánů státní správy, orgánů veřejné správy a údajně i zástupců odborné veřejnosti.

### Jaká jsou rizika?

Ačkoliv v obecné rovině se s vládním návrhem dá souhlasit, neboť cloudové technologie jsou pro efektivnější egovernment nezbytným infrastrukturním prvkem, některé oblasti působí dost rozpačitým dojmem. Takže zatímco u služeb typu IAAS a PAAS (neboli “Infrastruktura jako služba” a “Platforma jako služba”) se dá předpokládat racionální přístup, problémy se dají očekávat u SAAS (“Software jako služba”). U tohoto typu služeb bude velmi záležet na tom, jaké služby budou vybrány do katalogu. Velmi snadno zde může dojít k protežování některých firem na úkor jiných. Tento problém ilustrují rámcové smlouvy, které MVČR uzavřelo s dodavateli některých platforem - například Microsoft, VMware, Oracle a další. Tyto smlouvy jsou velmi silnou konkurenční výhodou oproti jiným tržním subjektům. V praxi je tak jednodušší objednat si drahou Oracle DB, než se snažit vysoutěžit podporu k otevřenému databázovému řešení, která je často poskytována zdarma a nemá ani další licenční omezení.

Další otazníky se pojí s administrativním a organizačním zajištěním chystaných změn. Není ponechána dostatečná rezerva pro nezbytnou migraci dat, není vyřešen soulad definic s širší legislativou, není jisté, zda jsou na přechod všechny státní instituce připraveny. Zejména přesun nákladů z kapitálových do běžných výdajů může pro mnoho organizací představovat významné komplikace. Ty mohou vyústit až v kritický nedostatek finančních prostředků v provozních rozpočtech jednotlivých organizací. Nemluvě o tom, že mnoho institucí investovalo nemalé peníze, např. I z grantů, na výstavbu vlastních datových center.

V rámci SeGC pak jistě vznikne několik nových datových center, která budou chod státního cloudu zabezpečovat. Dá se předpokládat, že hardware pro tato datová centra se bude soutěžit v jedné nebo několika málo zakázkách. Znovu tedy hrozí významné riziko, že veškeré hardwarové vybavení bude od několika málo dodavatelů. Takový stav není správný, jelikož v hardware se často objevují chyby nebo dokonce i backdoory od výrobce. Drtivá většina hardware se navíc vyrábí mimo území ČR i EU, k jeho pořizování pro účely SeGC je proto nutné přistupovat nanejvýše obezřetně. Kromě zjevného bezpečnostního rizika, které představuje nebezpečí sabotáže či špionáže prostřednictvím dodaného hardware, je třeba se důkladně zaměřit na odstranění neúmyslných chyb. Příkladem takových chyb jsou třeba meltdown a spectre, které tvrdě postihly právě důvěryhodnost cloudu.

Na jednání [Podvýboru pro egovernment 12. prosince](http://www.psp.cz/sqw/text/text2.sqw?idd=152824), kdy je projednání vize Egovernment cloudu na programu, se tedy zaměříme na následující nevyřešené otázky:

* V regionech je **již vystavěna infrastruktura** za 100 milionů Kč. Jaka je její budoucnost?
* Jaké je bezpečnostní riziko, pokud nebudou různí dodavatelé HW, zvláště pokud budou výhradně ze zemí jako je Čína. Stejně tak je problémem **Single point of failture** (SPOF), pokud by byl jeden dodavatel (např. switchů).
* Jaká bude podpora **IPv6**? Stále není běžné, že je plná podpora v komerčních cloudech.
* **Konektivita** regionů nemusí být dostatečná pro cloudové řešení interních aplikací. Může se jednat např. o věci přímo komunikující s HW, kde je velmi těžké zajistit moderní standardy protokolů. Typickým příkladem může být kamerový systém apod. Přenáší se zde velké množství dat a bez výměny HW nejde ani zaručit, že v kvalitně komprimovaném formátu.
* Rozdělení dle **kritičnosti de facto určí cenu**. Zde je potřeba postupovat velmi obezřetně, aby se aplikace nedostávaly do příliš vysoké úrovně zabezpečení zbytečně (popř. z důvodu navýšení ceny či preferování vybraného dodavatele).
* **SAAS** může vést k oligopolu
* Velká změna v **rozpočtován**í (kapitálové vs běžné výdaje) je potřeba, ale samozřejmě musí být provedena dobře.
* Realističnost **termínu migrace**.

### Závěr

Výhody eGC jsou nesporné a nejlépe se mohou projevit zejména u menších institucí a úřadů, které si v objednávkovém rozhraní budou moci jednoduše vybrat a naklikat například pár virtuálních serverů, které budou moci hned využívat. Zároveň ale hrozí známá a reálná nebezpečí typu vendor lock-in (závislost na dodavateli) nebo single point of failure (jednoho místa selhání), kterým je potřeba předcházet.

Strategický rámec eGC je stále jen strategií, velmi bude záležet na skutečném nasazení, do kterého se může ještě mnohé změnit. Jasné je ale jedno - projekt eGC bude jedním z největších a nejrozsáhlejších projektů digitalizace států. Je proto nutné mu věnovat patřičnou pozornost.

### Odkazy

* [Vláda v oblacích?](https://www.profant.eu/2018/vlada-v-oblacich.html) - úvodní článek k problematice egovernment cloudu
* [Piráti varují před bezpečnostními riziky cloudového řešení pro veřejnou správu](https://www.pirati.cz/tiskove-zpravy/pirati-varuji-pred-riziky-cloudu-pro-verejnou-spravu.html) - tisková zpráva Pirátské strany k problematice
