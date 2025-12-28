---
aliases:
- /2020/formulare.html
date: 2020-04-14
extra:
  author: Bára Soukupová, Ondřej Profant
  comments: true
  img: koduj.jpg
  layout: post
taxonomies:
  categories:
  - Digitalizace
  tags:
  - egovernment
  - digitalizace
title: 'Digitalizace: zaspané roky nedoženeme za měsíc'
---

Současná krize s sebou přináší dosud nevídaný nápor na státní správu, ve velké míře pak speciálně na náš sociální systém. Úřady nejsou připraveny na masový příjem žádostí o podporu a pod jejich náporem lehce kolabují. Přitom na podobnou situaci mohly být připraveny daleko lépe.

<!--more-->

Již téměř 10 let fungují dva klíčové prvky českého e-governmentu - [datové schránky](https://www.profant.eu/2019/datove-schranky.html) a základní registry. Datové schránky mohou zabezpečit komunikaci mezi všemi občany, firmami a úřady. Základní registry pak tvoří jakousi bazální databázi nejdůležitějších entit ve státě, hlavně tedy osob. Na těchto základech tak státní správa může již dekádu stavět specializované systémy pro jednotlivé agendy a racionalizovat a zefektivinit svůj přístup k nim. Úřady však po většinu této doby pro to dělaly jen velmi málo. V běžném provozu to tak nevadilo. Léta neměnné postupy se lidé naučily, údaje se vypisovaly do ručně či tiskem do formulářů, a když něco nebylo jasné, konzultovalo se osobně. Současné situaci však tyto staré metody nevyhovují a také kapacitně nestačí. Pojďme si ukázat současné problémy na několika případech.

## Hlavní problém - identita

Stejně jako u papírového podání, kde je garancí podpis, je nutné i u elektronického postupu nějak [ověřit identitu](https://www.profant.eu/2019/sonia.html). K tomu měly od začátku sloužit datové schránky, později se přidala i e-občanka a v budoucnu se počítá s propojením s elektronickým bankovnictvím (2021). Přihlašování ke státnímu e-governmentu se zastřešilo pod [NIA](https://www.eidentita.cz/). Řada chyb však způsobila, že dnes, téměř 11 let po spuštění datových schránek, má přístup k nějaké formě elektronické identity méně než 10 % populace. Datové schránky od začátku provázela negativní reklama, spojená hlavně s povinností vlastníků datových schránek komunikovat výhradně přes ni, a tak si ji dobrovolně zřídilo jen malé množství fyzických osob (méně než 200 tisíc). Většina datových schránek je stále firemní. Přitom zřízení datové schránky není složité - zabere průměrně 5 minut na CzechPOINTu.

Problémy provázejí i e-občanky. Uživatelsky nepřehledné množství kódů (až 5), které je třeba zadat při jejich aktivaci, úředníci a úřednice téměř až odrazující občany od jejich aktivace a potřeba zakoupení externí čtečky karet způsobují, že většina čipů občanek stále zůstává neaktivovaných. Vinu nese i Ministerstvo vnitra, které nadále odmítá bezkontaktní čipy. Ty by přitom umožnily fungování ve spolupráci s mobilem a odpadla by tak mimojiné nutnost kupovat čtečku karet.

Současná malá dostupnost elektronické identity způsobuje, že jakkoliv chytré řešení nyní úřady představí, stejně většina lidí musí výsledek vytisknout a poslat poštou, případně donést na úřad osobně.

## Úřad práce

Těžiště působení úřadů práce se za poslední roky přesunulo více směrem k poskytování sociálních dávek. V souvislosti s aktuální situací je jedná hlavně o mimořádnou okamžitou pomoc (MOP). Úřad práce má formuláře zveřejněné na svých stránkách a [MOP není výjimkou](https://www.mpsv.cz/web/cz/-/zadost-o-mimoradnou-okamzitou-pomoc). Při tvorbě těchto “interaktivních” formulářů se však postupovalo principem “co na papíře, to na webu”. Formulář tak neumožňuje přihlášení přes NIA, načtení informací o žadateli (jména, adresy, příbuzné) ze základních registrů ani rozumné našeptávání adres. Hlavně však není uživatelsky přívětivý a srozumitelný - žadatel neví, co a v jakém rozsahu má kam vyplnit, což způsobuje velkou chybovost vyplněných formulářů a pracnost jejich pozdější oprav. Zejména vhodný by byl strukturovanější popis situace, ve které se žadatel ocitl. Veřejným tajemstvím pak je, že i digitálně vyplněné dotazníky přeťukávají pracovníci Úřadů práce do systému ručně.

Během víkendu jsme v systému DocAssemble udělali [ideový návrh nového řešení](https://bit.ly/2R3SyVZ), který se vyznačuje hlavně pozvolným provedením žadatele celým procesem. Vedení formulářů v tomto open source systému navíc umožňuje snadnou modifikovatelnost dotazníků a možnosti větvení. Uživatel je tak tázán jen na informace, které se ho konkrétně týkají a není zatěžován stovkami políček, z nichž většinu nepotřebuje (jako například v současném daňovém přiznáním).

## Antivirus

Program [Antivirus](https://antivirus.mpsv.cz/) pro zaměstnavatele je naopak ukázkou, že srozumitelnou, jednoduchou a dobře popsanou žádost umí rychle udělat i MPSV, když je k tomu vůle. Web zvládá automaticky vyplňovat některé údaje, má srozumitelné UX a díky responzivnímu designu je přehledný i na mobilu. Nezvládá ale doplnění všech údajů - například právní formy nebo rodného čísla (jehož nutnost je zde diskutabilní). Formulář chce na závěr přiložit doklad o vlastníkovi bankovního účtu, tedy něco, co lze vyčíst z Centrální evidence účtů. Nutnost vyplnění těchto údajů, které již stát někde má, tak uživatelskou přívětivost snižuje.
Pokud by bylo implementováno přihlášení skrz NIA, které by mělo být u podobných aplikací standardem, šlo by snadno pracovat i s neveřejnými údaji.

## Kompenzační bonus - program Pětadvacítka

Program Pětadvacítka, který poskytuje kompenzační bonus až 25 000 Kč pro živnostníky, se hned po svém spuštění 10.4. stal předmětem velkého zájmu. Finanční správa k němu nejprve zveřejnila ”interaktivní” [formulář PDF](https://ouc.financnisprava.cz/osvc25/Zadost_o_bonus_pro_OSVC_bez_zastupce.pdf), který je spustitelný jen a pouze v Adobe Acrobat Reader. Jediná interaktivita tohoto formuláře navíc spočívala ve vyplnění emailu na příslušné pracoviště Finančního úřadu, kam je třeba žádost poslat. Pod který úřad spadáte, si ale musíte zjistit sami jinak. Kromě toho šlo opět o formu “co na papíře, to na webu”.
Příznačné je, jak sama finanční správa tuto formu žádosti komentuje:
> První zveřejněný formát žádosti byl přizpůsoben formě očekávané cílovou skupinou OSVČ: „aby to vypadalo jako formulář“, neboť to byl jeden z nejčastějších podnětů přijímaný na zřízených informačních linkách Finanční správy.

Jinými slovy: děláme uživatelsky nepřívětivé formuláře, protože takové uživatelé očekávají.

Prostřednictvím DocAssemble jsme začali připravovat alternativu, avšak Finanční správa nás naštěstí sama předběhla. Během jednoho dne měla hotový [nový formulář](https://ouc.financnisprava.cz/kompenzace), který je značně příjemnější. Avšak i ten by bylo možné vylepšit:
- Formulář načítá data, ale pouze z veřejného přístupu k ARES. Nezvládne tak doplnit třeba DIČ či datum narození. DIČ by šlo implementovat při přihlášení datovkou či skrze NIA. Datum narození živnostníků zveřejňuje sám stát v jiném dotazu.
- Formulář nedokáže podle IČ a adresy určit, k jakému finančnímu úřadu žadatel náleží.
- Formulář nutí uživatele vyplnit jak kód banky, tak i její název.
- Nevaliduje - dovolí vyplnit špatné DIČ
- Naopak závěrečná shrnující stránka s možnostmi podání si zaslouží pochvalu, stejně jako přehledné UX a responzivní design.

## Srovnání formulářů

| **žádost** | MOP        | Antivirus | Pětadvacítka  |
|------------|------------|-----------|---------------|
| **instituce**  | Úřad práce | MPSV | Finanční správa |
| **odkaz**      | [zde](https://www.mpsv.cz/web/cz/-/zadost-o-mimoradnou-okamzitou-pomoc) | [zde](https://antivirus.mpsv.cz/) | [zde](https://ouc.financnisprava.cz/kompenzace) |
| **přihlášení NIA** | ne | ne | ne |
| **možnosti poslání**  | datovka, email s el. podpisem,  pošta | datovka, email s el. podpisem | datovka, emailem s naskenovaným podpisem, pošta |
| **předvyplnění dat** | ne | jen veřejné rejstříky | jen veřejné rejstříky |
| **validace dat** | některých | nedostatečná | ano |
| **zbytečně požadované údaje** | mnoho (zejména k identitě a adrese žadatele) | rodné číslo, právní forma, doklad o vlastníkovi účtu | DIČ, rodné číslo, název banky, územní pracoviště Finančního úřadu |
| **přehledné UX** | ne | ano | ano |
| **responzivní design** | ne | ano | ano |
| **dodavatel** | Software602, OKsystem | [OKsystem](https://www.oksystem.com/cz/aktuality/oksystem-pomaha-v-dobe-krize-pro-mpsv-zajisti-upravy-systemu-pro-vyplatu-socialnich-davek-bez-naroku-na-odmenu) | ? |


## Ponaučení

Současné situace přinesla několik poznatků k digitalizaci veřejné správě:

- Na příkladu Antiviru a Pětadvacítky se ukázalo, že veřejná správa dokáže velice promptně vytvářet moderní a uživatelsky přívětivé rozhraní pro podávání žádostí. Vyvstává otázka, proč se to děje až nyní, pět minut po dvanácté, když tuto úroveň mohla již několik let mít veškerá komunikace s veřejnou správou?
- Většina služeb této úrovně nedosahuje, jak je zřejmé na MOP nebo na daňovém přiznání.
- Stát by měl ke svým službám poskytovat veřejně dostupné API, aby umožnil připojení dalších služeb a vznik alternativních formulářů. Na tomto principu funguje například služba [podejto](https://podejto.cz/). V zahraničí běžně najdeme různé formuláře veřejné správy např. v internetovém bankovnictví. Budeme navrhovat přidání této povinnosti do zákona.
- Propojení státních databází stále nefunguje správně - formuláře neumějí načítat neveřejná data (DIČ, datum narození, telefon, email), nutí vyplňovat zbytečné položky (jméno banky) a nedokáží určit příslušnost k místnímu pracovišti úřadu.
- Místní struktura úřadů neodpovídá potřebě propojeného digitálního světa. Mnoho agend veřejné správy má odlišnou místní strukturu od administrativního členění (Správa sociálního zabezpečení, Úřad práce, Finanční úřad, ...). Pokud tato instituce vyžaduje podání na místně příslušnou pobočku, je často problém zjistit, která to je - ani sama Finanční správa pak na základě vašeho IČ a adresy nedokáže poradit, ke kterému jejímu pracovišti spadáte. Řešením je zřízení centrální podatelny těchto úřadů.
- Roztříštěnost úřadů a nepřehlednost jejich webových stránek často brání v orientaci, na co má žadatel nárok. To je zřejmé například v oblasti sociálních dávek, kde jsme proto připravili přehledný web [SocialniSystem.cz](https://socialnisystem.pirati.cz/).  
- Hlavním problémem všech řešení je digitální identita. Přístup k digitálním identitním prostředkům (datová schránka, e-občanka) nemá více jak 90 % občanů. Jakkoliv chytré řešení bude bez ověřené identity pouze polovičaté.

Systém formulářů je administrativní pomůcka a je to zároveň jedno z nejčastějších rozhraní komunikace mezi občany a státem. Některé formuláře svoji formou spíše odrazují. To ale rozhodně nemá být jejich funkce - naopak mají motivovat žadatele, aby se nebáli ozvali. Už samo o sobě podání žádosti o pomoc může být pro někoho psychicky těžké, snažme se místo komplikací vycházet lidem co nejvíce vstříc. Stejně jako v mezilidských vztazích je i ve vztahu občanů a státu komunikace a její forma důležitá. Chceme zdravý stát se zdravou ekonomikou, který je tu pro lidi.

Veškeré úspěchy Pirátů v oblasti digitalizace najdete na [pirati.cz](https://www.pirati.cz/vysledky/#type=resorts&datefilter2=all&resorty-select-2=resort-informatika). Pracujeme, předkládáme, ale vládní většina blokuje.