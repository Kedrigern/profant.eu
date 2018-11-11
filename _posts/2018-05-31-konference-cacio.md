---
layout:     post
title:      "Konference CACIO: Pozitivní příklady open source"
date:       2018-05-31 16:00:00 +0100
categories: Egovernment
comments:   true
tags:       [digitalizace, opensource, informatika, egovernment]
img:        konference-cacio.jpg
author:     Ondřej Profant
---

Konference České asociace manažerů informačních technologií (CACIO) [konaná dne 15. 5. 2018](http://www.cacio.cz/akce/2018/kdy-a-proc-zvolit-reseni-open-source-2018) byla zaměřená na využívání open source řešení ve veřejné správě. Měl jsem to štěstí se této konference zúčastnit a dozvěděl jsem se hned o dvou pozitivních příkladech nasazení open source ve veřejné správě. Rád bych se o ně prostřednictvím tohoto článku podělil.

<!--more-->

O open source se často říká, že je to sice hezká myšlenka, ale v praxi se takový software na úřadech moc používat nedá. Následující příklady ukazují, že je to nejenom možné, ale že to i přináší viditelné úspory a zvyšuje kontrolu objednatele nad dodanými systémy.

## IdM v Národní technické knihovně

[Prezentace ke stažení](https://github.com/Kedrigern/Kedrigern.github.io/raw/master/assets/pdf/upgrade_idm_v_ntk241.pdf)

Prvním příkladem je systém pro správu identit (Identity Management - IdM) Národní technické knihovny (NTK). Tedy systém, který zajišťuje, aby uživatelé měli přístupy k těm systémům, ke kterým tyto přístupy mít mají. V případě tak velké veřejné instituce, jako je NTK, se tak jedná o systém s desítkami tisíc unikátních identit, které jsou řazeny do různých kategorií dle komplexních pravidel. To umožňuje návštěvníkovi knihovny si půjčit knížku, rezervovat místnost, používat veřejné tiskárny, spravovat své čtenářské konto a další služby, které knihovna poskytuje. Jde tedy o značně robustní systém.

NTK na základě dříve uzavřené smlouvy využívala proprietární řešení, které ji přišlo na téměř 8,5 milionu, přičemž přibližně neuvěřitelné 2,5 milionu z této sumy byla licence k užívání software. Jedním z častých problémů proprietárních je i uzavřená znalost systému, kdy se objednatel stává závislým na dodavateli čistě z toho důvodu, že neexistuje nikdo jiný, kdo by tomu systému rozuměl. Když pak dodavatel přestane daný systém rozvíjet a podporovat - což se může stát z mnoha příčin, nejčastěji z tržních důvodů -, ocitne se zákazník v pasti. Software je mrtvý, dodavatel deklaroval, že se o něj přestává starat, ale smlouva zůstává v platnosti. Stovky až tisíce hodin práce, které zákazník stráví zaučováním svých zaměstnanců nebo napojováním systému na své další systémy, tak připadnou vniveč. To samé se stalo i NTK s původním IdM systémem od Sunu.

Když tedy NTK vyhlašovala výběrové řízení na nový systém, vložila si do zadávací dokumentace v návrhu smluvního závazku podmínku, že k výslednému dílu (systému) obdrží veškerá majetková práva. IdM systém, který tak NTK vysoutěžila, má stát necelé 4 miliony, což je o více než polovinu levnější než v případě předchozího systému. Z této částky je přibližně 1,4 milionu určeno na implementaci, 1,5 milionu na údržbu systému a zbytek na jeho rozvoj. To jsou daleko lépe vynaložené prostředky než nesmyslná platba za licenci k užívání software. Které v tomto případě není třeba vůbec hradit, protože NTK se stává vlastníkem majetkových práv. Místo toho, aby si software jen pronajímala, tak software skutečně vlastní.

## MČ Praha 10

[Prezentace ke stažení](http://www.cacio.cz/Frontend/Webroot/uploads/files/2018/05/180515-p10-cacio234.pdf)

Druhým zmiňovaným příkladem je situace na Úřadu městské části Praha 10, kde rovněž významným způsobem měnili svou infrastrukturu. Z původního stavu, kdy využívali specializovaný hardware a nesourodý mix uzavřeného a otevřeného software, se dokázali přeorientovat na hardwarové vybavení tvořené ze standardních komponent a plně otevřená řešení, například i nástroje pro virtualizační infrastrukturu.

Nejlépe se dá úspěch Prahy 10 při přechodu na open source ukázat na realizaci zadání na diskové úložiště. Oproti původnímu korporátnímu řešení za téměř pět milionů dokázala Praha 10 v novém zadání srazit cenu skoro na tři miliony, zároveň došlo k výraznému nárůstu kapacity úložiště. Opět se tedy ukázalo, že otevřená řešení jsou výhodná, úsporná i užitečná.

|            | Původně        | Nově           |
|------------| :------------- | :------------- |
| Cena v Kč  | **4.900.000**  | **3.042.000**  |
|Vendor      | IBM Pole       |  Standardní komponenty vysoutěženo dle zákona o VZ      |
|Technologie | FiberChannel, SAS, HW RAID | IP (iSCSI) |
|Kapacita    | **30TB**       |  2x pole 9,6TB SSD + **180TB HDD**, 1x pole 288TB HDD |

Srovnání 2: podrobnosti v prezentaci

## Závěr

Já osobně jsem za tyto dva příspěvky z konference velmi vděčný, protože pomáhají nabořit mýtus, že open source je pro širší využití ve státní správě a samosprávách nepoužitelný.
