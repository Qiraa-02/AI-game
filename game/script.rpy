define j_nvl = Character("Jaka", kind=nvl, image="nighten", callback=Phone_SendSound)
define m_nvl = Character("Mafuyu", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)
define G = Character("Girl")
define J = Character("Jaka")
define M = Character("Mafuyu")
default Mafuyu_affection_score = 10

label start:
show kantin
play music "ost.ogg" fadein 2.5
centered "..."
scene hitam with dissolve
centered "The cafeteria's bustle fades\ninto scattered clatters and footsteps."
centered "Jaka weaves through crowded tables,\ntray in hand, eyes scanning like radar."
centered "One open seat. She's already there."
centered "Sitting perfectly still."
centered "Black hair tucked behind one ear."
centered "Earbuds sealing her world, a near-empty iced latte beside her."
centered "She doesn't notice him approach."
with fade
scene kantin
J "Hey.... uh, mind if I sit here?"
show mafuyu_n with dissolve
G "(glancing up)\n...Go ahead."
show dim_overlay onlayer master
with fade
centered "{color=#f0f5f2}{b}Her tone isn't cold, nor warm.{/color}{/b}"
centered "{color=#f0f5f2}{b}Neutral, distant. Yet something soft lingers beneath,\nlike a whisper behind a curtain.{/color}{/b}"
centered "{color=#f0f5f2}{b}He sits beside her.{/color}{/b}"
hide dim_overlay
with fade
hide mafuyu_n
J "Thanks."
J '''({i}Quiet, huh? Her eyes still glued to her screen{/i}.)'''
J '''({i}Guess conversation's over before it began{/i}.)'''
scene hitam with fade
centered "They eat in silence."
centered "Jaka tries focusing on his meal,\nbut his attention keeps drifting."
centered "She isn't doing anything."
centered "Not scrolling, not texting."
centered "Just gazing at her dark screen."
centered "Her fingers cradle the cup like it's something fragile."
centered "Finally, Jaka clears his throat."
with fade
scene kantin with dissolve
J "({i}Hmm... What should I do?{/i})"
menu:
    "Greet her.":
        jump choice_1A
        $Mafuyu_affection_score += 1

    "Tease her.":
        jump choice_1B   
        $Mafuyu_affection_score -= 1

label choice_1A:
    J "I'm Jaka. Just trying to avoid social death today."
    show mafuyu_h with dissolve
    M "...Mafuyu."
    J "Mafuyu... Beautiful name."
    show dim_overlay onlayer master
    centered "{color=#f0f5f2}{b}He says it without thinking. The name hangs in the air for a moment.{/color}{/b}"
    hide dime_overlay
    M "({i}It's just an ordinary name{/i})"
    show dim_overlay onlayer master with fade
    centered "{color=#f0f5f2}{b}She returns to her cup.{/color}{/b}"
    centered "{color=#f0f5f2}{b}But something shifts in her expression,\nlike a petal unfurling slowly.{/color}{/b}"
    centered "{color=#f0f5f2}{b}Five minutes pass. She finishes her coffee.\nLifts the cup gently, as if it's the last warm thing on earth.{/color}{/b}"
    centered "{color=#f0f5f2}{b}She starts to rise, then...{/color}{/b}"
    hide dime_overlay with fade
    J "Wait... Sorry, your name again?"
    M "(half-turning)\nMafuyu."
    show dim_overlay onlayer master with fade
    centered "{color=#f0f5f2}{b}The name echoes again,\nfeeling different this time.{/color}{/b}"
    hide dime_overlay with fade
    jump continue_1

label choice_1B:
    J "If this turns into awkward silence, I'm blaming you."
    show mafuyu_s with dissolve
    M "....Okay."
    show dim_overlay onlayer master with fade
    with fade
    centered "{color=#f0f5f2}{b}Silence deepens like a stone dropped in water.{/color}{/b}"
    centered "{color=#f0f5f2}{b}Five minutes pass. She finishes her coffee.\nLifts the cup gently, as if it's the last warm thing on earth.{/color}{/b}"
    centered "{color=#f0f5f2}{b}She starts to rise, then...{/color}{/b}"
    hide dime_overlay with fade
    J "Wait... Sorry. May I ask your name?"
    M "(half-turning)\nMafuyu."
    show dim_overlay onlayer master with fade
    centered "{color=#f0f5f2}{b}The name,\nfeels like a key turning in an old lock.{/color}{/b}"
    hide dime_overlay with fade
    jump continue_1

