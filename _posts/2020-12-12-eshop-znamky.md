---
layout:     post
title:      "Eshop na dálniční známky aneb Jak nedělat egovernment"
date:       2020-12-12 19:00:00 +0100
categories: Egovernment
comments:   true
tags:       [egovernment, digitalizace]
img:        edalnice2.jpg
author:     Ondřej Profant
---

Eshop na dálniční známky vyvolal vášně už na začátku roku, kdy byla zrušena původní zakázka na jeho realizaci. Problémy s eshopem ale vyvrcholily s jeho oficálním spuštěním, které doprovázala řada technických selhání způsobených špatnými rozhodnutími.

<!--more-->

Přestože Češi jsou "eshopovou velmocí" (když se na to díváme z pohledu počtu eshopů na jednoho obyvatele), stát pod vedením Babiše není schopen provozovat ani ten nejjednodušší obchod se třemi položkami. Kauza s prodejem dalničních známek online dobře ukazuje, jak Babišova vláda v praxi přistupuje k digitalizaci.

Se zakázkou na systém nákupu dálničních známek online se pojí spousta špatných kroků více státních institucí, největší podíl na zpackaném startu projektu ale nese Babišova vláda. 

Pro rekapitulaci shrnutí základních informací:

1) SFDI publikoval v lednu 2020 zcela nesmyslně napsanou a utajenou zakázku. Se zakázkou se nesměl seznámit dokonce ani ředitel fondu, který zakázku vypisoval.

2) Po následném mediálním humbuku premiér Andrej Babiš odvolal ministra dopravy Vladimíra Kremlíka (za ANO). A nahradil ho dvojministrem Havlíčkem (za ANO). Nešetřil při tom hanlivými slovy na účet exministra a SFDI. Uchýlil se dokonce až k [podání trestního oznámení](https://www.idnes.cz/ekonomika/domaci/andrej-babis-e-shop-dalnicni-znamky-zakazka-trestni-oznameni-ministr-kremlik.A200203_121243_ekonomika_elka) z přesvědčení "že zakázka byla předražená, že jsme o tom nevěděli a SFDI ji dělal ve vlastním režimu".

3) Podnikatel Tomáš Vondráček s pomocí mnoha dalších odborníků uspořádal hackathon. Hackathon je hromadná akce, při které programátoři společně pracují na zadaném softwarovém produktu. Akce měla svou přípravnou architektonickou fázi a přes víkend se programovalo řešení.

4) Výsledkem hackhatonu je koncept řešení (proof of concept). Nejedná se tedy o hotový produkční kód, ale ukázku toho, jak to lze napsat, tedy jak rozvrhnout komponenty, jak spolu mají komunikovat, jaké nástroje využít apod. Myslím si, že výsledek práce je velmi dobrý vzhledem k rychlosti organizace a času na vývoj.

5) Výsledkem práce hackathonu je frontend a dva různé backendy. Jeden je postaven na komerčním frameworku, čili by se jeho použítím obcházela veřejná soutěž, a druhý je dělaný od píky. Ten je však v horším stavu. Což je ale docela normální stav po dvou dnech vývoje a jasně to prošlapává cesty.

6) Z bezpečnostního hlediska měla část výsledku své mouchy. To je samozřejmé vzhledem k tomu, že se jedná o výsledek práce za víkend. Nicméně pokud je mi známo, žádná z těchto chyb nebyla v návrhu, ale byly to věci, co se za pár týdnů testování dají zcela bez problémů odladit.

7) Ukázalo se, že velký problém je utajená část zadání. Ze všech stran jsme byli ujišťováni, že v ní není nic špatného. Postupně jsme se dobrali nejspíše pravdy, ale lajdáctví SFDI a BIS v této věci je skutečně nezměrné. Oficiální důvody by zcela jednoduše byly řešitelné poukázkou na dálniční známku. Státní orgány včetně bezpečnostních složek by jednoduše dostaly slevový kupon a SFDI by tak vůbec nemusel vědět, kdo je kdo.

