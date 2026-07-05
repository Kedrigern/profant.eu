---
date: 2026-07-05
extra:
  author: Ondřej Profant
  comments: true
  img: eturista-ilustrace.webp
  layout: post
taxonomies:
  categories:
  tags:
title: "Střípky z vlády 2: eTurista"
---

V letech 2022–2024 jsem zastával roli náměstka vicepremiéra pro digitalizaci. V této sérii se pokusím poodhalit nějaké ty historky z pozadí fungování státního kolosu. nes se podíváme na eTuristu, Národní plán obnovy a na to, jak se z docela rozumné digitalizační myšlenky může stát politicko-legislativní problém.

<!-- more -->

eTurista není jednoduchý příběh „zlý stát chce šmírovat turisty“ ani „hloupí kritici brání digitalizaci“. Je to případová studie toho, jak ve státě vzniká digitální projekt: staré papírové povinnosti, evropské peníze, milníky NPO, resortní tlak, nedostatečně vysvětlená architektura a oprávněná obava o soukromí se potkají v jednom bodě.

Hlavní poučení je pro mě jednoduché: digitalizace má povinnosti zjednodušovat a data minimalizovat, ne centralizovat všechno jen proto, že to technicky jde. eTurista mohl být dobrý projekt, ale jen s jasnými zárukami.

## NPO jako tlakový hrnec

Nejdřív kontext. Národní plán obnovy (NPO) je česká implementace evropského Nástroje pro oživení a odolnost (*Recovery and Resilience Facility*, RRF). Ten vznikl po covidu jako součást širšího balíku NextGenerationEU. Nejde tedy o jeden „dotační program“, ale o balík reforem a investic, kde stát slíbil konkrétní výsledky a Evropská komise následně kontroluje, zda byly splněny.

Český plán připravila ještě vláda Andreje Babiše. Rada EU ho schválila 8. září 2021. Později byl upraven mimo jiné o kapitolu REPowerEU; tuto aktualizaci Rada schválila 17. října 2023. Podle Evropské komise má český plán hodnotu zhruba 9,2 miliardy eur, obsahuje 105 investičních proudů a 58 reforem. Zhruba 43 % prostředků má podporovat klimatické cíle a 23 % digitální transformaci.[^npo-ek]

Český web NPO to překládá do praktičtějších čísel: celkově až 216,5 miliardy korun, z toho až 208,4 miliardy ve formě grantů a až 8,1 miliardy ve formě půjček. Peníze se nevyplácejí najednou, ale ve splátkách. Uvolnění každé splátky je navázáno na plnění milníků a cílů. Všechny milníky a cíle musí být splněny nejpozději do konce srpna 2026.[^npo-cr]

Pro tento příběh jsou důležité hlavně tři věci:

1) Fialova vláda nepřišla k prázdnému papíru, ale k už schválenému plánu s milníky.
2) Nesplnění milníků neznamená jen mediální problém, ale riziko neproplacení části prostředků.
3) Mezi projekty navázané na NPO patřil i eTurista.

Zde je potřeba udělat jednu odbočku: český stát má rozbité financování rozvoje. Běžný rozpočet často pokrývá hlavně provoz — mzdy, budovy, povinné výdaje, udržování starých systémů při životě. Skutečný rozvoj se pak lepí z dotací, evropských programů a mimořádných zdrojů.

U velkých projektů to dává smysl. Nová kanalizace má jasný dopad, jednu větší zakázku a výsledek, který se dá ukázat na mapě. Jenže u menších změn se celý mechanismus stává kanónem na vrabce. Chcete opravit náves, zjednodušit formulář nebo vylepšit interní systém? Administrativa kolem peněz může být větší než samotný projekt.

Trpí tím obce i ministerstva. Proto ztráta peněz z NPO není ztráta nějakého bonusu navíc. Často jde o peníze, se kterými už resort počítá jako s běžnou součástí rozpočtu. A když žádá o národní peníze, ministerstvo financí mu řekne: proč chcete víc, vždyť máte NPO.

