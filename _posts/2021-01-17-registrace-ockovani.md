---
layout:     post
title:      "Jak selhala registrace očkování"
date:       2021-01-17 20:30:00 +0100
categories: Bezpečnost
comments:   true
tags:       [Bezpečnost, Soukromí]
img:        facepalm-ockovani.jpg
author:     Ondřej Profant
---

Konečně jsme se dočkali světla na konci dlouhého pandemického tunelu - distribuce vakcíny. Opravdového způsobu jak vrátit naše životy do normálu. Avšak i tento nadějný okamžik provází naprosté selhání vlády.

<!--more-->

15\. 1. byl spuštěn rezervační systém. A objevila se v něm celá řada chyb. 

<blockquote class="twitter-tweet"><p lang="cs" dir="ltr">Zahájení očkování proti koronaviru v Česku nebylo připravené, nezvládlo by se bez nemocnic, které ale dostává pod další tlak, tvrdí Milan Kubek. Nechápe také, proč se senioři mají přihlašovat pomocí elektronického systému, který „jediné, co dělá, že zaměstnává jejich příbuzné.“ <a href="https://t.co/aRvqKSk6je">pic.twitter.com/aRvqKSk6je</a></p>&mdash; CT24zive (@CT24zive) <a href="https://twitter.com/CT24zive/status/1350818278134976512?ref_src=twsrc%5Etfw">January 17, 2021</a></blockquote>

## Chyby organizační

1) První otázkou je, zda je vůbec **vhodné registrovat lidi 80+ přes internet**. Chápu, že systém bude sloužit i dalším skupinám obyvatel, avšak dělat ze seniorů pokusné králíky mi přijde krajně nevhodné. Zvláště když Piráti prosadili do Zákona o právu na digitální služby právo nebýt digitální.
2) **Časová tíseň**: O důležitosti logistické operace s vakcínou se ví de facto od vypuknutí krize. Od podzimu víme, že nás od vakcíny dělí nanejvýš měsíce. Akorát naše vláda se odmítla velmi dlouho vyjádřit, jak se celá věc bude řešit v ČR. Proto se distribuce, které jsme svědky, začala řešit až okolo Vánoc. V reálu tedy na přípravu systému bylo cca 14 pracovních dní.
3) Díky časové tísni z bodu 2) nebyla možnost systém řádně vyzkoušet a **otestovat** v širší skupině, zapracovat připomínky odborníků apod. To by měla být standardní součást procesu vývoje obdobného systému (zvláště pokud ho neumějí správně navrhnout).
4) **Systém byl naroubován na systém společnosti Reservatic**. Na smlouvu, kterou měl NAKIT již od října. Avšak ta počítala s centrální registrací na ag testy, nikoliv na očkování. Tato úloha se velmi liší v množství předávaných osobních dat. U očkování podle skupin obyvatelstva musíte zkoumat věk, zdravotní stav a další ukazatele. Systém Reservatic byl nejspíš zvolen jen proto, že UVN ho již měla propojen se softwarem ÚZIS.
5) **Špatná komunikace s médii**. Server iRozhlas.cz se již měsíc zajímal přesně o palčivé problémy okolo nakládání s osobními údaji, ale komunikace ze strany NAKIT byla formalistická a snažila se chyby zapírat.
6) **Nebyla domluva s mobilními operátory**, proto nestačila SMS brána jak informoval [DeníkN][].

    <blockquote class="twitter-tweet"><p lang="cs" dir="ltr">Mobilní operátoři o ověřovacích SMS pro registraci k očkování nevěděli. PIN kódy tak lidem přicházely se zpožděním. O půl deváté měli operátoři Chytré karantény ve frontě 40 tisíc SMS zpráv. <a href="https://t.co/v5RYPg5QwF">pic.twitter.com/v5RYPg5QwF</a></p>&mdash; CT24zive (@CT24zive) <a href="https://twitter.com/CT24zive/status/1350094469484457985?ref_src=twsrc%5Etfw">January 15, 2021</a></blockquote>
7) Některá **očkovací centra** (např. Blansko) **nejsou integrována** do systému. Občané je tedy ani nenajdou v nabídce.

Odpovědnost je zcela jistě na vládě, která má zemi svěřenou do péče. Parlament jí ve všem vyšel vstříc, avšak i přesto vláda v čele s premiérem Andrejem Babišem nedokázala připravit klíčové věci včas. Zcela absurdní je výrok poslance ANO J. [Špičáka][spicak], který se snaží hodit vinu na opozici, protože vládě neporadila, že má věci řešit v předstihu.

