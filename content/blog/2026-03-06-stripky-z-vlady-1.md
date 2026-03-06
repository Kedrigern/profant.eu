---
date: 2026-03-06
extra:
  author: Ondřej Profant
  comments: true
  img: mastodon.jpg
  layout: post
taxonomies:
  categories:
  - Vlada
  tags:
  - Fediverse
title: "Střípky z vlády 1: Fediverse"
---


V letech 2022–2024 jsem zastával roli náměstka vicepremiéra pro digitalizaci. V této serii se pokusím poodhalit nějaké ty historky z pozadí fungování státního kolosu. Dnes o digitální suverenitě a nasazování decentralizované sociální sítě.

<!-- more -->

## Digitální suverenita

Digitální suverenita je pro Evropu klíčová, obdobně jako energetická nezávislost. V letech 2022-2023 však byl naprosto dominujícím problémem ruský útok na Ukrajinu. Dokonce tehdejší ukrajinské zkušenosti často hovořily proti digitální suverenitě. Bombardovaná datová centra bleskurychle přenesly do hyperscale cloudu. Provoz na západě jim v této oblasti rozvázal ruce. Což je naprosto pochopitelné v jejich situaci. Satelitní internet byl také velkou pomocí - až do momentu kdy se Elon Musk rozhodl mačkat vypínač a narušovat vojenské operace jak se mu zlíbí. Další prozření přišlo se [stíhačkami F16][F16], kde USA vědomě narušili jejich fungování.

Tvrdé poučení je, že digitální suverenita je nezbytná, avšak nevybuduje se za den. Klíčové je držet si know how a mít seriozní partnery.

Piráti toto téma od svého vzniku řeší. Hezky je to vidět třeba na pirátské infrastruktuře. Pojďme se však podívat na to jak i jednoduchá úloha může být náročnou v kontextu státní správy.

## Mastodon a důležitost informačních zdrojů

V odborné sekci Pirátů zvedl Jan Korbel téma nasazení Mastodonu pro stát. Společně jsme vypracovali dokument, který zmapoval co to obnáší a jaké to má výhody a nevýhody. Idea je jednoduchá - nasadí se Mastodon na doméně info.gov.cz, účty tam budou mít jen státní instituce. Občan má tedy jistotu, že sleduje pouze oficiální zprávy a ne parodické účty, platforma je z principu otevřená, čili ji jde snadno sledovat mnoha způsoby. Další výhodou je, že by šlo vyhledávat jen mezi oficiálními účty. Mastodon spadá pod Fediverse a jde snadno sledovat obsah mezi instancemi - tedy občan má účet na kterékoliv jiné a přidá si profily, které ho zajímají, ale vidí u nich, že pochází z oficiální instance. Díky tomu stát není závislý na žádné další straně. Má opensource software, snadno ho může sám nasadit a spravovat.

Rok 2025 ukázal jak moc je toto klíčové. V USA došlo ke změně a jedna z opor Trumpova režimu jsou technologičtí oligarchové. Trumpova politika je založena na arogantní nenávisti (obdobně jako Ruská) a pro takovou emoci jsou sociální sítě naprosto klíčovým parťákem. Toto téma dlouhodobě řeší skvělý podcast [Kanárci v síti][Kanárci v síti]. Byly časy, kdy Barack Obama přišel na Twitter a mimo jiné s jeho pomocí se stal prezidentem USA. V dnešní době nový majitel bývalého Twitteru Elon Musk udělal z této sociální sítě naprostou žumpu. Sám aktivně šíří nenávistný obsah a uměle si zvyšuje dosah (jeho příspěvky vidí více lidí). Samozřejmě snadným řešením je odejít - jako jsem před lety učinil já. Ale problém je, když třeba podnikáte a potřebujete na takových místech být. A stejně tak je problém, kde brát informace - velké firmy i stát si navykly být právě na Twitteru, později X.

Jenže tyto naprosto markantní případy v době naší diskuse ještě nebyly. Samozřejmě lidé, kteří se tématikou zabývali věděli jak škodlivé jsou algoritmy Facebooku, Youtube apod., ale v české veřejné debatě toto téma bylo naprosto okrajové a mainstreamové zdroje k této problematice nebyly.

### Ideální scénář