To je pro příběh eTuristy důležité. Jakmile je projekt jednou zanesený do NPO, není to jen „nápad ministerstva“. Stane se z něj součást smluveného harmonogramu. A když se pak ukáže, že architektura nebo legislativa nejsou ideální, nejde jednoduše říct: tak to celé zastavíme a za dva roky vymyslíme znovu. Tlak na plnění milníků začne deformovat i normální odbornou debatu.

## Jaký problém měl eTurista řešit

Myšlenka eTuristy je na první pohled jednoduchá: ubytovatelé dnes mají povinnost vykazovat spoustu věcí o ubytovaných hostech. Nejvýraznější je přítomnost cizinců pro cizineckou policii a evidence kvůli místnímu poplatku z pobytu pro obec. Proto po vás v hotelu vždy chtějí občanku nebo pas.

Důležité je říct, že sběr údajů o hostech není nový. Už dnes existují dvě hlavní agendy:

- **Poplatek z pobytu:** podle zákona o místních poplatcích vede poskytovatel úplatného pobytu evidenční knihu. Zapisuje mimo jiné začátek a konec pobytu, jméno, adresu, datum narození, druh a číslo dokladu, výši vybraného poplatku nebo důvod osvobození. Evidenční knihu uchovává 6 let.[^mistni-poplatky]
- **Pobyt cizinců:** podle zákona o pobytu cizinců má ubytovatel povinnost oznámit ubytování cizince policii zpravidla do 3 pracovních dnů a vést domovní knihu. I zde se uchovává agenda typicky 6 let.[^cizinci-zakon]

Současný stav tedy není ideální ani z pohledu podnikatelů, ani z pohledu soukromí. Ubytovatel často zapisuje podobné údaje vícekrát. Část agendy je papírová, část digitální, část se posílá policii, část se drží kvůli obci. Host předává doklad na recepci a většinou netuší, kdo ho vidí, zda si ho někdo kopíruje a jak dlouho údaje zůstanou uložené.

Správně uchopený eTurista měl tento stav zlepšit. Ubytovatel by údaje zadal jednou a systém by správným institucím předal jen to, co opravdu potřebují. Obec nepotřebuje kompletní identitu každého hosta v rozsahu cizinecké policie. Statistik nepotřebuje číslo dokladu. A pokud už stát nějaký údaj zpracovává, má být jasné proč, kdo k němu přistoupil a kdy se smaže.

To je zásadní rozdíl oproti části veřejné debaty. Kritici často mluvili tak, jako by stát z ničeho nic vymyslel, že hotely budou sbírat doklady hostů. Jenže to už dělají. Reálná otázka tedy nestojí „sbírat, nebo nesbírat“, ale:

1) jaké údaje jsou opravdu nutné,
2) kdo k nim má mít přístup,
3) jak dlouho se mají uchovávat,
4) zda digitalizace papír ruší, nebo jen přidává další vrstvu,
5) a zda systém nevytváří centrální databázi, která je lákavá pro úplně jiné účely.

Tento typ systému je v zahraničí běžný. ČR podle dostupných informací úzce spolupracovala například s Rakouskem a pilotní provoz probíhal v Krkonoších. Do toho později vstoupilo i evropské nařízení o krátkodobých pronájmech přes platformy typu Airbnb. To přidává další legislativní vrstvu, ale pro tento příběh není podstatné. Klíčové je, že český eTurista měl řešit hlavně domácí problém: jak nahradit roztříštěné evidence jedním rozumným, bezpečným a srozumitelným procesem.

Ani u eTuristy tedy nešlo o jeden izolovaný krok. Potřeba se propsala do NPO, následně do legislativy, veřejných zakázek, technické architektury, metodiky a provozu. Když se pak objeví oprávněná kritika, nestačí upravit jednu větu v tiskové zprávě. Musíte vědět, ve které vrstvě systému má změna proběhnout.

