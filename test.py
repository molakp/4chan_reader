text="why is bill gates SO obsessed with niggers He wants to exterminate them He really is not doing a great job then Hes trying He should try harder By the size of the niggers dicks I guess he already invented the dick enlargement vacine He trained his daughter well hits pipe why is every thread on this board such low effort shit now Always was your just noticing it now Easily manipulated can inject them with anything and give them a cookie and he will never be held accountable for anything bad that happens All whites are obsessed with niggers they give their niggers virgin white women to impregnate as their proudest virtue Nah white people never did love niggers Jews literally worship them like idols Every hollywood movie is centered around niggers every jewish owned sports league is about worshiping niggers ever financial institution and academia is centered around niggers"

offensive_words = ['nigger', 'kike','shit','fuck','fucking','shit','shitlib','nigger','niggers','nigga','cunt','bitch','jew' ]  # Aggiungi qui le parole offensive
    
censored_text = text
print(text)
for word in offensive_words:
    censored_text = censored_text.replace(word, '*' * len(word))
print("CESNORED    " + censored_text)
