---
layout:     post
title:      "Není podpis jako podpis"
date:       2020-11-19 08:00:00 +0100
categories: Egovernment
comments:   true
tags:       [Egovernment, bezpečnost]
img:        podpis.jpg
author:     Martin Archalous
---

Když se řekne elektronický podpis, většina lidí si představí šifry a zaručené certifikáty. Ale elektronických podpisů máme několik typů, nebo spíše řekněme úrovní.

<!--more-->

### Prostý elektronický podpis

Elektronický podpis může vypadat i takto:

> Objednávám ve vašem e-shopu pět housek a mléko.
S úctou,
Franta Novák

Ona dvě slova, která jsem na klávesnici připsal za text dopisu, jsou elektronickým podpisem. Samozřejmě elektronickým podpisem nijak zvlášť průkazným. Na rozdíl od vlastnoručního podpisu na papíře tady není žádný jedinečný "klikyhák," který by mohl v případě sporu porovnávat soudní znalec. Proto vás s takovým podpisem nenechají z e-shopu ani objednat si ty housky… (Ostatně, ani já nejsem Franta Novák.) Ale klidně by mohli. I takové jednání je totiž podepsané, a tudíž platné. Takovýto podpis má tedy praktické využití, pokud je zde ještě něco navíc, čím si adresát ověří, že jste to skutečně vy. V civilním styku to může být třeba osobní známost - dlouhá léta spolu komunikujete přes stejný e-mail a pravidelně si objednáváte housky, adresát má tedy důvod věřit, že autorem podpisu jste vy.

### Zaručený elektronický podpis

Zaručený elektronický podpis funguje na stejném principu, jako když pod dokument připíšete své jméno a příjmení. Akorát že dokument nepodepisujete dvěma slovy vyťukanými na klávesnici, ale souborem zašifrovaných dat. A protože šifrovací klíč máte na svém počítači jenom vy (a vydala vám ho nějaká dostatečně důvěryhodná autorita), tak adresát už má v ruce něco silnějšího.
Zaručený elektronický podpis má ještě jednu výhodu - v podstatě “zmrazí“ celý dokument. Jinými slovy je zaručeno nejen “kdo“ jedná, ale i “co“ říká. Pokud by adresát chtěl dokument změnit (například škrtnout z objednávky krabici mléka a nahradit ji luxusním mercedesem), zaručený elektronický podpis bude zneplatněn.

### Uznávaný elektronický podpis

Uznávaný elektronický podpis je pak vyšší úrovní zaručeného elektronického podpisu. Liší se tím, že jeho součástí je takzvaný kvalifikovaný certifikát, tedy certifikát, který může vydat pouze akreditovaná kvalifikovaná certifikační autorita řídící se zákonem o elektronickém podpisu. Pouze s takovým uznávaným elektronickým podpisem můžete jednat vůči orgánu veřejné moci. (Existuje ještě vyšší úroveň, takzvaný **kvalifikovaný elektronický podpis**, který však pro zjednodušení vynecháme.)

Požadavek podpisu je v zákonech poměrně striktní. Většina zákonů trvá na tom, že jednání vůči úřadu má být “podepsáno“ (např. § 37 správního řádu, který se vztahuje téměř na všechna úřední podání). I když tedy ověříte svou identitu jinak, třeba i metodou násobně bezpečnější, nepomůže vám to.

### Vlastnoruční a ověřený podpis - zatím jen na papíře

Kromě různých forem a úrovní elektronického podpisu máme ještě podpisy čistě papírové. Vlastnoruční podpis je podpis vlastní rukou. Tedy, pokud po vás někdo požaduje vlastnoruční podpis, není možné ho nahradit ani tou nejvyšší a nejbezpečnější formou podpisu elektronického.

Stejně tak je to s podpisem úředně ověřeným. Úředně ověřený podpis znamená, že nějaká důvěryhodná autorita - státní úřad, notář, advokát, nebo i pošta - k vašemu vlastnoručnímu podpisu připojí doložku, kterou ověří, že “ano, tento podpis skutečně patří panu Františku Novákovi, protože se podepsal přede mnou a ukázal mi přitom občanský průkaz”.
Úředně ověřené podpisy jsou vyžadovány při některých velmi důležitých typech právních jednání - například žádáte-li poštou o voličský průkaz, zakládáte obchodní společnost nebo si dělíte majetek před rozvodem.
Zákon nepamatuje na to, že by se úředně daly ověřovat podpisy elektronické. Znamená to tedy, že když zákon požaduje bez výjimky jen a pouze úředně ověřený podpis, není možné takové jednání dělat elektronicky? Skoro ano. V praxi se tento “nedostatek“ obchází tak, že se elektronický dokument vytiskne, notář ověří podpis na papíře a dokument se znovu konvertuje do elektronické podoby. Jistě uznáte, že to není ideální stav věcí

Stejně tak vám nepomohou ani datové schránky. Zákon říká, že “Úkon učiněný (...) prostřednictvím datové schránky má stejné účinky jako úkon učiněný písemně a podepsaný“. Ale ani datová schránka (ačkoliv poskytuje nejvyšší záruku zabezpečení) ověřený podpis nenahradí.

To vše se ale brzy změní.