## Anatomie kritiky: V čem měli odpůrci pravdu?

Objevila se však kritika. Pro MMR nejhorší možná, protože kombinovala naprosto oprávněné obavy, které bylo třeba řešit, s absolutním nepochopením konceptů a až smyšlenými věcmi. Tím se rozmělňovala pozornost a energie všech.

Hlavní body kritiky bych shrnul takto:

- **Příliš široký sběr dat.**
  - Návrh působil dojmem, že se nejdřív sesbírá maximum údajů a až potom se nastaví, kdo co uvidí.
  - U citlivých osobních údajů má být postup opačný: nejdřív účel, potom nezbytný rozsah dat.

- **Riziko centrální databáze.**
  - Registr pobytů je citlivá věc.
  - Bez jasných pravidel přístupu a auditní stopy vzniká oprávněná obava z budoucího rozšiřování účelů.

- **Digitální kočkopes.**
  - Digitalizace má papír nahradit.
  - Pokud vznikne digitální evidence a vedle ní zůstane papírová kniha, je to jen další administrativa.[^nasepenize-eturista]

- **Nedůvěra ve funkčnost státu.**
  - Ubytovatelé se oprávněně bojí systému, který vypadne v sezoně, nepůjde napojit na jejich hotelové systémy a nakonec jim přidá práci.

- **Tlak NPO na termíny.**
  - U citlivého systému s osobními údaji je nebezpečné dodat „něco“, jen aby byl splněn milník.

Za mě tedy nebyl problém v samotné myšlence eTuristy. Problém byl v tom, že se dohromady potkaly citlivé osobní údaje, více účelů zpracování, tlak na milníky NPO, nedůvěra vůči státu a ne úplně přesvědčivě vysvětlená architektura.

## Pohled insidera

Tady je fér vyjasnit moji roli. Nebyl jsem ownerem eTuristy, neřídil jsem tým, veřejnou zakázku ani legislativu k cestovnímu ruchu. Byl jsem náměstkem Ivana Bartoše v jeho digitalizační agendě na Úřadu vlády. Zajímal jsem se o to ze stejného důvodu jako o jiné státní IT projekty: aby se to povedlo a aby se z dobré myšlenky nestal špatný systém.

Když se objevila veřejná kritika, reakce byla poměrně rychlá. Začali jsme řešit, co je věcná kritika, co je nedorozumění a kde návrh skutečně potřebuje opravit.

Část debaty přitom stála na chybném předpokladu, že „Bartoš vymyslel eTuristu“ a že správná odpověď má být jednoduché politické gesto: „zastavuji“. Jenže takhle ten projekt nevznikl. Navazoval na existující zákonné povinnosti, NPO, legislativu, veřejné zakázky a rozjetou technickou přípravu.

Důležité proto bylo nepřijít jen s jednoduchým „ne“. U podobného projektu nestačí říct: tohle celé zahoďte. A často to ani nejde bez dopadů na financování a další návazné projekty. Je potřeba rozplést, co patří do zákona, co do podzákonných předpisů, co do technické architektury, co do metodiky a co do provozních pravidel. Jinak se stane, že se sice deklaruje ochrana soukromí, ale v systému se fakticky nic nezmění — nebo naopak vznikne legislativní brzda, která znemožní i rozumnou digitalizaci.

Proto jsme navázali dialog s Iuridicum Remedium (IuRe), velmi renomovanou neziskovou organizací, která se dlouhodobě věnuje digitálním právům a ochraně soukromí. S nimi jsme návrh zákona a možné záruky probírali.

Co jsme reálně prosazovali“:

