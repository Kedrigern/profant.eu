---
layout:     post
title:      "Legislativa v oblasti egovernmentu v roce 2023"
date:       2023-02-25 10:00:00 +0100
categories: Digitalizace
comments:   true
tags:       [Egovernment, Digitalizace]
img:        rules.png
author:     Ondřej Profant
---

Když se průbojný a flexibilní svět IT střetne se světem rigidní a pevně dané legislativy, tak to zákonitě musí být náročné. Pojďme se podívat jak moc.

<!-- more -->

V Česku do zákonů uvádíme až chorobné detaily. Z pohledu úředníka i poslance je to relativně pochopitelné. Oni se snaží dosáhnout jasně daného cíle a obecná formulace je spíš na obtíž a navíc později může být vykládána jinak.

Vezměme si příklad [eshopu na dálniční známky](https://www.profant.eu/2020/eshop-znamky.html). Stručně řečeno vzniklo předražené řešení, které nebylo digital born. Tedy nebylo od začátku navrženo digitálně. Šlo o jednoduchou věc - skupiny, které mají dálniční známku ze zákona zdarma. Zde se prostě přepsalo řešení ze starého zákona, kde tyto skupiny nebyly problém. Vyskytly se dva problémy:
- SFDI vymyslelo, že vozidla bezpečnostních složek budou vedeny ve speciální databázi. Tím vznikl požadavek na databázi v utajovaném režimu, což je výrazně náročnější než bežná implementace databáze. Řešení je přitom tak prosté a známe ho z každého eshopu. Jednoduše by tyto instituce obdržely poukázky na dálniční známky zdarma a nikdo by neřešil pro jaká vozidla jsou. 
- Druhou skupinou byly ZTP u kterých je problém, že mohou jet jakýmkoliv vozidilem a mají užití zdarma. Zde je řešení složitější, ale jistě by se našlo. Např. možnost auto nahlásit v systému dočasně.

Z pohledů autorů legislativní novely je pochopitelné, že šli politicky nejsnažší cestou - seznam výjimek neměnili. Z pohledu digitalizace a hospodaření státu je z toho dodnes katastrofa.

Najít vyvážený stav není vždy lehké. Obecně se dá říci, že čím víc se úřadům něco nechce dělat, tím podrobněji je to popsáno v zákoně.

## Konkrétní zákony

Český egovernment je rozprostřen do mnoha zákonů a mnohé další se ho přímo dotýkají. Jsou to (převážně) tyto zákony:

- **právo na digitální služby** ([12/2020 Sb.][]): dnes zastřešující zákon, který na egov pohlíží z pohledu občana a také se v něm zřizuje Digitální a informační agentura (DIA).
- **informační systémy veřejné správy** ([361/2000 Sb.][]): pojednává o provozu agendových informačních systémů, využívání cloudu apod. Tedy egov z pohledu úředníka.
- **službách vytvářejících důvěru pro elektronické transakce** ([297/2016 Sb.][]): elektronické podpisy, více [viz samostatný článek][podpisy].
- **elektronické úkony a autorizovaná konverze dokumentů** ([300/2008 Sb.][]): datové schránky, tedy způsob jak (v dobrém slova smyslu) obejít elektronický podpis
- **základní registry** ([111/2009 Sb.][]): vymezení základních registrů
- **přístupnost webových stránek a mob. aplikací** ([99/2019 Sb.][]): primárně o přizpůsobení web. stránek pro lidi s postižením, ale jedná se o obecné zásady dobrého UI.

A úzce související:
- **svobodný přístup k informacím** ([106/1999 Sb.][]): v rámci něj jsou ukotvena otevřená data.
- **ochrana osobních údajů** ([439/2004 Sb.][])
- **veřejné zakázky** ([134/2016 Sb.][])
- **archivnictví a spisová služba** ([499/2004 Sb.][]): spisová služba je páteř každého úřadu, je to jeden z nejpoužívanějších informačních systémů, není divu že tedy dosti ovlivňuje chod celého úřadu.

Nad většinou z těchto zákonů jsou příslušné **Evropské normy**. U těch rozlišujeme směrnice (directive) a nařízení (regulation). Nařízení má přímou účinnost, příkladem je třeba General Data Protection Regulation (GDPR). Tedy není potřeba žádný český zákon, aby celé GDPR platilo. To mimojiné dává právní jistotu uživatelům práva napříč EU (tedy podmínky jsou stejné u nás stejně jako např. v Portugalsku). Přesto však speciální lokální zákon o ochraně osobních údajů máme, protože může být přesnější či se zabývat dalšími oblastmi. Směrnice je volnější a je potřeba jí transponovat do právního řádu každé země pro kterou je platná. Ano, směrnice navíc mohou být platné jen pro vybrané země.  

Pojďme se vrátit k českým zákonům. Podivejme, co zajímavého ukrývají:

### Zákon o právu na digitální služby

Relativně nový zákon (protlačili jsme v minulém volebním období). Zajímá nás verze [platná od dubna 2023][12/2020 Sb. dub] (tedy ta která již počítá s DIA). Ta mimojiné říká:

> **§ 2a** zřizuje DIA, včetně hlavních obrysů:
> (2) Agentura je ústředním správním úřadem pro elektronickou identifikaci a služby vytvářející důvěru a pro informační systémy veřejné správy.
(3) Agentura
> &nbsp;&nbsp; a) plní koordinační úlohu v oblasti digitálních služeb a digitálních úkonů podle tohoto zákona,
> &nbsp;&nbsp; b) plní koordinační úlohu pro informační technologie,
> &nbsp;&nbsp; c) plní koordinační úlohu v oblasti evidence a sdílení dat,
> &nbsp;&nbsp; d) zajišťuje systém podpory centrálních způsobů komunikace veřejné správy,
> &nbsp;&nbsp; e) zajišťuje odborný rozvoj, školení, sdílení znalostí, osvětu a vzdělávání v oblasti své působnosti,
> &nbsp;&nbsp; f) provozuje kompetenční centra.
(4) V čele Agentury je ředitel, kterého jmenuje a odvolává vláda na návrh člena vlády stojícího v čele Rady vlády pro informační společnost. Ředitel se považuje za služební orgán podle zákona o státní službě.
(5) Ředitel Agentury je oprávněn dávat státnímu zaměstnanci zařazenému k výkonu státní služby v Agentuře příkazy k výkonu státní služby podle zákona o státní službě.
>
> **§ 3 Právo na digitální službu**
(1) Uživatel služby má právo využívat digitální službu a orgán veřejné moci má povinnost poskytovat digitální službu.
>
> **§ 7 Právo na využívání údajů**
(1) Orgán veřejné moci nevyžaduje údaje vedené v základním registru nebo agendovém informačním systému, které jsou mu zpřístupněné pro výkon agendy nebo na základě souhlasu uživatele služby.
>
> **§ 13 Právo na technologickou neutralitu**
(1) Orgán veřejné moci zpřístupní digitální službu uživateli služby bez závislosti na konkrétní platformě či technologii, ledaže by takové řešení bylo nepřiměřeně ekonomicky náročné, nesplňovalo požadavky na bezpečnost informačního systému veřejné správy nebo mu bránil jiný právním předpisem chráněný veřejný zájem.
(2) Orgán veřejné moci poskytne uživateli výstupy digitální služby v otevřeném, a je-li to možné, též strojově čitelném formátu.
>
> **§ 14 Přechodná a závěrečná ustanovení**
(1) Nepodnikající fyzické osoby nemohou být nuceny využívat digitální služby nebo činit digitální úkony podle tohoto zákona.

