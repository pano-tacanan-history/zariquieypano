from lingpy import *

def run(wordlist):

    D = {0: wordlist.columns}
    for idx in wordlist:
        D[idx] = [wordlist[idx, h] for h in D[0]]
    wl = Wordlist(D)
    for idx in wl:
        wl[idx, "tokens"] = [x for x in wl[idx, "tokens"] if x != "+"]
    lex = LexStat(wl)
    lex.get_scorer(runs=10000)

    lex.cluster(threshold=0.55, method="lexstat", cluster_method="infomap", ref="autocogid")
    lex.cluster(threshold=0.45, method="sca", cluster_method="infomap", ref="autoscaid")

    D = {0: wordlist.columns+["autocogid", "autoscaid"]}
    for idx in lex:
        D[idx] = [lex[idx, h] for h in D[0]]
    return Wordlist(D)
