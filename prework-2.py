def totoro():
    #plot and some dialogue lifted quite heavily from My Neighbor Totoro (1988)

    invalid_command = "Sorry, I don't know how to do that. Please only use numbers when making selections."
    
    print("Your family has just moved to this farming village in the dusty countryside to be closer") 
    print("to your mother.")
    print("She's recovering from a long illness at the hospital nearby.")
    print("Your older sister has gone to school this morning, and your father is at work drafting")
    print("engineering drawings.")
    print("As you are watching him crumple up yet another draft, a wrinkled lady with a large mole appears")
    print("in the doorway of your new house.")
    print("\n")

    username = input("She says, 'Welcome to the village! What's your name?' \n")
    print("\n")

    print("'Nice to meet you, {}. Please call me Nanny.'".format(username))
    print("'Your daddy has to work, but I've come to look after you today.'")
    print("'Would you like to help me sweep up all this soot?'")
    print("\n")
    print("(1) 'Okay, but I want to use the big kid broom!'")
    print("(2) 'No! I'm going exploring!'")
    choice1 = int(input(username + " chooses: "))
    print("\n")

    if choice1 == 1: #'Okay, but I want to use the big kid broom!'
        print("'What a helpful child! Here is the broom.'")
#        print(" *Received: Broom* ")
        print("Nanny pulls down the attic access and helps {} climb the dusty stairs.".format(username))
        print("It's dark, but in the light from the main floor you think you see movement!")
        print("If you turn your head quickly, you can just glimpse a black ball that blinks at you.")
        print("Now that you look closely, there are more of these fuzzy creatures in the corner of the room.")
        print("\n")
        print("What would {} like to do?".format(username))
        print("(1) Chase them! I want to catch one and hold it in my hands.")
        print("(2) Open the shutters so I can see them better.")
        print("(3) Call for Nanny. What are these things?")
        choice2 = int(input(username + " chooses: "))
        print("\n")

        if choice2 == 1: #Chase them! I want to catch one and hold it in my hands.
            print("Dropping the broom, {} runs at full tilt towards the little swarm of blinking creatures.".format(username))
            print("They bob away, hopping through the air, as if afraid of {}.".format(username))
            print("{} has nearly cornered them, but they scatter and dash away along the walls.".format(username))
            print("But luckily, one little ball is dazed and too slow!")
            print("With arms wide, {} prepares to slap their hands together and catch this little creature.".format(username))
            print("CLAP! {} has it between their fingers!".format(username))
            print("\n")
            print("What would {} like to do?".format(username))
            print("(1) Peek inside my hands and see what I've caught.")
            print("(2) Take it to show Nanny.")
            choice3 = int(input(username + " chooses: "))
            print("\n")

            if choice3 == 1: #Peek inside my hands and see what I've caught.
                print("Peeking inside their hands, {} expects to see the little ball that they captured.".format(username))
                print("But there is nothing in their hands, which are now completely covered in black powder!")
                print("Dirty and perplexed, {} makes their way back down the attic stairs to the home office.".format(username))
                print("'Daddy, look, I almost caught a fuzzy thing! But then I opened my hands and they're all black.'")
                print("Daddy looks up from his drawings. 'Oh I see. Where did you find this fuzzy thing?'")
                print("'It was upstairs in the attic. Do you think there are ghosts upstairs?'")
                print("'Dust bunnies make much more sense than ghosts,' he responds.")
                print("'Why?' {} asks.".format(username))
                print("'Well, ghosts are a lot harder to see. But when you suddenly move from a lighted room to a dark one,")
                print("you can't see for a second, and that's when the dust bunnies come out. Got it?'")
                print("{} responds, 'Boy, yeah! Come out! Come out!'".format(username))
                print("/n")
                print("THE END")
                print("/n")
                print("Thank you for playing through this interactive fiction.")
                #end

            elif choice3 == 2: #Take it to show Nanny.
                print("{} rushes down the attic stairs, almost tripping in excitement.".format(username))
                print("{} is watching their hands so carefully that they almost bump into Nanny at the base".format(username))
                print("of the attic stairs.")
                print("'Careful, little {},' Nanny says, laughing.".format(username))
                print("'Nanny, look!' cries {}. Opening their hands, {} expects to see the little ball".format(username,username))
                print("that they captured.")
                print("But there is nothing in their hands, which are now completely covered in black powder!")
                print("'Ahhh,' says Nanny, 'it appears the soot sprites are hard at work.'")
                print("{} says, 'Soot sprites? Like dust bunnies in my sister's picture book?".format(username))
                print("\n")
                print("'Yes, that's right. They breed in very old, empty houses, building invisible nests,")
                print("and turning everything into dust. I could see them too, when I was a very small child.'")
                print("There's nothing to be frightened of. If we all keep smiling,")
                print("the sprites may gradually go away and leave this place alone.'")
                print("\n")
                print("How would {} like to answer?".format(username))
                print("(1) 'I'm not afraid of dust bunnies!'")
                print("(2) 'S- sprites? Is our house haunted?'")
                choice4 = int(input(username + " chooses: "))
                print("\n")

                if choice4 == 1: #'I'm not afraid of dust bunnies!'
                    print("Nanny nods sagely. 'Of course you aren't, brave child. Just remember, you have to")
                    print("laugh loud to scare away a spirit,' she remarks with a wink.")
                    print("'Let's go get you cleaned up, you're all covered in soot.'")
                    print("'Nanny, will I be able to meet the other spirits near our house?' asks {}.".format(username))
                    print("'Hmm,' Nanny muses, leading our dusty protagonist towards the well.")
                    print("'I think you just might.'")
                    print("/n")
                    print("THE END")
                    print("/n")
                    print("Thank you for playing through this interactive fiction.")
                    #end
                elif choice4 == 2: #'S- sprites? Is our house haunted?'
                    print("'No need to be frightened, my young friend. Just remember, if you laugh loud, the")
                    print("spirit will be scared away. And as for haunted, well - ' Nanny looks out past the trees.")
                    print("'That you are able to see them makes me very glad.'")
                    print("'O-okay,' responds {}. 'Then I won't be scared of them anymore. And I want to ".format(username))
                    print("tell Daddy all about the spirits!'")
                    print("'What a wonderful idea, {}!' remarks Nanny. 'Let's go tell him right now.'".format(username))
                    print("/n")
                    print("THE END")
                    print("/n")
                    print("Thank you for playing through this interactive fiction.")
                    #end
                else:
                    print(invalid_command)
            else:
                print(invalid_command)
        
        elif choice2 == 2: #Open the shutters so I can see them better.
            print("{} hurries over to the shutters to let in some light.".format(username))
            print("As they throw open the shutters and look back towards the ceiling, the little black motes")
            print("rush away into the corners. {} blinks, wondering if they really saw anything before.".format(username))
            print("{} takes the broom and starts to sweep the dusty room, when they think they see some movement".format(username))
            print("just a few steps away behind the shutter. {} carefully moves closer, reaches out, and")
            print("CLAP! {} has it between their fingers!".format(username))
            print("\n")
            print("What would {} like to do?".format(username))
            print("(1) Peek inside my hands and see what I've caught.")
            print("(2) Take it to show Nanny.")
            choice3 = int(input(username + " chooses: "))
            print("\n")

            if choice3 == 1:
                print("Peeking inside their hands, {} expects to see the little ball that they captured.".format(username))
                print("But there is nothing in their hands, which are now completely covered in black powder!")
                print("Dirty and perplexed, {} makes their way back down the attic stairs to the home office.".format(username))
                print("'Daddy, look, I almost caught a fuzzy thing! But then I opened my hands and they're all black.'")
                print("Daddy looks up from his drawings. 'Oh I see. Where did you find this fuzzy thing?'")
                print("'It was upstairs in the attic. Do you think there are ghosts upstairs?'")
                print("'Dust bunnies make much more sense than ghosts,' he responds.")
                print("'Why?' {} asks.".format(username))
                print("'Well, ghosts are a lot harder to see. But when you suddenly move from a lighted room to a dark one,")
                print("you can't see for a second, and that's when the dust bunnies come out. Got it?'")
                print("{} responds, 'Boy, yeah! Come out! Come out!'".format(username))
                print("/n")
                print("THE END")
                print("/n")
                print("Thank you for playing through this interactive fiction.")
                #end
                
            elif choice3 == 2: #Take it to show Nanny.
                print("{} rushes down the attic stairs, almost tripping in excitement.".format(username))
                print("{} is watching their hands so carefully that they almost bump into Nanny at the base".format(username))
                print("of the attic stairs.")
                print("'Careful, little {},' Nanny says, laughing.".format(username))
                print("'Nanny, look!' cries {}. Opening their hands, {} expects to see the little ball".format(username,username))
                print("that they captured.")
                print("But there is nothing in their hands, which are now completely covered in black powder!")
                print("'Ahhh,' says Nanny, 'it appears the soot sprites are hard at work.'")
                print("{} says, 'Soot sprites? Like dust bunnies in my sister's picture book?".format(username))
                print("\n")
                print("'Yes, that's right. They breed in very old, empty houses, building invisible nests,")
                print("and turning everything into dust. I could see them too, when I was a very small child.'")
                print("There's nothing to be frightened of. If we all keep smiling,")
                print("the sprites may gradually go away and leave this place alone.'")
                print("\n")
                print("How would {} like to answer?".format(username))
                print("(1) 'I'm not afraid of dust bunnies!'")
                print("(2) 'S- sprites? Is our house haunted?'")
                choice4 = int(input(username + " chooses: "))
                print("\n")

                if choice4 == 1: #'I'm not afraid of dust bunnies!'
                    print("Nanny nods sagely. 'Of course you aren't, brave child. Just remember, you have to")
                    print("laugh loud to scare away a spirit,' she remarks with a wink.")
                    print("'Let's go get you cleaned up, you're all covered in soot.'")
                    print("'Nanny, will I be able to meet the other spirits near our house?' asks {}.".format(username))
                    print("'Hmm,' Nanny muses, leading our dusty protagonist towards the well.")
                    print("'I think you just might.'")
                    print("/n")
                    print("THE END")
                    print("/n")
                    print("Thank you for playing through this interactive fiction.")
                    #end
                elif choice4 == 2: #'S- sprites? Is our house haunted?'
                    print("'No need to be frightened, my young friend. Just remember, if you laugh loud, the")
                    print("spirit will be scared away. And as for haunted, well - ' Nanny looks out past the trees.")
                    print("'That you are able to see them makes me very glad.'")
                    print("'O-okay,' responds {}. 'Then I won't be scared of them anymore. And I want to ".format(username))
                    print("tell Daddy all about the spirits!'")
                    print("'What a wonderful idea, {}!' remarks Nanny. 'Let's go tell him right now.'".format(username))
                    print("/n")
                    print("THE END")
                    print("/n")
                    print("Thank you for playing through this interactive fiction.")
                    #end
                else:
                    print(invalid_command)
            else:
                print(invalid_command)
            
        elif choice2 == 3: #Call for Nanny. What are these things?
            print("{} calls out, 'Nanny! What are these things that fly around and then disappear up into the ceiling?'".format(username))
            print("Nanny's footsteps creak up the stairs and {} can hear her low chuckle.".format(username))
            print("'Ahhh - it appears the soot sprites are hard at work.'")
            print("{} says, 'Soot sprites? Like dust bunnies in my sister's picture book?".format(username))
            print("As Nanny appears in the attic doorway, she explains:")
            print("'Yes, that's right. They breed in very old, empty houses, building invisible nests,")
            print("and turning everything into dust. I could see them too, when I was a very small child.'")
            print("'There's nothing to be frightened of. If we all keep smiling,")
            print("the sprites may gradually go away and leave this place alone.")
            print("/n")
            print("How would {} like to answer?".format(username))
            print("(1) 'I'm not afraid of dust bunnies!'")
            print("(2) 'S- sprites? Is our house haunted?'")
            choice3 = int(input(username + " chooses: "))
            print("\n")

            if choice3 == 1: #'I'm not afraid of dust bunnies!'
                print("Nanny nods sagely. 'Of course you aren't, brave child. Just remember, you have to")
                print("laugh loud to scare away a spirit,' she remarks with a wink.")
                print("'Let's go get you cleaned up, you're all covered in soot.'")
                print("'Nanny, will I be able to meet the other spirits near our house?' asks {}.".format(username))
                print("'Hmm,' Nanny muses, leading our dusty protagonist towards the well.")
                print("'I think you just might.'")
                print("/n")
                print("THE END")
                print("/n")
                print("Thank you for playing through this interactive fiction.")
                #end
            elif choice3 == 2: #'S- sprites? Is our house haunted?'
                print("'No need to be frightened, my young friend. Just remember, if you laugh loud, the")
                print("spirit will be scared away. And as for haunted, well - ' Nanny looks out past the trees.")
                print("'That you are able to see them makes me very glad.'")
                print("'O-okay,' responds {}. 'Then I won't be scared of them anymore. And I want to ".format(username))
                print("tell Daddy all about the spirits!'")
                print("'What a wonderful idea, {}!' remarks Nanny. 'Let's go tell him right now.'".format(username))
                print("/n")
                print("THE END")
                print("/n")
                print("Thank you for playing through this interactive fiction.")
                #end
            else:
                print(invalid_command)

        else:
            print(invalid_command)
    elif choice1 == 2: #(2) 'No! I'm going exploring!'
        #go into the garden
        #there is a pair of white ears sticking up in the grass
        #follow it / do cartwheels
        print("'My, my, what an obstinate child!' laughs Nanny.")
        print("'But it's good for children to explore. Have fun, and don't go too far.'")
        print("{} strides deliberately into the garden, looking for acorns.".format(username))
        print("Look, there's one. And here's another one, just a step or two away.")
        print("{} looks up and sees pointed white ears disappearing into the grass just ahead.".format(username))
        print("\n")
        print("What would {} like to do?".format(username))
        print("(1) Run after the ears, leaving behind the acorns.")
        print("(2) Ignore the ears. They probably belong to a local spirit who might be mischievous.")
        choice2 = int(input(username + " chooses: "))
        print("\n")

        if choice2 == 1: #Run after the ears, leaving behind the acorns.
            print("The ears belong to a small furry white creature carrying a sack of acorns.")
            print("The creature notices you and starts to run!")
            print("{} chases it at top speed! It zigs and zags all across the yard.".format(username))
            print("Just as {} is about to catch it, the furry animal disappears into a tunnel in the hedge.".format(username))
            print("\n")
            print("What would {} like to do?".format(username))
            print("(1) Follow it into the tunnel! I've come this far!")
            print("(2) It's dirty and cramped in there. But what a great story for Dad!")
            choice3 = int(input(username + " chooses: "))
            print("\n")

            if choice3 == 1: #Follow it into the tunnel! I've come this far!
                print("")

            elif choice3 == 2: #It's dirty and cramped in there. But what a great story for Dad!
                print("")

            else:
                print(invalid_command)
        
        elif choice2 == 2: #Ignore the ears. They probably belong to a local spirit who might be mischievous.
            print("{} goes back to collecting acorns. Big sister will be very impressed.".format(username))
            print("Here at the end of the garden there's a large hedge.")
            print("Let's see if there are any acorns around the bushes.")
            print("No more acorns here, but there's a hole in the bushes. I wonder where it goes?")
            print("\n")
            print("What would {} like to do?".format(username))
            print("(1) Let's go in. I'm just the right size for this tunnel!")
            print("(2) I don't want to say it, but it's a little scary to go in there by myself.")
            choice3 = int(input(username + " chooses: "))
            print("\n")

            if choice3 == 1: #Let's go in. I'm just the right size for this tunnel!
                print()
            
            elif choice3 == 2: #I don't want to say it, but it's a little scary to go in there by myself.
                print("Admitting that they were a little frightened, {} decided to wait until their big sister".format(username))
                print("would be home from school. ")
            
            else:
                print(invalid_command)
        else:
            print(invalid_command)
    else:
        print(invalid_command)