### Zákon o informačních systémech veřejné správy

Jedná se o hlavní provozní zákon egovernmentu. Je zde definováno jak stát používá cloud, schvalovací proces hlavního architekta, role RVIS, vztah s dodavatelem … Z konkrétních paragrafů bych vypíchnul jen:

> HLAVA XI § 9e SOUČINNOST PROVOZOVATELE INFORMAČNÍHO SYSTÉMU VEŘEJNÉ SPRÁVY
(1) Provozovatel informačního systému veřejné správy předá bezodkladně na vyžádání správce informačního systému veřejné správy data a provozní údaje týkající se provozovaného informačního systému veřejné správy.
(2) Provozovatel informačního systému veřejné správy předá bezodkladně po ukončení provozování informačního systému veřejné správy data a provozní údaje týkající se provozovaného informačního systému veřejné správy správci informačního systému veřejné správy a kopie těchto dat a provozních údajů zlikviduje.

### Zákon o elektronických úkonech a autorizované konverzi dokumentů

Datová schránka je vlastně *service bus* celé veřejné správy. Tedy rozhraní po kterém komunikují instituce napříč státem. Centrální instituce může zaslat oficiální dokument i té nejmenší organizaci (např. mateřské školce). A obě strany mají jistotu, že si píší spolu, že dokument byl doručen a kdy přesně. To vše v reálném čase. Navíc té samé služby mohou využít občané i podnikatelé. Vůči veřejné správě (resp. orgánům veřejné moci - OVM) není služba zpoplatněna. Pro zasílání mezi soukromými subjekty je.

