init:
    image bg holst = "bg holst.jpg"
    $ m = Character(u'Serg', color="#c8ffc8")
    
label start:
    scene bg holst

    m "привет"

    menu:

        "Это видеоигра.":
            jump game

        "Это интерактивная книга.":
            jump book

    label game:

        m "Это своего рода видеоигра, в которую можно играть на компьютере или консоли."

        jump marry

    label book:

        m "Это как интерактивная книга, которую можно читать на компьютере или консоли."

        jump marry

    label marry:

        "И так мы стали командой по разработке визуальных новелл."

    return