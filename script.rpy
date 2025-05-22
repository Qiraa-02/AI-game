 # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define G = Character("Girl", color="FFC0CB")
define J = Character("Jaka")
define M = Character("Mafuyu", color="FFC0CB")
default Mafuyu_affection_score = 0


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    with dissolve
    centered "It's past lunch peak. The buzz of conversation fades into scattered clatter and footsteps."
    centered "Jaka walks through the crowded cafeteria,\n tray in hand, his eyes scanning tables like radar."
    centered "One open seat. She's already there."
    centered "Sitting perfectly still."
    centered "Black hair tucked behind one ear."
    centered "Earbuds in, a mostly-finished iced latte on the tray."
    centered "She doesn't seem to notice him approach."
    with fade
    J "Hey....uh, is this seat taken?"
    G "(glancing up)...No. You can sit."
    with fade
    centered "Her tone isn't cold, not warm either."
    centered "Neutral, and distant. But, there's something soft beneath it,\n like a sound just under the surface."
    centered "He sits down beside her."
    with fade
    J "Thanks."
    J '''({i}Cool, She doesn't respond, and she still looking at her phone{/i}.)'''
    J '''({i}Welp, guess that's the end of this conversation{/i}.)'''
    with fade
    centered "They eat in silence."
    centered "Jaka tries to focus on his food,\n but his attention keeps drifting."
    centered "She's not doing much."
    centered "No scrolling, not texting."
    centered "Just staring at her screen."
    centered "Her fingers rest on the cup like it's something fragile."
    centered "Eventually, He cleans his throat."
    with fade
menu:
    J "({i}Hmm... What should I say?{/i})"

    "Greet Her.":
        jump choice_1A
        $Mafuyu_affection_score += 10

    "Blame Her.":
        jump choice_1B   
        $Mafuyu_affection_score -= 10

label choice_1A:
    J "I'm Jaka by the way. Just trying to avoid social death today."
    G "...Mafuyu."
    J "Cool, Mafuyu. Sound familiar."
    centered "He says it without thinking. The name sits heavy for a moment."
    M "({i}It's a common name anyways.{/i})"
    with fade
    centered "She goes back to her cup."
    centered "But something about her expression shifts\n just a little."
    centered "Five minute pass. She finishes her coffee. \nPicks it up gently like it's the last warm thing in the world."
    centered "She begin to stand, and then....."
    with fade
    J "Hey... wait. Sorry, what was your name again?"
    M "(turning slightly)\n Mafuyu."
    centered "That name again,\n it feels different this time."

    jump continue_1

label choice_1B:
    J "If this encounter turns into awkward silence, I'm blaming you."
    G "....Okay."
    with fade
    centered "The silence deepens like a dropped stone."
    centered "Five minute pass. She finishes her coffee. \nPicks it up gently like it's the last warm thing in the world."
    centered "She begin to stand, and then....."
    with fade
    J "Hey... wait. Sorry. Can I ask what's your name please?"
    G "(turning slightly)\n Mafuyu."
    centered "That name,\n it feels different this time."

    jump continue_1

label continue_1:
    J "({i}Mafuyu... Where have I....\n No, it couldn't be.{/i})"
    J "({i}Just a name.{/i})"
    J "({i}Just a voice.{/i})"
menu:
    J "({i}That name really ring a bell in my head.{/i})" 

    "Your name feels... Familiar, somehow.":
        jump choices_2A
        $Mafuyu_affection_score += 10

    "You've got a real 'main character' aura. Just saying.":
        jump choices_2B
        $Mafuyu_affection_score -= 10

label choices_2A:
    J "Your name feels... Familiar, somehow."
    M "...People say that a lot."
    J "({i}DO THEY?{/i})"
    with fade
    centered "She leaves. No wave, no goodbye."
    centered "Just her name"
    centered "and the soft echo of something left behind."
return

label choices_2B:
    J "You've got a real 'main character' aura. Just saying."
    M "...I don't think that's a good thing."
    with fade
    centered "She leaves. No wave, no goodbye."
    centered "Just her name"
    centered "and the soft echo of something left behind."
return
# This ends the game.