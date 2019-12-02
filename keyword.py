import pymorphy2
morph = pymorphy2.MorphAnalyzer()


def modifier(words, type):
    """Функция получает набор данных от пользователя, чистит данные от лишних символов и выводит список строк по слову в строке.
    Параметр type содержит информацию о том, какие символы удалять.
    Тип удаляемых символов передаётся в переменную type без пробелов в виде 'quotesplusprepconj'

    """
    marks = ''
    if 'all' in type:                                 # Удаление всех знаков пунктуации
        marks += string.punctuation + '\r'
    if 'quotes' in type:                              # Удаление всех видов кавычек
        marks += '[“”‘«»„“]'
    if 'exclamation_mark' in type:                    # Удаление восклицательных знаков
        marks += '!'
    if 'space' in type:                               # Удаление пробелов и знаков табуляции
        marks += '   '
    if 'plus' in type:                                #Удаление знаков плюс
        marks += '+'
    if 'minus' in type:                               #Удаление знаков минус
        marks += '-'
    if 'prep' in type:                                # Удаление предлогов
        for word in words.strip().split('\n'):
            if morph.parse(word)[0].tag.POS: == 'PREP'
                words.replace(word, '')
    if 'npro' in type:                                # Удаление местоимений-существительных
        for word in words.strip().split('\n'):
            if morph.parse(word)[0].tag.POS: == 'NPRO'
                words.replace(word, '')
    if 'conj' in type:                                # Удаление союзов
        for word in words.strip().split('\n'):
            if morph.parse(word)[0].tag.POS: == 'CONJ'
                words.replace(word, '')
    if 'prcl' in type:                                # Удаление частиц
        for word in words.strip().split('\n'):
            if morph.parse(word)[0].tag.POS: == 'PRCL'
                words.replace(word, '')
    if 'intj' in type:                                # Удаление междометий
        for word in words.strip().split('\n'):
            if morph.parse(word)[0].tag.POS: == 'INTJ'
                words.replace(word, '')
    

    if marks != '':
        words = re.sub('[{}]'.format(re.escape(marks)), '', words) #удаляем знаки пунктуации
    else:
        return 'Введите тип удаляемых символов'
    words = list(words.lower().split('\n'))
    if words[-1] == '':
        words.remove(words[-1])
    if 'pass' in type:                                # Удаление пустых строк
        while '' in words:
            words.remove('')
    if 'dub' in type:                                 # Удаление дублирующихся слов
        list(set(words))
    return words