label continue_1:
    J "({i}Mafuyu... Where have I...\nNo, it can't be.{/i})"
    J "({i}Just a coincidence.{/i})"
    J "({i}Just a similar voice.{/i})"
menu:
    J "({i}But my heart says it's not a coincidence{/i})" 

    "Your name... echoes in my memories.":
        jump choices_2A
        $Mafuyu_affection_score += 1

    "You've got this strong 'main character' aura.":
        jump choices_2B
        $Mafuyu_affection_score -= 1

label choices_2A:
    J "Your name... echoes in my memories."
    show mafuyu_h with dissolve
    M "...People tell me that often."
    J "({i}DO THEY?{/i})"
    show dim_overlay onlayer master with fade
    centered "{color=#f0f5f2}{b}She leaves. No wave, no goodbye.{/color}{/b}"
    centered "{color=#f0f5f2}{b}Just her name{/color}{/b}"
    centered "{color=#f0f5f2}{b}and the soft echo of something left behind.{/color}{/b}"
    hide dime_overlay with fade
    hide mafuyu_h with dissolve
    jump continue_scene_2

label choices_2B:
    J "You've got this strong 'main character' aura."
    show mafuyu_s with dissolve
    M "...I doubt that's a compliment."
    show dim_overlay onlayer master with fade
    centered "{color=#f0f5f2}{b}She leaves. No wave, no goodbye.{/color}{/b}"
    centered "{color=#f0f5f2}{b}Just her name{/color}{/b}"
    centered "{color=#f0f5f2}{b}and the soft echo of something left behind.{/color}{/b}"
    hide dime_overlay with fade
    hide mafuyu_s with dissolve
    jump continue_scene_2

label continue_scene_2:
    scene kamar_s with fade
    centered "..."
    scene black with dissolve
    centered "Evening falls. Jaka lies in bed,\nscrolling Instagram. His eyes glaze over mundane posts."
    centered "Then, a story catches his eye."
    centered "Muted tones. Pale lighting."
    centered "Mafuyu, standing before a gray-tiled building\nhe knows like his own palm."
    centered "{i}His faculty building.{/i}"
    scene kamar_s with dissolve
    J "{i}That's... my building.\nSame spot. Same star-patterned railing.{/i}"
    centered "{color=#f0f5f2}{b}Pieces click. Her name.\nHow she said it. A profile he hadn't recalled in two years.{/color}{/b}"
    centered "{color=#f0f5f2}{b}{i}She's here.{/i}{/color}{/b}"
menu:
    J "{i}What should I do?{/i}"

    "DM her on IG":
        $Mafuyu_affection_score += 1
        jump Choice_3A
    "Stay silent":
        $Mafuyu_affection_score -= 1
        jump Choice_3B
    "Unfollow":
        $Mafuyu_affection_score -= 2
        jump Scene_2_Fatal

label Choice_3A:
    nvl_narrator "Messages and calss are end-to-end encrypted. only people in this chat can read, listen to, or share them. \n Learn more."
    j_nvl "Hey... Random question. Do you go to Kairoku Uni?"
    m_nvl "Yeah."
    m_nvl "Why?"
    j_nvl "I think we shared a table earlier."
    j_nvl "Cafeteria, long black hair, coffee,\nnot much talking."
    m_nvl "...That was you?\nDidn't recognize you."
    j_nvl "Been a while, huh?"
    m_nvl "...Jaka.\nI remember that name."
    j_nvl "Really? Thought you'd forgotten me."
    m_nvl "I don't forget easily.\nYou were annoying, but consistent."
    j_nvl "Hahaha. Classic me."
    m_nvl "...But I didn't dislike it."
    m_nvl "Back then, I mean."
    m_nvl "Today wasn't bad either."
    centered "{color=#f0f5f2}{b}Her typing bubble vanishes.\nNothing more follows.{/color}{/b}"
    centered "{color=#f0f5f2}{b}But something has shifted.{/color}{/b}"
    jump continue_scene_3

