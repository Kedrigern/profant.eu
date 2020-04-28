---
layout:     post
title:      "MVČR pokřivuje tržní prostředí"
date:       2020-04-14
categories: Digitalizace
comments:   true
tags:       [egovernment, digitalizace]
img:        vendor-lock-in-case-study.png
author:     Ondřej Profant
---

Ministerstvo Vnitra 27. 4. informovalo Vládu o prodloužení rámcové dohody se společností VMware. Tím se chystá i nadále zvýhodněním tohoto dodavatele  težce deformovat tržní prostředí. 

<!--more-->

Ministerstvo vnitra má 5 obdobných rámcových dohod. Se společnostmi VMware, Microsoft, IBM, Oracle a Cisco. V praxi to znamená, že zájemce o produkty těchto firem neabsolvuje administrativně náročné a zdlouhavé výběrové řízení, ale jen pošle objednávku na MVČR. Je skvělé, že se MVČR snaží ubrat úmornou administrativu z veřejných zakázek, ale v tomto případě ji ubírá jen u 5 společností a všichni zbylí jsou tím silně znevýhodněni.

Touto formou centrálního nákupu tak dochází k nežádoucí fixaci tržního prostředí. Noví hráči se nemají šanci zapojit do dodávek pro veřejnou správu. A netýká se to jen malých inovátorů. O zapojení do rámcových dohod požádali i velmi renomovaní dodavatelé, kteří mají silné zastoupení v soukromém sektoru a i ti byli odmítnuti. Veřejná správa tím ztrácí možnost získávat potřebný software za tržní cenu a dlouhodobě potlačuje inovaci, ze které by mohla jinak těžit.

Tento přístup škodí dokonce i konkurenci mezi zmíněnými třemi dodavateli, jelikož nejsou motivováni nabízet a propagovat ve veřejné správě vzájemně konkurenční produkty. Kdyby neudržovali status quo, tak by totiž mohli přijít o tato zlatá vejce, které rámcové dohody představují. Příkladem může být virtualizační software, který nabízí VMware i Microsoft, ale ve veřejné správě se setkáme téměř výhradně s VMware.

Tržní mechanismy neslouží jen ke snížení ceny a lepší uživatelské přívětivosti, pochopitelně ovlivňují i bezpečnost. Pokud je software zatížen příliš mnoha bezpečnostními přešlapy, tak zájem trhu poleví. To se však v tomto případě nemůže stát. Příkladem může být bezpečnostní chyba zveřejněná minulý týden, v rámci které lze získat administrátorská práva právě u VMware ([CVE-2020-3952](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-3952)). Hlavním problémem z pohledu bezpečnosti je však monokultura, která je snadno napadnutelná jako celek. Pokud je monokultura ještě navíc uzavřená, tak je nemožné pomoci opravit kritické chyby (například v případě krachu tvůrce se může stát, že není žádná legální možnost opravit chybu v programu).

Pokud má ministerstvo vnitra zájem na zjednodušení nákupů IT, tak může metodicky podporovat open source řešení u kterých není potřeba nakupovat licence a zároveň začít aktivně pečovat o to, aby v každé kategorii poptávaných řešení existovala reálná konkurence.

---

