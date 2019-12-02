import pymorphy2
morph = pymorphy2.MorphAnalyzer()


def modifier(words, type):
    """Функция получает набор данных от пользователя, чистит данные от лишних символов и выводит список строк по слову в строке.
    Параметр type содержит информацию о том, какие символы удалять.
    Тип удаляемых символов передаётся в переменную type без пробелов в виде 'quotesplusprepconj'

    """
    marks = ''
    result = []
    if 'punct' in type:                               # Удаление всех знаков пунктуации
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
        words = re.sub('[{}]'.format(re.escape(marks)), '', words) # Удаление символов
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
    if 'decl' in type:                                # Удаление дублирующихся слов и склонений
        while len(words) > 0:
            result.append(words[0])
            words = list(set(words) - set(declension(words[0]).split('\n')))
    return words


def declension(userinput):
    """Функция получает одно или несколько слов ивозвращает список склонений заданных слов.

    """
    result = []
    decls = []
    userinput = modifier(userinput, 'punct') 
    for word in userinput:
        words = morph.parse(word)[0].lexeme        # Получение списка склонений
        for element in words:                      # Отчистка от лишних данных
            decl = str(element).split(' ')
            decls.append(decl[-3].replace("'", '').replace(',', ''))  
        if word not in decls:                      # Проверка наличие изначальной формы в результирующем списке
            decls.append(word)
        if len(userinput) == 1:                    # Если задано одно слово - возвращаем результат
            return decls
        else:
            result.append(decls)
    return result


def counter(words, deldub = False, deldecl = False):
    """Функция считает количество слов.
    Возвращает список, в котором первый элемент - количество слов, второй - все слова через пробел.
    Если передать переменной deldub значение True, будут удалены повторяющиеся слова,
    если передать переменной decl значение True, так-же будут удалены повторяющиеся склонения слов.
    
    """
    if deldub == False:
        words = modifier(words, 'all')
    elif deldub == True and deldecl == False:
        words = modifier(words, 'alldub')
    elif deldecl == True:
        words = modifier(words, 'alldecl')
    return words.insert(0, 'Количество слов - ' + str(len(result)))
