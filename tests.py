from wordside import modifier, declension, counter, generator, lemma, cityremover, trimutm, crossminus

#text = 'Купить айфон, Москва,'
text2 = 'Куплю айфон, Москва\nкуплю айфон Мск\nкуплю айфон Xr'
#text3 = ['Куплю Купить', 'айфон, iPhone, iPad, айпад, айпэд', 'Москва, Мск, Спб, Казань, Киров, Санкт-Петербург']
#text4 = 'Купить, покупка, скупка, айфона, продам, продать'
#text5 = 'Готовлю'
#text6 = 'http://jackio.ml/?utm_source=google&utm_medium=cpc&utm_campaign=promo\nhttp://adirect.ml/?utm_source=yandex&utm_medium=cpc&utm_campaign=promo'
#text7 = 'http://jackio.ml/?utm_source=google&utm_medium=cpc&utm_campaign=promo'
#print(modifier(text, 'punct'))
#print(modifier(text5, 'punct'))
#print(declension(text))
#print(counter(text))
#print(counter(text2))
#print(counter(text2, True))
#print(counter(text2, True, True))
#print(generator(text3))
#print(lemma(text))
#print(lemma(text4))
#print(lemma(text5))
#print(cityremover(text2))
#print(cityremover(text2, True))
#print(cityremover(text5))
#print(trimutm(text6))
#print(trimutm(text7))
print(crossminus(text2))
