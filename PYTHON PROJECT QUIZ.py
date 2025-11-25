import random

print("WHAT HISTORY TOPIC YOU WANNA DO A QUIZ?")
print("a. WORLD WAR 1")
print("b. WORLD WAR 2")
print("c. INDO-PAKISTAN WARS")
print("d. COLD WAR")
choice = input("WHATS YOUR CHOICE (a/b/c/d): ")

# ==========================================
# TOPIC A: WORLD WAR 1
# ==========================================
if choice == "a":
    score = 0
    # Pick 5 random numbers between 1 and 10
    questions = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
    
    # Run a loop for the 5 selected numbers
    for q in questions:
        
        if q == 1:
            print("WHAT CAMPAIGN WAS LAUNCHED BY ALLIES IN 1915 TO CAPTURE CONSTANTINOPLE?")
            print("a. TREBIZOND CAMPAIGN")
            print("b. GALLIPOLI CAMPAIGN")
            print("c. SINAI CAMPAIGN")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "b":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 2:
            print("WHO WAS THE FIRST LORD OF ADMIRALTY IN UK AT THE OUTBREAK OF WW1?")
            print("a. LORD MOUNTBATTEN")
            print("b. ARCHIBALD MURRAY")
            print("c. WINSTON CHURCHILL")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "c":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 3:
            print("WHICH TREATY ENDED THE WAR BETWEEN GERMANY AND ALLIED POWERS IN 1919?")
            print("a. TREATY OF VERSAILLES")
            print("b. TREATY OF PARIS")
            print("c. TREATY OF LONDON")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "a":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 4:
            print("WHICH BATTLE IS CONSIDERED THE BLOODIEST BATTLE OF WW1?")
            print("a. BATTLE OF SOMME")
            print("b. BATTLE OF VERDUN")
            print("c. BATTLE OF TANNENBERG")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "b":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 5:
            print("WHICH ASSASSINATION TRIGGERED THE OUTBREAK OF WW1?")
            print("a. ARCHDUKE FRANZ FERDINAND")
            print("b. TSAR NICHOLAS II")
            print("c. OTTO VON BISMARCK")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "a":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 6:
            print("WHAT WAS THE NICKNAME OF THE FAMOUS PILOT MANFRED VON RICHTHOFEN?")
            print("a. THE RED BARON")
            print("b. THE BLACK KNIGHT")
            print("c. THE EAGLE")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "a":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")
        
        elif q == 7:
            print("WHICH SHIP WAS SUNK BY A GERMAN U-BOAT IN 1915 ANGERING THE USA?")
            print("a. TITANIC")
            print("b. LUSITANIA")
            print("c. OLYMPIC")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "b":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 8:
            print("WHAT NEW WEAPON WAS INTRODUCED BY THE BRITISH AT THE BATTLE OF FLERS-COURCELETTE?")
            print("a. TANK")
            print("b. SUBMARINE")
            print("c. JET FIGHTER")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "a":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 9:
            print("WHAT DATE DID THE FIGHTING STOP (ARMISTICE DAY)?")
            print("a. NOV 11, 1918")
            print("b. JUNE 6, 1918")
            print("c. DEC 25, 1918")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "a":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 10:
            print("WHICH EMPIRE COLLAPSED AFTER WW1?")
            print("a. BRITISH EMPIRE")
            print("b. OTTOMAN EMPIRE")
            print("c. JAPANESE EMPIRE")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "b":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

    print("YOUR TOTAL SCORE IS", score, "OUT OF 5")