label Choice_3B:
    centered "He hesitates. Then, without overthinking,\nfingers tap her story and hit 'Reply'."
    nvl_narrator "Messages and calss are end-to-end encrypted. only people in this chat can read, listen to, or share them. \n Learn more."
    j_nvl "That building looks familiar. Arts faculty?"
    m_nvl "Yeah."
    m_nvl "You too?"
    j_nvl "Yeah, think I saw you earlier.\nWe shared a table."
    m_nvl "Hmm. Didn't notice."
    m_nvl "I usually don't."
    m_nvl "Well, fair. Lots of faces around lately."
    centered "A pause. No warmth.\nBut no rejection either."
    m_nvl "Guess we'll see each other again." 
    m_nvl "Maybe."
    j_nvl "{i}She's distant. But she replied.\nMaybe there's still something underneath.{/i}"
    jump continue_scene_3

label Scene_2_Fatal:
    centered "{color=#f0f5f2}{b}He stares at the photo a moment longer.{/color}{/b}"
    centered "{color=#f0f5f2}{b}Then opens her profile. Taps 'Unfollow.' No hesitation.{/color}{/b}"
    centered "{color=#f0f5f2}{b}She vanishes from his feed.{/color}{/b}"
    J "Too weird. Too late. Just let it fade."
    stop music fadeout 2.5
    play music "bad.ogg" fadein 2.5
    centered "{color=#f0f5f2}{b}No reply.\nNo connection.\nSome silences are self-made.{/color}{/b}"
    centered "{color=#f0f5f2}{b}She wasn't sure if it was truly you. But part of her hoped.\nThat soft voice in the cafeteria. The glance. The name.\nIt tugged at something she hadn't let herself feel for years.\nBut she said nothing either. Because she was waiting. For you.{/color}{/b}"
    centered "{color=#f0f5f2}{b}And perhaps that's the cruelest part... she waited.\nNot forever. But long enough.{/color}{/b}"
    centered "{color=#f0f5f2}{b}Long enough to tell herself:\nIf he remembers... he'll reach out.\nYou didn't.\nYou could've asked: 'Hey, remember me?'\nYou could've said anything. Instead—you chose Unfollow.{/color}{/b}"
    centered "{color=#f0f5f2}{b}You thought it harmless.\nJust a tap, you said.\nJust a cleaner feed. No more awkward memories.\nBut deep down, you knew.\nYou didn't delete her photo. You deleted possibility.{/color}{/b}"
    centered "{color=#f0f5f2}{b}How many have you done this to?\nThe friend ghosted because 'life got busy.'\nThe one who typed a message then deleted it, waiting for you to speak first.\nThe one you never replied to.\nYou don't even recall their names now, do you?{/color}{/b}"
    centered "{color=#f0f5f2}{b}But they remember yours.\nAnd so does she.{/color}{/b}"
    centered "{color=#f0f5f2}{b}You won't see her on campus again.\nShe'll walk past you once without noticing,\nand that will be the end.\nNo second cafeteria lunch. No exchanged messages. No shared silence that feels safe.{/color}{/b}"
    centered "{color=#f0f5f2}{b}You threw it away.\nYOU. THREW. IT. AWAY.{/color}{/b}"
    centered "{color=#f0f5f2}{b}And it's your fault.\nYour fault.\nYour fault.\nYour fault.\nYour fault.\nYour fault.\nYour fault.{/color}{/b}"
    pause
return

