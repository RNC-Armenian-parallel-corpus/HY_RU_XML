def convert_tags(tag_string):
    '''
    Replace dissimilar EANC tags with RNC ones
    '''
    # fast track for case where no tags
    if tag_string == '':
        return ''
    # main track
    else:
        tag_list = tag_string.split(',')
        if len(tag_list) > 1:
            if tag_list[1].isupper(): # when two POS tags
                pos = ','.join(tag_list[:2])
                lex_gram = ','.join(tag_list[2:])
                return convert_pos(pos) + ',' + convert_lex_gram(lex_gram)
            else: # when one POS tag
                pos = tag_list[0]
                lex_gram = ','.join(tag_list[1:])
                return convert_pos(pos) + ',' + convert_lex_gram(lex_gram)
        else: # only POS tag (same as "elif len(tag_list) == 1") 
            pos = tag_list[0]
            return convert_pos(pos)
    
def convert_pos(pos_tag):
    pos_dict = {
        # format is "EANC: RNC"
        "PREP": "PR",
        "N": "S",
        "PRON,S": "SPRO", "S,PRON": "SPRO",
        "PRON": "SPRO/APRO", # in EANC PRON without S/ A/ ADV exist
        "A,PRON": "APRO", "PRON,A": "APRO",
        "A,NUM": "ANUM", "NUM,A": "ANUM",
        "ADV,PRON": "ADVPRO", "PRON,ADV": "ADVPRO"
    }
    if pos_tag in pos_dict:
        return pos_dict[pos_tag]
    else:
        return pos_tag

def convert_lex_gram(lex_gram_tag):
    lex_gram_dict = {
        # Case
        "obl": "gen/dat", # to older version, more match with Russian
        # Mood/ form
        "imp": "imper",
        "sbjv": "subj",
        # Participle
        "ptcp": "partcp",
        # Converb + Aspect
        "dest": "des",
        "ipfv": "ipf",
        "pfv": "pf",
        # Grade
        "sup": "supr",
        # Tense
        "prs": "praes",
        "pst": "praet",
        # Voice
        "pass": "med",
        # Person + Determination
        "1": "2p",
        "2": "2p",
        "3": "3p",
        "poss.1": "poss1p",
        "poss.2": "poss2p",
        # Lexical/ other categories
        "hum": "pers",
        "inanim": "inan",
        "topn": "topon",
        "tr": "tran",
        "intr/tr": "intr/tran"
    }
    lgr_tags_list = lex_gram_tag.split(',')
    # delete OBL (because of stem type) if ABL or INS case is present
    if 'obl' in lgr_tags_list:
        if 'abl' in lgr_tags_list or 'ins' in lgr_tags_list \
                or 'gen' in lgr_tags_list: # or even GEN for pronouns
            lgr_tags_list.remove('obl')
    # get RELATIONAL NOUN tag on condition GEN/ OBL + NMLZ + DEF
    if ('gen' in lgr_tags_list and 'nmlz' in lgr_tags_list \
            and 'def' in lgr_tags_list) or ('obl' in lgr_tags_list \
            and 'nmlz' in lgr_tags_list and 'def' in lgr_tags_list):
        lgr_tags_list.append('rel')
    # main part
    for i in range(len(lgr_tags_list)):
        if lgr_tags_list[i] in lex_gram_dict:
            lgr_tags_list[i] = lex_gram_dict[lgr_tags_list[i]]
    return ','.join(lgr_tags_list)