class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
        "1. Factorii primari ai deciziei manageriale se afla printre elementele prezentate mai jos: \na. decidentul si mediul ambiant decisional \nb.decidentul si elementele endogene firmei care alcatuiesc situatia decizionalac. \nc.decidentul si lementele exogene firmei ce alcatuiesc situatia decizionalad. \nd.decidentul si variantele decizionalee. \ne.decidentul, variantele decizionale si criteriile decizionale \nRaspuns:",
            "2.Deciziile de management sunt adoptate, la nivelul unei societati comerciale, de catre: \na. adunarea generala a actionarilor si consiliul de administratie \nb.directorul general \nc.directorul general si directorii executivi \nd.directori, sefi de compartimente si maistrie.practic de orice manager individual si de grup, indiferent de pozitia ierarhica din cadrul organizatiei \nRaspuns:",
            "3.Precizarea modalitatilor de realizare a obiectivelor este un element de continut al functiei: \na.previziune \nb.organizarec. \nc.coordonared. \nd.antrenaree. \ne.control - evaluare;\nRaspuns:",
            "4.Comunicarea si motivarea constituie suportul: \na. relatiilor intre manageri si executanti \nb. subsistemului metodologic si decizional \nc. functiunii de personal si de cercetare-dezvoltare \nd. functiei de coordonare si de antrenare \ne. functiei de coordonare si activitatii de personal\nRaspuns:",
            "5.Unele componente ale strategiei se afla printre elementele prezentate mai jos. Va rugam sa leidentificati: \na. obiective strategice, misiune, sinergie, resurse, oameni, informatii \nb. obiective strategice, misiune, termene, oameni, informatii, avantaj competitive  \nc. obiective strategice, misiune, resurse, modalitati, termene, avantaj competitive \nd. obiective strategice, misiune, modalitati, resurse, oameni, avantaj competitive. \ne. obiective strategice, misiune, modalitati, oameni, termene, avantaj competitive;\nRaspuns:",
            "6.Aratati care dintre variantele prezentate mai jos reprezinta functii ale managementului firmei: \na. previziune, organizare, coordonare, antrenare, control-evaluare \nb. previziune, cercetare-dezvoltare, organizare, productie, salarizare \nc. previziune, organizare, planificare, conducere, motivare \nd. previziune, coordonare, decizie, comerciala, financiar-contabila \ne. previziune, organizare, cercetare-dezvoltare, comunicare, personal;\nRaspuns:",
            "7.Ce elemente definesc un post: \na. sarcinile, atributiile, lucrarile \nb. sarcinile, atributiile, responsabilitatile \nc. sarcinile, activitatile, competentele \nd. sarcinile, competentele, responsabilitatile \ne. sarcinile, competentele, obiectivele specifice  \nRaspuns:",
            "8.Postul, compartimentul si ponderea ierarhica sunt componente structurale ale firmei.Ce alte subdiviziuni organizatorice cunoasteti din cele prezentate in continuare: \na. functia, nivelul ierarhic si relatiile organizatorice \nb. sarcinile, functiunile, functia \nc. sarcinile, atributiile, obiectivele individuale \nd. functia, nivelul ierarhic si competentele \ne. functia, functiunile si activitatile\nRaspuns:",
            "9.Filtrajul, ca deficienta a sistemului informational, consta in: \na. modificarea intentionata a mesajului informational \nb. modificarea mesajului informational prin transmiterea repetata pe circuite informationale paralele aacelorasi infomati \nc. modificarea informatiei functie de modificarile in mijloacele de tratare a acesteia \nd. modificarea continutului informatiei la solicitarea managementului de nivel superior \ne. modificarea neintentionata a continutului informatiei \nRaspuns:",
            "10.Care dintre variante exprima cel mai bine componentele sistemului informational? \na. date-informatii, circuite informationale, documente informationale, proceduri informationale \nb. date-informatii, circuite informationale, documente informationale, mijloace de tratare a informatiei \nc. date-informatii, circuite si fluxuri informationale, procedure informationale, calculatorul electronic \nd. date-informatii, circuite si fluxuri informationale, documente informationale, mijloace de tratare ainformatiei \ne. date-informatii, circuite si fluxuri informationale, procedure informationale, mijloace de tratare ainformatiei \nRaspuns:",


    ]


questions = [
    Question(question_prompts[0], "a"),
        Question(question_prompts[1], "c"),
        Question(question_prompts[2], "a"),
        Question(question_prompts[3], "d"),
        Question(question_prompts[4], "c"),
        Question(question_prompts[5], "a"),
        Question(question_prompts[6], "d"),
        Question(question_prompts[7], "a"),
        Question(question_prompts[8], "a"),
        Question(question_prompts[9], "e"),a
    ]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Punctajul obtinut este", score)
run_quiz(questions)