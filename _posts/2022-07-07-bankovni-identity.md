---
layout:     post
title:      "Bankovní identita není všespásná"
date:       2022-07-07 15:00:00 +0100
categories: Egovernment
comments:   true
tags:       [Egovernment, Digitalizace]
img:        identita.jpg
author:     Ondřej Profant
---

Soukromoprávní identity umožňující přístup ke službám egovernmentu znamenají významný posun pro digitalizaci státu. Přesto je jejich používání i vinou legislativních překážek stále nedokonalé.

<!--more-->

# Bankovní identita není všespásná

Využití soukromoprávních identit pro přístup ke službám egovernmentu je ohromným krok vpřed. Dlouho jsme měli velmi prostý problém. Měli jsme online služby, ale neměl je kdo používat. Zkušenosti ze zahraničí nám jasně ukázaly cestu -- spolupracujme s institucemi, které již klienty mají ztožněné. Zde se nabízí silně regulované odvětví bank (ještě před přijetím zákona měly klienty ztotožněné proti základním registrům). Nutno též zmínit, že jsou i jiné subjekty, které poskytují identity. Zvláště pak mojeID od cz.nic je skvělým příkladem nezavislé identity, která narozdíl od bank splňuje i nejvyšší bezpečnostní úroveň pro komunikaci se zahraničním egovernmentem napříč EU. Plný výčet poskytovatelů nalezenete na portálu [identitaObcana.cz][].

## Dvě vady na kráse

I tento významný krok vpřed má však své mouchy. Obě jsou přímo v zákoně č. [21/1992 Sb.][] o bankách:

> § 38ad
> 
> (1) Přístup do informačního systému veřejné správy nebo elektronické aplikace s využitím prostředku pro elektronickou identifikaci splňujícího požadavky podle § 38ac odst. 1 se považuje za přístup se **zaručenou** identitou podle zákona o informačních systémech veřejné správy.
>
> (2) **Státní orgán a orgán územního samosprávného celku** jsou oprávněny použít prostředek pro elektronickou identifikaci vydaný bankou, pobočkou zahraniční banky nebo poskytovatelem identifikačních služeb pro účely prokázání totožnosti, které vyžaduje právní předpis nebo výkon působnosti, pouze prostřednictvím kvalifikovaného systému.

Prvním problémem bankovních identit je, že se banky bojí nejvyšší úrovně. Identita má tři úrovně zabezpečení: nízkou, značnou a vysokou. V praxi služby nejčastěji využívají značnou. Vysoká je potřeba například pro přeshraniční komunikaci. Tento problém je zatím spíše teoretický, neb drtivá většina služeb si vystačí s úrovní značná. K tomuto kompromisu došlo z důvodu obavy bank ze zodpovědnosti za úkony činěné v nejvyšší úrovni. Což je teoreticky cokoliv, v praxi však třeba katastr je chráněn ještě ochrannými lhůtami, čili zneužití není záležitostí "přihlásím se a odkliknu".

Druhý probléme je však mnohem palčivější. Definice "Státní orgán a orgán územního samosprávného celku" znamená státní orgán, obce a kraje. V tomto výčtu viditelně a záměrně chybí soukromoprávní subjekty, avšak také vysoce nezávislé subjekty, které jsou však zřízeny státem např. fondy. Zvláště patrné je to pak u [Státního fondu životního prostředí][], který vypisuje program [Zelená úsporám][]. Nebo třeba u Státního fondu dopravní infrastruktury, který provozuje portál edalnice, přes který se kupuje dalniční známka.

Tento problém vznikl záměrně. Banky pochopitlně chtějí vydělat, a tak soukromoprávní identity nejsou zahrnuty v zákoně. Koneckonců je to soukromoprávní vztah mezi bankou a někým jiným, kdo potřebuje identifikovat klienta. Připojení se tedy řídí [ceníkem][]. Je ale nesmysl, aby státní fondy platily bankám za ztotožnění oproti státnímu registru obyvatel.

## Jak tedy požádat o zelenou úsporám?

Jak tedy podat žádost o zelenou úsporám či jinou službu státního fondu? Naštěstí toto omezení jde obejít. I když je to poněkud kostrbaté.

1. Pomocí bankovní identity se přihlásíte na https://www.identitaobcana.cz
2. Zde najdete nadpis **Mobilní klíč eGovernmentu** a v něm odkaz: **Připojení Mobilního klíče eGovernmentu**.
3. Na odkaze si stáhnete aplikaci Mobilní klíč eGovernmentu
4. Tuto aplikaci si propojíte se svou identitou

![Jak získat mobilní klíč](/assets/img/posts/mobilni-klic.png)

Nyní máte dva možné způsoby, jak se přihlašovat. Prostřednictvím bankovní identity od banky a aplikací mobilní klíč. Tato aplikace vám však bude fungovat právě i u státních fondů, čili s ní můžete např. podat žádost v programu Zelená úsporám.

Pokud aplikaci nechcete víc používat, tak ji můžete na té samé stránce i odpojit. Například pokud se bojíte zneužití vašeho mobilu.

## Kdy se to změní?

Jelikož je toto zaneseno přímo v zákoně, tak to může změnit pouze Parlament. Ten projednává mnoho věci, je proto obvykle lepší se připojit k nějaké již probíhající změně daného zákona.

Poslanecká sněmovna je však zpomalena obstrukcemi od ANO a SPD, čili je velmi těžké podobné drobné vylepšení protlačit. Při nejbližší příležitosti tuto změnu ale určitě předložíme.




[identitaObcana.cz]: https://info.identitaobcana.cz/idp/
[21/1992 Sb.]: https://www.zakonyprolidi.cz/cs/1992-21#p38ad
[Státního fondu životního prostředí]: https://www.sfzp.cz/
[Zelená úsporám]: https://novazelenausporam.cz/
[ceníkem]: https://www.bankid.cz/cenik
[Zákon roku]: https://www.pirati.cz/tiskove-zpravy/online-komunikace-bankovni-identita-zakon.roku.html
