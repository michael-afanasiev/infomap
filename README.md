# infomap
A simple set of scripts to plot colour-coded infographic maps.

[![Build Status](https://travis-ci.org/michael-afanasiev/infomap.svg?branch=master)](https://travis-ci.org/michael-afanasiev/infomap)

`infomap` takes a `JSON` file with the format
```
{
    "countries":
    {
        "NAME1": "VAL1",
        "NAME2": "VAL2"
    }
}
```
as input. Use the following country codes as `NAMEx`, and ensure that `VALx` are percentages between 0 and 100.
```
AFG: Afghanistan
AGO: Angola
ALB: Albania
ARE: United Arab Emirates
ARG: Argentina
ARM: Armenia
ATA: Antarctica
ATF: French Southern and Antarctic Lands
AUS: Australia
AUT: Austria
AZE: Azerbaijan
BDI: Burundi
BEL: Belgium
BEN: Benin
BFA: Burkina Faso
BGD: Bangladesh
BGR: Bulgaria
BHS: Bahamas
BIH: Bosnia and Herzegovina
BLR: Belarus
BLZ: Belize
BOL: Bolivia
BRA: Brazil
BRN: Brunei Darussalam
BTN: Bhutan
BWA: Botswana
CAF: Central African Republic
CAN: Canada
CHE: Switzerland
CHL: Chile
CHN: China
CIV: b"C\xf4te d'Ivoire"
CMR: Cameroon
COD: Democratic Republic of the Congo
COG: Republic of Congo
COL: Colombia
CRI: Costa Rica
CUB: Cuba
CYN: Northern Cyprus
CYP: Cyprus
CZE: Czech Republic
DEU: Germany
DJI: Djibouti
DNK: Denmark
DOM: Dominican Republic
DZA: Algeria
ECU: Ecuador
EGY: Egypt
ERI: Eritrea
ESP: Spain
EST: Estonia
ETH: Ethiopia
FIN: Finland
FJI: Fiji
FLK: Falkland Islands
FRA: France
GAB: Gabon
GBR: United Kingdom
GEO: Georgia
GHA: Ghana
GIN: Guinea
GMB: The Gambia
GNB: Guinea-Bissau
GNQ: Equatorial Guinea
GRC: Greece
GRL: Greenland
GTM: Guatemala
GUY: Guyana
HND: Honduras
HRV: Croatia
HTI: Haiti
HUN: Hungary
IDN: Indonesia
IND: India
IRL: Ireland
IRN: Iran
IRQ: Iraq
ISL: Iceland
ISR: Israel
ITA: Italy
JAM: Jamaica
JOR: Jordan
JPN: Japan
KAZ: Kazakhstan
KEN: Kenya
KGZ: Kyrgyzstan
KHM: Cambodia
KOR: Republic of Korea
KOS: Kosovo
KWT: Kuwait
LAO: Lao PDR
LBN: Lebanon
LBR: Liberia
LBY: Libya
LKA: Sri Lanka
LSO: Lesotho
LTU: Lithuania
LUX: Luxembourg
LVA: Latvia
MAR: Morocco
MDA: Moldova
MDG: Madagascar
MEX: Mexico
MKD: Macedonia
MLI: Mali
MMR: Myanmar
MNE: Montenegro
MNG: Mongolia
MOZ: Mozambique
MRT: Mauritania
MWI: Malawi
MYS: Malaysia
NAM: Namibia
NCL: New Caledonia
NER: Niger
NGA: Nigeria
NIC: Nicaragua
NLD: Netherlands
NOR: Norway
NPL: Nepal
NZL: New Zealand
OMN: Oman
PAK: Pakistan
PAN: Panama
PER: Peru
PHL: Philippines
PNG: Papua New Guinea
POL: Poland
PRI: Puerto Rico
PRK: Dem. Rep. Korea
PRT: Portugal
PRY: Paraguay
PSX: Palestine
QAT: Qatar
ROU: Romania
RUS: Russian Federation
RWA: Rwanda
SAH: Western Sahara
SAU: Saudi Arabia
SDN: Sudan
SDS: South Sudan
SEN: Senegal
SLB: Solomon Islands
SLE: Sierra Leone
SLV: El Salvador
SOL: Somaliland
SOM: Somalia
SRB: Serbia
SUR: Suriname
SVK: Slovakia
SVN: Slovenia
SWE: Sweden
SWZ: Swaziland
SYR: Syria
TCD: Chad
TGO: Togo
THA: Thailand
TJK: Tajikistan
TKM: Turkmenistan
TLS: Timor-Leste
TTO: Trinidad and Tobago
TUN: Tunisia
TUR: Turkey
TWN: Taiwan
TZA: Tanzania
UGA: Uganda
UKR: Ukraine
URY: Uruguay
USA: United States
UZB: Uzbekistan
VEN: Venezuela
VNM: Vietnam
VUT: Vanuatu
YEM: Yemen
ZAF: South Africa
ZMB: Zambia
ZWE: Zimbabwe
```