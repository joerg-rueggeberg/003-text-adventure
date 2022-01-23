print('''
      ________________.  ___     .______
     /                | /   \    |   _  \
    |   (-----|  |----`/  ^  \   |  |_)  |
     \   \    |  |    /  /_\  \  |      /
.-----)   |   |  |   /  _____  \ |  |\  \-------.
|________/    |__|  /__/     \__\| _| `.________|
 ____    __    ____  ___     .______    ________.
 \   \  /  \  /   / /   \    |   _  \  /        |
  \   \/    \/   / /  ^  \   |  |_)  ||   (-----`
   \            / /  /_\  \  |      /  \   \
    \    /\    / /  _____  \ |  |\  \---)   |
     \__/  \__/ /__/     \__\|__| `._______/
''')
print("\nWillkommen auf Tatooine, Kopfgeldjäger '" + input("Wie lautet dein Name?\n") + "'!")
print("\nDeine Mission lautet: Finde den verschollenen Droiden 'R2D2' bevor das Imperium dir zuvorkommt.")

print(
    "\nKAPITEL 1:\nDu landest deinen Gleiter hinter einer Felsformation in Sichtweite einer kleinen Siedlung mit "
    "einigen Hütten.\nLinks von der Felsformation befindet sich ein schmaler Felsspalt, doch du kannst nicht sehen "
    "wohin er führt. Rechts findest du einen großen Torbogen der in die Felsformation geschlagen wurde.")

# Choice 1
c1 = input("Welchen Weg schlägst du ein? (links/ rechts):\n").lower()
if c1 == "rechts":
    print(
        "\nDu hast zwei Strumtruppen übersehen, die sich hinter dem Torbogen als Wache aufgestellt haben. "
        "Als sie dich erblicken, beginnen diese sofort zu feuern.\nÜberraschenderweise, und anders als in den Filmen, "
        "erwischen Sie dich sehr zuverlässig. Du wirst mehrfach getroffen, sinkst zu Boden und stirbst."
        "\n\nMISSION GESCHEITERT!")
else:
    print(
        "\nObwohl du noch nicht abschätzen kannst, was dich hinter dem kleinen Eingang direkt im Fels erwartet, "
        "versuchst du dich durch die Öffnung zu pressen. Es ist stockdunkel sobald du den Eingang passiert hast. "
        "Kurz darauf bemerkst du, wie der Boden unter deinen Füßen nachgibt und du zu fallen beginnst."
        "\nNach wenigen Momenten voller Panik im freien Fall tauchst du in ein unterirdisches Wasserdepot ein ohne "
        "dich zu verletzen.")

print(
    "\nKAPITEL 2:\nIn der Ferne entdeckst du eine Art Ufer. Doch aufgrund der Dunkelheit kannst du nicht mehr "
    "erkennen, ohne zuvor dorthin zu schwimmen. In der Mitte des Wasserdepots befindet sich eine Art künstliche "
    "Plattform, hellbeleuchtet, eine merkwürdiger Mechanismus scheint sich darauf zu befinden.")

# Choice 2
c2 = input("Welchen Ort möchtest du untersuchen? (Ufer/ Plattform):\n")
if c2.lower() == "plattform":
    print(
        "\nDu schwimmst die wenigen Meter bis zur Plattform. Es gelingt dir dich mit etwas Kraft auf die Plattform zu "
        "ziehen. Sofort richten sich einige Scheinwerfer, die in die Plattform eingelassen wurden, auf dich. Du hörst "
        "einen Mechanismus und kannst grade noch sehen, wie die Vorrichtung auf der Plattform sich nach dir "
        "ausrichtet. Du siehst einen grellen, roten Lichtblitz. Dann wird es schwarz. Du bist tot."
        "\n\nMISSION GESCHEITERT!")
else:
    print(
        "\nDer Weg zum Ufer ist weiter als du erwartet hättest und es kostet dich einiges an Kraft es zu erreichen. "
        "Das Licht das von der mysteriösen Plattform in der Mitte des Depots ausging verblasst immer mehr, je weiter "
        "du dich auf das Ufer zubewegst. Als du am Ufer ankommst, siehst du hinter einer Anöhe ein Lagerhaus. Und drei "
        "mögliche Eingänge.")

    print("\nKAPITEL 3:\nDu siehst eine rote Tür, eine blaue Tür und eine gelbe Tür.")

    # Choice 3
    c3 = input("Für welche Entscheidest du dich? (rot/ blau/ gelb)\n")
    if c3.lower() == "rot":
        print(
            "Du machst dich am Schloss der roten Tür zu schaffen. Als plötzlich zwei Flammenwerfer aus den Giebeln "
            "ausfahren und damit beginnen, Feuer auf dich zu speien.\n\nMISSION GESCHEITERT!")
    elif c3.lower() == "blau":
        print(
            "Du machst dich am Schloss der roten Tür zu schaffen. Als plötzlich zwei Eiswerfer aus den Giebeln "
            "ausfahren und damit beginnen, dich zu vereisen.\n\nMISSION GESCHEITERT!")
    elif c3.lower() == "gelb":
        print(
            "\nMit ein wenig Feingefühl gelingt es dir die Tür zu öffnen. In einer der hinteren Ecken des Raumes "
            "findest du wonach du gesucht hast: 'R2D2'...\n\nMISSION ERFOLGREICH!")
    else:
        print(
            "Noch bevor du eine der Türen erreichst wirst du von irgendeiner fremdartigen Kreatur angefallen und "
            "zerfleischt.\n\nMISSION GESCHEITERT!")