- **Účelová minimalizace dat:** Každá instituce dostane jen to, co legálně potřebuje. Obec nepotřebuje pas hosta pro poplatek, statistici nepotřebují jména.
- **Auditní stopa a Role-Based Access:** Každý přístup k datům musí být logovaný. Občan má vědět, který úředník se na jeho data díval a proč.
- **Bezvýznamové identifikátory:** Propojování agend (např. vnitro vs. místní poplatky) se nemá dít přes rodná čísla nebo plnou identitu, ale přes šifrované identifikátory.
- **Konec duplicit:** Pokud stát data digitalizuje, musí zákonem škrtnout povinnost vést paralelní papírovou knihu. Jinak je to jen digitální kočkopes.

To je však jen zadání pro změny. Ty samozřejmě musí probublat do všech částí projektu ke konkrétním lidem a také musí být projednány s dalšími stakeholdery.

A pak přišla politika. V září 2024 byl Ivan Bartoš odvolán z pozice vícepremiéra a tím jsme na další pokračování projektu ztratili vliv. Od té chvíle už bylo na MMR, jak agilně a poctivě nalezené úpravy zapracuje. To už jsem já ani Ivan neuměli ovlivnit.

Ve výsledku si myslím, že eTurista nemusel skončit jako symbol šmírování nebo byrokratického kočkopsa. Mohl být opraven s patřičnými zárukami. Ale právě na tom je vidět, jak křehké jsou státní digitální projekty: nestačí dobrý záměr, nestačí ani identifikovat problém. Musíte mít čas, politickou podporu, legislativní trpělivost a tým, který změny skutečně dotáhne.

## Závěr

eTurista pro mě není důkaz, že digitalizace je špatně. Současný papírový a roztříštěný stav je špatný pro ubytovatele, úřady i hosty. Jenže pokrok nevznikne tím, že všechny existující povinnosti nasypeme do jedné databáze.

Dobrá digitalizace má dělat opak: ptát se, které údaje jsou skutečně nutné, kdo je opravdu potřebuje a jak dlouho mají existovat. Má rušit duplicity, ne vytvářet digitální evidenci vedle papírové. Má být auditovatelná, vysvětlitelná a navržená tak, aby chránila občana i před budoucím pokušením státu používat data k jiným účelům.

Kritici eTuristy podle mě trefili podstatný bod: stát si u citlivých osobních údajů nemůže říct o důvěru jen tím, že slíbí dobré úmysly. Musí ji doložit architekturou, zákonnými zárukami a provozní praxí. V tom s nimi souhlasím. Zároveň ale nejde čekat, že se takový projekt změní druhý den po vydání článku a že se následné opravy propíšou do médií se stejnou intenzitou jako původní senzace. Odpovědí tedy nemá být rezignace na digitalizaci. Odpovědí má být lepší digitalizace.

Poučení z eTuristy je tedy širší než jeden registr pro ubytovatele. Digitální stát nemá být Velký bratr, který o nás ví všechno a rychleji. Má to být efektivní partner, který po nás chce méně věcí, s daty zachází s úzkostlivou opatrností a umí kdykoliv složit účty z toho, proč je vůbec potřebuje.

[^npo-ek]: [Czechia’s recovery and resilience plan, European Commission](https://commission.europa.eu/business-economy-euro/economic-recovery/recovery-and-resilience-facility/country-pages/czechias-recovery-and-resilience-plan_en)
[^npo-cr]: [Národní plán obnovy – oficiální web](https://planobnovy.gov.cz/)
[^mistni-poplatky]: [Zákon č. 565/1990 Sb., o místních poplatcích, § 3g](https://www.zakonyprolidi.cz/cs/1990-565#p3g)
[^cizinci-zakon]: [Zákon č. 326/1999 Sb., o pobytu cizinců, § 97 a § 100–102](https://www.zakonyprolidi.cz/cs/1999-326#p97)
[^nasepenize-eturista]: [NašePeníze.cz: Konec soukromí na dovolené? Hoteliéři mají hlásit hosty dvojím způsobem](https://www.nasepenize.cz/konec-soukromi-na-dovolene-hotelieri-maji-hlasit-hosty-dvojim-zpusobem-hrozi-uredni-silenstvi-595648)
