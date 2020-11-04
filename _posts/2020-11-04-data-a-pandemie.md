---
layout:     post
title:      "Data a pandemie"
date:       2020-11-04 08:00:00 +0100
categories: Bezpečnost
comments:   true
tags:       [Bezpečnost]
img:        data.jpg
author:     Bára Soukupová
---

Pandemie koronaviru nepochybně změní svět v mnoha ohledem. Nejen v Česku bude milníkem v možnostech práce z domova, distančním vzdělávání, digitalizaci a mnoha dalších oblastech. Významný posun také způsobí v oblasti chápání dat, jejich zveřejňování a obecně politiky postavené na datech.

<!--more-->

Datová politika je jednou ze stěžejních součástí pirátského programu. Byli jsme první politickou silou, která konzistentně otevírání veřejných dat i přes odpor prosazovala. Na letošní pandemii je vidět, proč je správné hospodaření s daty důležité.

## Uvolňování dat o epidemii

Když v březnu pandemie propukla, nebylo systematicky denně zveřejňováno téměř nic. Od novinářů, osob v exekutivních funkcích, výzkumníků i občanů nastala velká poptávka po pandemických datech.

Ministerstvo zdravotnictví a hlavně Ústav zdravotnických informací a statistiky (ÚZIS) poměrně rychle zareagovaly a již na konci března byl k dispozici [dashboard](https://onemocneni-aktualne.mzcr.cz/covid-19) a nejdůležiější otevřená data na denní bázi, včetně API. V průběhu dalších měsíců pak byla data i vizualizace rozšiřována a vylepšována. Za tento počin je třeba ÚZIS pochválit.

Stále však mnohá potřebná data zveřejňována nebyla. Piráti na začátku května marně [žádali](https://www.pirati.cz/tiskove-zpravy/data-o-epidemii-vedcum.html) o poskytnutí epidemiologických modelů, podrobných anonymizovaných dat a scénářů vývoje. Později jsme pak [žádali](https://www.pirati.cz/tiskove-zpravy/opatreni-proti-koronaviru-pirati-svolali-vybor.html) i o data, na jejichž základě jsou vyhlašována jednotlivá opatření.

Postupně se daří data z ÚZISu dostávat. Již poskytnul parametry svého epidemiologického modelu i detailní informace o kapacitách nemocnic. Problémem je ale jejich forma.

## Forma dat

Epidemiologický model [byl poskytnut](https://www.dropbox.com/s/eg46eb5qzp2x76t/1_Metodicka_dokumentace_model_populacni_kratkodoby.pdf?dl=0) formou jeho slovního popisu. Přitom je naprogramován ve jazyce VBA, tudíž by nebyl problém zveřejnit přímo jeho zdrojový kód.

Aktuální epidemiologické informace včetně podrobných kapacit zdravotní péče jsou zase každé ráno posílány v několika excelových tabulkách na množství poslanců a dalších osob, které o to prof. Duška (ředitele ÚZIS) požádaly. Přitom nejde z principu o citlivá data a jejich šíření není omezeno. Stejně se tak dostávají oklikou i k novinářům a veřejnosti. Jejich nezveřejnění ÚZISem standardní cestou jako otevřená data je tak jen zbytečný alibismus.

Obsáhlejší datovým zdrojem jsou týdenní souhrnné reporty, které prof. Dušek prezentuje vládě a poslancům a poslankyním na Zdravotním výboru Sněmovny. V nich jsou aktuální data shrnuta do několika desítek více či méně nepřehledných tabulek a grafům. I tyto prezentace se stejně dostávají na veřejnost a novinové titulky popisující ["uniklé dokumenty"](https://prazsky.denik.cz/zpravy_region/na-konci-rijna-130-mrtvych-denne-podivejte-se-na-unikla-data-o-covidu-20201014.html) zrovna nepřispívají v důvěru lidí vládě.

Zbytečná politika tajení dat, které z principu tajné nejsou a mohou být velmi prospěšné v mnoha oblastech, tak zbytečně komplikuje efektivní postup proti pandemii a podráží již tak téměř neexistující důvěru lidí.

## Predikce vývoje

Samostatnou kapitolou jsou epidemiologické modely a predikce vývoje. To jsou totiž ty nejdůležitější informace pro správná politická rozhodnutí ve správný čas.

V březnu nás zachránil [muž s excelem](https://www.seznamzpravy.cz/clanek/tajemny-muz-ktery-na-jare-zachranil-cesko-exreditel-ceske-pojistovny-124767), v srpnu a září už se takový zázrak nekonal. Ač ÚZIS měl potřebný model i všechna data, nepodařilo se dostat klíčovou informaci na správná exekutivní místa (v tomto případě k vládě a premiérovi) a konat. Mít data totiž nestačí.

ÚZIS měl potřebná data a použitím svého epidemiologického modelu i zvládnul vypočítat informace o pravděpodobném vývoji epidemie. Nedokázal je ale smysluplně předat a vysvětlit. V jeho reportech je množství dat a vydedukovat z nich hodnotné informace a podklady k politickém u rozhodování je pro člověka necvičeného s prací s daty prakticky nemožné. Často se také ve svých prezentacích ÚZIS dopouštěl vyložených datových faulů - nepřepočítával data na počet obyvatel jednotlivých krajů a nepoužíval sedmidenní součty nutné kvůli rozdílným kapacitám testování v jednotlivých dnech v týdnu.

Špatnou informační hodnotu reportů ÚZIS lze ukázat na aktuální prezentaci k předpokládanému vývoji epidemie. ÚZIS zde [operuje se čtyřmi scénáři](https://www.seznamzpravy.cz/clanek/statistik-dusek-predpovedel-pristi-dva-tydny-v-nemocnicich-127394) podle rozdílného R (R=0,73; R=1,1; R=1,29 a R=1,47). Tyto scénáře pak předvídají 15. listopadu od 4 000 hospitalizovaných (R=0,73) po 35 000 hospitalizovaných (R=1,47). Není přitom vyčíslena pravděpodobnost jednotlivých scénářů a nejpravděpodobnější scénář podle aktuálního čísla R (R=1,0) zcela chybí. Podle takových informací nelze efektivně dělat politická rozhodnutí.

Stejně důležitá jako samotná data je totiž i forma jejich prezentace a vizualizace tak, aby z nich každý dokázal rychle vyčíst podstatné informace. Kdyby informace z epidemiologického modelu poskytoval ÚZIS nejen formou powerpointových prezentací vládě, ale i v přehledné vizualizaci dostupné pro širokou veřejnost, pravděpodobně bychom dnes měli mnohem méně mrtvých.

Za dobrou formu prezentace pokládám interaktivní model, na kterém si může i široká veřejnost představit efekt exponenciály a vyzkoušet chování v závislosti na různých scénářích budoucího R. Např. pro území USA je těchto modelů [publikováno mnoho](https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/forecasts-cases.html) a předpovědi jsou dělány jako [agregace výsledků všech modelů](https://viz.covid19forecasthub.org/). Sárská univerzita zase publikovala [hezký interaktivní model](https://shiny.covid-simulator.com/covidsim/) pro Německo s možností uživatelské změny budoucího R. Věřím, že kdyby takovouto vizualizaci předpokládaného vývoje zveřejňoval ÚZIS (nebo i některá česká univerzita či výzkumná organizace) pro Česko, velmi by to přispělo jak k informovanosti veřejnosti, tak ke kompetentnímu rozhodování vlády.

## Ideál

Koronavirus je velmi živé téma a důležitá rozhodnutí je třeba dělat na denní bázi. ÚZIS je v tomto případě odpovědným  statistickým a analytickým útvarem při Ministerstvu zdravotnictví a měl by tudíž dodávat přehledné podklady pro manažerské zvládnutí situace. Tato schopnost není jenom o tom mít správná data, ale je třeba je dát i do správného kontextu a hlavně je umět předat politikům a dalším exekutivním pracovníkům. V tom bohužel ÚZIS zatím spíše selhává.

Mohl by se inspirovat třeba datovou žurnalistikou. Tento mladý obor se totiž zaměřuje právě na to, jak získat informace z dat a předat je veřejnosti pochopitelně pomocí vizualizace. Po počátečních problémech se datové týmy uchytily nejen v [Českém rozhlase](https://www.irozhlas.cz/zpravy-tag/datova-zurnalistika), ale i v dalších českých médiích.

Analytické týmy by měly být při rozhodování ve veřejné správě standardem, nejen v opatřeních ke koronaviru, ale i při rozhodování o zákonech a všech dalších opatřeních, které mají velké společenské dopady. Bohužel, jak konstatuje i nedávná [vládní zpráva o praxi hodnocení dopadů regulace](https://ria.vlada.cz/wp-content/uploads/Zpr%C3%A1va-k-%C5%A1et%C5%99en%C3%AD-praxe-RIA-2019.pdf), analytická činnost je na českých ministerstvech a úřadech využívána nedostatečně. Čeká nás tak ještě dlouhá cesta rozvoje analytických pracovišť, která budou schopná produkovat hodnotné informace jako podklad pro politická rozhodnutí. Věřím, že významu dat a rozhodování podle nich současná krize prospěje a tento proces uspíší.
