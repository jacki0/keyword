from wordside import modifier, declension, counter, generator, lemma, cityremover, trimutm, crossminus

#text = 'Купить айфон, Москва,'
text2 = 'Куплю айфон, Москва купить аЙфон Мск'
#text3 = ['Куплю Купить', 'айфон, iPhone, iPad, айпад, айпэд', 'Москва, Мск, Спб, Казань, Киров, Санкт-Петербург']
#text4 = 'Купить, покупка, скупка, айфона, продам, продать'
text5 = 'Готовлю'
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
print(cityremover(text2))
print(cityremover(text2, True))
print(cityremover(text5))