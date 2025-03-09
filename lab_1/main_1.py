import string
from collections import Counter

cipher_text = """
=73КЙИZКРИИNИ@О=гQZiЯХN@И@ХТуiNiО7КЖгТЙИGNЖТ7@ИGуИ
NJгGNО7ТJ=ХЖ7КYТЙИGNЖЙТ@ТЙИGN@гi1КFЙU<NИZуТЙТЙИFNК
ЖХ=7ИZ=ЖКЙЙUуИNО=гQZ=ЖКХТгGуИ
JЖКNО=гQZ=ЖКХТгИNЙТNу=3iХN=ПЙ=ЖгGХQN=JИЙNИNХ=ХNRТN=
ПsТ%Х
=ПsТ%ХКуИNу=3iХNПUХQNДКFгUNZКОИ@ИNПКZUNJКЙЙU<NИгИN
Х7КЙZК%РИИ
ЙКО7ИуТ7NОТ7ЖUFNО=гQZ=ЖКХТгQN=Х%7UЖКЯYИFNJ=%iуТЙХNИ
уТТХN7КZ7ТюТЙИТNЙКNИZуТЙТЙИТNЁХ=3=NJ=%iуТЙХКNNЖХ=7=FN
О=гQZ=ЖКХТгQNИуТТХN7КZ7ТюТЙИТNХ=гQ%=NЙКN1ХТЙИТ
Х=1ЙUТN7ТZТ7ЖЙUТN%=ОИИNО=у=3КЯХN@=<7КЙИХQNРТг=@ХЙ=
@ХQNJКЙЙU<NЖN@гi1КТNО=Ж7ТRJТЙИGNJКЙЙU<
=73КЙИZКРИGуN@гТJiТХN%=ЙХ7=гИ7=ЖКХQNО7=РТ@@N7ТZТ7ЖЙ=
3=N%=ОИ7=ЖКЙИGN1Х=ПUN3К7КЙХИ7=ЖКХQNРТг=@ХЙ=@ХQN7ТZ
Т7ЖЙU<N%=ОИFNИNО7ТJ=ХЖ7КYТЙИТNО=ХТ7ИNJКЙЙU<
КЖХ=7ИZКРИGN=О7ТJТгGТХN%Х=NИуТТХNJ=@ХiОN%N7Т@i7@КуN
=73КЙИZКРИИNЙКN=@Й=ЖТNЖUО=гЙGТуU<NЖN=73КЙИZКРИИN=П
GZКЙЙ=@ХТF
ЙКО7ИуТ7N@NО=у=YQЯNО7КЖNJ=@ХiОКN%NДКFгКуNИN@7ТJ@ХЖ
N7КZ37КЙИ1ТЙИGNJ=@ХiОКN=ПТ@ОТ1ИЖКТХ@GN3К7КЙХИGNХ=3
=N1Х=NХ=гQ%=N=О7ТJТгТЙЙUТNО=гQZ=ЖКХТгИNу=3iХNИZуТЙGХQ
NJКЙЙUТ
КJуИЙИ@Х7КХ=7Nу=RТХNi@ХКЙ=ЖИХQNО7КЖКNJ=@ХiОКN%NДКF
гiNХ=гQ%=NЙКN1ХТЙИТ
ЖN7ТZiгQХКХТNО=гQZ=ЖКХТгQN%=Х=7UFNО=гi1КТХNJ=@ХiОN%N
ЁХ=уiNДКFгiNЙТNу=RТХNЖЙТ@ХИNЖNДКFгNЙИ%К%И<NИZуТЙТЙ
ИF
"""

cipher_text = cipher_text.replace('\n', '')

frequency_index = {
    ' ': 0.128675,
    'О': 0.096456,
    'И': 0.075312,
    'Е': 0.072292,
    'А': 0.064841,
    'Н': 0.061820,
    'Т': 0.061619,
    'С': 0.051953,
    'Р': 0.040677,
    'В': 0.039267,
    'М': 0.029803,
    'Л': 0.029400,
    'Д': 0.026983,
    'Я': 0.026379,
    'К': 0.025977,
    'П': 0.024768,
    'З': 0.015908,
    'Ы': 0.015707,
    'Ь': 0.015103,
    'У': 0.013290,
    'Ч': 0.011679,
    'Ж': 0.010673,
    'Г': 0.009867,
    'Х': 0.008659,
    'Ф': 0.007249,
    'Й': 0.006847,
    'Ю': 0.006847,
    'Б': 0.006645,
    'Ц': 0.005034,
    'Ш': 0.004229,
    'Щ': 0.003625,
    'Э': 0.002416,
    'Ъ': 0.000000
}

frequency = Counter(cipher_text)

total_chars = sum(frequency.values())
frequency_index_cipher = {char: count / total_chars for char, count in frequency.items()}

sorted_frequency_cipher_index = dict(sorted(frequency_index_cipher.items(), key=lambda item: item[1], reverse=True))

print("Индекс частоты появления букв:")
for char, freq in sorted_frequency_cipher_index.items():
    print(f"Символ: '{char}', Частота: {freq:.6f}")