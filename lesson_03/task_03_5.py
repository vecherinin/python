from random import choice

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью', 'гораздо']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий', 'вялый', 'ароматный']


def get_jokes(num, n=nouns, adv=adverbs, adj=adjectives):
    """get_jokes (num, n=nouns, adv=adverbs, adj=adjectives)
    Choose random three words from each list
    and return a list of strings
    with a certain number of sentences.

    Optional keyword arguments:
    num: number (int) of sentences to output.
    n: list of nouns (default: nouns).
    adv: list of adverbs (default: adverbs).
    adj: list of adjectives (default: adjectives).
    """
    output = []
    for _ in range(num):
        chosen_n = choice(n)
        chosen_adv = choice(adv)
        chosen_adj = choice(adj)
        output.append(f'{chosen_n} {chosen_adv} {chosen_adj}')
    return output
