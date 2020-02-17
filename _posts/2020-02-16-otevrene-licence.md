---
layout:     post
title:      "Otevřené licence softwarových projektů pro veřejnou správu"
date:       2020-16-02
categories: Digitalizace
comments:   true
tags:       [egovernment, digitalizace, licence]
img:        open-source-licenses.jpg
author:     Ondřej Profant
---

Tomu, aby veřejné instituce pořizovaly software za podmínek umožňujících jeho další rozvoj a sdílení, nic nebrání. Experti na autorské právo a veřejné zakázky se na tom shodují i se zaměstnanci Ministerstva vnitra a dalších úřadů. Za jakých podmínek by však měly veřejné instituce takto získaný kód dále šířit?

<!--more-->

Protože veřejná instituce musí postupovat s péčí řádného hospodáře, měla by stanovit takové licenční podmínky, které jsou pro ni prospěšné. Tedy takové, které budou motivovat k dalšímu užívání daného softwarového projektu, opravování jeho nedostatků a jeho rozvíjení. 

Volba vhodné licence může šíření projektu výrazně pomoci, nebo z něj naopak udělat propadák. A protože je běžně užívaných [otevřených licencí celá řada](https://opensource.org/licenses/category), nemusí být na první pohled zřejmé, kterou zvolit. Existuje však dobrá praxe, kterou se vyplatí následovat.

V první řadě je potřeba si uvědomit, jaký software má být vlastně uveřejněn. Obecně se může jednat buď o hotovou aplikaci (spisová služba, agendový systém), nebo pouze o dílčí komponentu (knihovna pro připojení k datovým schránkám, framework pro uživatelská rozhraní). Aplikace může mít architekturu klient-server (typicky informační systém) nebo běžet přímo na zařízení uživatele (například nástroj na úpravu dokumentů).

Pro aplikace je vhodné zvolit silnější, tedy tzv. copyleftovou licenci z rodiny GPL. Tyto licence požadují, aby uživatel původního i upraveného programu získal přístup k jeho zdrojovému kódu a mohl jej za stejných podmínek šířit dále. Takže v případě, že jiný subjekt takovou aplikaci vylepší a prodá, získá nabyvatel možnost všechna vylepšení uveřejnit nebo rovnou navrhnout jejich začlenění do původního projektu.

Pro aplikace určené k běhu na zařízení uživatele postačí licence GPLv3, ale pro systémy s architekturou klient-server je potřeba zvolit licenci AGPLv3 (Affero GPL), která zaručuje uživateli klientské části systému přístup ke zdrojovým kódům serverové části. Bez ní by bylo snadné “uzavřít” projekt jeho poskytováním formou SaaS (tedy hostováním serverové části v cloudu).

Pro komponenty, tedy různé knihovny a frameworky se naopak vyplatí použít slabší, tzv. permisivní licenci. Oblíbené jsou licence MIT a Apache Software License (ASL) 2.0. Licence Mozilla Public License (MPL) 2.0 je pak určitým mezistupněm. Slabší licence je zde výhodou proto, že komponentu může použít více subjektů pro vytvoření různých aplikací včetně uzavřených. Motivace přispět do projektu je zde stejná jako u původní instituce - podělit se o náklady na údržbu a rozvoj.

### Příklady otevřených licencí a jejich výhody

* **[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)**  
Další šíření musí být pod stejnou licencí, včetně zdrojového kódu a to i pro odvozená díla. Aplikaci nelze uzavřít a uživatelé jsou motivováni rozvíjet stejnou code base.

* **[GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/)**  
Stejná jako GPLv3, ale na zdrojový kód má nárok každý jednotlivý uživatel (tedy i uživatel konzumující software prostřednictvím SAAS).

* **[Mozilla Public License 2.0](https://choosealicense.com/licenses/mpl-2.0/)**  
Další šíření může být pod smíšenou licencí. Části původně pod MPL musí být dodány včetně zdrojových kódů, ale další vylepšení mohou zůstat uzavřená.

* **[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)** a **[MIT License](https://choosealicense.com/licenses/mit/)**  
Další sdílení nemusí být se zdrojovými kódy. Velmi se hodí pro programovací frameworky či knihovny, které jsou určeny k integraci do dalšího projektu.