Klíčová část zákona je, zprávy a dokumenty nemusejí být elektronicky podepsané. Bez zvláštní úpravy tohoto zákona byste mohli doručit písemnost mailem nebo na flash disku, avšak dokumenty by mysely být podepsány [*uznávaným* či *kvalifikovaným* el. podpisem][podpisy].

### Zákon o základních registrech

Zavadí 4 základní registry:

- Registr obyvatel (ROB): fyzické osoby včetně některých cizinců
- Registr osob (ROS): právnické osobo
- Registr práv a povinností (RPP): eviduje práva a povinnosti, které typicky vyplývají z legislativy. Avšak není úplný, některé povinnosti jsou extrémně obecné a tedy nepřiliš vhodné pro strojové zpracování a ne všechny služby z něj čerpají data.
- Registr územní identifikace, adres a nemovitostí (RÚIAN): Katastralní mapa

K tomu ještě náleží IS ORG, který spravuje Úřad pro ochranu osobních údajů. Tento poslední dílek skládačky zajišťuje převod mezi identifikátory jednotlivých AIS na identifikátory jednotlivých ZR.

Jak přesně to funguje? Představme si, že máme registr řidičů. Tam chceme evidovat něco jako: "Ondřej Profant, narozen 2. 5. 1988, bydlištěm Praha, obdržel ŘO skupiny B dne 15. 4. 2010. Zkoušel instruktor Jan Novák. Byl mu vystaven ŘP s čislem XY, platný do 15. 4. 2025." To se zapíše do databáze. Nicméně v praxi se vynechá první část. Údaje o fyzické osobě se scvrknou na jedno číslo, např. 123456. A právě IS ORG zajistí, že z 123456 získáme jiné číslo, které vede do ROB, kde mám uvedené všechny údaje o dané fyzické osobě.

Proč tak složitě? Jde o ochranu osobních údajů a tzv. [normalizaci databází][normalizace db]. Pokud dojde k úniku dat z registru řidičů, tak v ideálním případě budou mít útočníci nicneříkající informaci: "123456 obdržel ŘO skupiny B dne 15. 4. 2010. Zkoušel instruktor Jan Novák. Byl mu vystaven ŘP s čislem XY, platný do 15. 4. 2025." a nikoliv propojení s fyzickou osobou, což sníží závažnost dopadů. Normalizace databází se zas používá proto, aby údaje byly na jednom místě. Tedy, když si změníte přijmení, tak se změní v ROB a nikde jinde to již není potřeba.

Zároveň je každý přístup do základních registrů evidován (logován).  A každý občan se může podívat, kdo k jeho údajům přistupoval a z jakého důvodu. Typickým důvodem je plnění povinností daného úřadu. Například policista při silniční kontrole přístoupí do registru osob (info o řidiči) a samozřejmě do mnohých dalších databází, ale ty mnohdy nemají takto striktně daná pravidla.



[12/2020 Sb.]: https://www.zakonyprolidi.cz/cs/2020-12
[12/2020 Sb. dub]: https://www.zakonyprolidi.cz/cs/2020-12/zneni-20230401
[361/2000 Sb.]: https://www.zakonyprolidi.cz/cs/2000-361
[297/2016 Sb.]: https://www.zakonyprolidi.cz/cs/2016-297
[300/2008 Sb.]: https://www.zakonyprolidi.cz/cs/2008-300
[111/2009 Sb.]: https://www.zakonyprolidi.cz/cs/2009-111
[99/2019 Sb.]: https://www.zakonyprolidi.cz/cs/2019-99
[439/2004 Sb.]: https://www.zakonyprolidi.cz/cs/2004-439
[134/2016 Sb.]: https://www.zakonyprolidi.cz/cs/2016-134
[106/1999 Sb.]: https://www.zakonyprolidi.cz/cs/1999-106
[499/2004 Sb.]: https://www.zakonyprolidi.cz/cs/2004-499
[podpisy]: https://www.profant.eu/2020/neni-podpis-jako-podpis.html
[normalizace db]: https://cs.wikipedia.org/wiki/Normalizace_datab%C3%A1ze
