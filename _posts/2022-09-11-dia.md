---
layout:     post
title:      "Digitální a informační agentura"
date:       2022-09-11 18:00:00 +0100
categories: Digitalizace
comments:   true
tags:       [Egovernment, Digitalizace, Piráti]
img:        egov-cr.jpg
author:     Ondřej Profant
---

Digitální transformace Česka konečně startuje. Nejedná se o nějaký jeden nový informační systém, přejmenování jedné pozice či něco podobného. Jedná se o opravdovou institucionální změnu na základě zkušeností od nás i ze zahraničí.

<!--more-->



## Historie

Před 13 lety byly spuštěny klíčové projekty: Základní registry, Czechpoint a Datové schránky. Projekty na svou dobu velmi revoluční. Technicky spíše podprůměrné, avšak doba ještě nepřála moderním IT postupům.

Těsně předtím bylo zrušeno [ministerstvo informatiky](https://cs.wikipedia.org/wiki/Ministerstvo_informatiky_%C4%8Cesk%C3%A9_republiky) (MI). Což v té době to dávalo smysl. Ministerstvo samo o sobě nebylo navrženo dobře - bylo slabé, nedisponovalo klíčovými pravomocemi. V té době nejspíš nikdo ani nevěděl, jaké pravomoci by mělo mít.

Po zrušení MI, v letech 2007-2022, byla digitalizace agendou ministerstva vnitra. Tam za těch 15 nezaznamenala žádný výrazný posun (kromě dvou výjimek, o těch dále) . Celá sekce fungovala přísně úřednicky. Pohledem zvenku neměla ambice digitalizovat ČR jako celek, namísto toho oprašovala systémy, které měla ve správě. A ani to se zcela nedařilo, základní registry jsou dnes v žalostném stavu, kdy potřebují víc jak jednogenerační obměnu HW i SW. Neexistovala politická podpora a ambice. Vše jelo samospádem.

Dvě zmíněné pozitivní výjimky za sebou zanechali dva ředitelé odborů MVČR. Roman Vrba vytvořil a projektově vedl Portál občana. Platformu postavenou na moderních technologiích, která záplatuje jednu z velkých bolístek českého egov - roztříštěnost. Na jednom portálu, v jednom UX provedení se sbíhá velké množství služeb státu. Inu, vyzkoušejte si to sami: portal.gov.cz. Spolu s Portálem vznikl [design systém](https://designsystem.gov.cz/), jednotný design, který lze nasadit pro všechny weby státní správy. Druhým ředitelem je Petr Kuchař, který budoval Odbor hlavního architekta egovernmentu. Podařilo se připravit [rozsáhlou koncepci](archi.gov.cz) a podařilo se vnést enterprise architekturu do projektů. Všechny zbylé projekty (např. jednotná [Identita občana](https://www.identitaobcana.cz)) jsou dílem Evropské unie. Za všechny tyto aktivity, které vznikly odporu navzdory, patří všem zúčastněným velký dík.

V minulém volebním období se také silně posunula legislativa. Do té doby jsme měli legislativu, která měla tendenci popisovat zamýšlené informační systémy do vysokých detailů, včetně podrobností jejich architektury. Tedy legislativa tvořila zbytečné výrazně svazující podmínky u běžných provozních věcí (věci nešlo dělat jinak beze změny zákona). Což je naprosto omezující a v důsledku i škodlivé. Přitom v praxi je potřeba jenom to, aby zákon určil správce agend a k nim příslušících agendových informačních systémů a definoval, kdo má nárok na zpracování osobních údajů.

Co se změnilo? Na základě široké politické shody byl schválen zákon [12/2020 Sb. o právu na digitální služby](https://www.zakonyprolidi.cz/cs/2020-12), který zcela změnil paradigma. Garantuje občanům nárok na služby státu digitálně, inventarizuje služby a vše zastřešuje. Také byla schválena zákonná pravidla pro používání cloudu ve státní správě.

Největší slabinou zákona o právu na digitální službu jsou specifické resortní zákony, které někdy digitalizaci vysloveně blokují (popisují proces do detailů, takže ho nelze změnit). 


## Hlavní problémy egovernmentu

Hlavní problémy egovernmentu v ČR jsou až notoricky známe:



* **Resortismus**: resorty spolu nespolupracují. Jeden bojuje s vendor lock-inem, druhý stejný produkt nakupuje. Jeden vytvoří moderní rozhraní, druhý ho odmítne použít.
* **Roztříštěnost**: Přirozeně se zkopírovaly gesce a dané resorty poskytují své služby, mnohdy však zcela duplicitní. Dlouho nebyla jednotná identita. Některé resorty mají dodneška problém vydat výpis z jednoduché databáze, kterou vedou. Pro občana je to matoucí a hraničí to až s nepoužitelností. Odstrašujícím příkladem je třeba [Registr živnostenských oprávnění](https://www.rzp.cz) a jeho UX.
* **Neschopnost adaptovat moderní postupy**: Toto je víceméně obecná vlastnost z podstaty věci konzervativní veřejné správy. V případě digitalizace to bylo ještě umocněno tím, že byla utopena v jednom z největších resortů, který ze své podstaty primárně řeší policii. V praxi hlavně žádné experimenty či změny.
* **Neschopnost změny**: Naše veřejné instituce se nemění. Přitom soukromý sektor i jiné státy neustále přizpůsobují svou organizační strukturu výzvám doby. Bankovní domy už mají běžně sdílená centra služeb, zatímco u státu si každá “pobočka“ (ministerstvo) buduje své služby sama apod.
* **Nedotaženost projektů**: Projekty jsou vlastně jen úkoly ve spisové službě. Nehledí se na ně jako na projekt, který má nějaké cíle a má přinést konkrétní benefity. Úkolem je například elektronický výpis. Ale nikdo uvnitř už se neptá, zda ho klient dostane rychle, pohodlně, jak ho případně reklamuje… Neznamená přece, že je úkol splněn, když na obskurní stránce popíšeme, že můžete na ještě obskurnější stránce na něco kliknout a výpis nám přijde Datovou schránkou.
* **Strach z neúspěchu**: Moderní firmy i státy aplikují princip “fail fast”. Tedy neboj se neuspět, ale včas to zjisti a přines užitečnou zkušenost: “tudy ne”. ČR naopak aplikuje až neuvěřitelnou opatrnost a úředníci radši nedělají nic, nebo dělají mnohokrát nepovedený leč zaběhlý postup, než aby vyzkoušeli cokoliv nového. Byť je např. daná inovace osvědčena v několika sousedních zemích.
* **Předražení jednotlivých projektů**: Projekty jsou drahé. A to zvláště v celkových nákladech. Není nic špatného zaplatit za kvalitní dlouhotrvající práci. Ale my často dostáváme podprůměrný SW za ceny, které víceméně jinde nevidíme. Tento jev ještě umocňuje, že daný SW mnohdy nesplní co slíbil (např. nedojde k plné automatizaci procesu). Další bolístkou jsou celkové náklady. Zcela elementární způsob jak ušetřit je nechat centrální systémy dělat svou práci a psát jen drobné rejstříky, což je většinou to, co jednotlivé resorty potřebují. Namísto toho mnohdy vidíme duplikaci s centrálními sdílenými systémy.

My naopak chceme veřejnou správu, která je



* stát pro občana, ne naopak
* důvěřující i důvěryhodná
* moderně a daty řízená
* motivující k inovacím a efektivitě
* efektivní, automatizovaná
* agilní a akceschopná
* jednoduše proklientská


## DIA

Problémů je, jak jsme viděli, opravdu hodně. Nejde předpokládat, že jeden člověk s drobným týmem může z měsíce na měsíc všechny odstranit. Navíc se o potřebě změny v kuloárech hovoří již dlouho.

Proto jsme poslední půlrok připravovali opravdovou systémovou změnu. Ta v červenci prošla meziresortním připomínkovým řízením, v srpnu vládou a v září prvním čtením v Poslanecké sněmovně. Zhmotněna je v [sněmovním tisku 287](https://www.psp.cz/sqw/historie.sqw?o=9&t=287) ([samotný materiál a důvodová zpráva](https://www.psp.cz/sqw/text/orig2.sqw?idd=215725); [RIA](https://www.psp.cz/sqw/text/orig2.sqw?idd=215727)). Do projektu je zapojeno 80 lidí z různých resortů.

Hlavní změny jsou:



* vyčlěnění Správy základních registrů a 2 odborů MVČR do samostatné instituce - Digitální a informační agentury (DIA)
* DIA je ústředním orgánem státní správy
* DIA má vlastní rozpočet
* DIA má ve správě zákony týkající se digitalizace
* DIA je samostatným připomínkovým místem v meziresortním připomínkovém řízení
* OHA v rámci DIA má širší kompetence - posuzuje projekty z hlediska ekonomického, z hlediska uživatelské přívětivosti, práce s daty atd.
* DIA převezme informační systémy, které jsou sdíleny napříč veřejnou správou: základní registry, Czechpoint, Portál občana a další. Některé ne hned.

Hlavní úkoly jsou:



* DIA převezme úkoly plynoucí ze zákona o právu na digitální služby a z programového prohlášení vlády v oblasti digitalizace.
* Planujeme pomáhat přímo dalším rezortům. Například přímou pomocí s navržením informačního systému, aby to neskončilo mrzením - jak je to naneštěstí běžné.
* V neposlední řadě chceme pořádně rozvíjet centrální sdílené systémy (např. základní registry), tak, aby nebyly úzkým hrdlem českého egov.


### Inspirace NÚKIBem

Kromě inspirace Dánskem, Izralem či Velkou Británií se inspirujeme českým Národním úřadem pro kybernetickou a informační bezpečnost (NÚKIB). Ten je také ústředním orgánem, obdobné velikosti (personální a finanční), ředitele jmenuje vláda. Co pro nás ale bylo klíčové, je kultura a mentální nastavení. Vedení NÚKIB bere kybernetickou bezpečnost ČR jako svoji odpovědnost. Je jasné, že to nemá na starost nikdo jiný a jejich prostředky jsou určeny přesně na to. Princip jasné zaměřené odpovědnosti (single responsibility). To je ve velkém kontrastu proti velkému resortu, který má i objektivně důležitější jiné zájmy.

Zároveň vidíme jasnou linii odpovědnosti. Politickou odpovědnost nese vždy ministr jakožto člen vlády. Ten představí svoji vizi. Na té se shodne s ředitelem DIA, který na ní začne pracovat. Ministr určuje kurz, kterým ředitel DIA kormidluje svůj úřad. . Z mých zkušeností je taková shoda výrazně častější. Pokud neshodnou, ministr má právo vládě předložit jméno nového ředitele, který bude jeho vizi sdílet. Už však nemůže vyměnit řadové úředníky a zaměstnance DIA (např. ty, kteří vydávají odborná stanoviska OHA). Ředitel samozřejmě bude vybrán v otevřeném výběrovém řízení. To mi přijde jako vyvážený přístup mezi politickou odpovědností a dlouhodobou stabilitou. Jen tak se lze vyhnout neřízenému chaosu, jaký jsme v mnoha případech mohli vidět v COVIDové krizi.

Obecně se dá říci, že moderní společnost směřuje spíš k menším institucím s jasně definovanými cíli. Doba obřích úředních molochů je za nmi, a státní správa se musí přizpůsobit.


## Bude to stačit?

Samozřejmě tato změna sama o sobě nestačí. Jak by řekli matematici, jedná se o podmínku nutnou, nikoliv postačující. Víceméně základní kameny jsou rozloženy dobře, ale chyběla organizovaná síla, která by dotahovala projekty do použitelné podoby. Teď máme robustní legislativní základy, základní informační systémy, ale čeká nás:



* generační obměna centrálních sdílených informačních systémů
* oprava legislativních překážek v resortně specifických zákonech
* spolupráce s resorty na navrhnutí digital born řešení pro jejich procesy
* přinesení nové agilnější kultury dovnitř veřejné správy
* jednotné UX a brand služeb
* centrální callcentrum, které pomůže klientům

Pokud chceme změny, nesmíme se změn bát.


[Post na FB]: https://www.facebook.com/ondrej.pirat.profant/posts/pfbid0rgxX8jz6RTuWPUcC1zk6rjgbseA3HkRUWHk4euGim5592cFbtuADwswuvF5YeS9Al
[1. tiskovka]: https://www.vlada.cz/cz/media-centrum/aktualne/ivan-bartos-zahajil-reorganizaci-digitalizace-statni-spravy--expertni-centrum-bude-udavat-technologicky-smer-a-zlepsi-kulturu-rizeni-digitalizace-198317/
[2. tiskovka]: https://www.vlada.cz/cz/media-centrum/aktualne/zakon-o-vzniku-dia-prosel-snemovnou-v-1--cteni--je-to-zasadni-krok-pro-odstartovani-digitalni-transformace-verejne-spravy--rika-vicepremier-bartos-198912/
