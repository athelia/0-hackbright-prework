english_to_dragaeran = {
    'Smith': 'Phoenix',
    'Johnson': 'Dragon',
    'Williams': 'Lyorn',
    'Jones': 'Tiassa',
    'Brown': 'Hawk',
    'Davis': 'Dzur',
    'Miller': 'Issola',
    'Wilson': 'Tsalmoth',
    'Moore': 'Vallista',
    'Taylor': 'Jhereg',
    'Anderson': 'Iorich',
    'Thomas': 'Chreotha',
    'Jackson': 'Yendi',
    'White': 'Orca',
    'Harris': 'Teckla',
    'Martin': 'Jhegaala',
    'Thompson': 'Athyra'
}
english_to_elvish = {
    'our': 'ae',
    'father': 'adar',
    'who': 'nin',
    'is': 'i',
    'in': 'vi',
    'heaven': 'menel',
    'hallowed': 'aer',
    'be': 'no',
    'your': 'lin',
    'name': 'eneth'
}
def translate(word):
    if word in english_to_elvish:
        return english_to_elvish[word]
    else:
        return "Sorry, I don't have a translation for that word."
    #if word is key in dictionary english_to_elvish
    #return english_to_elvish[word]
    #else
    #return "Sorry, I don't know that word."

is_in_dic = translate("heaven")
print(is_in_dic)

not_in_dic = translate("suddenly")
print(not_in_dic)