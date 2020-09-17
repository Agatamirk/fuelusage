from calculations import spalanie
from flask import Flask, request, render_template

def home_page():
    errors = ""
    if request.method == "POST":
        przebieg_przed = None
        przebieg_po = None
        ile_paliwa_zatankowano = None
        try:
            przebieg_przed = int(request.form["przebieg_przed"])
        except:
            errors += "<p>{!r} Nie wpisałeś przebiegu przed tankowaniem!</p>\n".format(request.form["przebieg_przed"])
        try:
            przebieg_po = int(request.form["przebieg_po"])
        except:
            errors += "<p>{!r} Nie wpisałeś przebiegu po tankowaniu!</p>\n".format(request.form["przebieg_przed"])
        try:
            ile_paliwa_zatankowano = int(request.form["ile_paliwa_zatankowano"])
        except:
            errors += "<p>{!r} Nie wpisałeś ilości zatankowanego paliwa w litrach!</p>\n".format(request.form["przebieg_przed"])

        if przebieg_przed is not None and przebieg_po is not None and ile_paliwa_zatankowano is not None:
            result = spalanie(przebieg_przed, przebieg_po, ile_paliwa_zatankowano)
            return render_template("result.html").format(result=result)

    return render_template("index.html").format(errors=errors)