label continue_scene_3:
    scene kamar_m with fade
    centered "{color=#f0f5f2}{b}Jaka sits at his desk now.\nPhone buzzing with trivial notifications.{/color}{/b}"
    centered "{color=#f0f5f2}{b}Except one. A friend request.\nOn Discord from: Asahina#xxxx{/color}{/b}"
    centered "{color=#f0f5f2}{b}His heart stutters. That name.\nHe accepts before reason catches up.{/color}{/b}"
    m_nvl "Hey"
    j_nvl "Whoa, fast. Didn't expect you'd add me."
    m_nvl "You were in my list, just never removed."
    j_nvl "So all this time...?"
    m_nvl "Saw your status updates sometimes,\nfigured you were alive lol."
    j_nvl "You vanished back then. Poof."
    m_nvl "I know\nSorry."
    j_nvl "Don't be."
    j_nvl "Life got hectic?"
    m_nvl "Everything felt too loud. Needed silence for a while."
    centered "{color=#f0f5f2}{b}Jaka doesn't push. Weight lies beneath her words,{/color}{/b}"
    centered "{color=#f0f5f2}{b}but she isn't ready to unpack it.{/color}{/b}"
    centered "{color=#f0f5f2}{b}He knows that tone. Has typed it himself.{/color}{/b}"
    j_nvl "Thought about messaging you sometimes but wasn't sure you'd reply."
    m_nvl "I wouldn't have. Back then."
    m_nvl "But... I remembered"
    j_nvl "Remembered what?"
    m_nvl "Everything. You were annoying but easy to talk to."
    centered "{color=#f0f5f2}{b}He rereads it. Easy to talk to.\nOrdinary words, but from her, they mean everything.{/color}{/b}"
    j_nvl "Today felt strange sitting beside you... Didn't know it was you,\nbut it felt... like coming home."
    m_nvl "Didn't feel heavy to me either."
    j_nvl "Missed whatever it was we had."
    centered "{color=#f0f5f2}{b}Another pause\nNo typing bubble.{/color}{/b}"
    centered "{color=#f0f5f2}{b}Then...{/color}{/b}"
    m_nvl "You were my first real friend even if we never met in person till today"
    j_nvl "Still counts."
menu:
    j_nvl "Do I want to meet again?"

    "Would you... want to meet up?":
        $Mafuyu_affection_score += 3
        j_nvl "Would you want to meet again?\nActually talk face to face?"

    "We can just talk like this":
        $Mafuyu_affection_score -= 3
        j_nvl "No pressure, we can just chat here if that's easier."

label ending_evaluation:
if Mafuyu_affection_score > 10:
    jump good_ending
else:
    jump bad_ending

label good_ending:
    m_nvl "......"
    m_nvl "Maybe. If it's not weird."
    j_nvl "It's already weird. Let's lean in."
    m_nvl "Heh. Okay. Lunch again maybe?"
    j_nvl "It's a date... sorta."
    m_nvl "Don't push it."
    centered "{color=#f0f5f2}{b}The weight between them lifts slightly.\nNo grand promises.\nNo drama.\nJust two people trying again.{/color}{/b}"
    centered "{color=#f0f5f2}{b}This is the Beautiful Ending.\nCongratulations.{/color}{/b}"
    centered "{color=#f0f5f2}{b}You didn't just find your way back to her.\nYou found your way back to a lost part of yourself.\nHer smile is the morning sun after a night's rain.\nAnd you know—this is only the beginning.{/color}{/b}"
    stop music fadeout 2.5
    play music "good.ogg" fadein 2.5
    scene good_ending with dissolve
    pause
    return

label bad_ending:
    m_nvl "Yeah... maybe for now."
    centered "{color=#f0f5f2}{b}She doesn't refuse.\nNor does she accept.\nThe thread holds.\nFragile but unbroken.{/color}{/b}"
    centered "{color=#f0f5f2}{b}Bitter ending? Or not?{/color}{/b}"
    centered "{color=#f0f5f2}{b}She didn't open up.\nBut she didn't shut you out.{/color}{/b}"
    centered "{color=#f0f5f2}{b}You said what you could.\nMaybe that was enough for now.{/color}{/b}"
    centered "{color=#f0f5f2}{b}You're not strangers. But not quite\nanything more yet.{/color}{/b}"
    centered "{color=#f0f5f2}{b}You don't drift apart. But don't move forward.\nYou didn't lose her. But didn't truly reach her.{/color}{/b}"
    centered "{color=#f0f5f2}{b}The thread didn't snap. Just stretched thinner,\nquieter.{/color}{/b}"
    centered "{color=#f0f5f2}{b}You won't find her waiting.\nBut you might still find her... later.{/color}{/b}"
    centered "{color=#f0f5f2}{b}If the moment remembers.{/color}{/b}"
    centered "{color=#f0f5f2}{b}If you remember too.{/color}{/b}"
    centered "{color=#f0f5f2}{b}And if neither lets go too soon.{/color}{/b}"
    centered "{color=#f0f5f2}{b}This is the Bitter Ending.\nTry Again?{/color}{/b}"
    stop music fadeout 2.5
    play music "bad.ogg" fadein 2.5
    scene bad_ending with dissolve
    pause
    return