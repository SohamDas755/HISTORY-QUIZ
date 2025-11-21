# ...existing code...
print("WHAT HISTORY TOPIC YOU WANNA DO A QUIZ?")
print("a. WORLD WAR 1")
print("b. WORLD WAR 2")
print("c. INDO-PAKISTAN WARS")
print("d. COLD WAR")
choice = input("WHATS YOUR CHOICE (a/b/c/d): ")

if choice == "a":
    score = 0
    
    print("1. WHAT IS THE NAME OF THE DISASTROUS CAMPAIGN LAUNCHED BY THE ALLIES IN 1915 TO CAPTURE THE OTTOMAN CAPITAL OF CONSTANTINOPLE?")
    print("a. TREBIZOND CAMPAIGN")
    print("b. GALLIPOLI CAMPAIGN")
    print("c. SINAI AND PALESTINE CAMPAIGN")
    ans = input("YOUR ANSWER (a/b/c): ")
    if ans == "b":
        print("CORRECT")
        score = score + 1
    else:
        print("WRONG")

    print("2. WHO WAS THE FIRST LORD OF ADMIRALTY AT THE OUTBREAK OF WORLD WAR I IN UK, THEN LATER FOUNDED THE ROYAL NAVAL AIR SERVICE?")
    print("a. LORD MOUNTBATTEN")
    print("b. ARCHIBALD WILLIAM MURRAY")
    print("c. WINSTON CHURCHILL")
    ans = input("YOUR ANSWER (a/b/c): ")
    if ans == "c":
        print("CORRECT")
        score = score + 1
    else:
        print("WRONG")

    print("3. WHICH TREATY ENDED THE STATE OF WAR BETWEEN GERMANY AND THE ALLIED POWERS IN 1919?")
    print("a. TREATY OF VERSAILLES")
    print("b. TREATY OF PARIS")
    print("c. TREATY OF LONDON")
    ans = input("YOUR ANSWER (a/b/c): ")
    if ans == "a":
        print("CORRECT")
        score = score + 1
    else:
        print("WRONG")

    print("4. WHICH BATTLE IS CONSIDERED THE BLOODIEST BATTLE OF WORLD WAR I, WITH OVER ONE MILLION CASUALTIES?")
    print("a. BATTLE OF SOMME")
    print("b. BATTLE OF VERDUN")
    print("c. BATTLE OF TANNENBERG")
    ans = input("YOUR ANSWER (a/b/c): ")
    if ans == "b":
        print("CORRECT")
        score = score + 1
    else:
        print("WRONG")

    print("5. WHICH ASSASSINATION IN 1914 IS OFTEN CITED AS THE IMMEDIATE CAUSE THAT TRIGGERED THE OUTBREAK OF WORLD WAR I?")
    print("a. ASSASSINATION OF ARCHDUKE FRANZ FERDINAND")
    print("b. ASSASSINATION OF TSAR NICHOLAS II")
    print("c. ASSASSINATION OF OTTO VON BISMARCK")
    ans = input("YOUR ANSWER (a/b/c): ")
    if ans == "a":
        print("CORRECT")
        score = score + 1
    else:
        print("WRONG")

    print("YOUR TOTAL SCORE IS", score, "OUT OF 5")

elif choice == "b":
    score = 0

    print("1. WHICH US GENERAL WAS APPOINTED AS THE SUPREME COMMANDER OF THE ALLIED EXPEDITIONARY FORCES IN EUROPE DURING WORLD WAR II?")
    print("a. GEORGE S. PATTON")
    print("b. DWIGHT D. EISENHOWER")
    print("c. DOUGLAS MACARTHUR")
    ans = input("YOUR ANSWER (a/b/c): ")
    if ans == "b":
        print("CORRECT")
        score = score + 1
    else:
        print("WRONG")

    print("2. WHAT WAS THE CODE NAME FOR THE ALLIED INVASION OF NORMANDY ON JUNE 6, 1944?")
    print("a. OPERATION OVERLORD")
    print("b. OPERATION BARBAROSSA")
    print("c. OPERATION MARKET GARDEN")
    ans = input("YOUR ANSWER (a/b/c): ")
    if ans == "a":
        print("CORRECT")
        score = score + 1
    else:
        print("WRONG")

    print("3. WHICH BATTLE IS CONSIDERED THE TURNING POINT OF THE WAR IN THE PACIFIC THEATRE DURING WORLD WAR II?")
    print("a. BATTLE OF MIDWAY")
    print("b. BATTLE OF GUADALCANAL")
    print("c. BATTLE OF IWO JIMA")
    ans = input("YOUR ANSWER (a/b/c): ")
    if ans == "a":
        print("CORRECT")
        score = score + 1
    else:
        print("WRONG")

    print("4. WHAT WAS THE NAME OF THE SECRET PROJECT THAT DEVELOPED THE ATOMIC BOMBS USED IN WORLD WAR II?")
    print("a. MARSHALL PLAN")
    print("b. MANHATTAN PROJECT")
    print("c. TRINITY PROJECT")
    ans = input("YOUR ANSWER (a/b/c): ")
    if ans == "b":
        print("CORRECT")
        score = score + 1
    else:
        print("WRONG")

    print("5. WHICH CONFERENCE IN 1945 LAID THE FOUNDATION FOR THE POST-WAR WORLD ORDER AND THE CREATION OF THE UNITED NATIONS?")
    print("a. YALTA CONFERENCE")
    print("b. POTSDAM CONFERENCE")
    print("c. SAN FRANCISCO CONFERENCE")
    ans = input("YOUR ANSWER (a/b/c): ")
    if ans == "a":
        print("CORRECT")
        score = score + 1
    else:
        print("WRONG")

    print("YOUR TOTAL SCORE IS", score, "OUT OF 5")

elif choice == "c":
    print("INDO-PAKISTAN WARS QUIZ COMING SOON")

else:
    print("INVALID OPTION")