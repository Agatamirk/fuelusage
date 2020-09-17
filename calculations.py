def spalanie(przebieg_przed, przebieg_po, ile_paliwa_zatankowano):
    spalanie = (ile_paliwa_zatankowano * 100/(przebieg_po - przebieg_przed))
    return (round(spalanie, 2))