| Produkty firmy | Od  | Do  | Počet distributorů | Max plnění (s DPH) | Plnění, vč. DPH (zdroj: hlídač státu) |     |
| ------- | --: | --: | ---------------: | ----------------------------: | ----------------------------------------: |-|
| [VMWare](https://www.mvcr.cz/clanek/centralni-nakup-produktu-vmware.aspx) | září 2016 |září 2020	|5|	3 225 860 000,00|	[377 000 000,00](https://www.hlidacstatu.cz/Hledat?q=%22k+R%C3%A1mcov%C3%A9+smlouv%C4%9B+na+po%C5%99izov%C3%A1n%C3%AD+licenc%C3%AD+k+produkt%C5%AFm+VMware%22) |
[Microsoft](https://www.mvcr.cz/clanek/centralni-nakup-produktu-microsoft.aspx) |	prosinec 2018	|prosinec 2022|	4|	5 566 000 000,00	| [1 985 000 000,00](https://www.hlidacstatu.cz/Hledat?q=7.+12.+2018+%22k+R%C3%A1mcov%C3%A9+dohod%C4%9B+na+po%C5%99izov%C3%A1ni+produkt%C5%AF+Microsoft+%22+zverejneno%3A%5B2018-12-12+TO+*%5D) |
| [IBM](https://www.mvcr.cz/clanek/centralni-nakup-produktu-ibm.aspx)	| květen 2017|	květen 2021	|1, resp. 3*|	1 936 000 000,00|	[1 059 000 000,00](https://www.hlidacstatu.cz/Hledat?Q=%22k%20R%C3%A1mcov%C3%A9%20dohod%C4%9B%20na%20poskytnut%C3%AD%20licenc%C3%AD%20a%20podpory%20k%20produkt%C5%AFm%20IBM%22%20zverejneno%3A%5B2017-06-09%20TO%20%2A%5D&order=4) |
|[Oracle](https://www.mvcr.cz/clanek/ramcova-dohoda-oracle.aspx)	|leden 2020	|leden 2024|	5|	1 089 000 000,00	| [0,00](https://www.hlidacstatu.cz/Hledat?q=%22k+R%C3%A1mcov%C3%A9+dohod%C4%9B+na+po%C5%99izov%C3%A1n%C3%AD+produkt%C5%AF+Oracle%22+podepsano%3A%5B2020-01-01+TO+*%5D)** |
|[Cisco](https://www.mvcr.cz/clanek/centralni-nakup-produktu-cisco-systems.aspx)	|leden 2018	|leden 2022|	5|	1 452 000 000,00	| [79 000 000,00](https://www.hlidacstatu.cz/Hledat?q=%22k+R%C3%A1mcov%C3%A9+dohod%C4%9B+na+po%C5%99izov%C3%A1n%C3%AD+produkt%C5%AF+Oracle%22+podepsano%3A%5B2020-01-01+TO+*%5D) |
|[ICT komodity](https://www.mvcr.cz/clanek/centralni-nakup-ict-komodit.aspx) (DNS)*** |	březen 2019|	březen 2023|	16|	3 025 000 000,00|	[16 000 000,00](https://www.hlidacstatu.cz/Hledat?q=%22k+R%C3%A1mcov%C3%A9+dohod%C4%9B+na+po%C5%99izov%C3%A1n%C3%AD+produkt%C5%AF+Oracle%22+podepsano%3A%5B2020-01-01+TO+*%5D) |

\* vzniklo totiž „Sdružení pro zakázku pořizování licencí a podpory k produktům IBM“, kde jsou tři společníci - tři firmy

\** Zde viditelně nejde o nečerpání, ale špatné evidování.

\*** Dynamický nákupní systém prostřednictvím kterého je možno nakupovat stolní počítače, ploché monitory, přenosné počítače, klávesnice a myši. Rozdíl je, že [DNS](https://www.epravo.cz/top/clanky/dynamicky-nakupni-system-dle-nove-pravni-upravy-nejasnosti-a-rizika-dil-prvni-109566.html) má jasná pravidla jak se mohou zapojit další dodavatelé a není omezen okruh výrobců.

---

Je třeba si uvědomit rozdíl mezi výrobcem a dodavatelem. Výrobcem MS Windows je Microsoft. Ten velkoobchodně prodává licence svým partnerům / distributorům. Jenže licence je zcela virtuální produkt a nejsou téměř žádné náklady na její uskladnění a distribuování. Drtivá většina koncové ceny jde tedy Microsoftu bez možnosti distributora toto nějak ovlivnit. Pokud bychom chtěli centrálně nakoupit kancelářský papír, tak udáme jeho parametry (např. gramáž) a je nám jedno od jakého výrobce ho distributor sežene. Navíc logisitcká obratnost distributora může hrát značnou roli. Situace v IT licencí je však zcela jiná. Zde MVČR řeklo, který konkrétní produkt (značku) chce a distributoři/dodavatelé hrají zcela zanedbatelnou roli.

O hrozbě, které tyto rámcové dohody, představyjí pro trh jsem zde [psal již v roce 2018](https://www.profant.eu/2018/egov-cloud.html#jak%C3%A1-jsou-rizika). V rámci debat s ministersvech o egovernment cloudu jsem odstrašující příklad rámcových dohod používal velmi často. Viditelně však bez výsledku.

Situace okolo veřejných zakázek rozhodně není jednoduchá. Pravidla, která zajišťují nediskriminaci, jsou samozřejmě složitá, každé odvětví má svá specifika a tak dále. Na možnosti řešení se podíváme v dalších článcích.