8) Už v lednu se navíc [objevily informace o možném narušování soukromí plošným sledováním aut](https://www.pirati.cz/tiskove-zpravy/plosne-sledovani-aut-v-tendru-na-znamky.html), které mělo být součástí zakázky. To by směřovalo k plošnému sledování a tím pádem k zásadnímu narušení osobnostních práv všech občanů.

9) Stát dostal řešení z hackathonu, ale vůbec ho nevyužil. Namísto toho zakázku předal státnímu podniku Cendis. Což je stále lepší varianta než původní Asseco. Nicméně cena je pořád dost vysoká. Výhodou státního podniku tak snad bude alespoň možná budoucí flexibilita.

10) Cena je namísto [401 nově 309 milionů Kč](https://www.seznamzpravy.cz/clanek/elektronicke-dalnicni-znamky-jsou-vyhozene-penize-rika-hlidac-statu-131945). Což je stále zcela nesmyslná suma, pokud by zadání bylo rozumně připravené. SFDI jistě přijde se sofistikovaným zdůvodněním, proč to bylo třeba, avšak to vše za předpokladu špatné architektury řešení, které náklady zjevně prodražuje.

![edalnice screenshot 1](edalnice3.jpg "Chybové hlášky")

11) Technické řešení nového systému je postavené na CMS Wordpress s množstvím pluginů. Je vidět, že je vše šito horkou jehlou. Například ve vyhledávači Google se vám při hledání "edalnice" zobrazoval text "Takto bude vypadat text. Vyzkoušejte si jaká velikost textu vám bude vyhovovat. Zvětšete nebo zmenšete si text podle vašich potřeb." V konzoli webového prohlížeče se dále objevovaly různé chybové hlášky. Od projektu za sta miliony bych očekával mnohem více. Nejméně důsledné otestování před spuštěním (na to ani nejsou potřeba kvalifikovaní specialisté, ale zvládnou to bez problémů běžní referenti).

![edalnice screenshot 2](edalnice1.jpg "Text vyhledávače")

12) Celé řešení je však k ničemu, protože nerespektuje digitální cestu. Legislativa není uzpůsobena a není možno automaticky kontrolovat dálniční známky. Čili hlavní [cíl projektu a možná nejvyšší úspora zcela chybí](
https://www.piratskelisty.cz/clanek-3650-spusteni-elektronicke-dalnicni-znamky-skoncilo-fiaskem-projekt-za-stovky-milionu-selhava-na-novou-eru-na-dalnicich-zatim-zapomenme).

13) V momentě veřejného spuštění web nevydržel nápor uživatelů, a proto ho ministr raději nechal vypnout. To vypovídá hodně o schopnosti vlády udržovat důležité systémy v chodu (nebo je vůbec dokázat spustit).

14) Web také nerespektuje centrální egovernment. Takto významný portál by měl být na centrální státní doméně `.gov.cz`. Stejně tak web nerespektuje společný design, který nastavil [Portál občana](https://portal.gov.cz) a který převzaly například již datové schránky.

15) Na hackathonu vznikla i koncepce, že by stát provozoval primárně backend. Samotný prodej by zajistily běžné eshopy. Výhoda je, že by státní eshop nebyl pod takovou návštěvností a leccos by mu šlo odpustit. Kupon byste si pak mohli zakoupit ve svém oblíbeném eshopu (třeba společně s jinými nákupy). 

Sečteno a podtrženo -- stát nemá schopné IT specialisty, neumí odhadnout velikost projektu (nadsazuje), neumí komunikovat, neumí projekt vést mezioborově (tedy zároveň řešit legislativní, odborné a bezpečnostní požadavky) a ministr neumí provést základní srovnání. [Běžné eshopy se opravdu za 300 milionů nepořizují](https://www.facebook.com/ondrej.profant/posts/10218455076954914).
