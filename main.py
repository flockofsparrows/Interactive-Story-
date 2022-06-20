# Title
print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
print("! The Enchanted Library !")
print("!  * Fictional Story *  !")
print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
print()
# Premise of Story
print("       Edmund was only ten. He wasn't much of a rule follower and thought it rather enjoyable to do the exact opposite of what he had been strictly told to do or not do. All that came to an end, you see, after a very meaningful encountor in his Great Uncle's mysterious and ancient house nesttled in the frosty Ore Mountains, a very remote area of Germany. It changed him forever.")
print()
print("       By the end of the third day, with no other kids to play with and tiresome old trinkets the old man thought would amuse him, he decided that if his great uncle didn't understand the first thing about what kids liked then his rules were probably silly and ought to be broken.")
print()
print("       You decide to ignore your Great Uncle, Kristoff's one house rule, albeit given in the gravest voice, that at all costs one cannot and must not enter the library. Strictly forbidden, especially for kids, it's not all make believe you see, he said.")
print()
print("       Having gently toggled the house keys off your uncle's belt while he slept in his reading chair, you find yourself unlocking the only locked door which must be the library. You can hardly believe your eyes! Rows and rows of books displayed in the most delightful manner from floor to ceiling, all the stories a bored human would only dream of.")
print()
# choice of three stories to play:
print("Three beaughtiful books stand out to you.")
print("   A.) Princess and the Pea")
print("   B.) Rumpelstiltskin")
print("   C.) Hansel and Gretel")
Story = input("Which book will you pick up to read. Please select 'a' through 'c': ")
print()
print("         ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
print()
# Story Option A: 
if(Story =="A" or Story =="a"):
  print("~ ~ STORY OPTION A: ")
  print("       You barely crack the book open, when you feel a rush of wind swirl about you, forcing you to close your eyes. Upon opening them you are addressed by a very angry Queen, pressing three peas into your hand, as she quickly rattled off instructions about mattresses and how important it was that you got the number right for the guest who claims she is a princess. Something about twenty of this and twenty of that and the peas under it all, but that sounds like overkill to you so it slips from your mind. It is your job to help prepare the test correctly or else the Queen will not be able to determine if the visiting lady is a real princess and she will punish you with a curse: never being able to sleep comfortably again.")
  print()
  # Multiple Choice & prompt user to make a selection
  print("How many mattresses did the queen say to use?")
  print("A.) Ten Mattresses")
  print("B.) Twenty Mattresses")
  print("C.) Forty Mattressess")
  Answer = input("Please pick 'a' through 'c': ")
  print()
  # Determine if asnwer is correct and display in story form
  if(Answer == "C" or Answer =="c"):
    print("** Success! Your memory lead to a succesful test proving the lady a real princess which made the Queen quite happy as she had found a suitable bride for her son. Once completed a rush of wind flew about you again and back in your great uncle's house you found yourself. Upon going to bed that night, you found three little peas under your mattress and after removing them, you had the best night of sleep in all ten years of your life.")
    print()
    print("             ~ END OF STORY ~")
  # Determine if asnwer is incorrect and display in story form  
  elif(Answer != "C" or Answer != "c"):
   print("** Fail! The Queen was angry and her son did not marry as the test was proven faulty for assessing the princess. The book shot you out of it's pages with a spiteful spit landing you on your behind with a thud. Later that night, and in fact for months afterward, you seemed to have the worst luck in getting a decent night of sleep.")
   print() 
   print("             ~ END OF STORY ~") 
# Story Option B:
if(Story == "B" or Story =="b"):
  print("~ ~ STORY OPTION B: ")
  print("       It went dark and immediately your ears picked up a cackling laugh that sent waves of disgust through your body. Trying to stay calm you waited for your eyes to adjust. It was a dark stone room with a tiny cut in the wall as a sad excuse for a window. The moonlight spilled in, draping itself on mounds and mounds of what looked lik hay covering the entire floor and right in the middle appeared to be another old boring relic from your great uncle's house, but as the seconds passed, you realized it was a spinning wheel.")
  print()
  print("       You sat down at the stool not sure what you were suppose to do, when a guard came to the locked door and with loud banging yelled, 'one hour till sunup, and if all that hay is not spun into gold the king will have your head.' Without hesitation you began to push the dry stalks of hay into the contraption but to no avail. No gold. After some time, there was movement from where the creepy laugh came from earlier, and out of the corner of the room a small imp like creature came forward with a big smile.")
  print()
  print("      'I see you don't want my help again? Haven't I proven to you that you can trust me? The past two nights I've succesfully turned hay into gold, saving you from the kings wrath, are you sure you want to do this without my help?' A great feeling of uneasiness came over you, but with no other option, you said ok, what do I do? 'Nothing' was the reply, 'only payment of which I will choose.'")
  print()
  print("       As the little devil stood watching you think it over, you noticed he had two of your own valuables on his person and was wondering how he got in posession of those, when he interrupted your thoughts, 'however becuase my work before me is much greater than the previous two nights, I require a much bigger payment...the rest of your childhood. Once the transaction is done, you will wake up as an adult, skipping all the years in between.' You disliked this little creature very much and said with great disdain, 'that's not a fair bargain, I won't do it!'")
  print()
  print("      'Fine. If you can guess my name by correctly solving this riddle, you won't have to pay me for turning this hay into gold, otherwise...'You agreed and in no time flat the whole room was full of strands of gold thread instead of dry stalks of hay. Turning to you he gave you the riddle.")
  print()
# Set up instructions riddle & math equation
  print("~ ~ Solve correctly the math equation to get the answer to this riddle. 'WHAT BELONGS TO YOU, BUT YOUR FRIENDS USE IT MORE.'Best of luck, your childhood depends on it!")
  print()
# Set up user input & convert answer to integar
  print("y = 8")
  print("x = 4")
  print()
  Riddle = input("What is y + y % x: ")
  Riddle = int(Riddle)
  print()
# Determine if answer to riddle is correct & print story
  if(Riddle == 4):
    print("** Success! You solved the riddle correctly which means you guessed the little imp's name - Rumplestiltskin! You are relieved to have not given up the rest of your childhood, since you dread most adults and think they are dull and boring. The creature could hardly believe you had solved it, he screamed and jumped out the window never to be seen again in all the land. Meanwhile the world went blinding light and you found yourself back in your uncle's library, so glad to be set free. The pockets of your clothing felt quite heavy but finding the contents to be bunches of gold strands, you yelled for joy!")
    print()
    print("              ~ END OF STORY ~ ")
# Set up result if answer above is incorrect and print story
  else:
    print("** Failed! The horrid creature pranced around you, singing, 'Your youth is mine, you have to pay the fine, all nine times for no one can guess my name it is too fine, Rumpelstiltskin is my sign.' With shock and panic you started to plead, but it was too late...sadly you lost the bargain. With a bright light you were back in the magical library but as you walked out you hit your head on the doorframe. You dind't remember being this tall. As your mind started to race you ran down the hall calling Kristoff's name asking what year it was. To your utter horror it was ten years later and you were no longer ten but twenty. You gave up the rest of your childhood all because you had no respect for rules or boundaries meant to keep you safe. It was a very, very hard way to learn a lesson.")
    print()
    print("              ~ END OF STORY ~ ")
# Story Option C: 
if(Story =="C" or Story =="c"):
  print("~ ~ STORY OPTION C: ")
  print("       Upon opening the book you are transported into another world. Warm spring air tingles your skin and rustling leaves of the black forest fill your ears, but it is quickly interruppted when your siser, Gretel is staring at you with an annoyed look while she says for a second time, 'Well what do you think! How much bread should we take with us on our forbidden trip into the woods?")
  print()
  print("       Gretel picked a route that cuts through a mushroom patch, a cluster of beehives and ultimatley leads to an apple orchard. You will retrace your steps to get back home safely. She gestures to the map you are holding, there is a key showing each mile requires one whole loaf of bread to safely retrace your steps. Each whole loaf has twelve pieces of bread. It is 1.5 miles from home to the apple orchard. *Feeling lazy you realize if you pick a large number, it will be more than enough bread to get back home safely, but the consequances may be different if you don't put the work in to find the exact amount needed.")
  print()
  # Prompt reader to enter their free response answer
  Answer = input("~ ~ Please enter how many SLICES of bread you should bring with you: ")
  print()
  # Convert answer to integer
  Answer = int(Answer)
  # Determine if answer is correct and display in story form
  if(Answer == 18):
    print("** Success! You brought the exact amount of bread needed to safely find your way back home which meant you had enough space to carry honey, mushrooms and apples to enjoy with your family. After having a nice dinner with Gretel and your storybook mother, you burped and the roomed began to spin until it became quiet yet again and you found yourself back in your uncle's library. Digging into your pockets you took out an apple turnover pastry sweetene with honey. With a smile, you ran out of the library to a world you better understood. ~ END OF STORY ~")
  # Determine if answer is second best option and display in story form
  elif(Answer > 18):
      print("** Partial Success! You made it back home safely, BUT with all the bread you were still holding you couldn't bring back as much apples, honey or mushrooms that you wanted. You tripped over a root and landed on your hands and knees on the hardwood floor of your uncle's library. Hmm, you thought, I guess that wasn't so bad, but you soon realized with shock and dismay that every time you asked for or served yourself honey or apples (you hated mushrooms) it was always half eaten. Thankfully this lasted only a few weeks.")
      print()
      print("             ~ END OF STORY ~ ")
  # Determine if answer is incorrect and display in story form  
  else:
      print("** Fail! You miscalculated and ran out of bread crumbs, thus getting lost and ending up in the witches cottage getting fattened up for a future meal..! Clencthing your eyes shut and feeling the heat of the oven get hotter and hotter, you wished you had never disobeyed your uncles rules. A moment later, you suddenly felt the air go cool around you. Slowly prying one eye open then the next, you saw with great relief that you were once again back in your uncle's library. You, couldn't help the sensation that there was a smokey air following you wherever you went and not untill later, when you went to the washroom to freshen up, your reflection in the mirror shocked you! Singed hair that was still smoking and really really fat cheeks, not to mention a full stomach. In fact you felt so full, you fasted for a whole week, sadly missing out on your uncle's birthday cake.")
      print()
      print("             ~ END OF STORY ~")