1) **Potřeba:** Cokoliv ve veřejné správě by samozřejmě mělo vycházet z jasné potřeby, kterou do požadavku formuluje někdo za danou oblast zodpovědný. V tomto případě by se měly ozvat: poradce pro národní bezpečnost, NUKIB - digitální suverenita (např. problematika identit v externích systémech) a zvláště Centrum proti hybridním hrozbám MV ČR. 
2) **Úkol:** Potřeba by měla být vyřčena na Vládě. Samozřejmě potřeba by byla širší, zaměřme se jen na část relevantní pro Mastodon. Vláda by se usnesla, že Vícepremiér pro digitalizaci připraví řešení. Mohlo by se jednat i o jiného člena vlády třeba Ministra vnitra, ale personálně by to takto dávalo větší smysl.
3) **Technická realizace:** Vícepremiér by svolal jednání. MVČR a NUKIB by řekly bezpečnostní předpoklady. S DIA by se dohodl provoz. A v neposlední řadě by se dohodl owner projektu, který by mimo jiné dělal osvětu, řešil spory apod. Náročné by bylo řešit automatickou správu identit, toto by se nejspíš v reálu řešilo ručně.
4) **Dlouhodobá realizace:** Důležité je, že práce nekončí nasazením platformy a vypořádáním se s porodními bolestmi. Enormní kus práce by bylo dostat orgány státní správy na tuto instanci a ohlídat, že tam obsah opravdu dávají. Jasně asi bychom to nechtěli 1:1 s Instagramem, ale třeba téměř 1:1 s X ano.

### Realita aneb co se stalo

Problém nastal hned na počátku. Potřebu nikdo vyjma Pirátů a úzce zaměřené odborné veřejnosti nevnímal. Poradce pro národní bezpečnost Tomáš Pojar vysloveně a opakovaně téma bagatelizoval. Tedy ani nemělo moc smysl jít na Vládu.

Strávil jsem nějaký čas snahou to i tak realizovat, ale DIA vznikala a byla notoricky přetížená. Priorit bylo moc. Rozhodně odmítala cokoliv jiného než elementární provoz. 

Neměli jsme ani jednu páku na další instituce. Problém se ještě prohluboval tím, že byla potřeba kooperace tiskových odborů, které jsou samozřejmě úzce spjaté s politickou reprezentací a poměrně nepokrytě nechtějí spolupracovat s jinou politickou stranou. V reálu tak nebyl skoro nikdo, kdo by byl ochoten danou instanci dobrovolně využívat. 

Projekt by tedy skončil tím, že by měl náklady a byly by tam 3 dlouhodobě spíš nedůležité účty a další vláda by ho zrušila. Stejně jako se stalo webu https://digitalnicesko.gov.cz, který jsme převzali od Babišovy vlády, rozvíjeli a další Babišova vláda ho zrušila.

Pikantní ilustrací celé situace je samotné Centrum proti hybridním hrozbám MV ČR. Instituce, která by měla být v čele boje za informační bezpečnost, má na svém webu jediný odkaz na sociální síť – a to na X (dříve Twitter), kde navíc ani aktivně nepřispívá. Orgán zodpovědný za boj s hybridními hrozbami tak sám nemá funkční komunikační kanál nezávislý na platformě technologického oligarchy.

## Co si z toho odnést

Příběh státního Mastodonu ukazuje širší problém české státní správy: i když máte dobré řešení, bez politické vůle a bez vnímané potřeby ho neprosadíte. V roce 2023 bylo téma digitální suverenity pro většinu politiků abstraktní. V roce 2025 už je bolestně konkrétní – stát komunikuje na platformě, kterou ovládá člověk aktivně podporující dezinformace a zasahující do geopolitiky.

Poučení je dvojí. Za prvé, budovat nezávislou infrastrukturu je třeba v klidných časech, ne až když hoří. Za druhé, i ten nejtechničtější projekt stojí a padá s lidmi – pokud tiskoví mluvčí a politická reprezentace nechtějí spolupracovat, sebelepší technologie nepomůže.

Federalizovaná sociální síť pro státní instituce zůstává otevřeným úkolem. Kdo ho zvedne?


[F16]: https://www.forbes.com/sites/davidaxe/2025/03/07/france-to-the-rescue-french-made-mirage-2000-jets-could-become-ukraines-most-important-aerial-radar-jammers/
[Kanárci v síti]: https://ceskepodcasty.cz/podcast/kanarci-v-siti