## Závažné technické chyby

1) Nedostatečná ochrana osobních údajů. Celý systém z logiky věci v dalších fázích bude pracovat s anamnézou klienta. Číslo pojištěnce (většinou rodné číslo) je předáváno v URL, což není bezpečná technika. Například je ukládáno v přítomných Google Analytics nebo v log souborech serverů, případného proxy serveru, může být posiláno v HTTP hlavičkách jako tzv. Referer.
2) Validace dat čistě v prohlížeči uživatele umožňuje [věkové restrikce obejít](https://www.novinky.cz/internet-a-pc/software/clanek/kterak-se-24lety-student-k-registraci-mezi-80letymi-dostal-40347976). Běžné je řešit validaci vstupních dat u klienta v prohlížeči i na straně serveru, aby nedošlo k chybě a zároveň byl klient rychle informován.
4) Druhá fáze je provozována na serverech soukromé společnosti Reservatic.com. Takto částečné zapojení nedává příliš velký smysl.
5) **Špatná validace rodných čísel**. Prvotní zprávy hovořily, že se špatně validují 9 místná rodná čísla. Vladní zmocneněc říká, že se jedná o jinou chybu u validace rodných čísel (lidé narození 31.). Tak jako tak je to problém.
6) Systém není provázán s centrální elektronickou identitou občanů (**NIA**). To je důležité hlavně z dlouhodobého hlediska, až bude registrace přístupná širší skupině obyvatel.
7) Absence **penetračních testů** ukazuje, že provozovatel se nestará o ochranu soukromí návštěvníků. Jejich neprovedení je jasné z počtu chyb. Toto je samozřejmě vina šibeničního termínu, za který opět může vláda.

## Chyby v návrhu a uživatelské přívětivosti

1) Stát měl zvolit lepší doménu než `https://registrace.mzcr.cz` či ` crs.uzis.cz`, například státní doména `gov.cz` sice není ideální, avšak je krátká. Nicneříkající zkratky ministerstev nepomáhají. Stát si určitě mohl koupit lepší doménu druhého řádu.
2) ReCaptcha od společnosti Google nepatří na klíčový web veřejné správy. Senioři jsou nuceni klikat na obrázky a rozpoznávat, na kterých jsou fotky semaforů či hydrantů z USA!
    <blockquote class="twitter-tweet"><p lang="cs" dir="ltr">Právě jsem mluvil s babičkou. <br><br>Poněkud jí zmátlo, že při registraci na očkování musela absolvovat test z rozpoznávání hydrantů (ReCaptcha).</p>&mdash; Ondřej Profant (@ondrej_profant) <a href="https://twitter.com/ondrej_profant/status/1350857240899682304?ref_src=twsrc%5Etfw">January 17, 2021</a></blockquote> 
3) Systém měl být navržen tak, aby nebyly třeba 2 šestimístné piny. Ideální by byl stav, kdy by uživatel mohl objednat i další rodinné příslušníky.
    <blockquote class="twitter-tweet"><p lang="cs" dir="ltr">U Francouzů se zbláznili. Registrace na dvě kliknutí a při jednom přihlášení rovnou zaregistrovat všechny příbuzné!🤦<br><br>Kde je první a druhý PIN? Kde je odeslání rodného čísla Googlu? Kde je souhlas se zasíláním obchodních sdělení? To Francie neví jak vypadá <a href="https://twitter.com/hashtag/CountyForTheFuture?src=hash&amp;ref_src=twsrc%5Etfw">#CountyForTheFuture</a>? <a href="https://t.co/p826Oa9kPp">pic.twitter.com/p826Oa9kPp</a></p>&mdash; Pavel Hertl (@PavelHertl) <a href="https://twitter.com/PavelHertl/status/1350478108789514241?ref_src=twsrc%5Etfw">January 16, 2021</a></blockquote> 

[lupa]: https://mobile.twitter.com/Lupacz/status/1350013368640413696
[Validace]: https://mobile.twitter.com/filipsedivy/status/1350046619429908480
[DeníkN]: https://denikn.cz/539388/infrastruktura-spusteni-ockovani-zvladla-jeli-jsme-na-dvacet-procent-s-operatory-jsme-se-bavili-tvrdi-dzurilla/?cst=ff9396291bea5aa41c82937672ada50ba64cfd6c
[navod]: https://www.facebook.com/ceska.piratska.strana/photos/a.117963484038/10158150543079039/
[spicak]: https://twitter.com/maestrosill/status/1349857358768439297
[statni-vyznamenani]: https://twitter.com/CT24zive/status/1350461115956916231
