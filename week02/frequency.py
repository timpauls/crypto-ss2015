#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This assignment is to implement some functions useful to performing
classical cipher attacks.

For this assignment, you have to implement some functions and decode a
ciphertext. See below.
"""

import hashlib
import pdb

######################################################################
#
# Helper functions
#
######################################################################

en_alphabet = "abcdefghijklmnopqrstuvwxyz"


#
# This function returns true if and only if the character c is an alphabetic character
#
def is_alphabetic_char(c):
    return (c.lower() in en_alphabet)

#
# This function converts a single character into its numeric value 
#
def char_to_num(c):
    return en_alphabet.index(c.lower())

#
# This function returns returns the character corresponding to x mod 26
# in the english alphabet
#
def num_to_char(x):
    return en_alphabet[x % 26]


######################################################################
#
# Assignments
#
######################################################################

# a) Implement a Python function that performs frequency attacks on a
# mono-alphabetic substitution ciphers.  This function should take a
# ciphertext string and compute a histogram of the incidence each letter
# (ignoring all non alphabet characters)  and return a list of pairs
# (letter, incidence percentage) sorted by incidence percentage.

def count_alphabetic_characters(text):
    count = 0
    for letter in text:
        if is_alphabetic_char(letter):
            count += 1
    return count


def compute_incidence(ciphertext):
    pairList = []
    for letter in en_alphabet:
        percentage = ciphertext.count(letter)*100.0/count_alphabetic_characters(ciphertext)
        pairList.append((letter, percentage))
    pairList.sort(key = lambda pair: pair[1], reverse=True)
    return pairList

def print_incidence(incidence):
    for pair in incidence:
        print "%s: %f%%"%(pair[0], pair[1])


# b) Implement a Python function that takes a partial mono-alphabetic
# substitution and a ciphertext and returns a potential plaintext.
# The partial mono-alphabetic substitution should be specified as
# follows: As a 26 character string where the character at position i
# is the substitution of ith character of the alphabet, OR an
# underscore ‘_’ if the corresponding substitution is unknown.  The
# potential plaintext should be the ciphertext with values specified
# by the mono-alphabetic substitution replaced by the lower-case
# plaintext.  If the corresponding character is unknown (i.e. ‘_’ in
# the monoalphabetic substitution cipher) print the cipher text as an
# uppercase character.

def monoalphabetic_substitution(text, subs):
    plainText = list(text)
    for i in range(len(plainText)):
        letter = plainText[i]
        if is_alphabetic_char(letter):
            plainLetter = subs[char_to_num(letter)]
            if is_alphabetic_char(plainLetter):
                plainText[i] = plainLetter
            else:
                plainText[i] = letter.upper()
    return "".join(plainText)


# c) Use your functions from (a) and (b) to decrypt the following
# cipher text. The plain text is written in English. All characters
# have been converted to lower case.

cipher_text = "sa. txcapmwz xmpsct, kxm kgt qtqgppr ocar pgjc nu jxc smaunuyt, tgoc qfmu jxmtc umj nuvachqcuj mwwgtnmut kxcu xc kgt qf gpp unyxj, kgt tcgjcl gj jxc eacgzvgtj jgepc. n tjmml qfmu jxc xcgajx-aqy gul fnwzcl qf jxc tjnwz kxnwx mqa ontnjma xgl pcvj ecxnul xns jxc unyxj ecvmac. nj kgt g vnuc, jxnwz fncwc mv kmml, eqpemqt-xcglcl, mv jxc tmaj kxnwx nt zumku gt g \"fcuguy pgkrca.\" iqtj qulca jxc xcgl kgt g eamgl tnpoca egul ucgapr gu nuwx gwamtt. \"jm igsct smajnsca, s.a.w.t., vams xnt vancult mv jxc w.w.x.,\" kgt cuyagocl qfmu nj, knjx jxc lgjc \"1884.\" nj kgt iqtj tqwx g tjnwz gt jxc mpl-vgtxnmucl vgsnpr fagwjnjnmuca qtcl jm wgaar-lnyunvncl, tmpnl, gul acgttqanuy.\n\
\n\
\"kcpp, kgjtmu, kxgj lm rmq sgzc mv nj?\"\n\
\n\
xmpsct kgt tnjjnuy knjx xnt egwz jm sc, gul n xgl ynocu xns um tnyu mv sr mwwqfgjnmu.\n\
\n\
\"xmk lnl rmq zumk kxgj n kgt lmnuy? n ecpncoc rmq xgoc crct nu jxc egwz mv rmqa xcgl.\"\n\
\n\
\"n xgoc, gj pcgtj, g kcpp-fmpntxcl, tnpoca-fpgjcl wmvvcc-fmj nu vamuj mv sc,\" tgnl xc. \"eqj, jcpp sc, kgjtmu, kxgj lm rmq sgzc mv mqa ontnjma't tjnwz? tnuwc kc xgoc eccu tm quvmajqugjc gt jm sntt xns gul xgoc um umjnmu mv xnt caagul, jxnt gwwnlcujgp tmqocuna ecwmsct mv nsfmajguwc. pcj sc xcga rmq acwmutjaqwj jxc sgu er gu cdgsnugjnmu mv nj.\"\n\
\n\
\"n jxnuz,\" tgnl n, vmppmknuy gt vga gt n wmqpl jxc scjxmlt mv sr wmsfgunmu, \"jxgj la. smajnsca nt g tqwwcttvqp, cplcapr sclnwgp sgu, kcpp-ctjccscl tnuwc jxmtc kxm zumk xns ynoc xns jxnt sgaz mv jxcna gffacwngjnmu.\"\n\
\n\
\"ymml!\" tgnl xmpsct. \"cdwcppcuj!\"\n\
\n\
\"n jxnuz gptm jxgj jxc famegenpnjr nt nu vgomqa mv xnt ecnuy g wmqujar fagwjnjnmuca kxm lmct g yacgj lcgp mv xnt ontnjnuy mu vmmj.\"\n\
\n\
\"kxr tm?\"\n\
\n\
\"ecwgqtc jxnt tjnwz, jxmqyx manynugppr g ocar xgultmsc muc xgt eccu tm zumwzcl gemqj jxgj n wgu xgalpr nsgynuc g jmku fagwjnjnmuca wgaarnuy nj. jxc jxnwz-namu vcaaqpc nt kmau lmku, tm nj nt conlcuj jxgj xc xgt lmuc g yacgj gsmquj mv kgpznuy knjx nj.\"\n\
\n\
\"fcavcwjpr tmqul!\" tgnl xmpsct.\n\
\n\
\"gul jxcu gygnu, jxcac nt jxc 'vancult mv jxc w.w.x.' n txmqpl yqctt jxgj jm ec jxc tmscjxnuy xquj, jxc pmwgp xquj jm kxmtc scsecat xc xgt fmttnepr ynocu tmsc tqaynwgp gttntjguwc, gul kxnwx xgt sglc xns g tsgpp factcujgjnmu nu acjqau.\"\n\
\n\
\"acgppr, kgjtmu, rmq cdwcp rmqatcpv,\" tgnl xmpsct, fqtxnuy egwz xnt wxgna gul pnyxjnuy g wnygacjjc. \"n gs emqul jm tgr jxgj nu gpp jxc gwwmqujt kxnwx rmq xgoc eccu tm ymml gt jm ynoc mv sr mku tsgpp gwxncocscujt rmq xgoc xgenjqgppr qulcaagjcl rmqa mku genpnjnct. nj sgr ec jxgj rmq gac umj rmqatcpv pqsnumqt, eqj rmq gac g wmulqwjma mv pnyxj. tmsc fcmfpc knjxmqj fmttcttnuy ycunqt xgoc g acsgazgepc fmkca mv tjnsqpgjnuy nj. n wmuvctt, sr lcga vcppmk, jxgj n gs ocar sqwx nu rmqa lcej.\"\n\
\n\
xc xgl ucoca tgnl gt sqwx ecvmac, gul n sqtj glsnj jxgj xnt kmalt ygoc sc zccu fpcgtqac, vma n xgl mvjcu eccu fnhqcl er xnt nulnvvcacuwc jm sr glsnagjnmu gul jm jxc gjjcsfjt kxnwx n xgl sglc jm ynoc fqepnwnjr jm xnt scjxmlt. n kgt famql, jmm, jm jxnuz jxgj n xgl tm vga sgtjcacl xnt trtjcs gt jm gffpr nj nu g kgr kxnwx cgaucl xnt gffamogp. xc umk jmmz jxc tjnwz vams sr xgult gul cdgsnucl nj vma g vck snuqjct knjx xnt ugzcl crct. jxcu knjx gu cdfacttnmu mv nujcactj xc pgnl lmku xnt wnygacjjc, gul wgaarnuy jxc wguc jm jxc knulmk, xc pmmzcl moca nj gygnu knjx g wmuocd pcut.\n\
\n\
\"nujcactjnuy, jxmqyx cpcscujgar,\" tgnl xc gt xc acjqaucl jm xnt vgomqanjc wmauca mv jxc tcjjcc. \"jxcac gac wcajgnupr muc ma jkm nulnwgjnmut qfmu jxc tjnwz. nj ynoct qt jxc egtnt vma tcocagp lclqwjnmut.\"\n\
\n\
\"xgt gurjxnuy ctwgfcl sc?\" n gtzcl knjx tmsc tcpv-nsfmajguwc. \"n jaqtj jxgj jxcac nt umjxnuy mv wmutchqcuwc kxnwx n xgoc mocapmmzcl?\"\n\
\n\
\"n gs gvagnl, sr lcga kgjtmu, jxgj smtj mv rmqa wmuwpqtnmut kcac caamucmqt. kxcu n tgnl jxgj rmq tjnsqpgjcl sc n scguj, jm ec vaguz, jxgj nu umjnuy rmqa vgppgwnct n kgt mwwgtnmugppr yqnlcl jmkgalt jxc jaqjx. umj jxgj rmq gac cujnacpr kamuy nu jxnt nutjguwc. jxc sgu nt wcajgnupr g wmqujar fagwjnjnmuca. gul xc kgpzt g ymml lcgp.\"\n\
\n\
\"jxcu n kgt anyxj.\"\n\
\n\
\"jm jxgj cdjcuj.\"\n\
\n\
\"eqj jxgj kgt gpp.\"\n\
\n\
\"um, um, sr lcga kgjtmu, umj gpp-er um scgut gpp. n kmqpl tqyyctj, vma cdgsfpc, jxgj g factcujgjnmu jm g lmwjma nt smac pnzcpr jm wmsc vams g xmtfnjgp jxgu vams g xquj, gul jxgj kxcu jxc nunjngpt 'w.w.' gac fpgwcl ecvmac jxgj xmtfnjgp jxc kmalt 'wxganuy wamtt' ocar ugjqagppr tqyyctj jxcstcpoct.\"\n\
\n\
\"rmq sgr ec anyxj.\"\n\
\n\
\"jxc famegenpnjr pnct nu jxgj lnacwjnmu. gul nv kc jgzc jxnt gt g kmaznuy xrfmjxctnt kc xgoc g vactx egtnt vams kxnwx jm tjgaj mqa wmutjaqwjnmu mv jxnt quzumku ontnjma.\"\n\
\n\
\"kcpp, jxcu, tqffmtnuy jxgj 'w.w.x.' lmct tjgul vma 'wxganuy wamtt xmtfnjgp,' kxgj vqajxca nuvcacuwct sgr kc lagk?\"\n\
\n\
\"lm umuc tqyyctj jxcstcpoct? rmq zumk sr scjxmlt. gffpr jxcs!\""


# Get frequency table
# print_incidence(compute_incidence(cipher_text))

# c: 10.449026%
# j: 9.121717%
# g: 8.641627%
# n: 8.133296%
# m: 8.076814%
# t: 7.088393%
# u: 6.636543%
# x: 6.382378%
# a: 5.083310%
# l: 3.586557%
# p: 3.558317%
# w: 3.162948%
# q: 3.078226%
# s: 2.880542%
# k: 2.456933%
# r: 2.146286%
# v: 2.146286%
# y: 1.835640%
# f: 1.524993%
# e: 1.299068%
# o: 1.186106%
# z: 1.129624%
# d: 0.225925%
# h: 0.084722%
# i: 0.084722%
# b: 0.000000%

# The most used letter is in english is e.
# So: cipher 'c' = plain 'e'
# subs = "__e_______________________"
# print monoalphabetic_substitution(cipher_text, subs)

# From the partially decrypted text I notice the word 'JXe' appearing multiple times.
# I assume this is the word 'the' (which also matches the frequency table).
# cipher 'j' = plain 't'; cipher 'x' = plain 'h'
# subs = "__e______t_____________h__"
# print monoalphabetic_substitution(cipher_text, subs)

# From frequency table:
# cipher 'g' = plain 'a'
# subs = "__e___a__t_____________h__"
# print monoalphabetic_substitution(cipher_text, subs)

# I assume 'aUL' is 'and'
# cipher 'u' = plain 'n'; cipher 'l' = plain 'd'
# subs = "__e___a__t_d________n__h__"
# print monoalphabetic_substitution(cipher_text, subs)

# 'tM' is probably 'to', 'aT' = 'as', 'N' = 'i'
# cipher 'm' = plain 'o', cipher 't' = plain 's', cipher 'n' = plain 'i
# subs = "__e___a__t_doi_____sn__h__"
# print monoalphabetic_substitution(cipher_text, subs)

# "KePP, Katson, Khat do RoQ SaZe oV it?" = "well, watson, what do you make of it?"
# k->w, p->l, r->y, q->u, s->m, z->k, v->f
# subs = "__e___a__twdoi_luymsnf_h_k"
# print monoalphabetic_substitution(cipher_text, subs)

# From the text: a->r, w->c, o->v, y->g, f->p, h->q, e->b, d->x
# Remaining two are j and z. Probably b->z, i->j
subs = "rzexbpaqjtwdoivluymsnfchgk"
# print monoalphabetic_substitution(cipher_text, subs)

plain_text = monoalphabetic_substitution(cipher_text, subs)

# Show that you got the right plain text by calling the following
# function:

def test():
    assert(hashlib.sha256(plain_text).hexdigest() ==
           '1dc539240874ef45badaa09adbc479136d44485a6bca8d9722a590ad9b9c5869')

test()