# ==========================================
# TOPIC B: WORLD WAR 2
# ==========================================
elif choice == "b":
    score = 0
    questions = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)

    for q in questions:
        
        if q == 1:
            print("WHO WAS THE SUPREME COMMANDER OF ALLIED FORCES IN EUROPE?")
            print("a. GEORGE PATTON")
            print("b. DWIGHT D. EISENHOWER")
            print("c. DOUGLAS MACARTHUR")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "b":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 2:
            print("WHAT WAS THE CODE NAME FOR THE INVASION OF NORMANDY?")
            print("a. OPERATION OVERLORD")
            print("b. OPERATION BARBAROSSA")
            print("c. OPERATION MARKET GARDEN")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "a":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 3:
            print("WHICH BATTLE WAS THE TURNING POINT IN THE PACIFIC?")
            print("a. BATTLE OF MIDWAY")
            print("b. GUADALCANAL")
            print("c. IWO JIMA")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "a":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 4:
            print("WHAT PROJECT DEVELOPED THE ATOMIC BOMB?")
            print("a. MARSHALL PLAN")
            print("b. MANHATTAN PROJECT")
            print("c. TRINITY PROJECT")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "b":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 5:
            print("WHICH CONFERENCE LAID THE FOUNDATION FOR THE UN?")
            print("a. YALTA CONFERENCE")
            print("b. POTSDAM CONFERENCE")
            print("c. SAN FRANCISCO CONFERENCE")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "a":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 6:
            print("WHICH EVENT CAUSED THE USA TO JOIN WW2?")
            print("a. BOMBING OF LONDON")
            print("b. ATTACK ON PEARL HARBOR")
            print("c. INVASION OF FRANCE")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "b":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 7:
            print("WHO WAS THE LEADER OF NAZI GERMANY?")
            print("a. ADOLF HITLER")
            print("b. JOSEPH STALIN")
            print("c. BENITO MUSSOLINI")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "a":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 8:
            print("WHICH CITY WAS THE FIRST TO BE HIT BY AN ATOMIC BOMB?")
            print("a. TOKYO")
            print("b. HIROSHIMA")
            print("c. NAGASAKI")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "b":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 9:
            print("WHICH MAJOR BATTLE WAS A TURNING POINT ON THE EASTERN FRONT?")
            print("a. BATTLE OF STALINGRAD")
            print("b. BATTLE OF BRITAIN")
            print("c. BATTLE OF THE BULGE")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "a":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 10:
            print("WHAT DATE WAS D-DAY?")
            print("a. JUNE 6, 1944")
            print("b. MAY 8, 1945")
            print("c. DEC 7, 1941")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "a":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

    print("YOUR TOTAL SCORE IS", score, "OUT OF 5")

# ==========================================
# TOPIC C: INDO-PAKISTAN WARS
# ==========================================
elif choice == "c":
    print("INDO-PAKISTAN WARS QUIZ COMING SOON - STAY TUNED FOR NEW QUIZZES")

# ==========================================
# TOPIC D: COLD WAR
# ==========================================
elif choice == "d":
    score = 0
    questions = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)

    for q in questions:
        
        if q == 1:
            print("WHAT YEAR DID THE BERLIN WALL FALL?")
            print("a. 1987")
            print("b. 1989")
            print("c. 1991")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "b":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 2:
            print("WHAT CRISIS IN 1962 ALMOST CAUSED NUCLEAR WAR?")
            print("a. SUEZ CRISIS")
            print("b. CUBAN MISSILE CRISIS")
            print("c. VIETNAM WAR")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "b":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 3:
            print("WHAT WAS THE FIRST SATELLITE IN SPACE?")
            print("a. APOLLO")
            print("b. VOYAGER")
            print("c. SPUTNIK")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "c":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 4:
            print("WHICH MILITARY ALLIANCE DID THE WEST FORM?")
            print("a. NATO")
            print("b. WARSAW PACT")
            print("c. LEAGUE OF NATIONS")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "a":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 5:
            print("WHICH WAR WAS FOUGHT FROM 1950 TO 1953?")
            print("a. VIETNAM WAR")
            print("b. KOREAN WAR")
            print("c. AFGHAN WAR")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "b":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 6:
            print("WHO WAS THE FIRST MAN ON THE MOON?")
            print("a. YURI GAGARIN")
            print("b. BUZZ ALDRIN")
            print("c. NEIL ARMSTRONG")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "c":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 7:
            print("WHICH WAR ENDED WITH THE FALL OF SAIGON?")
            print("a. KOREAN WAR")
            print("b. VIETNAM WAR")
            print("c. GULF WAR")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "b":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 8:
            print("WHICH SOVIET LEADER INTRODUCED GLASNOST (OPENNESS)?")
            print("a. MIKHAIL GORBACHEV")
            print("b. JOSEPH STALIN")
            print("c. VLADIMIR PUTIN")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "a":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 9:
            print("WHO COINED THE PHRASE 'IRON CURTAIN'?")
            print("a. HARRY TRUMAN")
            print("b. WINSTON CHURCHILL")
            print("c. FRANKLIN ROOSEVELT")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "b":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

        elif q == 10:
            print("WHICH US PRESIDENT SERVED DURING THE CUBAN MISSILE CRISIS?")
            print("a. JOHN F. KENNEDY")
            print("b. RICHARD NIXON")
            print("c. RONALD REAGAN")
            ans = input("YOUR ANSWER (a/b/c): ")
            if ans == "a":
                print("CORRECT")
                score = score + 1
            else:
                print("WRONG")

    print("YOUR TOTAL SCORE IS", score, "OUT OF 5")

else:
    print("INVALID OPTION")
