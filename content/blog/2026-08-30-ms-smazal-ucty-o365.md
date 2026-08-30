---
date: 2026-08-30
extra:
  author: Ondřej Profant
  comments: true
  img: vendor-lock-in.png
  layout: post
taxonomies:
  categories:
  tags:
title: "Když vám cloud změní pravidla hry"
---

**Roky používáte službu, všechno funguje a není důvod řešit, co je za tím. Pak ale poskytovatel změní podmínky a vy zjistíte, že na jeho rozhodnutí stojí fungování celé organizace. Přesně to teď řeší část neziskových organizací používajících Microsoft 365. A je to velmi dobrá ukázka toho, proč „just works“ nestačí.**

Americký [Slate](https://slate.com/technology/2026/08/microsoft-software-nonprofit-data-delete.html) popsal případy neziskových organizací, které po změně licenčního programu Microsoft 365 přišly o přístup ke svým datům. Podle některých svědectví v několika případech dokonce nevratně.

Microsoft dříve poskytoval neziskovým organizacím zdarma licence **Microsoft 365 Business Premium** a **Office 365 E1**. V roce 2025 oznámil jejich ukončení. Organizace měly přejít na jinou bezplatnou nebo placenou variantu. Přechod ale nebyl automatický a bylo nutné ho provést ručně.

Microsoft přitom sám upozorňoval, že pokud organizace nepřejdou včas na jinou licenci, může dojít ke ztrátě přístupu ke službám a později i k datům.
[Podrobnosti přímo od Microsoftu](https://learn.microsoft.com/en-us/industry/nonprofit/microsoft-for-nonprofits/updates)

Podobně na změnu upozorňoval také **TechSoup**, který pomáhá neziskovým organizacím získávat technologické služby. Jeho česká pobočka uváděla, že po skončení licence zůstávají data dostupná jen omezenou dobu a bez dalšího kroku o ně organizace může přijít.
[České shrnutí TechSoup](https://www.techsoup.cz/content/konec-darovan%C3%BDch-licenc%C3%AD-microsoft-365-business-premium-office-365-e1-zdarma)

Slate popisuje například případ neziskové organizace **Canopy**, která zjistila, že její data zmizela. Podpora měla nejprve tvrdit, že je bude možné obnovit, později ale přišla opačná zpráva.

V článku se objevuje také číslo přibližně **171 tisíc postižených organizací**. To je ale potřeba brát s rezervou — nejde o oficiální statistiku Microsoftu ani nezávisle ověřené číslo, ale o údaj, který měl podle jednoho ze zákazníků zaznít od pracovníka podpory.

Samotný problém je přesto reálný.

## Když nemáte jednoduchou cestu ven

Nejdůležitější lekce podle mě není ani samotná ztráta dat. Jde o to, co se stane, když je organizace plně závislá na jednom dodavateli.
Představme si neziskovku, která Microsoft 365 používá deset let. Dokumenty má na OneDrivu a SharePointu, komunikuje přes Teams, používá Outlook, Word, Excel, kalendáře a další služby.
Pak dodavatel změní podmínky. Teoreticky můžete odejít. Prakticky ale dostanete na výběr:

**Zaplaťte nové licence, nebo zaplaťte náročnou a bolestivou migraci.**

To je **vendor lock-in** v praxi. Problém není v tom, že Microsoft chce za svůj software peníze. To je samozřejmě legitimní.
Problém nastává ve chvíli, kdy jsou náklady na odchod tak vysoké, že ve skutečnosti příliš na výběr nemáte.

## A právě tady dává smysl open source

Open source se často redukuje na cenu.
Jenže jeho mnohem důležitější vlastností je, že **software není svázaný s jediným poskytovatelem**. Vezměme třeba Nextcloud.
Mohu ho provozovat sám. Mohu si ho koupit jako službu od jednoho z řady poskytovatelů. A pokud mi jeden z nich přestane vyhovovat, mohu přejít k jinému.
Samozřejmě ani taková migrace není bez práce. Rozdíl je ale zásadní:

**Neměním celý ekosystém. Měním jeho provozovatele.** To je skutečná výhoda otevřených technologií.

## Digitální suverenita není jen vlastní server ve sklepě

Digitální suverenita podle mě neznamená, že si každý musí provozovat vlastní infrastrukturu.
A neznamená ani to, že bychom neměli používat Microsoft, Google nebo jiné velké poskytovatele.
Znamená něco mnohem praktičtějšího:

**Vím, kde mám data. Vím, jaké kolem nich mám garance. Dokážu je exportovat. A mám realistickou možnost změnit dodavatele.**

Cloudové služby mohou být skvělé. Často jsou levnější, bezpečnější a jednodušší než amatérsky provozovaná vlastní infrastruktura.
Ale pohodlí nesmí znamenat ztrátu svobody. Pokud je odpověď na otázku:

> **Co uděláme, když náš dodavatel zítra zásadně změní podmínky?**

jen:

> **Snad to neudělá.**

pak žádnou digitální suverenitu nemáme.

## Další čtení

- [Původní článek ve Slate](https://slate.com/technology/2026/08/microsoft-software-nonprofit-data-delete.html)
- [Microsoft: změny programu pro neziskové organizace](https://learn.microsoft.com/en-us/industry/nonprofit/microsoft-for-nonprofits/updates) — Microsoft skutečně uvádí, že přechod na jiné licence musel být proveden ručně a varoval před výpadkem či ztrátou dat.
- [TechSoup ČR](https://www.techsoup.cz/content/konec-darovan%C3%BDch-licenc%C3%AD-microsoft-365-business-premium-office-365-e1-zdarma?utm_source=chatgpt.com): konec darovaných licencí — pěkný český zdroj, který popisuje i 90denní lhůtu pro přístup k datům.
