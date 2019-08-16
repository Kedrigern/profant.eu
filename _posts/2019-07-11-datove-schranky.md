---
layout:     post
title:      "Deset let datových schránek v ČR"
date:       2019-07-11 10:00:00 +0100
categories: Egovernment
comments:   true
tags:       [egovernment, digitalizace, informatika, veřejná správa]
img:        logo-ds.jpg
author:     Ondřej Profant
---

Datové schránky oslavily 1. července 2019 deset let své existence v Česku. Mezi lidmi však ani po této době nejsou přijímány příliš kladně. Často jsou vnímány jako nepraktická alternativa emailu pro komunikaci s veřejnou správou. Jejich pověsti pak nepřispěl zejména fakt, že z jejich zřízení plyne povinnost řešit některé úkony s úřady výhradně přes ni (např. podávání daňových přiznání).

<!--more-->

### K čemu slouží?

Z pohledu uživatele je komunikace prostřednictvím datových schránek (DS) skutečně podobná kostrbatějšímu emailu. Uživatel dostane přidělenou unikátní adresu (ID), ze které může poslat zprávu každému jinému uživateli DS. Komunikace s orgány veřejné moci (OVM) je zdarma. Jedná se nejen o orgány státu, jako jsou ministerstva, soudy, policie a různé správní úřady, ale i obce a kraje a jejich orgány anebo třeba školy. Komunikace se soukromoprávními subjekty je zpoplatněna a lze ji vypnout. Datové zprávy nemají tělo, jejich obsah je tvořen pouze přílohami (typicky PDF nebo XML). Datová zpráva je ve schránce uchovávána po omezenou dobu 90 dní. Kapacita datové zprávy je 20 MB, v rámci komunikace o stavebním řízení se bude kapacita navyšovat.

K 21. červnu 2019 bylo aktivních 542 010 DS právnických osob (zřizovány povinně), 154 802 DS fyzických osob podnikajících a 142 038 DS fyzických osob[^1].

Celkově se tedy pro běžného občana nejedná o žádný zázrak, ale umožňuje to to důležité - předávat si ověřené dokumenty se státní správou. Velkým plusem je, že i strojově čitelné / strukturované dokumenty.

Výrazně silnější stránka datových schránek je na straně veřejné správy. Ta je totiž velmi rigidní a zvláště mezi sebou má problém komunikovat méně formální formou. Datové schránky nabízejí snadné propojení jakéhokoliv OVM s jakýmkoliv jiným. Čili dva úřady z druhé strany země si snadno, téměř v reálném čase, předají autentizovaně dokumenty, tedy bez pochybností o doručení a autorovi zprávy. Dané dokumenty mohou být i XML, čili následně je lze automaticky zpracovat. S trochou nadsázky se dá systém datových schránek označit za service bus veřejné správy.

### Hlavní problémy

Datové schránky[^2] mi celkově nepřipadají jako nejlepší koncept. Osobně si myslím, že se mělo jít spíše cestou certifikovaných emailů. Nicméně datové schránky už jednou máme a používat je lze. Spousta problémů vzniká jen ze způsobu použití. Například obsese úředníků v nepraktickém formátu PDF je až zarážející. 

Uživatele nejvíce trápí již zmíněná omezená doba uložení zprávy a omezení velikosti zprávy. Oboje je v dnešní době zcela směšné a je chybou MVČR, že tyto problémy neřeší.

I přes konzervativnost celého systému a nemalou cenu je však komunikace přes datové schránky **levnější než klasická pošta**. Veřejná správa platí 2,5 Kč za zprávu. Pokud se rozpočítají fixní paušální výdaje, tak tato cena stoupne na 4,2 Kč[^3]. Pro soukromníka je cena jedné zprávy 18 Kč, doporučené psaní v listinné podobě od ČP stojí 44 Kč[^4].