<table>
  <thead>
    <tr>
      <th colspan="2">Druh podpisu</th>
      <th>Popis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4">
        <span style="writing-mode: vertical-lr;
                     -ms-writing-mode: tb-rl;
                     transform: rotate(180deg);
                     min-width:15px;">
                     Elektronický
        </span>
      </th>
      <td>prostý</td>
      <td><em>“Franta Novák”</em></td>
    </tr>
    <tr>
      <td>zaručený</td>
      <td>podepsáno a zmraženo šifrovacím klíčem</td>
    </tr>
    <tr>
      <td>uznávaný</td>
      <td>podepsáno a zmraženo šifrovacím klíčem, který je vydán akreditovanou certifikační autoritou</td>
    </tr>
    <tr>
      <td>kvalifikovaný</td>
      <td>podepsáno a zmraženo šifrovacím klíčem, který je vydán akreditovanou certifikační autoritou; podpis vytvořen kvalifikovaným prostředkem (např. el. občanka)</td>
    </tr>
    <tr>
      <th rowspan="2">
        <span style="writing-mode: vertical-lr;
                     -ms-writing-mode: tb-rl;
                     transform: rotate(180deg);">Listinný
         </span></th>
      <td>vlastnoruční</td>
      <td>vlastní rukou na papír</td>
    </tr>
    <tr>
      <td>úředně ověřený</td>
      <td>potvrzený autoritou, s připojenou doložkou</td>
    </tr>
  </tbody>
</table>


### Místo podpisu e-identita - již za pár měsíců

Striktní požadavky na podpis, vlastnoruční podpis či úředně ověřený podpis jsou jednou z překážek digitalizace státní správy. Nové zákony na nich proto již netrvají, respektive nabízejí širší škálu možností, jak může člověk vůči úřadu prokázat, že “já jsem skutečně já“.

Datové schránky tu již byly zmíněny - pokud jednáte skrze datovou schránku, podepisovat už nemusíte, protože systém datových schránek se bere jako dostatečná záruka vaší identity. Modernější než datové schránky je projekt eIDAS, neboli celoevropská elektronická identita, která umožňuje ověřit vaši identitu skrze jakýkoliv nástroj, který je do systému zapojen. Všechny prostředky eIDAS použitelné v Česku jsou dostupné na [eindentita.cz](https://www.eidentita.cz/). K dnes již poměrně široké škále možných přihlašovacích prostředků se v průběhu příštího roku připojí i banky se svým internetovým bankovnictví.

Starší zákony s e-identitou nepočítají, z čehož vznikají problémy popsané výše. To se ale má brzy změnit. Chystají se tudíž dva zákony, které mají napravit problémy zmíněné výše.

První z nich už byl schválena a do dvou let začne fungovat v praxi - zákon o právu na digitální služby ve svém § 6 má vyřešit zmíněnou absurditu ohledně úředně ověřených podpisů. Sílu ověřovací doložky tedy bude mít kvalifikovaný elektronický podpis ověřující osoby. Ověřování tedy bude probíhat jako dosud, akorát notář nebo úředník nedá razítko na papír, ale k elektronickému dokumentu. A co je zajímavější - tento proces bude moct být provedený i automatizovaně, pokud se přihlásíte s e-identitou v nejvyšším stupni záruky. V praxi tedy - přihlásíte se skrze e-identitu na dejme tomu speciální webový portál krajského úřadu, nahrajete tam svůj dokument, a vrátí se vám s elektronickou ověřovací doložku, přesněji řečeno s kvalifikovanou elektronickou pečetí.

Možná ale ověřování podpisů už nebudete potřebovat. Ten samý zákon totiž stanoví, že uznávaný elektronický podpis, který doteď měl sílu podpisu prostého, může mít i sílu podpisu ověřeného, pokud bude ze základních registrů zjistitelné, že patří vám. Jinými slovy, pokud ministerstvu vnitra nahlásíte, jaké číslo má váš uznávaný elektronický podpis, všechny úřady ho budou automaticky akceptovat jako úředně ověřený.

Konečně, za několik měsíců nás možná čeká změna, která všechno ještě usnadní. Pokud parlament schválí změnu zákona o informačních systémech veřejné správy, jednání učiněná skrze tyto systémy už nebudou muset být podepsaná. Co to znamená? Dnes nemůžete podat žádost dejme tomu o nový řidičský průkaz tak, že se přihlásíte na web městského úřadu s stisknete tlačítko “Požádat o nový průkaz“ jako když nakupujete v eshopu. Právě proto, že úřední žádost musí být podepsaná. (Vzpomínáte? § 37 správního řádu.) Podpis můžete nahradit podáním datovou schránkou nebo podpisem elektronickým, ale ne tím, že se přihlásíte na městský web. Již začátkem příštího roku by to ale mělo být možné - přinejmenším právně. Samozřejmě nebude stačit přihlášení pod náhodným jménem a heslem, jako do eshopu, budete potřebovat třeba už zmiňovanou e-identitu. Ale jakmile bude mít informační systém dostatečnou jistotu, že “vy jste skutečně vy,” umožní vám vůči úřadu jednat i bez podpisu. Tedy, třeba stiskem tlačítka na webové stránce.