Velký potenciál datových schránek tkví v použití standardizovaných formátů datových zpráv. Je tak možné zjednodušit a automatizovat v podstatě každý úkon. A to jak mezi OVM navzájem, tak i pro komunikaci fyzických a právnických osob s veřejnou správou. Je však třeba, aby zodpovědné autority tyto standardy definovaly (například jako XML schémata) a naučily se je automatizovaně přijímat a zpracovávat. Pak mohou vzniknout (i externě) potřebné formuláře a napojení na externí agendové aplikace. Ze strany uživatele tento přístup vidíme například na portálu [Podej to](https://podejto.cz).

Nepraktické je rovněž počáteční nastavení datové schránky. V základním nastavení totiž vyžaduje změnu hesla každých 90 dnů, což je dnes i z bezpečnostního hlediska považováno za překonané. Naštěstí dnes již (po výtkách uživatelů) lze dodatečně nastavit neomezenou platnost hesla. Rovněž velice užitečná funkce notifikace emailem není v počátečním nastavení zapnutá a uživatel na ni není upozorněn.

### Tipy a triky

Pro větší pohodlí při užívání je třeba si datovou schránku přizpůsobit v jejím nastavení. Existuje naštěstí několik způsobů, jak se dá z uživatelského pohledu používání datových schránek vylepšit.

* Lze si nastavit upozornění o nových zprávách na mail
* CZ.nic vyrobil aplikaci Datovka, která je klientem k datovým schránkám podobným jako známe u mailů
* MVČR představilo aplikaci Mobilní klíč, která umožňuje přihlásit se k systému datových schránek přes mobil (nepotřebujete u sebe mít přihlašovací údaje)
* V Portálu občana lze spravovat více datovek najednou
* Portál občana poskytuje možnost archivace datových zpráv na neomezenou dobu v objemu do 500 MB (vyhnete se tak limitu 90 dní nebo nutnosti použít placenou službu České pošty Datový trezor[^5])

### Jaké kroky jsme učinili?

Datové schránky jako prostředek pro elektronickou komunikaci mezi občanem a státem jsou významným prvkem v konceptu českého e-Governmentu[^6]. Piráti se proto snaží prosazovat jejich širší využívání a posílit jejich legislativní rámec.

* Navrhli jsme rozšířit poněkud zastaralý seznam formátů (definováno ve vyhlášce)
Upozornili jsme na to, že přístupové údaje do dalších schránek (například právnických osob) se neodešlou do datovky, ale listinně, i když dotyčná osoba datovku má
* V rámci Youth Speak Up jsme jednali o fikci doručení
* Hlasovali jsme pro notifikaci konce platnosti řidičského průkazu prostřednictvím datové schránky
* Podíleli jsme se na připomínkování Portálu občana, který datové schránky využívá
* Kritizujeme nepřiměřenou cenu ISDS (jedním z viditelných důvodů je řetězec subdodavatelů) 
* Učíme úřady datové schránky častěji využívat (například při našem příchodu s námi nechtěla Sněmovna komunikovat elektronicky)
* Datovými schránkami se zabýváme v rámci Zákonu o právu na digitální službu

### Jaké další kroky chystáme?

Na datových schránkách je samozřejmě potřeba pracovat do budoucna, aby bylo jejich využívání stále jednodušší a posléze častější než listinná komunikace. Chystáme tedy i další kroky, kterými chceme přispět k jejich zlepšení.

* Navrhneme centrální registr XML schémat, abychom podpořili využívání strojově čitelných formátů
* Budeme podporovat snížení poplatků za odesílání datových zpráv, dlouhodobě pak budeme usilovat o jejich úplné zrušení

---

[^1]: [Deset let datových schránek v Česku](https://computerworld.cz/internet-a-komunikace/deset-let-datovych-schranek-v-cesku-55491)

[^2]: [Datové schránky](https://www.jaknainternet.cz/page/1264/datove-schranky/)

[^3]: Informace z odboru egovernmentu MVČR

[^4]: [Ceník služeb České pošty platný k 1. 6. 2019](https://www.ceskaposta.cz/ke-stazeni/cenik-sluzeb-ceske-posty)

[^5]: [Jak funguje a co nabízí Portál občana](https://www.lupa.cz/clanky/jak-funguje-a-co-nabizi-portal-obcana/)

[^6]: [Pilíře e-governmentu ČR](https://www.profant.eu/2018/pilire-egovernmentu-cr.html)
