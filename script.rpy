﻿## this is the main script file; everything starts here
## the goal is to offload as much declaring to the init module and jump
## back here for main control

## Declare characters used by this game.
#TO DO

    ##disable the main menu for easy iteration
label splashscreen:
    $BM = Battle()

    scene black
    pause 0.5
    show logo 1 with dissolve
    $ renpy.pause(2)
    show logo 2 with dissolve
    $ renpy.pause(2)
    hide logo with dissolve
    $ renpy.pause(0.5)

    stop music fadeout 1.0
    return

label quit:
    $ renpy.quit(relaunch=False)
    return


# The game starts here.
label start:

#####################################VARIABLE SET UP

    call initialize

    call firstvariables

#####################################VARIABLE SET UP

    #temporary
    #jump test_battle


    stop music fadeout 3.0
    play sound "Sound/buttonclick.wav"
    scene bg cera:
        pause 5.0
    with Dissolve(2)

    window hide

    play music "Music/Tides.ogg" loop
    $ renpy.pause (0.5)
    show introtext0:
        yalign 0.12
        xalign 0.5
    pause
    hide introtext0 with Dissolve(1)
    show intro1:
        yalign 0.12
        xalign 0.5
        alpha 0.0
        linear 1.0 alpha 1.0
    pause
    hide intro1 with Dissolve(1)
    show intro2:
        yalign 0.12
        xalign 0.5
        alpha 0.0
        linear 1.0 alpha 1.0
    pause
    hide intro2 with Dissolve(1)
    show intro3:
        yalign 0.12
        xalign 0.5
        alpha 0.0
        linear 1.0 alpha 1.0
    pause
    hide intro3 with Dissolve(1)
    show intro4:
        yalign 0.12
        xalign 0.5
        alpha 0.0
        linear 1.0 alpha 1.0
    pause
    hide intro4 with Dissolve(1)
    show intro5:
        yalign 0.12
        xalign 0.5
        alpha 0.0
        linear 1.0 alpha 1.0
    pause
    hide intro5 with Dissolve(1)

    show introtext1:
        parallel:
            xalign 0.35 yalign 0.4
            easein 6.0 xalign 0.5
        parallel:
            alpha 0.0
            linear 2.5 alpha 1.0
    $ renpy.pause (2.0)
    show introtext2:
        parallel:
            xalign 0.65 yalign 0.5
            easein 6.0 xalign 0.5
        parallel:
            alpha 0.0
            linear 2.5 alpha 1.0
    $ renpy.pause (2.0)
    show introtext3:
        parallel:
            xalign 0.35 yalign 0.6
            easein 6.0 xalign 0.5
        parallel:
            alpha 0.0
            linear 2.5 alpha 1.0
    $ renpy.pause (8.0)
    hide introtext1 with dissolve
    hide introtext2 with dissolve
    hide introtext3 with dissolve

    $VNmode() #enables rollback

    window show dissolve

    "Shields leaned forward on his seat and spoke to his pilot. The pilot was obscured by his seat and Shields could only hear his burly voice humming to the tinny radio."
    kay "How much further until we get there?"
    pi "Just a moment now. Can't wait until you meet your girl, can you sir?"
    kay "I haven't seen Ava since we were in high school. I doubt she even remembers me."
    pi "The commander? Psh, not her! I mean the Sunrider. The newest ship in the fleet!"
    pi "Here, let me turn the ship around and give you a view."

    scene cg sunrider_drydock:
        xalign 0.0
        linear 20.0 xalign 0.8
    with dissolve

    "Shields leaned against his window and laid his eyes on the Sunrider."
    "Colossal in size, but still sleek looking, Shields found her to his liking. The behemoth vessel stuck a deadly image, like a poised arrowhead at the ready."
    pi "Aye, there, have a look at her. So advanced that the brass needed to train a new line of officers to fly her."
    kay "She looks like a fine vessel."
    pi "Just hang tight, captain. Won't be long now."
    "The shuttle continued its docking approach. Shields sat tight as the shuttle neared the Sunrider and docked."

    scene bg hangar
    with dissolve

    "After exiting the shuttle, Shields walked through the airlock and entered the Sunrider's hangar."

    show ava uniform salute talk with dissolve

    ava "Captain on deck!"

    show ava uniform neutral neutral with dissolve

    ava "Welcome aboard, captain. First Officer Ava Crescentia reporting for duty."

    menu:
        "At ease, commander.":
            jump at_ease

        "It's been awhile, Ava.":
            jump its_been_awhile

label at_ease:
    jump give_report

label its_been_awhile:

    $ affection_ava += 1

    show ava uniform neutral lookleft with dissolve

    ava "Same to you, uh, captain."
    kay "The last time we saw each other was your graduation in high school. I didn't ever dream that I'd ever become your commanding officer."

    show ava uniform neutral neutral with dissolve

    ava "Neither did I."

    menu:
        "I guess things have changed since then.":
            jump things_have_changed

        "It'll be just like old times again.":
            jump old_times

label things_have_changed:
    ava "I agree."
    jump give_report

label old_times:

    $ affection_ava += 1

    kay "Anyways, don't be too awkward around me, alright? I'll be counting on you from now."

    show ava uniform salute neutral with dissolve

    ava "Understood captain."
    kay "I'm not sure you understand..."

    show ava uniform neutral neutral with dissolve

    ava "Understand what?"
    kay "The whole captain thing... It's just bizarre hearing you call me that."
    ava "I do believe that is the correct protocol for a first officer, is it not?"
    kay "Ah, never mind..."
    jump give_report

label give_report:
    kay "Give me a report of Sunrider's status."

    show ava uniform alt neutral neutral with dissolve

    ava "We've been working for the past two weeks testing her systems. She's prepped to go on your word, sir."
    kay "Good. It sounds like High Command wants us out of here asap."

label give_report_menu:
    menu:
        "Tell me more about the Sunrider":
            jump tell_more_Sunrider

        "Tell me more about this orange alert.":
            jump tell_more_orange_alert

        "Let's move on. What's next on our agenda?":
            jump give_report_move_on

label tell_more_Sunrider:

    show ava uniform alt neutral neutral with dissolve
    ava "She's the newest ship in the fleet. She's armed like a warship, but built like a carrier. We can field up to twelve ryders and also provide capital ship support for them."
    ava "Her biggest asset is the Vanguard cannon. They took a gun from a battleship-class warship, modified it extensively, and put it on top of our ship. Still, it works like a charm and can rip holes through ships over twice as big as ours."
    ava "Not only that, but the Sunrider can be flown with a crew of just 50 and has one of the most efficient warp drives in the fleet. We'll be able to jump across the galaxy in just days."
    kay "Sounds like a fine vessel."
    jump give_report_menu

label tell_more_orange_alert:

    show ava uniform armscrossed neutral with dissolve
    ava "Don't tell me you don't know. Rynar's surrendered to PACT just this morning."
    kay "Already? That's another neutral world that's been taken by PACT."
    ava "Not only that, but PACT's taken Minerva, Barona, and Gerald in the past three months. One neutral planet after another. What do you think that means?"
    kay "Encirclement. We're next."
    ava "Exactly. So that's why High Command's not taking any risks. If any hostiles enter our gravity well, we're to open fire first and ask questions later."
    jump give_report_menu

label give_report_move_on:

    show ava uniform alt neutral neutral with dissolve
    ava "First, a tour of the ship."
    kay "Oh good."
    ava "As you've noticed, this is the Sunrider's hangar. We can store up to twelve ryders here."
    kay "I don't see any ryders here. Where are they now?"
    ava "We won't be receiving them until Wednesday. Once they're here though, you'll be able to access them and order equipment changes here."
    ava "This is an interactive map of the Sunrider. You can use it to navigate around the ship."
    ava "We're going to head up to the bridge, up above us on deck 1."
    ava "Try using the map to navigate there. Make sure you click on the deck 1 tab first."

    $ captaindeck = 2
    $ ava_location = "bridge"
    $ ava_event = "bridge_tour"
    jump dispatch

label bridge_tour:

    hide screen deck1

    scene bg bridge
    show ava uniform alt neutral neutral:
        xanchor 0.5 xpos 0.8
    with dissolve

    window show

    ava "This is the Sunrider's main bridge. This is where you'll be commanding the ship."
    kay "That's a pretty fancy star map in the middle."
    ava "You can use that star map to plot our course and to warp to other systems."
    ava "I'll also usually be here if you ever need me."

    $ captaindeck = 1
    $ ava_location = "engineering"
    $ ava_event = "engineering_tour"
    jump dispatch

label engineering_tour:

    hide screen deck1

    scene bg engineering
    show ava uniform alt neutral neutral:
        xanchor 0.5 xpos 0.8
    with dissolve

    window show

    ava "This is engineering. The ship's main reactor is located here and we can also use the lab to research and construct new equipment. Unfortunately, the research lab's not yet open."
    kay "That's also going to be available on Wednesday?"
    ava "Correct."

    $ captaindeck = 1
    $ ava_location = "messhall"
    $ ava_event = "messhall_tour"
    jump dispatch

label messhall_tour:

    hide screen deck0
    scene bg messhall
    show ava uniform alt neutral neutral:
        xanchor 0.5 xpos 0.8
    with dissolve

    window show

    ava "This is the ship's mess hall. We can come down here to eat and relax after work."
    kay "Sounds good to me."

    $ captaindeck = 0
    $ ava_location = "captainsloft"
    $ ava_event = "captainsloft_tour"
    jump dispatch

label captainsloft_tour:

    hide screen ship_map
    scene bg captainsloft
    show ava uniform alt neutral neutral:
        xanchor 0.5 xpos 0.8
    with dissolve

    window show

    ava "Finally, these are your personal quarters."
    kay "Looks like I've moved up in life. Wow, it's almost like a loft in Cera City."

    show ava uniform armscrossed looklefttalk with dissolve

    ava "Please don't mess up your room too much, captain."
    kay "I've already got some ideas on how to redecorate it."

    show ava uniform handonhip neutral with dissolve

    ava "You can come here to access your personal logs and other material. Furthermore, if a member of the crew needs your help with something, they'll be waiting outside of your door."
    ava "You can use your map to walk around the ship. You're encouraged to interact with your crew mates whenever possible."
    kay "Alright. A happy ship makes for a strong ship."
    ava "And that concludes our tour. Like I said, I'll be in the bridge most of the time, so you can come to me if you need help."
    kay "What's next?"
    ava "I'm afraid we'll have to cut the formalities short, captain. Like I said, Command wants us out of dry dock as soon as possible."
    ava "We are scheduled for our first live engine test. We'll be sailing port shortly and making one loop around the moon."
    kay "Fine with me. Let's return to the bridge and see what the Sunrider's capable of."

    scene bg bridge
    show ava uniform handonhip neutral:
        xalign 0.5
    with screenwipe
    play music "Music/WorldBuilder.ogg" fadein 1.5 fadeout 1.5

    kay "All hands, this is your captain speaking."
    kay "Man your stations. Activate the main reactor and light the engines.  Momentarily, we'll begin a live test of our engines by sailing port and making one round to the moon."
    kay "We are to enter orange alert as soon as we clear port. Raise shields and scan for any possible hostiles."
    kay "I know this is just a test, but keep your guard up. I want everyone to be on their feet in case we run into any problems."
    ava "Main reactor is coming awake, captain. Power is increasing."
    kay "Wake our lady up, Ava. We're getting out of here."

    show ava uniform order talk with dissolve

    ava "Aye sir. Helmsman, light the engines."

    show ava uniform handonhip neutral with dissolve

    ava "Engineering reports the reactor is working within parameters."
    ava "Power is increasing to the engines."
    ava "Blast off in three."
    ava "Two."

    stop music fadeout 0.5
    play sound "Sound/explosion1.wav"
    scene bg bridge:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 8
    show ava uniform handonhip neutral:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 8

    hide ava uniform order talk with dissolve

    ava "Ugh..."
    kay "What the hell was that!?"

    show ava uniform alt neutral angry with dissolve

    ava "Checking status."
    ava "Engineering reports the reactor core is still stable. No explosions reported in either deck 0 or 2."
    ava "Captain, the only place that blast could have come from is outside."
    kay "Outside!? As in-"
    ava "Contact!  PACT warp signatures detected!"
    kay "What?"
    ava "Missile boats! They jumped in right under our noses!"
    kay "Red alert! Cancel the engine test!"

    play sound "Sound/redalert.ogg"
    play music "Music/Intruders.ogg"
    scene bg bridgered
    show ava uniform alt order angry
    with dissolve

    ava "Aye captain. All hands, battle stations! This is not a drill!"
    kay "This is turning out to be one hell of a maiden flight. Ava, what's our weapon status?"

    show ava uniform alt neutral mad with dissolve

    ava "Limited. The vanguard cannon is still off line. We have flak turrets, saviors, and a few shots of hell darts."
    kay "... ... ..."
    ava "Captain... You're not seriously thinking of taking the Sunrider into battle, are you? We haven't even completed any of our engine tests, much less any munitions checks."
    kay "No time like the present, Ava."

    play sound "Sound/explosion1.wav"
    scene bg bridgered:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 8
    show ava uniform alt neutral mad:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 8
    with dissolve

    show ava uniform alt neutral mad:
        xalign 0.5
    with dissolve

    kay "And from the sound of things, I don't think PACT's going to wait for us to finish our tests."
    kay "Get this ship operational, double time."

    show ava uniform alt order angry with dissolve

    ava "Aye sir. Helmsman, all power to engines!"
    ava "Warning, we have inbound one enemy!"

    scene bg space1
    show missileboatdrydock:
        xpos 0.55 ypos 0.5
    show parallax_ship1 behind missileboatdrydock
    show parallax_ship2 behind missileboatdrydock
    show parallax_ship3 behind missileboatdrydock
    with screenwipe

    "An enemy missile frigate took aim at the Sunrider. Captain Shields gritted his teeth as the Sunrider's engines sparked back to life - painfully slowly."

    play sound "Sound/missile.ogg"
    show missileboatmissile1:
        xpos 0.6 ypos 0.4 additive 1.0
        ease .5 xpos -0.1 ypos 1.0
        repeat 3
    pause 0.2
    play sound1 "Sound/missile.ogg"
    show missileboatmissile2:
        xpos 0.62 ypos 0.43 additive 1.0
        ease .5 xpos -0.1 ypos 1.0
        repeat 3
    pause 0.2
    play sound2 "Sound/missile.ogg"
    show missileboatmissile3 behind missileboatdrydock:
        xpos 0.45 ypos 0.4 additive 1.0
        ease .5 xpos -0.1 ypos 0.9
        repeat 3
    pause 0.2
    play sound3 "Sound/missile.ogg"
    show missileboatmissile4 behind missileboatdrydock:
        xpos 0.46 ypos 0.4 additive 1.0
        ease .5 xpos -0.1 ypos 0.9
        repeat 3
    pause 0.2
    play sound4 "Sound/missile.ogg"
    show missileboatmissile1:
        xpos 0.6 ypos 0.6 additive 1.0
        ease .5 xpos 0.1 ypos 1.1
        repeat 3
    pause 0.2
    play sound5 "Sound/missile.ogg"
    show missileboatmissile2 behind missileboatdrydock:
        xpos 0.4 ypos 0.6 additive 1.0
        ease .5 xpos 0.0 ypos 1.1
        repeat 3
    pause 0.2
    play sound5 "Sound/missile.ogg"

    kay "Ava...!"

    scene bg black
    show parallax_missile1
    show parallax_missile2
    show parallax_missile3
    with screenwipe
    play sound "Sound/missilefly.ogg"
    show missileboatmissilelarge5:
        xpos 1.2 ypos 0.43 zoom 0.04
        ease 4 xpos 0.3 ypos 0.5 zoom 0.1
    show missileboatmissilelarge6:
        xpos 1.2 ypos 0.65 zoom 0.08
        ease 4 xpos 0.5 ypos 0.63 zoom 0.1
    show missileboatmissilelarge4:
        xpos 1.2 ypos 0.23 zoom 0.3
        ease 4 xpos 0.4 ypos 0.32 zoom 0.2
    show missileboatmissilelarge8:
        xpos 1.2 ypos 0.65 zoom 0.2
        ease 4 xpos 0.21 ypos 0.90 zoom 0.3
    show missileboatmissilelarge3:
        xpos 1.2 ypos 0.76 zoom 0.4
        ease 4 xpos 0.34 ypos 0.65 zoom 0.3
    show missileboatmissilelarge7:
        xpos 1.2 ypos 0.12 zoom 0.6
        ease 4 xpos 0.21 ypos 0.23 zoom 0.4
    show missileboatmissilelarge2:
        xpos 1.2 ypos 0.56 zoom 0.6
        ease 4 xpos 0.43 ypos 0.34 zoom 0.5
    show missileboatmissilelarge1:
        xpos 1.2 ypos 0 zoom 0.7
        ease 4 xpos 0.23 ypos 0.45 zoom 0.6
    pause 3

    scene cg drydockdestroyed 0 with screenwipe
    show missileboatmissile1:
        xpos 1 ypos 0.3 additive 1.0 zoom 0.3
        linear .3 xpos 0.65 ypos 0.4
        repeat
    $ renpy.pause (0.3)
    play sound1 "Sound/explosion1.ogg"
    show cg drydockdestroyed 1:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 8
    show missileboatmissile2:
        xpos 1 ypos 0.4 additive 1.0 zoom 0.3
        linear .3 xpos 0.7 ypos 0.45
        repeat 3
    $ renpy.pause (0.3)
    play sound2 "Sound/explosion1.ogg"
    show cg drydockdestroyed 2:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 8
    show missileboatmissile3:
        xpos 0.8 ypos 0 additive 1.0 zoom 0.3
        linear .3 xpos 0.5 ypos 0.2
    $ renpy.pause (0.3)
    play sound3 "Sound/explosion1.ogg"
    show cg drydockdestroyed 3:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 8
    show missileboatmissile4:
        xpos 0.9 ypos 0 additive 1.0 zoom 0.3
        linear .3 xpos 0.4 ypos 0.24
    $ renpy.pause (0.3)
    play sound4 "Sound/explosion2.ogg"
    show cg drydockdestroyed 4:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 8
    hide missileboatmissile1
    $ renpy.pause (0.5)
    hide missileboatmissile2
    $ renpy.pause (0.5)
    hide missileboatmissile3
    $ renpy.pause (0.5)
    hide missileboatmissile4

    "Simultaneously as the frigate launched a swarm of missiles at the Sunrider, her engines roared to life, lurching the ship forward."
    "The missiles struck the dry dock's supports exactly as the Sunrider flew out of the resulting fireball. Behind her, the dry dock collapsed in a chaos of steel and fire."

    scene bg bridgered
    show ava uniform alt neutral mad
    with screenwipe

    "Captain Shields breathed a sigh of relief while Ava looked utterly unaffected by the peril they were just in."
    ava "We're in the clear. Sunrider is joining the fight."
    kay "Fire weapons! Take these bastards out!"

label firstbatle:

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    scene bg bridgered:
        xalign 0.5
        ease 0.025 xalign 0.45
        ease 0.05 xalign 0.55
        ease 0.025 xalign 0.5
        repeat 2
    show ava uniform alt neutral mad:
        xalign 0.5
        ease 0.025 xalign 0.45
        ease 0.05 xalign 0.55
        ease 0.025 xalign 0.5
        repeat 2
    show battlewarning:
        xpos 0.5 ypos 0.5
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide battlewarning

    call mission1_inits
    $ BM.mission = 1  #this sets the label to loop on. in this case it will be mission1
    $ battle1_check1 = False  #without this you would see the dialogue over and over again all the time
    jump battle_start #jumps to mission1 automatically thanks to setting BM.mission to 1

label mission1:

        #an example of scripted dialogue inside the battle
    if not battle1_check1:  #if you don't check for a flag like this you'll see this dialogue every loop.
        $BM.draggable = False  #this makes clicking to advance text work but you can't drag the battlefield around anymore

        show ava uniform alt neutral neutral onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve  #the onlayer part is required to make ava visible on top of the battle_screen

        ava "Welcome to the tactical screen, captain.  From here, you can issue orders to the crew during battle."
        ava "In front, you see the battle grid.  This grid shows where friendlies and enemies are positioned on the battlefield."
        ava "You may click and drag the left mouse button move the camera around the battle grid.  Further, you can use the mouse wheel to zoom in and out."
        ava "To issue an order to a unit, simply select an unit under your command, indicated by the blue ring.  Then you may either order the unit to move to another grid, or to use an attack."
        ava "Moving and attacking expends energy.  Each unit has a finite number of energy points.  Once all of the units under your command no longer have enough energy to act, you must end your turn."
        ava "PACT units are indicated by the red ring.  Your current objective is to eliminate all PACT units from the map."
        ava "The Sunrider is armed with a comprehensive suite of weapons to fulfill this task."
        ava "Laser based weapons have the longest range, but deal little damage.  Kinetic based weapons have short range, but pack a punch.  Missile based weapons have both long range and firepower, but are limited in supply, and so must be used wisely."
        ava "Use the Sunrider's weapons to eliminate the PACT missile frigates.  Good luck, captain."

        hide ava onlayer screens with dissolve #onlayer is also required here because otherwise the hide statement can't find the right image

        $ battle1_check1 = True #this ensures you see this dialogue only once

        $ BM.draggable = True  #this enables dragging the viewport again.

    $BM.battle()  #continue the battle
    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission1 #loop back
    else:
        pass #continue down to the next label

label firstbattle_end:

    hide screen battle_screen
    hide screen commands

    play music "Music/WorldBuilder.ogg"

    scene bg bridgered
    show ava uniform handonhip neutral
    with dissolve

    window show

    ava "Our forces are pushing the remaining PACT units back. The PACT frigates are no longer a threat."
    kay "Join the rest of our fleet. Let's pitch in with the mop up operation."
    ava "Aye captain."
    kay "Two missile frigates down with hardly a scratch. Not bad for my first command, huh Ava?"

    show ava uniform armscrossed smile with dissolve

    ava "Hmph."
    kay "Charge up trinities again. Let's give the rest of those missile frigates a parting gift before they warp out of Cera."

    show ava uniform alt neutral neutral with dissolve

    ava "Aye captain. Charging trinities."
    kay "They must have been trying to warp in missile frigates and take out our ships before we could respond."
    kay "Given how small the attacking force was though, I'd say the entire operation was-"

    show ava uniform alt neutral angry with dissolve
    stop music fadeout 1.5

    ava "Alert! New contacts on scanner!"
    kay "More missile frigates?"
    ava "No... It's unlike anything I've ever seen before."

    scene cg_legionwarpin_background with dissolve
    $ renpy.predict("CG/legionwarpin_full.jpg")
    $ renpy.predict("CG/legionwarpin_legion_warp.png")

    play music "Music/Posthumus_Regium.ogg"

    play sound1 "Sound/small_warpout.ogg"
    show cg_legionwarpin_missilefrigate2 warp:
        xpos 1940 ypos 200
        ease 0.05 xpos 300 ypos 200
    pause 0.05
    show cg_legionwarpin_missilefrigate_warpflash:
        xpos 300 ypos 200
    show cg_legionwarpin_missilefrigate2 out
    pause 0.15
    play sound2 "Sound/small_warpout.ogg"
    show cg_legionwarpin_missilefrigate1 warp:
        xpos 1940 ypos 800
        ease 0.05 xpos 700 ypos 900
    pause 0.05
    show cg_legionwarpin_missilefrigate_warpflash:
        xpos 700 ypos 900
    show cg_legionwarpin_missilefrigate1 out behind cg_legionwarpin_missilefrigate_warpflash
    pause 0.15
    play sound3 "Sound/small_warpout.ogg"
    show cg_legionwarpin_missilefrigate3 warp behind cg_legionwarpin_missilefrigate2:
        xpos 1950 ypos 100
        ease 0.05 xpos 975 ypos 100
    pause 0.05
    show cg_legionwarpin_missilefrigate_warpflash behind cg_legionwarpin_missilefrigate2:
        xpos 975 ypos 100
    show cg_legionwarpin_missilefrigate3 out behind cg_legionwarpin_missilefrigate2
    pause 0.2
    play sound4 "Sound/large_warpout.ogg"
    show cg_legionwarpin_legion warp behind cg_legionwarpin_missilefrigate1:
        xpos 3000 ypos 600
        ease 0.2 xpos 970 ypos 600
    pause 0.2
    scene cg_legionwarpin_legion_full:
        xpos 0.505 ypos 0.56
        pause 1.0
        ease 0.5 zoom 0.4
        ease 0.5 zoom 0.42
    with flash
    $ renpy.pause(4)

    scene bg bridgered with dissolve
    show ava uniform neutral surprise with dissolve

    ava "Sweet mother of god..."
    kay "What is that thing, Ava!? I don't remember PACT having anything that colossal!"

    show ava uniform alt neutral mad with dissolve

    ava "I'm just getting intel from HQ... It's the PACT Super-Dreadnought class warship Legion."

    show ava uniform alt neutral angry with dissolve

    ava "Over three kilometers in length... Armed with enough guns to take down a fleet three times our size by itself! That thing's Veniczar S. Arcadius' personal flagship!"
    ava "HQ has issued a general retreat! All units are to fall back! The Prime Minister's Office has been advised to issue an immediate unconditional surrender!"
    kay "Retreat? It's over already?"

    show ava uniform alt order angry with dissolve

    ava "Warning! I'm detecting a massive power surge coming from it... Wait! Brace for impact!"

    scene legion_cera_fleetfire1 with dissolve
    pause 0.5
    play sound "Sound/legion_laser.ogg"
    show legion_cera_fleetfire2 with screenwipereverse
    hide legion_cera_fleetfire2 with screenwipereverse

    scene cerafleet1 with dissolve
    pause 0.5

    play sound "Sound/explosion1.wav"
    pause 0.1
    play sound1 "Sound/explosion1.wav"
    pause 0.1
    play sound2 "Sound/explosion1.wav"
    scene cerafleet2:
        xalign 0.5
        ease 0.025 xalign 0.40
        ease 0.05 xalign 0.6
        ease 0.025 xalign 0.5
        repeat 8
    $ renpy.pause(5)

    scene bg bridgered with dissolve
    show ava uniform neutral surpriseangry with dissolve

    ava "What disgusting firepower..."

    show ava uniform alt neutral angry with dissolve

    ava "Battleships Gallant and the Behomian Maiden have been sunk! The Fearless has sustained severe damage!"
    ava "Hull breaches reported on section 34-A! Our port trinities are no longer operative!"
    kay "Break away! Our ship doesn't stand a chance against that!"
    ava "The enemy warship is powering its weapons again!"

    scene legion_cerafire1 with dissolve
    play sound "Sound/legion_maincannon.ogg"
    scene legion_cerafire2 with dissolvelong
    pause 1.0
    scene legion_cerafire3 with dissolvemedium
    $ renpy.pause(1)
    scene legion_cerafire4 with dissolve
    show legion_cerafire5 with horizontalwipereversefast
    hide legion_cerafire5 with horizontalwipereversefast
    play sound1 "Sound/explosion1.wav"
    play sound1 "Sound/explosion5.ogg"
    scene legion_cerafire6:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 4
    with dissolve
    scene legion_cerafire7:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 15
    with dissolve
    $ renpy.pause(2.0)

    scene bg bridgered
    show ava uniform altneutral surpriseshout
    with dissolve

    kay "R-report!"
    ava "The warship's nuked Cera City with that last shot. I'm still trying to figure out the scope of the damage, but..."
    kay "U-unbelievable... To use a weapon of that magnitude on a civilian target..."
    ava "More than a million civilians have been lost! All contact has been lost with our civilian and military leadership!"
    ava "The rest of the Cera Space Force is scattering! We're going to get overwhelmed if we don't get out of here!"
    ava "What are your orders, captain!?"
    kay "... ... ..."
    ava "CAPTAIN!!"
    "The Sunrider began to pound as more enemies arrived. Shields wiped sweat off from his brows and saw that his hand was soaked."
    "The pounding wasn't coming from the enemy. It was his own heart."
    kay "Fall back..."
    kay "... ... ..."
    kay "Fall back! Warp to the nearest safe harbor!"

    play music "Music/Coming_Soon_Part1.ogg" fadeout 1.5
    show ava uniform alt neutral mad with dissolve

    ava "Understood."

    show ava uniform alt order angry with dissolve

    ava "Navigator, punch in the fall back coordinates into the computer! Spool up the warp drive and prepare to jump!"
    kay "... ... ..."
    "Shields took a final look at his burning home world."
    "This wasn't the end."
    "He was going to be back. No matter the cost."

    play music "Music/Coming_Soon_Part2.ogg" noloop fadeout 0.5
    scene bg space_red
    show sunrider_warpout 1:
        xpos 0.5 ypos 0.5
    show parallax_ship1 behind sunrider_warpout
    show parallax_ship2 behind sunrider_warpout
    show parallax_ship3 behind sunrider_warpout
    with dissolve
    pause 2.0

    show sunrider_warpout_engine:
        xpos 0.5 ypos 0.48
        alpha 0
        linear 5.0 alpha 1
    show ava uniform alt neutral mad:
        xpos 0.2 xzoom -1
    with dissolve

    ava "Warp out in 3...!"
    $ renpy.pause(1.0)
    ava "2..."

    hide ava with dissolve
    show captain order 1:
        xpos 0.4
    with dissolve
    kay "... ... ..."

    $ renpy.pause(1.0)

    show captain order 2 with dissolve
    kay "WARP!!!"

    hide captain with dissolve

    pause 1.5
    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_flash:
        xpos 0.5 ypos 0.5
        alpha 1.0
        linear 0.5 alpha 0
    hide sunrider_warpout_engine with dissolvequick
    show sunrider_warpout 3:
        ease 0.3 xpos -1.0 ypos 2.0
    pause 0.5

    window hide

    play sound1 "Music/Posthumus_Regium_Finale.ogg" fadeout 0.5 fadein 0.5 noloop
    scene bg black2 with dissolvelong
    pause 0.1
    show mainlogo:
        subpixel True
        xpos 0.5 ypos 0.5 zoom 1.0
        ease 7.0 zoom 1.1
    with dissolvelong
    $ renpy.pause(9.0)
    hide mainlogo with dissolvelong
    pause 1.0

    window show

    scene bg captainsoffice with dissolve
    play music "Music/The_Meteor.ogg"

    "Shields sat at his office, writing his daily log."
    kay "{i}It's been a week since the fall of Cera. Despite our best efforts, we have been unable to regroup with the rest of the Cera Space Force. The crew is starting to fear that we may be the only ones who got out of that massacre in one piece. To tell the truth, I'm beginning to believe that too.{/i}"
    kay "{i}I don't know what we're going to do or what next step to take. All I know is that we're going to be alone from now.{/i}"
    "The doorbell interrupted Shields' thoughts."
    kay "Come in."

    show ava uniform armscrossed neutral with dissolve

    ava "Captain."
    kay "Any news of the fleet?"
    ava "None."
    kay "... ... ..."
    ava "The crew's beginning to get worried. We've been doing nothing but scanning for the past week. If a PACT force finds us, we're sitting ducks here."

    menu:
        "You're suggesting that we give up the search?":
            jump giveupsearch
        "That's agreed. I think we've wasted enough of our time here.":
            jump wastedenoughtime

label giveupsearch:

    show ava uniform alt neutral neutral with dissolve

    ava "Long range scanners do not show any Cera signatures. What's left of our government surrendered and was dissolved six days ago. Most likely, what's left of the Cera Space Force has either gone rogue or been impressed into the PACT fleet."
    jump shipwithoutflag

label wastedenoughtime:

    show ava uniform alt neutral neutral with dissolve

    ava "What's left of our government surrendered and was dissolved six days ago. I don't think there's any hope in looking for our military any more."
    jump shipwithoutflag

label shipwithoutflag:
    kay "Ava, tell me something. What's a ship without a flag?"

    show ava uniform neutral looklefttalk with dissolve

    ava "Sir? Well, a pirate ship."

    menu:
        "Pirate ship Sunrider. I like the sound of that.":
            jump pirateshipsunrider

        "I don't intend on becoming a pirate captain.":
            jump notapiratecaptain


label pirateshipsunrider:

    $ captain_moralist += 1

    show ava uniform handonhip neutral with dissolve

    ava "Are you suggesting we go rogue?"
    kay "I don't think we have much of a choice. Our government's no more. We're going to have to go it alone from now on."
    jump whatareyousuggesting

label notapiratecaptain:

    $ captain_prince += 1

    show ava uniform handonhip neutral with dissolve

    ava "I wasn't suggesting we turn to piracy."
    kay "Remember, Ava. The Sunrider will always be carrying the flag of Cera."
    jump whatareyousuggesting

label whatareyousuggesting:

    ava "So what are you suggesting?"
    kay "PACT won't get away with what they did to our home. We're going to take the fight to them."

    show ava uniform armscrossed neutral with dissolve

    ava "With just our one ship?"
    kay "We'll find allies. We're not the only neutral world to have been conquered by them."
    kay "We find others like us. Build a fleet together. And then retake all of our planets, one by one."
    ava "Hm. I suppose you've already got a plan."

    menu:
        "Just like old times, Ava.":
            jump justlikeoldtimes

        "Are you questioning my orders, commander?":
            jump questioningorders

        "I'm not the kid you remember anymore, Ava.":
            jump notthekidyouremember

label justlikeoldtimes:

    $ affection_ava += 1

    show ava uniform alt neutral neutral with dissolve

    ava "It's a good thing they put me as your first officer. I don't even want to imagine how much trouble you'd cause if I weren't here to clean up after you."
    kay "Hahaha. Come on now, is that all you can remember of me from high school?"
    ava "Well, I do recall that you were certainly one of the most frustrating youths for a student council president to have to deal with..."
    ava "I remember the time you installed an anti-gravity device in the student council room. It was impossible getting everything cleaned up afterwards."
    kay "Ah, that little thing. Come on, you had a good laugh afterwards, didn't you?"

    show ava uniform armscrossed frown with dissolve

    ava "No."

    jump newordersjumptotydaria

label notthekidyouremember:

    kay "I'm not the kid you remember anymore, Ava."
    kay "We can't let ourselves be defeated so easily. If PACT pushes us, I say we push back. The Sunrider's still got a lot of fight left in her yet."

    show ava uniform alt neutral neutral with dissolve

    ava "All right. We fight."
    ava "I must say, captain..."
    kay "What's that?"
    ava "You still haven't changed a bit."

    jump newordersjumptotydaria

label questioningorders:

    $ affection_ava -= 2

    kay "Are you questioning my orders, commander?"

    show ava uniform alt neutral neutral with dissolve

    ava "My apologies, captain. I, uh, had a momentary slip of the tongue."

    jump newordersjumptotydaria

label newordersjumptotydaria:

    show ava uniform alt neutral neutral with dissolve

    ava "In the meantime, what are your orders?"
    kay "We'll warp to the nearest neutral planet of Tydaria. Chances are, after the fall of Cera, they'll be more than likely to be jittery about PACT. "
    ava "Understood. The ship will be prepared to warp at your command."

    menu:
        "What's the status of the Sunrider?":
            jump statusofthesunrideraftercera

        "How are you holding up after what happened?":
            jump howareyouholdingup

        "Report to the bridge. I'll see you there once I'm ready.":
            jump seeyouthereonceready

label statusofthesunrideraftercera:

    ava "She's had better days. We had to sail port before we could finish any of our tests. Our missiles are empty and our Vanguard Cannons are still offline."
    ava "And that's not even the worst. We had to leave Cera before we could pick up any of our ryders. Not only that, but we're missing our chief engineer and our doctor. Both Research and Development and the Sickbay are still dark."
    kay "Whew. Try to make do with what we have. We'll have to resupply and finish our tests at Tydaria."
    ava "On that note, I have one more issue."
    ava "Running a ship is going to take money. I've looked into some ways to raise some immediate cash."
    ava "The various galactic powers all post bounties on rival factions. I've been putting together a folder containing letters of marque from all governments currently aligned against PACT."
    kay "In other words, our only way of making money right now is privateering for other planets which have a grudge against PACT. Which is pretty much everyone, I'm guessing."
    ava "Correct. We'll be paid a sum of money for each PACT target we sink. The bigger the target, the bigger the reward."
    kay "Alright, keep me posted on the money situation."

    menu:
        "How are you holding up after what happened?":
            jump howareyouholdingup

        "Report to the bridge. I'll see you there once I'm ready.":
            jump seeyouthereonceready


label howareyouholdingup:

    show ava uniform armscrossed lookleftmouthopen with dissolve

    ava "I'm... fine, captain. There's no reason to worry about me."
    kay "Are you sure?"

    show ava uniform alt neutral neutral with dissolve

    ava "Yes. We've got more immediate problems than that."
    kay "I suppose you're right."
    ava "Indeed."
    kay "Still, if you need to talk about anything, my door's always open."

    menu:
        "What's the status of the Sunrider?":
            jump statusofthesunrideraftercera

        "Report to the bridge. I'll see you there once I'm ready.":
            jump seeyouthereonceready

label seeyouthereonceready:

    ava "Understood."

    $ captaindeck = 0
    $ ava_location = "bridge"
    $ ava_event = "warptotydaria"
    jump dispatch

label warptotydaria:

    $ warpto_occupiedcera = True
    $ warpto_tydaria = True

    hide screen deck1

    scene bg bridge
    show ava uniform alt neutral neutral
    with dissolve

    window show

    ava "You can use the starmap at the center of the bridge to plot our course."

    hide ava with dissolve

    menu:
        "Access galaxy map.":
            jump galaxymap

        "Return to map.":
            jump dispatch

label Tydaria_jump1:

    window show

    play music "Music/WorldBuilder.ogg" fadeout 1.5

    scene bg bridge with fade
    show ava uniform alt neutral neutral with dissolve

    ava "Aye captain. Course laid in."

    show ava uniform order talk with dissolve

    ava "All hands, this is the Commander speaking. We will momentarily enter jump space to the neutral world of Tydaria."
    ava "Assume jump stations and await further orders on dropout."
    ava "The jump drive is functioning as expected, captain. Core status is green. On your word."
    kay "Warp!"

    $ Random = renpy.random.randint(1,9)

    if Random == 1:
        scene space back1
    if Random == 2:
        scene space back2
    if Random == 3:
        scene space back3
    if Random == 4:
        scene space back4
    if Random == 5:
        scene space back5
    if Random == 6:
        scene space back6
    if Random == 7:
        scene space back7
    if Random == 8:
        scene space back8
    if Random == 9:
        scene space back9

    show sunrider_warpout_standard:
        xpos 700 ypos 350
    with dissolve

    pause 1.0

    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_standard_flash:
        xpos 426 ypos 0 alpha 0
        linear 0.1 alpha 1
        linear 0.1 alpha 0
    show sunrider_warpout_standard out:
        xpos 700 ypos 350
        ease 0.2 xpos 200 ypos 300 zoom 0

    pause 1.0

    scene tydaria_orbit:
        ypos 0
        ease 1.5 ypos -120
    with dissolve
    pause 1

    show sunrider_warpout_standard out:
        xpos 2300 ypos 1200 zoom 2
        ease 0.2 xpos 1000 ypos 500 zoom 0.5
    pause 0.2
    play sound "Sound/large_warpout.ogg"
    show cg_legionwarpin_missilefrigate_warpflash:
        zoom 1.5 xpos 1550 ypos 750
    show sunrider_warpout_standard

    pause 2.0

    scene bg bridge with fade
    show ava uniform alt neutral neutral with dissolve

    ava "Warp complete, captain. We're arriving at the mining world of Tydaria."
    ava "What kind of help do you think we'll be able to get here?"
    kay "Resources and supplies, at least. There's a big space mining operation going on around the rings of the planet."
    ava "You might want to hold that thought. I'm detecting unknown vessels on an intercept course for us."
    kay "Flag?"
    ava "I'm not finding any of them on any of the flag registries..."

    play music "Music/Sui_Generis.ogg" fadeout 1.5
    show ava uniform alt neutral angry with dissolve

    ava "Damn. Pirates!"

    play sound "Sound/redalert.ogg"
    scene bg bridgered
    show ava uniform alt neutral angry
    with dissolve

    kay "Red alert! Raise shields and power weapons!"
    ava "We are being hailed!"

    show ava uniform alt neutral angry:
        zoom 1
        ease 0.5 xpos 0.7
    pause 0.5
    show cosette plugsuit handsonhip evilsmile:
        xpos 0.3
    with wipeup

    cos "Haahaaahaaa! This is the pirate ryder Havoc! Lower your shields and surrender your cargo!"
    kay "Stand down. This is an armed warship of the Cera Space Force. We will not hesitate to open fire if you approach."
    cos "Cera Space Force, huh? Your ship will make a lovely addition to my pirate fleet. After we've dealt with you, of course!"

    show cosette plugsuit point evilsmile with dissolve

    cos "Boys, rough them up!"

    hide cosette plugsuit point evilsmile with wipedown
    show ava uniform alt neutral angry:
        zoom 1
        ease 0.5 xpos 0.5

    kay "Ava, what's the situation?"
    ava "Two pirate ryders, inbound fast.  Both infantry class. There's one more bomber-class ryder leading them, designation Havoc."
    ava "Also, two pirate destroyers are approaching. Estimated time until arrival: Ten minutes."
    kay "Let's try to end this before the destroyers get here. Concentrate all firepower on the lead pirate ryder!"
    kay "Besides, she just looks like a little girl. Maybe a little show of force will help put her in her place."

    show ava uniform armscrossed frown with dissolve

    ava "Captain... Please don't underestimate the enemy..."

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    scene bg bridgered:
        xalign 0.5
        ease 0.025 xalign 0.45
        ease 0.05 xalign 0.55
        ease 0.025 xalign 0.5
        repeat 2
    show ava uniform armscrossed frown:
        xalign 0.5
        ease 0.025 xalign 0.45
        ease 0.05 xalign 0.55
        ease 0.025 xalign 0.5
        repeat 2
    show battlewarning:
        xpos 0.5 ypos 0.5
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide cosette
    hide battlewarning

    call mission2_inits
    $ BM.mission = 2
    $ battle2_check1 = False
    $ battle2_check2 = False
    jump battle_start

label mission2:

    if not battle2_check1:
        $BM.draggable = False

        show ava uniform armscrossed frown onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve  #the onlayer part is required to make ava visible on top of the battle_screen

        ava "We're heavily outnumbered, captain. What are your orders?"
        kay "Concentrate on the lead bomber. These pirates think about nothing but themselves. Once Cosette realizes we mean business, she'll probably back off."
        show ava uniform handonhip mad onlayer screens zorder 50 with dissolve

        ava "Understood, captain. Let's hope this goes as planned..."

        show ava uniform handonhip mad onlayer screens zorder 50:
            ease 0.25 xpos -0.15

        play sound "Sound/objectives.ogg"
        "Objective: Destroy the Havoc"

        hide ava onlayer screens with dissolve #onlayer is also required here because otherwise the hide statement can't find the right image

        $ battle2_check1 = True #this ensures you see this dialogue only once

        $ BM.draggable = True  #this enables dragging the viewport again.

    if battle2_check2 == False and sunrider.hp < sunrider.max_hp:
        $BM.draggable = False

        kay "Damage report!"

        show ava uniform alt neutral angry onlayer screens zorder 50:
            xzoom -1 xpos 0.2
        with dissolve

        ava "We're venting air in four sections. Our systems are stretched to capacity!"
        kay "How did so many missiles get through!? Are the gunners blind, Ava?"
        ava "We're still recovering from Cera, captain. The Sunrider's giving it her all."

        hide ava onlayer screens with dissolve
        scene havoc_tydaria_miss1 onlayer screens

        show cosette plugsuit point evilsmile onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        cos "Now's our chance! Take their engines out, but leave the ship intact!"
        cos "We'll board and cut down the crew hand to hand."

        kay "You're awfully persistent for a little girl, aren't you?"

        play sound "Sound/hit.wav"
        show cosette plugsuit neutralalt yandereshock onlayer screens:
            xpos 0.2
            ease 0.02 xpos 0.19
            ease 0.04 xpos 0.21
            ease 0.02 xpos 0.2
            repeat 4
        with dissolve

        cos "Hurk..."
        cos "Did... you... just... call... me..."

        show cosette plugsuit neutral yanderegrin onlayer screens:
            zoom 1.0
        with dissolve

        cos "LITTLE!?"
        kay "Uh... yes?"

        show cosette plugsuit neutral yanderegrin onlayer screens:

        cos "Y-YOOUUUU!!!"
        cos "KILL THEM ALL! BUT LEAVE THE CAPTAIN FOR ME!"
        cos "HE'S... MINE!"

        hide cosette plugsuit neutral yanderegrin onlayer screens with dissolve
        show ava uniform armscrossed looklefttalk onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        ava "Captain... Please do not provoke the enemy..."

        hide ava uniform armscrossed looklefttalk onlayer screens with dissolve

        kay "Damn... Just one problem after another..."

        play sound "Sound/laser.wav"
        show havoc_tydaria_miss2 onlayer screens with dissolvequick
        pause 0.2
        play sound "Sound/laser.wav"
        show havoc_tydaria_miss3 onlayer screens  with dissolvequick
        pause 0.2
        hide havoc_tydaria_miss2 onlayer screens  with dissolvequick
        play sound "Sound/laser.wav"
        show havoc_tydaria_miss4 onlayer screens  with dissolvequick
        pause 0.2
        hide havoc_tydaria_miss3 onlayer screens  with dissolvequick
        pause 0.2
        hide havoc_tydaria_miss4 onlayer screens  with dissolvequick

        show cosette plugsuit point yandereneutral onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        cos "Eh?"

        scene blackjack_tydaria_enter onlayer screens with dissolve
        play music "Music/Driving_the_Top_Down.ogg"

        $ PlayerTurnMusic = "Music/Driving_the_Top_Down.ogg"

        show asaga plugsuit neutralalt alert onlayer screens:
            xpos 0.8
        with dissolve

        asa "The cavalry has arrived!"
        kay "What the... Who are you?"

        show asaga plugsuit vpose onlayer screens with dissolve

        asa "A HERO OF JUSTICE!"
        asa "Looks like you could use a hand there! Don't worry, my Black Jack will take care of these guys in a flash!"

        show ava uniform armscrossed neutral onlayer screens:
            xpos 0.2
        with dissolve

        ava "She's flying a mercenary ryder licensed by the United Mining Guild, captain. Probably hired security for the mining operation on Tydaria. Do you think we can trust her?"
        kay "Doesn't look like we have much of a choice."
        kay "Alright, pilot of the Black Jack. Let's see what you've got."
        asa "No problem!"

        hide blackjack_tydaria_enter onlayer screens
        hide ava onlayer screens
        hide asaga onlayer screens
        hide cosette onlayer screens

        show screen battle_screen

        python:
            blackjack_weapons = [BlackjackMelee(),BlackjackLaser(),BlackjackAssault(),BlackjackMissile(),BlackjackPulse()]
            blackjack = create_ship(BlackJack(),(6,3),blackjack_weapons)

        show asaga plugsuit neutralalt smile onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        asa "By the way, did you know about repeating attacks?"
        asa "Some weapons like assault rifles don't deal much damage, but shoot multiple times in a single attack.  It's a good way to deal reliable damage against units with high evasion like ryders."
        asa "Watch out though! They're totally useless against units with armor, like capital ships."
        asa "If you select a weapon, the third number listed on the enemy unit is that unit's armor rating.  Be careful when you're using your kinetic-type weapons especially, because armor's twice as effective against kinetics!"

        hide asaga onlayer screens with dissolve

        $ battle2_check2 = True
        $ BM.draggable = True


    $ BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission2 #loop back
    else:
        pass #continue down to the next label

label secondbattle_end:

    hide screen battle_screen
    hide screen commands

    scene bg black2 with horizontalwipereverse
    scene bg hangar with horizontalwipereverse
    window show

    play music "Music/WorldBuilder.ogg"  fadeout 1.5

    show asaga plugsuit handsonhips happy:
        xpos 0.35
    with dissolve

    asa "Whew, that sure was hairy! I didn't ever think those pirates would pick on a military ship!"

    show ava uniform armscrossed frown:
        xpos 0.65
    with dissolve

    ava "Stop right there, pilot. You're going to have get searched for weapons."

    menu:
        "Hey Ava... Don't be so uptight.":
            jump dontbesouptight

        "Sorry, regular protocol.":
            jump sorryregularprotocol

label dontbesouptight:

    $ affection_asaga += 1
    $ captain_moralist += 1

    show ava uniform handonhip mad with dissolve

    ava "Captain, military protocol section 9-32B clearly states that all-"
    kay "I'm Captain Kayto Shields of the assault carrier Sunrider. Excuse my first officer, Commander Ava Crescentia. She's not as bad as she seems at first. Who are you?"

    jump asagaoakrunpilot

label sorryregularprotocol:

    $ affection_ava += 1
    $ captain_prince += 1

    show asaga plugsuit armscrossed sad with dissolve

    asa "Uuu... Does this mean that I'm gonna have get groped by the mean lady beside you?"

    show ava uniform armscrossed surprisemad with dissolve

    ava "L-lady...?"
    kay "Hahaha. I'm Captain Kayto Shields of the assault carrier Sunrider. The mean lady beside me is Commander Ava Crescentia. And who are you?"

    jump asagaoakrunpilot

label asagaoakrunpilot:

    show asaga plugsuit neutralalt smile with dissolve

    asa "Asaga Oakrun, pilot of the Black Jack."
    kay "Thanks for the help out there."
    asa "Eh-heh... Don't worry, those guys were nothin'!"
    kay "So, what exactly were you doing out there? I can't imagine a lone ryder operating out here for no reason."
    asa "Oh nothing, just keeping the space ways safe!"

    show ava uniform alt neutral mad with dissolve

    ava "Safe...?"

    show asaga plugsuit vpose with dissolve

    asa "Dunnnndadada!! Coming to the rescue wherever the weak are oppressed! It's the hero of justice, the vanguard of the innocent! For love, freedom, and just a little bit of money on the side, it's Asaga of the Black Jack!"

    show ava uniform armscrossed frown with dissolve

    ava "... ... ..."
    kay "Let me guess. You're a freelancer?"

    show asaga plugsuit armscrossed smile:
        xzoom -1
    with dissolve

    asa "Eh-heh... I guess you could call me that."

    show asaga plugsuit neutral content with dissolve

    asa "The space around here's pretty dangerous, so the Mining Union's been paying me to bust up any pirates around here. Easier said then done though! Those guys are harder to kill than cockroaches!"

    menu:
        "Tell me more about your freelancing.":
            jump tellmorefreelancing
        "Tell me more about the pirates.":
            jump tellmorepirates
        "Tell me more about the Mining Union.":
            jump tellmoreUnitedMiningFederation
        "Let's move on to our next course of action.":
            jump moveonnextaction

label tellmorefreelancing:

    show asaga plugsuit armscrossed content with dissolve

    asa " Ah, I've been wandering around the neutral rim, looking around for any odd jobs here and there. I'd like to call myself an adventurer."
    kay " And you do this alone, in just a single ryder?"
    asa " Ah, not really. I have Chigara to help me out. She's the one who built me my Black Jack here."
    kay " Chigara...? Is she an engineer?"
    asa " Yeah, you can call her that. She's a genius when it comes to technology, and she can fix just about anything mechanical!"
    kay "(I'm betting we'll get to meet this Chigara very soon...)"

    menu:
        "Tell me more about the pirates.":
            jump tellmorepirates
        "Tell me more about the United Mining Federation.":
            jump tellmoreUnitedMiningFederation
        "Let's move on to our next course of action.":
            jump moveonnextaction

label tellmoreUnitedMiningFederation:

    show asaga plugsuit armscrossed content with dissolve

    kay "The Mining Union?"
    asa "I'm working for them right now. I don't really know much about 'em, aside from the fact that they mine the ore on Tydaria and pay me money to take out the pirates."
    asa "A lady by the name of Sophita is my contact with the Union.  If you're looking for some work, she'd be the person to talk to around here."
    kay "What do they think of PACT?"
    asa "Nothing much, really.  They don't really pick sides, as long as they can keep mining."
    kay "(I wonder how long that'll last...)"

    menu:
        "Tell me more about your freelancing.":
            jump tellmorefreelancing
        "Tell me more about the pirates.":
            jump tellmorepirates
        "Let's move on to our next course of action.":
            jump moveonnextaction

label tellmorepirates:

    show asaga plugsuit armscrossed mad with dissolve

    asa "The pirates in this sector are led by a nasty girl named Cosette Cosmos. You've already met her."
    kay "What's a little girl like that doing committing piracy?"
    asa "Cosette may look like a brat, but don't underestimate her. She's feared in this whole sector as a ruthless pirate. I even heard a rumor the other day that she slit her own pa's throat for not buying her candy on her 14th birthday."
    kay "I'm not sure if I really believe-"
    asa "And there's this other one about her ship, the Havoc, being filled with rats, that she keeps as pets."
    kay "Really."
    asa "Anyways, I've had a couple run ins with her, and I can say, she's not to be trifled with."
    asa "Be careful of the Havoc's anti-matter missiles. Those will definitely put more than a dent on any capital ship's hull."
    asa "The Havoc's only weakness is that it's pretty slow and sluggish, so it can be picked off by other ryders."
    kay "Thanks, I'll keep that in mind."

    menu:
        "Tell me more about your freelancing.":
            jump tellmorefreelancing
        "Tell me more about the United Mining Federation.":
            jump tellmoreUnitedMiningFederation
        "Let's move on to our next course of action.":
            jump moveonnextaction

label moveonnextaction:

    show asaga plugsuit neutral content with dissolve

    asa "Hey, you guys are a part of the former Cera Space Force, huh?"
    kay "That's right."
    asa "Why don't we join forces for awhile? From the look of things here, you seem to be an assault carrier without any ryders. Help me take care of these pirates, and I'll join you guys as the Sunrider's first ryder."

    show ava uniform armscrossed frown with dissolve

    ava "Captain, we don't know if we can trust this girl. We've only just met her!"

    menu:
        "She's already saved our necks. And she's right. A carrier without any ryders is useless. I say we work together for now.":
            jump savednecksworktogether
        "Sorry, Asaga. I don't think I can let you join the team without making Ava lose sleep for the next week.":
            jump sorryasagaavalosesleep

label savednecksworktogether:

    $ affection_asaga += 1

    show ava uniform facepalm with dissolve

    ava "Sigh..... I knew you were going to say that."

    show asaga plugsuit neutralalt closedeyessmile with dissolve

    asa "Eh-heh... I'm glad we agree, capt'n!"

    jump fornowsunriderrepairs

label sorryasagaavalosesleep:

    $ affection_ava += 1

    show asaga plugsuit neutral sad with dissolve

    asa "Aww..."
    kay "But you can stay onboard for a bit, I guess. I don't want to be caught without a ryder if the pirates decide to come back with reinforcements."

    show asaga plugsuit excited closedeyessmile with dissolve

    asa "Yayyy--"

    show ava uniform facepalm with dissolve

    ava "Unbelievable..."

    jump fornowsunriderrepairs

label fornowsunriderrepairs:

    kay "For now, the Sunrider needs repairs and supplies."
    kay "We'll make our way to Tydaria and dock there. Then we'll decide our next course of action."

    show asaga plugsuit handsonhips happy with dissolve

    asa "Oh! I know someone who can help us with that! Chigara has her workshop in Tydaria. She'll be able to fix your ship in no time!"
    ava "Chigara? Friend of yours?"
    asa "Uh-huh! She's a genius when it comes to technology!"
    kay "Alright, if your friend can help us, we can head to her workshop."
    kay "Ava and I are going to head up to the bridge now. You should stay here with your ship. We'll call you on the comm if anything comes up."
    asa "Understood, capt'n!"

    scene bg black2 with horizontalwipereverse
    scene bg bridge with horizontalwipereverse

    show ava uniform armscrossed neutral with dissolve

    ava "Sigh... I can't believe you're seriously going to let her stay onboard."
    kay "What's the matter, Ava?"
    ava "Nothing! It's just... ugh..."
    ava "Anyways, what are you waiting for? The quicker we get to Tydaria, the less I need to worry about a fleet of pirate ships warping in around us. Just use the star map and order the Sunrider to the workshop. I've already put in its coordinates on the computer, so you should be able to find it without any problems."

    scene bg black2 with horizontalwipereverse
    scene bg bridge with horizontalwipereverse
    show ava uniform armscrossed neutral with dissolve

    kay "This is the Sunrider, requesting permission to dock."
    chi "Ah... Welcome to the Stardust Bakery."
    kay "B-bakery...? Didn't Asaga say this was a workshop?"
    ava "I knew we shouldn't have trusted her..."
    chi "Ummm... We offer a cupcakes, cream puffs, strawberry cakes, and various muffins... Oh."
    chi "And we might just do starship repairs as well."
    kay "This is getting weirder and weirder by the minute."
    chi "If I can just come on board, I'll be able to survey the extent of the repairs and give you a quote. How's that?"
    kay "Uh, alright, sure. I think we have a friend of yours waiting in the hangar too."

    scene bg hangar with dissolve
    play music "Music/Colors_Of_An_Orchestra.ogg"  fadeout 1.5

    show asaga plugsuit excited happy with dissolve

    asa "Hey Chigaraaa! I'm back home!"

    show asaga plugsuit excited happy:
        zoom 1
        ease 0.5 xpos 0.35
    show chigara plugsuitlabcoat altneutral smile:
        xpos 0.65
    with dissolve

    chi "Ah... And you've brought friends..."

    show asaga plugsuit altneutral happy with dissolve

    asa "Uh huh, this is Capt'n Kayto Shields of the starship Sunrider! And that lady's First Officer Ava Crescentia."

    show ava uniform facepalm:
        xpos 0.9
    with dissolve

    ava "Ugh..."

    hide ava with dissolve
    kay "It's nice to meet you. You must be Chigara."

    chi "Umm... Chigara Lynn's my full name, but Asaga calls me that."

    menu:

        "So what's this about this place being a bakery?":
            jump beingabakery
        "This is a strange place for a girl to have a workshop...":
            jump girltohaveaworkship
        "Let's get down to business. The Sunrider's in need of repairs. Not only that, but we still need to complete our tests and resupply.":
            jump completeourtestsandresupply

label beingabakery:

    show chigara plugsuitlabcoat altneutral forcedsmile with dissolve

    chi "Ah, the Stardust Bakery is the best place to get pastries in Tydaria."

    show asaga plugsuit handsonhips happy with dissolve

    asa "The only place!"
    chi "Cup cakes, cream puffs, sandwiches, we have it all."
    kay "Errr... Do you get a lot of business here?"

    show chigara plugsuitlabcoat altneutral sad with dissolve

    chi "Uuuu... No. Everyone seems much more interested in getting their ship fixed..."
    kay "So why don't you just open a dry dock instead of a bakery?"

    show asaga plugsuit handsonhips mad with dissolve

    asa "Oy, oy! It's always been Chigara's dream to run a bakery! You can't just shut a girl's dreams down like that!"
    chi "Uuu... M-maybe I really should consider giving up. It feels so awkward selling cupcakes next to the starship fuel..."

    menu:
        "This is a strange place for a girl to have a workshop...":
            jump girltohaveaworkship
        "Let's get down to business. The Sunrider's in need of repairs. Not only that, but we still need to complete our tests and resupply.":
            jump completeourtestsandresupply


label girltohaveaworkship:

    show chigara plugsuitlabcoat altneutral smile with dissolve

    chi "Not at all.  Tydaria is one of the Mining Union's primary worlds.  I've been renting this dock from the Union and patching up ships with Asaga for a while now."
    chi "As long as I service the Union's ships, they've been very supportive of my efforts here."

    show chigara plugsuitlabcoat altneutral sad with dissolve

    chi "Well… aside from the bakery."
    kay "I was referring more to yourself..."

    show chigara plugsuitlabcoat altneutral forcedsmile with dissolve

    chi "Me? Mmm... Well, I guess you can call me one of those people like Asaga..."
    kay "A freelancer?"
    chi "Oh yes, that."
    kay "(Something tells me there's more to this pair than they're letting on… These girls don't exactly fit my image of freelancers…)"

    menu:
        "So what's this about this place being a bakery?":
            jump beingabakery
        "Let's get down to business. The Sunrider's in need of repairs. Not only that, but we still need to complete our tests and resupply.":
            jump completeourtestsandresupply


label completeourtestsandresupply:

    show chigara plugsuitlabcoat neutral neutral with dissolve

    chi "Mmm... Most of the damage seems to be to the outer hull. It shouldn't be too hard to repair."
    kay "Now, I think you're understating things. The Sunrider's a top of the line military vessel. It's not going to be like scraping a meteoroid impact from a mining ship."

    show asaga plugsuit armscrossed confident with dissolve

    asa "Ufufufu... Don't worry, capt'n. Chigara's a crazy genius when it comes to technology. I've never seen a single machine that she couldn't fix."
    kay "Look over there. See that? That's a busted power convertor that took a lab of twelve  scientists a month to make. There's no way you could fix that!"

    show chigara plugsuitlabcoat altneutral forcedsmile with dissolve

    chi "Ummm... I actually made this little contraption in my sleep yesterday night... I was really confused when I woke up and saw a power converter on my bed, but I think it should work perfectly for your ship."
    kay "Wha..."
    asa "C'mon, try it, capt'n! I swear it'll work!"
    chi "Excuse me... Here we go..."
    kay "Well, I'll be damned. Not only does it work, but the efficiency's been increased by 20 percent."
    asa "I told ya she was a genius!"
    chi "Ehehehehe..."
    kay "Uh, well okay then. You can start repairs as soon as possible."

    hide asaga with dissolve
    show ava uniform handonhip neutral:
        xpos 0.35
    with dissolve

    ava "Do you want to oversee the repair work?"
    kay "Uhh, I think I'll leave you in charge of that. I'll be in my quarters, trying to find a way to write about this in my logs."
    ava "Understood captain. I'll contact you once repairs are complete."

    scene bg black2 with horizontalwipereverse
    scene bg captainsoffice with horizontalwipereverse

    kay "Begin captain's log. The Sunrider's been in dry dock for the past two days. Repairs have gone ahead of schedule and we're back to full combat status already. That Chigara girl really is something. I wouldn't mind having her in my engineering staff."
    kay "We're about to set sail again. I'm still not sure what to do about our two guests. Even though Ava still doesn't trust them, they've been an invaluable help. I think they'd do well on board the Sunrider."
    kay "... ... ..."
    kay "End captain's log."
    kay "(Well, I guess it's time to explore the ship.)"

    $ captaindeck = 0
    $ ava_location = "bridge"
    $ ava_event = "firstpriority"
    $ asa_location = "hangar"
    $ asa_event = "defeatingthepirates"
    $ chi_location = "engineering"
    $ chi_event = "chigarafirstconvo"

    jump dispatch

label firstpriority:

    $ captaindeck = 1

    hide screen deck1

    scene bg bridge
    show ava uniform handonhip neutral
    with dissolve

    window show

    ava "The ship is at your command, captain."

    menu:
        "What do you think our next move should be?":
            jump firstprioritytofindryders
        "What's the ship's status?":
            jump readytosetsailcommand
        "Carry on, Ava.":
            jump dispatch

label firstprioritytofindryders:

    ava "First things first. Like you said, the Sunrider's an assault carrier without any ryders. Our first priority should be to find pilots and ryders to fill up our empty hangar."
    kay "We already have one interested pilot."

    show ava uniform armscrossed frown with dissolve

    ava "You should be careful with that one. Asaga's the type of person that seeks out danger."
    kay "How do you even know that?"
    ava "Woman's intuition."
    kay "Huh, alright then."

    menu:
        "What's the ship's status?":
            jump readytosetsailcommand
        "Carry on, Ava.":
            jump dispatch

label readytosetsailcommand:

    show ava uniform handonhip neutral with dissolve

    ava "The repairs are already complete. We're ready to set sail as soon as you give the command."
    menu:
        "What do you think our next move should be?":
            jump firstprioritytofindryders
        "Carry on, Ava.":
            jump dispatch

label defeatingthepirates:

    $ captaindeck = 2

    hide screen deck2

    scene bg hangar
    show asaga plugsuit neutralalt smile
    with dissolve

    window show

    asa "Oh! Did you need me for something, capt'n?"

    menu:
        "How did you meet Chigara?":
            jump howdidyoumeetChigara
        "How's the Black Jack doing?":
            jump howstheBlackJackdoing
        "About joining the Sunrider...":
            jump aboutjoiningtheSunrider
        "That'll be all for now, Asaga. Try to stay out of trouble.":
            jump thatllbeallasagastayouttrouble

label howdidyoumeetChigara:

    $ ChigaraRefugee = True

    show asaga plugsuit armscrossed smile with dissolve

    asa "Me and Chigara go back pretty far. I think we met about five years ago, back when she was just a girl. Mmm... Well, I think she was a refugee from a planet that was destroyed in a natural disaster. Anyways, I saw a bunch of these dirty guys scaring her in the middle of the street, so I stepped in and tried to scare them away."
    kay "How'd that turn out?"
    asa "Eh-heh... Let's say that I kind of bit off more than I could chew. But I swear, I was gonna win in the end! Lucky for those guys though, Chigara pulled out a gadget that zapped them with electricity, so I didn't have to space them for good."

    menu:
        "You're lucky she was there to save you!":
            jump luckyshewastheretosave
        "So you rescued Chigara?":
            jump soyourescuedChigara

label luckyshewastheretosave:

    show asaga plugsuit armscrossed annoyed with dissolve

    asa "H-hey, like I said, I was gonna beat them in the end!"
    jump eversincethencomrades

label soyourescuedChigara:

    show asaga plugsuit armscrossed smile with dissolve

    asa "Yup, totally!"
    jump eversincethencomrades

label eversincethencomrades:

    show asaga plugsuit handsonhips happy with dissolve

    asa "And ever since then, we've been comrades in arms!"
    kay "(It feels like she skipped a few chapters of that story...)"
    kay "(Still, a refugee from a doomed world?  Maybe I should ask Chigara more about this.)"

    menu:
        "How's the Black Jack doing?":
            jump howstheBlackJackdoing
        "About joining the Sunrider...":
            jump aboutjoiningtheSunrider
        "That'll be all for now, Asaga. Try to stay out of trouble.":
            jump thatllbeallasagastayouttrouble

label howstheBlackJackdoing:

    show asaga plugsuit armscrossed confident with dissolve

    asa "Uwah-hah! Thanks for askin', but nothing ever troubles mah Black Jack! It's always in tiptop form!"
    asa "By the way, if you happen to get your hands on any ryder upgrades, feel free to arm it on the Black Jack, or on any other ryder the Sunrider's carrying. Although preferably on the Black Jack."
    kay "How do we get ryder upgrades?"

    show asaga plugsuit thinking lookleft with dissolve

    asa "Well, most of the time I just ask Chigara to research some upgrades for me. It takes some money, but it's a pretty reliable way of getting upgrades!"

    menu:
        "How did you meet Chigara?":
            jump howdidyoumeetChigara
        "About joining the Sunrider...":
            jump aboutjoiningtheSunrider
        "That'll be all for now, Asaga. Try to stay out of trouble.":
            jump thatllbeallasagastayouttrouble

label aboutjoiningtheSunrider:

    show asaga plugsuit excited happy with dissolve

    asa "So, are you willing to help, capt'n? If you help me take out the pirates, I'll join you guys on board the Sunrider!"

    menu:
        "Why do you want to join the Sunrider?":
            jump whyjoinSunrider
        "Tell me more about the pirates you're after.":
            jump tellmoreaboutpirates
        "I think I'll have to think about it more...":
            jump illhavetothinkmore
        "All right, you've got a deal.":
            jump youvegotadeal

label whyjoinSunrider:

    show asaga plugsuit vpose with dissolve

    asa "For the adventure, of course! And the excitement!"
    kay "Really, is that all?"

    show asaga plugsuit armscrossed smile with dissolve

    asa "Well, you're headed after PACT, right?"
    kay "PACT's conquered our home. Of course we're after them."
    asa "Well, maybe I want to help out. If we don't do anything, PACT's going to take over the galaxy. And that's not just bad for us. That's going to be bad for anyone who cares about freedom and justice."

    menu:
        "I couldn't agree more.":
            jump couldntagreemore

        "What's your grudge against PACT?":
            jump whatsgrudgeagainstPACT

label couldntagreemore:

    show asaga plugsuit armscrossed confident with dissolve

    asa "Eh-heh... I knew we'd think alike from the moment I met you, capt'n."

    menu:
        "Tell me more about the pirates you're after.":
            jump tellmoreaboutpirates
        "I think I'll have to think about it more...":
            jump illhavetothinkmore
        "All right, you've got a deal.":
            jump youvegotadeal

label whatsgrudgeagainstPACT:

    show asaga plugsuit thinking content with dissolve

    asa "Mmm... Well, nothing as big as having my planet conquered by them. It's... Uhh... Something more personal."

    show asaga plugsuit excited happy with dissolve

    asa "Anyways, let's just say I'm doing it for the heroics!"

    menu:
        "Tell me more about the pirates you're after.":
            jump tellmoreaboutpirates
        "I think I'll have to think about it more...":
            jump illhavetothinkmore
        "All right, you've got a deal.":
            jump youvegotadeal

label tellmoreaboutpirates:

    show asaga plugsuit armscrossed mad with dissolve

    asa "They've been terrorizing this sector for the past year. Merchants, military, even unarmed civilians. Nobody's safe from them."
    asa "Now that kind of thing just makes my blood boil! I say we go and take the fight to them!"
    asa "There's a pirate's nest hidden in the Tydarian asteroid field where they operate from. We can take the Sunrider and mess that nest up! That'll show them not to pick on civilians!"
    kay "And also get you your payment from the Mining Union?"

    show asaga plugsuit armscrossed content with dissolve

    asa "Eh-heh, that too. Hey, everyone's got to make a living!"

    menu:
        "Why do you want to join the Sunrider?":
            jump whyjoinSunrider
        "I think I'll have to think about it more...":
            jump illhavetothinkmore
        "All right, you've got a deal.":
            jump youvegotadeal

label illhavetothinkmore:

    show asaga plugsuit neutralalt smile with dissolve

    asa "Well, don't wait too long, capt'n! Each moment that passes is more time for PACT to get stronger!"

    menu:
        "How did you meet Chigara?":
            jump howdidyoumeetChigara
        "How's the Black Jack doing?":
            jump howstheBlackJackdoing
        "About joining the Sunrider...":
            jump aboutjoiningtheSunrider
        "That'll be all for now, Asaga. Try to stay out of trouble.":
            jump thatllbeallasagastayouttrouble


label youvegotadeal:

    $ pro_location = "bridge"
    $ pro_event = "attackonpiratesnest"

    show asaga plugsuit armscrossed confident with dissolve

    asa "Eh-heh... I knew you'd agree, capt'n."

    show asaga plugsuit excited happy with dissolve

    asa "Don't worry, don't worry! We'll whack those pirates in no time at all, and then attend to your PACT problem together."
    kay "Welcome to the team, Asaga."

    show asaga plugsuit handsonhips happy with dissolve

    asa "I won't let you down, capt'n! Ah-hahahaha!"

    menu:
        "That'll be all for now, Asaga. Try to stay out of trouble.":
            jump thatllbeallasagastayouttrouble

label thatllbeallasagastayouttrouble:

    jump dispatch

label chigarafirstconvo:


    $ captaindeck = 1
    hide screen deck1

    scene bg engineering
    show chigara plugsuitlabcoat holdingipad surprise
    with dissolve

    window show

    chi "E-eah! Oh, sorry, Captain Shields, I didn't see you coming."
    kay "Sorry for surprising you."

    show chigara plugsuitlabcoat holdingipad curious with dissolve

    chi "Was there something you needed?"

    if ChigaraRefugee:
        menu:
            "So you made the Black Jack yourself?":
                jump youmadeblackjackyourself

            "Do you also pilot a ryder, Chigara?":
                jump youalsopilotryder

            "I heard from Asaga you were a refugee.":
                jump asagayouwerearefugee

            "Where did you learn to work with machines like that?":
                jump wherelearnmachinelikethat

            "Thanks Chigara. That'll be all for now.":
                jump thanksallfornow

    menu:
        "So you made the Black Jack yourself?":
            jump youmadeblackjackyourself

        "Do you also pilot a ryder, Chigara?":
            jump youalsopilotryder

        "Where did you learn to work with machines like that?":
            jump wherelearnmachinelikethat

        "Thanks Chigara. That'll be all for now.":
            jump thanksallfornow

label youmadeblackjackyourself:

    show chigara plugsuitlabcoat holdingipad smile with dissolve

    chi "That's correct. Asaga used to pilot around a military surplus fighter that she put together from a junk heap. I used to be worried sick that it'd fall apart, so I decided that I'd build a new ryder for her."
    kay "The Black Jack's unlike anything I've seen in my life. You know, if you worked for a engineering company, you could change the galaxy."

    show chigara plugsuitlabcoat holdingipad sad with dissolve

    chi "Ah... But then I wouldn't be able to open my bakery..."

    if ChigaraRefugee:
        menu:

            "Do you also pilot a ryder, Chigara?":
                jump youalsopilotryder

            "I heard from Asaga you were a refugee.":
                jump asagayouwerearefugee

            "Where did you learn to work with machines like that?":
                jump wherelearnmachinelikethat

            "Thanks Chigara. That'll be all for now.":
                jump thanksallfornow

    menu:
        "Do you also pilot a ryder, Chigara?":
            jump youalsopilotryder

        "Where did you learn to work with machines like that?":
            jump wherelearnmachinelikethat

        "Thanks Chigara. That'll be all for now.":
            jump thanksallfornow

label youalsopilotryder:

    show chigara plugsuitlabcoat holdingipad smile with dissolve

    chi "I do. The Liberty's a support ryder though, so I usually fly as Asaga's wing mate and provide her with support. That's only for really tough missions though. Usually, the Black Jack's strong enough to fly by itself."
    kay "The Liberty, huh... Did you also make that yourself?"
    chi "Uh-huh. They're both my creations."
    kay "We could sure use more ryders... I don't suppose we could also bring the Liberty on board?"

    show chigara plugsuitlabcoat holdingipad forcedsmile with dissolve

    chi "Eh-heh... About that..."
    chi "Asaga's been pumped up about attacking the pirates, so she's already arranged to bring the Liberty here."
    kay "Really? Shesh, nobody's told me about that, and I'm supposed to be the captain."

    if ChigaraRefugee:
        menu:
            "So you made the Black Jack yourself?":
                jump youmadeblackjackyourself

            "I heard from Asaga you were a refugee.":
                jump asagayouwerearefugee

            "Where did you learn to work with machines like that?":
                jump wherelearnmachinelikethat

            "Thanks Chigara. That'll be all for now.":
                jump thanksallfornow

    menu:
        "So you made the Black Jack yourself?":
            jump youmadeblackjackyourself

        "Where did you learn to work with machines like that?":
            jump wherelearnmachinelikethat

        "Thanks Chigara. That'll be all for now.":
            jump thanksallfornow

label asagayouwerearefugee:

    show chigara plugsuitlabcoat holdingipad neutral with dissolve

    chi "Ah, that's right. I used to be a refugee from the planet Diode."
    kay "Diode... I remember hearing about the Diode catastrophe about six years ago. Didn't a science experiment go terribly wrong and open a micro black hole on the planet?"

    show chigara plugsuitlabcoat holdingipad sad with dissolve

    chi "It was a terrible event..."
    chi "Ever since that happened, I've been on my own. Well, at least until Asaga found me."
    chi "I'm sorry. I don't really like talking about what happened that day."
    kay "Sorry, I didn't mean to pry."

    menu:
        "So you made the Black Jack yourself?":
            jump youmadeblackjackyourself

        "Do you also pilot a ryder, Chigara?":
            jump youalsopilotryder

        "Where did you learn to work with machines like that?":
            jump wherelearnmachinelikethat

        "Thanks Chigara. That'll be all for now.":
            jump thanksallfornow

label wherelearnmachinelikethat:

    show chigara plugsuitlabcoat holdingipad neutral with dissolve

    chi "My people were always experts with technology. I guess it's because I've been trained since I was really little."
    chi "Unfortunately, there's not many of us left now, so it must seem really amazing to you. But back home, I wasn't even that amazing with science."

    show chigara plugsuitlabcoat holdingipad reminsice with dissolve

    chi "Eh-heh... You should have seen my parents. They were really amazing."
    kay "What did your parents do?"
    chi "They were researching some incredible things. Technology to bring people back from the dead. To synthesize complicated machinery from thin air. To tell the truth, compared to what they were making, what I'm doing here is really only child's play."

    if ChigaraRefugee:
        menu:
            "So you made the Black Jack yourself?":
                jump youmadeblackjackyourself

            "Do you also pilot a ryder, Chigara?":
                jump youalsopilotryder

            "I heard from Asaga you were a refugee.":
                jump asagayouwerearefugee

            "Thanks Chigara. That'll be all for now.":
                jump thanksallfornow

    menu:
        "So you made the Black Jack yourself?":
            jump youmadeblackjackyourself

        "Do you also pilot a ryder, Chigara?":
            jump youalsopilotryder

        "Thanks Chigara. That'll be all for now.":
            jump thanksallfornow

label thanksallfornow:

    jump dispatch


label attackonpiratesnest:

    hide screen deck1

    play music "Music/Mission_Briefing.ogg" fadeout 1.5

    scene bg bridge
    show asaga plugsuit altneutral neutral:
        xzoom -1 xpos 0.2
    show ava uniform alt neutral neutral
    show chigara plugsuitlabcoat altneutral neutral:
        xpos 0.8
    with dissolve

    window show

    kay "Bring me up to date on our situation."

    show ava uniform handonhip neutral with dissolve

    ava "Cosette's pirates are operating from an asteroid base near Tydaria's moon."
    ava "Even with the help of our new pilots, the attack will not be easy."
    ava "The base itself has been built into an asteroid which the pirates dug out, then reinforced with armor and decked out with weapons.  The asteroid base is impervious to most conventional weaponry as a result.  Not only that, but the asteroids surrounding the base will make a natural environment for ambush."
    kay "Just one problem after another…"

    show asaga plugsuit handsonhips happy with dissolve

    asa "Don't worry, captain! These pirates are cowards. They're only used to fighting unarmed civilians and ragtag freelancers.  They'll be shakin' in their boots once they see the Sunrider barreling towards them!"

    show ava uniform armscrossed neutral with dissolve

    ava "Regardless, we should prepare the Sunrider's systems to the utmost before attempting any operation against the pirate's nest.  This is where our new guest comes in."

    show chigara plugsuitlabcoat altneutral forcedsmile with dissolve

    chi "O-oh… H-hello everyone."

    show chigara plugsuitlabcoat holdingipad smile with dissolve

    chi "I've been working on getting the Sunrider's Research and Development Lab operational.  I'd say that we're just about ready to open our doors."
    chi "From now, you'll be able to allocate funding to research new technologies, captain.  Just speak with me in the Lab and I can get started."
    kay "Sounds good. But where are we going to get the money for that?"

    show ava uniform handonhip neutral with dissolve

    ava "Missions. There're a lot of people out there in the galaxy who need a helping hand. If we sort their problems out, usually through judicious application of our main cannon, then we can be paid in return."
    kay "So we'll essentially be freelancing ourselves, huh? All right."

    ava "I've already prepared a potential mission for you, captain."
    ava "There's a PACT communications spire near us, which has been coordinating nearly 35 percent of their military efforts in the Neutral Rim.  Normally, it'd be guarded by an entire fleet, but we've hit a stroke of good luck."
    ava "An ion storm delayed the arrival of the spire's guardian fleet during a switchover, and now the communication spire is undefended.  If we were to warp in and destroy it, we could throw a wrench into all of PACT's war efforts in the Neutral Rim.  And not only that, the leaders of at least three neutral worlds would pay us handsomely."

    show asaga plugsuit altneutral neutral with dissolve

    asa "Hang on, capt'n. I have something else for you too."
    asa "There's been a band of particularly nasty thugs who've been kidnapping girls from Tydaria and selling them into the slave trade."
    kay "More of Cosette's goons?"

    show asaga plugsuit armscrossed mad with dissolve

    asa "Nah, these guys are something else. At least Cosette sticks to just killing and smuggling weapons."

    show ava uniform armscrossed lookleftmouthopen with dissolve

    ava "Human traffickers, captain. Out here, the laws protecting human dignity don't amount to much."
    asa "I just got a tip from a friend in the Tydarian government that their raiding party's been spotted in the Astral Expanse.  If we get there in time, we might still be able to catch them and put an end to their operation for good!"
    ava "Captain, as much as the trafficking of innocent girls aches our collective conscience, we have a war to win against PACT.  That communication spire's clearly more important than getting rid of some low life perverts."

    show asaga plugsuit excited angry with dissolve

    asa "But they're kidnapping innocents and selling them into the slave trade! Come on, captain, we can't just forget about them!"
    ava "Hmph. Whichever you choose captain, remember that time is of the essence for some missions.  We only have a limited window of time to perform side missions, so be sure to choose wisely which mission to undertake."
    ava "It is also in your discretion to ignore side missions and focus on our main objectives as well."
    kay "All right. I'll think on it and see what I can do."

    $ captaindeck = 1
    $ asa_location = None
    $ chi_location = "lab"
    $ chi_event = "researchanddevelopment"
    $ ava_location = "captainsloft"
    $ ava_event = "meetsophita"
    $ pro_location = None
    $ gal_location = "bridge"
    $ gal_event = "jumptogalaxy"

    $ warpto_astralexpanse = True
    $ warpto_pactstation1 = True

    $ mission_pirateattack = True

    $ liberty_weapons = [LibertyLaser(),Repair(),AccUp(),Disable(),FlakOff(),ShutOff()]
    $ liberty = create_ship(Liberty(),(5,7),liberty_weapons)
    $ sunrider.register_weapon(SunriderPulse()) #add a new weapon

    jump dispatch

label jumptogalaxy:

    hide screen deck1
    with dissolve
    jump galaxymap

label meetsophita:

    $ captaindeck = 0

    hide screen deck0

    scene bg captainsoffice
    show ava uniform handonhip neutral
    with dissolve

    window show

    ava "Captain, I have news for you."
    kay "What is it?"
    ava "I've received a message from the Mining Union. It seems that they're interested in speaking to you."
    kay "Any thoughts on what they want from us?"

    show ava uniform alt neutral neutral with dissolve

    ava "The Mining Union is one of the biggest private corporations in the galaxy. They control nearly every stage of the mining process, from the extraction of ores from the rock bed, to the refinement of those ores into starship grade steel. Last time I checked, the Mining Union provides the steel for nearly half the galaxy's navies."
    kay "So they stand to profit the most from a war, huh. How do I contact them?"
    ava "Your office is equipped with a FTL transponder.  You'll be able to make real time holographic calls from your office to anywhere else in the galaxy with it."
    ava "I'll update your address book with the Mining Union's representative.  It's a woman named Sophita Brooks.  You can also make FTL calls to anyone else on your address book from your office."
    kay "All right, thanks."

    $ ava_location = None
    $ cal_location = "captainsloft"
    $ cal_event = "introsophita"

    menu:
        "(Use FTL Transponder)":
            jump FTLTransponderintro

        "(Return to ship map)":
            jump dispatch

label FTLTransponderintro:

    menu:
        "(Call Sopita Brooks)":
            jump introsophita
        "(Return)":
            jump dispatch

label introsophita:

    scene bg captainsoffice with dissolve

    $ cal_location = "captainsloft"
    $ cal_event = "ftltransponder"

    show sophita with dissolve

    sop "Captain. I'm pleased to make your acquaintance.  I am Sophita Brooks, vice secretary of operations."
    kay "Captain Kayto Shields of the starship Sunrider. And to what do I owe the pleasure?"
    sop "I come to you with a business opportunity. We at the Union are always eager to seek new partners. And certainly, the opportunity to work with the captain of a prototype warship does not come often."
    kay "I'm listening."
    sop "We've forwarded you a list of contracts.  If you wish, you may seek to undertake them. And of course, we will provide you with fair compensation for your efforts if you choose to undertake them."
    kay "Contracts? Of what sort?"
    sop "Of the sort requiring a big stick, captain. I'll leave it to you to figure out what I mean."
    sop "Further, if you wish to trade with us, I am available as your contact as well."
    kay "What do you have for sale?"
    sop "Proton torpedoes, tactical nuclear warheads, and all the other necessities of modern life."
    sop "Also, during our excavations, sometimes we find... shall we say, interesting artifacts.  While they're quite old, I am told they still possess impressive powers."
    kay "(Ancient artifacts... Could she be referring to lost technology?)"
    sop "I see I have your attention now, captain."
    sop "If you have the money, we will deliver these artifacts for your personal use. I'm sure that you will find them to be most helpful."
    kay "I'll keep that in mind."
    sop "Just remember, the Union will always be available to help - provided you have the money and the will."
    kay "The only two forces in the galaxy greater than any warship."
    sop "I see we are on the same page than."

    menu:
        "Show me what you have for sale.":
            jump unionstore
        "Good bye.":
            jump dispatch

label ftltransponder:

    hide screen ship_map
    jump unionstore

label unionstore:

    scene store_back with dissolve
    window hide

    $sunrider_rocket = sunrider.weapons[3]

    call screen store_union
    hide screen store_rocket

label researchanddevelopment:

    $ captaindeck = 1

    hide screen deck1

    scene bg lab

    show chigara plugsuitlabcoat holdingipad neutral with dissolve

    chi "Welcome to research and development, captain.  Is there anything I can help you with?"

    menu:
        "Let me allocate our funds.":
            jump allocatefunds

        "Nothing right now.":
            jump dispatch

label allocatefunds:

    window hide

    python:
        BM.active_upgrade = None
        config.rollback_enabled = False
        buy_upgrades()
        renpy.block_rollback()
        config.rollback_enabled = True
        captaindeck = 1

    jump dispatch

label humantraffickers:

    $ Random = renpy.random.randint(1,9)

    if Random == 1:
        scene space back1
    if Random == 2:
        scene space back2
    if Random == 3:
        scene space back3
    if Random == 4:
        scene space back4
    if Random == 5:
        scene space back5
    if Random == 6:
        scene space back6
    if Random == 7:
        scene space back7
    if Random == 8:
        scene space back8
    if Random == 9:
        scene space back9

    show sunrider_warpout_standard:
        xpos 700 ypos 350
    with dissolve

    pause 1.0

    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_standard_flash:
        xpos 426 ypos 0 alpha 0
        linear 0.1 alpha 1
        linear 0.1 alpha 0
    show sunrider_warpout_standard out:
        xpos 700 ypos 350
        ease 0.2 xpos 200 ypos 300 zoom 0

    pause 1.0

    scene bg bridge

    show ava uniform handsonhips neutral with dissolve

    ava "Warp complete, captain. We're arriving at the Astral Expanse."
    kay "Scan for unregistered starships. They couldn't have gotten very far away."

    show ava uniform alt neutral mad with dissolve

    ava "Pirate signatures detected up ahead! It's the traffickers!"

    play sound "sound/redalert.ogg"
    scene bg bridgered
    show ava uniform alt neutral mad
    with dissolve

    kay "All hands, red alert! Set in an intercept course! Let's take these bastards out!"

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    scene bg bridgered:
        xalign 0.5
        ease 0.025 xalign 0.45
        ease 0.05 xalign 0.55
        ease 0.025 xalign 0.5
        repeat 2
    show ava uniform alt neutral mad:
        xalign 0.5
        ease 0.025 xalign 0.45
        ease 0.05 xalign 0.55
        ease 0.025 xalign 0.5
        repeat 2
    show battlewarning:
        xpos 0.5 ypos 0.5
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide battlewarning

    call mission3_inits
    $ BM.mission = 3
    $ check1 = False
    jump battle_start

label mission3:

    if check1 == False:
        $BM.draggable = False

        show chigara plugsuit altneutral neutral onlayer screens:
            xpos 0.2 xzoom -1
        with dissolve

        chi "Ah captain.  The Liberty is capable of generating a small energy field."
        chi "Energy fields provide protection against laser based weapons for all units within the blue field indicated on the map."
        chi "Using allied defenses while exploiting weaknesses in the enemy's defenses is essential to winning."
        chi "No defense is perfect though, so make sure you exploit the holes in the enemy's defenses by using the best weapon type for the situation."

        hide chigara onlayer screens with dissolve

        $ check1 = True

        $ BM.draggable = True

    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission3 #loop back
    else:
        pass #continue down to the next label

label aftermission3cutscene:

    $ captain_moralist += 5
    $ affection_asaga += 3

    stop music fadeout 1.5
    hide screen commands
    hide screen battle_screen

    scene bg bridgered with dissolve
    play music "Music/WorldBuilder.ogg"  fadeout 1.5    #this was missing, so I added it. not sure if it's the right song

    window show

    show ava uniform handonhip neutral with dissolve

    ava "Captain, some of the traffickers have managed to survive on escape pods.  They have dropped a distress beacon and are requesting relief.  What are your orders?"

    show asaga plugsuit armscrossed evil:
        xpos 0.2
    with wipedown

    asa "Eh-heh, serves 'em right!  Let's make an example of them and space them for good!"

    show chigara plugsuit handonchest sad:
        xpos 0.8
    with wipedown

    chi "A-ah... But shouldn't we turn them over to the authorities on Tydaria instead?"

    show ava uniform armscrossed frown with dissolve

    ava "The Tydarian justice system is underfunded as it is.  It'll be years until these traffickers face trial.  I say we speed the process up by leaving them here to their fates."

    menu:
        "We still have an obligation to the law.  Pick them up and lock them in the brig.":
            jump leavethemtydarianauthorities

        "Let them get a taste of their own medicine.  Jam the distress beacon and get us out of here.":
            jump jamdistressbeaconleave

label leavethemtydarianauthorities:

    $ affection_chigara += 1

    show ava uniform alt neutral neutral with dissolve

    ava "Aye captain.  I'll inform security to prepare to take in some prisoners."

    show asaga plugsuit excited angry with dissolve

    asa "But captain, these guys could just bribe themselves out of jail!  They're too dangerous to let live!"
    kay "Killing these people in cold blood won't put us in the right, Asaga. The justice system will deal with these crooks.  Not our guns."

    show asaga plugsuit armscrossed frustrated with dissolve

    asa "Arrgghh, all right, all right, you're right."

    show chigara plugsuit handstogether forcedsmile with dissolve

    chi "Asaga can get a little too excited at times, especially when people are being hurt.  I'm glad you're here to keep her on the right path, captain."

    jump mission3complete

label jamdistressbeaconleave:

    $ affection_ava += 1
    $ affection_asaga += 1

    show ava uniform alt neutral neutral with dissolve

    ava "Aye captain.  All ryders, return home.  Let's get out of here."

    show asaga plugsuit armscrossed evilgrin with dissolve

    asa "Heh heh, I jammed their beacon.  I hope these guys get what's coming!"

    show chigara plugsuit twidlefingers scared with dissolve

    chi "Oh dear, oh dear..."

    jump mission3complete

label mission3complete:

    $ mission3_complete = True

    jump dispatch

label pactstationattack:

    $ Random = renpy.random.randint(1,9)

    if Random == 1:
        scene space back1
    if Random == 2:
        scene space back2
    if Random == 3:
        scene space back3
    if Random == 4:
        scene space back4
    if Random == 5:
        scene space back5
    if Random == 6:
        scene space back6
    if Random == 7:
        scene space back7
    if Random == 8:
        scene space back8
    if Random == 9:
        scene space back9

    show sunrider_warpout_standard:
        xpos 700 ypos 350
    with dissolve

    pause 1.0

    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_standard_flash:
        xpos 426 ypos 0 alpha 0
        linear 0.1 alpha 1
        linear 0.1 alpha 0
    show sunrider_warpout_standard out:
        xpos 700 ypos 350
        ease 0.2 xpos 200 ypos 300 zoom 0

    pause 1.0

    scene bg bridge with dissolve

    window show

    show ava uniform handonhip mad with dissolve

    ava "Warp complete, captain.  The spire is right up ahead."
    ava "Warning, PACT signatures. The spire is being protected by squad of ships led by a PACT cruiser."
    kay "A cruiser? I thought you said this thing was undefended!"

    show ava uniform armscrossed neutral with dissolve

    ava "A single cruiser is undefended, captain.  Normally, there'd be an entire fleet surrounding the spire."
    ava "Be careful - that spire's decked out with rail guns. Our scans indicate that it's out of missiles though. Let's try taking it out from a distance."
    kay "All right. Asaga, Chigara, are you ready down there?"

    show asaga plugsuit neutralalt alert:
        xzoom -1 xpos 0.2
    with wipedown

    asa "On your word, capt'n! Let's take these guys out!"

    show chigara plugsuit excited scared:
        xpos 0.8
    with wipedown

    chi "I-I'll try my best, captain!"

    play sound "sound/redalert.ogg"
    scene bg bridgered
    show ava uniform armscrossed neutral
    show asaga plugsuit neutralalt alert:
        xzoom -1 xpos 0.2
    show chigara plugsuit neutral scared:
        xpos 0.8
    with dissolve

    kay "All hands, battle stations!"

    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    show battlewarning:
        xpos 0.5 ypos 0.5
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide asaga
    hide chigara
    hide battlewarning

    call mission4_inits
    $ BM.mission = 4
    $ battle_check1 = False
    jump battle_start

label mission4:

    if battle_check1 == False:

        $BM.draggable = False

        show ava uniform handonhip mad onlayer screens zorder 50 with dissolve

        ava "This is a hit and run operation, captain.  Our primary objective is the destruction of the PACT spire.  All other enemy units are secondary targets."
        kay "All right.  All units, focus on the spire!  Try to minimize combat with the escort fleet!"

        play sound "Sound/objectives.ogg"
        "Objective: Destroy the PACT Spire"

        hide ava onlayer screens with dissolve

        show chigara plugsuit altneutral neutral onlayer screens:
            xpos 0.2 xzoom -1
        with dissolve

        chi "Ah captain.  The Liberty is capable of generating a small energy field."
        chi "Energy fields provide protection against laser based weapons for all units within the blue field indicated on the map."
        chi "Using allied defenses while exploiting weaknesses in the enemy's defenses is essential to winning."
        chi "No defense is perfect though, so make sure you exploit the holes in the enemy's defenses by using the best weapon type for the situation."

        hide chigara onlayer screens with dissolve

        $ battle_check1 = True

        $ BM.draggable = True

    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission4 #loop back
    else:
        pass #continue down to the next label

label mission4_end:

    $ mission4_complete = True

    hide screen battle_screen
    hide screen commands

    play music "Music/WorldBuilder.ogg" fadeout 1.5

    scene bg bridgered
    show ava uniform fistup yes
    with dissolve

    window show

    ava "The spire has been destroyed! The mission is accomplished!"
    kay "All units, return to the Sunrider! Let's get out of here before PACT realizes what's going on and sends reinforcements."

    hide ava with dissolve
    show asaga plugsuit handsonhips grin with wipedown

    asa "Understood, captain! All wings are returning home. We did it!"

    $ Random = renpy.random.randint(1,9)

    if Random == 1:
        scene space back1
    if Random == 2:
        scene space back2
    if Random == 3:
        scene space back3
    if Random == 4:
        scene space back4
    if Random == 5:
        scene space back5
    if Random == 6:
        scene space back6
    if Random == 7:
        scene space back7
    if Random == 8:
        scene space back8
    if Random == 9:
        scene space back9

    show sunrider_warpout_standard:
        xpos 700 ypos 350
    with dissolve

    pause 1.0

    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_standard_flash:
        xpos 426 ypos 0 alpha 0
        linear 0.1 alpha 1
        linear 0.1 alpha 0
    show sunrider_warpout_standard out:
        xpos 700 ypos 350
        ease 0.2 xpos 200 ypos 300 zoom 0

    pause 1.0

    $ captaindeck = 1
    $ warpto_pactstation1 = False

    jump dispatch

label piratebaseattack:

    $ Random = renpy.random.randint(1,9)

    if Random == 1:
        scene space back1
    if Random == 2:
        scene space back2
    if Random == 3:
        scene space back3
    if Random == 4:
        scene space back4
    if Random == 5:
        scene space back5
    if Random == 6:
        scene space back6
    if Random == 7:
        scene space back7
    if Random == 8:
        scene space back8
    if Random == 9:
        scene space back9

    show sunrider_warpout_standard:
        xpos 700 ypos 350
    with dissolve

    pause 1.0

    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_standard_flash:
        xpos 426 ypos 0 alpha 0
        linear 0.1 alpha 1
        linear 0.1 alpha 0
    show sunrider_warpout_standard out:
        xpos 700 ypos 350
        ease 0.2 xpos 200 ypos 300 zoom 0

    pause 1.0

    scene asteroid back1:
        yanchor 0 ypos 0
        ease 1.5 ypos -200
    with dissolve
    pause 1

    show sunrider_warpout_standard out:
        xpos 2300 ypos 1200 zoom 2
        ease 0.2 xpos 1000 ypos 500 zoom 0.5
    pause 0.2
    play sound "Sound/large_warpout.ogg"
    show cg_legionwarpin_missilefrigate_warpflash:
        zoom 1.5 xpos 1550 ypos 750
    show sunrider_warpout_standard

    pause 2.0

    scene bg bridge with fade
    window show

    show ava uniform alt neutral mad with dissolve

    ava "Warp successful. We've arrived at the Tydarian Asteroid Field."
    kay "All right everyone. Keep your eyes peeled for any pirate vessels. The rocks here are interfering with our scanners, so I'm 120 percent sure the pirates are waiting to ambush us."

    show asaga plugsuit excited happy:
        xpos 0.2
    with wipedown

    asa "Roger that! We're all ready down here in the hanger! Just give the word, capt'n!"

    show ava uniform alt neutral angry with dissolve

    ava "Alert. Enemies detected. Incoming pirate fleet!"

    show cosette plugsuit front evilsmile:
        xpos 0.8
    with wipedown

    cos "Huufufu... I didn't think anyone would be so bold as to attack our base. Show these whelps what happens when you cross Cosette Cosmos!"

    play sound "sound/redalert.ogg"
    scene bg bridgered
    show cosette plugsuit front evilsmile:
        xpos 0.8
    show asaga plugsuit excited happy:
        xpos 0.2
    show ava uniform alt neutral angry
    with dissolve

    kay "All hands! Battle stations!"

    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    show battlewarning:
        xpos 0.5 ypos 0.5
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide asaga
    hide cosette
    hide battlewarning

    call mission5_inits
    $ BM.mission = 5
    $ battle_check1 = False
    $ check2 = False
    jump battle_start

label mission5:

    $BM.battle_bg = "Background/asteroids3.jpg"

    if check2 == False:

        $BM.draggable = False
        show ava uniform handonhip neutral onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        ava "The time has come for you to issue executive orders, captain."
        ava "As you win battles, you gain command points based on your battlefield performance."
        ava "Those command points may be spent to issue powerful executive orders which can quickly change the tide of combat."
        ava "Simply select the orders tab at the top left side of the battle screen and then select the order you wish to issue."

        hide ava onlayer screens with dissolve

        $BM.draggable = True

        $ check2 = True

    if battle_check1 == False and BM.turn_count == 5:

        $BM.draggable = False
        show cosette plugsuit armscrossed angry onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        cos "What are you doing, you fools!  Kill them!"
        kay "Not this time, Cosette.  We're here to end your activities in this sector."

        show cosette plugsuit front evilsmile onlayer screens with dissolve

        cos "Heh-heh... You're a bold one..."

        show cosette plugsuit point yanderegrin onlayer screens with dissolve

        cos "But naive!"

        hide cosette onlayer screens with dissolve

        python:
            create_ship(PirateGrunt(),(17,6),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
            create_ship(PirateGrunt(),(17,5),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
            create_ship(PirateGrunt(),(17,7),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
            create_ship(PirateGrunt(),(17,4),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])

            create_ship(PirateBomber(),(18,6),[PirateBomberMissile(),PirateBomberRocket(),PirateBomberAssault()])
            create_ship(PirateBomber(),(18,5),[PirateBomberMissile(),PirateBomberRocket(),PirateBomberAssault()])

            create_ship(PirateDestroyer(),(12,1),[PirateDestroyerLaser(),PirateDestroyerKinetic()])
            create_ship(PirateDestroyer(),(12,10),[PirateDestroyerLaser(),PirateDestroyerKinetic()])

        play sound "sound/Voice/Ava/Ava Others 4.ogg"
        $ PlayerTurnMusic = "music/Sora_no_Senritsu.ogg"

        $ BM.draggable = True
        $ battle_check1 = True

    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission5 #loop back
    else:
        pass #continue down to the next label

label mission5_end:

    $ mission5_complete = True
    $ mission_pirateattack = False

    hide screen battle_screen
    hide screen commands

    play music "Music/The_Beginning_Of_The_Adventure.ogg" fadeout 1.5

    scene bg bridge
    show ava uniform armscrossed smile
    with dissolve

    window show

    ava "I must say captain, I'm impressed. Perhaps we do stand a chance against PACT after all."

    menu:
        "Of course we do, Ava. This is only the beginning of our story.":
            jump onlythebeginningofstory

        "Don't let your guard down. We still have a lot of work ahead of us.":
            jump stillworkahead

label onlythebeginningofstory:

    ava "And I look forward to seeing how it'll continue."
    jump celebratehangar

label stillworkahead:

    show ava uniform salute talk with dissolve

    ava "Understood sir!"
    jump celebratehangar

label celebratehangar:

    show ava uniform neutral talk with dissolve

    ava "The girls should be in the hanger. You should go and celebrate with them."

    $ captaindeck = 1
    $ asa_location = "hangar"
    $ asa_event = "celebratepiratebase_asa"
    $ chi_location = None
    $ chi_event = None
    $ gal_location = None

    jump dispatch

label celebratepiratebase_asa:

    hide screen deck2

    $ asa_location = None
    $ asa_event = None

    scene bg hangar
    show asaga plugsuit excited happy
    with dissolve

    window show

    asa "Uwah-hahahaha! We did it, capt'n, we did it! That pirate's nest is history!"

    show asaga plugsuit neutralalt smile with dissolve

    asa "Eh-hehh... As promised, I'll be glad to join you aboard the Sunrider. If you've got a war against PACT, then sign me up!"
    kay "Good to hear that. PACT's empire is still getting stronger with each day. We'll need all the help we can get if we're going to stop them."

    show asaga plugsuit vpose with dissolve

    asa "Understood, capt'n! Asaga Oakrun at your service!"

    menu:
        "What do you think will happen to the pirates?":
            jump thinkwillhappenpirates
        "What's going to happen with Chigara?":
            jump goingtohappenwithChigara
        "Let's move on. We need to assign you a room on the Sunrider.":
            jump assignasagaroom

label assignasagaroom:

    show asaga plugsuit altneutral happy with dissolve

    asa "I'm lookin' forward to a bed! It gets so uncomfortable sleeping on the Black Jack sometimes..."
    kay "Ava can help you get moved in."
    asa "Oh, by the way, I think Chigara's wanted to talk to you. You should go speak to her!"

    $ chi_location = "hangar"
    $ chi_event = "celebratepiratebase_chi"
    $ captaindeck = 2

    jump dispatch

label thinkwillhappenpirates:

    show asaga plugsuit thinking content with dissolve

    asa "Without their pirate's nest, their activities in this sector are practically finished. But I don't think we've seen the last of them yet."
    asa "They've probably retreated deeper into uncolonized space to recoup and rebuild their fleet. Then they'll probably come back for revenge."
    kay "Sounds like we've made some enemies today."

    show asaga plugsuit excited happy with dissolve

    asa "Don't worry 'bout a thing! I'm sure we'll be able to take care of them if they ever decide to come back!"

    menu:
        "What's going to happen with Chigara?":
            jump goingtohappenwithChigara
        "Let's move on. We need to assign you a room on the Sunrider.":
            jump assignasagaroom

label goingtohappenwithChigara:

    show asaga plugsuit excited happy with dissolve

    asa "Oh! You should talk to her about that. I think she wanted to speak to you anyways."

    menu:
        "What do you think will happen to the pirates?":
            jump thinkwillhappenpirates
        "Let's move on. We need to assign you a room on the Sunrider.":
            jump assignasagaroom

label celebratepiratebase_chi:

    hide screen deck2

    scene bg hangar
    show chigara plugsuit handonchest smile
    with dissolve

    window show

    chi "Ah, captain. I'm back."
    kay "Welcome back, Chigara. You did good out there."

    show chigara plugsuit twiddlefingers embarrassed with dissolve

    chi "Eh-heh... Really? I wonder..."
    kay "What are your plans now?"

    show chigara plugsuit handstogether sad with dissolve

    chi "Umm... Well, I guess with Asaga gone, it's going to get more lonely."
    chi "And business hasn't been so good at the bakery either..."
    kay "You should join us on the Sunrider too. We could use an extra pilot like you."

    show chigara plugsuit palmsup surprise with dissolve

    chi "E-eh!? Really!? Is that allowed?"
    kay "Of course it is. I'm the captain."

    show chigara plugsuit handstogether smile with dissolve

    chi "Eh-heh... Well, I guess I don't really have a choice, do I? In that case, I'll be in your care from now on, captain."
    kay "Welcome to the Sunrider, Chigara."
    kay "I've got to go now. You can speak to Ava if you have any problems with moving in."
    chi "Understood, captain. I look forward to working with you."

    window hide

    stop music fadeout 1.5

    show eyecatch_top with eyecatch_wipe
    show eyecatch_bottom with eyecatch_wiperev
    show eyecatch_logo with dissolve
    $ renpy.pause (2.0)
    scene bg black2 with dissolvelong
    scene bg captainsoffice with dissolvelong

    window show

    play music "Music/The_Meteor.ogg"

    kay "Begin captain's log."
    kay "It's been a two weeks since we took down Cosette's base in the asteroids.  Since then, we've been chasing down minor criminals and undertaking hit and run attacks on PACT supply lines."
    kay "Despite our efforts, PACT's invasion of the Neutral Rim has continued unabated."
    kay "Six more governments have voluntarily joined PACT and two more have been conquered.  PACT's war machine has been indiscriminate, slaughtering both civilians and combatants alike."
    kay "In the mere month since Cera, millions more innocents have been murdered."
    kay "Unless something is done, the day when PACT rules the entire Neutral Rim appears to be fast approaching."

    play sound "sound/doorbell.ogg"

    "-Door bell-"
    kay "Come in."

    show ava uniform handonhip neutral with dissolve

    ava "Captain, we've just received an encrypted transmission."
    kay "Transmission? Where from?"
    ava "It's from the Solar Alliance.  Admiral Harold Grey is interested in speaking to you."
    kay "An audience with the admiral, huh?  I didn't realize we were so important already."
    ava "I've added the Admiral's line to your FTL transponder.  You can patch him through now."
    kay "All right, let's hear what the Admiral wants with us."

    $ badpolitics = False

    show ava uniform handonhip neutral:
        zoom 1.0
        ease 0.5 xpos 0.7
    pause 0.0001
    show grey:
        xpos 0.3
    with dissolve

    gre " Greetings, Captain of the Sunrider. I am Admiral Grey of the Alliance Space Force."
    kay "This is Captain Kayto Shields of the Cera Space Force.  This is my First Officer, Ava Crescentia.  What would the admiral of the Solar Alliance want with us?"
    gre " You must have my condolences for the loss of your great planet. It pains me to hear that another neutral world has fallen to PACT's war machine."
    kay "PACT must be stopped at all costs, admiral.  I am certain of this."
    gre " I understand you've been operating as a freelancer since your government's fall.  I've got a certain proposal that you might be interested in."
    kay "You've got my attention."
    kay "(Another interested client...  Being a mercenary armed with an assault carrier sure helps get business.)"
    gre "Our diplomats have been sent on a mission to the neutral world of Versta to convince its people to join the Alliance for quite some time."
    gre "Unfortunately, it does not seem like the mission was successful, and a PACT invasion fleet is rapidly approaching the world. I need you to go in there and get our men out before the PACT fleet finds them and kills them."
    gre "Of course, I will see to it that you and your crew are rewarded for your efforts."

    menu:
        "Why do you need us? Surely, the Alliance must have other ships up to the task.":
            jump othershipstask

        "Are the diplomats high ranking government officials? Why do you need them protected so much?":
            jump protectedsomuch

        "Is there really no hope of getting Versta to join the Alliance?":
            jump nohopejoin

        "You have a deal, admiral. Any mission against PACT is good in my book.":
            jump goodinbook

label othershipstask:

    gre " Unfortunately, because of the break down in talks, our military vessels are forbidden to enter Versta space. It is too dangerous getting the diplomats out without an armed escort, so we've had no choice but to resort to an unaligned vessel like the Sunrider."

    menu:
        "Are the diplomats high ranking government officials? Why do you need them protected so much?":
            jump protectedsomuch

        "Is there really no hope of getting Versta to join the Alliance?":
            jump nohopejoin

        "You have a deal, admiral. Any mission against PACT is good in my book.":
            jump goodinbook


label protectedsomuch:

    gre " Not per se. But an execution of our diplomats by PACT will be viewed by my government as an act of war, and the Alliance will have no choice but to declare war on PACT."
    gre "I've been ordered by President Alythe himself that an intergalactic war with PACT over a minor neutral rim world would be an unacceptable outcome."

    menu:
        "A devastating war between PACT and the Alliance now would cost the lives of billions. The Alliance should wait for a better moment to fight PACT.":
            jump matterforpoliticians

        "But PACT's going to take over the galaxy one way or another, admiral. The Alliance must stop them.":
            jump matterforpoliticians

label nohopejoin:

    gre " I'm afraid the latest reports from our negotiators have been grim. Now, Versta's in a state of total panic regarding the approaching invasion fleet, and they somehow think we're responsible for it."
    gre " My government views it as a lost cause and just want the diplomats pulled out before PACT gets their hands on them."

    menu:
        "Why do you need us? Surely, the Alliance must have other ships up to the task.":
            jump othershipstask

        "Are the diplomats high ranking government officials? Why do you need them protected so much?":
            jump protectedsomuch

        "You have a deal, admiral. Any mission against PACT is good in my book.":
            jump goodinbook

label matterforpoliticians:

    $ badpolitics = True

    gre " A matter for politicians to decide, unfortunately.  Hmph.  The President has ordered that we prevent an intergalactic war, so those are your directives."

    menu:
        "Why do you need us? Surely, the Alliance must have other ships up to the task.":
            jump othershipstask

        "Are the diplomats high ranking government officials? Why do you need them protected so much?":
            jump protectedsomuch

        "You have a deal, admiral. Any mission against PACT is good in my book.":
            jump goodinbook

label goodinbook:

    $ amissionforalliance = True

    gre " Good.  My staff have already mailed your First Officer with the details.  You have your orders, Sunrider. I expect results. Admiral Grey out."

    hide grey with dissolve
    show ava uniform handonhip neutral:
        zoom 1.0
        ease 0.5 xpos 0.5

    kay "A mission from the Alliance. Can't say I was expecting that."

    show ava uniform alt neutral neutral with dissolve

    ava "Times like this, almost everyone wants a hired gun.  Especially if you happen to have a very big gun.  At this rate, we might see a new golden age of privateering."
    kay "We might want to swap out your uniform with something more eye catching then.  Do you have the Pirate Commander design yet?"

    show ava uniform armscrossed frown with dissolve

    ava "No."

    if badpolitics == True:
        menu:

            "Tell me about the situation between the Alliance and PACT.":
                jump situationbetweenalliance

            "It doesn't sound like the admiral is a fan of his own government.":
                jump notfanofgov

            "Well, now we know our next step. Let's get underway to Versta.":
                jump getunderwayvesta

    menu:

        "Tell me about the situation between the Alliance and PACT.":
            jump situationbetweenalliance

        "Well, now we know our next step. Let's get underway to Versta.":
            jump getunderwayvesta

label notfanofgov:

    show ava uniform armscrossed neutral with dissolve

    ava "Hmm... I get the same feeling as well."
    ava "So far, the President of the Alliance has been avoiding war with PACT at all costs. But my sense is that the military establishment inside the Alliance is already gearing up for a war."
    kay "That makes sense. PACT intends to take over the galaxy one way or another. It's only matter of time until the Alliance will be forced into the fight."

    menu:

        "Tell me about the situation between the Alliance and PACT.":
            jump situationbetweenalliance

        "Well, now we know our next step. Let's get underway to Versta.":
            jump getunderwayvesta

label situationbetweenalliance:

    show ava uniform alt neutral neutral with dissolve

    ava "What do you want to know?"

    menu:
        "Tell me more about the Alliance.":
            jump tellmorealliance

        "Tell me more about PACT.":
            jump tellmorepact

        "The Alliance and PACT aren't at war yet?":
            jump alliancepactnowar

label tellmorealliance:

    ava "The Solar Alliance is the current power house of the galaxy. It's actually a military, economic, and research alliance between the planet of Solaris and numerous other worlds."
    kay "It doesn't sound like everyone wants to join the Alliance though."
    ava "Some planets simply wish to be left alone. The planets that make up the neutral rim are too far from Solaris and have so far avoided joining the Alliance. Cera was one of those planets."
    kay "Still, isn't the Alliance a democracy? What's so bad about it?"
    ava "A space democracy is a difficult thing to maintain. A single politician might need to represent over a billion citizens."
    ava "Recently, political deadlock has characterized the Alliance."
    ava "The United Universalist Party in the Solar Congress wishes to take the war path against PACT. Meanwhile, the Progress Party wishes a negotiated settlement."
    ava "Neither party has managed to get anything done because of their irreconcilable differences."
    ava "President Alythe has avoided war with PACT at all costs. Even though PACT continues to swallow up most of the neutral rim, the Alliance has done nothing about it."

    menu:
        "Tell me more about PACT.":
            jump tellmorepact

        "The Alliance and PACT aren't at war yet?":
            jump alliancepactnowar

        "Thanks for the history lesson. That's all I needed to know.":
            jump thankshistorylesson

label tellmorepact:

    ava "PACT, short for the People's Alliance for Common Treatment, was originally an independence movement which started at New Eden against the New Empire."
    ava "New Eden was a paradise planet which was rich in valuable resources. However, the rulers of the New Empire hoarded the planet's riches for themselves, while the masses lived in poverty."
    ava "Eventually, the division in wealth reached a critical point and the people of New Eden declared a revolution against their own rulers."
    kay "If they're an independence movement, then why are they trying to take over the galaxy now?"
    ava "The independence movement went horribly wrong shortly after PACT overthrew the New Empire. Extreme nationalism and paranoia set in."
    kay "So then what happened?"
    ava "A mysterious figure known as Veniczar Arcadius took power. Much about him is shrouded in mystery. He appears behind a mask at all times and speaks only through a computer."
    ava "During the war of independence, he was a heroic figure who freed his people. But after he took power, he became a different man."
    ava "Arcadius wielded the nationalism and the paranoia of his people and led them on a war path, beginning PACT's rapid expansion. You can see that today, as PACT conquers every planet in the neutral rim, one by one. Nobody really knows when they're going to stop."

    menu:
        "Tell me more about the Alliance.":
            jump tellmorealliance

        "The Alliance and PACT aren't at war yet?":
            jump alliancepactnowar

        "Thanks for the history lesson. That's all I needed to know.":
            jump thankshistorylesson

label alliancepactnowar:

    show ava uniform handonhip neutral with dissolve

    ava "No, but I wouldn't bet on that lasting. War between the two powers is all but inevitable, I would say."
    kay "What makes you say that?"
    ava "So far, PACT has only been hitting neutral rim planets that are far away from Solaris. Eventually though, the entire neutral rim is going to belong to PACT. And then who's PACT going to attack next?"
    kay "Right, I see your point."

    menu:
        "Tell me more about the Alliance.":
            jump tellmorealliance

        "Tell me more about PACT.":
            jump tellmorepact

        "Thanks for the history lesson. That's all I needed to know.":
            jump thankshistorylesson

label thankshistorylesson:

    if badpolitics == True:
        menu:

            "Tell me about the situation between the Alliance and PACT.":
                jump situationbetweenalliance

            "It doesn't sound like the admiral is a fan of his own government.":
                jump notfanofgov

            "Well, now we know our next step. Let's get underway to Versta.":
                jump getunderwayvesta

    menu:

        "Tell me about the situation between the Alliance and PACT.":
            jump situationbetweenalliance

        "Well, now we know our next step. Let's get underway to Versta.":
            jump getunderwayvesta

label getunderwayvesta:

    show ava uniform neutral neutral with dissolve

    ava "Understood captain."

    $ captaindeck = 0
    $ asa_location = None
    $ chi_location = None
    $ gal_location = "bridge"
    $ res_location = "lab"
    $ res_event = "allocatefunds"
    $ warpto_versta = True
    $ warpto_occupiedcera = True
    $ warpto_tydaria = True
    $ warpto_astralexpanse = True

    jump dispatch

label jumphotversta:

    $ Random = renpy.random.randint(1,9)

    if Random == 1:
        scene space back1
    if Random == 2:
        scene space back2
    if Random == 3:
        scene space back3
    if Random == 4:
        scene space back4
    if Random == 5:
        scene space back5
    if Random == 6:
        scene space back6
    if Random == 7:
        scene space back7
    if Random == 8:
        scene space back8
    if Random == 9:
        scene space back9

    show sunrider_warpout_standard:
        xpos 700 ypos 350
    with dissolve

    pause 1.0

    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_standard_flash:
        xpos 426 ypos 0 alpha 0
        linear 0.1 alpha 1
        linear 0.1 alpha 0
    show sunrider_warpout_standard out:
        xpos 700 ypos 350
        ease 0.2 xpos 200 ypos 300 zoom 0

    pause 1.0

    scene versta_approach:
        ypos 0
        ease 1.5 ypos -120
    with dissolve
    pause 1

    show sunrider_warpout_standard out:
        xpos 2300 ypos 1200 zoom 2
        ease 0.2 xpos 1000 ypos 500 zoom 0.5
    pause 0.2
    play sound "Sound/large_warpout.ogg"
    show cg_legionwarpin_missilefrigate_warpflash:
        zoom 1.5 xpos 1550 ypos 750
    show sunrider_warpout_standard

    pause 2.0


    scene bg bridge with fade
    show ava uniform alt neutral neutral with dissolve


    ava "We've arrived at the planet of Vesta."

    play music "Music/Driving_the_Top_Down.ogg" fadeout 1.5
    show ava uniform alt neutral angry

    ava "Wait a minute... Alert! Drop point is hot! I'm detecting PACT signatures all around us!"

    play sound "Sound/redalert.ogg"
    scene bg bridgered
    show ava uniform alt neutral angry
    with dissolve

    kay "Red alert! Scramble our ryders!"

    show asaga plugsuit excited happy:
        xpos 0.2
    with wipeup

    asa "We're ready at your command, capt'n! Just give the word!"
    kay "One hell of an entrance... All right everyone, let's take the enemy out!"

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    show layer master at shake1
    play sound "Sound/drum.ogg"
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide asaga
    hide battlewarning

    call mission6_inits
    $ BM.mission = 6
    $ check1 = False
    jump battle_start

label mission6:

    $BM.battle_bg = "Background/space7.jpg"

    if check1 == False and BM.turn_count == 2:

        $BM.draggable = False

        show ava uniform alt neutral angry onlayer screens zorder 50:
            xpos 0.8
        with dissolve

        ava "I'm detecting a new warp signature..."

        scene space back7 onlayer screens zorder 50 with dissolve
        pause 0.5

        play sound "sound/small_warpout.ogg"

        show phoenixwarpin onlayer screens zorder 50:
            xpos 1500 ypos 150 zoom 0.0
            ease 0.1 xpos 960 ypos 540 zoom 1.0
        pause 0.1
        hide phoenixwarpin onlayer screens zorder 50
        show white onlayer screens zorder 100:
            alpha 0
            ease 0.1 alpha 0.4
            ease 0.1 alpha 0
        show phoenixwarpout onlayer screens zorder 50

        pause 0.0001

        show ava uniform alt neutral angry onlayer screens zorder 50:
            xpos 0.8
        with dissolve

        ava "An unidentified ryder has just entered the battle!"
        kay "A ryder capable of warping...?"
        ava "It seems to be using some sort of booster pack..."
        kay "Flag?"
        ava "Unidentified... It doesn't match any of our pirate designs ..."

        play sound "sound/Laser 1.ogg"
        show phoenixwarpout laser onlayer screens zorder 50 with dissolve
        show phoenixwarpout onlayer screens zorder 50 with dissolve

        hide ava onlayer screens zorder 50
        show asaga plugsuit handsonhips surpriseangry onlayer screens zorder 50:
            xpos 0.8
        with dissolve

        asa "W-woah! W-whatever that is, it isn't friendly!"
        kay "Tsch... For now, treat it as a PACT special unit! Take it down along with the rest of the enemy!"

        hide asaga onlayer screens
        hide phoenixwarpout onlayer screens
        hide space back7 onlayer screens

        $ BM.draggable = True
        $ check1 = True

        show screen battle_screen

        python:
            create_ship(PhoenixBoaster(),(15,6),[PhoenixBoasterLaser(),PhoenixBoasterAssault()])

    $ BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission6 #loop back
    else:
        pass #continue down to the next label

label mission6victory:

    $ mission6_complete = True

    hide screen battle_screen
    hide screen commands

    scene bg bridgered
    show ava uniform neutral neutral
    with dissolve

    window show

    show asaga plugsuit excited happy:
        xpos 0.2 xzoom -1
    with wipeup

    asa "We did it! The PACT fleet's history!"

    show chigara plugsuit handonchest smile:
        xpos 0.8
    with wipeup

    chi "Ah... It looks like we won."

    show ava uniform armscrossed frown with dissolve

    ava "Don't celebrate just yet. That was too weak to have been the main invasion force. It was just an recon squad."
    kay "And now the enemy knows we're here."
    kay "Asaga, Chigara, return to the Sunrider for now."

    hide asaga with dissolve
    hide chigara with dissolve

    show ava uniform handonhip neutral with dissolve

    ava "Captain, I'm still reading the PACT special unit on scanners."
    kay "Left behind, huh... I guess it can't go anywhere without its warp booster."
    ava "Your orders?"
    kay "Disable it, and then get the Liberty to haul it to our hangar. I think we have ourselves our first PACT prisoner."

    show ava uniform salute neutral with dissolve

    ava "Understood captain."

    scene bg hangar with dissolve
    play music "Music/Mission_Briefing.ogg"
    show asaga plugsuit neutralalt alert with dissolve

    asa "Oh! Chigara tells me that we have a prisoner!"
    kay "Yeah."

    show asaga plugsuit armscrossed confident with dissolve

    asa "Uu-fufufu... So... You gonna interrogate the pilot? Throw 'em out the airlock if they don't spill all their secrets?"
    kay "Uhhh no, I was actually just planning on asking some questions and then turning him over to the Alliance after this is all done."

    show asaga plugsuit altneutral sad with dissolve

    asa "Aw, so much for how they do it on the holovision..."

    show ava uniform armscrossed frown:
        xpos 0.2
    with dissolve

    ava "Hmph. Stand back, everyone. This guy might be dangerous."

    show chigara plugsuit twiddlefingers scared:
        xpos 0.8
    with dissolve

    chi "Huu... I think I'll just watch from back here..."
    kay "Alright, open the ryder's hatch and get our prisoner out."

    show ava uniform armscrossed frown:
        zoom 1
        ease 0.5 xpos 0.4
    show asaga plugsuit altneutral sad:
        zoom 1
        ease 0.5 xpos 0.6
    show chigara plugsuit twiddlefingers scared:
        zoom 1
        ease 0.5 xpos 0.8
    pause 0.001
    show icari plugsuit neutral closedeyes:
        xpos 0.12
    with dissolve

    ica "... ... ..."

    show asaga plugsuit excited surprise with dissolve

    asa "O-oh! She's just a girl like us, Chigara!"

    show icari plugsuit neutral neutral with dissolve

    ica "Is this... a PACT vessel?"
    kay "No. I'm Captain Kayto Shields of the Cera Space Force. Welcome aboard the Sunrider."

    show icari plugsuit armscrossed neutral with dissolve

    ica "Cera? I thought you were conquered by PACT."
    kay "Not all of us. Who are you?"
    ica "Icari Isidolde. Private mercenary."
    kay "Were you hired by PACT?"

    show icari plugsuit armscrossed confident with dissolve

    ica "Heh... Nothing of the sort. Was on a mission. I can't tell you more than that."

    show ava uniform armscrossed frowntalk with dissolve

    ava "You're now our prisoner.  Put your hands up and turn over all your weapons."
    kay "Have security escort our guest to the brig.  We'll continue with our discussion there."

    scene bg brig
    show brigoverlay
    with dissolve
    show icari plugsuit armscrossed wait behind brigoverlay:
        xpos 0.3
    with dissolve
    show ava uniform alt neutral neutral:
        zoom 1.5 xpos 0.7 ypos 1.35
    with dissolve

    kay "How's our guest holding up, Ava?"

    show ava uniform armscrossed neutral with dissolve

    ava "Per protocol, we've scanned her for contraband.  We found enough assassination tools on her person to topple small governments.  I'd say we caught a professional hitman."
    kay "Anything identifying who she's working for?"
    ava "We scanned through the database on her ryder and all of her electronics and found nothing.  She's no amateur."
    kay "All right. Let's try talking to her."

    show icari plugsuit armscrossed frown with dissolve

    ica "Tsch. I sure hope you haven't dirtied up my ryder."
    kay "You don't need to worry about that. Why don't you avoid all this trouble by giving us some info?"

    show icari plugsuit handonhip lookawaysnide with dissolve

    ica "Heh, what do you want?"
    kay "Why'd you attack us? Are you working for PACT?"

    show icari plugsuit handonhip annoyedtalk with dissolve

    ica "I already told you, I don't work for those fanatics. Haven't you been listening?"
    ica "I attacked you because I thought you were PACT freelancers.  Last I heard, the entire Cera Space Force was impressed into the PACT Fleet and the few survivors became pirates or freelancers."
    ica "If you haven't noticed, this area of the galaxy's like the Wild Wild West. Plenty of guns for sale have thrown their lots with PACT nowadays, thinking that's the way the galaxy's gonna spin."

    show icari plugsuit handonhip lookawaysnide with dissolve

    ica "Heh, not if I have anything to say about it anyways."
    kay "You're no friend of PACT?"

    show icari plugsuit handonhip annoyedtalk with dissolve

    ica "No! Hate 'em. I would have busted up their whole fleet back there."

    show icari plugsuit armscrossed tsun with dissolve

    ica "If it weren't for you smashing up my booster anyways. Ugh..."
    kay "Well, at least we're on the same side then."

    show icari plugsuit handonhip annoyedtalk with dissolve

    ica "So are you going to tell me what a Cera captain's doing here?"

    show ava uniform alt neutral angry with dissolve

    ava "We're asking the questions here, not you."

    show icari plugsuit handonhip snide with dissolve

    ica "Heh, what, we're not here to become friends?"
    ica "C'mon captain, throw me something here. Aren't we going to work this out together?"
    kay "All right."
    kay "We're here on Alliance business.  We're doing a bit of freelancing ourselves."

    show icari plugsuit handonhip lookawaysnide with dissolve

    ica "Heh, interesting."
    kay "There, you have our secret. How about you tell me yours?"
    ica "... ... ..."

    show icari plugsuit armscrossed frown with dissolve

    ica "All right, captain. You've made your point. If I tell you mine, you're going to have to promise not to lay a finger on my Phoenix. Oh, and also to get your damned housewife's scowl out of my face."

    show ava uniform armscrossed frown with dissolve

    ava "Hmph."
    kay "All right.  I suppose we could lay off your ryder."

    show icari plugsuit armscrossed tsun with dissolve

    ica "I hope so."

    show icari plugsuit handonhip annoyedtalk with dissolve

    ica "You wouldn't have happened to have been hired by an Alliance admiral who looked like a grey old statue, would you?"
    kay "Well, he certainly was grey.  In more ways than one."

    show icari plugsuit handonhip snide with dissolve

    ica "Hahahaha.  That bastard hasn't changed a bit."
    kay "You know him?"
    ica "Know him? I've worked for him for ages."
    kay "Doing what?"
    ica "What do you think? If you want anything in this galaxy, you need some undesirables erased.  Oh, nothing terrible, mind you, the admiral's a pretty principled guy."
    ica "But you have a crazed criminal on the loose? Then you need my services."
    ica "Have a sleazy dictator whose been getting too out of hand? I can set that straight too.  Ongessite prices too high? I provide the stick - and the Admiral provides the carrots. If you catch my drift."
    kay "You're a contract assassin."
    ica "Let me guess, you're here about the diplomats on Versta right?"
    kay "Looks like the big secret's out."

    show icari plugsuit armscrossed confident with dissolve

    ica "Heh."
    kay "What's a contract assassin like you doing here then?  Versta's a rescue mission.  Nobody needs to be shot."

    show icari plugsuit neutral snide with dissolve

    ica "Rescue mission? Is that what the Admiral told you?"

    show ava uniform armscrossed frowntalk with dissolve

    ava "If you know something, you better spill it."
    ica "Not so fast.  That little information's gonna cost you.  Nothing big, mind you."
    ava "If I recall correctly, you're the one stuck sitting in a jail cell, not us."

    show icari plugsuit armscrossed tsun with dissolve

    ica "I'm not going to go around revealing client information unless there's security for me."
    ica "And I'd say you need my help more than ever if you still think you're here on a rescue mission.  If I tell you what's going on, you let me outta this cell and give me back my ryder."
    kay "(It seems like she's interested in talking.  Let's play along for now and see what she says.)"
    kay "All right.  If we're both against PACT, I'm interested in seeing what you have to say."
    ica "I may be an assassin, but I'm no scoundrel.  You can depend on my words, captain."

    show icari plugsuit neutral neutral with dissolve

    ica "War between the Solar Alliance and PACT is inevitable.  Everyone knows that and they're just too scared to admit it.  The galaxy's on the brink of an interstellar war on a scale it hasn't seen in one hundred years."
    ica "There's a certain faction within the Alliance which understands this and wants to intervene before the entire Neutral Rim's PACT's back yard."
    ica "And honestly, I'd rather not be bowing to the Veniczar, so I say good on them.  The only issue is that President Alythe's a damned pussy who couldn't fight an angry duck to save his own life."
    ica "The Alliance needs a push.  And this crisis is the opportunity everyone's been waiting for to bring the Alliance into this fight."

    show ava uniform handonhip neutral with dissolve

    ava "So you've been hired by this faction to hover around Vesta, and make sure that those diplomats are captured by PACT to spark a war.  Is that what you're saying?"
    ica "Now you're catching on.  You let me ensure that those diplomats are captured by PACT, and you can bet you'll have the Alliance's full support behind you in your war."
    kay "And if they find out I had anything to do with their capture?"

    show icari plugsuit armscrossed neutral with dissolve

    ica "Who gives a damn? The Alliance military wants PACT to get those diplomats to get this war started anyways.  You'll probably get a shiny medal for saving the Neutral Rim or something."
    kay "(This is a little hard to believe, but her hatred of PACT seems sincere.  What should I do?)"

    menu:
        "All right, you've made your point.  I'll let you out of your cell, but you'll be confined to quarters for now while we perform our own investigation.":
            jump outcellinvestigation
        "I don't believe you.  You can stay here in your cell while we perform our own investigation.":
            jump dontbelieveicari

label outcellinvestigation:

    $ affection_icari += 1

    show icari plugsuit armscrossed annoyed with dissolve

    ica "Tsch, that's the best you can do?"
    kay "It's not like you're going anywhere on your ryder without a booster pack.  So enjoy the warm bed."
    ica "Fine, just get me outta this cell and bring me something to eat."

    $ asa_location = "messhall"
    $ asa_event = "whattodoicari_asa"

    $ chi_location = "engineering"
    $ chi_event = "whattodoicari_chi"

    $ ava_location = "bridge"
    $ ava_event = "whattodoicari_ava"

    $ cal_location = "captainsloft"
    $ cal_event = "ftltransponder"

    $ gal_location = None
    $ captaindeck = 1
    jump dispatch

label dontbelieveicari:

    show icari plugsuit neutral angry with dissolve

    ica "Are you kidding me, captain!?  We had a deal!"
    kay "I didn't promise anything.  Ava, get our guest something to eat.  She'll be staying here for a while."
    ava "Understood."

    show icari plugsuit armscrossed bitter with dissolve

    ica "Tsch... Whatever.  Once you find out that I'm telling the truth, you'll be back here begging for help.  Just you wait!"

    $ asa_location = "messhall"
    $ asa_event = "whattodoicari_asa"

    $ chi_location = "engineering"
    $ chi_event = "whattodoicari_chi"

    $ ava_location = "bridge"
    $ ava_event = "whattodoicari_ava"

    $ cal_location = "captainsloft"
    $ cal_event = "ftltransponder"

    $ gal_location = None
    $ captaindeck = 1
    jump dispatch

label whattodoicari_ava:

    hide screen deck1

    scene bg bridge
    show ava uniform alt neutral neutral:
        zoom 1 xpos 0.5
    with dissolve

    window show

    kay "Did you get our guest set up?"
    ava "She's getting comfortable. About what she said..."

    menu:
        "She's got a point. Sparking an Alliance-PACT war is the only way we can stop PACT.":
            jump pointwaronlyway

        "She's obviously crazy. We're going to complete our mission and save those diplomats.":
            jump obviouslycrazysave

label pointwaronlyway:

    $ captain_prince += 1

    show ava uniform armscrossed neutral with dissolve

    ava "I admit, the only power in the galaxy capable of stopping PACT is the Alliance.  But can we trust the mercenary's words?"
    kay "PACT's destroyed our home. We're going to get payback for what they've done, no matter what."
    ava "I hope that you're not being blinded by what happened at Cera."
    kay "It's not like you disagree."
    ava "... ... ..."

    show ava uniform neutral lookleft with dissolve

    ava "True, Alliance intervention is the only hope we have at liberating Cera.  Liberating our home world will take a fleet.  And the Alliance has a mighty one at that."
    kay "PACT's going to take over the whole galaxy unless the Alliance steps in. If a few diplomats have to be sacrificed for the safety of the galaxy, so be it."

    show ava uniform handonhip neutral with dissolve

    ava "Very well, captain. I may not trust the mercenary, but I don't disagree with what you're saying."

    jump consideringoptionsfornow

label obviouslycrazysave:

    $ captain_moralist += 1

    ava "I agree we should be careful about her. But given our situation, we should consider what she has told us."
    kay "I won't have the blood of civilians on my hands, Ava."

    show ava uniform armscrossed neutral with dissolve

    ava "Noble of you. But know this captain: War between the Alliance and PACT will happen one way or another."
    ava "All we would be doing would be hastening the process. Every second we wait, PACT will have conquered one more neutral world and grown that much stronger."
    ava "The quicker the war between the Alliance and PACT begins, the more lives we can save in the end."

    jump consideringoptionsfornow

label consideringoptionsfornow:

    kay "Anyways, I'm still considering our options for now. What's our next step?"

    show ava uniform neutral talk with dissolve

    ava "I've made contact with the Alliance diplomats.  They're going to attempt to make an escape soon."
    kay "All right.  Will we be bringing them aboard?"
    ava "Actually, they've arranged to escape on the civilian liner Agamemnon.  We'll be providing escort in case things gets hairy."
    kay "Civilian liner?  I'm not so sure..."
    ava "They tell me international law prohibits them from coming aboard a foreign military vessel."
    kay "(That's the first time I've ever heard of a rule like that.  Something's amiss...)"
    kay "One challenge after another.  Keep me posted, Ava."

    $ ava_location = None
    $ pro_location = "captainsloft"
    $ pro_event = "proceed_rescuediplomats"
    $ captaindeck = 1

    jump dispatch

label whattodoicari_asa:

    hide screen deck0

    scene bg messhall
    show asaga uniform neutral happy
    with dissolve

    window show

    asa "Oh, did you need me for something, capt'n?"
    kay "I presume you've heard the rumors about the mercenary we've captured."

    show asaga uniform excited grin with dissolve

    asa "Well, we're still gonna rescue those diplomats, aren't we? And beat up the PACT fleet, of course!"
    kay "I don't think we'll be able to destroy the whole invasion fleet by ourselves, Asaga..."

    show asaga uniform neutral happy with dissolve

    asa "Don't worry, don't worry! Just leave it to me and mah Black Jack! We'll take care of the invasion fleet in no time!"

    menu:
        "What do you think about what the mercenary said?":
            jump whatdoyouthink

        "Just be careful out there and don't do anything reckless, okay?":
            jump caredontreckless

label whatdoyouthink:

    show asaga uniform armscrossed nonono with dissolve

    asa "No, no, no, capt'n! You can't do that and let innocents die!"

    show asaga uniform excited angry with dissolve

    asa "You gotta stand for what's right!  We're gonna win this fight the hard way, but the right way!"

    menu:
        "But we'll never beat PACT without the Alliance's help. We're just one ship.":
            jump neverbeatpactalliance
        "You're right.  We're going to win this war with our principles intact.":
            jump betterpactwinprinciples

label neverbeatpactalliance:

    $ captain_prince += 1

    show asaga uniform armscrossed confidenthappy with dissolve

    asa "Ahh, don't be so down, capt'n! You have me and the Black Jack! Together, we can do anything!"

    jump thanksfortalkasaga

label betterpactwinprinciples:

    $ captain_moralist += 1

    show asaga uniform excited grin with dissolve

    asa "Hell yeah, capt'n!"
    jump thanksfortalkasaga

label thanksfortalkasaga:

    kay "Uh, I'll keep that in mind. Thanks."

    show asaga uniform neutral smile with dissolve

    asa "I'll see you later!"

    $ asa_location = None
    $ pro_location = "captainsloft"
    $ pro_event = "proceed_rescuediplomats"
    $ captaindeck = 0

    jump dispatch

label caredontreckless:

    asa "Of course, capt'n!"

    $ pro_location = "captainsloft"
    $ pro_event = "proceed_rescuediplomats"
    $ captaindeck = 0

    jump dispatch

label whattodoicari_chi:

    hide screen deck1

    scene bg engineering
    show chigara uniform handsup surprise
    with dissolve

    window show

    chi "E-eah! O-oh, sorry, captain, I didn't see you coming..."

    menu:
        "What's your take on what's going on with the mercenary?":
            jump yourtakemercenary
        "How's the research station coming?":
            jump howsresearchstation

label yourtakemercenary:

    show chigara uniform twiddlefingers smile with dissolve

    chi "Ummm... I'm not very good with making decisions, so I think you'd be much better suited to thinking about it than I am..."

    show chigara uniform handstogether smile with dissolve

    chi "Eh-heh. Whatever the captain decides, I'm sure it'll be the right decision."

    menu:
        "Thanks for the vote of confidence, Chigara.":
            jump thanksconfidencechigara
        "Are you sure? You're smarter than anyone else I've ever met.":
            jump smarteranyoneelse

label howsresearchstation:

    show chigara uniform neutral neutral with dissolve

    chi "Ah, I've finished setting my equipment up. Even though it's still at the beginning stages, I'll be able to get started on some basic research projects."

    menu:
        "Good to hear. I'll allocate funding later.":
            jump goodallocatefundinglater
        "Great, let's see what projects need funding...":
            jump allocatefunds

label goodallocatefundinglater:

    chi "Understood, captain."

    menu:
        "What's your take on what's going on with the mercenary?":
            jump yourtakemercenary
        "Thanks for your work.  I'll see you later, Chigara.":
            jump thanksbyechigara

label smarteranyoneelse:

    chi "Uh-huh. I may be comfortable with machines, captain, but that's just about it. Where people are concerned, I feel... Well, I just don't feel like I understand them very well."
    kay "Maybe machines really are easier to deal with than people..."

    menu:
        "How's the research station coming?":
            jump howsresearchstation

        "Thanks for your work.  I'll see you later, Chigara.":
            jump thanksbyechigara

label thanksconfidencechigara:

    chi "Eh-heh. Any time, captain. Was there something else you needed?"

    menu:
        "How's the research station coming?":
            jump howsresearchstation

        "Thanks for your work.  I'll see you later, Chigara.":
            jump thanksbyechigara

label thanksbyechigara:

    show chigara uniform neutral neutral with dissolve

    chi "Good bye, captain."

    $ chi_location = None
    $ pro_location = "captainsloft"
    $ pro_event = "proceed_rescuediplomats"
    $ captaindeck = 1

    jump dispatch

label proceed_rescuediplomats:

    hide screen deck0
    stop music fadeout 1.5
    scene black
    window show
    with dissolve

    kay "Well then, I think I'll return to my room to think about what to do..."

    scene bg captainsoffice with dissolve

    kay "Begin captain's log. We've made contact with the diplomats on Versta and are going to attempt an escape."
    kay "I should be focused on getting them out of here safe, but I can't get what the mercenary said out of my mind."
    kay "Some part of my head thinks that she has some ulterior motive and she's tricking us all. Maybe she's a PACT spy and making us wander into a trap."
    kay "Maybe the diplomats know something that PACT doesn't and she's just fooling us into silencing them."
    kay "Or maybe she's really telling the truth."

    play music "Music/A_Dark_Dream.ogg"
    scene bg captainsoffice_nolights
    show captainsoffice_nolights_overlay
    with dissolve

    kay "What the-"

    show icari plugsuit armscrossed confident behind captainsoffice_nolights_overlay with dissolve

    ica "Hello again, captain. Unfortunately, it looks like you'll have to upgrade your security system, since it was all too easy for me to crack."
    kay "Security, get to my quarters now!"
    ica "Of course, I've already disabled all communications out of this room as well."
    kay "What do you want, mercenary?"

    show icari plugsuit handonhip snide behind captainsoffice_nolights_overlay with dissolve

    ica "Relax captain. I'm not here to slit your throat, or anything gory like that. I just want to talk."
    kay "Just talk?"

    show icari plugsuit altneutral neutral behind captainsoffice_nolights_overlay with dissolve

    ica "I never imagined that I'd find myself onboard a Cera vessel. It must be hard, being the only ship left."
    kay "I don't disagree, but we get by."
    ica "Tell me... How many people died at Cera that day?"

    menu:
        "Your attempts at manipulating me won't work, mercenary.":
            jump photoalbumlook
        "Too many.":
            jump photoalbumlook

label photoalbumlook:

    show item album:
        xpos 0.1 ypos 0.2
    with dissolve

    ica "Who's that in the picture album behind you?"
    kay "That's none of your business."

    show icari plugsuit altneutral smallsnide with dissolve

    ica "She looks young.  You don't seem like a father though.  So I'm thinking... your sister?"
    kay "You're walking on thin ice.  I suggest you drop it."

    hide item with dissolve

    ica "What's the matter, captain? Did I hit a soft spot?"

    show icari plugsuit altneutral smallsnide:
        zoom 1
        ease 1.00 zoom 1.5 ypos 1.4

    ica "Are you scared for her?"
    ica "... ... ..."

    show icari plugsuit neutral neutral with dissolve

    ica "I know what it's like to lose family... Listen to me, captain."
    ica "PACT killed my entire family years ago.  I swore I'd get PACT back for what they did, and I'm finally so close."
    ica "We can work together, you and I.  Let's bring the Alliance into this war and end the PACT invasion.  I'll even work under you as a pilot if you're going after PACT."
    kay "What if I said I don't trust you?"
    ica "How about I let you in a little secret, captain..."
    kay "I thought mercenaries didn't share secrets."
    ica "I'm willing to make an exception, just for you."
    ica "Do you know who it was that hired me to take out those diplomats? It was Admiral Grey of the Solar Alliance himself."
    kay "Admiral Grey? Funny you say that, considering he sent us here to protect the diplomats."

    show icari plugsuit armscrossed neutral with dissolve

    ica "Get with the program, captain.  Everyone in the Alliance military knows that war is inevitable."
    ica "You can save those diplomats now... And with each passing day, PACT will conquer one planet after another.  Millions more will lose their lives..."
    ica "Until PACT finally runs out of neutral planets to conquer and turns to Alliance space."
    ica "Then there will be an interstellar war of unimaginable proportions, with PACT bringing to bear the resources of every planet of the Neutral Rim against the Alliance."
    ica "Or those diplomats can die now.  Then the Alliance will intervene while PACT is still mustering its strength."
    ica "While a few may have to be sacrificed, you will save the lives of millions."
    ica "Admiral Grey understands this.  That is why he hired me to ensure those diplomats never make it out of Verstra space."

    menu:
        "You're not making any sense. Why would Admiral Grey send us here to save the diplomats, and then hire you to make sure they get captured by PACT?":
            jump nosensesavediplomats
        "You're saying Alliance military's going to coup the civilian government?":
            jump militarycoupgovernment
        "So in the end, what are you after?":
            jump endafterwhat

label nosensesavediplomats:

    ica "Admiral Grey still has to obey the commands of President Alythe. The President has ordered that war with PACT is to be avoided at all costs."
    ica "That's why he used the official channels to send the Sunrider here to protect the diplomats."
    ica "Then on the unofficial channels, he contacted me to ensure that the diplomats are captured."

    menu:
        "You're saying Alliance military's going to coup the civilian government?":
            jump militarycoupgovernment
        "So in the end, what are you after?":
            jump endafterwhat

label militarycoupgovernment:

    ica "Perhaps. Not today, or tomorrow, but if the Solar Congress continues to be mired in politics while PACT swallows up the entire neutral rim, the Alliance military will act to protect its citizens, with or without the support of the civilian leaders."

    menu:
        "You're not making any sense. Why would Admiral Grey send us here to save the diplomats, and then hire you to make sure they get captured by PACT?":
            jump nosensesavediplomats
        "So in the end, what are you after?":
            jump endafterwhat

label endafterwhat:

    show icari plugsuit altneutral smallsnide with dissolve

    ica "Like I said, captain, I just want to see PACT defeated. I think we share that common goal, don't we?"

    show icari plugsuit neutral neutral:
        ease 0.5 zoom 1.8 ypos 1.6

    ica "So, what will it be captain?"
    ica "Will you stand by while PACT conquers one neutral planet after another, growing more powerful with each day; or will you make a stand and stop PACT once and for all?"

    menu:
        "I hate PACT and everything they stand for. That includes killing innocents to accomplish my goals.  Now get back to the brig where you belong.":
            jump hatepactbackbrig
        "All right.  I believe you.  Let's work together.":
            jump rightyouworktogether

label hatepactbackbrig:

    $ captain_moralist += 10

    show icari plugsuit neutral frown:
        ease 0.5 zoom 1.5 ypos 1.4
    with dissolve

    ica "You don't understand, captain. PACT is evil. They don't care about the lives of innocents. We have to act now to stop them, before it's too late!"
    kay "We still have a duty to humanity on board this ship.  I will not command the killing of innocents."

    play music "Music/Battle_Against_Time.ogg"

    show icari plugsuit pistol angry with dissolve

    ica "Tsch... Looks like you've left me no choice then."
    ica "PACT must be stopped no matter what, and I won't let you interfere with my mission."

    scene bg captainsoffice
    show icari plugsuit pistol angry:
        zoom 1.5 xpos 0.5 ypos 1.4
    show ava uniform alt neutral angry:
        xpos 0.8 zoom 1
    with dissolve

    ava "Captain!"

    show icari plugsuit pistol angry:
        ease 0.5 ypos 1.4 xpos -0.5

    ica "!!!"

    show ava uniform neutral angrytalk:
        ease 0.5 xpos 0.5

    ava "Are you alright?"
    kay "Yeah."
    ava "I ran up here as soon as I realized the mercenary escaped.  Looks like I was almost too late."
    kay "That mercenary's becoming a problem. Find her and stop her!"

    jump findherandstopher

label rightyouworktogether:

    $ captain_prince += 1
    $ affection_icari += 3

    show icari plugsuit neutral smile:
        ease 0.5 zoom 1.5 ypos 1.4
    with dissolve

    ica "I'm glad we agree."
    kay "Now, will you please turn the lights in my office back on?"

    show icari plugsuit armscrossed confidentlaugh with dissolve

    ica "Hahahaha.  Of course, captain."

    scene bg captainsoffice
    show icari plugsuit armscrossed confidentlaugh:
        zoom 1.5 xpos 0.5 ypos 1.4
    with dissolve

    kay "I'll need to inform Ava of the change in plans.  You should go back to where you're supposed to be now, and just play along for now."

    show icari plugsuit armscrossed confident with dissolve

    ica "All right, I'm willing to be your prisoner for a bit."

    show icari plugsuit armscrossed embarassedtsun with dissolve

    ica "Oh... And thank you captain."
    ica "For uh... hearing me out."
    kay "???"
    ica "Seriously, you're going to need my help if you couldn't figure it out on your own..."

    jump agreehelpicari

label findherandstopher:

    $ affection_asaga += 2

    scene bg bridge with dissolve

    kay "What's the status on the Phoenix!?"

    show ava uniform alt neutral angry with dissolve

    ava "Damn! She's already hacked into our security system and escaped on her ryder!"

    show ava uniform alt order angry with dissolve

    ava "All pilots, scramble your ryders and pursue!"

    show ava uniform alt neutral angry with dissolve
    show asaga uniform excited surprise:
        xpos 0.2
    with wipeup

    asa "O-oh! Press quick save, Chigara, it's go time!"

    show chigara uniform handsup surprise:
        xpos 0.8
    with wipeup

    chi "E-eh!?"

    show ava uniform fistup angry with dissolve

    ava "What's going on down there!?"

    show asaga uniform armscrossed embarassedgrin with dissolve

    asa "Oh nuthin', was just in the middle of a game, that's all!"

    hide asaga with dissolve
    hide chigara with dissolve

    kay "It was their break time."

    show ava uniform facepalm with dissolve

    ava "Unbelievable..."

    play sound "sound/warning.ogg"

    "-Warning-"

    kay "What now?"

    show ava uniform neutral angrytalk with dissolve

    ava "Uh... Warning! Massive PACT signatures detected!"

    play music "Music/Driving_the_Top_Down.ogg" fadeout 1.5
    play sound "Sound/redalert.ogg"
    scene bg bridgered
    show ava uniform neutral angrytalk
    with dissolve

    kay "Red alert!  All hands, assume battle stations!"
    ava "It's the PACT invasion fleet. They arrived here early!"
    kay "Just one thing after another. Asaga, come in."

    show asaga plugsuit excited focushappy:
        xpos 0.2
    with wipeup

    asa "I'm here, capt'n!"
    kay "Change of plans.  Focus on defending the diplomats against the PACT fleet.  Keep your eyes out for the mercenary unit.  I have the feeling she'll be back to interfere with our mission."
    asa "Aye capt'n!"
    kay "Bring us alongside the Agamemnon.  A civilian transport won't last long against that PACT fleet without the Sunrider's cover fire."
    ava "Aye captain.  We are being hailed by the Agamemnon."
    kay "Put her through."
    "Agamemnon" "It looks like the PACT fleet's going to make our escape complicated.  Good to have you by our side, Sunrider."
    kay "Glad to be here.  Stay close and let us do the fighting.  Warp as soon as we leave Versta's gravity well with or without us."
    "Girl" "Is the big ship going to protect us?"
    kay "Uh, Agamemnon, did we just hear that last transmission correctly?"
    "Agamemnon" "I'm sorry, but with the PACT invasion fleet approaching, we couldn't just leave the children behind!"
    kay "(As if this couldn't get any worse! So that's why they were so against escaping with us!)"
    kay "How many?"
    "Agamemnon" "Six hundred children in all.  It was the only way to get them off planet before PACT arrived!"
    kay "This mission just got even more complicated."
    kay "All ryders.  Your orders are to defend the Agamemnon at all costs.  Don't let a single PACT unit hit it."

    show asaga plugsuit handsonhips determined with dissolve

    asa "Understood, captain!  Don't worry, we'll keep those children safe!"

    show chigara plugsuit excited determined:
        xpos 0.8
    with wipeup

    chi "We'll do this with our lives!"
    kay "All ryders, launch!"

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    $ renpy.pause(2)

    $ ep2_cancelwarp = False

    window hide
    hide bg bridgered
    hide ava
    hide asaga
    hide chigara
    hide battlewarning

    call mission8_inits
    $ BM.mission = 8
    $ check1 = False
    $ check2 = False
    $ check3 = False
    $ check4 = False
    $ check5 = False
    $ check6 = False

    jump battle_start

label agreehelpicari:

    $ affection_ava += 1

    scene bg bridge with dissolve
    show ava uniform armscrossed neutral with dissolve

    ava "Captain.  We're nearly finished with the preparations for our escort mission.  The diplomats are secure on the civilian transport Agamemnon.  I was just about to call you down here, in fact."
    kay "About that.  There's been a change of plans, Ava."
    ava "Oh?"
    kay "The mercenary is right."
    kay "The lives of a few diplomats cannot compare to the billions of innocents who will be killed if PACT is permitted to invade the Neutral Rim unchallenged."

    show ava uniform armscrossed smile with dissolve

    ava "Understood, captain. As is the norm in war, sacrifices must be made for the greater good.  I will relay your new orders to the crew then."
    kay "Thank you, Ava."

    play sound "sound/warning.ogg"

    "-Warning-"

    kay "What happened!?"

    show ava uniform neutral angrytalk with dissolve

    ava "Contact!  Multiple warp signatures detected!  It's PACT!"

    play music "Music/Driving_the_Top_Down.ogg" fadeout 1.5
    play sound "Sound/redalert.ogg"
    scene bg bridgered
    show ava uniform neutral angrytalk
    with dissolve

    kay "Red alert! All hands, assume battle stations!"
    ava "It's the PACT invasion fleet.  They arrived here early!"
    kay "Get us out of the planet's gravity well and spool up our warp drive.  Our role here is finished."
    ava "Understood, captain."

    show ava uniform handonhip mad with dissolve

    ava "The PACT fleet has noticed us.  A squadron of ships has broken off to intercept.  Time until in range: Ten minutes."
    ava "We are receiving a message from the Agamemnon.  Should I open the channel?"

    menu:
        "Put me through to them.":
            jump agaputmethrough
        "No, close the channel.":
            jump agaclosechannel

label agaputmethrough:

    ava "Aye captain."
    "Agamemnon" "What are you doing!?  I thought you were supposed to be our escort!"
    kay "Change of plans.  It seems like your leaders no longer wish to see you alive."
    "Agamemnon" "What do you mean...?"
    kay "Your sacrifice is necessary to stop PACT and save the lives of billions."
    "Agamemnon" "What? What is this nonsense you're spurting!?"
    "Agamemnon" "Wait-- you mean to sacrifice us to spark a war...  Of course...!"
    kay "I hope you understand your position."
    "Agamemnon" "No... You cannot possibly do this to us!  Not when we..."
    "Girl" "What's going on?  Why isn't the big ship protecting us?"
    kay "What the-  Agamemnon, did I just hear what I think I did?"
    "Agamemnon" "There are six hundred children on board this ship, Sunrider!"
    "Agamemnon" "With the PACT invasion fleet approaching, taking the Versta children under Alliance protection was the only thing we could do!"
    kay "What!?"

    show ava uniform neutral angrytalk with dissolve

    ava "Captain, we are getting underway.  What are your orders?"
    "Agamemnon" "Without your protection, our act of charity will instead doom the children!"
    "Agamemnon" "Please, help us!"
    kay "(Six hundred children? There was no way to have foreseen this!)"

label cmd_savethechildren:

    if BM.cmd >= 300:
        menu:
            "...Maintain course.  Prepare to break through that PACT squadron.":
                jump maintainpreparethroughpact
            "COMMAND DECISION: Cancel warp.  We're going to escort the Agamemnon out of here! |300 CMD/[BM.cmd] Available|":
                jump cancelwarpagaout

    if BM.cmd < 300:
        menu:
            "...Maintain course.  Prepare to break through that PACT squadron.":
                jump maintainpreparethroughpact
            "COMMAND DECISION: Cancel warp.  We're going to escort the Agamemnon out of here! |INSUFFICIENT CMD POINTS|":
                jump cmd_savethechildren


label maintainpreparethroughpact:

    $ affection_asaga -= 2
    $ captain_prince += 10

    show ava uniform salute angry with dissolve

    ava "Aye captain."
    kay "Asaga, your orders are to focus on the PACT squadron ahead of us and open up a path for the Sunrider to warp.  Ignore the Agamemnon, understand?"

    show asaga plugsuit altneutral surprise:
        xpos 0.2
    with wipeup

    asa "B-but what about-"
    kay "It's necessary to stop PACT.  Do it."

    show asaga plugsuit armscrossed grumpy with dissolve

    asa "I'm not feeling so good about this....."

    show chigara plugsuit excited scared:
        xpos 0.8
    with wipeup

    chi "Asaga, we have to do this or else Vestra won't be the last planet that PACT invades!"

    show asaga uniform armscrossed madshout with dissolve

    asa "A-all right, all right, let's go!"

    hide chigara with dissolve
    show icari plugsuit armscrossed confident:
        xpos 0.8
    with wipeup

    ica "Heh, I think you'll need my help too."

    show asaga uniform handsonhips mad with dissolve

    asa "Eh? What are you doing here?"
    ica "Just a bit of back up, in case things don't go as planned.  With the captain's approval, of course."
    kay "All right, Icari.  Help us break through the PACT fleet and you will have earned our trust."

    show ava uniform armscrossed looklefttalk with dissolve

    ava "Looks like I'll be taking another look at our security protocols after this..."
    kay "Icari's no ordinary prisoner, Ava.  I think we can let it slide this time."
    kay "All ryders, launch!"

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide icari
    hide asaga
    hide battlewarning

    call mission7_inits
    $ BM.mission = 7
    jump battle_start

label cancelwarpagaout:

    $ ep2_cancelwarp = True

    play sound "sound/swordhit.ogg"
    show captainflash:
        xpos 1.1 ypos 0.2
        ease 0.7 xpos 0.35
        pause 0.5
        ease 0.8 alpha 0

    $ BM.cmd -= 300
    $ captain_moralist += 5
    $ affection_asaga += 2

    show ava uniform salute angry with dissolve

    ava "Aye captain.  Changing course.  We will take the Agamemnon under our wing."

    show asaga plugsuit excited focushappy:
        xpos 0.2
    with dissolve

    asa "All right! Let's go and kick some PACT ass! Haha!"

    show chigara plugsuit excited determined:
        xpos 0.8
    with dissolve

    chi "I'm ready, captain!"
    kay "All ryders, launch!"

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide asaga
    hide chigara
    hide battlewarning

    call mission8_inits
    $ BM.mission = 8
    $ check1 = False
    $ check2 = False
    $ check3 = False
    $ check4 = False
    $ check5 = False
    $ check6 = False

    jump battle_start

label agaclosechannel:

    $ captain_prince += 5

    ava "Understood."

    show ava uniform handonhip mad with dissolve

    ava "The Agamemnon has left port, captain.  They are making a run for it out of Versta's gravity well."
    kay "Let them be.  Prepare to break through that PACT squadron and engage warp."
    ava "Aye captain."
    kay "Asaga, your orders are to focus on the PACT squadron ahead of us and open up a path for the Sunrider to warp.  Ignore the Agamemnon, you understand?"

    show asaga plugsuit altneutral surprise:
        xpos 0.2
    with wipeup

    asa "B-but-"
    kay "It's necessary to stop PACT.  Do it."

    show asaga plugsuit excited forcedsmile with dissolve

    asa "O-okay, captain.  C'mon Chigara, let's go out there and beat PACT up!"

    show chigara plugsuit excited scared:
        xpos 0.8
    with wipeup

    chi "I-I'll try my best, captain!"

    hide chigara with dissolve
    show icari plugsuit armscrossed confident:
        xpos 0.8
    with wipeup

    ica "Heh, I think you'll need my help too."

    show asaga uniform handsonhips mad with dissolve

    asa "Eh? What are you doing here?"

    ica "Just a bit of back up, in case things don't go as planned.  With the captain's approval, of course."
    kay "All right, Icari.  Help us break through the PACT fleet and you will have earned our trust."

    show ava uniform armscrossed looklefttalk with dissolve

    ava "Looks like I'll be taking another look at our security protocols after this..."
    kay "Icari's no ordinary prisoner, Ava.  I think we can let it slide this time."
    kay "All ryders, launch!"

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide icari
    hide asaga
    hide battlewarning

    $ check1 = False

    call mission7_inits
    $ BM.mission = 7
    jump battle_start

label mission7:

    if check1 == False:
        $BM.draggable = False

        play sound "sound/objectives.ogg"
        "Note:  The Phoenix can briefly become immune to blindside attacks by going into stealth mode."

        $ check1 = True

        $ BM.draggable = True  #this enables dragging the viewport again.

    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission7 #loop back
    else:
        pass #continue down to the next label

label aftermission7:

    $ Saveddiplomats = False

    hide screen commands
    hide screen battle_screen

    play music "Music/Invasion of Chaos.ogg"

    scene bg bridgered with dissolve
    window show

    show ava uniform neutral angrytalk with dissolve

    ava "The PACT squadron has been neutralized!"
    kay "Get us out of the planet's gravity well, double time!"
    ava "Aye captain."

    scene cg_epi2_cgback
    show cg_epi2_phoenix
    with dissolve

    asa "Wait!  I'm reading the Agamemnon on the scanner!"
    ava "It made it past the PACT fleet?"
    chi "No... look!"

    show cg_epi2_shuttleflame:
        xpos 0.5 ypos -0.1
        ease 1.0 xpos 0.0 ypos 0.0

    "Agamemnon" "...-static- requesting assistance... -static-... critical... -static-... the children..."

    show cg_epi2_cgset:
        ease 0.8 xpos -2900 ypos -528 zoom 3
        ease 0.5 alpha 0
    show cg_epi2_cg2:
        alpha 0
        pause 0.5
        ease 0.8 alpha 1.0

    ica "...!!!"

    pause 0.5
    scene cg_epi2_cg3 with dissolve
    pause 1.0
    scene cg_epi2_cg2 with dissolve
    pause 0.8
    scene white with dissolve

    play sound "sound/explosion4.ogg"

    scene cg_epi2_cgback
    show cg_epi2_shuttleflame
    show cg_epi2_explode1:
        alpha 0
        ease 0.8 alpha 1
        ease 0.8 alpha 0
    show cg_epi2_explode2:
        alpha 0
        pause 0.3
        ease 0.8 alpha 1
        ease 0.8 alpha 0
    show cg_epi2_explode3:
        alpha 0
        pause 0.6
        ease 0.8 alpha 1
        ease 0.8 alpha 0
    pause 1.0
    hide cg_epi2_shuttleflame

    pause 1.5
    scene bg bridgered with dissolve
    show ava uniform neutral angrytalk:
        xpos 0.4
    with dissolve

    ava "Contact lost with Agamemnon!"
    kay "... ... ..."

    show icari plugsuit armscrossed sad:
        xpos 0.6
    with wipeup

    ica "I've been looking forward to this for as long as I can remember..."

    show icari plugsuit armscrossed cry with dissolve

    ica "And yet why..."

    show asaga plugsuit excited shout:
        xpos 0.8
    with wipeup

    asa "Tsch.....  PACT...!!!"

    show chigara plugsuit handonchest sadsurprise:
        xpos 0.2
    with wipeup

    chi "How horrible...."
    ava "The Sunrider has cleared the planet's gravity well.  Warp out at your command, captain."
    kay "All ryders, return home."
    kay "We're getting out of here."

    stop music fadeout 1.5
    scene black with dissolvelong
    scene bg captainsoffice with dissolve
    play music "Music/The Tumbrel.ogg" fadeout 1.5

    show ava uniform alt neutral neutral with dissolve

    ava "The results of our investigation are complete, captain."
    ava "It appears that what the mercenary told us was the truth.  While Admiral Grey's Office officially denies any involvement, several inside sources have informed me that the mercenary had been hired by the Admiral."
    ava "Further, by going through previous obituaries, I've confirmed that the mercenary's mother, father, and brother were killed by PACT thirteen years ago."
    kay "I see..."

    show ava uniform armscrossed looklefttalk with dissolve

    ava "Are you feeling all right sir?"
    "Shields stood from his chair."
    kay "Yeah."
    "He turned around and picked up the picture frame of his sister."

    show item album:
        xpos 0.2 ypos 0.3
    with dissolve

    kay "So the girl's lost her whole family to PACT, huh."

    hide item with dissolve

    show ava uniform neutral neutral with dissolve

    ava "It would appear so.  What do you intend to do with her?"
    kay "Invite her to stay.  She's a talented pilot.  And she's got an axe to grind against PACT.  We could use someone like her on our side."
    ava "Understood, captain."
    ava "There is one final matter."
    kay "Hm?"
    ava "The Solar Congress convened for an emergency session earlier today."
    ava "While the official vote has not yet taken place, all indications show it will unanimously adopt a resolution condemning PACT aggression in the Neutral Rim and mobilize the Space Force in defense of Alliance space."
    kay "So the Alliance will finally take action."
    ava "The galaxy's mere seconds away from total intergalactic war now."
    kay "Good."
    ava "... ... ..."

    show ava uniform armscrossed looklefttalk with dissolve

    ava "Kayto. Is this really..."
    kay "What?"

    show ava uniform neutral neutral with dissolve

    ava "Nothing sir.  That concludes my report."
    ava "I must attend to other matters now."
    kay "Carry on, Ava."
    hide ava with dissolve

    scene black with dissolve
    scene bg messhallwindows with dissolve
    show icari uniform armscrossed sad:
        zoom 1.5 ypos 1.4 xpos 0.5
    with dissolve

    ica "... ... ..."
    kay "What's the matter.  You got exactly what you wanted, and now you're giving me the long face?"

    show icari uniform armscrossed lookawayannoyed with dissolve

    ica "Tsch.  Sneaking up on me, captain?"
    kay "Don't give me that.  I know you heard me coming from the moment I entered the door."
    ica "Contract killing's an ugly business, captain.  If you think I'm going to be torn up about those kids, then you're wrong."
    kay "I saw your face after you came back."

    show icari uniform armscrossed tsun with dissolve

    ica "I was just... dazed, that's all.  A-also, I keep onions in my cockpit.  W-what, you don't believe me? It's true!"

    show icari uniform armscrossed sad with dissolve

    ica "... ... ..."
    ica "Tsch."
    ica "I saw a girl on that ship. And it just reminded me..."
    ica "When I was twelve, I was just a kid wandering the stars with my parents."
    ica "Damned PACT ships came out of nowhere one day and they boarded our ship, demanding star charts which we knew nothing about."
    ica "I saw their leader shoot my mom between the eyes right in front of me."
    ica "I barely managed to get to the escape pod before they blasted the whole ship. I drifted through space for five days until I was rescued by an Alliance patrol."

    show icari uniform armscrossed depressedblush with dissolve

    ica "In the end... I was the only survivor."

    show icari uniform neutral madblush with dissolve

    ica "They all deserve to die for what they did that day... I've spent my whole life trying to avenge my family.  And I won't stop now."
    kay "... ... ..."
    "Shields walked to the window and gazed out into the stars."
    "Far away, invisible to the naked eye, Cera glimmered among the countless lights."
    "A wave of sadness came upon Shields, suffocating his throat and squeezing the air out of his lungs."
    "Then came the rage - boiling rage which could barely be suppressed."
    kay "No."
    kay "Neither will I."

    window hide
    scene black with dissolve
    scene cg_album:
        ease 5.0 xpos -0.3
    with dissolvelong

    pause 8.0

    jump ep3_start

label mission8:

    if ep2_cancelwarp == True:

        $BM.draggable = False

        show ava uniform altneutral angry onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        ava "Captain, we just had an unauthorized launch from our hangar! It's the mercenary!"
        kay "Disable her ryder!"
        ava "Too late! She's already out of our range."
        kay "All units. Icari has escaped on the Phoenix. Keep your eyes open for her. No doubt she intends to interfere with our mission."

        hide ava onlayer screens with dissolve
        $ ep2_cancelwarp = False
        $ BM.draggable = True

    if check1 == False:

        $BM.draggable = False

        play sound "Sound/objectives.ogg"
        "Objective: Bring the Agamemnon to the far right edge of the map."

        $ check1 = True
        $ BM.draggable = True

    if check2 == False and BM.turn_count == 3:

        play sound "sound/Voice/Ava/Ava Others 6.ogg"
        python:
            create_ship(PactMook(),(13,3),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactMook(),(13,4),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactBomber(),(14,3),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])

            create_ship(PactMook(),(13,7),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactBomber(),(14,8),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])

        $ check2 = True

    if check3 == False and BM.turn_count == 5:

        play sound "sound/Voice/Ava/Ava Others 5.ogg"
        python:
            create_ship(MissileFrigate(),(15,8),[PactFrigateMissile()])
            create_ship(PactCruiser(),(14,6),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(14,7),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
        $ check3 = True

    if check4 == False and BM.turn_count == 6:

        $BM.draggable = False

        show icari plugsuit point angry onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        ica "Get outta my way!"

        hide icari onlayer screens with dissolve
        show asaga plugsuit handsonhips angry onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        asa "Oy!  Don't you see what's happening here!?  If you go through with this, all those children are gonna die!"

        hide asaga onlayer screens with dissolve
        show icari plugsuit neutral angry onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        ica "And if I don't, a million more will die as PACT conquers planet after planet!"

        hide icari onlayer screens with dissolve
        show asaga plugsuit excited angry onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        asa "You don't even know if letting everyone die now will prevent that!"
        asa "Screw thinking about what might happen tomorrow!  'Cause you've got innocents to protect today, right in front of you!"

        hide asaga onlayer screens with dissolve
        show icari plugsuit handonhip snide onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        ica "Heheh...  You're naïve."
        ica "War cannot be won without sacrifice.  The righteous like you are just blind to reality!"

        hide icari onlayer screens with dissolve
        show asaga plugsuit point angry onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        asa "Y-you're crazy!"

        hide asaga onlayer screens with dissolve

        python:
            create_ship(PhoenixEnemy(),(18,6),[PhoenixEnemyMelee(),PhoenixEnemyAssault()])

        $ BM.draggable = True
        $ check4 = True


    if check5 == False and BM.turn_count == 9:

        play sound "sound/Voice/Ava/Ava Others 6.ogg"
        python:
            create_ship(PactCruiser(),(16,1),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(17,1),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(18,1),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(16,16),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(17,16),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(18,16),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])

        $ check5 = True

    if check6 == False and BM.turn_count == 11:

        $BM.draggable = False

        show ava uniform facepalm onlayer screens with dissolve

        ava "That's enough heroics, captain! We have to get out of here now!!"

        hide ava onlayer screens with dissolve

        python:
            create_ship(PactCruiser(),(16,1),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(17,1),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(18,1),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(MissileFrigate(),(16,2),[PactFrigateMissile()])
            create_ship(MissileFrigate(),(17,2),[PactFrigateMissile()])
            create_ship(MissileFrigate(),(18,2),[PactFrigateMissile()])

            create_ship(MissileFrigate(),(16,15),[PactFrigateMissile()])
            create_ship(MissileFrigate(),(17,15),[PactFrigateMissile()])
            create_ship(MissileFrigate(),(18,15),[PactFrigateMissile()])
            create_ship(PactCruiser(),(16,16),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(17,16),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(18,16),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])

        $ check6 = True
        $BM.draggable = True

    $BM.battle()  #continue the battle

    if agamemnon.location != None:
        if agamemnon.location[0] == 18:
            $ BM.battle_end()

    if agamemnon.hp <= 0:
        $ renpy.jump('sunrider_destroyed')

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission8 #loop back
    else:
        pass #continue down to the next label

label aftermission8:

    python:
        BM.ships.remove(agamemnon)
        player_ships.remove(agamemnon)

        phoenix_weapons = [PhoenixAssault(),PhoenixMelee(),Stealth()]
        phoenix = create_ship(Phoenix(),(9,5),phoenix_weapons)

    $ Saveddiplomats = True

    hide screen commands
    hide screen battle_screen

    play music "Music/Battle_Against_Time.ogg" fadeout 1.5

    scene space back8
    show blackjack
    with dissolve

    window show

    show asaga plugsuit point angry:
        xzoom -1 xpos 0.2
    with dissolve

    asa "It's over, Icari!  Surrender!"

    scene space back9
    show phoenix:
        xzoom -1
    with dissolve

    show icari plugsuit neutral creepy:
        xpos 0.3
    with dissolve

    ica "... ... ..."

    show icari plugsuit neutral creepygrin with dissolve

    ica "Ufufufu..."

    show icari plugsuit point crazylaugh with dissolve

    ica "HAH!  You think you've won? "
    ica "The only thing you'll accomplish today is allow PACT to win this war!  And I'll never allow that!"
    ica "With these very hands... I'll rid the galaxy of PACT!  For everyone that they've murdered!"
    kay "Icari, stop!"
    ica "Hehehehe... Hahahahaha!!"

    play sound "sound/mechchange.ogg"
    show phoenix assault with dissolve

    ica "I'm... going to avenge everyone!  And there won't be anyone to stop me!"

    scene cg_epi2_cgback
    show cg_epi2_shuttle
    with dissolve

    show cg_epi2_phoenix:
        xpos -0.75 ypos 1.75
        ease 0.8 xpos 0.0 ypos 0.0

    pause 2.0

    stop music fadeout 1.5

    show cg_epi2_cgset2:
        ease 0.8 xpos -2900 ypos -528 zoom 3
        ease 0.5 alpha 0
    show cg_epi2_cg2:
        alpha 0
        pause 0.5
        ease 0.8 alpha 1.0

    ica "... ... ..."

    scene cg_epi2_cg3 with dissolve
    pause 1.0
    scene cg_epi2_cg2 with dissolve

    ica "... ... ..."

    scene cg_epi2_cgset2 with dissolve

    ica "...Tsch..."

    play music "Music/Limitless.ogg"

    scene bg bridgered
    show icari plugsuit neutral mad
    with dissolve
    pause 0.5
    show icari plugsuit neutral mad2 with dissolve
    pause 0.5
    show icari plugsuit neutral sadblush with dissolve
    pause 0.5
    show icari plugsuit neutral sadcry with dissolve

    ica "Why..."
    kay "Because you're not like PACT, Icari.  Don't ever forget that."

    show icari plugsuit armscrossed cryclosedeyes with dissolve

    ica "...Tsch."
    ica "So uncool..."

    show ava uniform neutral talk:
        xpos 0.2
    with dissolve

    ava "Captain, we've escaped Versta's gravity well.  The Agamemnon is warping out."
    kay "Spool up our warp drive.  Get us out of here too."
    kay "All ryders, return home.  That includes you, Icari."

    show icari plugsuit armscrossed crysmile with dissolve

    ica "... ... ..."
    ica "Understood.  Phoenix, returning."

    $ Random = renpy.random.randint(1,9)

    if Random == 1:
        scene space back1
    if Random == 2:
        scene space back2
    if Random == 3:
        scene space back3
    if Random == 4:
        scene space back4
    if Random == 5:
        scene space back5
    if Random == 6:
        scene space back6
    if Random == 7:
        scene space back7
    if Random == 8:
        scene space back8
    if Random == 9:
        scene space back9

    show sunrider_warpout_standard:
        xpos 700 ypos 350
    with dissolve

    pause 1.0

    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_standard_flash:
        xpos 426 ypos 0 alpha 0
        linear 0.1 alpha 1
        linear 0.1 alpha 0
    show sunrider_warpout_standard out:
        xpos 700 ypos 350
        ease 0.2 xpos 200 ypos 300 zoom 0

    pause 1.0

    scene bg hangar with dissolve

    show asaga plugsuit vpose:
        xpos 0.4
    with dissolve

    asa "Ah hah!! That's two for two, captain!"
    kay "Good job, Asaga. I admit, I was starting to sweat pretty heavily there."

    show asaga plugsuit armscrossed smile with dissolve

    asa "Eh-heh... Any time!"

    show chigara plugsuit handonchest smile:
        xpos 0.2
    with dissolve

    chi "Ah, I've come back too, captain."
    kay "Good job to you too, Chigara."
    chi "Eh-heh... Thank-you, captain."

    show ava uniform alt neutral mad:
        xpos 0.8
    show icari plugsuit armscrossed concernedlookaway:
        xpos 0.6
    with dissolve

    ava "I've apprehended the mercenary. What should we do with her?"
    ica "... ... ..."
    kay "Well, I guess it's better being one of the good guys after all, huh Icari?"

    show icari plugsuit armscrossed tsun with dissolve

    ica "What? I-it's not like I wanted to help you out or anything! I just felt bad about those kids..."

    show icari plugsuit armscrossed sad with dissolve

    ica "... ... ..."
    ica "But... I guess I was wrong. For just a moment there, I would actually have done it."
    ica "I would have shot at those kids, just to get even with PACT."
    ica "My whole family was killed by PACT when I was just twelve years old."
    ica "We were... just space explorers. But they still came onboard, demanding charts that we knew nothing about."

    show icari plugsuit armscrossed cry with dissolve

    ica "When we couldn't give them what they wanted, their leader shot my mom between the eyes."
    ica "I... barely managed to get to the escape pod before they blasted the ship... I drifted through space for five days until I was rescued by an Alliance patrol."
    ica "In the end... I was the only survivor."
    ica "They all deserve to die for what they did... I've spent my whole life trying to avenge my family.  And I won't stop now."
    kay "You want to avenge your family by murdering a bunch of children?  You won't be any better than PACT if you did that."
    ica "... ... ..."
    ica "I know..."
    kay "I know a better way.  Our hangar bay's awfully empty, and we're looking for skilled pilots."
    kay "You play by our rules, and there might be a space for you onboard this ship."
    kay "We'll defeat PACT the right way, without harming any innocents."
    kay "It'll be a hard mission and we might all die trying, but I'd rather be dead than forget about what we're fighting to protect."

    show icari plugsuit neutral sadcry with dissolve

    ica "You'd still have me on your team? Even after all I've done?"
    kay "Everyone on this ship knows what it feels like to lose family.  Don't think for a second that you're alone."

    show icari plugsuit neutral smilecry with dissolve

    ica "I... never expected such kindness from you, captain. Perhaps... you're right. We can win this war without using the same methods as PACT."
    kay "There is a way to win. PACT won't get away with what they did to Cera, or your family. I'll make sure we all get payback."
    ica "All right... You have a deal. I'll help you defeat PACT... and in exchange, I'll play by your rules."

    show ava uniform armscrossed frowntalk with dissolve

    ava "Don't think this means I won't have my eyes on you, mercenary. You might have won over the captain's sympathy, but the instant you cause any trouble, I'll be throwing you in the brig."

    show asaga plugsuit armscrossed grumpy with dissolve

    asa "Oy Capt'n, you suppose putting this person on our ship is a good idea? She's already tried to slit our throats one too many times..."
    kay "We're all trying to stop PACT, aren't we? Besides, we'll need all the help we can get."

    show asaga plugsuit armscrossed sigh with dissolve

    asa "All right, I guess an extra wing mate isn't so bad... So long as she's aiming at PACT."

    show icari plugsuit neutral talkconcernblush with dissolve

    ica "I swear, I'll win your trust. We'll fight together from now."
    asa "Yeah... but I think I'll lock the doors when I sleep, just in case..."

    show chigara plugsuit handstogether forcedsmile with dissolve

    chi "Ah... W-welcome to the team, Icari... Eh-heh..."
    chi "Let's try to get along well from now, alright? No more fighting..."

    show asaga plugsuit handsonhips happy with dissolve

    asa "Ah well, now that that's over, let's grab some grub! I'm hungry!"

    show ava uniform facepalm with dissolve

    ava "Unbelievable..."

    show asaga plugsuit handsonhips laugh with dissolve

    asa "Haahhahahaha! C'mon capt'n! Come join me and Chigara! We have so much to talk about!"
    kay "Well Ava, looks like you'll be taking a break. And Icari, you too."

    show icari plugsuit armscrossed tsunblush with dissolve

    ica "S-seriously... I guess I have no choice then..."

    hide chigara with dissolve
    hide asaga with dissolve
    hide icari with dissolve
    hide ava with dissolve

    "With that, the team walked upstairs to the star lounge to celebrate their latest victory."
    "While the clouds of war which loomed in the distance were darker than ever, tonight they had something to celebrate."

    window hide
    scene black with dissolve
    scene cg_album:
        ease 5.0 xpos -0.3
    with dissolvelong

    pause 8.0

    jump ep3_start

label ep3_start:

    #try to remove the agamemnon from the game
    python:

        res_location = "lab"
        res_event = "allocatefunds"
        try:
            a,b = agamemnon.location
            BM.grid[a-1][b-1] = False
            BM.ships.remove(agamemnon)
            player_ships.remove(agamemnon)
            del agamemnon  #deletes the last traces. the variable will henceforth not even be defined, as though it was never used.
        except:
            pass
#            show_message('debug: there was an error removing the agamemnon. maybe it already was.')


    $ renpy.pause (0.1)

    window hide

    stop music fadeout 1.5

    show eyecatch_top with eyecatch_wipe
    show eyecatch_bottom with eyecatch_wiperev
    show eyecatch_logo with dissolve
    $ renpy.pause (2.0)
    scene bg black2 with dissolvelong
    scene bg captainsloft with dissolvelong

    window show

    play music "Music/Moonlit_Night.ogg"

    scene cg_avateatime with dissolve

    "Ava relaxed on the sofa as Shields brought a tray of tea to the table."
    kay "I've been meaning to use this tea set. There you go. Fresh out of the box."
    ava "I didn't know you were into tea."
    kay "Heh, I'm not nearly sophisticated enough. It was a little going away gift from family for my commission."
    "Ava raised her tea cup and took a sip. Steam wafted up as she held the cup in her hand."
    ava "It's been awhile since we could talk like this."
    kay "Reminds me of the old times, when we used to play cards in the student council room."
    ava "I'm surprised you even remember. It's been so many years since then."
    kay "I guess seeing you again made me nostalgic. You know, you haven't really changed much since those days."
    ava "Well, things are different now, captain."
    ava "Back then, you were the one following me."

    menu:
        "I guess I just wanted to see you in action.":
            jump guessseeaction

        "Someone had to keep you out of trouble.":
            jump someonekeepouttrouble

label guessseeaction:

    ava "Hm?"
    kay "You were always in motion. Getting things done. I guess I was a bit in awe."
    kay "Maybe I wanted to watch you and learn from the best."
    ava "It's strange, hearing you say that now."

    menu:
        "That was then. Things are different now.":
            jump thenthingsdifferent

        "Do you ever think about what it'd be like if you sat in the captain's seat instead?":
            jump everthinkcaptainsseat

label someonekeepouttrouble:

    ava "Ah, was that what it was?"
    kay "Of course. You were always trying to solve other people's problems. It was only a matter of time until you hurt yourself."
    ava "Heh. Alright, I won't deny that."
    kay "Remember your campaign slogan? Something about being the duty of the student council president to solve the student body's troubles?"
    ava "I guess... Things were simpler back then."
    ava "You're right. I did try too hard. And in the end, I just left disappointed."
    kay "Disappointed? You never told me that."
    ava "I wanted to do more. It was a chance to turn the entire school around. I thought I could really make a difference."
    ava "Heh. But people don't like change. Those that stand out are just naturally made the target of scorn."
    ava "I guess despite everything I did, I was forgotten. Just like all the class presidents before me."

    jump highschooldayslaugh

label thenthingsdifferent:

    ava "Understood. I'm your first officer before anything else, captain."

    jump highschooldayslaugh

label everthinkcaptainsseat:

    ava "... ... ..."
    ava "No."
    ava "I'm your first officer. There's nothing more to it than that."
    ava "I'll execute your orders, captain. That's all there is to it."

    jump highschooldayslaugh

label highschooldayslaugh:

    ava "... ... ..."
    ava "Hahahaha."
    kay "What? What's so funny?"
    ava "Look at me. We're in the middle of a war, and here I am, reminiscing about high school."
    ava "I thought the problems I had back then were insurmountable. And now, here we are, a one ship army against the entire PACT Empire. Kind of makes our high school problems seem like a joke, doesn't it?"
    kay "Hah. Well, we were just kids. I'm sure back then, our problems were as big as the Veniczar himself."

    if Saveddiplomats == True:
        jump tookindstopstopmism

    if Saveddiplomats == False:
        jump solongagoentangled

label tookindstopstopmism:

    ava "You're too kind. Considering our situation, I wonder if it's time for you to drop your optimism and start making the hard calls."
    kay "What do you mean?"
    ava "We're not in high school any more. It's a war out there."
    ava "Compassion may mean death on the battlefield. As captain, you'll have to put all of us in danger. You can't let your personal feelings interfere with what needs to be done."
    kay "As captain, it's my job to keep all of you safe. I wouldn't be able to do that unless I considered my feelings."
    ava "Alright. It's your ship. It's just something to keep in mind, that's all."

    jump guessjustmoveonthose

label solongagoentangled:

    ava "It seems like so long ago. Now, we're entangled in Alliance conspiracies and too busy counting the dead."
    kay "This war's already a piece of hell."
    kay "It's barely even been a month and it's claimed far too many lives."
    ava "Everything you've did was for the greater good."
    ava "None of us wants to see more lives taken by PACT. The crew's behind you in stopping this conflict as quickly as possible."
    kay "Still doesn't make sleeping any easier."

    jump guessjustmoveonthose

label guessjustmoveonthose:

    ava "I guess we'll just have to move on from those days. It's not like we can ever go back now."
    kay "... ... ..."
    kay "PACT will pay for what they've done to our home."
    ava "To tell the truth, I'd rather not think about it. All the people we've lost. All the memories destroyed."
    kay "... ... ..."
    ava "I'm sorry. Pretty much the whole crew's lost someone close to them."

    menu:
        "We'll kill the Veniczar for this. It's the only way justice can be done.":
            jump killveniczaronlyjustice

        "We have to stop PACT, so that what happened on Cera will never happen again.":
            jump stoppactwhathappenednever

label killveniczaronlyjustice:

    $ captain_prince += 1
    ava "Understood, sir. I'll be right behind you every step of the way."

    menu:

        "Give me your thoughts on the crew.":
            jump givemethoughtscrew
        "Thanks for the chat. I should get back to work.":
            jump thankschatback

label stoppactwhathappenednever:

    $ captain_moralist += 1
    ava "Understood, sir. I'll be right behind you every step of the way."

    menu:

        "Give me your thoughts on the crew.":
            jump givemethoughtscrew
        "Thanks for the chat. I should get back to work.":
            jump thankschatback

label givemethoughtscrew:

    ava "A motley bunch, I'll give you that."
    ava "Asaga's been stirring up every sort of trouble you could imagine. I caught her gambling with the crew just the other day."

    menu:
        "Oh come on, what's wrong with a little game of cards now and then?":
            jump whatswronggamecard

        "I presume you've dealt with her?":
            jump presumedealther

label whatswronggamecard:

    $ supportedasagacards = True

    ava "Captain, military protocol mandates that gambling be strictly-"
    kay "Try to loosen up a bit, Ava. Our pilots need to blow off some steam now and then."
    ava "Well, if that's your order."
    kay "No, Ava… You know that military protocol doesn't mean much now that Cera's a PACT colony."
    kay "I didn't think the protocols for the situation we're in now even exist."
    ava "That is unfortunate. However, someone must enforce discipline on this ship."
    kay "All right… Just don't push yourself too hard, alright? Relax every now and then."
    ava "Understood, captain."
    kay "(She still totally doesn't get what I mean…)"

    menu:
        "How's Chigara been doing?":
            jump howschigarabeendoing
        "How's our mercenary been adjusting?":
            jump howmercenaryadjust
        "Thanks for the chat. I should get back to work.":
            jump thankschatback

label howschigarabeendoing:

    ava "Things have been going much better with her. I must say I'm impressed. She's really turned engineering around. You should go check out her research lab."
    kay "Sounds good."

    menu:
        "How's our mercenary been adjusting?":
            jump howmercenaryadjust
        "Thanks for the chat. I should get back to work.":
            jump thankschatback

label howmercenaryadjust:

    ava "Better than I thought she would. She's been helping us fix the bugs in our security systems. Maybe I was wrong about her."
    kay "Good to hear."

    menu:
        "How's Chigara been doing?":
            jump howschigarabeendoing
        "Thanks for the chat. I should get back to work.":
            jump thankschatback

label presumedealther:

    ava "Right. I've restricted her to eating rations for the next week."

    menu:
        "How's Chigara been doing?":
            jump howschigarabeendoing
        "How's our mercenary been adjusting?":
            jump howmercenaryadjust
        "Thanks for the chat. I should get back to work.":
            jump thankschatback

label thankschatback:

    ava "As should I."
    kay "We should have these talks more often. I could put my tea set to use."

    play music "Music/Mission_Briefing.ogg" fadeout 1.5

    $ captaindeck = 0
    $ asa_location = "messhall"
    $ asa_event = "ep3_asatalk"

    $ chi_location = "engineering"
    $ chi_event = "ep3_chitalk"

    $ ica_location = "hangar"
    $ ica_event = "ep3_icatalk"

    $ pro_location = "bridge"
    $ pro_event = "missionfromryuvians"

    $ res_location = "lab"
    $ res_event = "allocatefunds"

    $ gal_location = None
    jump dispatch

label ep3_asatalk:

    hide screen ship_map
    scene bg messhall
    show asaga uniform neutral happy
    with dissolve

    window show

    asa "Oh, did you need me for something, capt'n?"

    menu:
        "What are your thoughts about what happened with Icari?":
            jump thoughtshappenedicari

        "How are you adjusting to the Sunrider?":
            jump howasaadjustsunrider

        "Actually, nevermind.":
            jump gostaytroubleasaga

label howasaadjustsunrider:

    show asaga uniform armscrossed talk with dissolve

    asa "Eh, I think it's going pretty well. Warm food and a bed to sleep on, anyways. The Sunrider's also much cleaner than Chigara's workshop."

    show asaga uniform armscrossed sad with dissolve

    asa "Uuu... I really wish the first officer would stop chewing me out though..."
    kay "What happened?"
    asa "Well, first I tried to hook up my Game Master to the holovision in the lounge. Ugh, you won't imagine how red her face was when she told me off for that. Something about contaminating the ship's electronics."
    asa "And then, I tried playing some Duel Creatures with Chigara in the crew quarters. And then she comes marching in, saying no card games. Bleh..."

    if supportedasagacards:
        jump alreadyspokeavano
    else:
        jump weremilitarynow

label alreadyspokeavano:

    $ affection_asaga += 1

    kay "I've already spoken to Ava about it. She won't be giving you any more trouble."

    show asaga uniform excited grin with dissolve

    asa "Really? Ahaha, you're the best, capt'n!"
    kay "Just try to keep it in moderation, alright?"

    show asaga uniform neutral smile with dissolve

    asa "Understood..."

    menu:
        "What are your thoughts about what happened with Icari?":
            jump thoughtshappenedicari

        "I should go. Try to stay out of trouble, Asaga.":
            jump gostaytroubleasaga

label weremilitarynow:

    kay "You're on a military vessel now. I like to run a tight ship."
    asa "Understood..."

    menu:
        "What are your thoughts about what happened with Icari?":
            jump thoughtshappenedicari

        "I should go. Try to stay out of trouble, Asaga.":
            jump gostaytroubleasaga

label thoughtshappenedicari:

    if Saveddiplomats == False:

        show asaga uniform armscrossed sad with dissolve

        asa "I've been thinking about what happened, and I just don't feel good about it."
        asa "It's good that the Alliance is finally stepping up and getting ready to help us. But I can't believe we had to do something so horrible to get their help."

        show asaga uniform armscrossed mad with dissolve

        asa "I fly the Black Jack to protect innocents, captain. Letting those children die was wrong."

        menu:
            "I can't say it's been easy sleeping. But their deaths will not be in vain.":
                jump sleepingdeathsnotvain

            "This is war, Asaga.  War cannot be won without sacrifice.":
                jump warasagasacrifice

    if Saveddiplomats == True:

        show asaga uniform altneutral talk with dissolve

        asa "I'm glad we managed to save those kids, but I'm not so sure about keeping the mercenary."

        show asaga uniform armscrossed frown with dissolve

        asa "Eh... I'm not so sure about having a person like that on our team. Nobody should shoot at civilians."

        menu:
            "Icari had her reasons. It's not always so black and white, Asaga.":
                jump herreasonsblackasaga
            "I'm still keeping my eyes on her. If she causes any more trouble, I'll drop her off on the nearest rock.":
                jump stilleyesdroprock


label sleepingdeathsnotvain:

    show asaga uniform armscrossed frown with dissolve

    asa "I guess..."
    asa "I just hope something like that doesn't ever happen again."
    asa "Sigh..."

    jump supposedtohelp

label warasagasacrifice:

    show asaga uniform handsonhips shoutmad with dissolve

    asa "Don't think I don't know that already!"

    show asaga uniform neutral lookawayfrown with dissolve

    asa "W-well, I don't... But..."

    show asaga uniform armscrossed shoutclosedeyes with dissolve

    asa "Argh, nevermind..."

    jump supposedtohelp

label herreasonsblackasaga:

    show asaga uniform armscrossed frown with dissolve

    asa "Whatever her reasons were, shooting at kids is just too far."
    asa "You can't do something like that and still say you're one of the good guys. Anyone willing to stoop down to that level's no better than PACT!"

    jump guessnotstillsame

label stilleyesdroprock:

    show asaga uniform armscrossed confident with dissolve

    asa "Hmph. I'll tell you right away if I catch her stirrin' up trouble, capt'n!"

    jump guessnotstillsame

label supposedtohelp:

    show asaga uniform altneutral sad with dissolve

    asa "I was supposed to help those kids. That's why I decided to become a freelancer. To stand up for people who were being oppressed by PACT."
    asa "It's just... Disappointing. I've let those kids down."

    show asaga uniform neutral lookawayfrown with dissolve

    asa "And well, I guess they're not really around to give me a second chance, are they?"

    menu:
        "How are you adjusting to the Sunrider?":
            jump howasaadjustsunrider

        "I should go. Try to stay out of trouble, Asaga.":
            jump gostaytroubleasaga

label guessnotstillsame:

    show asaga uniform armscrossed talk with dissolve

    asa "Anyways, I guess it's not all bad since she is a good pilot and all. But still, just because we're on the same team doesn't mean we have to be friends."
    asa "By the way capt'n, did you find out what happened to those kids?"
    kay "They've been placed in Alliance protection. Versta's been annexed by PACT, so it's the best place for the kids right now."
    kay "With all the political attention the rescue's caused, you can bet they'll be well taken care of by the Alliance."

    show asaga uniform excited grin with dissolve

    asa "I guess it's for the best. Let's hurry up and kick PACT out of the Neutral Rim so that we can get those kids back to their parents!"
    kay "One step at a time, Asaga..."

    menu:
        "How are you adjusting to the Sunrider?":
            jump howasaadjustsunrider

        "I should go. Try to stay out of trouble, Asaga.":
            jump gostaytroubleasaga

label gostaytroubleasaga:

    show asaga uniform neutral happy with dissolve

    asa "Understood, capt'n!"

    jump dispatch

label ep3_chitalk:

    hide screen ship_map
    scene bg engineering
    show chigara uniform handsup surprise
    with dissolve

    window show

    chi "E-eah! Oh, sorry captain, I didn't see you coming there!"

    show chigara uniform handonchest forcedsmileblush with dissolve

    chi "Ehheh... T-that must be the third time that's happened..."
    kay "Sorry. You really get focused in your work, huh?"
    chi "Whenever I'm working on something, I tend to lose awareness of everything else..."

    show chigara uniform handstogether smile with dissolve

    chi "Was there something you needed, captain?"

    menu:
        "How are you adjusting to the Sunrider?":
            jump howchiajustsunrider
        "What do you think about what happened with the mercenary?":
            jump whatchimercenary
        "Keep up the good work, Chigara. I'll talk to you later.":
            jump keepgoodchilater

label howchiajustsunrider:

    show chigara uniform handonchest smile with dissolve

    chi "The Sunrider's a wonderful vessel. In fact, I don't think I've ever been on a ship as advanced in my life."
    chi "In fact, I was just running some energy conversion models the other day and I can say that the Sunrider's core drive is one of the most efficient in the galaxy."
    chi "Since the Sunrider's powered through atomic fusion, we don't have to worry about radiation management. Now, I think if I were to upgrade the fuel feeder with..."

    show chigara uniform palmsup embarrasssurprise with dissolve

    chi "O-oh! I'm sorry, I didn't mean to bore you with techno babble... Er, I mean, y-you must be busy, so, erm... Uhh... What were we talking about again? "
    chi "C-can you please repeat your question?"

    menu:
        "Calm down, Chigara. I was just asking how you were doing.":
            jump calmchigaraaskingdoing

        "Actually, I was thinking of upgrading the fuel feeder with the new paraxium coating too.":
            jump actuallyparaxiumcoating

label calmchigaraaskingdoing:

    show chigara uniform handonchest smileblush with dissolve

    chi "O-oh! Everything's good actually!"

    show chigara uniform handstogether smile with dissolve

    chi "The first officer's helped me move in all of my things. I even managed to improve the research lab here in engineering too."
    kay "I'm glad to hear that."

    menu:
        "What do you think about what happened with the mercenary?":
            jump whatchimercenary
        "Keep up the good work, Chigara. I'll talk to you later.":
            jump keepgoodchilater

label actuallyparaxiumcoating:

    show chigara uniform handonchest ooscienceblush with dissolve

    chi "Eh? You mean you knew about the mark II?"
    kay "That just came out a week ago, didn't it?"

    show chigara uniform handstogether smileblush with dissolve

    chi "Ooohh... I didn't know captain was a gearhead too."
    kay "They wouldn't give me the keys to this ship without me knowing something about it."
    chi "I guess that's true. Ehehe..."

    menu:
        "What do you think about what happened with the mercenary?":
            jump whatchimercenary
        "Keep up the good work, Chigara. I'll talk to you later.":
            jump keepgoodchilater

label whatchimercenary:

    if Saveddiplomats == True:

        show chigara uniform neutral neutral with dissolve

        chi "Mm... So long as Icari's going to be working with us, I guess I don't see a big problem."
        chi "I haven't really spoken with her much since, but I think she regrets what she did."

        show chigara uniform handstogether smile with dissolve

        chi "I hope we can work together to stop PACT..."

        menu:
            "How are you adjusting to the Sunrider?":
                jump howchiajustsunrider
            "Keep up the good work, Chigara. I'll talk to you later.":
                jump keepgoodchilater

    if Saveddiplomats == False:

        show chigara uniform handonchest sad with dissolve

        chi "It was terrible seeing all those kids die..."
        chi "I..."
        chi "It's not the first time I've seen something like that happen. But you never get used to it."
        chi "I guess it's unavoidable that innocents die in war."
        chi "That's why I like machines. You can fix them back up even after they break."

    menu:
        "How are you adjusting to the Sunrider?":
            jump howchiajustsunrider
        "Keep up the good work, Chigara. I'll talk to you later.":
            jump keepgoodchilater


label keepgoodchilater:

    show chigara uniform altneutral neutral with dissolve

    chi "Good bye captain."

    jump dispatch

label ep3_icatalk:

    hide screen ship_map
    scene bg hangar
    show icari uniform handonhip neutral
    with dissolve

    window show

    ica "Captain."

    if Saveddiplomats == True:
        menu:
            "So what exactly did you do as a mercenary, Icari?":
                jump whatdomercenaryica

            "I noticed you liked swords.":
                jump noticedlikedswords

            "How are you adjusting to the Sunrider?":
                jump howicaadjustsunrider

            "Your ryder was smashed up pretty badly last time. Is it operable?":
                jump rydersmashedlastoper

    if Saveddiplomats == False:
        menu:
            "So what exactly did you do as a mercenary, Icari?":
                jump whatdomercenaryica

            "I noticed you liked swords.":
                jump noticedlikedswords

            "How are you adjusting to the Sunrider?":
                jump howicaadjustsunrider

label whatdomercenaryica:

    ica "Don't think I was just some goon for hire. I only took out PACT targets."
    ica "Blew up a couple refueling stations here and there. Sank some crippled cruisers. Even impersonated a low level PACT veniczar once."
    kay "I can't really imagine you as a veniczar."

    show icari uniform bothhandsonhips grin with dissolve

    ica "I had to put on a special latex suit to make myself look 80 pounds fatter. Haha."
    kay "Uh, wow. So what exactly were you doing?"

    show icari uniform armscrossed smilesidesmile with dissolve

    ica "It was a slave sale bust. The Alliance hired me to bust a transaction between a pirate cell and this PACT veniczar."
    ica "PACT's been... Ah, liberating slaves by paying off their slavers. In exchange for serving as personnel on their ships, of course."
    ica "This was going to be one of the biggest sales ever. Nearly 200 adults. The Alliance got involved when PACT accidentally included a citizen in the group."
    ica "I guess they forgot to check their passports or something."
    kay "So you just impersonated the veniczar to pay the pirates off and free the slaves after?"

    show icari uniform handonhip neutral with dissolve

    ica "Tsch. If only if it were simple. You see, the cheapskates at the Alliance were only willing to pay to free their own citizen. Something about not wanting to fund piracy."
    ica "Anyways, that was all irrelevant, since it was a double cross and the pirates were planning to slit the veniczar's throat after they got the money anyways."
    ica "Got grazed by a couple of their shots, which melted through my latex suit. That was a sight to see."
    kay "I bet... So how did you get out of that alive?"

    show icari uniform altneutral smile with dissolve

    ica "I swapped places with the real veniczar just as she arrived. Haha, you should have seen the look on her face as the pirates grabbed her."
    ica "Meanwhile, all the slaves got loose. It was total pandemonium in there."
    ica "Finally, the pirates opened fire on the PACT star liner, spacing everyone on board."

    show icari uniform armscrossed smilesidesmile with dissolve

    ica "I don't know what happened to the slaves. I managed to get the Alliance citizen out of there though, and in the end, that's all that mattered to my clients."

    menu:
        "That's pretty crazy. I can't believe you made it out of that in one piece.":
            jump crazybelieveonepiece
        "So you couldn’t save the slaves in the end?":
            jump couldntsaveend

label crazybelieveonepiece:

    show icari uniform bothhandsonhips grin with dissolve

    ica "Hahaha, and that's what I loved about mercenary work. It's my life or theirs. No time to stop and contemplate on philosophical questions."

    jump prettymuchmerclike

label couldntsaveend:

    ica "No. But I still took down a veniczar and a PACT star liner, so I'd call it a good day. "

    jump prettymuchmerclike

label prettymuchmerclike:

    show icari uniform handonhip neutral with dissolve

    ica "Anyways, that's pretty much what being a mercenary was like. It was risky work, but I liked the excitement. It kept my mind off other things."

    if Saveddiplomats == True:
        menu:
            "I noticed you liked swords.":
                jump noticedlikedswords

            "How are you adjusting to the Sunrider?":
                jump howicaadjustsunrider

            "Your ryder was smashed up pretty badly last time. Is it operable?":
                jump rydersmashedlastoper

            "I need to get going.":
                jump dispatch

    if Saveddiplomats == False:
        menu:
            "I noticed you liked swords.":
                jump noticedlikedswords

            "How are you adjusting to the Sunrider?":
                jump howicaadjustsunrider

            "I need to get going.":
                jump dispatch

label noticedlikedswords:

    show icari uniform handonhip neutral with dissolve

    ica "In the ancient times, they said the invention of gunpowder ended the age of swordsplay. Well, the creation of personal shielding's brought it back."
    ica "Now that people can emit shields that can deflect small arms, the only way to take them down in to draw your sword and get up close and personal with them."
    kay "Have you ever killed someone with your sword in person?"
    ica "Couple of PACT soldiers and pirates. When they pop up personal shielding, it's the best way to take them down."

    menu:
        "Sounds barbaric to me.":
            jump soundsbarbaric
        "Sounds like a good strategy. I'll keep it in mind.":
            jump soundsgoodkeepmind

label soundsbarbaric:

    show icari uniform handonhip snide with dissolve

    ica "Heh. Real world's different from officer school, captain. A lot less clean."
    jump stillmostfaces

label soundsgoodkeepmind:
    ica "It gets the job done, that's for sure."
    jump stillmostfaces

label stillmostfaces:

    show icari uniform handonhip neutral with dissolve

    ica "I can still remember most of their faces. It definitely makes you think about what you're doing more than pressing a button and firing a rocket at an enemy space ship."
    ica "They were armed enemies though. It was either their lives or mine."
    kay "Right."

    if Saveddiplomats == True:
        menu:
            "So what exactly did you do as a mercenary, Icari?":
                jump whatdomercenaryica

            "How are you adjusting to the Sunrider?":
                jump howicaadjustsunrider

            "Your ryder was smashed up pretty badly last time. Is it operable?":
                jump rydersmashedlastoper

            "I need to get going.":
                jump dispatch

    if Saveddiplomats == False:
        menu:
            "So what exactly did you do as a mercenary, Icari?":
                jump whatdomercenaryica

            "How are you adjusting to the Sunrider?":
                jump howicaadjustsunrider

            "I need to get going.":
                jump dispatch


label howicaadjustsunrider:

    ica "I'm satisfied with my current accommodations. It's much better than what I'm used to. Thanks for your concern."

    if Saveddiplomats == True:
        menu:
            "So what exactly did you do as a mercenary, Icari?":
                jump whatdomercenaryica

            "I noticed you liked swords.":
                jump noticedlikedswords

            "Your ryder was smashed up pretty badly last time. Is it operable?":
                jump rydersmashedlastoper

            "I need to get going.":
                jump dispatch

    if Saveddiplomats == False:
        menu:
            "So what exactly did you do as a mercenary, Icari?":
                jump whatdomercenaryica

            "I noticed you liked swords.":
                jump noticedlikedswords

            "I need to get going.":
                jump dispatch


label rydersmashedlastoper:

    show icari uniform armscrossed lookawayannoyed with dissolve

    ica "Not without a bunch of repairs. Your pilot was pretty thorough about taking it down."
    kay "You're lucky you didn't get spaced. Asaga may look silly, but she's pretty dangerous with a ryder."

    show icari uniform armscrossed smilesidesmile with dissolve

    ica "Heh. That so? I wouldn't mind having a rematch. On the simulator, of course, captain."

    show icari uniform handonhip neutral with dissolve

    ica "Thankfully, your girl in engineering managed to fix most of the damage. She's really something. I've never seen someone as talented as her."
    kay "Chigara's one of the best minds in the galaxy. We're lucky to have her on our team."

    show icari uniform altneutral smile with dissolve

    ica "Good thing we're on the same side now. You've got a pretty good crew here."

    show icari uniform armscrossed sad with dissolve

    ica "... ... ..."

    show icari uniform armscrossed tsun with dissolve

    ica "Tsch. I can't believe I said that out loud."

    show icari uniform point embarassed tsun with dissolve

    ica "W-what!? Talk about something else before I embarrass myself even more!"

    menu:
        "So what exactly did you do as a mercenary, Icari?":
            jump whatdomercenaryica

        "I noticed you liked swords.":
            jump noticedlikedswords

        "How are you adjusting to the Sunrider?":
            jump howicaadjustsunrider

        "I need to get going.":
            jump dispatch

label missionfromryuvians:

    hide screen ship_map
    scene bg bridge
    show ava uniform neutral neutral
    with dissolve

    ava "Captain, I've just received a message from the neutral world of Ryuvia."
    kay "Ryuvia? You mean we've been contacted by royalty?"
    ava "Correct. Ryuvia's one of the oldest nations in the galaxy, with a history going back for over 10 000 years. In fact, some historians say that Ryuvia might even have been the birth place of humanity."
    kay "Let's hear what they've got to say. Put them on screen."

    show ava uniform neutral neutral:
        zoom 1.0
        ease 0.5 xpos 0.3
    pause 0.01
    show king:
        xpos 0.7
    with wipeup

    ryu "Hail Sunrider. I am King Jaylor di Ryuvia."
    kay "Greetings, your highness. I'm Captain Kayto Shields of the starship Sunrider. This is my First Officer, Ava Crescentia."
    ryu "I have heard of your deeds in the Neutral Rim, and believe you may be of help."
    ryu "There is a treasure known to our people which we seek to retrieve from the Nomodorn Corridor. Perform well, and we shall bestow you with great riches."
    kay "What are you looking for?"
    ryu "The crown jewel of Ryuvia."
    kay "The crown jewel? I presume it's of value?"
    ryu "The kingdom of Ryuvia holds many secrets, captain. You have our request. I shall be waiting."

    hide king with wipedown

    kay "Uh, that's it? Not much to go off of, is it?"

    show ava uniform armscrossed neutral:
        ease 0.5 xpos 0.5

    ava "Well, maybe this might shed some light on the matter."
    kay "What?"
    ava "The rumor on the streets of Ryuvia is that the princess has been missing."
    kay "The princess? And what's the crown jewel have to do with that?"
    ava "I've been doing some research on Ryuvian treasures, and I came across this book."
    kay "The Lost Technology Catalogue?"
    ava "It's an encyclopedia of various Ryuvian treasures that have gone missing throughout history."
    ava "According to this book, the crown jewel isn't a carved gem, but rather a highly advanced crystalline device which can pin point the location of royal blood across astronomical distances."
    kay "Ah... And let me guess, the Ryuvians want this crown jewel to help find their princess?"

    show ava uniform handonhip neutral with dissolve

    ava "Bingo. At least, that's the best explanation I can think of."

    menu:
        "Debrief me on King Jaylor and the Ryuvians.":
            jump debriefkingryuvians

        "Why would the Ryuvians invent such a crazy device in the first place?":
            jump whyryuvianscrazyplace

        "Tell me more about Lost Technology.":
            jump morelosttech

        "Well, since we could use the money, we might as well help the Ryuvians get their crown jewel back.":
            jump moneyhelpcrownback

label debriefkingryuvians:

    show ava uniform handonhip neutral with dissolve

    ava "A long time ago, the Ryuvian Empire stretched across the galaxy, its vast military powered by technologies which have become long forgotten."
    ava "It was a vast and mighty empire, where culture and the sciences flourished."
    ava "But their glory days could not last forever. Legend speaks of a vast calamity that shook the core of the Ryuvian Empire and caused its ultimate collapse."
    ava "The formation of the Solar Alliance further degraded Ryuvia's power, and today, all that is left of its former glory is the sole planet of Ryuvia. "
    ava "You can still find pieces of their former empire scattered throughout the galaxy though. Many archeologists and space explorers seek to find Ryuvian treasures, which may hold the secret to unlocking the power of their lost technology."

    menu:
        "Why would the Ryuvians invent such a crazy device in the first place?":
            jump whyryuvianscrazyplace

        "Tell me more about Lost Technology.":
            jump morelosttech

        "Well, since we could use the money, we might as well help the Ryuvians get their crown jewel back.":
            jump moneyhelpcrownback

label whyryuvianscrazyplace:

    show ava uniform alt neutral neutral with dissolve

    ava "Dynastic succession. During ancient times, whoever succeeded the Ryuvian throne essentially ruled the galaxy. Needless to say, there were many imposters who claimed the throne."
    ava "The crown jewel of Ryuvia was made with the utmost precision to detect royal blood. You could even say the fate of the galaxy depended upon its accuracy."
    ava "Much of what we've dug up of the ancient Ryuvian's technology escapes comprehension though. Some of the details of the device may never be understood."

    menu:
        "Debrief me on King Jaylor and the Ryuvians.":
            jump debriefkingryuvians

        "Tell me more about Lost Technology.":
            jump morelosttech

        "Well, since we could use the money, we might as well help the Ryuvians get their crown jewel back.":
            jump moneyhelpcrownback

label morelosttech:

    show ava uniform neutral neutral with dissolve

    ava "It's ancient technology left behind by the former Ryuvian Empire."
    ava "A long time ago, even before the formation of the Solar Alliance, the Ryuvian Empire conquered the entire galaxy using technology we could not even conceive of."
    ava "When their empire collapsed, much of their technology was lost in the ensuing chaos."
    ava "You could say that humanity's scientific knowledge peaked at the height of the Ryuvian Empire, and with its collapse, entered into a dark age."
    ava "We've been trying to catch up to the Ryuvian's level of sophistication ever since, but it'll still take decades until we have anything as good as the ancient Ryuvians."
    ava "We call the pieces of technology left by the ancient Ryuvians Lost Technology. Whenever one is found, it can dramatically change the power balance of the galaxy."

    menu:
        "Debrief me on King Jaylor and the Ryuvians.":
            jump debriefkingryuvians

        "Why would the Ryuvians invent such a crazy device in the first place?":
            jump whyryuvianscrazyplace

        "Well, since we could use the money, we might as well help the Ryuvians get their crown jewel back.":
            jump moneyhelpcrownback

label moneyhelpcrownback:

    show ava uniform neutral neutral with dissolve

    ava "Understood captain. I've punched in the coordinates for the Nomodorn Corridor. Just set our course on the star map and we'll be underway."

    $ warpto_nomodorn = True
    $ amissionforalliance = False
    $ missionforryuvia = True

    $ captaindeck = 1
    $ gal_location = "bridge"
    $ pro_location = None

    jump dispatch

label jumptonomodorn:

    $ warpto_nomodorn = False

    $ Random = renpy.random.randint(1,9)

    if Random == 1:
        scene space back1
    if Random == 2:
        scene space back2
    if Random == 3:
        scene space back3
    if Random == 4:
        scene space back4
    if Random == 5:
        scene space back5
    if Random == 6:
        scene space back6
    if Random == 7:
        scene space back7
    if Random == 8:
        scene space back8
    if Random == 9:
        scene space back9

    show sunrider_warpout_standard:
        xpos 700 ypos 350
    with dissolve

    pause 1.0

    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_standard_flash:
        xpos 426 ypos 0 alpha 0
        linear 0.1 alpha 1
        linear 0.1 alpha 0
    show sunrider_warpout_standard out:
        xpos 700 ypos 350
        ease 0.2 xpos 200 ypos 300 zoom 0

    pause 1.0

    scene map_nomodorn:
        ypos 0
        ease 1.5 ypos -120
    with dissolve
    pause 1

    show sunrider_warpout_standard out:
        xpos 2300 ypos 1200 zoom 2
        ease 0.2 xpos 1000 ypos 500 zoom 0.5
    pause 0.2
    play sound "Sound/large_warpout.ogg"
    show cg_legionwarpin_missilefrigate_warpflash:
        zoom 1.5 xpos 1550 ypos 750
    show sunrider_warpout_standard

    pause 2.0

    scene bg bridge
    show ava uniform alt neutral neutral
    with fade

    window show

    ava "Warp successful, captain. We are arriving at the Nomodorn Corridor."
    kay "This is going to be like trying to find a needle in a haystack. Any ideas where we should start looking?"
    ava "The nearest planet in this sector is the neutral world of Tautenia.  It's what we call a dark planet, or a world where technology has fallen to pre-warp era levels. We're talking civil unrest, violence, and warfare on the surface."
    ava "Nothing we need to worry about though. The Tautenian space force is... Kind of a joke."
    kay "Right. Keep our pilots on alert though. I want to be prepared for anything."
    ava "Aye sir."

    play music "Music/Driving_the_Top_Down.ogg" fadeout 1.5

    show ava uniform fistup angryshout with dissolve

    ava "Scratch that. Pirate signatures detected!"

    play sound "sound/redalert.ogg"
    scene bg bridgered
    show ava uniform fistup angryshout
    with dissolve

    kay "Red alert! Raise shields and power weapons! Ready all ryders for combat!"

    show asaga plugsuit excited happy:
        xpos 0.2
    with wipeup

    asa "We're all ready down here, capt'n!"

    show ava uniform alt neutral mad with dissolve

    ava "Wait a minute... I'm reading a distress beacon from another ship."
    kay "A Tautenian ship?"
    ava "No, it's Alliance. Civilian signature, designation \"Mochi.\" Possibly a transport vessel being targeted by the pirates."
    kay "Looks like this just turned into a rescue mission. Patch me through to our pilots."
    ava "Done."
    kay "Asaga, looks like it'll be a rescue mission this time. The pirates are targeting a civilian transport."

    show asaga plugsuit handsonhips happy with dissolve

    asa "Understood capt'n! We'll keep those civilians safe!"
    ava "The Sunrider will be vulnerable without our ryders. What are your orders, captain?"

    menu:
        "That's a risk that we'll have to take. I want all our ryders to go forward and save the civilian.":
            jump riskallforwardsave
        "The safety of the Sunrider comes first. Our ryders will stay back and escort the Sunrider.":
            jump safetyfirstwillescort

label riskallforwardsave:

    $ protectmochi = True
    $ captain_moralist += 2

    ava "Understood captain."

    jump oldfriendcosettetail

label safetyfirstwillescort:

    $ protectmochi = False
    $ captain_prince += 2

    ava "Understood captain."

    jump oldfriendcosettetail

label oldfriendcosettetail:

    kay "Our old friend Cosette Cosmos might be out there. Watch your tail, everyone."
    kay "All right! All units, launch!"

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide asaga
    hide battlewarning

    $ check1 = False
    $ check2 = False

    call mission9_inits
    $ BM.mission = 9
    jump battle_start

label mission9:

    if check1 == False:
        $BM.draggable = False

        show cosette plugsuit armscrossed happy onlayer screens:
            xpos 0.8
        with dissolve

        cos "Heh-heh, I didn't fancy seeing you again, captain..."
        kay "Ah, my favorite space pirate. I see you've still been skimping on the milk."

        play sound "sound/hit.ogg"

        show cosette plugsuit neutralalt yandereshock onlayer screens:
            ease 0.02 xpos 0.8
            ease 0.02 xpos 0.79
            ease 0.04 xpos 0.81
            ease 0.02 xpos 0.8
            repeat 5
        with dissolve

        cos "G-gurk..."
        cos "Y-you've interfered with my plans for the last time..."

        show cosette plugsuit point yanderegrin onlayer screens with dissolve

        cos "Kill him!"

        hide cosette onlayer screens with dissolve

        play sound "sound/objectives.ogg"
        "Objective: Protect the civilian transport."

        if Saveddiplomats == True:
            "Tip:  The Phoenix can briefly become immune to blindside attacks by going into stealth mode."

        $ check1 = True

        $ BM.draggable = True  #this enables dragging the viewport again.

    if check2 == False and BM.turn_count == 3:

        $BM.draggable = False

        python:
            create_ship(PactMook(),(8,2),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactBomber(),(9,2),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])
            create_ship(PactMook(),(8,15),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactBomber(),(9,15),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])
            create_ship(PactCruiser(),(18,8),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(18,6),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(MissileFrigate(),(5,2),[PactFrigateMissile()])
            create_ship(MissileFrigate(),(5,15),[PactFrigateMissile()])

        show cosette plugsuit point evilsmile onlayer screens:
            xpos 0.8
        with dissolve

        cos "Hahahaha! You won't win this time! We even brought in our friends from PACT!"
        kay "Working for the big bad now, huh? They say birds of the same feather flock together."

        hide cosette onlayer screens with dissolve

        show cullen onlayer screens:
            xpos 0.8
        with dissolve

        cul "Bwah-HAH-HAH! What do we have here? An uppity little rascal?"
        kay "That's Captain Kayto Shields of the starship Sunrider."
        cul "Bah! No matter! You are no match for I, the glorious Veniczar B. Cullen! I will rid the Neutral Rim of vermin like you and unify these poverty stricken worlds into our new galactic order!"
        kay "And where does orbital bombing millions of innocents fit into this unity of yours?"
        cul "Pah! The likes of you will never understand the necessities of war! Now en garde, captain! Allow me to show you the true power of PACT!"

        hide cullen onlayer screens with dissolve

        kay "(Looks like Veniczar Porkchops means business. We're heavily outnumbered here... Should we fall back?)"

        show cg_mochi 1 onlayer screens with dissolve

        ava "Captain, I'm reading weird readings coming from that civilian vessel."
        kay "Weird?"

        play sound "sound/mechchange.ogg"
        show cg_mochi 2 onlayer screens with dissolve

        ava "A sudden spike in power usage... Something inside it is coming online..."
        ava "Wait, this is-"

        show claude plugsuit fingeronlip kittysmile onlayer screens:
            xpos 0.8
        with dissolve

        cla "I guess it's time to get moving, huh...?"

        hide claude onlayer screens with dissolve

        show cg_mochi_bianca onlayer screens:
            xpos 0.5 ypos 0.3 zoom 0.2
            ease 1.0 xpos 0.0 ypos 0.0 zoom 1.0

        play sound1 "sound/Laser 1.ogg"
        show cg_mochi 4 onlayer screens with dissolve

        pause 0.1

        hide cg_mochi_bianca onlayer screens
        show cg_mochi 5 onlayer screens:
            ease 0.02 xpos 0.5
            ease 0.02 xpos 0.495
            ease 0.04 xpos 0.505
            repeat 12
        with dissolve
        play sound2 "sound/explosion2.ogg"

        pause 2.0

        hide cg_mochi onlayer screens

        show ava uniform alt neutral angry onlayer screens:
            xpos 0.8
        with dissolve

        python:
            BM.grid[13][6] = False
            BM.ships.remove(mochi)
            player_ships.remove(mochi)

        ava "Captain, a ryder! Hidden inside the storage compartment in the Alliance vessel!"

        python:

            bianca_weapons = [BiancaAssault(),GravityGun(),AccDown(),DamageUp(),Restore()]
            bianca = create_ship(Bianca(),(14,7),bianca_weapons)

        kay "Patch me through to her."
        kay "This is Captain Kayto Shields of the starship Sunrider, to the unidentified Alliance ryder. State your intentions."

        hide ava onlayer screens with dissolve
        show claude plugsuit altneutral neutral onlayer screens:
            xpos 0.8
        with dissolve

        cla "This is Claude Trillo. I was delivering some medical supplies to Tautenia when I was attacked by these pirates. I could sure use a hand here..."
        kay "(One extra ryder. This should even the odds.)"
        kay "All right, Claude. The Sunrider is at your service. Let's get these bogies off of you."
        play sound "sound/objectives.ogg"
        "New Objective: Defeat all enemies."

        hide claude onlayer screens with dissolve

        $BM.draggable = True

        $ check2 = True

    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission9 #loop back
    else:
        pass #continue down to the next label

label aftermission9:

    python:
        #this code will be useful if you shift-P through last battle
        if mochi in player_ships:
            BM.ships.remove(mochi)
            player_ships.remove(mochi)
            bianca_weapons = [BiancaAssault(),GravityGun(),AccDown(),DamageUp(),Restore()]
            bianca = create_ship(Bianca(),(14,7),bianca_weapons)


    hide screen commands
    hide screen battle_screen

    play music "music/The_Beginning_Of_The_Adventure.ogg"

    scene bg bridge with dissolve

    window show

    show cullen:
        xpos 0.8
    with wipeup

    cul "Fools! What are you doing!? How could you let yourself be beat by a single ship!?"
    kay "Looks like today's not your day, Veniczar Porkchops."
    cul "T-tsch... How dare you! I will not stand for this mockery!"
    cul "Mark my words... You will regret crossing me, captain!"

    show cosette plugsuit point evilsmile:
        xpos 0.5
    with wipeup

    cos "Hah! Your days are numbered now!"
    kay "I'm truly shaking in my boots."

    hide cullen with wipedown
    hide cosette with wipedown

    show ava uniform handonhip neutral with dissolve

    ava "The remaining enemy units are pulling back."
    kay "Good. Let them go for now."
    ava "Aye sir."
    kay "Let's bring our new friend on board."

    scene bg hangar with dissolve
    play music "Music/As_I_Figure.ogg" fadeout 1.5

    show claude plugsuit neutral kittyclosedeyessmile with dissolve

    cla "Pwahhh... That was close..."
    kay "Welcome aboard the Sunrider."

    show claude plugsuit excited hearteye with dissolve

    cla "Oooaaahh..."

    play sound "sound/chime.ogg"
    scene cg_shojocaptain with dissolve

    cla "M-my captain in shining armor..."

    show ava uniform facepalm:
        xpos 0.8
    with dissolve

    ava "Ugh... And so another bizarre being washes up on our hangar..."

    scene bg hangar with dissolve

    show claude plugsuit fingeronlips hearteyekittyblush with dissolve

    cla "O-oh my... Eh-heh... You're cuter in person than you looked on the monitor."

    menu:
        "What were you doing out here alone? This area of space is dangerous.":
            jump hereareaisdangerous

        "You don't look so bad yourself.":
            jump youlooksoyourself

label youlooksoyourself:

    $ affection_claude += 1

    show claude plugsuit fingerup smileblush with dissolve

    cla "Ahahaha, oh my. It's still too soon to be flirting with your damsel in distress, capt'n. Especially with a hangar full of other women watching."

    show ava uniform facepalm:
        xpos 0.7
    with dissolve

    ava "Captain! Just please get to business already! Arggghh!"

    show chigara plugsuit handonchest sadblush:
        xpos 0.3
    with dissolve

    chi "Uuuu... I guess the captain is into girls with big boobs, huh..."

    show asaga plugsuit thinking confident:
        xpos 0.12
    with dissolve

    asa "Shhh, Chigara... This could be a special form of interrogation!"

    show icari plugsuit armscrossed seriously:
        xpos 0.88
    with dissolve

    ica "Seriously..."

    hide asaga with dissolve
    hide chigara with dissolve
    hide ava with dissolve
    hide icari with dissolve

    jump hereareaisdangerous

label hereareaisdangerous:

    cla "I was just delivering some medical supplies to a clinic on Tautenia when I was stopped by those pirates. I imagine I would have been killed had you not arrived in time."

    show claude plugsuit handstogether hearteye with dissolve

    cla "Looks like I'm in your debt now, captain."
    kay "Medical supplies? But you don't look like a freighter pilot..."
    cla "Oh, no, no. I'm a doctor."
    kay "A doctor, huh? Well, that makes more sense."
    kay "Well, uh, aside from the ryder piloting part."

    show claude plugsuit fingerup smileblush with dissolve

    cla "Eh-heh... You pick strange skills like that up when you've stayed in the Neutral Rim too long."
    kay "Well then, we'll just drop you off at Tautenia and you can take a shuttle to the surface. Glad we could be of help."

    show claude plugsuit excited surpriseblush with dissolve

    cla "Oh, no, captain! I couldn't possibly leave without first repaying my debt."

    show claude plugsuit handstogether drool with dissolve

    cla "Eh-heh... not to mention it'd be a shame to leave a total hottie behind so soon..."
    kay "What's that?"

    show claude plugsuit excited surpriselaugh with dissolve

    cla "Oh, nothing, captain!"

    show claude plugsuit fingerup smileblush with dissolve

    cla "Say... I don't suppose you need a doctor on board this ship?"
    kay "Actually... We do! Our sickbay's been closed ever since we've left port without our doctor!"

    show claude plugsuit excited happyblush with dissolve

    cla "Ka-ching! Dr. Trillo at your service, captain!"
    kay "Haha, what good luck! Hey Ava, we finally have a doctor for our ship!"

    show claude plugsuit excited closedsmilelaugh with dissolve

    cla "Oh captain! I'm so glad we could meet!"
    kay "Nah, I'm glad you're here to help. Haha, I was getting worried about the sickbay!"

    show ava uniform facepalm:
        xpos 0.15
    with dissolve

    ava "...unbelievable. He's eating completely out of her hand."

    show asaga plugsuit handsonhips annoyed:
        xpos 0.7
    with dissolve

    asa "Uu-uwah... Chigara, I think you've met quite a formidable rival here..."

    show chigara plugsuit palmsup surpriseblush:
        xpos 0.85
    with dissolve

    chi "M-me? E-eh? Eehhh!?"

    $ asa_location = None
    $ chi_location = None
    $ ica_location = None
    $ ava_location = "bridge"
    $ ava_event = "dubious_credentials"
    $ pro_location = "sickbay"
    $ pro_event = "medical_examination"

    $ captaindeck = 2

    jump dispatch

label dubious_credentials:

    hide screen ship_map

    play music "Music/The_Rest_of_the_Ents.ogg" fadeout 1.5

    scene bg bridge
    show ava uniform armscrossed frowntalk
    with dissolve

    window show

    ava "Captain. A word with you."
    kay "Is there an issue?"
    ava "I've done some research into our new \"doctor.\" The only problem is that I can't find her medical license on the Alliance Medical Association's database."
    kay "Strange. Maybe she's licensed with a different medical organization?"

    show ava uniform handonhip neutral with dissolve

    ava "Possibly. Despite the AMA being the most reputable, many neutral planets run their own medical licensing schemes."
    ava "Still, I've checked through all of the major neutral medical circles too and she's nowhere to be found."
    kay "...weird..."
    kay "Well, keep up the search, Ava. She's gotta be licensed with someone."

    show ava uniform armscrossed skeptical with dissolve

    ava "Wouldn't it be better to just ask, captain?"
    kay "Oh right, I suppose I could do that."
    ava "Really?"
    kay "Really."
    ava "... ... ..."
    kay "I should go."

    $ captaindeck = 1
    $ ava_location = None

    jump dispatch

label medical_examination:

    hide screen ship_map

    stop music fadeout 1.5

    scene bg sickbay
    show chigara uniform handonchest sadblush
    with dissolve

    window show

    chi "... ... ..."
    kay "Chigara? Are you all right? You don't look so good..."

    show chigara uniform handsup surprise with dissolve

    chi "O-oh! C-captain..."

    show chigara uniform twiddlefingers forcedsmile with dissolve

    chi "I-it's nothing... I... was just here for my medical exam..."
    kay "It's important to get checked, Chigara. We've been without a doctor for long. You never know what you'll pick up with all the people and goods which come and go from the ship."

    show chigara uniform twiddlefinger forcedhappy with dissolve

    chi "O-oh yes... C-checked..."

    show chigara uniform handonchest sadblush with dissolve

    chi "... ... ..."
    chi "I... think I should get going now."
    kay "All right."

    show chigara uniform palmsup closedeyesscared:
        zoom 1
        pause 0.75
        ease 0.75 xpos -0.5
    with dissolve

    chi "G-good bye!!"

    hide chigara

    kay "(That was strange... I wonder what happened to her...)"

    play music "Music/As_I_Figure.ogg" fadeout 1.5

    show claude uniform handstogether closedeyeshappy with dissolve

    cla "Oh captain! I was waiting for you!"
    cla "It's time for your medical exam!"
    kay "Okay..."

    show claude uniform fingerup kittyblush with dissolve

    cla "I hear you've operated this ship without a doctor for nearly a month! Now that simply will not do!"
    kay "Let's just say we didn't have much of a choice."
    "Shields took a seat at one of the beds."

    show claude uniform excited perv with dissolve

    cla "Well, time to unbutton your shirt~"
    "Shields took his shirt off and laid it on the bed, exposing his abs."

    show claude uniform neutral drool:
        zoom 1
        ease 1.00 zoom 1.5 ypos 1.4
    with dissolve

    cla "O-oohh...."
    kay "Uh, is something the matter, doc? You're staring pretty intensely here..."

    show claude uniform fingeronlip forcedsmileblush with dissolve

    cla "O-oh? N-no! Absolutely nothing wrong!"

    show claude uniform excited happyblush with dissolve

    cla "I'll just feel up your ribs, make sure nothing misplaced! Haha! Hah!"
    "Claude felt up Shield's chest, running her palms against Shield's ribs."

    show claude uniform neutral drool with dissolve

    cla "O-oh my..."
    kay "W-what's wrong?"

    show claude uniform fingeronlip forcedsmileblush with dissolve

    cla "N-nothing! Absolutely nothing!"
    kay "(There's something fishy going on here...)"

    show claude uniform excited heartdrool with dissolve

    cla "Heh-heh-heh... Now, time for you to stand and take your trousers off too."
    kay "All right..."
    "Shields undid his belt and took his pants off, placing them next to the bed."
    cla "Oooohhh..."
    "Shields eyed Claude."
    kay "...Well?"

    show claude uniform fingerup heartdrool with dissolve

    cla "Well, it's time for you to take your underwear off too. Haven't you ever had a medical exam done before?"
    kay "None quite like this one."

    show claude uniform fingerup poutblush with dissolve

    cla "Now, now captain... Don't be shy. I'm just a trained professional doing her job."

    show claude uniform excited happyblush with dissolve

    cla "Now, off! This is for your sake, captain."
    kay "Sigh..."
    "Shields reluctantly pulled down his underwear."

    show claude uniform fingeronlip drool with dissolve

    cla "Ufufufufu..."
    "Shields grimaced as Claude poked and prodded his privies. For what purpose, he couldn't really tell."
    cla "O-oh my...!"
    "Shields eyed Claude suspiciously."
    kay "(Suspicious... Highly suspicious!)"
    kay "Say... you are a doctor, aren't you?"
    cla "What do you mean, captain? Of course I'm a doctor!"
    kay "Uh... Y-you wouldn't happen to have a certificate, do you?"

    show claude uniform altneutral smileblush with dissolve

    cla "Of course I do! Unfortunately, it was on the Mochi when the pirates got to it."
    kay "I-is that... REALLY!?"
    kay "W-WHAT ARE YOU DOING!?"

    show claude uniform neutral hearthappy with dissolve

    cla "Getting a semen sample! What else!?"
    kay "I-isn't there a standardized device you can use for that!?"

    show claude uniform excited hearthappy with dissolve

    cla "Who needs a fancy device when I got a strong hand right here!"
    kay "(This is so far from protocol not even I can handle it!)"

    play music "Music/Run Amok.ogg" fadeout 1.5

    show ava uniform fistup shout:
        xpos 0.2
    with dissolve

    ava "CAPTAIN!"
    kay "HURK! A-Ava!?"
    ava "I found it here!!!"
    kay "F-found what!?"

    show ava uniform point angry with dissolve

    ava "That little skeever isn't a doctor at all! Look here on this form!"
    ava "Medical license suspended due to malpractice!"
    ava "WARNING: This individual is known to masquerade as a medical practitioner. Her skills fall below all reasonable standards of modern medical care. Patients are advised to seek the advice of a professional medical practitioner instead of this individual."
    kay "I-I knew it!"

    show ava uniform salute angry with dissolve

    ava "Orders, captain!?"
    kay "F-fire vanguards!"
    kay "... ... ..."
    kay "I mean, get me my clothes damnit!"

    show ava uniform alt neutral angry with dissolve

    ava "You're under arrest!"

    show claude uniform neutral ooshock:
        ease 0.5 ypos 1.0 zoom 1.0
    with dissolve

    cla "G-GONG... F-for what?"
    ava "For impersonating as a medical professional!"
    kay "(And molesting a starship captain!)"

    show chigara uniform handonchest sad:
        xpos 0.8
    with dissolve

    chi "U-um... I think I forgot my badge here... and what's all this commotion a-"

    show chigara uniform palmsup surpriseblush with dissolve

    chi "H-EH!? C-c-c-c-captain!?"

    show chigara uniform neutral dazed:
        zoom 1
        pause 0.5
        ease 0.8 ypos 2.0
    with dissolve

    pause 0.5

    play sound "sound/hit.ogg"
    show layer master at shake1

    chi "O-oh my...."

    kay "C-Chigaraaa...!"

    scene bg captainsoffice with fade

    stop music fadeout 1.5

    show ava uniform armscrossed frown with dissolve
    show claude uniform neutral sob:
        xpos 0.75
    with dissolve

    ava "Captain, I've placed our \"doctor\" under arrest. What should we do with her?"
    kay "Send a transmission to the Alliance. We'll just turn her over to the authorities."
    cla "Sniff... sniff..."
    kay "... ... ..."

    show claude uniform handstogether puppy with dissolve #####REPLACE

    cla "Y-you wouldn't do that to ol' Claude now, captain, would you?"
    cla "You see... Claude was just trying to help! I didn't mean any harm by it."
    cla "Whenever I see someone in need, I just can't stop myself from trying to help..."

    show ava uniform armscrossed lookawaymad with dissolve

    ava "Hmph."
    kay "(This girl's good, I'll give her that. But she's not going to fool me twice.)"
    kay "We're here on serious Ryuvian business. A warship is no place to fool around, Claude."

    show claude uniform handstogether closedeyesblush with dissolve

    cla "Sniff... If you're looking for Ryuvian treasure, the place you're looking for is the Mnemosyne Abyss."
    kay "(Damnit! I accidently let slip what we were here for. That was careless.)"

    show ava uniform alt neutral mad with dissolve

    ava "The Mnemosyne Abyss? What do you know about it?"

    show claude uniform neutral sadblush with dissolve

    cla "It's pretty well known among the locals on Tautenia as the site of an ancient Ryuvian battle. Thousands of derelict ships litter the area."
    cla "This area's largely unexplored, so many hidden treasures still remain there."
    kay "(Hidden treasures? This sounds like a possible lead for the Crown Jewel...)"

    show ava uniform handonhip neutral with dissolve

    ava "What do you think, captain? Could this be a possible lead?"
    kay "It's the best we have right now. It's worth investigating."
    kay "We'll set course for the Mnemosyne Abyss."
    ava "Oh. And what of our \"doctor?\""
    kay "Looks like we'll have to delay turning her over to the authorities."

    menu:
        "She'll be confined to quarters in the meantime until we're finished with our mission.":
            jump confineduntilwithmission

        "Get her to the hangar. She'll be more useful as a pilot than a doctor.":
            jump hangarusefulpilotdoc

label confineduntilwithmission:

    $ ClaudeConfine = True

    show ava uniform salute neutral with dissolve

    ava "Understood, sir."

    show claude uniform neutral sob with dissolve

    cla "No way! Captain..."

    show ava uniform armscrossed angry with dissolve

    ava "Come on, this way! Unless you want to be zapped again."
    cla "Sniffle sniffle..."

    jump jumptograveyard

label hangarusefulpilotdoc:

    $ ClaudeConfine = False

    $ affection_claude += 1

    show claude uniform neutral smallsurprise with dissolve

    cla "Does this mean..."

    show claude uniform excited hearthappy with dissolve

    cla "You're still giving me another chance!?"

    play sound "sound/chime.ogg"
    scene cg_shojocaptain with dissolve

    cla "Oh captain... My hero!"

    scene bg captainsoffice
    show claude uniform excited hearthappy:
        xpos 0.75
    show ava uniform handonhip neutral:
        xpos 0.5
    with dissolve

    show ava uniform facepalm with dissolve

    ava "Unbelievable... Come on, the hangar's below us."
    cla "Oh captain! Thank-you so much! I won't let you down!"

label jumptograveyard:

    scene bg black with screenwipe
    scene bg bridge with screenwipe
    show ava uniform neutral neutral with dissolve

    play music "Music/La_Busqueda_de_Lanna.ogg"

    ava "Setting in coordinates. Are you sure you want to jump there?"
    kay "Who knows? Maybe we might also find lost technology which can make the Veniczar magically disappear."
    ava "Coordinates are in. Spooling up warp drive."
    kay "Jump!"

    window hide
    scene map_nomodorn:
        ypos -0.2
    show sunrider_warpout_standard:
        xpos 700 ypos 350
    with dissolve

    pause 2.0

    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_standard_flash:
        xpos 426 ypos 0 alpha 0
        linear 0.1 alpha 1
        linear 0.1 alpha 0
    show sunrider_warpout_standard out:
        xpos 700 ypos 350
        ease 0.2 xpos 200 ypos 300 zoom 0
    pause 2.0

    stop music fadeout 1.5

    scene bg bridge
    show ava uniform neutral neutral
    with dissolve

    window show

    ava "Arrival on target."
    ava "I'm reading... something strange on scanners."
    kay "Strange?"

    play music "Music/Arcadia.ogg"
    scene cg_graveyard:
        xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.25
        ease 10.0 ypos 0.7
    with dissolve

    kay "Sweet mother of god..."
    kay "I've never seen anything like this. Ava, what am I seeing here?"
    ava "An... ancient warship of some kind. Over four kilometers long."
    kay "This could be the biggest finding of lost technology of this decade. All this time, this was hidden here..."
    ava "So do you really think the crown jewel is out here?"

    scene bg bridge
    show ava uniform neutral neutral
    with dissolve

    kay "Let's find out. Asaga, are you there?"

    show asaga plugsuit neutralalt alert:
        xpos 0.2
    with wipeup

    asa "We're ready down here, capt'n! What're your orders?"
    kay "I want our ryders to launch and provide recon for the Sunrider. Find out what's out there and figure out where all this wreckage came from."
    asa "Understood, captain! Alright, you heard the man! All units, launch after me!"

    scene cg_graveyard:
        yanchor 0.5 xanchor 0.5 xpos 0.5 ypos 0.6
    with dissolve

    chi "It's... eerily beautiful."
    ica "In all my years of flying, I've never seen anything like this. Are you seeing this, captain?"
    kay "Yeah..."
    ica "Look up ahead!"
    chi "It's... a vessel. Almost perfectly preserved, even after all these years."
    asa "There're more of them! T-they're everywhere!"
    kay "A dark starship graveyard."
    ava "My father used to tell me ghost stories about space graveyards when I was younger to scare me... This looks like something that could be right out of one of his tales..."
    chi "I've dated those ships, captain. They're over two thousand years old."
    chi "According to those markings, these ships belonged to the Ryuvian princess' royal guard."
    kay "Then the crown jewel could be nearby. Chigara, we're looking for some kind of crystalline device. See if it's on any of those ships."
    ica "A battle took place here, there's no doubt about it."
    ava "How do you know the ships weren't just abandoned here?"
    ica "Because I'm reading organic material inside the ships. The crews were perfectly preserved in the vacuum of space."
    ica "Look into the windows. There're frozen body parts inside..."
    chi "Uuu... C-Chigara's closing her eyes now..."
    kay "What could have caused this...?"
    ica "It looks like some kind of... blast. The ships are more and more damaged the deeper we head into the field."
    kay "Can you determine the epicenter?"
    chi "It's the super dreadnought, captain. A massive energy blast must have emanated from it, while still keeping most of its own structure intact."
    chi "The technology inside that ship alone could... improve our current technology by a hundred fold. If you factor in all the ships in this field..."
    chi "This could be the biggest discovery of Lost Technology in the past hundred years!"
    kay "I think we've hit the jackpot. Asaga, get us a closer view of that Ryuvian super battleship."
    asa "Understood sir."
    asa "I'm... seeing some kind of a hangar bay."
    asa "Eh-heh... I'm going to check out what's inside that thing. I'm goin' ahead, capt'n!"

    scene bg bridge with dissolve
    show ava uniform alt neutral neutral with dissolve

    kay "Hold on Asaga. We don't know what we're up against yet."

    show asaga plugsuit handsonhips happy:
        xpos 0.2
    with wipeup

    asa "Ah c'mon capt'n, it's just a big old frozen ghost ship! What's there to be scared about?"
    kay "Seriously... Would you listen to yourself for a moment?"

    show asaga plugsuit neutral content with dissolve

    asa "The inside of the ship's pretty spacious..."
    asa "It looks like this ship was definitely a carrier... I'm seeing a lot of open space. Enough to store a thousand ryders!"

    show chigara plugsuit altneutral neutral:
        xpos 0.75
    with wipeup

    chi "The Ryuvians were the ones who originally invented ryder technology. So of course they must have the carriers to support a battalion of ryders."
    asa "The design of this ship's nothing like any ship I've been on though. It's like the whole ship is one big hangar. Almost like... the inside of a hive."
    asa "I think the ship's command center should be up above."

    show icari plugsuit armscrossed confident:
        xpos 0.9
    with wipeup

    ica "Think the crew's still frozen up there?"
    asa "Who knows? We haven't seen any other crewmen here though."

    show chigara plugsuit handonchest neutral with dissolve

    chi "Could the ship have been fully AI controlled? If the ship was depressurized in the middle of a battle, you'd think there'd be frozen crewmen..."

    show icari plugsuit handonhip neutral with dissolve

    ica "An AI? Control something this big?"
    chi "Anything could be possible with Ryuvian technology."

    show asaga plugsuit neutral neutral with dissolve

    asa "I've made it to what looks like the entrance to the ship's bridge."
    asa "I'm detecting a faint energy signal beyond that airlock. The life support systems are still functional in the bridge!"

    show asaga plugsuit excited closedeyessmile with dissolve

    asa "I'm going to leave my ryder and head in there for a closer look!"

    show icari plugsuit point mad with dissolve

    ica "Are you crazy! You don't know what's in there!"

    scene cg_ryuvianbridge with dissolve

    asa "I'm out of my cockpit. I'm feeding you the POV camera on my suit, capt'n."
    kay "I see it..."
    asa "It's definitely unlike any bridge I've seen. Only one control station. Was this entire ship meant to be flown by just one person?"
    asa "Wait a minute... I'm seeing... Something weird..."
    asa "There's... some kind of a capsule..."
    asa "Oh..."
    asa "Are you seeing this, captain?"
    kay "I'll be damned. She's been... perfectly preserved."
    chi "No... Not preserved....."

    play music "Music/Poltergeist_Attack.ogg"
    play sound "sound/Ryuvian klaxon.ogg"

    scene cg_ryuvianbridge_red with dissolve

    asa "Uh oh!"
    kay "What did you do!?"
    asa "N-nothing! I swear! The thing just came to life on its own!"
    "Ship" "Ga'rk! Sharn-la ree seath ta!"
    asa "Uuhh... Anyone understand what it's saying?"
    chi "Captain, I'm reading a sudden increase in power! The super battle ship..."
    chi "I-It's coming back to life!"

    scene bg bridge
    show ava uniform alt neutral angry
    with dissolve

    ava "Warning! All the Ryuvian vessels have powered up!"
    kay "What-!? B-but the crew-"

    show icari plugsuit neutral surprise:
        xpos 0.8
    with wipeup

    ica "I-it's a ghost fleet! This whole place is cursed!"
    ava "The Ryuvian fleet is powering weapons, sir! Your orders!"

    play sound "Sound/redalert.ogg"
    scene bg bridgered
    show ava uniform alt neutral angry
    show icari plugsuit neutral surprise:
        xpos 0.8
    with dissolve

    kay "Red alert! All hands, battle stations!"
    kay "Asaga, GET OUT OF THERE!"

    scene cg_ryuvianbridge_empty with dissolve

    asa "U-uh... c-captain..."
    show sola face awakened:
        ypos 1.0 xpos 0.5 yanchor 935
        ease 0.5 zoom 2.0 yanchor 1600 alpha 0
    with dissolvequick

    show white:
        alpha 0
        ease 0.5 alpha 1.0

    pause 0.75

    scene bg bridge with dissolve
    show ava uniform alt neutral angry
    with dissolve

    ava "We've lost contact with Asaga!"
    kay "What in hell's-"
    ava "The enemy vessels are firing on us! Shall we return fire!?"
    kay "Tsch... No choice! All units! Defend the Sunrider!"

    if ClaudeConfine == True:

        show ava uniform armscrossed frown with dissolve

        ava "What about the Black Jack?"
        kay "Asaga's a tough girl.  She'll make it out of there."
        kay "(We're still one ryder short though... This is going to be a challenge...)"

        show claude plugsuit excited determined:
            xpos 0.2
        with wipeup

        cla "Captain!"
        kay "Claude? What are you doing on this line!"
        cla "Let me help! I might not be a licensed doctor, but I can still fight!"
        kay "...All right. Doesn't look like we have much of a choice."
        kay "All units, launch!"

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide icari
    hide claude
    hide battlewarning

    $ check1 = False
    $ check2 = False

    call mission10_inits
    $ BM.mission = 10
    jump battle_start

label mission10:

    $BM.battle_bg = "CG/graveyard.jpg"

    if check1 == False:

        $BM.draggable = False

        "Tip: Take cover in the wreckage to avoid enemy attacks."

        $ check1 = True

        $BM.draggable = True

    if check2 == False and BM.turn_count == 2:

        $BM.draggable = False

        show asaga plugsuit excited focushappy onlayer screens:
            xpos 0.8
        with dissolve

        python:
            blackjack.set_location(10,3)
            player_ships.append(blackjack)

        asa "Ompf. Sorry I'm late, captain!"
        kay "Asaga! Are you all right?"

        show asaga plugsuit handsonhips annoyed onlayer screens with dissolve

        asa "Fine... just..."

        python:

            create_ship(SeraphimEnemy(),(16,8),[SeraphimEnemyKinetic()])
            create_ship(SeraphimEnemy(),(17,9),[SeraphimEnemyKinetic()])
            create_ship(SeraphimEnemy(),(16,10),[SeraphimEnemyKinetic()])

        hide asaga onlayer screens
        show icari plugsuit point mad onlayer screens:
            xpos 0.8
        with dissolve

        ica "Watch it Black Jack! You have three ryders on your tail!"

        show asaga plugsuit handsonhips determined onlayer screens:
            xpos 0.8
        hide icari onlayer screens
        with dissolve

        asa "Ryder! There's just one pilot!"
        kay "Did I just hear you right? Pilot!?"

        show chigara plugsuit excited determined onlayer screens:
            xpos 0.8
        hide asaga onlayer screens
        with dissolve

        chi "Captain, two of those three ryders are copies! The super dreadnought appears to be using some kind of holographic emitter!"

        show asaga plugsuit handsonhips determined onlayer screens:
            xpos 0.8
        hide chigara onlayer screens
        with dissolve

        asa "I don't know what kind of holograms these are though, 'cause the two fake ones are just as deadly as the real thing!"

        show icari plugsuit neutral mad onlayer screens:
            xpos 0.8
        hide asaga onlayer screens
        with dissolve

        ica "Tsch...! Even after 2000 years of decay, these enemies are still insane!"

        hide icari onlayer screens

        $ check2 = True

        $BM.draggable = True

    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission10 #loop back
    else:
        pass #continue down to the next label

label aftermission10:

    hide screen commands
    hide screen battle_screen

    python:
        if not blackjack in player_ships:
            blackjack.set_location(10,3)
            player_ships.append(blackjack)

    scene bg bridgered with dissolve

    window show

    show claude plugsuit excited happy with wipeup

    cla "Ah-hah! We got all of them!"

    play music "Music/Battle_Against_Time.ogg"

    scene space back1
    show seraphimenemy:
        xpos 0.5 ypos 0.5
    with dissolve

    asa "Uwah oh! Negative, captain! All three ryders were decoys! The real one's still here!"
    kay "Take it out!"

    asa "Chigara, watch out! It's targeting you!"

    window hide

    play sound "sound/mech1.ogg"
    show seraphimenemy kinetic with dissolve

    pause 0.1

    play sound1 "sound/Sola Sniper.ogg"
    pause 0.6
    show seraphimenemy_charge1 with dissolve
    pause 0.6

    show layer master at shake1(pausetime=0.1)

    show seraphimenemy_charge2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.1 alpha 1
        pause 0.1
        ease 0.1 alpha 0 zoom 1.5
    show seraphimenemy_bullet:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.1
        alpha 1.0
        ease 0.2 xpos -2.0 ypos 4.0

    pause 0.8

    scene cg_deflectbullet1 with dissolve

    chi "H-eh??"
    asa "Argh... As if...!"

    play sound "sound/boasters.ogg"
    pause 0.7
    show cg_deflectbullet2:
        xpos -0.8
        ease 0.7 xpos 0.0

    pause 1.0

    play sound2 "sound/Sword Shing 2.ogg"
    scene cg_deflectbullet3 with dissolve

    pause 1.0

    play sound3 "sound/explosion1.ogg"
    scene cg_deflectbullet4:
        ease 0.01 xpos 0.02
        ease 0.02 xpos -0.02
        ease 0.01 xpos 0.0
        repeat 8
    with dissolve
    play sound4 "sound/explosion2.ogg"
    scene cg_deflectbullet5:
        ease 0.01 xpos 0.02
        ease 0.02 xpos -0.02
        ease 0.01 xpos 0.0
        repeat 8
    with dissolve
    pause 2.0

    window show

    scene bg bridgered with dissolve

    kay "Chigara! Report! Are you safe!?"

    show chigara plugsuit excited scared with wipeup

    chi "Y-yes, captain! A-Asaga just deflected the bullet!"

    show icari plugsuit point angry:
        xpos 0.8
    with wipeup

    ica "A-are you kidding me!? T-that bullet was traveling at 150 percent the speed of light! That's absolute bullshit! There's no way she did that!!!"

    scene space back1
    show seraphimenemy:
        xpos 0.5 ypos 0.5
    with dissolve

    show sola plugsuit neutral madglow:
        xpos 0.2
    with dissolve

    sol "You... are..."
    sol "... ... ..."
    sol "There is only one capable of fighting like you."
    sol "Impossible... There cannot be another... And..."
    sol "How is it that I yet live?"

    show asaga plugsuit point angry:
        xpos 0.8
    with dissolve

    asa "You're not makin' any sense!"

    show sola plugsuit altneutral neutral:
        xzoom -1 xpos 0.2
    with dissolve

    sol "I yield. The battle has been decided."
    ava "The Seraphim has powered down!"

    hide asaga
    show icari plugsuit neutral angry:
        xpos 0.8
    with dissolve

    ica "Tsch! The rest of the cruisers are still coming online though! We've got more enemies inbound!"
    sol "My control over the fleet has been lost. But their power shall soon fail."

    play music "Music/Coming_Soon_Part1.ogg" fadeout 1.5
    scene bg bridgered with dissolve
    show chigara plugsuit neutral scared:
        xpos 0.8
    with dissolve

    chi "A-ah! C-captain! I'm reading massive power fluctuations coming from the super battleship!"
    chi "I-it is attempting to power its main weapon!"
    kay "All ryders! Fall back! We're getting out of here!"

    show chigara plugsuit excited scared with dissolve

    chi "No... The ship's structure has been too badly damaged!"
    chi "It's overloading its main reactor... At this rate..."
    chi "There'll be a total reactor core meltdown! We have to get out of here now!"

    play music "Music/Coming_Soon_Part2.ogg" fadeout 0.5 noloop

    kay "Everyone, emergency landing procedures! We're getting out of here!"
    asa "All units have returned! We're ready here, captain!"

    window hide

    scene cg_graveyardescape1
    show cg_graveyardescape4
    with dissolve

    chi "The core's going critical! It's going to-"

    play sound1 "sound/explosion5.ogg"
    scene cg_graveyardescape2
    show cg_graveyardescape5
    with dissolve

    ava "Holy sweet---"
    kay "Spool up warp drive! WARP! WARP! Get us out of here!!"

    pause 1.0

    play sound2 "sound/large_warpout.ogg"
    show cg_graveyardescape6:
        alpha 0
        ease 0.2 alpha 1
        ease 0.2 alpha 0
    hide cg_graveyardescape5
    show cg_graveyardescape7:
        xpos 0.5 ypos 0.5
        ease 0.6 xpos -1.0 ypos 2.0 zoom 10.0

    pause 2.0

    play sound3 "sound/explosion4.ogg"
    scene cg_graveyardescape3 with dissolve
    scene white with dissolvelong

    scene bg bridgered with dissolvelong

    window show

    show ava uniform handonhip neutral with dissolve

    ava "Warp successful, captain. All sections are reporting in."
    kay "What happened to the Ryuvian ships?"
    ava "All vaporized by the blast."
    kay "(Damn! There goes our chance to recover all that lost technology!)"
    kay "All right.  Stand down red alert."

    scene bg bridge
    show ava uniform handonhip neutral
    with dissolve

    ava "The Ryuvian girl has been taken into custody in the hangar. Your orders?"
    kay "Let's go down there. She's the only clue we have at figuring out what happened back there."

    play music "Music/Mission_Briefing.ogg"
    scene bg hangar with dissolve

    show sola plugsuit altneutral neutral with dissolve

    sol "... ... ..."
    kay "I'm Captain Kayto Shields. Welcome aboard the Sunrider."
    sol "You... are the leader?"
    kay "What's your name?"

    show sola plugsuit handonchest neutral with dissolve

    sol "I... I am Princess Sola vi Ryuvia."
    kay "P-Princess!? Are you the Princess who's been missing from Ryuvia all this time?"

    show chigara plugsuit palmsup surprise:
        xpos 0.2
    with dissolve

    chi "No... T-that's impossible!"
    chi "Sola vi Ryuvia's been dead for two thousand years!"

    show sola plugsuit altneutral neutral with dissolve

    sol "... ... ..."

    hide chigara with dissolve

    menu:
        "Why did you attack us?":
            jump whydidyouattack
        "Do you know what destroyed all those Ryuvian ships?":
            jump destroyedallryuvianships
        "What were you doing on board that super dreadnought?":
            jump boardthatsuperdreadnought
        "You've been frozen for over two millennia on board that ship!":
            jump youfrozentwomillenia
        "That's enough questions. We are seeking a Ryuvian artifact known as the crown jewel. Do you know where to find it?":
            jump enoughryuvianknownjewel

label whydidyouattack:

    sol "The last I remember before the Final Tear was battle."
    sol "The Fallen had overwhelmed our position. They were about to end us."
    sol "Then... a flash, followed by utter destruction."
    sol "To me... the sleep felt like an instant. I did not even realize that the battle had been interrupted, or that my adversary had changed."
    kay "(I'm not sure I follow what she's saying... But it seems like she attacked us by mistake.)"

    menu:
        "Do you know what destroyed all those Ryuvian ships?":
            jump destroyedallryuvianships
        "What were you doing on board that super dreadnought?":
            jump boardthatsuperdreadnought
        "You've been frozen for over two millennia on board that ship!":
            jump youfrozentwomillenia
        "That's enough questions. We are seeking a Ryuvian artifact known as the crown jewel. Do you know where to find it?":
            jump enoughryuvianknownjewel

label destroyedallryuvianships:

    show sola plugsuit neutral neutral with dissolve

    sol "Such is the ultimate weapon of the Sharr'Lac."
    sol "The Final Tear. A devastating power to destroy everything within half a light year radius. And one which cannot be unleashed without paying the ultimate sacrifice."
    kay "(The Sharr'Lac? She must be referring to the super-dreadnought.)"
    kay "(To think that single ship was capable of such destruction... It could destroy entire systems!)"

    menu:
        "Why did you attack us?":
            jump whydidyouattack
        "What were you doing on board that super dreadnought?":
            jump boardthatsuperdreadnought
        "You've been frozen for over two millennia on board that ship!":
            jump youfrozentwomillenia
        "That's enough questions. We are seeking a Ryuvian artifact known as the crown jewel. Do you know where to find it?":
            jump enoughryuvianknownjewel

label youfrozentwomillenia:

    show sola plugsuit neutral sad with dissolve

    sol "... ... ..."
    kay "You must be even more shocked than us. Uh, welcome to the future."
    sol "What of the Fallen? Was... my mission successful?"
    kay "I don't know. It happened so long ago. Much of our knowledge of your time has been lost."
    sol "... ... ..."
    sol "I see..."

    menu:
        "Why did you attack us?":
            jump whydidyouattack
        "Do you know what destroyed all those Ryuvian ships?":
            jump destroyedallryuvianships
        "What were you doing on board that super dreadnought?":
            jump boardthatsuperdreadnought
        "That's enough questions. We are seeking a Ryuvian artifact known as the crown jewel. Do you know where to find it?":
            jump enoughryuvianknownjewel

label boardthatsuperdreadnought:

    show sola plugsuit altneutral neutral with dissolve

    sol "... ... ..."
    sol "In battle."
    kay "Battle? You mean before you were frozen?"
    sol "Yes."
    sol "... ... ..."
    kay "Who were you fighting?"
    sol "The Fallen."
    kay "Who are they?"
    sol "Imposters to the throne, led by the pretender Crow Harbour."
    kay "(She's not revealing much... It sounds like she's referring to some kind of civil war within Ryuvia during her time period.)"

    menu:
        "Why did you attack us?":
            jump whydidyouattack
        "Do you know what destroyed all those Ryuvian ships?":
            jump destroyedallryuvianships
        "You've been frozen for over two millennia on board that ship!":
            jump youfrozentwomillenia
        "That's enough questions. We are seeking a Ryuvian artifact known as the crown jewel. Do you know where to find it?":
            jump enoughryuvianknownjewel

label enoughryuvianknownjewel:

    sol "The... crown jewel?"
    ava "It is a crystalline device which shows the location of members of the royal family."

    show sola plugsuit handonchest neutral with dissolve

    sol "You speak of the talbur. It is in my possession."

    show sola plugsuit back neutral with dissolve

    sol "Shall I retrieve it from the Seraphim?"
    kay "Sure, can you go get it?"

    hide sola with dissolve

    "... ... ..."

    show sola plugsuit neutral neutral with dissolve
    show item_jewel:
        xpos 0.2
    with dissolve

    sol "It is here."

    show claude plugsuit altneutral surprise:
        xpos 0.8
    with dissolve

    cla "O-oohh... It's... glowing!"
    sol "Yes. The talbur illuminates in the presence of the royal family."

    show sola plugsuit handonchest sad with dissolve

    sol "And yet... It shall never glow for I."

    play music "Music/Invasion of Chaos.ogg" fadeout 1.5
    play sound "sound/redalert.ogg"

    "-warning-"
    kay "The hell? What's wrong?"

    hide claude
    show ava uniform altneutral angry:
        xpos 0.8
    with dissolve

    ava "Proximity warning! PACT signatures detected!"
    kay "Damn! Not a moment's peace!"
    kay "C'mon people, return to battle stations!"

    scene bg bridgered with dissolve

    kay "What's our status!"
    ava "Multiple PACT signatures detected! U-uh..."
    kay "How many!?"

    play music "Music/Posthumus_Regium.ogg"
    scene porkfleet_back with dissolve

    show portfleet_1a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound "sound/large_warpout.ogg"
    show portfleet_1b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_1c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_2a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound1 "sound/large_warpout.ogg"
    show portfleet_2b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_2c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_3a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound2 "sound/large_warpout.ogg"
    show portfleet_3b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_3c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_4a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound3 "sound/large_warpout.ogg"
    show portfleet_4b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_4c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_5a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound4 "sound/large_warpout.ogg"
    show portfleet_5b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_5c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_6a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound5 "sound/large_warpout.ogg"
    show portfleet_6b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_6c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_7a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound6 "sound/large_warpout.ogg"
    show portfleet_7b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_7c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_8a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound7 "sound/large_warpout.ogg"
    show portfleet_8b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_8c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_9a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound8 "sound/large_warpout.ogg"
    show portfleet_9b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_9c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.

    show portfleet_10a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound1 "sound/large_warpout.ogg"
    show portfleet_10b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_10c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_11a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound2 "sound/large_warpout.ogg"
    show portfleet_11b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_11c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    ava "Forty - no... sixty ships, captain! I-it's an entire fleet!"
    kay "Spool up the warp drive! Get ready to-"
    ava "It'll take another half hour before we can warp again after our last emergency warp, captain!"
    kay "Tsch..."

    scene bg bridgered with dissolve
    show cullen with wipeup

    cul "Haaah-hahahaha! Did I not tell you that you would regret crossing me!?"
    kay "Veniczar Porkchops!"
    cul "T-tsch! Curse you and your foul ship!"
    cul "You are hopelessly outnumbered! I know you have the crown jewel aboard. Why don't you be a good lad and turn it over, eh?"
    kay "The crown jewel? And what would PACT want with it?"
    cul "Hah! It seems that little contraption can let us find our dear leader's runaway bride. I have been tasked with finding it on his behalf!"
    kay "(Veniczar Arcadius' bride? The princess of Ryuvia's engaged to Arcadius?)"
    kay "(...no wonder she's run away.)"

    menu:
        "You can take the crown jewel from my cold, dead hands.":
            jump jewelcolddead

        "All right. But in exchange, you promise me the safety of my crew.":
            jump exchangepromisesafety

label jewelcolddead:

    cul "Tsk. I was afraid it would come to this."
    cul "Men! Open fire! Perhaps a little show of force will mellow out this boggart!"

    hide cullen with wipedown

    jump porkfleetopenfire

label exchangepromisesafety:
    cul "Hah! That's a good boy now."
    cul "You have my word! Your crew shall not come to harm!"
    kay "Tsch."
    "... ... ..."

    show ava uniform alt neutral mad:
        xpos 0.2
    with dissolve

    ava "The transfer is complete, captain. PACT has taken the crown jewel."

    hide ava with dissolve

    kay "There. We kept our end of the bargain."
    cul "Hehh... Too bad for you captain, but a certain pirate has paid me quite handsomely for your head."
    cul "Men! Open fire! Rid this vermin from my sight!"
    kay "(I should have known better than to trust this python!)"

    hide cullen with wipedown

    jump porkfleetopenfire

label porkfleetopenfire:

    scene porkfleet_assembled with dissolve
    pause 0.5

    play sound "sound/legion_laser.ogg"
    show porkfleet_fire with horizontalwipereversefast
    hide porkfleet_fire with horizontalwipereversefast

    pause 2.0

    scene bg bridgered with dissolve

    show ava uniform alt neutral angry with dissolve

    ava "The PACT fleet has opened fire!"

    play sound "sound/explosion1.ogg"
    show layer master:
        ease 0.02 xpos 0.05
        ease 0.04 xpos -0.05
        ease 0.02 xpos 0
        repeat 8

    ava "A-argh! W-we can't-"
    kay "L-launch our ryders!"

    play sound "sound/explosion1.ogg"
    show layer master:
        ease 0.02 xpos 0.05
        ease 0.04 xpos -0.05
        ease 0.02 xpos 0
        repeat 8

    ava "Massive damage reports coming from all sectors! W-we're..."
    ava "Ugh!"

    show ava uniform neutral surpriseangry with dissolve

    ava "T-there's too many of them, captain!"

    play sound "sound/explosion1.ogg"
    show layer master:
        ease 0.02 xpos 0.05
        ease 0.04 xpos -0.05
        ease 0.02 xpos 0
        repeat 8

    ava "We've sustained critical damage! O-our weapons are inoperative!"
    ava "Engineering reports our reactor is at critical levels!"
    kay "(Is this the end...?)"
    kay "(... ... ...)"
    ava "C-Captain!? Y-your orders!?"
    kay "It's all right, Ava."

    show ava uniform neutral surprise with dissolve

    ava "S-sir?"
    "Shields smiled wryly and held onto Ava's hand."
    kay "Been an honor."

    show ava uniform armscrossed tearsadblush with dissolve

    ava "...T-tsch..."
    "... ... ..."

    play music "Music/One_Day_in_August.ogg" fadeout 1.5

    hide ava with dissolve
    show asaga plugsuit excited shout with wipeup

    asa "WAIT!"
    asa "I'M THE ONE YOU'RE LOOKING FOR!"
    cul "Oh?"

    show asaga plugsuit handsonhips mad with dissolve

    asa "I... am Princess Asaga di Ryuvia. By my command, I order you to halt your assault, Cullen!"

    show cullen:
        xpos 0.8
    with wipeup

    cul "Well, I'll be."
    cul "My scans indicate that you are indeed the princess. Hah! Who would have ever thought that you'd be hiding here, my grace!"
    cul "Men, hold your fire! Retrieve the princess for me, and let us be off on our merry way."
    kay "What!? Asaga...!? All this time....?"
    kay "(Aarrggghhh... How could I have never known?)"

    show asaga plugsuit armscrossed sadtear with dissolve

    asa "Captain... I'm sorry for lying to you all this time."
    asa "B-but... this is for the best. Ok?"
    cul "Bwaahahahaha! You had best say your good byes now, captain. Onwards to the state wedding! Set course for Ryuvia Prime!"

    hide cullen with wipedown

    asa "...F-farewell, captain! A-and..."

    show asaga plugsuit neutral forcedsmiletear with dissolve

    asa "Thanks for all the fun!"

    hide asaga with dissolvelong

    kay "T-tsch..."
    kay "(No... This isn't our farewell...)"

    show ava uniform handonhip mad with dissolve

    ava "Captain?"
    kay "Get our repair drones online."
    kay "We've got a wedding to crash."

    play sound "sound/ToBeContinued.ogg"
    scene black
    window hide

    stop music fadeout 1.5

    show eyecatch_logo with dissolve
    $ renpy.pause (2.0)
    scene bg black2 with dissolvelong
    scene cg_asagakidnap_legion with dissolvelong

    play music "Music/A_Dark_Dream.ogg"

    pause 1.0

    show cg_asagakidnap_legion_text with horizontalwipereversefast
    pause 2.0
    hide cg_asagakidnap_legion_text with horizontalwipereversefast
    pause 1.0

    scene bg legionwindows with dissolve

    show asaga plugsuit altneutral sad with dissolve
    window show

    asa "... ... ..."

    show cullen behind asaga:
        xpos 0.2
    with dissolve

    cul "There you are, my princess. I was beginning to fear that I had lost you again!"
    cul "Not that there's anywhere to hide on board our flagship anyways! Bwah-hahah!"

    show asaga plugsuit neutral mad with dissolve

    asa "You are arrogant, Cullen. You will do well to remember I am still royal consort to Veniczar Arcadius and above your station."
    cul "Hah! Above my station, you say? It is you who must consider your position."

    show cullen smile with dissolve
    show cullen smile:
        ease 0.5 xpos 0.34

    cul "As long as you are onboard my ship, you belong to me. Muufufufu..."

    show asaga plugsuit armscrossed narroweyeshout with dissolve

    asa "Leave me alone!"
    cul "Your position in that sad little kingdom is meaningless. The Ryuvia of the old is gone. It is I, the governor of the Neutral Rim, who you should obey!"

    show cullen smile:
        ease 0.1 xpos 0.335
        ease 0.2 xpos 0.345
        ease 0.1 xpos 0.34
        repeat 4
    show asaga plugsuit armscrossed madtears with dissolve

    cul "Mmmfuuufuu... Such a shame that you must be turned over to our dear leader so soon, my little flower."
    cul "But I'm sure just a small taste is all right..."


    asa "Y-you're disgusting..."

    show fontana:
        xpos 0.75
    with dissolve

    fon "Heh... I see you are busy entertaining our guest, Cullen."

    show cullen with dissolve
    show cullen:
        ease 0.5 xpos 0.2

    cul "Tsch. And what do you want?"
    fon "We will reach Ryuvia momentarily. I've received orders from headquarters that Veniczar Arcadius himself is to take command of the fleet for the state wedding. We are to prepare for his arrival."
    fon "And you will do well to keep your hands off things which do not belong to you, Cullen."
    cul "Hmph! I was doing no such thing. Now, get me the security plans for the wedding!"

    show cullen:
        ease 1.5 xpos -0.5

    cul "Merely because he is young, he thinks he owns this place! I'll show that whelp who owns what once I'm governor of Ryuvia... Hmph! Always interfering at the worst of times..."
    fon "Heh. I see our old Imperial is still up to his usual habits."
    fon "Well then, your highness, it is time for me to take my leave as well."

    show asaga plugsuit handsonhips frown with dissolve

    asa "You're... Veniczar Fontana."
    fon "A pleasure. I'm sure we will be seeing each other more often."
    fon "Well then... my regards, your highness."

    hide fontana with dissolve
    window hide

    play music "Music/Mission_Briefing.ogg" fadeout 1.5

    scene cg_sunrider_afterkidnap with dissolve
    pause 0.5
    show cg_sunrider_afterkidnap_text with horizontalwipereversefast
    pause 2.0
    hide cg_sunrider_afterkidnap_text with horizontalwipereversefast

    scene bg captainsoffice
    show ava uniform neutral neutral
    with dissolve

    window show

    $ sunrider.repair_drones = 0

    ava "...repairs on the ship are nearly complete, captain. We've been working around the clock to patch her back together after that last assault."
    ava "However, we've used up our last stock of repair drones for the emergency repairs."
    kay "See if we can get some more from the Mining Union."
    ava "Aye captain."
    kay "What's the situation on Ryuvia?"

    show ava uniform handonhip neutral with dissolve

    ava "Alliance intel reports that four PACT fleets have converged on the planet. The Veniczar's flagship, the Legion, just arrived there. All together, I estimate Asaga is behind approximately six hundred PACT ships and one super dreadnought."
    ava "The whole place is in lockdown. Any rescue operation will be akin to suicide now."
    kay "... ... ..."

    show ava uniform armscrossed narroweyefrown with dissolve

    ava "I know that look. It means you're going to say something I don't like."
    kay "Asaga's a member of our crew. I'm not going to abandon her."

    show ava uniform armscrossed frowntalk with dissolve

    ava "Captain, Asaga is merely one person."
    ava "You have a duty to protect this ship. Throwing all our lives away for the life of one would be a foolhardy decision."
    kay "Not if we have a plan."
    ava "Plan?"
    kay "Chigara, come in."

    show ava uniform armscrossed frown:
        zoom 1.0
        ease 0.5 xpos 0.3

    show chigara uniform handonchest smile:
        xpos 0.7
    with dissolve

    chi "Ah... captain."
    kay "Tell us what you've managed to devise from looking at the data we gathered from the Seraphim."

    show chigara uniform pad neutral with dissolve

    chi "I've managed to reverse engineer the Seraphim's targeting computer, which allowed some substantial upgrades to the Sunrider's navigational computer."
    chi "We will now be able to make pin point FTL jumps with an exit area within eight centimeters of our target and speed control within 0.01 meters per second."
    chi "In other words, if you could find a watermelon floating in space, the Sunrider's warp drive is now precise enough to place the watermelon inside a large bowl in the mess hall when we warp out."

    show ava uniform handonhip neutral with dissolve

    ava "And how's that going to help us?"
    kay "According to Alliance intel, the marriage will take place in low orbit around Ryuvia in the Star Palace."
    kay "We'll make a pin point jump right next to the wedding hall, pick Asaga up, then high tail it out of Ryuvia before the PACT fleet can respond."

    show ava uniform neutral neutral with dissolve

    ava "Captain, you do realize that once you warp the Sunrider into low orbit, you won't be able to warp out until you've cleared the planet's gravity well?"
    kay "One thing at a time, Ava."
    kay "We'll have the element of surprise. Nobody will expect the Sunrider to warp past the entire PACT fleet and come out on top of the Star Palace."

    show ava uniform facepalm with dissolve

    ava "Sigh..."
    ava "You're as reckless as ever."
    kay "I'm going to protect everyone on this ship, Ava. Nobody gets left behind. Not while I'm the captain."

    show ava uniform handonhip forcednarrowsmile with dissolve

    ava "Understood, captain. I... will be in my quarters, readying the battle plans."
    kay "Everyone's dismissed."

    hide ava with dissolve
    hide chigara with dissolve

    play music "Music/One_Day_in_August.ogg" fadeout 1.5

    $ seraphim_weapons = [SeraphimKinetic(),Awaken()]
    $ seraphim = create_ship(Seraphim(),(6,8),seraphim_weapons)

    $ captaindeck = 0
    $ chi_location = "lab"
    $ chi_event = "sorryfordeceiving"

    $ sol_location = "messhall"
    $ sol_event = "sol_intro"

    $ cla_location = "messhall"
    $ cla_event = "icecreamclaude"

    $ pro_location = None
    $ ava_location = None
    $ gal_location = None

    jump dispatch

label sorryfordeceiving:


    hide screen ship_map
    scene bg lab
    show chigara uniform altneutral neutral
    with dissolve

    window show

    chi "Ah... captain."
    kay "You wanted to see me?"

    show chigara uniform handstogether sad with dissolve

    chi "Yes. Um... I don't think I've ever apologized to you for lying to you all this time about Asaga."

    show chigara uniform handstogether sadclosedeyes with dissolve

    chi "So... You have my apology, captain."

    menu:
        "You were just trying to protect Asaga. Apology accepted.":
            jump protectasagaapology

        "Keeping secrets like that could place the crew in danger. Don't lie to me again.":
            jump secretsdangerlie


label protectasagaapology:

    $ affection_chigara += 1

    show chigara uniform handonchest smileblush with dissolve

    chi "Thank you, captain..."
    jump shockfirstfoundryuvia

label secretsdangerlie:

    show chigara uniform handonchest sad with dissolve

    chi "Yes captain. I promise I won't ever do it again."
    jump shockfirstfoundryuvia

label shockfirstfoundryuvia:

    show chigara uniform altneutral sad with dissolve

    chi "It was a shock to me too when I first found out Asaga was the princess of Ryuvia many years ago."
    chi "I certainly understand how it must feel for you. But please, don't blame Asaga for deceiving you."

    show chigara uniform neutral mad with dissolve

    chi "To be engaged to marry to such a vile man... She must have had no choice but to run away and hide her identity."

    menu:
        "How did you find out Asaga was the princess?":
            jump howfindasagaprincess
        "PACT is nothing more than a tyrannical regime led by a madman. Veniczar Arcadius will never honor a political alliance with Ryuvia.":
            jump pacttyrannicalmadman
        "This is going to be our hardest mission yet. Prepare yourself, Chigara.":
            jump goinghardestyet

label howfindasagaprincess:

    show chigara uniform altneutral neutral with dissolve

    chi "It was a long time ago, when I first met Asaga, years before any of us knew the name Arcadius."
    chi "It was near the time when I arrived on Ryuvia as a refugee from Diode."

    show chigara uniform twiddlefingers closedeyes with dissolve

    chi "I was lost on my way to my work and panicking when some gentlemen came by to help give some directions. Then all of a sudden, Asaga burst into the scene and started shouting at the men."
    chi "They didn't take kindly to what Asaga was saying and things started getting dangerous..."

    show chigara uniform twiddlefingers forcedsmile with dissolve

    chi "Luckily, I had my handy hair ribbon on, so I used it to temporarily stun the men and ran away with Asaga."

    menu:
        "Uhh... The story was really different when I heard it from Asaga...":
            jump storydifferentasaga

        "That Asaga causes nothing but trouble...":
            jump asaganothingbuttrouble

        "Your hair ribbon can do that!?":
            jump hairribboncando

label asaganothingbuttrouble:

    show chigara uniform handonchest smile with dissolve

    chi "She may be a bit of a loose cannon and she carries things too far sometimes... But she's got a good heart, captain."
    jump shortlyaftertruereally

label storydifferentasaga:

    show chigara uniform twiddlefingers closedeyes with dissolve

    chi "Uuu... Asaga does tend to exaggerate her stories so much..."
    jump shortlyaftertruereally

label hairribboncando:

    show chigara uniform handonchest smile with dissolve

    chi "Yes, captain... It's actually one of my inventions, you see..."

    show chigara uniform altneutral happy with dissolve

    chi "In addition to various defensive mechanisms, can also store music, tell me the time, turn into a flashlight, and keep my hair clean. Ah, with an assortment of other miscellaneous features, of course..."
    kay "Your hair ribbon really is indispensable, isn't it?"

    show chigara uniform handonchest closedeyessmile with dissolve

    chi "Yes captain, I put it on wherever I go."

    show chigara uniform neutral dazed with dissolve

    chi "Umm... what were we talking about again? Mmm... Ah, yes, about how I found out about Asaga."
    jump shortlyaftertruereally

label shortlyaftertruereally:

    show chigara uniform neutral neutral with dissolve

    chi "Shortly after I ran away with Asaga, I found out her true identity."
    chi "I was really shocked to meet the Princess of Ryuvia, but Asaga made it seem like it wasn't anything special."

    show chigara uniform handonchest smile with dissolve

    chi "To her, being the princess didn't define who she was."
    chi "She was going to leave Ryuvia one day and find adventure among the stars. She was never meant to be in politics."

    show chigara uniform handstogether sad with dissolve

    chi "But then, the war approached Ryuvia. Asaga's mother passed away and her father fell ill. The royal court was darkened by talk of succession and fear of PACT's power."
    chi "I still remember Asaga bursting into my apartment after finding out what her father had done. Then we decided to run away together. It was the only thing I could do to protect Asaga."
    chi "And that's how we became freelancers and met you, captain."

    menu:
        "PACT is nothing more than a tyrannical regime led by a madman. Veniczar Arcadius will never honor a political alliance with Ryuvia.":
            jump pacttyrannicalmadman
        "This is going to be our hardest mission yet. Prepare yourself.":
            jump goinghardestyet

label pacttyrannicalmadman:

    show chigara uniform handonchest sad with dissolve

    chi "I don't understand much of politics, but I know that the Veniczar is evil."

    show chigara uniform altneutral mad with dissolve

    chi "He... merely wants Asaga. He does not care about anything about alliances or Ryuvia."
    chi "To a man like him... she is merely a prize to be won. The Veniczar will not stop until the entire galaxy and everyone in it is under his power. And he will use any means to accomplish that."
    chi "To think the King sold Asaga to such a person..."
    kay "Don't worry, Chigara. We'll go in there and rescue Asaga before the Veniczar can even lay a finger on her."

    menu:
        "How did you find out Asaga was the princess?":
            jump howfindasagaprincess
        "This is going to be our hardest mission yet. Prepare yourself.":
            jump goinghardestyet

label goinghardestyet:

    show chigara uniform excited determined with dissolve

    chi "Yes, captain. I'll do everything in my power to save Asaga from the Veniczar!"
    kay "Good. We'll be counting on your expertise to pull this off."

    show chigara uniform altneutral neutral with dissolve

    chi "One more thing, captain. Asaga gave me this."
    kay "A holo recording?"
    chi "She told me to give it to you if anything like this ever happened. With everything that's been going on, I couldn't give it to you until now."
    chi "She made me promise not to look at it, so it is meant only for you."
    kay "Thanks. I'll take a look at it in my office."
    chi "Thank you captain."

    show chigara uniform handonchest closedeyessmile with dissolve

    chi "I was worried before... but now I feel better. We'll rescue Asaga and end this!"

    $ captaindeck = 1
    $ chi_location = None
    $ asa_location = "captainsloft"
    $ asa_event = "Asagarecording"

    jump dispatch

label Asagarecording:

    hide screen ship_map
    scene bg captainsoffice
    with dissolve

    window show

    kay "(Let's play this recording and find out what Asaga has to say.)"

    show asaga uniform neutral funnysmile with dissolve

    asa "Ah. Is this thing on? Hello? Hello? Can you hear me?"
    kay "(You know, you could have edited this part off, Asaga...)"

    show asaga uniform altneutral content with dissolve

    asa "Captain? I sure hope you're the one hearing this. If you're playing this message, then it means that I've left the Sunrider and probably on route to Ryuvia."

    show asaga uniform altneutral sad with dissolve

    asa "First, let me say that I'm really sorry for fooling you! I didn't mean to have been lying to you all this time!"
    asa "I thought it could really work out. That we could just travel the stars forever and beat PACT in the ass for good measure."
    asa "But... I guess you've gotta wake up from all dreams eventually."
    asa "When the time comes and I go back to Ryuvia..."
    asa "Please don't come after me."
    asa "Even though I don't agree with it... My father is still doing the right thing."
    asa "Without the royal marriage, what happened at Cera will happen again at Ryuvia."
    asa "Millions of people will be killed. Worse, what little remains of our way of life will be destroyed."
    asa "Ryuvia's already suffered too much in the past one hundred years... If we take one more hit, it'll be the end of our entire way of life."
    asa "It just takes the sacrifice of one life to save the lives of millions and the preservation of a history which spans longer than the length of the known galaxy."

    show asaga uniform excited determined with dissolve

    asa "If that's the case... then I'll gladly become the Veniczar's bride!"

    show asaga uniform altneutral sad with dissolve

    asa "There's a legend in Ryuvian... Whenever the kingdom is in danger, the sacrifice of the king's only daughter is necessary to save the kingdom."
    asa "Things like this have occurred throughout our history. I'm... ready to play my role, even though it wasn't the role I wanted!"

    show asaga uniform excited determined with dissolve

    asa "Because that's what it takes to be a true hero, capt'n! And that's the only thing I ever wanted to become!"

    hide asaga with dissolve

    "... ... ..."
    kay "(No Asaga... We're coming for you.)"
    kay "(You know the Veniczar is fooling the king! PACT will never honor an alliance with Ryuvia!)"

    $ captaindeck = 0
    $ asa_location = None
    $ ava_location = "bridge"
    $ ava_event = "sawasagarecording"
    $ pro_location = "bridge"
    $ pro_event = "operationweddingcrash"

    jump dispatch

label sol_intro:

    hide screen ship_map
    scene bg messhallwindows
    show sola uniform backturn neutral
    with dissolve

    window show

    sol "... ... ..."
    kay "You must be confused."
    sol "...It is dark. I cannot tell if I have truly awakened, or if I still sleep on board the Sharr'Lac, and this is merely a strange dream."
    kay "Trust me, you're among the living again."

    show sola uniform altneutral neutral with dissolve

    sol "You wish something of me?"

    menu:
        "What do you plan on doing now?":
            jump whatsoladoingnow
        "Tell me more of your time.":
            jump tellmoretime
        "Your eye was glowing during the battle. What was that?":
            jump eyeglowingthat
        "We need help. The technology of your time far surpasses our own. Help us rescue our friend.":
            jump helptimeourfriend

label whatsoladoingnow:

    show sola uniform handonchest sad with dissolve

    sol "... ... ..."
    sol "I do not know."
    sol "The world I know is no more."
    sol "The war against the Fallen is long concluded, and history no longer even remembers who the victors were."
    sol "All which I swore to protect are now long dead or destroyed."
    sol "I now live a hollow existence."
    sol "I wish to close my eyes once more, and disappear into nothingness. As it was meant to be."

    menu:
        "Your story isn't over yet. New enemies now challenge Ryuvia. You must raise your sword once more and fight.":
            jump storynotchallenge
        "You'll find new friends here with us. You can rebuild your life.":
            jump newhererebuild

label storynotchallenge:

    show sola uniform altneutral neutral with dissolve

    sol "You speak of your enemy, PACT?"
    sol "I know not of what quarrels you have with them."
    sol "War is an ugly affair. The truth is lost amidst the sea of blood. No side can claim the moral high ground."
    kay "I understand that you must be confused. But PACT has murdered millions of my people. They'll pay for what they did to us."

    show sola uniform handsbehindback sad with dissolve

    sol "... ... ..."
    sol "Even after countless millenia, leaders still speak the same words before leading men to battle."
    sol "... ... ..."

    show sola uniform handonchest sad with dissolve

    sol "Very well. My guns belong to Ryuvia alone. If there be a threat which threatens my people in this timeline, then I shall once again offer my life to the Holy Ryuvian Empire."
    sol "The defense of Ryuvia is the only reason for my existence. That is all, captain."

    menu:
        "Tell me more of your time.":
            jump tellmoretime
        "Your eye was glowing during the battle. What was that?":
            jump eyeglowingthat
        "We need help. The technology of your time far surpasses our own. Help us rescue our friend.":
            jump helptimeourfriend


label newhererebuild:

    show sola uniform handonchest sad with dissolve

    sol "... ... ..."
    sol "Friends?"
    kay "Like a family connected not by blood, but by bonds."

    show sola uniform handsbehindback sad with dissolve

    sol "I know naught of either friends or family."
    kay "You're just lonely. I don't know what happened to you before you ended up in that tube, but you can join our crew here onboard the Sunrider."

    show sola uniform backturn neutral with dissolve

    sol "... ... ..."
    sol "I have no desire for friendship. But neither does this time have another place for me."
    sol "Very well. I shall choose to remain with your crew."
    sol "But merely because I belong nowhere else in this galaxy."
    sol "I need not become part of your family nor find camaraderie among those who live now. That is all, captain."

    menu:
        "Tell me more of your time.":
            jump tellmoretime
        "Your eye was glowing during the battle. What was that?":
            jump eyeglowingthat
        "We need help. The technology of your time far surpasses our own. Help us rescue our friend.":
            jump helptimeourfriend

label tellmoretime:

    show sola uniform altneutral neutral with dissolve

    sol "It was a violent time for the Holy Ryuvian Empire."
    sol "The Emperor and the Crown Prince were killed in an assassination, leaving the throne to my father, the second prince."
    sol "Yet Crow Harbour, the jealous bastard son of the Emperor, laid a competing claim to the throne. He gathered forces across the galaxy. His ambition: to seize the throne for himself."
    sol "For fourteen years, Ryuvia was caught in a bloody civil war. It seemed as if the Empire itself would crumble if drastic measures were not taken."
    kay "Drastic measures? Like what?"

    show sola uniform altneutral neutral with dissolve

    sol "The awakening of the Sharr'Lac."
    kay "You mean the super dreadnought we found in that grave yard?"
    sol "It is a weapon of unimaginable power. Yet, it can only be helmed by one of the King's daughters."
    sol "The Sharr'Lac cannot be awakened without also sealing the fate of the princess. For when the Sharr'Lac unleashes its ultimate power, it also takes the life of its user."
    kay "That just sounds like a fantasy legend, not the stuff of real life."
    sol "Our ships are operated by the power of science, just like yours. Not magic."
    sol "Long before my time, countless warships bearing the same power as the Sharr'Lac were built. War became horrible. Humanity possessed the power to not only destroy itself, but to collapse the entire universe into a singularity."
    sol "It was fear of our own power which led to the creation of the Sharr'Lac. The wise Emperors of the past decreed such almighty power could only be used with the sacrifice of the Emperor's most precious daughter."
    sol "With the price of infinite power so high, even the most arrogant of Emperors bid second thought before awakening the Sharr'Lac."
    sol "And so, with our most devastating weapon so limited, the Holy Ryuvian Empire could continue to exist in peace."
    kay "But despite that, your father still choose to sacrifice you to awaken the Sharr'Lac."

    show sola uniform handsbehindback sad with dissolve

    sol "... ... ..."
    sol "It was a desperate time."
    kay "You unleashed the Sharr'Lac's final weapon in that battle and destroyed all those ships. But I thought you were supposed to die after you did that."
    sol "... ... ..."
    sol "I believed the same."
    sol "... ... ..."
    kay "Why is it that you're still alive?"
    sol "... ... ..."

    show sola uniform backturn neutral with dissolve

    sol "I have already spoken too much. I do not wish to speak of this further."

    menu:
        "What do you plan on doing now?":
            jump whatsoladoingnow
        "Your eye was glowing during the battle. What was that?":
            jump eyeglowingthat
        "We need help. The technology of your time far surpasses our own. Help us rescue our friend.":
            jump helptimeourfriend

label eyeglowingthat:

    show sola uniform altneutral neutral with dissolve

    sol "... ... ..."
    sol "You find me unnatural?"
    kay "I've never seen anything like that before."
    sol "Perhaps I am not of your species, captain. Or do you fancy that I am some kind of android?"
    kay "(...That's got to be the most deadpan joke ever.)"

    show sola uniform neutral neutral with dissolve

    sol "... ... ..."
    sol "Fear not. I am as human as your mother and father."
    sol "My eye is merely the result of millennia of scientific research. Thanks to genetic modification, I can momentarily increase the vision in my right eye one hundred fold."
    sol "The effect is not only limited to my eye, but also provides a brief but tremendous boast to both my muscle control and brain function."
    sol "Perhaps such technology appears radical to you, but it was a trite affair during my time."
    kay "So everyone during your time possessed super human abilities?"

    show sola uniform altneutral neutral with dissolve

    sol "No. The Holy Ryuvian Emperors feared the power the masses would wield if they had access to such technology."
    sol "Thus, the law across the galaxy was that only royalty could augment their own DNA."
    kay "That makes sense. The Ryuvian rulers would want to use such powers to make themselves more powerful."

    menu:
        "What do you plan on doing now?":
            jump whatsoladoingnow
        "Tell me more of your time.":
            jump tellmoretime
        "We need help. The technology of your time far surpasses our own. Help us rescue our friend.":
            jump helptimeourfriend

label helptimeourfriend:

    show sola uniform altneutral neutral with dissolve

    sol "The current princess?"
    kay "Ryuvia needs your help."

    show sola uniform backturn neutral with dissolve

    sol "This timeline is not my own. Your fights are not mine."
    sol "Yet, even if I so wished, I would be of no use in improving your technology. Such matters are beyond my skills."
    sol "I am merely a marksman, nothing more. I am no technologist."
    kay "Okay. But still help us rescue Asaga. We could really use your skills out there."

    show sola uniform handonchest neutral with dissolve

    sol "... ... ..."
    sol "Very well. I am still sworn to protect Ryuvia, even millennia in the future."
    sol "I will defend Ryuvia with my life. I have already cast down my body for Ryuvia once, and I do not flinch at the thought of doing so again."

    menu:

        "We're all going to come out of this alive. Watch yourself out there.":
            jump goingalivethere
        "We'll give PACT hell until our dying breath.":
            jump giveuntilbreath

label goingalivethere:

    $ affection_sola += 1
    $ captain_moralist += 1

    show sola uniform backturn neutral with dissolve

    sol "Now... farewell, captain. Leave me to my peace."

    $ captaindeck = 0
    $ sol_location = None

    jump dispatch

label giveuntilbreath:

    $ captain_prince += 1

    show sola uniform backturn neutral with dissolve

    sol "Now... farewell, captain. Leave me to my peace."

    $ captaindeck = 0
    $ sol_location = None

    jump dispatch

label sawasagarecording:

    hide screen ship_map
    scene bg bridge
    show ava uniform handonhip neutral
    with dissolve

    window show

    ava "The battle plans for the rescue operation are nearly complete, captain."
    kay "Right. Thanks, Ava."
    ava "Was there something else you needed?"

    menu:
        "Asaga left me a recording asking us not to follow her.":
            jump recordingnotfollow
        "Looks like Claude's going to stay on board for awhile longer.":
            jump claudestayonboard
        "Thanks Ava. I'll keep you posted on additional developments.":
            jump postedthanksdevelopments

label recordingnotfollow:

    show ava uniform altneutral frown with dissolve

    ava "Sounds like even she has more common sense than you do."

    show ava uniform neutral lookleft with dissolve

    ava "Uh, sir."
    kay "Ava..."
    kay "If you were captain and I was the one captured, I know you'd dive into the heart of the Veniczar's palace to rescue me."

    show ava uniform armscrossed frown with dissolve

    ava "You presume too much, captain."
    kay "O-oh. Ouch."
    kay "What are your thoughts?"

    show ava uniform neutral talk with dissolve

    ava "While Ryuvia is no longer a galactic power, the stories of its former glory are known throughout the galaxy."

    show ava uniform alt neutral neutral with dissolve

    ava "Marrying the princess of Ryuvia will place Veniczar Arcadius in line to eventually become the king. And what tyrant could ever pass up the opportunity to restore the Holy Ryuvian Empire and become Emperor of the infinite cosmos?"
    ava "Many millennia ago, the Ryuvian Emperor was the ruler of all life. Legend speaks that he controlled time itself, and indeed, he was worshipped throughout the galaxy not as a man, but as a god."
    kay "Exactly the sort of power a man like Arcadius would dream of wielding."
    ava "But that was then. Today, Ryuvia is merely an obscure backwater planet."
    ava "It's former glory is gone. Just look. We had the Princess of Ryuvia on board our ship for two months and nobody even recognized her."
    ava "Intergalactic treaties are only as powerful as the guns backing the paper. And Ryuvia has none."
    ava "Offering Asaga to Arcadius was merely a form of surrender. An offering, by a dying world to the new rising galactic power, in the hopes of being spared from the coming fire."
    ava "Asaga's sacrifice, however tragic, will spare Ryuvia from a PACT invasion."

    show ava uniform armscrossed neutral with dissolve

    ava "Are you willing to doom Ryuvia to share the same fate as Cera merely to rescue Asaga?"
    kay "... ... ..."
    ava "I prepare the battle plans just the same, captain."

    menu:
        "Looks like Claude's going to stay on board for awhile longer.":
            jump claudestayonboard
        "Thanks Ava. I'll keep you posted on additional developments.":
            jump postedthanksdevelopments

label claudestayonboard:

    show ava uniform facepalm with dissolve

    ava "Peh..."

    show ava uniform armscrossed frowntalk with dissolve

    ava "She's already made a total mess out of the crew quarters. She always leaves her belongings in the showers, gets tooth paste splattered all over the mirrors, and has already spilled coffee on the lounge twice."
    ava "And of course, instead of getting any work done, all she does is stay in bed in her pajamas all day! Arrggghhh!"
    kay "Sounds like you've finally met your match."

    show ava uniform facepalm with dissolve

    ava "I swear, why do all the ryder pilots in the galaxy have to have such crippling personality defects! I honestly can't believe we're entrusting fusion powered weapons of mass destruction to these people!"
    kay "Now Ava... Claude's been a big help to our team..."

    menu:
        "Asaga left me a recording asking us not to follow her.":
            jump recordingnotfollow
        "Thanks Ava. I'll keep you posted on additional developments.":
            jump postedthanksdevelopments

label postedthanksdevelopments:

    show ava uniform neutral neutral with dissolve

    ava "Alright. I'll see you later, captain."

    $ ava_location = None
    $ captaindeck = 1

    jump dispatch

label icecreamclaude:

    play music "Music/As_I_Figure.ogg" fadeout 1.5

    hide screen ship_map
    scene bg messhall
    with dissolve

    show claude uniform handstogether closedeyeshappy with dissolve

    cla "Oh captain... Care to join me for some ice cream?"
    kay "All right, I have some time to chat."

    show claude uniform neutral smallsurprise with dissolve

    cla "Chocolate or vanilla? Or would you just like to eat out of my bowl--"
    kay "Uh... no thanks."

    menu:
        "Do you flirt with every single space captain you happen to meet, Claude?":
            jump flirtcaptainmeet
        "So, what are you going to do now?":
            jump whatgoingnow
        "Ava says that you've been causing her problems...":
            jump avatcausingproblems
        "I'm going to go back to work now. Enjoy your ice cream.":
            jump goingworkicecream

label flirtcaptainmeet:

    show claude uniform fingeronlip hearteyeblush with dissolve

    cla "Eh-heh... Only the cute ones---"
    kay "Uh, alright. Sorry I asked."

    show claude uniform handstogether puppy with dissolve

    cla "What's the matter, capt'n? You don't think Claude's cute?"

    menu:
        "I'm the captain of a military vessel. We have to be serious around here or else people will get hurt.":
            jump captainserioushurt
        "Sure... But Ava will be after me with chains if she saw me with you.":
            jump sureavachainssaw

label captainserioushurt:

    show claude uniform altneutral yawn with dissolve

    cla "Boorrriinnggg..."
    kay "I never was the dashing space captain type, I'm afraid."

    show claude uniform fingerup neutral with dissolve

    cla "Mmm... I wouldn't be so sure about that."
    kay "What?"

    show claude uniform altneutral lookawaykitty with dissolve

    cla "Eh-heh... I actually caught the girl in engineering looking over some photos she took of you the other day. Are you sure you don't have an admirer?"
    kay "You're making that up."

    show claude uniform excited heartdrool with dissolve

    cla "Why would I? Besides, I'd like to keep you all for myself, capt'n--"
    kay "Ugh, please, no more..."

    menu:
        "So, what are you going to do now?":
            jump whatgoingnow
        "Ava says that you've been causing her problems...":
            jump avatcausingproblems
        "I'm going to go back to work now. Enjoy your ice cream.":
            jump goingworkicecream

label sureavachainssaw:

    show claude uniform altneutral laugh with dissolve

    cla "Ahahaha. Just what's your relationship with your first officer anyways?  Ex-wife?"
    kay "Hell no. I think we have regulations against that."
    kay "We went to high school together, that's all. We used to be pretty close back in the days, but it's not like we were dating or anything."
    kay "I guess she's always been more like an older sister."

    show claude uniform fingerup happy with dissolve

    cla "Haha. And now she's your first officer? That's awkward!"
    kay "(You wouldn't know half of it.)"

    menu:
        "So, what are you going to do now?":
            jump whatgoingnow
        "Ava says that you've been causing her problems...":
            jump avatcausingproblems
        "I'm going to go back to work now. Enjoy your ice cream.":
            jump goingworkicecream

label whatgoingnow:

    show claude uniform neutral neutral with dissolve

    cla "Well, my ship was wrecked by the pirates, so looks like I'm stuck here."

    show claude uniform fingerup kittyblush with dissolve

    cla "Eh-heh, not that I have any problems with that."
    kay "I wouldn't count on becoming a doctor here, but you still helped us out with those Ryuvian cruisers. We could use a pilot like you."

    show claude uniform excited perv with dissolve

    cla "Eh-heh... In that case, you can command me any time, captain!"
    kay "All right. Just... uhh..."
    kay "No more medical exams."

    show claude uniform excited concern with dissolve

    cla "Oh but captain! It's for your own health!"
    kay "(More like just to fuel your own perversions!)"

    menu:
        "Do you flirt with every single space captain you happen to meet, Claude?":
            jump flirtcaptainmeet
        "Ava says that you've been causing her problems...":
            jump avatcausingproblems
        "I'm going to go back to work now. Enjoy your ice cream.":
            jump goingworkicecream

label avatcausingproblems:

    show claude uniform altneutral mad with dissolve

    cla "Bleh. That woman just never lets up. Just 'cause I'm staying here for now doesn't mean I have to do the whole military thing."

    menu:
        "I know Ava can be frustrating at times, but she's only doing her job. Can't you two at least try to get along?":
            jump suddenzzz

        "Like it or not, you're on a military vessel now. We have a chain of command here.":
            jump suddenzzz

label suddenzzz:

    show claude uniform excited surprise with dissolve

    cla "Oh! Captain!"
    kay "W-what?"

    show claude uniform neutral sleepdrool with dissolve

    cla "I think I've been hit with a sudden sleep spell. Good night!"
    cla "Zzzzzzz..."
    kay "Claude?"
    cla "Zzzzzzz...."
    kay "Quit fooling around."
    cla "Zzzzzzz...... Mmm..."
    kay "Your ice cream's melting..."
    cla "Mmm... Nom..."
    kay "You're kidding me..."

    menu:
        "Do you flirt with every single space captain you happen to meet, Claude?":
            jump flirtcaptainmeet
        "So, what are you going to do now?":
            jump whatgoingnow
        "I'm going to go back to work now. Enjoy your ice cream.":
            jump goingworkicecream

label goingworkicecream:

    show claude uniform neutral neutral with dissolve

    cla "Bye bye, captain-- Feel free to join me again."

    $ cla_location = None
    $ captaindeck = 0

    play music "Music/One_Day_in_August.ogg" fadeout 1.5

    jump dispatch

label operationweddingcrash:

    $ cla_location = None
    $ sol_location = None

    play music "Music/The Tumbrel.ogg" fadeout 1.5

    hide screen ship_map
    scene bg bridge
    with dissolve

    window show

    show ava uniform handonhip neutral with dissolve

    kay "Report."
    ava "I've completed the battle plans for Operation Wedding Crash."
    kay "Show me."

    show ava uniform alt neutral neutral with dissolve

    ava "We will make a pin point jump past the entire PACT fleet and come out mere meters away from the Star Palace. A security team supported with combat drones will then launch from modified escape pods into the wedding hall, secure Asaga, then return to the Sunrider."
    ava "Following that, the Sunrider will hit full thrusters and attempt to shake the PACT fleet by swinging around the first Ryuvian moon while we prep our warp drive for a second emergency warp."
    kay "Sounds like the best we've got. All right, Operation Wedding Crash is approved."

    show ava uniform neutral lookleft with dissolve

    ava "Also, there is an alternative plan..."
    kay "Alternative?"
    ava "You could say it's something far more daring..."
    kay "Right on, I'm listening..."

    scene black with screenwipe
    scene bg starpalace with screenwipe

    play music "Music/The_Flight_of_the_Crow.ogg"

    "The Star Palace - T-minus 4 hours until the state wedding"

    show fontana:
        xpos 0.8
    with dissolve

    fon "My Veniczar. Welcome to Ryuvia."

    show arcadius altneutral with dissolve

    arc "... ... ..."
    arc "This world was once the center of humanity."
    arc "Such a pity that we cannot see the halls of the Star Palace as they were millennia ago, lavished with the splendors of the Holy Empire."

    show cullen:
        xpos 0.2
    with dissolve

    cul "Hah! Fear not, my lord. The Star Palace is still plenty baroque to this day!"

    show arcadius neutral with dissolve

    arc "Cullen. How goes the invasion of the Neutral Rim?"
    cul "It is nearly complete, my lord. Day after day, more worlds eagerly join our cause! And those that don't? Well, hah! Our cannons prove them most cooperative!"
    arc "The Neutral Rim is but a testing ground of our power. Our true objective lies at Far Port."
    cul "Those Alliance cowards don't see what's coming! Five of our best fleets are poised to strike Far Port within days!"
    cul "With the fall of Far Port, the gateway to Alliance space will be broken! We will break through the enemy's gates and march to Solaris before the Solar Congress can muster its forces."
    fon "Careful Cullen. The Alliance is different from the backwater planets you have dealt with in the Neutral Rim. They will not be defeated as easily."
    cul "Hah! Perhaps to your fleets, Fontana! They are no match for mine!"
    arc "Very well. Veniczar Cullen. You will lead our forces at Far Port."
    arc "Let us see if you can translate your words into actions."
    cul "Thank you, my lord!"
    fon "This way, my leader, to your chambers. We've prepared a special guest for you."

    scene bg legionwindows with dissolve
    show arcadius neutral:
        xpos 0.3
    with dissolve

    arc "Our... beloved. Are you ready for eternity?"

    show asaga wedding angry:
        xpos 0.7
    with dissolve

    asa "Y-you...!"
    arc "Hahahaha!"
    arc "Truly your father is naïve to believe offering such a pathetic girl to us will save his dying world from the coming revolution."
    arc "Ryuvia and its secrets will be mine."

    show arcadius fist with dissolve

    arc "Just as the old Ryuvian Emperors of the past, we shall hold the galaxy upon our palms. But it will not be around the halls of the ancient Star Palace that the galaxy revolves, but from our mighty fortress at New Eden!"
    asa "Not if I stop you!"

    show arcadius neutral with dissolve

    arc "Oh? And what would a naïve school girl do to oppose us, the Veniczar of the crimson armada?"

    show arcadius neutral:
        ease 0.5 xpos 0.5

    arc "Your life now belongs to me. Your body is now mine. Your soul will be crushed, until you are but an obedient dog, eagerly licking her master's boots."
    asa "Never!"

    show arcadius neutral:
        ease 0.1 xpos 0.7
        ease 0.1 xpos 0.5
    pause 0.1

    play sound "sound/punch.ogg"

    show layer master at shake1
    show asaga wedding scared:
        zoom 1.0
        ease 0.1 ypos 1.2

    arc "Silence!"
    asa "Eah!"
    arc "How cruel is destiny, that it is we who must suffer, while a little doll like you holds a destiny greater than us."
    arc "But in mere hours... You will be mine. And with that, the keys to a weapon which shall send a frozen shiver down the galaxy's spine will be in our hands."

    show arcadius laugh with dissolve

    arc "Hahahaha... HAHAHAHAHA!!!"

    scene bg weddinghall with dissolve
    play music "Music/wedding_march.ogg" fadeout 1.5

    show king with dissolve
    show arcadius altneutral:
        xpos 0.8
    with dissolve
    show asaga wedding sad:
        xpos 0.2 xzoom -1
    with dissolve

    ryu "Dear our kind guests. We are gathered here to witness the marriage of the righteous Veniczar S. Arcadius to my lovely daughter, Princess Asaga di Ryuvia."
    ryu "Does the honorable Veniczar S. Arcadius take Princess Asaga di Ryuvia as his lawfully wedded wife, to love unconditionally, in sickness and in health, in good times and in bad, and in joy as well in sorrow, to cherish and to hold for as long as he shall live?"
    arc "Yes."
    ryu "And does Princess Asaga di Ryuvia solemnly pledge to take Veniczar S. Arcadius as her lawfully wedded husband, to love unconditionally, in sickness and in health, in good times and in bad, and in joy as well in sorrow, to cherish and to hold for as long as she shall live?"
    asa "I..."
    asa "... ... ..."
    ryu "Ahem..."

    show asaga wedding sadtear with dissolve

    asa "I........"
    asa "... ... ..."
    ryu "Then I do declare you husband and wife. You may now kiss the bride."
    asa "... ... ..."

    play music "Music/The_Flight_of_the_Crow.ogg" fadeout 1.5

    show arcadius laugh with dissolve

    arc "Hahahahahahaha!"

    show arcadius neutral with dissolve

    arc "We are afraid this charade is now over, your majesty. Your pathetic kingdom shall now be extinguished from the face of the galaxy."

    play sound "sound/hit.ogg"
    show king at shake1:
        zoom 1.0


    ryu "What? We had a deal, Veniczar!"

    show arcadius fist with dissolve

    arc "A deal made only of paper. Men! Seize our guests."

    hide king with dissolve

    show asaga wedding angry:
        ease 0.5 xpos 0.3
    with dissolve

    show arcadius fist:
        ease 0.5 xpos 0.7

    asa "You! I knew this was all a trick!"

    show arcadius altneutral with dissolve

    arc "Silence, our little princess. You shall learn to serve us."
    arc "We hope your cooperation is forthcoming, for the life of your father depends on it."
    asa "Y-you..."
    arc "How fitting it is that our marriage hall is high above the skies of Ryuvia. From here, you will all witness the true power of PACT... And the end of your pathetic kingdom."
    arc "For ten thousand years, Ryuvia has ruled the galaxy... And now... PACT shall earn its place in history as the power to finally extinguish Ryuvia's last flickering ember."

    show asaga wedding angry:
        ease 0.5 xpos 0.2
    show arcadius altneutral:
        ease 0.5 xpos 0.8
    show king with dissolve

    ryu "... ... ..."
    ryu "Hahaha..."
    ryu "Empty words, Veniczar..."
    ryu "I have ruled Ryuvia for all my life... And I have long realized, all our traditions... All our rites... All our culture..."
    ryu "They are but sad remnants of our former selves, meant to cloak us from the truth: That we have become weak."
    ryu "Ryuvia, the infinite kingdom of all space and time, is no longer... All that is left is embodied in this old, frail man."
    ryu "Go ahead. Shoot. You will only have killed an old, dying man, whose time has long come. That... Is all that you have accomplished today..."
    arc "Hah. You speak too much. Farewell, my king."

    play sound "sound/pistol.ogg"
    show white:
        alpha 0
        ease 0.3 alpha 1.0
        ease 0.3 alpha 0

    show king:
        zoom 1.0
        ease 0.5 ypos 1.3 zoom 1.0

    ryu "Eaah!!!"

    show asaga wedding surprisetears with dissolve

    asa "Father!"
    ryu "Asaga... I'm sorry."
    ryu "It was... The only way... The Veniczar promised your safety if you would wed him..."
    asa "You didn't have to..."
    ryu "Forgive me... Asaga..."

    hide king with dissolve

    show asaga wedding surprisetears:
        ease 0.5 xpos 0.3
    show arcadius altneutral:
        ease 0.5 xpos 0.7

    asa "NO!!"

    show arcadius fist with dissolve

    arc "Seize them. They shall now be made to serve PACT. Prepare my shuttle for the Legion. We shall dissect Ryuvia until all its secrets are ours!"
    asa "No! Let me go!! You'll pay for this, Veniczar!!"

    show arcadius altneutral with dissolve

    arc "Oh?"

    show arcadius laugh with dissolve

    arc "We are Veniczar Arcadius! It is us who will rule the known cosmos! There is no force left in this galaxy to challenge us!"
    arc "Our power is infinite! And you, our pretty little doll... will belong to us for eternity!"
    arc "With the key to the galaxy in our hand... We shall be unstoppable!"

    window hide

    play music "Music/Driving_the_Top_Down.ogg" fadeout 1.5

    scene cg_weddinghall_ceilingspace
    show cg_weddinghall_ceiling
    with dissolve

    show cg_weddinghall_sunrider warp behind cg_weddinghall_ceiling:
        zoom 0.7 xanchor 0.5 xpos 0.5 ypos 0.5
        ease 0.1 zoom 1.0 ypos -0.2

    pause 0.5

    play sound "sound/large_warpout.ogg"

    show cg_weddinghall_sunrider behind cg_weddinghall_ceiling
    show white:
        alpha 0
        ease 0.2 alpha 0.8
        ease 0.2 alpha 0

    $ renpy.pause(3.0)

    scene bg weddinghall
    show arcadius neutral
    with dissolve

    window show

    arc "What-? What is that vessel!?"

    show cullen:
        xpos 0.88
    with dissolve

    cul "G-guck!"

    show asaga wedding surprise:
        xpos 0.2
    with dissolve

    asa "It's... the Sunrider!"

    scene bg bridgered with dissolve

    show ava uniform alt neutral angry with dissolve

    ava "Warp successful! We've dropped out 10 meters from the wedding hall!"
    kay "Begin operation! Launch our drones and take out the guard ships!"
    ava "Aye captain."
    ava "I will lead the security squad as planned. You have the bridge captain."
    kay "No. I'm coming with you."

    show ava uniform armscrossed frown with dissolve

    ava "Captain, protocol strictly states that during all high risk away missions, the captain is to remain on the bridge at all times."
    "Ava pulled out a handbook from her pocket and rapidly flipped through the pages."
    ava "Section 48, paragraph 8 clearly states, when engaging in level 9 security protocols, the ranking officer must-"

    menu:
        "No.":
            jump justno
        "COMMAND DECISION: HELL no. (50 CMD)":
            jump hellno

label justno:

    kay "I'm not letting you do this alone."

    show ava uniform armscrossed neutral with dissolve

    ava "... ... ..."

    show ava uniform alt neutral mad with dissolve

    ava "All right. Come this way."

    jump theweddingcrash

label hellno:

    if BM.cmd >= 50:
        $ BM.cmd -= 50

        play sound "sound/swordhit.ogg"
        show captainflash:
            xpos 1.1 ypos 0.2
            ease 0.7 xpos 0.35
            pause 0.5
            ease 0.8 alpha 0

        "Shields grabbed the handbook from Ava's hands, shredded it to pieces, and scattered it to the winds."

        show ava uniform altneutral annoyed with dissolve

        ava "... ... ..."

        show ava uniform salute talk with dissolve

        ava "Right this way, sir."

        jump theweddingcrash

    if BM.cmd < 50:
        "Insufficient command points."
        menu:
            "No.":
                jump justno
            "COMMAND DECISION: HELL no. (50 CMD)":
                jump hellno

label theweddingcrash:

    scene bg weddinghall with dissolve
    show arcadius fist with dissolve
    show fontana:
        xpos 0.7
    with dissolve

    fon "Take cover sir! We've got a security breach!"

    show cullen:
        xpos 0.23
    with dissolve

    cul "Bah! Destroy those drones!"
    arc "Fools! It is merely one ship! Blow it out of the sky!"

    show asaga wedding surprise:
        xpos 0.34
    with dissolve

    asa "Captain! Over here!"

    show cullen:
        ease 0.5 xpos 0.3

    cul "Oh no, your highness! You're not going anywhere!"

    show asaga wedding angry:
        ease 0.2 xpos 0.35
        ease 0.2 xpos 0.34
        repeat 5

    asa "Eah! Lemme go ya fatty!"
    cul "Disrespectful little whelp! I'll show you, you little-"
    kay "Veniczar Porkchops! Let her go!"

    play sound "sound/hit.ogg"
    show cullen:
        ease 0.01 xpos 0.295
        ease 0.02 xpos 0.305
        ease 0.01 xpos 0.3
        repeat 5

    cul "Y-you! I should have killed you when I had the chance!"

    play sound "sound/punch.ogg"

    show asaga wedding angry:
        ease 0.1 xpos 0.3
        ease 0.1 xpos 0.34

    asa "Eah!"

    show cullen:
        ease 0.5 ypos 1.2
        block:
            ease 0.1 xpos 0.31
            ease 0.1 xpos 0.29
            repeat 8

    cul "AAARRGGHH!!!!! My foot!"
    cul "ARGGHHH!!! That bitch just crushed my foot with her heels! ARRGGHHH MEDIC!!!"

    show asaga wedding angry:
        ease 0.5 xpos -0.4

    fon "Men! Seize the princess! Don't let her-"

    scene cg_weddingcrash1 with dissolve

    kay "Asaga, here! We're getting you out of here!"
    asa "Captain!"
    kay "Hang on!"
    cul "YOU!!!"
    kay "Sorry to bride snatch, but I think this marriage's been annulled!"
    asa "Careful captain! Two, up in the rafters!"

    scene cg_weddingcrash2 with dissolve
    play sound "sound/pistol.ogg"

    pause 0.4
    play sound1 "sound/pistol.ogg"

    pause 0.3
    play sound2 "sound/pistol.ogg"
    pause 0.3
    play sound2 "sound/pistol.ogg"

    asa "Eaaahh!!!"
    kay "U-uh. Thanks for the cover."
    kay "Ava, I've secured Asaga."
    kay "Commence Stage Two."
    ava "Aye captain."

    scene bg weddinghall
    show arcadius fist:
        xpos 0.49
    with dissolve

    arc "Fools! Do not allow the princess to escape!"

    show cg_crosshairs with dissolve

    ava "Sola, eliminate the target."
    sol "Understood."
    sol "Acquiring target."

    play sound "sound/rifle.ogg"
    hide arcadius with dissolve

    sol "Target neutralized."
    kay "Ava, confirm! Is the target down?"

    show arcadius fist behind cg_crosshairs with dissolve

    ava "Negative!"
    ava "It was just a hologram. Arcadius was never even in the wedding hall."

    scene cg_weddingcrash1 with dissolve

    kay "Damn!"
    kay "Abort mission! Get out of there! Return to the Sunrider!"
    ava "Understood captain. We're falling back!"
    kay "C'mon Asaga, back into the escape pod! We're getting out of here!"

    scene bg hangar with dissolve

    kay "We've made it back, Ava! What's the situation!"
    ava "The space around us just lit up like a Christmas tree! We've got 200 ships, closing in fast!"
    kay "All ahead full! Launch all our ryders to protect the Sunrider as we make it to the moon!"
    ava "Aye captain!"

    stop music fadeout 1.5

    scene black with screenwipe
    scene bg hangar with screenwipe
    show asaga plugsuit neutral crush:
        ypos 1.4 zoom 1.6 xpos 0.5
    with dissolve

    kay "Here's the Black Jack. We kept her warm for you."
    asa "Captain..."
    asa "You came for me. Even after..."
    kay "Of course I did. You're a member of my crew."
    kay "Stay safe out there."

    show asaga plugsuit neutral smileblush with dissolve

    pause 0.5

    play sound "sound/heartbeat.ogg"

    show asaga plugsuit neutral smileblush:
        ypos 1.4
        ease 0.03 xpos 0.495
        ease 0.05 xpos 0.505
        ease 0.03 xpos 0.5
        repeat 3

    asa "... ... ..."
    asa "Uu..."

    show asaga plugsuit vpose with dissolve

    asa "Asaga di Ryuvia, returnin' to duty, sah!"
    kay "Good to have you back."
    kay "Now go get 'em."

    scene bg weddinghall with dissolve
    show arcadius neutral:
        xpos 0.3
    with dissolve
    show fontana:
        xpos 0.7
    with dissolve

    play music "Music/March_to_Glory.ogg"

    fon "Sir, the Sunrider is attempting to escape behind the first moon. We've already scrambled all our forces to intercept. What are your orders?"
    arc "We will not be humiliated at our own wedding."

    show arcadius fist with dissolve

    arc "Slaughter them all. But bring the princess to us alive."
    arc "Death is too lenient of a sentence for the humiliation she has caused us today."
    fon "Yes sir."

    hide fontana with dissolve
    show arcadius altneutral with dissolve
    show arcadius altneutral:
        ease 0.5 xpos 0.5

    arc "Her struggle is meaningless, for Ryuvia is already ours."
    arc "Soon, we will have the means to rule the galaxy just as the Ryuvian Emperors of the old."

    show arcadius laugh with dissolve

    arc "Hahahaha...."
    arc "HAHAHAHAHAHAHAHAHAHAHA!!!"

    scene bg bridgered with dissolve

    show ava uniform alt neutral angry with dissolve

    ava "Captain, we've got PACT vessels coming from every direction to intercept us."
    kay "Make it to Ryuvia's moon as fast as possible. We'll slingshot ourselves out of Ryuvia's gravity well and block off the PACT fleet while we're at it."

    show ava uniform alt order angry with dissolve

    ava "Aye captain! All hands, prepare for emergency maneuvers!"

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide battlewarning

    $ check1 = False
    $ check2 = False
    $ check3 = False
    $ check4 = False
    $ check5 = False
    $ check6 = False

    call mission11_inits
    $ BM.mission = 11
    jump battle_start

label mission11:

    $BM.battle_bg = "Background/space6.jpg"

    if check1 == False:

        $BM.draggable = False

        show ava uniform handonhip mad onlayer screens:
            xpos 0.8
        with dissolve

        ava "The two PACT battleships are trying to cut us off!"
        ava "Tractor beam detected! We'll have to sink the battleships before we can warp!"

        hide ava uniform handonhip mad onlayer screens with dissolve

        play sound "Sound/objectives.ogg"
        "Objective: Sink the two PACT battleships."

        $ check1 = True
        $ BM.draggable = True

    if check2 == False and BM.turn_count == 4:

        play sound "sound/Voice/Ava/Ava Others 6.ogg"
        python:
            create_ship(PactMook(),(16,3),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactMook(),(17,3),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(MissileFrigate(),(13,3),[PactFrigateMissile()])

            create_ship(PactMook(),(16,14),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactCruiser(),(15,14),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(MissileFrigate(),(13,14),[PactFrigateMissile()])


        $ check2 = True

    if check3 == False and BM.turn_count == 6:

        play sound "sound/Voice/Ava/Ava Others 5.ogg"
        python:
            create_ship(MissileFrigate(),(17,6),[PactFrigateMissile()])
            create_ship(PactCruiser(),(17,7),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
        $ check3 = True

    if check4 == False and BM.turn_count == 8:

        $BM.draggable = False

        show ava uniform handonhip mad onlayer screens:
            xpos 0.8
        with dissolve

        ava "Incoming more enemy reinforcements!"
        ava "Hurry up, captain! We're running out of time!"

        hide ava uniform handonhip mad onlayer screens with dissolve
        play sound "sound/Voice/Ava/Ava Others 6.ogg"
        python:
            create_ship(PactCruiser(),(17,1),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(18,1),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(17,16),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(16,16),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactMook(),(14,3),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactMook(),(16,3),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactMook(),(15,3),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactBomber(),(16,2),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])
            create_ship(PactBomber(),(16,15),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])
            create_ship(PactMook(),(16,14),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactMook(),(17,14),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactMook(),(15,14),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(MissileFrigate(),(13,14),[PactFrigateMissile()])

        $BM.draggable = True
        $ check4 = True

    if check6 == False and BM.turn_count == 10:

        $BM.draggable = False

        show ava uniform handonhip mad onlayer screens:
            xpos 0.8
        with dissolve

        hide ava uniform handonhip mad onlayer screens with dissolve
        play sound "sound/Voice/Ava/Ava Others 6.ogg"
        python:
            create_ship(PactMook(),(14,3),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactMook(),(16,3),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactMook(),(15,3),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactBomber(),(14,2),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])
            create_ship(PactBomber(),(14,15),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])
            create_ship(PactBomber(),(15,2),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])
            create_ship(PactBomber(),(15,15),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])
            create_ship(PactBomber(),(16,2),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])
            create_ship(PactBomber(),(16,15),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])
            create_ship(PactMook(),(16,14),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactMook(),(17,14),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactMook(),(15,14),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(MissileFrigate(),(13,12),[PactFrigateMissile()])
            create_ship(MissileFrigate(),(14,12),[PactFrigateMissile()])
            create_ship(MissileFrigate(),(15,12),[PactFrigateMissile()])
            create_ship(MissileFrigate(),(13,5),[PactFrigateMissile()])
            create_ship(MissileFrigate(),(14,5),[PactFrigateMissile()])
            create_ship(MissileFrigate(),(15,5),[PactFrigateMissile()])

        $BM.draggable = True
        $ check4 = True

    python:

        battleships_remaining = 0
        for ship in enemy_ships:
            if ship.stype == 'Battleship':
                battleships_remaining += 1

    if battleships_remaining == 0 and check5 == False:

        $BM.draggable = False

        show ava uniform handonhip mad onlayer screens:
            xpos 0.8
        with dissolve

        ava "All battleships destroyed, captain!"
        ava "Now let's get out of here before more enemies show up!"

        play sound "Sound/objectives.ogg"
        "Objective: Get the Sunrider to the far right edge of the map."

        $BM.draggable = True
        $ check5 = True

        hide ava uniform handonhip mad onlayer screens with dissolve

    $BM.battle()  #continue the battle

    if sunrider.location != None:
        if sunrider.location[0] == 18 and check5 == True:
            $ BM.battle_end()

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission11 #loop back
    else:
        pass #continue down to the next label


label aftermission11:

    hide screen commands
    hide screen battle_screen

    scene bg bridgered
    show ava uniform alt neutral angry
    with dissolve

    window show

    ava "We have made it to the moon captain!"
    kay "Retrieve our ryders! Slingshot us around the moon close enough to graze the sand!"
    ava "Aye captain! Our artificial gravity generator is nearing its limit!"

    play music "Music/Posthumus_Regium.ogg"

    scene cg_legionsurprise1 with dissolve

    ava "Holy----!"
    ava "It's the Legion, waiting for us on the other side of the moon!"

    play sound "sound/legion_maincannon_charge.ogg"
    scene cg_legionsurprise2 with dissolve

    ava "It is preparing to fire!"
    kay "Break off! HARD TO PORT!!!"

    scene bg bridgeredtilt
    show bridgeredtiltfore
    show ava uniform altneutral surpriseshout behind bridgeredtiltfore:
        rotate -45 xpos 0.8 ypos 0.8 zoom 1.2
        ease 1.0 xpos 0.2 ypos 2.0
    with dissolve

    pause 0.2

    show layer master at shake1
    play sound "sound/hit.ogg"

    ava "Arrggghhh!!!"

    show ava uniform altneutral surpriseshout behind bridgeredtiltfore:
        rotate -20 xpos 0.4 ypos 1.2
    with dissolve

    ava "We're exceeding our safeties, captain!"
    kay "All hands, BRACE FOR IMPACT!!!"

    scene cg_legionsurprise2 with dissolve

    ava "Warp preparations are complete!"
    kay "WARP!!!"

    play sound "sound/legion_maincannon_fire.ogg"
    pause 0.6
    scene cg_legionsurprise3

    play sound1 "sound/large_warpout.ogg"

    show cg_legionsurprise_sunrider:
        xpos 0.0 ypos 0.0
        ease 0.4 zoom 10 xpos 1.1 ypos -6.5
    show cg_legionsurprise_sunriderflash:
        alpha 0
        parallel:
            ease 0.2 alpha 1.0
            ease 0.1 alpha 0
        parallel:
            ease 0.3 zoom 1.5 ypos -0.32
    with dissolve

    pause 3.0

    stop music fadeout 3.0
    scene black with dissolvelong

    pause 1.0

    scene bg bridgered
    show ava uniform neutral neutral
    with dissolvelong

    ava "Captain, we're now safely inside Alliance space. No sign of further PACT pursuit."

    play music "Music/The_Beginning_of_the_Adventure.ogg"

    kay "Good. Stand down red alert."

    scene bg bridge
    show ava uniform armscrossed smile
    with dissolve

    ava "That was one hell of a rescue, captain. Tell the truth, I can't believe we made it out of that alive."
    kay "You did well, Ava. I knew I could count on you."

    show ava uniform salute neutral with dissolve

    ava "Thank-you, captain."

    show ava uniform handonhip neutral with dissolve

    ava "We're receiving a message from the Alliance vessel Aristotle. They want to know our status."
    kay "Tell them we mean no harm. We'll be approaching the nearest safe harbor for supplies and repairs."
    ava "Aye sir."
    kay "Take us into port, Ava. I think we've had more than enough adventure for one day."
    ava "Understood, captain. Setting course for the Alliance planet of Far Port. ETA: 18 hours."

    scene black with screenwipe
    scene bg captainsoffice with screenwipe

    kay "Begin captain's log. We've arrived at the Alliance world of Far Port. News of Ryuvia's fall has spread throughout Alliance space like wildfire."
    kay "Now, there can be no doubt about Arcadius' ambitions. With PACT now at its doorsteps, the Solar Congress has convened for an emergency session. The only possible outcome is a declaration of war."
    kay "The Sunrider is now caught right in the middle of the biggest intergalactic war of our time."
    kay "I'm not sure just where we stand here..."

    menu:
        "My gut feeling is that we shouldn't get too close to the Alliance.":
            jump gutshouldntalliance
        "My gut feeling is that we should assist the Alliance in whatever capacity we can.":
            jump thatassistalliance

label gutshouldntalliance:

    kay "The Alliance is mired in politics. Whatever is good for the Alliance may not be in the best interests of my ship."
    kay "For now, it'll be better to wait and see just what the Alliance wants out of this war."

    jump asagaafterrescue

label thatassistalliance:

    kay "The Alliance is our best hope of defeating PACT. We have to accept the fact that we're just one ship against an entire empire. We need powerful allies if we're going to survive."

    jump asagaafterrescue

label asagaafterrescue:

    play music "Music/Colors_of_an_Orchestra.ogg" fadeout 1.5

    play sound "sound/doorbell.ogg"
    "(Doorbell)"

    kay "End log. Come in."

    show asaga uniform armscrossed blushsmile with dissolve

    asa "Uh, how's it going, capt'n."
    kay "Asaga. Have a seat."
    kay "I've been meaning to speak to you about what happened on Ryuvia."
    asa "You must have so many questions."

    show asaga uniform altneutral sorryblush with dissolve

    asa "First, I'm sorry for lying to you. I didn't mean to place the crew in danger like that."

    show asaga uniform altneutral sadblush with dissolve

    asa "I guess... I was just naïve. I thought I could just keep pretending to be Asaga Oakrun for the rest of my life. I guess real life doesn't work like that..."
    kay "That doesn't matter now. I'm just glad to have you back."

    menu:
        "You saw your own father get killed. Are you feeling all right?":
            jump sawfatherkilled
        "You must know more about Arcadius. Is there anything you can tell me about him?":
            jump knowarcadiustell
        "You're now the Queen of Ryuvia. What are you going to do?":
            jump nowqueendo
        "That'll be all. I'm glad to have you back, Asaga.":
            jump allgladback

label sawfatherkilled:

    show asaga uniform altneutral sadblush with dissolve

    asa "Yeah..."
    asa "Even though I hated my father for marrying me to the Veniczar, I think in the end, he was just trying to do his best to protect me..."

    show asaga uniform handonhips sadsmile with dissolve

    asa "I'm not the type to get all depressed, captain. Not while there's still something I can do."
    asa "I'm going to avenge my father by ending PACT once and for all. As long as I still have my Black Jack, I'll keep fighting for my father's memory."
    kay "I'm glad to hear you're taking this strong. But remember, we're all here for you. You don't have to carry your burdens alone."

    menu:
        "You must know more about Arcadius. Is there anything you can tell me about him?":
            jump knowarcadiustell
        "You're now the Queen of Ryuvia. What are you going to do?":
            jump nowqueendo
        "That'll be all. I'm glad to have you back, Asaga.":
            jump allgladback

label knowarcadiustell:

    show asaga uniform handonchin thinking with dissolve

    asa "I'm sorry captain, but not even I know much about him."
    asa "I hardly ever saw him, and even when I did, he always hid his face and voice behind a mask. I have no idea who or what he is."
    asa "All I know is that he has always been obsessed with old Ryuvian legends."

    show asaga uniform armscrossed neutral with dissolve

    asa "He's always spurting nonsense about lost technology and becoming immortal. I think conquering Ryuvia has been an obsession of his for years."
    asa "Rumor has it that he's amassing a collection of Ryuvian relics from across the galaxy. For what purpose, nobody knows."
    kay "Whatever purpose it is, it's not for ending world hunger. Someone like Arcadius finding lost technology is bad news for the entire galaxy. We have to act fast to stop him before he becomes unstoppable."

    menu:
        "You saw your own father get killed. Are you feeling all right?":
            jump sawfatherkilled
        "You're now the Queen of Ryuvia. What are you going to do?":
            jump nowqueendo
        "That'll be all. I'm glad to have you back, Asaga.":
            jump allgladback

label nowqueendo:

    show asaga uniform armscrossed thinkingfrown with dissolve

    asa "Ugh... I don't even want to think about being called that..."
    asa "I'm through with being royalty, capt'n. It's just not what I was meant to be."

    menu:
        "You have every right to choose your own destiny, Asaga.":
            jump rightchoosedestiny

        "Even if it's not what you wanted, you still have a responsibility to your people.":
            jump notwantresponsibility

label rightchoosedestiny:

    show asaga uniform altneutral sad with dissolve

    asa "Ryuvia's been ruled by a monarch for too long."
    asa "After all of this is over, I'm abdicating."

    jump nobodykingsday

label notwantresponsibility:

    show asaga uniform altneutral sad with dissolve

    asa "I know that..."
    asa "I'm going to fight to liberate Ryuvia from PACT. I won't stop until Arcadius is defeated and my people are free again."
    asa "Then, after all of this is over, I'm abdicating."

    jump nobodykingsday

label nobodykingsday:

    asa "Nobody needs kings and queens in this age, captain. The people deserve elected officials. Not royals."
    kay "You're right. That's the best you can do for your people right now."

    menu:
        "You saw your own father get killed. Are you feeling all right?":
            jump sawfatherkilled
        "You must know more about Arcadius. Is there anything you can tell me about him?":
            jump knowarcadiustell
        "That'll be all. I'm glad to have you back, Asaga.":
            jump allgladback

label allgladback:

    show asaga uniform armscrossed smileblush with dissolve

    asa "I'm glad to be back too, capt'n!"

    hide asaga with dissolve

    $ sol_location = "messhall"
    $ sol_event = "fallofryuvia"

    $ chi_location = "engineering"
    $ chi_event = "chigarathankrescue"

    $ ica_location = "hangar"
    $ ica_event = "icarithoughtsalliance"

    $ cla_location = None
    $ ava_location = None
    $ asa_location = None
    $ pro_location = None

    $ captaindeck = 0

    jump dispatch

label fallofryuvia:

    hide screen ship_map
    scene bg messhallwindows
    show sola uniform backturn neutral
    with dissolve

    window show

    sol "Captain."
    kay "I thought I'd find you here."
    kay "Thanks for helping us out with that rescue."
    sol "... ... ..."

    show sola uniform handsbehindback sad with dissolve

    sol "The worst has come to pass. Ryuvia has fallen."
    kay "Not yet. The Queen still lives. We'll liberate Ryuvia and free your people."

    show sola uniform handonchest sad with dissolve

    sol "My sacrifice was meaningless. In my time, the Holy Ryuvian Empire stretched across the galaxy. It was the center of all of the sciences, civilization, and produce."
    sol "And yet... you tell me the Ryuvia of today is nothing more than a forgotten world, to be conquered so easily by barbarians?"
    kay "Your sacrifice was not in vain. For over a millennia after your death, the flame of Ryuvia burned on. It was only within the last 400 years that Ryuvia lost its power, and only due to infighting within the royal court."

    show sola uniform handsbehindback sad with dissolve

    sol "... ... ..."
    sol "And so it was us who sabotaged our own empire and caused our eventual collapse?"
    kay "Yes."
    sol "... ... ..."
    sol "Then nothing has changed."

    show sola uniform backturn neutral with dissolve

    sol "Leave me. I wish solitude."
    kay "All right."
    sol "... ... ..."
    kay "You don't have to be alone, Sola. We're all here for you."
    sol "Farewell."

    $ sol_location = None
    $ captaindeck = 0

    jump dispatch

label chigarathankrescue:

    hide screen ship_map
    scene bg engineering
    show chigara uniform handonchest smile
    with dissolve

    window show

    chi "Ah, captain. Umm... Thank-you for helping Asaga."
    chi "As her friend, it means a lot to me, what you did for her..."
    kay "Of course we had to rescue her. Asaga's a member of our crew."

    show chigara uniform handonchest closedeyessmile with dissolve

    chi "Eh-heh. I'm glad to have you as our captain... Captain."

    show chigara uniform altneutral neutral with dissolve

    chi "Was there anything else you needed? Perhaps an anomaly to scan? A new research project? Eh-heh..."
    kay "Nothing at the moment, Chigara."
    chi "Please come by my lab any time you need anything, captain."
    kay "By the way... You're not startled any more when I come around."
    chi "Ah, I installed some cameras around engineering which now warn me whenever you approach."
    kay "O-oh. I, uh... didn't know you did that."

    show chigara uniform handonchest sad with dissolve

    chi "Is it not allowed?"
    kay "Well, I'm sure it's fine. Just, uh... don't let Ava find out about it."

    show chigara uniform handstogether smileblush with dissolve

    chi "Yes captain. Maybe I could test out my new camouflage composite on them..."

    $ chi_location = None
    $ captaindeck = 1
    $ pro_location = "captainsloft"
    $ pro_event = "alliancedeclareswar"

    jump dispatch

label icarithoughtsalliance:

    hide screen ship_map
    scene bg hangar
    show icari uniform handonhip smile
    with dissolve

    window show

    ica "I must say, that was quite a rescue captain. I wasn't sure if we could have pulled it off."

    menu:
        "Of course we had to pull it off. Asaga's a member of our crew.":
            jump pulloffcrew
        "To tell the truth, I'm surprised we made it out of there myself.":
            jump truthsurprisedthere

label pulloffcrew:

    show icari uniform armscrossed smilesidesmile with dissolve

    ica "Heh. One day captain, that heart of yours is going to get you killed. I just hope I'm there to save your ass when that happens."
    kay "That heart's the reason why you're onboard this ship, Icari. Doing the right thing and doing the expedient thing aren't mutually exclusive, you know. You can stand for what's right and still make it out alright."
    ica "Alright, captain."

    jump icarianywaysforsomething

label truthsurprisedthere:

    show icari uniform armscrossed smilesidesmile with dissolve

    ica "Haha, just don't go around looking so unconfident in front of the crew. You know, there are even some rumors circulating about you."
    kay "What rumors?"
    ica "Haven't you been checking the holonet? You've just rescued the Ryuvian princess. People are starting to take notice of what you've been doing."
    ica "The more things are looking like it's going down the chute, the more people want to rally around a leader. So make sure you live up to expectations, alright?"

    menu:
        "I'm just doing what's good for the galaxy, Icari. I'm not in this for the attention.":
            jump doinggoodgalaxy
        "The galaxy needs to rally against PACT. I'll do everything I can to inspire people in the war against PACT.":
            jump needsagainsteverything

label doinggoodgalaxy:

    $ captain_moralist += 1

    ica "Right. Well, it won't be long until holovision news crews are begging you for interviews."

    jump icarianywaysforsomething

label needsagainsteverything:

    $ captain_prince += 1

    ica "You better get a new suit then. From the look of things, you'll be in the limelight much more from now."

    jump icarianywaysforsomething

label icarianywaysforsomething:

    show icari uniform altneutral smile with dissolve

    ica "Anyways, did you need me for something?"

    menu:
        "Do you think we should fight alongside the Alliance?":
            jump youshouldalongsidefight
        "Nothing more. Keep up the good work, Icari.":
            jump morekeepwork

label youshouldalongsidefight:

    show icari uniform armscrossed neutral with dissolve

    ica "I meant what I said earlier. The only chance we have of stopping PACT is to work with the Alliance. Right now, practically the entire Neutral Rim belongs to PACT and the few independent planets left don't stand a chance by themselves."
    ica "PACT needs to be stopped no matter the cost. I say working with the Alliance is the best chance we've got at ending this war quickly."

    menu:
        "I think we can trust the Alliance. They're the biggest democracy the galaxy has known. Better working with them than letting PACT rule the galaxy with an iron fist.":
            jump trustdemocracyworking
        "I don't know if I like this yet. If the Alliance does defeat PACT, what will that mean for planets like Cera? Won't we be replacing one dictator for another?":
            jump likewillreplace

label trustdemocracyworking:

    $ captain_moralist += 1

    show icari uniform handonhip smile with dissolve

    ica "Sure. Although I like the fact they carry the biggest guns in the galaxy more than the fact they're a democracy. Haha."

    show icari uniform armscrossed neutral with dissolve

    ica "Look captain, democracies don't win wars. Warships and cannon do. We need warships and the Alliance has warships. So we work together. It's as simple as that."

    jump offerhelpnoway

label likewillreplace:

    $ captain_prince += 1

    show icari uniform neutral neutral with dissolve

    ica "Heh. Well, once PACT's gone, the Alliance will probably fill in the power vacuum. I'm not sure what that'll mean for the Neutral Rim."
    ica "Probably, the current PACT occupied territories will end up being occupied by the Alliance instead. Either way, it doesn't look like your planet will be able to return to the way things were."
    kay "I'm not going to let Cera become a colony. Alliance or PACT."

    show icari uniform armscrossed neutral with dissolve

    ica "Hopefully for you, the Solar Congress will be too busy debating to make much of a difference. Well, that's assuming the military doesn't take over anyways."
    ica "Anyways, that's too far into the future to really predict. Right now, it's obvious that you're going to need the Alliance's help if you're going to take back Cera."

    jump offerhelpnoway

label offerhelpnoway:

    ica "If the Alliance is going to offer their help in stopping PACT, we have to take it. There's no other way to stop PACT."
    kay "I get what you're saying. I'll keep it under advisement."
    ica "Thanks captain. Anyways, tell me what ends up happening."

    $ ica_location = None
    $ captaindeck = 2
    jump dispatch

label morekeepwork:

    ica "See you."

    $ ica_location = None
    $ captaindeck = 2
    jump dispatch

label alliancedeclareswar:

    hide screen ship_map
    scene bg captainsoffice
    show ava uniform neutral neutral
    with dissolve

    window show

    ava "Captain, have you checked the holovision?"
    kay "No."
    ava "The Solar Alliance has just declared war on PACT. Admiral Grey is on the line for you."
    kay "Seems like the invasion of Ryuvia finally woke the Alliance up. Put me through."

    hide ava with dissolve
    show grey with dissolve

    play music "Music/New_Dawn.ogg" fadeout 1.5

    gre "Captain. A pleasure to see you again."
    kay "Admiral Grey."

    menu:

        "A pleasure to see you too admiral.":
            jump pleasuretooadmiral
        "You put us in quite a bind at Versta...":
            jump usbindversta

label pleasuretooadmiral:

    jump worddaringspread

label usbindversta:

    gre "I have no idea what you may be referring to."

    if Saveddiplomats == True:
        jump hadwhichfulfilled
    if Saveddiplomats == False:
        jump deathtragicrallying

label hadwhichfulfilled:

    gre "You had a mission which you fulfilled. That is all which I recall."
    jump worddaringspread

label deathtragicrallying:

    gre "The death of the diplomats was tragic, but not in vain. Their deaths were a rallying cry for those in Alliance who wanted leadership instead of cowardice."
    jump worddaringspread

label worddaringspread:

    gre "Word of your daring rescue of the princess has spread even here. I must say captain, I am quite impressed you made it out of that alive."
    kay "I have one hell of a team here, admiral."
    gre "Yet, the rescue was merely the silver lining of a grim situation. With the fall of Ryuvia, PACT is in the perfect position to strike Far Port, the entryway into Alliance space."
    gre "If Far Port falls, PACT will flood into at least five populated Alliance systems before we can even muster our forces. The Alliance has not seen a war fought within our own soil in a hundred years."
    gre "A PACT occupation of an Alliance planet is not an option. We must hold Far Port if we are to win this war."
    kay "We're already in position here at Far Port. We just need some repairs and supplies."

    if Saveddiplomats == True:
        gre "I have sent four of our closest fleets to Far Port to mount a defense."
        gre "I will not mince words. The situation is not looking good here."
        gre "Years of neglect and bureaucratic resistance have made our fleets inefficient. Only one of the fleets which I have dispatched will make it in time to meet the PACT assault."
        gre "Our fleets are not prepared for this war. Some of our ships have not even been manned for decades. Worse, our supplies and ships are scattered across our territory with no unifying chain of command."
        gre "But all is not lost, captain. We have very skilled pilots and an economic base which far out produces PACT. We will muster our strength and meet PACT head on. It will merely take time."
        gre "You must hold out at Far Port with the Second Fleet until the remaining fleets arrive."

    if Saveddiplomats == False:
        gre "I have sent four of our closest fleets to Far Port to mount a defense."
        gre "After the death of the diplomats on Versta, I tried my best to mobilize our fleets."
        gre "It was not easy. Years of neglect has made our fleets inefficient. Everything is blocked behind red tape now."
        gre "Our supply chains were broken. Virtually everything had to be remade from scratch."
        gre "Of the fleets I've dispatched, only one will make it in time to meet the PACT fleet."
        gre "Our fleets are vast and mighty. But it will still take time to muster our strength. You must hold out at Far Port until our full forces arrive."

    kay "What is the size of the enemy fleet?"
    gre "Our intelligence reports that five PACT fleets are converging on Far Port's position. The commander of the attack will be Veniczar Cullen."
    gre "I believe you are already familiar with him."
    gre "All together, I predict at least seven battleships, six carriers, eighty cruisers, and over four hundred support vessels. Further, we believe Arcadius himself will observe the battle from his flagship, the Legion."
    kay "If we only have one fleet to defend the planet, we're outnumbered nearly one to five. Those aren’t good odds, admiral."
    gre "Yes, which is why I am appointing you my special advisor."
    gre "You're the only one whose fought those odds. Nobody in the Alliance fleet has even seen a PACT vessel up close. Yet you know how they operate. You're the only person we have who've fought them outside of simulators."
    gre "Your mission is the defense of the Alliance gateway world, Far Port. You must hold out there until our reinforcements arrive."
    kay "Understood, admiral."
    gre "I know I'm asking much. To help you prepare for the battle, I'm sending you one of my personal advisors to your starship."
    gre "I understand that you're currently looking for more pilots. I'm sure she'll be a valuable asset to your crew."

    menu:
        "We'll need all the help we can get. Thank you, admiral.":
            jump needhelpyou
        "Wait, an Alliance officer serving onboard my ship? I'm not sure if that's really necessary...":
            jump needhelpyou

label needhelpyou:

    gre "She's a talented pilot and a loyal officer. I'm sure she'll fit right in with your crew."
    gre "She's already been dispatched and will arrive with the Second Fleet by tomorrow. I expect she'll be given due care."
    gre "That'll be all for now, captain. My lieutenant will give you the specifics of the coming battle when she arrives. Admiral Grey out."

    hide grey with dissolve

    kay "(An Alliance officer here? I'm not sure if the crew will like this...)"
    kay "(That admiral sure is pushy...)"

    window hide

    stop music fadeout 1.5

    show eyecatch_top with eyecatch_wipe
    show eyecatch_bottom with eyecatch_wiperev
    show eyecatch_logo with dissolve
    scene bg black2 with dissolvelong
    scene cg_asagashower1 with dissolvelong



    window show

    play music "Music/shower.ogg"

    "... ... ..."
    asa "... ... ..."
    asa "(Pah... So good to be back.)"
    asa "(I never thought I'd get out of that jam in one piece...)"
    asa "... ... ..."

    play sound "sound/heartbeat.ogg"

    scene cg_weddingcrash1 with dissolve

    pause 0.5

    scene cg_asagashower2 with dissolve

    asa "Urk..."
    asa "W-what am I thinking..."
    asa "(So much stuff's happened, but the only thing I can think about is the captain...)"
    asa "C'mon Asaga! Pull yourself together!"
    asa "You're the queen now!"
    asa "... ... ..."
    asa "(Except that just makes everything worse...)"
    asa "Huu..."
    asa "This sucks..."
    asa "... ... ..."
    asa "I'm so hot down there just thinking about it..."
    asa "Uuu..."

    play sound "sound/hit.ogg"
    show layer master at shake1

    pause 0.2

    play sound "sound/hit.ogg"
    show layer master at shake1

    pause 0.2

    play sound "sound/hit.ogg"
    show layer master at shake1

    ica "Hurry up in there! What's taking forever!?"
    asa "Eek! H-hang on!"
    cla "Oh Icari... Why don't we just all shower together if you're gonna be so impatient!"
    ica "S-shut up!!! L-like I would ever want to see y-y-your... chest rockets!"
    asa "Sniffle... Okay, okay, I'm done..."

    play music "Music/Love.ogg" fadeout 1.5
    scene black with horizontalwipe

    scene bg messhallwindows with horizontalwipe

    show asaga uniform armscrossed sadwideeyesblush with dissolve

    asa "... ... ..."
    asa "Uck... W-what am I thinking lately..."

    show asaga uniform excited focusedpoutblush with dissolve

    asa "No! No! This isn't the time for that!"
    asa "You've got a fight to win, Asaga!"
    asa "Come on... You're the hero of justice! For freedom and equality!"

    show asaga uniform altneutral gloomblush with dissolve

    asa "Uuuuu..... It's not working..."

    show sola uniform backturn neutral:
        xpos 0.8
    with dissolve

    sol "... ... ..."

    show asaga uniform neutral surprise with dissolve

    asa "U-uck!"

    show sola uniform handonchest neutral with dissolve

    sol "You are... the Queen."

    show asaga uniform altneutral embarassedsurpriseblush with dissolve

    asa "... ... ..."
    asa "How long have you been there?"

    show sola uniform backturn neutral with dissolve

    sol "The stars give me peace."

    show asaga uniform altneutral neutral with dissolve

    asa "... ... ..."
    asa "Ya know... You don't have to call me that. I'm just Asaga."

    show sola uniform altneutral neutral with dissolve

    sol "... ... ..."

    show sola uniform handonchest neutral with dissolve

    sol "I am Sola."

    show asaga uniform altneutral neutral:
        zoom 1
        ease 0.5 xpos 0.3
    show sola uniform altneutral neutral:
        zoom 1
        ease 0.5 xpos 0.7

    asa "What are you doing here?"

    show sola uniform neutral neutral with dissolve

    sol "Reflecting."
    sol "Far Port was a mighty trade world during my time. Merchants from across the Empire gathered here to engage in commerce and exchange ideas."
    sol "It was the gateway to the core worlds, where Ryuvian splendor met the exotic cultures of outsiders."
    sol "And it was the place where I was born."

    show sola uniform handsbehindback sad with dissolve

    sol "Yet, now... It is merely an abandoned world, where civilization has been overtaken by the wilderness."
    asa "... ... ..."

    show asaga uniform handsonhips happy with dissolve

    asa "One day, this place'll be a bustling port again."
    asa "After we send PACT packing back to New Eden, Ryuvia will grow again."
    sol "Our Empire has become weak. Our enemies have stolen our technology. Our culture has been forgotten."

    show asaga uniform neutral smile with dissolve

    asa "That's why we gotta change."
    asa "It was our own arrogance which led to our fall. The Ryuvian lords became too selfish. Sons killed their fathers and brothers betrayed brothers, all for a piece of the Ryuvian dream."
    asa "In the end, in our fight to own the Empire, we destroyed the very thing we wanted."
    asa "We're gonna make a new Ryuvia, where the leaders act for the good of the people."
    sol "... ... ..."

    show sola uniform handsbehindback lookleft with dissolve

    sol "The talbur was right to illuminate only for you."

    show sola uniform backturn neutral with dissolve

    sol "... ... ..."
    sol "You desire the captain to lead by your side?"

    play sound "sound/hit.ogg"
    show asaga uniform neutral shockooblush:
        zoom 1
        ease 0.02 xpos 0.292
        ease 0.04 xpos 0.307
        ease 0.02 xpos 0.3
        repeat 5
    with dissolve

    asa "G-guck!"

    show asaga uniform neutral laughooblush with dissolve

    asa "No, no, no! Whatever gave you that idea!? Uwah-hahahaha!"

    show asaga uniform armscrossed happyblush with dissolve

    asa "The captain's got his own mission! The total surrender of PACT and the liberation of his home world, Cera!"
    sol "... ... ..."
    sol "Your face."

    show asaga uniform thinking forcedsmilekittyblush with dissolve

    asa "Eh?"
    sol "It is red."

    show asaga uniform excited forcedlaughblush with dissolve

    asa "Uhh... well, time to calibrate the Black Jack for the big battle! You better get your Seraphim ready too!"
    asa "Uwah-hahahaha!"

    show asaga uniform altneutral grinblush with dissolve
    show asaga uniform altneutral grinblush:
        zoom 1
        ease 0.2 xpos 0.4
        ease 0.5 xpos -0.3

    pause 1.0

    sol "... ... ..."
    sol "(...She's still no queen.)"


    play music "Music/Tokyo_Lights.ogg" fadeout 1.5

    scene bg black with horizontalwipe
    scene bg bridge with horizontalwipe

    show ava uniform handonhip neutral with dissolve

    ava "Captain. The Second Fleet has arrived. And our guest is waiting for us in the hangar."
    kay "Right. Well, let's go meet our new guest."
    ava "Are you sure this is wise, captain? Letting foreign military personnel on board the ship, I mean."
    kay "Uh, let's just say the admiral insisted."
    kay "Let's see who she is before making any judgments though."

    show ava uniform salute neutral with dissolve

    ava "Understood captain."

    scene bg hangar with dissolve
    show kryska uniform salute mad:
        xpos 0.3
    with dissolve
    show ava uniform altneutral neutral:
        xpos 0.7
    with dissolve

    kry "Lieutenant Kryska Stares reporting for duty, sir!"
    kay "At ease, lieutenant. I'm Captain Kayto Shields and this is First Officer Ava Crescentia. Welcome aboard the Sunrider."

    show kryska uniform neutral frown with dissolve

    kry "My pleasure, sir!"

    show kryska uniform altneutral focustalk with dissolve

    kry "I have been ordered by Admiral Grey himself to serve as the Alliance liaison officer on board the Sunrider. I look forward to working with you, captain."

    menu:
        "Tell me about yourself, lieutenant.":
            jump meyourselflieutenant

        "Did you come with your own Ryder?":
            jump comeownryder

        "You're a member of our crew now. Feel free to make yourself at home.":
            jump membercrewyourself

        "You're on board this ship, but don't forget, this isn't an Alliance vessel. We have our own rules here.":
            jump forgetalliancerules

label meyourselflieutenant:

    show kryska uniform altneutral frown with dissolve

    kry "Rank: Lieutenant, First Class. Twenty two years of age. Previous service: Commander of the Air Group onboard the Alliance carrier Montesquieu. Hometown: New Seattle, Luna."

    show ava uniform altneutral neutral with dissolve

    ava "You were an Alliance CAG? Then what are you doing here, on the Sunrider?"
    kry "I go wherever my duties require me to, ma'am."
    kay "A long way from home, at least."

    hide ava with dissolve

    menu:
        "Did you come with your own Ryder?":
            jump comeownryder

        "You're a member of our crew now. Feel free to make yourself at home.":
            jump membercrewyourself

        "You're on board this ship, but don't forget, this isn't an Alliance vessel. We have our own rules here.":
            jump forgetalliancerules

label comeownryder:

    show kryska uniform neutral frown with dissolve

    kry "Yes captain. I've already arranged to have the Paladin transferred to the Sunrider. You will find it a fine complement to your current Ryder wing, I'm sure."
    kay "Glad to hear."

    menu:
        "Tell me about yourself, lieutenant.":
            jump meyourselflieutenant

        "You're a member of our crew now. Feel free to make yourself at home.":
            jump membercrewyourself

        "You're on board this ship, but don't forget, this isn't an Alliance vessel. We have our own rules here.":
            jump forgetalliancerules

label membercrewyourself:

    $ affection_tera += 1

    show kryska uniform salute mad with dissolve

    kry "Thank-you sir!"
    kay "Ava will help you move into our crew quarters. You think you can squeeze one more person into the female quarters, Ava?"

    show ava uniform armscrossed neutral with dissolve
    ava "I've already taken the liberty of converting the male quarters to accommodate the growing size of our female crew."
    kay "Wha-"
    ava "Obviously, I will not allow any males join our team in light of the modifications I've made."
    kay "(Even that Ava knows how to crack a joke, huh... Or is she actually serious!?)"

    jump endofkryskaintro

label forgetalliancerules:

    show kryska uniform salute mad with dissolve

    kry "Understood sir! I won't let you down!"
    kay "You're dismissed, lieutenant. First Officer Crescentia will help you get moved in."

    show ava uniform armscrossed neutral with dissolve

    ava "Just come this way."

label endofkryskaintro:


    $ paladin_weapons = [PaladinMissile(),PaladinAssault(),PaladinKinetic()]
    $ paladin = create_ship(Paladin(),(9,8),paladin_weapons)

    $ captaindeck = 2
    $ asa_location = "messhall"
    $ asa_event = "asachi_maskofveniczar"
    $ chi_location = "messhall"
    $ chi_event = "asachi_maskofveniczar"

    $ ava_location = "bridge"
    $ ava_event = "fakeservicerecord"

    $ kry_location = "hangar"
    $ kry_event = "disputeicariphoenix"
    $ ica_location = "hangar"
    $ ica_event = "disputeicariphoenix"

    $ sol_location = None
    $ cla_location = None
    $ pro_location = None

    jump dispatch

label fakeservicerecord:

    hide screen ship_map
    scene bg bridge
    show ava uniform neutral neutral
    with dissolve

    window show

    kay "Finished helping soldier girl move in?"
    ava "All done. By the way, I think you should take a look at this."

    show ava uniform handonhip neutral with dissolve

    ava "I took the liberty of looking a bit deeper into our lieutenant's service records on the Alliance."
    kay "And?"
    ava "Well, I found a slight discrepancy. Her records indicate that she served on the Montesquieu two days before it was officially commissioned."
    ava "It could have been nothing, but after what happened with Claude, I got Chigara to take another look at it. She discovered that the lieutenant's record had been wiped clean and then rewritten with new data."

    show ava uniform armscrossed neutral with dissolve

    ava "As far as Chigara can tell, she doesn't even think the Montesquieu is a real ship."
    kay "So what are you saying?"

    show ava uniform handonhip neutral with dissolve

    ava "An ace pilot with a fake profile, serving onboard a ship that doesn't exist? That sounds likes like something only Alliance Spec Ops would do."
    kay "Heh, should have known. Our new pilot's probably the Admiral's spy, sent here to keep tabs on us just in case. Doesn't look like the Alliance quite trusts us yet, does it?"
    ava "Want me to keep an eye out for her?"

    menu:
        "Keep our guest on a short leash. If she does anything suspicious, tell me immediately.":
            jump guestleashsuspicious
        "Don't worry about it. We don't have anything to hide from the Alliance. We're going to have to learn to trust each other eventually.":
            jump worryhidetrust

label guestleashsuspicious:

    $ captain_prince += 1

    show ava uniform salute neutral with dissolve

    ava "Understood captain. If she as much as sneezes suspiciously, I'll make a log of it."

    $ captaindeck = 1
    $ ava_location = None
    jump dispatch

label worryhidetrust:

    $ captain_moralist += 1

    show ava uniform armscrossed looklefttalk with dissolve

    ava "If you say so. I'll bug her bunk just in case though."
    kay "Ava..."

    show ava uniform armscrossed narroweyefrown with dissolve

    ava "It'll just be a small one."

    $ captaindeck = 1
    $ ava_location = None
    jump dispatch

label asachi_maskofveniczar:

    hide screen ship_map
    scene bg messhall
    with dissolve

    show asaga uniform armscrossed grin:
        xpos 0.3
    with dissolve
    show chigara uniform handonchest smile:
        xpos 0.7
    with dissolve

    window show

    asa "Oh! It's the capt'n!"
    chi "Ah, good evening captain."
    kay "Our next battle will be the biggest one yet. How are you two holding up?"

    show asaga uniform armscrossed confidenthappy with dissolve

    asa "Don't worry 'bout a thing! Chigara and I will do our best!"
    kay "How about you, Chigara? Are you eating alright?"

    show chigara uniform twiddlefingers sadsmileblush with dissolve

    chi "Umm... It's a little hard digesting because I'm so nervous, but I think I'll be alright."

    show asaga uniform excited determined with dissolve

    asa "No, no, no, Chigara! You gotta eat before a fight or else you're gonna run outta energy!"

    menu:

        "Not everyone's as macho as you, Asaga.":
            jump everyonemachoasaga
        "Asaga's right, Chigara. Eat up.":
            jump asagachigaraeat

label everyonemachoasaga:

    $ affection_chigara += 1
    jump notsleepingleft

label asagachigaraeat:

    $ affection_asaga += 1
    jump notsleepingleft

label notsleepingleft:

    show asaga uniform excited happy with dissolve

    asa "Uwahaha! Nom nom nom..."

    show chigara uniform handonchest sad with dissolve

    chi "I'm sorry captain. I haven't really been sleeping well lately, ever since we left Ryuvia."
    chi "It was frightening to finally meet the Veniczar in person... I can still hear his voice ringing in my head when I sleep."

    show asaga uniform handonhips happy with dissolve

    asa "Bah, don't be scared, Chigara! We'll take him down together!"
    chi "Veniczar S. Arcadius. Who do you think he is underneath that mask?"

    show asaga uniform thinking thinking with dissolve

    asa "He was the former slave who led the PACT Rebellion against the New Empire, right? I heard some rumors from my father's advisors that the man who claims to be Arcadius now might actually be a different person though."
    asa "Mmmm, why do you suppose he always wears that mask, captain?"

    menu:
        "It might to make the Veniczar immortal. Even if Arcadius dies, someone else can just take up the mask and continue on as if nothing's changed.":
            jump immortalancientpoured

        "It's intimidating, isn't it? People fear the unknown.":
            jump intimidatingfearunknown

        "He hides behind a mask because he's scared. The mask lets him use body doubles and keeps his true identity a secret.":
            jump hidesscaredmask

label immortalancientpoured:

    asa "Mmm... An immortal leader, huh? I remember, the ancient Ryuvians kings poured billions into researching immortality. Even though they couldn't succeed, the research lead to some crazy breakthroughs for anti-aging facial creams."
    kay "Ava might be interested. You wouldn't happen to have some now, would you?"

    show asaga uniform armscrossed grin with dissolve

    asa "Ahahaha, I think the last stores of it were depleted decades ago."

    jump underneathtearmask

label intimidatingfearunknown:

    show asaga uniform armscrossed grin with dissolve

    asa "Ahahaha, you suppose he looks really ugly underneath?"
    kay "The Veniczar's been around ever since the beginning of the PACT Rebellion. If it's still the same guy from back then, he's probably in his late 60's. I don't imagine he's that good looking."

    show asaga uniform thinking thinking with dissolve

    asa "Mmm... The Veniczar we met seemed younger than that though."
    kay "He could just be acting. Or maybe the Veniczar now is a different one from back then."

    jump underneathtearmask

label hidesscaredmask:

    asa "So you're sayin' essentially that the Veniczar's too much of a coward to reveal his identity in public?"
    kay "Something like that."

    show asaga uniform handsonhips closedeyesgrin with dissolve

    asa "Bah, someone like that won't be hard to beat at all!"

    jump underneathtearmask

label underneathtearmask:

    show asaga uniform excited happy with dissolve

    asa "Still, I'd love to see just who's underneath that mask. Eh-heh, I want to be the one to finally tear that mask off!"
    kay "One day, Asaga. One day."

    $ asa_location = None
    $ chi_location = "hangar"
    $ chi_event = "chigarafirsttea"

    $ captaindeck = 0

    jump dispatch

label disputeicariphoenix:

    hide screen ship_map

    scene bg hangar
    show icari uniform point angry:
        xpos 0.3
    show kryska uniform armscrossed madtalk:
        xpos 0.7
    with dissolve

    window show

    ica "Oy, I'm not going to let you touch my Phoenix!"
    kry "Ms. Isidolde. Your ryder is in violation of at least 14 different Alliance safety regulations. In its current condition, I cannot allow it to fly with the rest of the squad!"
    kay "What's going on here?"

    show kryska uniform altneutral focustalk with dissolve

    kry "Captain Shields. I was informing Ms. Isidolde that her ryder is a potential safety hazard to both herself and the crew."
    kay "What's wrong with it?"

    show icari uniform armscrossed madtalk with dissolve

    ica "The only thing wrong with it is that I cut through the damned red tape the Alliance puts around everything."
    ica "Since the Solar Congress' in the Karium lobby's pockets, all Alliance ryders need to have exhaust ports made with Karium, even though pretty much the whole galaxy knows Heratium works just as well and is lighter!"

    show kryska uniform altneutral madtalk with dissolve

    kry "The mercenary fails to point out that Heratium shatters into a thousand razor sharp fragments when it explodes, while Karium splinters into harmless strings."
    kry "Captain, you cannot allow such a danger to exist on your hangar bay. The safety of your pilots is at stake here, all for the ego of one mercenary."
    ica "Ah, I've used Heratium all my life and I never had problems with it!"
    ica "That's just all damned propaganda spread by the Karium lobby to make the galaxy buy an obsolete good that should have been kicked off the market ages ago."
    ica "If the Solar Congress actually let people decide what to buy instead of gets bullied by cartel interests, then everyone would know Heratium is stronger, lighter, and more efficient!"

    menu:
        "Your concerns have been noted, Lieutenant. But this is my ship, and we don't follow Alliance protocols here.":
            jump notedshipprotocols
        "Sorry Icari, but you're not working solo any more. I can't let you risk lives by modifying your ryder.":
            jump solodependrisk

label notedshipprotocols:

    $ affection_icari += 2

    show kryska uniform salute mad with dissolve

    kry "Understood, sir. But you will excuse me if I steer clear of the Phoenix while it is doing its burn tests on the hangar floor."

    show icari uniform armscrossed smilesidesmile with dissolve

    ica "Tsch. Don't come back to me begging for Heratium when the Phoenix leaves your Paladin in the dust during the battle."

    show kryska uniform neutral frown with dissolve

    kry "Well then, I do believe I have more work to do. May I be dismissed, captain?"
    kay "You're dismissed, Lieutenant."
    kry "Sir."

    hide kryska with dissolve
    show icari uniform bothhandsonhips grin with dissolve

    ica "Hah, good riddance! Just who does she think she is, coming onboard this ship and bossing everyone around?"


    $ kry_location = None
    $ ica_location = None
    $ captaindeck = 2

    jump dispatch

label solodependrisk:

    $ affection_tera += 2

    show icari uniform point angry with dissolve

    ica "You're actually buying into their propaganda too, captain!?"
    kay "I'll have Chigara take a look at your ryder, Icari. I'm sure we can figure out a way to make it safe while still keeping its specs."

    show icari uniform armscrossed closedeyesshout with dissolve

    ica "Ugh... It's fine the way it is, thank you."
    kry "Is that how you respond to your superior officer, mercenary?"
    ica "Damn you... sir."

    $ kry_location = None
    $ ica_location = None
    $ captaindeck = 2

    jump dispatch

label chigarafirsttea:

    hide screen ship_map
    scene bg hangar
    show chigara uniform palmsup surpriseblush
    with dissolve

    window show

    chi "Oh! Captain!"
    kay "Calibrating the Liberty for the big day?"

    show chigara uniform handstogether smile with dissolve

    chi "I was just finishing up."
    kay "You haven't been looking so well lately. Still not sleeping well?"

    show chigara uniform handonchest sad with dissolve

    chi "I'm sorry. I hope I won't be a burden during the battle."
    kay "You're still the best engineer we've got. Get some rest."
    chi "The Veniczar's voice... I feel like it's ringing in my head. It calls out to me, like a siren's song."
    kay "Hey relax. You've been under a lot of stress lately."

    show chigara uniform palmsup surpriseblush with dissolve

    chi "Ah, uhh... I'm sorry, captain. I-I must just sound crazy. Please forget what I just said."

    show chigara plugsuit handstogether sadblush with dissolve

    chi "... ... ..."
    chi "I've been thinking of what happened on Diode lately."
    kay "You mean the Diode catastrophe?"
    chi "Yes..."
    kay "Do you want to talk about it?"

    show chigara uniform handonchest forcedsmileblush with dissolve

    chi "Umm... If it's not too much trouble. I was just finishing up with the Liberty here."
    kay "Come on. I have a tea set in my office."

    play music "Music/Moonlit_Night.ogg" fadeout 1.5
    scene bg captainsloft with dissolve
    show chigara uniform handstogether embarassedsmile with dissolve

    kay "Here, take your pick. All of these brews are from Cera."
    chi "Thank-you, captain."
    kay "Make yourself at home, Chigara. Heh, I never imagined Cera Command would give me such a nice office. I guess the Sunrider's pretty cutting edge in more ways than one."
    chi "Eh-heh..."
    kay "I heard from the reports that nobody made it out of the Diode catastrophe alive. I guess they forgot to count one survivor."

    scene cg_chigarateatime_sad with dissolve

    chi "Yes..."
    chi "Diode was a strange world in a former binary star system where one of the suns had collapsed into a black hole. Obviously of no interest to anyone but scientists."
    chi "My father was the lead scientist on the Paradox Project. I was actually born on the science station on Diode."
    kay "The Paradox Project?"
    chi "We were seeking the holy grail of scientific technology: The power to control time."
    chi "Imagine a device which lets you return to the past and redo your life. Or which allowed you to restore yourself after you were killed. Or which even allowed you to remove your enemies before they were even born."
    chi "Not even the ancient Ryuvians discovered that power, or else they'd still be alive today."

    menu:
        "Technology like that is dangerous.":
            jump techthatdangerous
        "Technology like that would sure help us now.":
            jump techwouldhelp

label techthatdangerous:

    $ captain_moralist += 1

    chi "But captain, technology is only as good as the person wielding it. In the right hands, technology like that could save billions of lives."
    chi "It might even mark the next stage of human existence. With such technology, wars, famine, and even human conflict would be mooted."
    chi "The power to control time would mark a new phase in our existence as a species, where we manipulate not three dimensions, but four."
    jump sohappenedparadox

label techwouldhelp:

    $ affection_chigara += 1

    chi "Eh-heh, technology always did make our lives easier..."
    chi "Too bad it can't save us all the time..."
    jump sohappenedparadox

label sohappenedparadox:

    kay "So what happened to the Paradox Project?"
    chi "... ... ..."
    chi "Something went wrong with the project. We accidentally opened a black hole in orbit around the planet, destroying our research station and most of Diode in the process. Luckily, I managed to get away on an escape pod... But the rest of the team weren't so lucky."
    chi "Both my parents died in the accident. As far as I know, I was the only survivor."

    menu:
        "How did you open a black hole on your planet?":
            jump howblackplanet
        "Do you know what exactly went wrong?":
            jump youexactlywrong
        "I'm sorry to hear that. The accident must have been tragic.":
            jump sorryaccidenttragic

label howblackplanet:

    chi "It's kind of complicated, but two super dense particles must have collided with each other during the experiment at such speeds as to create a singularity."
    chi "The resulting particle would be so dense as to tear a hole in the space-time continuum, or open what is commonly called a black hole."
    chi "There was only one possible outcome after something like that happened."
    chi "Our research station was slowly devoured by the black hole. Luckily, I just happened to be right next to the escape pods. Everyone else wasn't so lucky..."
    chi "I saw with my own eyes the entire planet crumbling under the massive gravitational forces as I escaped. While the planet was luckily uninhabited, it was still terrifying seeing the power of what we had accidentally unleashed that day."
    chi "It was... life changing."

    menu:
        "Do you know what exactly went wrong?":
            jump youexactlywrong
        "I'm sorry to hear that. The accident must have been tragic.":
            jump sorryaccidenttragic


label youexactlywrong:

    chi "... ... ..."
    chi "There's no explanation why a black hole should have formed. We had so many safeguards... Something like that was simply theoretically impossible."
    chi "I've rerun computerized tests of what we did thousands of times. Every time, everything worked exactly as it was supposed to. I... don't have a scientific explanation as to why something so horrible happened..."
    kay "But?"
    chi "There's only one possible explanation left. What happened on Diode was the work of sabotage. Someone on our team must have betrayed us."
    kay "Betrayal? What would someone stand to gain by killing a team of scientists?"
    chi "... ... ..."
    chi "I don't know. I'm sorry captain. I'm... just rambling again."
    chi "I've thought about what happened so many times... Our calculations... they were so perfect. There's no way we..."

    menu:
        "Keep searching, Chigara. Black holes don't just pop up and swallow planets for no reason. There's got to be a cause.":
            jump chiteayes
        "Accidents happen, Chigara. We just have to accept it.":
            jump chiteayes

label chiteayes:
    chi "Yes captain..."

    menu:
        "How did you open a black hole on your planet?":
            jump howblackplanet
        "I'm sorry to hear that. The accident must have been tragic.":
            jump sorryaccidenttragic

label sorryaccidenttragic:

    chi "Yes..."
    chi "I never want to see the people around me die again. I'll do my best to protect this ship."
    kay "Of course, Chigara. We'll do everything in our power to make sure nobody else has to die."
    chi "Yes captain."
    chi "I'm counting on you."

    scene cg_chigarateatime_embarassed with dissolve

    chi "... ... ..."
    chi "Eh heh..."
    chi "The tea was delicious."
    kay "Really? My sister got them for me."
    "... ... ..."
    "... ..."
    "... ... ..."
    chi "Eh heh... I'm feeling better now."
    chi "I'm glad to have you as our captain."
    kay "I'll try not to let you down."
    chi "Thank-you for having me over. You must have other matters to attend to."
    kay "It was my pleasure, Chigara. You can knock on my door anytime you need me."
    chi "Eh-heh, maybe I will. Good-bye."

    play music "Music/Tokyo_Lights.ogg" fadeout 1.5

    $ chi_location = "bridge"
    $ asa_location = "bridge"
    $ asa_event = "asagachigarasneakingbridge"
    $ chi_event = "asagachigarasneakingbridge"
    $ pro_location = "bridge"
    $ pro_event = "planningbattlefarport"

    $ captaindeck = 0
    jump dispatch

label asagachigarasneakingbridge:

    play music "Music/The_Rest_of_the_Ents.ogg" fadeout 1.5

    hide screen ship_map
    scene bg bridge

    show asaga uniform altneutral confidentaggressivesmile:
        xpos 0.1
    show chigara uniform handstogether embarassedsmile:
        xpos 0.2
    show kryska uniform altneutral neutral:
        xpos 0.85 zoom 1 xzoom -1
    with dissolve

    window show

    asa "Shhh Chigara..."
    chi "Ummm... I'm not sure if we're allowed to be here, Asaga..."
    asa "This is all for the sake of the ship, Chigara! All for the sake of the ship!"
    kay "What are you two doing here?"

    show chigara uniform palmsup surpriseblush with dissolve

    chi "E-eah! C-captain!"

    show asaga uniform armscrossed confidenthappy with dissolve

    asa "Oh! Don't break our cover, capt'n! We're keepin' our eyes on the spy!"
    kay "You mean the lieutenant?"
    asa "Who else!?"
    kay "Sigh... You wouldn't have been spreading rumors about her, have you Asaga?"

    show asaga uniform armscrossed laugh with dissolve

    asa "M-me? Oh-hohoho! No, no, no, no!"

    show asaga uniform armscrossed confident with dissolve

    asa "I might have warned some of the crew who were eating with me in the lounge about the Admiral's mole, but nothing more! I'm just doin' my duty to the ship, sir!"

    show chigara uniform handstogether sadclosedeyes with dissolve

    chi "Uuu... I'm sorry, captain... I accidentally let slip to Asaga about the lieutenant's forged service record..."
    kay "You know, everyone can tell that you're here. See? Look at Ava glaring at you from across the bridge, Asaga."

    hide kryska
    show ava uniform armscrossed narroweyefrown:
        xpos 0.85
    with dissolve

    ava "Hmph!"

    hide ava with dissolve

    kay "I think you have a lecture coming later."

    show asaga uniform neutral surprise with dissolve

    asa "Uck..."

    show asaga uniform armscrossed grin with dissolve

    asa "Eh-heh... Well then, I think the two of us will be going back to the hangar... Tune up our ryders... Practice a bit on the simulator... You know, pilot-y stuff..."
    kay "Yeah. I think so too."

    show asaga uniform armscrossed grin:
        ease 0.2 xpos 0.25
        ease 0.5 xpos -0.3

    asa "See you!"

    show chigara uniform handstogether sadclosedeyes with dissolve

    chi "I'm sorry about this, captain..."

    hide chigara with dissolve

    $ chi_location = None
    $ asa_location = None
    $ captaindeck = 1
    play music "Music/Tokyo_Lights.ogg" fadeout 1.5

    jump dispatch


label planningbattlefarport:

    play music "Music/Mission_Briefing.ogg" fadeout 1.5
    hide screen ship_map
    scene bg bridge
    show ava uniform neutral neutral:
        xpos 0.3
    show kryska uniform altneutral frown:
        xpos 0.7
    with dissolve

    window show

    kay "Well lieutenant, brief me on the situation."
    kry "Sir. As you know, we have five PACT fleets approaching Far Port. Our mission objective is to hold this planet until our reinforcements arrive."
    kay "What's the ETA on the Alliance fleets?"
    kry "The First Fleet is approximately two days out. The Third, Fourth, and Sixth Fleets will not arrive for another three days."
    kay "With PACT liable to strike any time, we'll be heavily outgunned in the coming battle."
    kay "Based on our numbers, I don't think this is a battle we can win head on. What are our options?"

    show ava uniform handonhip neutral with dissolve

    ava "Far Port may be a tactically pivotal world, but it is largely uninhabited. We could try scattering the Alliance fleet around the planet and picking off the PACT fleet with hit and run tactics."
    ava "With no risk of civilian casualties on the planet, we could draw the battle out until the rest of our ships arrive."

    show kryska uniform armscrossed frown with dissolve

    kry "With all due respect commander, such a plan involves the risk of the PACT fleet bypassing us all together and warping deeper into populated Alliance space. Alliance Command has ordered us all to keep PACT contained at Far Port at all costs."

    show ava uniform alt neutral mad with dissolve

    ava "PACT won't be able to warp out an armada of that size easily. And facing a PACT fleet that large with our current forces would be suicide."
    kay "... ... ..."
    kay "Looks like we're in quite a bind..."

    play music "Music/Love_Theme.ogg" fadeout 1.5 fadein 1.5
    scene black with dissolve
    scene bg captainsoffice with dissolve
    show ava uniform neutral neutral with dissolve

    kay "Well, here we are. The opening battle of the Alliance-PACT War."
    kay "How're you feeling, Ava?"

    show ava uniform armscrossed neutral with dissolve

    ava "Hopelessly outnumbered and outgunned? Facing a far superior force with minimal back up and no hope of reinforcements arriving on time, all for a naïve schoolboy cause?"

    show ava uniform handonhip forcednarrowsmile with dissolve

    ava "Feels like one of our old summer vacations all over again."
    kay "... ... ..."
    kay "I thought you had forgotten everything about those days."

    show ava uniform handonhip neutral with dissolve

    ava "Not everything."
    kay "Why didn't you ever respond to my messages after you left?"

    show ava uniform armscrossed looklefttalk with dissolve

    ava "I was busy."
    kay "Heh."
    kay "I figured as much."

    show ava uniform neutral neutral with dissolve

    ava "... ... ..."
    ava "I moved on. I went to space and you stayed home. It's not like it could have lasted forever."
    kay "... ... ..."
    kay "Nothing's set in stone unless you let it stay that way."
    "... ... ..."

    show ava uniform altneutral neutral with dissolve

    ava "Captain."
    kay "Yes?"

    show ava uniform armscrossed narroweyefrown with dissolve

    ava "I'm still waiting for you to complete that stack of paperwork on your desk."
    kay "Oh."

    scene black with horizontalwipe
    scene bg lab with horizontalwipe
    show chigara uniform handstogether narroweyessmileblush with dissolve

    chi "... ... ..."

    show claude uniform fingeronlip kittycurious:
        xpos 0.2
    with dissolve

    show claude uniform fingeronlip kittycurious:
        zoom 1
        ease 0.5 xpos 0.3

    cla "Oooohhh..."

    show chigara uniform handsup surprise with dissolve

    chi "E-eh!?"

    show claude uniform altneutral smile with dissolve

    cla "Reviewing your camera footage again?"

    show chigara uniform handonchest sadblush with dissolve

    chi "U-uhn..."

    show claude uniform excited happy with dissolve

    cla "The capt'n shows up at about the 61 minute mark. O-oh, right there!"
    cla "Eh-heh, there's our man!"

    show chigara uniform handonchest smileblush with dissolve

    chi "... ... ..."

    show icari uniform armscrossed lookawayannoyed:
        xpos 0.8
    with dissolve

    ica "Seriously... what are you two doing?"

    show icari uniform handonhip snide with dissolve

    ica "Heh. I don't know what you see in that loser, Chigara. He's just a little schoolboy."
    chi "...The captain's always doing what is best for the crew."

    show chigara uniform handonchest sadblush with dissolve

    chi "But... there's something lonely about him."
    chi "He must miss his home."

    show claude uniform fingerup laugh with dissolve

    cla "Ah... maiden love!"

    show icari uniform bothhandsonhips grin with dissolve

    ica "All right, we've gotta hook you up with a wild night at the Stardust to turn you into a real woman! Some pumping bass and hard drinks should blow that innocence from your head!"

    show chigara uniform handstogether sadopenmouthblush with dissolve

    chi "Stop it..."

    show icari uniform armscrossed smilesidesmile with dissolve

    ica "Heh... You're hopeless."

    show claude uniform excited happy with dissolve

    cla "You better make your move fast, Chigara. Or else I'm gonna snatch him away before you~"

    show chigara uniform fingerstwiddle gloom with dissolve

    chi "Uuu... Sniffle sniffle..."


    stop music fadeout 1.5
    show icari uniform handonhip neutral with dissolve

    ica "Hmm... Changing the subject, what's that spy doing in the recording?"

    show chigara uniform handonchest surprise with dissolve

    chi "Eh? I don't remember ever seeing this part..."
    ica "Wait a minute... Isn't that..."

    scene bg captainsoffice with dissolve

    kay "(Even in a situation like this, Ava's still making me do the paperwork, huh...)"
    kay "(I thought I could get away with it until after the battle...)"
    kay "(She's always just way too uncompromising! One day, I'm going to have to take her to shore leave and show her how to actually relax...)"

    play music "Music/Proditionis.ogg"

    "Icari over Radio" "Captain, we need you in the hangar!"
    kay "Icari? What's the matter?"
    ica "That Alliance mole's been tampering with our systems! You've gotta arrest her!"
    kay "I'll be right down."

    scene bg hangar
    show icari uniform point angry:
        xpos 0.12
    show chigara uniform handonchest surprise:
        xpos 0.37
    show kryska uniform neutral frown:
        xpos 0.62
    show ava uniform handonhip mad:
        xpos 0.87
    with dissolve

    ica "Tsch... I should have known better than to trust you."
    kay "What's going on here!?"
    ica "I caught the spy snooping on the Sunrider's warp core controls. No doubt trying to copy our core schematics into that little data drive she's hiding..."

    show kryska uniform armscrossed frown with dissolve

    kry "An unfortunate misunderstanding, captain. I was merely running a diagnostic on the ship's performance specs so I could formulate our tactical plan for the coming battle."
    kay "Chigara, did you see anything?"

    show chigara uniform twiddlefingers scaredsad with dissolve

    chi "T-the Lieutenant attached some kind of a data copier to the console... I think she was trying to hack into our secure data..."

    show icari uniform bothhandsonhips angry with dissolve

    ica "See? She's a spy!"
    kay "Are you sure, Chigara?"

    show chigara uniform handonchest sad with dissolve

    chi "Yes... I have it all on video... Since I did set up some cameras in engineering and all..."

    menu:
        "Look people, we're all on the same side here.":
            jump peoplesamehere
        "I should have known better than to trust the Alliance. Ava, escort the Lieutenant to the brig.":
            jump bettertrustbrig

label peoplesamehere:

    $ affection_tera += 2

    show icari uniform point angry

    ica "But captain! She's Alliance Black Ops! For all we know, she might slit our throats while we're sleeping! Those people aren't accountable to anyone!"

    show kryska uniform neutral angry with dissolve

    kry "For the record, the Alliance does not have a Black Ops."
    ica "Don't bullshit me! What kind of self respecting military does NOT have a Black Ops!?"
    kay "Calm down Icari. Weren't you the one who was always saying we needed the Alliance on our side if we're going to win this war?"

    show icari uniform armscrossed closedeyesshout with dissolve

    ica "I-I... Arggh!!"

    jump battlefarportstart

label bettertrustbrig:

    show ava uniform salute neutral with dissolve

    ava "Yes captain."

    show kryska uniform altneutral madtalk with dissolve

    kry "The Alliance will hear of this, captain. You're making a mistake."
    kay "I can't have you hacking into our ship's warp core, even if you're with the Alliance. Just whose side are you on, Lieutenant?"
    kry "You need the Alliance's help. You can't fight PACT by yourself."
    kay "Ava, the brig."

    show ava uniform handonhip mad with dissolve

    ava "About time. Come on Lieutenant, this way. We can have a nice chat while you're behind bars."

    jump battlefarportstart

label battlefarportstart:

    play sound "sound/warning.ogg"
    "(Klaxon)"
    kay "What the-"

    show ava uniform altneutral angry with dissolve

    ava "Proximity warning! It's the PACT fleet!"
    kay "Damn! They're here already?"
    kay "We'll deal with this later! Man your stations, people! Move!"

    show ava uniform salute angry with dissolve

    ava "Sir!"

    scene bg bridgered with dissolve
    show ava uniform handonhip mad with dissolve

    ava "The PACT invasion fleet's just warped in. Distance: 10 000 kilometers, and closing in fast."
    kay "Size?"
    ava "Bigger than anything we've seen so far. Roughly 20 battleships and carriers. Over 600 ships in total."
    kay "They out number us nearly 1 to 6, huh..."
    kay "Asaga, are our ryders ready?"

    show asaga plugsuit handsonhips happy:
        xpos 0.25
    with wipeup

    asa "All ready down here, captain! Just give the word!"

    show icari plugsuit armscrossed annoyed:
        xpos 0.75
    with wipeup

    ica "Tsch... I just hope our Lieutenant doesn't stab us in the back out there..."
    kay "We're going to have to deal with that later. For now, I need all the ryders we have."

    hide asaga with dissolve
    show kryska plugsuit altneutral frown:
        xpos 0.19
    with wipeup

    kay "Lieutenant Stares, regardless of what orders you have from your superiors, the Admiral has reassured me you will be under my command during combat operations. I expect you to obey my orders."

    show kryska plugsuit salute angry with dissolve

    kry "Yes sir. I understand."
    ava "We're being hailed by the PACT flagship."
    kay "Put it through."

    hide kryska with dissolve
    hide icari with dissolve
    show cullen:
        xpos 0.82
    with wipeup

    cul "BWAAHHH-HAHAHAHA! This is all you could muster to defend Far Port?"
    cul "This will be far too easy!"
    kay "Veniczar Porkchops. The Alliance has over a thousand more ships on route to Far Port. Now that you've sparked an Alliance intervention, it's all over for PACT."
    cul "Fool! We will crush the Alliance just as we crushed the Neutral Rim! The future belongs to PACT!"
    cul "En garde, captain! For my mighty fleet will be the last sight you see before you are slaughtered like animals!"

    hide cullen with wipedown

    kay "Ava, show me the situation on the screen."

    show ava uniform handonhip mad:
        zoom 1
        ease 0.5 xpos 0.8

    show cg_farport 1:
        xpos 0.1 ypos 0.2
    with dissolve

    ava "Aye sir. We are currently holding position here."

    show cg_farport 2 with dissolve

    ava "Five PACT fleets approach our position."

    show cg_farport 3 with dissolve

    ava "Fleets one and two are composed of fast frigates and destroyers. They intend to circle ahead of the main enemy fleet and flank us from the sides."

    show cg_farport 4 with dissolve

    ava "Fleets three and four are composed of slower cruisers. They are approaching from the rear. While they present a considerable threat, they have warped out too far behind the battle lines. ETA until they are in range: 4 hours."

    show cg_farport 5 with dissolve

    ava "Finally, fleet five is the enemy's command group. Comprised of battleships and carriers, this will be the enemy's backbone."
    kay "What about the Legion?"
    ava "It is holding position 800 000 kilometers away. It appears to be merely observing the battle."
    ava "Cullen has employed a fully offensive fleet position. The two light fleets will effectively flank us from the sides, while the command fleet delivers the killing blow. The two cruiser fleets will provide reinforcements and engage in mop up operations."

    show ava uniform alt neutral mad with dissolve

    ava "Shall I give the order to the Second Fleet to scatter and begin hit and run operations?"
    kay "... ... ..."
    kay "No."

    show ava uniform armscrossed frowntalk with dissolve

    ava "Captain?"
    kay "Cullen's only fought weakly defended Neutral Rim worlds and the remnants of the New Empire during the PACT Revolution. He's overconfident and underestimates us."

    show ava uniform handonhip mad with dissolve

    ava "What are your orders?"
    kay "We charge forward."
    kay "Cullen's never dealt with an enemy who took the offensive. Cullen may know how to overwhelm defensive positions, but he doesn't know a thing about stopping an enemy attack."
    kay "By keeping his force split into five groups and committing all five to the offensive, Cullen rendered his command fleet defenseless."

    show cg_farport 6 with dissolve

    kay "We'll charge toward the command fleet on full thrusters and make fleets 1 and 2 overshoot us. They'll need to circle around again before they can reach us."

    show cg_farport 7 with dissolve

    kay "While the flanking fleets are busy circling around, we'll commit all our ships to taking down fleet five before the cruisers in the rear get here. The Alliance's smaller vessels will engage the battleships and carriers at knife fight range and sink them before Cullen can react."

    show ava uniform armscrossed frown with dissolve

    ava "Even with the command fleet gone, the remaining PACT fleet will still be formidable."
    kay "Our mission objective isn't the protection of Far Port, but the defense of the deeper inhabited Alliance worlds."
    kay "With all of their command ships destroyed, the remaining PACT vessels will have no means to continue beyond us for a coordinated invasion of the Alliance worlds."
    kay "Once their command vessels are sunk, the PACT fleet will be disorganized and will have no choice but to retreat."

    show ava uniform handonhip neutral with dissolve

    ava "A daring plan, captain. But what about the Legion?"
    kay "Let's just hope that it's only here to watch the party. They won't commit the Legion to the battle if Arcadius is on board. He's too important to risk taking into battle."
    ava "Then let's hope that he's there watching."

    play music "Music/DayDream_Cut.ogg" fadeout 1.5

    kay "Put me through to all our ships."

    show ava uniform alt neutral neutral with dissolve

    ava "Done."

    scene cg_farport_charge1:
        xpos 0.0 subpixel True
        ease 15.0 xpos -0.27
    with dissolve

    pause 5.0

    kay "All ships, this is Captain Shields speaking."
    kay "The enemy is at your gate. The Alliance now fights a war for its very survival."

    show chigara plugsuit excited blushdetermined:
        xpos 0.2 alpha 0
        ease 0.5 alpha 1.0
        pause 0.5
        ease 0.5 alpha 0

    chi "(Captain... Do your best!)"
    kay "The task before us is great. We stand guard of billions of innocent lives beyond Far Port."
    kay "And yet the enemy outnumbers, outguns, and outpowers us one to six."
    kay "I have seen with my own eyes what PACT does to civilians. For those who we left behind, steel yourself for the coming fire!"

    scene cg_farport_charge2:
        xpos 0.0 subpixel True
        ease 15.0 xpos -0.27
    with dissolve

    show arcadius altneutral:
        xpos 0.8
        ease 1.5 alpha 1.0
        pause 0.5
        ease 1.5 alpha 0

    arc "For as long as recorded time, we have suffered at the hands of the Imperialists."
    arc "After many years of bloody revolution, we have at last arrived at the enemy's gates..."
    arc "Tell me, my comrades, shall we let these capitalists live?"
    arc "Those that would let starve billions of children throughout the galaxy merely because there is no profit to be had?"
    arc "Those who would oppress the common people, all to maintain their decaying grip upon their empires?"
    arc "Let it be heard!"
    arc "Death to the aging men in their gleaming ivory towers! Death to the kings in their decadent throne rooms!"
    arc "All hail the revolution!"

    scene cg_farport_charge1:
        xpos -0.27
    with dissolve

    kay "In the face of such odds, we will not scatter, but instead charge forward to meet the enemy head on!"

    show asaga plugsuit handsonhips determined:
        xpos 0.2 alpha 0
        ease 0.5 alpha 1.0
        pause 0.5
        ease 0.5 alpha 0

    asa "(I'm... going to protect everyone...!)"
    kay "The enemy may have strength in numbers, but their numbers are meaningless when we outnumber them one hundred to one in mettle!"
    kay "For the defense of the inner worlds, we will march forward! Let the crimson fleet learn today the might of the free men of the Alliance!"
    kay "All units... FORWARD!!"

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    $ renpy.pause(2)

    window hide
    hide cg_farport_charge1

    $ check1 = False
    $ check2 = False
    $ check3 = False

    $ alliancecruiser_weapons = [AllianceCruiserLaser(),AllianceCruiserMissile(),AllianceCruiserKinetic(),AllianceCruiserAssault()]
    $ alliancecruiser1 = create_ship(AllianceCruiser(),(5,5),alliancecruiser_weapons)
    $ alliancecruiser2 = create_ship(AllianceCruiser(),(5,4),alliancecruiser_weapons)

    $ BM.orders['SHORT RANGE WARP'] = [750,'short_range_warp']

    call mission12_inits
    $ BM.mission = 12
    jump battle_start

label mission12:

    $BM.battle_bg = "Background/space6.jpg"

    if check3 == False:

        $ BM.draggable = False

        "Tip 1: Use the Short Range Warp order to instantly relocate the Sunrider to another location."
        "Tip 2: PACT Carriers will continually launch enemy ryders until destroyed."

        $ check3 = True
        $ BM.draggable = True

    if check1 == False and BM.turn_count == 3:

        $BM.draggable = False

        show ava uniform handonhip mad onlayer screens:
            xpos 0.8
        with dissolve

        ava "We're being flanked to the sides by the frigates!"

        hide ava uniform handonhip mad onlayer screens with dissolve

        python:
            create_ship(MissileFrigate(),(6,2),[PactFrigateMissile()])
            create_ship(MissileFrigate(),(7,2),[PactFrigateMissile()])
            create_ship(MissileFrigate(),(8,2),[PactFrigateMissile()])
            create_ship(MissileFrigate(),(9,2),[PactFrigateMissile()])

            create_ship(MissileFrigate(),(6,16),[PactFrigateMissile()])
            create_ship(MissileFrigate(),(7,16),[PactFrigateMissile()])
            create_ship(MissileFrigate(),(8,16),[PactFrigateMissile()])

        $ BM.draggable = True
        $ check1 = True

    if check2 == False and BM.turn_count == 6:

        $BM.draggable = False

        show ava uniform handonhip mad onlayer screens:
            xpos 0.8
        with dissolve

        ava "The enemy cruisers are now in weapons range!"

        hide ava uniform handonhip mad onlayer screens with dissolve

        python:
            create_ship(PactCruiser(),(17,9),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(17,10),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(17,11),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(17,12),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])

        $ BM.draggable = True
        $ check2 = True

    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission12 #loop back
    else:
        pass #continue down to the next label

label aftermission12:

    hide screen commands
    hide screen battle_screen

    play music "Music/Riding_With_the_Wind.ogg" fadeout 1.5

    scene bg legionwindows with dissolve
    show fontana:
        xpos 0.3
    with dissolve
    show arcadius altneutral:
        xpos 0.7
    with dissolve

    window show

    fon "My leader. The enemy fleet has ambushed Cullen's command group."
    arc "The fool. We long suspected his incompetence."
    fon "Shall we assist?"
    arc "Yes Fontana. Prepare to fire the Legion's main cannon."
    fon "But sir... At this distance, there is a risk that we would hit our own ships as well."
    arc "That is irrelevant. Destroy them all."
    fon "Understood, my Veniczar."

    scene bg bridgered with dissolve
    show ava uniform altneutral angry with dissolve

    ava "Warning! The cruiser fleets have reached weapons range! We're taking heavy fire!"
    kay "What's the status of the enemy command fleet?"
    ava "We've taken down most of the command ships, but Cullen's flagship still remains!"

    show ava uniform neutral surpriseangry with dissolve

    ava "W-wait... Energy spike detected! It's the Legion!"
    kay "Order the fleet to take evasive maneuvers!"

    scene cg_legion_farport_fire1:
        xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 zoom 0.8
    with dissolve
    pause 1.0
    play sound "sound/legion_maincannon.ogg"
    pause 0.5
    scene cg_legion_farport_fire2:
        xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 zoom 0.8
    with dissolve
    pause 1.4
    scene cg_legion_farport_fire3:
        xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 zoom 0.8
    with horizontalwipereversefast
    pause 2.0

    scene cg_alliancefleet_farport1 with dissolve

    play sound5 "sound/legion_maincannon_fire.ogg"

    pause 0.5
    scene cg_alliancefleet_farport2 with horizontalwipereversefast
    play sound "sound/explosion4.ogg"

    scene cg_alliancefleet_farport3 at shake1(repeats=8) with dissolvemedium

    play sound1 "sound/explosion2.ogg"

    scene cg_alliancefleet_farport4 at shake1(repeats=8) with dissolvemedium

    play sound2 "sound/explosion1.ogg"

    scene cg_alliancefleet_farport5 at shake1(repeats=8) with dissolvemedium

    play sound3 "sound/explosion1.ogg"

    scene cg_alliancefleet_farport6 at shake1(repeats=8) with dissolvemedium

    play sound4 "sound/explosion2.ogg"

    scene cg_alliancefleet_farport7 at shake1(repeats=8) with dissolvemedium

    pause 2.0

    scene bg bridgered with dissolve
    show ava uniform altneutral surpriseshout with dissolve

    ava "The Hiakili squad has been annihilated! Taylor Squad is down to three cruisers!"
    ava "Two of PACT's own vessels were caught in the blast and vaporized as well!"
    kay "Arcadius... you insane son of a bitch..."
    kay "Merge squad Taylor with squad Arturia! Move our ships closer to the PACT vessels!"

    show ava uniform salute angry with dissolve

    ava "Sir!"
    kay "Don't let the Legion take any more of our ships without taking twice as many of its own down with it!"

    scene cg_porkdeath1 with dissolve

    cul "Hah! This battle is still far from over, captain!"
    cul "Prepare to fire the quantum torpedo! Target the Sunrider!"

    scene cg_blackjack_farport1
    show cg_blackjack_farport2:
        xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
    with dissolve

    asa "As if I'll let you!"

    play sound "sound/mech1.ogg"
    show cg_blackjack_farport2:
        ease 0.5 xpos 0.42 ypos 0.54  zoom 0.5

    pause 0.5

    scene cg_blackjack_farport3 with dissolve

    cul "Heh! What do you expect to do with those tiny lasers, girl?"

    play sound "sound/chargeup.ogg"
    scene cg_blackjack_farport4 with dissolve

    asa "EAAHHH!!!"

    scene cg_blackjack_farport5 with dissolve

    chi "The Black Jack has undone its safety limiters! Asaga---!"

    scene cg_blackjack_farport6 with dissolve
    show asaga plugsuit neutral angry:
        xpos 0.5 zoom 1.7 ypos 1.5
    with dissolve

    asa "Don't..."

    asa "Mess..."

    play sound1 "sound/heartbeat.ogg"
    show asagaplugsuitneutralangry:
        xpos 0.5 zoom 1.7 ypos 1.5
        ease 0.3 xpos 0.5 zoom 4.0 ypos 3.0 alpha 0
    show asaga plugsuit neutral awakenangry:
        ease 0.1 xpos 0.5 zoom 2.0 ypos 1.7
    with dissolve
    asa "WITH ME!!!!"

    scene cg_porkdeath1 with dissolve

    cul "W-what!?"

    play sound "sound/vanguard cannon laser.ogg"
    show cg_blackjack_farportlaser:
        xanchor 0.0 yanchor 0.5 xpos -0.4 ypos -0.3 xzoom 1.5 yzoom 0.5
        rotate -40
    with dissolve

    asa "EAAAAHHHHH!!!!!"

    cul "I-Impossible.......!!!!"

    show cg_blackjack_farportlaser:
        ease 0.5 rotate -30 ypos 0.0

    asa "This... is for Ryuvia!"

    show cg_blackjack_farportlaser:
        ease 0.5 rotate -20 ypos 0.3

    show cullen:
        xpos 0.8
        block:
            ease 0.1 xpos 0.82
            ease 0.1 xpos 0.78
            repeat 8
    with dissolve
    cul "No...! No!!! I--"

    show cg_blackjack_farportlaser:
        ease 0.5 rotate -10 ypos 0.6

    pause 0.5
    play sound "sound/explosion5.ogg"
    scene white with dissolve

    cul "BWWWAAAAAAAHHHHHHHHHHHHHHHHHH!!!!!!!!!!!!!!"

    scene cg_porkdeath2 with dissolve
    scene cg_porkdeath3 with dissolvelong
    pause 1.0

    scene bg bridgered with dissolve
    show ava uniform fistup yes with dissolve

    ava "Confirmed hit! The enemy fleet's flagship has been sunk!"
    kay "Yes!"

    play sound "sound/explosion1.ogg"
    show layer master at shake1(repeats=8)
    show ava uniform altneutral angry with dissolve

    ava "U-ugh!"
    ava "The enemy attack is still continuing! Our fleet is down to 33 percent!"
    ava "We won't be able to survive much more of this!"
    kay "Order the fleet to scatter! Our objectives are complete!"

    show ava uniform salute angry with dissolve

    ava "Aye captain!"

    play music "Music/Bladed_Druid_Cut.ogg" fadeout 1.5
    scene cg_phoenixpaladin with dissolve

    kry "I'll down you all!"
    ica "Tsch..."
    ica "Didn't think that I'd ever end up like this..."
    ica "Fightin' some stupid war alongside the likes of you!"
    kry "Wait...! Look!"

    scene cg_emeraldfleet_warpinback with dissolve
    show cg_emeraldfleet_warpin1:
        zoom 0.1
        ease 0.5 zoom 1.0
    pause 0.5
    play sound1 "sound/large_warpout.ogg"

    ava "Captain!!!"
    ava "It's the Alliance fleet!"
    gre "I commend you for holding out this long, captain."
    gre "Now, behold the power of the Emerald Fleet!"

    play sound1 "sound/large_warpout.ogg"
    show cg_emeraldfleet_warpin2 behind cg_emeraldfleet_warpin1:
        zoom 0.1
        ease 0.5 zoom 1.0

    pause 0.25

    play sound2 "sound/large_warpout.ogg"
    show cg_emeraldfleet_warpin3 behind cg_emeraldfleet_warpin2:
        zoom 0.1
        ease 0.5 zoom 1.0

    pause 0.1

    play sound3 "sound/large_warpout.ogg"
    show cg_emeraldfleet_warpin4 behind cg_emeraldfleet_warpin3:
        zoom 0.1
        ease 0.5 zoom 1.0

    pause 0.1

    play sound4 "sound/large_warpout.ogg"
    show cg_emeraldfleet_warpin5 behind cg_emeraldfleet_warpin4:
        zoom 0.1
        ease 0.5 zoom 1.0

    pause 0.1

    play sound5 "sound/large_warpout.ogg"
    show cg_emeraldfleet_warpin6 behind cg_emeraldfleet_warpin5:
        zoom 0.1
        ease 0.5 zoom 1.0

    gre "All ships! Open fire!"
    gre "Show these reds what happens when you cross the Alliance!"

    scene bg legionwindows with dissolve
    show fontana:
        xpos 0.3
    with dissolve
    show arcadius altneutral:
        xpos 0.7
    with dissolve

    fon "My Veniczar. Cullen has been dispatched. Our ships are in disarray."
    fon "The First Fleet has arrived with 200 fresh ships. Our spies indicate that more Alliance reinforcements are on route."
    fon "Shall I commit the Legion to the battle?"
    arc "... ... ..."

    show arcadius neutral with dissolve

    arc "No."
    arc "The battle no longer favors us. Order our forces to fall back."
    fon "Understood my leader."

    hide fontana with dissolve
    show arcadius altneutral with dissolve
    show arcadius:
        ease 0.5 xpos 0.5

    arc "... ... ..."
    arc "This loss is irrelevant."

    show arcadius fist with dissolve

    arc "Soon... the galaxy will witness the true power of what we accomplished at Diode... And tremble!"

    show arcadius laugh with dissolve

    arc "Hahahahahaha!!!"

    scene black with dissolve
    play music "Music/Firn.ogg" fadeout 3.0
    scene bg hangar with dissolvelong

    show asaga plugsuit vpose with dissolve

    asa "Hahaaa!!! We did it capt'n!"

    show chigara plugsuit handonchest smile:
        xpos 0.38
    with dissolve

    chi "Captain, I'm back!"

    show sola plugsuit altneutral neutral:
        xpos 0.91
    with dissolve

    sol "Mission successful."

    show ava uniform facepalm:
        xpos 0.65
    with dissolve

    ava "Seriously..."

    show ava uniform armscrossed smile with dissolve

    ava "This was only the first battle of the war. It's too soon to celebrate yet."
    kay "Kind of hard to take that seriously when you're grinning ear to ear, eh, Ava?"

    show ava uniform neutral surprise with dissolve

    ava "W-wha...?"
    ava "I'm not--!"

    hide asaga with dissolve
    hide chigara with dissolve
    hide ava with dissolve

    show icari plugsuit handonhip annoyedtalk:
        xpos 0.35
    with dissolve

    ica "Hmph..."

    show kryska plugsuit altneutral happy:
        xpos 0.65
    with dissolve

    kry "It was my pleasure to fight alongside you, Ms. Isidolde. We make quite a team."

    show icari plugsuit armscrossed tsun with dissolve

    ica "Well, I guess you're not that bad of a shot! Just call me Icari from now, alright? I don't like ranks or titles in front of my name."
    kry "Of course."
    kay "Well, it looks like you two are getting along for a change."

    show kryska plugsuit salute angry with dissolve

    kry "Captain."

    show kryska plugsuit altneutral frown with dissolve

    kry "I apologize for my actions, sir. I expect to be escorted by Commander Crescentia to the brig now that the crisis has passed."
    kay "About that..."
    kay "Here's the data you were trying to access."
    kay "We're going to be a team from now on, so we're going to have to learn to trust each other. The next time you need information, why don't you just ask?"

    show kryska plugsuit neutral question with dissolve

    kry "Sir?"
    kay "If we're going to get anything done, it's going to be done together."

    show kryska plugsuit salute smile with dissolve

    kry "Understood sir. I will inform you personally if my superiors wish information in the future."

    show icari plugsuit handonhip tsuntalkblush with dissolve

    ica "Hmph. Well, this doesn't mean that we'll be friends or anything! But I guess we can work together. Just for now!"

    show claude plugsuit fingeronlip kittysmile:
        xpos 0.79
    with dissolve

    cla "Ufufu... It looks like a certain someone's blushing..."

    show icari plugsuit armscrossed blushtsun with dissolve

    ica "S-shut up! This is only so we can beat PACT!"

    show claude plugsuit fingerup laugh with dissolve

    cla "My, my! Isn't this ship turning into a little love nest! Ufufufu..."

    show icari plugsuit armscrossed shoutblush with dissolve

    ica "SHUT UP!!! EAAHH!!!"

    show asaga plugsuit excited happy:
        xpos 0.09
    with dissolve
    show chigara plugsuit handonchest smile:
        xpos 0.25
    with dissolve

    kay "... ... ..."

    show ava uniform neutral neutral:
        xpos 0.5
    with dissolve

    ava "Captain?"
    kay "Hard to believe this was just an empty hangar when we first left Cera."
    ava "You said you'd gather allies from across the galaxy."
    kay "Yeah. I did."

    show  ava uniform handonhip forcednarrowsmile with dissolve

    ava "Well done, captain. Well done."
    ava "... ... ..."

    scene black with dissolve

    ava "...But I still await the completion of your paperwork."

    window hide

label credits:

     ###############################################################PLACE HOLDER

    scene bg black2 with dissolvelong

    show credits1:
        xalign 0.5
        yalign 0.5
    with dissolve
    $ renpy.pause(2.0)

    hide credits1 with dissolve

    show credits2:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits3:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits4:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits5:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits6:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits7:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits8:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits9:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits10:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits11:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits12:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits13:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits14:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits15:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits16:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits16b:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits16c:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits16d:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits16e:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits16f:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits17:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits18:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits19:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits20:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits21:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits22:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits23:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits24:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    pause 3.0
    show credits25:
        xalign 0.5
        ypos 1.1
        linear 6.666666666666667 ypos 0.5
    pause 15.0
    hide credits25 with dissolve

    scene bg black2

    $ renpy.pause(0.1)

    show credits26:
        xalign 0.5 ypos 0.2

    pause 4.0
    hide credits26 with dissolve

    window hide

    cre "SYMBOL TO A:{p}Kyubey, ~ren, Kirino is love, AAAYogibearAAA, Aaron, Aaron Holding, Aaron Kaluszka, Aaron Kettle, Aaron Matthews, Aaron Taylor, Abe, AbeFM, Accelsharp, accRei, AceMcKillYoFace, Adam Little, Adam Pitt, Adam Raines, Adrian A. Gallegos, Adrian Bergström, Adrian Ferrer (Sixten), Adriano Gagliardi, Agent Francis York Morgan, but please, just call me York, Agus Hartono, Ágúst Sigurjónsson, AJ Nordstrom, akaPassion, Akures, Albert \"Warrax\" Aloma, Alberto Garcia, Alec Tomlins, Alemina Bismarck, Alex \"Xelada\" Hargreaves, Alex Aranovsky, Alex Churchill, Alex Donks, Alex Edwards, Alex Worthington, Alexa Vitovsky, Alexander  Gene Schulz & Ken Kim Schulz &  Melissa Lynn Schulz, Alexander Frey, Alexander John Aristotle Kimball, Alexander Kent, Alexander Liebau, Alexander Petrovic, Alexander W. Knowlton, Alexandre \"nah\" Bailly, Alexei \"Roflcopter\" Short, Alexis Perron, Allen J Medlen, Allen Kwan, AlliedG, Almost Human, Alto, Amber Hein, Ampereox Irfan, Anaël Verrier, Anderan, Anders Kronquist, Anders Schack Østergaard, Andre Bellarin, Andrea Martinelli, Andreas Gyllblad, Andrew Bethesda, Andrew Biernacki, Andrew Hovanec, Andrew Juljenjai, Andrew Nelson aka SomePoorSap, Andrew P. Bullen, Andrew Paul Maggio III, Andrew Simpson, Andrew Wilson, Angelo \"Brooklyn Finest\" Lima Representing Brazil In Da House, Angelus Luminous, Anna Lee, Anne Nonymous, anonymous, Anonymous, Anonymous, anonymous, Ansel Wong, Anthony Ambrassi, Anthony DeBartolo, Anthony Kinnear, Anthony Luu, Anthony R. Evans, Anton Gorbunov, Anton Guryanov, Arcbleast, ArcherRush, ArchSenex, Arild Iversen aka. Foamed, Arjuna Chatrathi, Arkent Golt, Arkheos Angelos, Armando A. Rosado, Arnel De Leon, ARoastedPenguin, ARPerson, Arthur Lee, Ashadow700, Atomsk, Augusto Andrade, Austin \"Yamato\" F., Avery Heart, Axel Miszczak, Axel Terizaki, Aymeric Hedin"
    cre "B:{p}Baldarhion, Bastiaan Rours, Beardsly, Ben, Ben \"OathAlliance\" Corum, Ben Bonds, Ben Hockley, Ben M, Ben Parsons, Ben Tiberius, Ben Waxman PA-C, BenEng91, Benjamin \"violink4swords\" Randall, Benjamin John Whittingham, Benji Bent, Bewoulve, bhakabane, Biiku Ryugaku, Billpete002, Bingo, Bjorn Vrancken, Bkarsi, Blaine Kawakami, Blake Cross, Blake Domeyer, B-Lo.Co, Bob Sintas, Bobby Skeens, Born2Love, Brad Dunlap, Brandon \"Gnome\" Davis, Brandon \"Zonz\" Chambers, Brandon Coleman, Brandon Nguyen, Bren Rowe, Brett \"DJ Archangel\" Strassner, Brett Martinez, Brett Pearson (J.C. Quiinn), Brian Henderson, Brian L, Brian L., Brian Santos, Brian Simms, Brian Townsend, Brittni Ballard, Brody Miron, Brozita #420BLAZEIT ( ͡° ͜ʖ ͡°), Bruce Novakowski, Bruno \"The Draconic Lord\" Santos, Bruno Marques, Bryan Elliott, Bryan Lyon, Bryan Massengale, Bryan Middlebrook, Bryan Russowsky, BtBurns, Budi Winarto, bugrom.san, Bulens Simon, Burstroc, Buwaro Elexion"
    cre "C:{p}C Weber, Caidran, Cail Synnacht, Caitlin Eckert, Cally, Calvin C., Cameron Sekulin, Canberk Koparal, Captain John M. Smith, Captain Max Zero, Carey Stanley, Carlos Bruno Alves, Carlton Solle, Casey C. Knowlton-Key, Cassie Halladay, Ceci Kiyomizu, Chaadon Peterson, Chankit Pongdhana AKA xredsoulz, Chaos, Charlie Tomlinson, Chase Earhart, Chase L., Chau Hoang, Chayadol, Choum, Chris Bates, Chris Fox, Chris G., Chris Headley, Chris McCleese, Chris Mear, Chris Renard, Chris Stewart, Chris Taran, Chris W, Chris Willard, Christian Dobson, Christian Skomorowski, Christian Waterhouse, Christian Witte, Christop, Christoph Kamper, Christopher \"Rigrot\" Wood, Christopher C. Cockrell, Christopher C. Hoitash, Christopher Gebhart, Christopher J. Epure, Christopher Liang, Christopher Roberts, Christopher Rubio, Christopher S Martin, Christopher Soon, Christopher Toy, Christopher Zhong, Chua Chong Yi, Cirvaazny, CLAUDE IS BEST GIRL, Clay Smith, Cody Hedgecock, Cody Spence, Colin Kennat, Connor Greeley (Shadowwolf9711), Coresplinter, Count Buggula, Craig Butler, Craig James Kelly (dynamo), Craig S. Weinstein, Craken, Cristobal Mera Collantes, Crucian, cupcakemann95, Cybolt, Cyen, cymricchen, Cyprien Randon (MisterTokijin)"
    cre "D:{p}Damien Pearson, Damien Terrasson, Damon Eric English, Dan \"J0nd03\" Beasley, Dan Svoboda, Dan Vince, Dan Whitmore, Daniel B, Daniel Drimus, Daniel Emmons, Daniel Guyton, Daniel Hull, Daniel Lin, Daniel Root \"Red Alchemy\", Daniel Widegren, Daniele Canciani (aka croma25td), Danny Lwin, Dargon, Dark09, Darkeva, Darkron008, Darksor, Darn, Darth Crater, dave55man, David, David \"Socratics101\" Chang, David Beauchamp, David C Werling, David Carreiro-Ricard, David Dalton, David Emanuel, David Francis, David H. Lee, David Ing, David John Pack, David Long (Neko), David McFadden, David Michael Finzi, David 'Milky' Barry, David Pieper, David Shireman, David Telles, David Tran, Dawfydd Kelly, Dawn_, deadering, Dean Kelly, Dean Reeder, Delbert Thompson, Denali Leland, Derek \"Pineapple Steak\" Swoyer, Derek \"Sokolov\" Chin, Derrick Lam, Derrick Pilgrim Jr, Desmond Sutcliffe, \"Devon \"Tag\" Courtney, DickJutsu.com, Dimitri Pivnicki, Dinko Serifovic, diragjie, Disoriented Effigy, DKDevil, D-Man, Dmitry Tretyakov, Do not include, Doctor Duckie - KY, DOKIE & KATHIE, Dominic \"RocK_M\" Ferrer, Dominic Christen, Don Hanson II, Don, Beth, & Meghan Ferris, dorlingo, Doug Grimes, Douglas Sloan, Drake Navarone, Drew Schultz, D-Rock, Duatha, Duncan, Duncan Jones, Dustin Roop, Dylan"
    cre "E:{p}Ebertb, eclipsednight, Ed130 The Vanguard, Eddie Akers, Eden Code, Edgar Martinez, Edward Benavides, Edward Gibbens, Edward Truong, Einjeru (Steven Rodriguez), Ektorus, Elari Tammenurm, Eli Mack, Eltrum, Elvis Henry Strunk, Endang Srie Redjeki, Enerccio, Ensign Enkrow, Erendil, Eric, Eric Lenoir, Eric Moeller, Eric T. Boyce, Eric Wei, Eric Zylstra, Erich Lah, Erik Proskin, Ernest Ivnik, Ernesto Ayala Jr, ErrBerry, Erwan Hellouin, Escelar, Ethan \"SteelAngel\" Deneault, Ethan Leyva, EuphoricField~Vesalious"
    cre "F:{p}Fabián M. Rebolledo, faeriehunter, Fakhrul Anwar, Falkmir, Falwin, Fang-Kai Hsieh, Fearfireg, Feenie, Felipe Augusto Batista, Felix Grothkopp, Felix Stelzer, fenixDG, Ferdinand Schober, Fimb ul Kron, finmarchicus, FiShiYun, fk000007, Flintspatula, Florian Sebesta, FoMothaRussia, Fractured, Francisco Garcia, Franklin Hamilton, Freddy \"KaKuna\" Hansson, Frédéric Magnin, Frederik Vezina, Frozen Friend (CD), Fury of the Tempest"
    cre "G:{p}Gabriel \"Gabe Khronos\" Godoy, Gabriel Silvas, Gareth Saxby, Garrett Muggy, Gary Gould (Lazzarus), Gary Howard, gekiganwing, Gentro, George Henry Shaft, Giacomo Russo, Giantenemycrab, Gideon K, Gilorm, Gilshim, Giovanni \"Allen92\" Cambi, Gnostic, Godewijn W. Perizonius, GoldenCrater, Goldenkitten, Gordon Wearing-Smith, Gotchabagoose, Grant Edwards, Grant Fraser, Greem, Gregory Doge Straight, Gregory Jehan Michel Claude Jacob Gallet, Gregory McCausland, Gregory Polander, Gregory W. Marlin, Groshonee, Grzegorz 'ggamer2' Kucharski, Gunnar Högberg, Gurney"
    cre "H:{p}H1r1n, Halasimov, Haldrin Loregrant, Hanh Van Tang, Harminder Gill, hellgod, Henrik Augustsson, Henry Tran, Hermann B, Hermit, Hessi, Hickname, Hidsnake, Hisakatana, hiyoko556, Honfei \"zisback\" Li, Hugo Crampon, Humberto Meireles (StarChuck), Hung Fuen Mak, Hunter- Captain Obvious the Fantastic, Hunter Goins, Hunterwolf1001"
    cre "I:{p}Ian, Ian \"ThaWulf\" Wolfe, Ian Cox, Ian Whitehead, Imban, Interitus, Isylia Vinland, Ivan \"DesuEagle\" Orlov, Ivan C, Ivan Garcia, Ivannorr, Ivron, Iwan C. A. Smith, Izkda"
    cre "J:{p}J. Andrew Hartman, J. Calkins, J. Hayden Pretzman, J. Quincy Sperber, J.J. Lee, Jack Gibbs, Jacob Hull, Jacob Searcy, Jacques Alexander Katzoff, Jaime Navarro Weber, Jamal L. McWillis, James \"Troll\" LeRoy, James Alexander Henley, James Connors, James H., James Kahalewai, James Lange, James Lofshult (Solav), James O'Bannon Tiffany, James Pineda, James Ross, James Sellman, James Talerico, James Taylor, James Virts, Jamie Manley, Jan Paulsson, Jan-Ole Hübner, Jan-Pierre Jaspers, JapaneseSandman, Jared Goodwater, Jared Rex, Jarosław Knaś, Jarred Nation, Jason, Jason Chou, Jason King, Jason M, Jason Paas, Jason Silva, jason wysocki, Jay Myers III, Jaydon Cannella, Jay-Yun Wang, JD, Jean-Louis Lanteigne, Jeff Coelho, Jeff Hunt, Jeff Netzke, Jeff S., Jeff Schmidt, Jeffery Lawler, Jeremy Duboscq, Jeremy James, Jesse Korhonen, Jesse O., Jezariael Demos, J-F \"Jim le Mime\" C., jghibiki, Jim Chen, Jim Rutkowski, Jim W., Jinx, joachim_kamikaze, João Carrera, Joe, Joe \"Joey\" Saint, Joe Egan, Joe Gilligan(Kingz), Joel Engel (Lightmare), Joey Colli, Johan De Witte, John \"Magnificent Beard\" Schmidt, John \"starfuryzeta\" Mathews, John Anderson, John BlueFreakQ McHugh, John Bremseth, John Christian \"Chriss\" Mæland, John Doyle, John Enright, John GT, John P. Doran, John R. \"Wattsman\" Watson, John Speigel III, John Woodgate, John, Mark, and Ron Aspuria, Johnathan \"MechaVsKaiju.com\" Wright, Jon (WEKM) Krupp, Jonas Bronée, Jonas Westerberg (Nody), Jonathan \"PrimeBacon\", Jonathan Chiu, Jonathan Grimm, Jonathan Shaham, Jonathan Souza, Jonathon \"Pamphy\" Pamphilon, Joonas Parviainen, Jordan Cunningham, Jordan Jeske, Jordan Radomi, Jordane \"Tamajyga\" Lemasson, Jose Angel \"Space Warrior\" Lara, Jose Ramón Vega, Jose Tenorio, Joseph \"Quorum\" Magnotti, Joseph Fong, Joseph Ng, Joseph Perez, Josh Griffiths, Josh Medin, Joshi120, Joshua Cubstead, Joshua Gammon, Joshua James Kern, Joshua Matthew Ruiz, Joshua Peng, Joshua Scott, Jozern, Juan Diego \"Goose\" Ramirez, Juan Peredo, Juancarlos Reyes, Juanjo Barrio, Judy McConnell, Juha \"Baric\" Laaksonen, Juho Juopperi, Julien LAMANT, Justin Horn, Justin Moor, Justin Porcelo, JY, jyuichi, JZL"
    cre "K:{p}K. Mason, k8207dz, Kaelyn Takata, kahadin, Kai Hellmeier, Kaisar69, Karan N. Patel, Karbunos, Karl K, Karl Lassen, Kasper Bergh, Kasper Gammelgaard Hansen, Katherine Williams, Kedo Ciepse, Keeper O Books, Keith Minton, Kelley J., Kelvin, Kenichi Morita, Kenneth Riebe, Keresian, Kestrel150, Kevin, Kevin \"Alythe\" Chow, Kevin Moreno, Kevin Mueller, Kevin S Robertson, Kevin Webb, Kierian O'Hare \^-^/, Kim Tae Woo, Kinoru07, Kirk R. Jensen, Kjetil \"Fyko\" Engvold, KlaisStardust, Kody Tschorn AKA Mr5cap, KogX, Konstantin Koptev, Konsulus, Kory Holtz, Kožec, Kray, Krinku, Kris Hjortshøj Nielsen, Kristiana Moretti, Kronophage, Krunjey, Kurik Lein, Kuritár Tamás György, Kuro \"Drill Battleship\" Gane, Kurt J Klemm, Kurt Montgomery, Kurt Staiger, Kyle Greene, Kyler Markowski"
    cre "L:{p}Laestril, Lamhirh, Lancelot H., Larissa Reynolds Loves Her Husband Levi, Lars Mattsson, Lars Nygaard Witter, Lassi Heliö, Laure Jansen, Laurence Stratton, Laurent \"Lapov\" Patillon, Laurent Trentaz Vite, Le Di Chang, Ledabot, Lee Barnes, Lee Zary, Leno Nunes, Lenworb, Leon Byford, Leon Yong L.O, Leônidas \"+300\" Soares Pereira, Levi McConnell, Lex, Liam Do, Lib, LibraSweets, Lightning Strike, Lim Ye Ping, Linda Barming, LMekko, Loc Le, Logan Lybbert, Long Nghiem, Long Ngoc Nguyen, Lord Eric of Belleau Wood, Lubrioz, Lucas Aquino de Assis-Trysson12, Lucas McMillan, Lucas Watson, Lukasz Gibel, Luke Michel, Luther McBlain"
    cre "M:{p}M Allan, M D Snider, M J V Kwan, M. Lara, Maciej Bojarski, Mackenzie Buckle, Mady vand, Maecolis, Magnvs, Malte M. Breckwoldt, Manje Jung, Manuel Acosta, Marc \"Markie\" Bondoc, Marc Agne, \"Marc David Karsai (BITE ME UNIVERSE) NEKO NEKO NYAN!, Marc Reid, Marcel Matz, Marco \"Dralel\", Marco \"xizro345\" Beltrame, Marcus A. Nichols, Marcus Soll, Marijn Hubert, Marius Kaufmann, Mark \"NeoWolf\" Howe, Mark \"Sparkles\" Vaz, Mark Gandy, Mark Gould, Mark Knewstubb, Mark L, Mark Shaw, Mark W. McCarthy, Markus Hessler, Marquess Joel Goldschmidt \"AngelicxSoul\", Martin \"Malangs\" Langhammer, Martin Do, Martin Estrada, Martin Hanze, Marty H, Master Yi & Wukong, Mathew Fang, Mathieu Krog, Matsubara Yuu (Lordmatsu), Matt, Matt C. Wepee, Matt Clark, Matt Halverson, Matt Kanon, Matthew A. Warren, Matthew Andrychuk, Matthew Bates, Matthew Ley, Matthew Robinson, Matthew Sanders, Matthew Schupack, Matthew Williams, Mattias Axblom, Max, Max \"NEXUS\" Sjøstrand, Max \"SpaceWizard\" Mohler, Max Battcher, Max McIntyre, MaxMahem, Mazikeen Wagner, Mega4709, meganothing, Mehlo, Mereck, Micah Steele, Michael, Michael \"beefsack\" Alexander, Michael \"BookwormOtaku\" Connell, Michael \"Chaostraveler\" Cencarik, Michael Armey, Michael Beemer, Michael Brand, Michael Edward Miller, Michael Fedrowitz, Michael Grose, Michael Holcombe, Michael Kaplan, Michael Kwiatkowski, Michael Lingg, Michael McCollum, Michael Muske, Michael Ragdamar Tremblay, Michael Salyer, Michael Sand Petersen, Michael Stenqvist Haglund, Michael T. Ilano, Michael Troester, Michael W. Sim, Michael Wilkerson, Michel Lauzon, Miguel \"Mr.GreenToS\" Martinez, Miguel De Serpa, Miguel Lollett, Mikael Ronzier, Mike \"Ski\" Thomas, mike a pennington, Mike Ong, Mike Ostrow, Mike Taggart, Miki Hoshii, Miles Matton, Miss Roady Pie Esquire, Mithagar, MK, moe.kyun.Vokurek, Mohaan, Mondy, Morgan Hamilton, Mostly_Magic, Mr.Quija, Murat Boduroglu, Myron Monteiro"
    cre "N:{p}N. Andrelli, N. Yoshimori, N/A, N/A, NAKAMZ, Natani Lucchini, Nathan Bunn, Nathan Taggart, Nathaniel Early, Nathaniel Pahl, Nahaniel Scott Rivers, Neil 'Elcs' Elcome, Nemo157, neothoron, Nersius, Neverstorm, Nicholas Bianchi, Nicholas Brady, Nicholas Lor, Nick Johnston, Nick Noe, Nico A Valdez, Nico B., Nicolas Barbezat, Nicolas Miranda, Nicolas Van Sintejan, Nigel Wright, Nijuu \"I Love GOG & DRM free\" Lau, Nikolay Donets, Nilesh 'Onomato', Nima Safaie, Nipun Wittayasooporn, Nobody679, Nolan \"AnalFries\" Raven, NoNamedFuzzyPanda2, None, Nonomo4"
    cre "O:{p}Oliver Perks, Olivier Lebeau-Paradis, Omar Rodriguez, Omikron, Onearmdude, Onery Popopango, Oniii-chan, OniPierreot, Opacity, Origin Angel, Owen Sa"
    cre "P-Q:{p}P. Rischka, Pablo Soler, Pat Jones, Patrick \"AThyper\" Daigle, Patrick \"Celowin\" Jones, Patrick \"Chaos\" Burke, Patrick Eitz, Patrick Ellis, Patrick LaCasse, Patrick Tan, Patrik Raijū Willner, Paul Coombes, Paul H, Paul Houston Clifford Martin Von Barron, Paul Mikelonis, Paul Rock, Paulo Rafael Guariglia Escanhoela, Paulus1000, Pavel Pohilko, Pawel Blizniak, Paweł Kolek, Peo01, Per Hedbor, Per Kristian Brastad, Per Sjödén, Perry, Peter B., Peter Lansdaal, Peter Schnare, Pharaohowen, Phil 'Kyubey' Lam, Phil Salon, Phil White, Philip Hagan, Pierre Nosek, pinvendor, Legendary Merchant of Pins, PJ Grant, pktlonewolf, Professor Ficus, prototype00, Puiheng Tse, Punner, Quan Doan"
    cre "R:{p}Radiovid, Ragnos13, Ramon Muradin, Randy Eckenrode, Randy Meister, Rasmus Vilsgaard, Raymond Au, Raymond Luis Armstrong, Raymond Y (Fatman139), Raz'Nagul, redeyesblackpanda, Redsnabba, Rehan Ansari, REMCAP, Rene Cabanza Jr., Revek, rgreat, Rias Klein, Ricardo \"kod\" Rodriguez, Richard \"Dablue\" Blaauw, Richard Daigle, Richard Ford, Richard Leiva, Richard Lin, Richard Loh, Rick Reischman, River Thames, Robbie Boerner, Robert Billings, Robert D., Robert Disbrow, Robert Kitzmueller, Robert Labier, Robert McNaughton, Robert Musser, Roberto Carioli, Roberto Casas - rcasas83, Roberto Quintans, robotsheepboy, ROK - Yong Seok Park, Rommy Kwan, Ron Vondrasek, Ronan 2L, Ronin Storm, Roomkaasje, Ross, Ross Boskovski JR, Ross Brierley, Rudy M. Soto, Rufus, Russell Street, Ryan Dunnison, Ryan J. Jackson, Ryan K. (cat_pack), Ryan Tabb, Ryan Templeton, Ryan Ward, Ryan Woodland, Rykki, Ryzuku"
    cre "S:{p}Sam \"Tarvos\" Gibbins, Sam 'Bobular' Whittingham, Sam Garamy, Sam Mui (Seraph), Sam Thomas, Samarix2, Samuel Foster, Samuel Hartp}Samuel Malo, Sarah J Brown, Sascha Kunze, Saúl Mostacero, SayEric, Schaffer, Schuyler Kreitz, Scott Newitt, SeaGnome, Sean Bailey, Sean Kemp, Sean Shuai, Sean Steder, Sean Thurston, Sebastian Gerhold, SEPIA, Seth Crofton, Seto Konowa, Seyren Windsor, SH VL, Shadow, Shane Agnew, Shane Kilpatrick, Sharif Elgamal, Shaun \"IrishWonda\" Danis, Shaun Skelton, Shenmage, shiinx, Shimble, shinobi, Shuai \"Seingan\" Lin, siegeofjones, Sightless, Sihan Wang, Silentwatcher, SilverWasp, Simo Nyyssönen, Simon Bumgardner, Simon 'garkham' Landureau, Simon Holk, Sinou Rémi, Snowboundkarma, Solgrid, Solomon Lee, Somebodycooler, SonicGTR, Sonny Larsson, Stanislav, Stefan \"ramsesoriginal\" Insam, Stefan Markovic, Stefan Winkler, Stephan Szabo, Stephen Dougherty, Stephen Hazlewood, Stephen Lemelin, Steve \"Bofferbrauer\" Weidig, Steve Green, Steve Jasper, Steve Lord, Steven \"mchief75\" Simon, Steven \"Walshee-poo\" Walsh, Steven Duncan, Steven Farrar, Steven Hoffmann, Steven Holt, Steven Kang, Steven Kirby, Steven Rexroth, Steven Tincknell, Steven Vuong, Stormfox, Stuart Logan, Sugartit, Super Jared, SusanTheCat, Szymon \"Amerth\" Przybylak"
    cre "T:{p}T. K. Motoyama, Tai Tran, Tanner Garrett, Tapper, Taylor \"Berserk\" Staley, Taylor Collins, Te Hung Tseng, Team Kazam, Tengku Aiman Zulfika, Terence Ow, Terris H20, The Blind Gardener, The Dude, The Grand Harmony of Cetacea, The Patrick Tran, The Wanderer, thezeldagamer, Thissa, Thomas Aasebø, Thomas Aigner, Thomas Custer, Thomas Haymes, Thomas Kaghan, Thomas Schwarz, Thomas Siemens, Thomas Z. Palka, Thomas Zilling, Thorgard, Tim Crothers, Tim Danysh, Tim Ferguson, Tim L, Tim Newman, Tim Reilly, Tim Reynolds, Tim Thacher, Time Lord Ponce, Timmothy \"Akeashar\" Clarke, Timothy Acuff, Timothy Chappell, Timothy Lim, Timothy Martin, Timothy McGowan, Timothy Miller, Timothy Updike, Ting \"Herobear\" Wong, toan tran, Tobias Bollinger, Tobias Schewe, Tom \"PyTom\" Rothamel, Tomare Utsu Zo, Tomas (Xarien) Refsland, Tommy Torenius, Tong Yu, Tony Roberts, Travis Spano, Travis Williams, Trevor Becker, Trevor DeVore, Trevor Sexton, Tristan Carranante, Tristan Kennison, Tsuki, Tuckles, twig, Tyler E. Trosper, Tyler Leger, Tyler Winfield"
    cre "U:{p}Unddphenix, unholyghost07, Uros Bartolj, Ursine Pedal Digit a/k/a \"Thug Life Otter\", USRPG"
    cre "V:{p}VAhrens, Valsang, Vasily Chinarev, Venron, Videogamer25, Vintson Knight, Vlad, Vladimir Putin, Vladimir Shvetsov, Voldar"
    cre "W-Y:{p}WalkingAtlas, Warboss Curb, Wes Owens, Will Chang, Will Kenni, Will Lawrence, William Bradley, William Bryant, William Fleming, William Joseph Owens, William Laminack, William Perry, William Roberts, William Taylor, Willid, Wilson Bilkovich, Wizbang The Mighty, www.boredgamer.co.uk, Wyrtt"
    cre "X-Z:{p}Xavier Dolci, Xiao, xxzindxx, Yaka, Yohan Withington, Yuri Van Dierendonck, Yurii Furtat, Zac Binion, Zach Milosic, Zach Whitesell, Zachary Kosarik, zack wood, Zak Kalles, Zalminen, zanza, Zenelix, Zenigame, Zero Null, Zetsuna, Zikri Muzammil, Zu Long, Zythiku, アルバート　ウェークス（AJ)"

    jump aftercredits4

label aftercredits4:

    scene black with dissolve

    window show
    play music "Music/March_of_Immortals.ogg"

    "NEXT TIME ON SUNRIDER..."
    "The Sunrider crew has won their first major victory with the help of the Alliance..."
    "But can Admiral Grey be trusted?"
    "Deception and intrigue in the Alliance's presidential election!"
    "The Sunrider crew finds itself ensnared in a galaxy wide conspiracy!"
    "Arcadius' secret doomsday weapon finishes construction!"
    "Three fleets converge deep inside a nebula to determine the fate of the galaxy!"
    "Icari faces the killer of her past!"
    "The Sunrider vs. the Legion! The battle cannot be won without the ultimate sacrifice!"
    "The Captain's past, revealed!"
    "Chigara confronts the curse of Diode!"
    "Join us next time in SUNRIDER: THE MASK OF ARCADIUS!"
    "And don't forget... There'll be lots of space whales next time too!"

    show dontmissit:
        zoom 10
        ease 0.5 zoom 1

    play sound "sound/drum.ogg"

    $ renpy.pause(1.0)

    stop music fadeout 1.5
    scene white with dissolvelong

    play sound "sound/drumroll.ogg"

    "And now... The results of our second character popularity contest!"
    "And the winner is..."

    show pollthree:
        xalign 0.5 yalign 0.5
    with dissolve

    "SHOCK! A three-way tie!"

    show sola uniform backturn neutral:
        xpos 0.75
    with dissolve

    sol "... ... ..."
    sol "... ..."
    sol "..."
    sol "(Absolutely no reaction at all)"

    show ava uniform facepalm:
        xpos 0.5
    with dissolve

    ava "I can't believe he actually put my name down on the ballot..."
    ava "And I hear they also made a daki of me!"
    ava "Absolutely unbelievable..."

    show chigara uniform handonchest ooscienceblush:
        xpos 0.25
    with dissolve

    chi "A-ah! I... I won again?!"
    chi "(Didn't expect that to happen.)"
    chi "O-oh my..."
    chi "T-thank you everyone for voting for me! Eh-heh..."
    chi "M-maybe this means I can finally be the main girl now..."

    show asaga uniform altneutral zomg:
        xzoom -1 zoom 1 xpos 0.1
    with dissolve

    asa "N-no way....!"

    return

label aftercreditsep3:

    scene black with dissolve

    window show
    play music "Music/March_of_Immortals.ogg"

    "NEXT TIME ON SUNRIDER..."
    "Captain Shields and the Sunrider crew race against time to rescue Asaga from the clutches of Veniczar Arcadius!"
    "A daring rescue!"
    "Will the Alliance arrive in time to help?"
    "The full Sunrider team is assembled!"
    "An ancient secret is revealed!"
    "Two armadas clash to determine the fate of the galaxy!"
    "And don't forget... There'll also be lots of space whales next time too!"

    show dontmissit:
        zoom 10
        ease 0.5 zoom 1

    pause 0.5
    play sound "sound/drum.ogg"

    $ renpy.pause(1.0)

    stop music fadeout 1.5
    scene white with dissolvelong

    play sound "sound/drumroll.ogg"

    "And now... The results of our second character popularity contest!"
    "And the winner is..."

    show polltwo:
        xalign 0.5 yalign 0.5
    with dissolve

    show icari plugsuit armscrossed embarassedtsun:
        xpos 0.8
    with dissolve

    ica "S-seriously... Winning such an embarrassing contest..."

    show icari plugsuit point angry with dissolve

    ica "This doesn't mean that I'm gonna do anything special for you in the beach episode, all right!?"

    show icari plugsuit point angry:
        ease 0.5 zoom 2.0 ypos 1.7

    ica "ALL RIGHT!?"

    "Who will win next time? Don't forget to vote at our forums!"

    return

label aftercreditsep2:

    window show
    play music "Music/SAMFREE.ogg" fadeout 1.5

    scene asagacorner with dissolve
    show asaga uniform neutral happy with dissolve



    play sound "sound/drumroll.ogg"
    show asaga uniform neutral happy with dissolve

    asa "With 33 votes counted, the winner is..."

    show pollone:
        xpos 0.01 ypos 0.4

    show asaga uniform neutral surprise with dissolve

    asa "E-eh!? Chigara!?"

    hide pollone with dissolve

    show chigara uniform handsup surprise:
        xpos 0.8
    with dissolve

    chi "O-oh? M-me? *Never expected to win*"

    show asaga uniform armscrossed sad with dissolve

    asa "N-no way... And I'm supposed to be the main girl... *100 percent expected to win*"

    show asaga uniform excited grin with dissolve

    asa "I guess this just means that the winner will get extra fan service shots in the beach episode!"

    show chigara uniform palmsup surpriseblush with dissolve

    chi "Eh!? N-no way..."
    asa "That's right people! Go root for your favorite girl in the next popularity poll! Who knows what nice things will happen to the winner in the beach episode. Heh-heh..."

    show chigara uniform twiddlefingers embarassed with dissolve

    chi "N-nice things huh..."

    show asaga uniform handsonhips happy with dissolve

    asa "And now... the moment you've been waiting for..."
    asa "We have some exclusive previews of our next big Kickstarter project, Doki Doki Space Whale and the Adventures of Unknown Pilot-kun!"
    asa "Ufufufu... Even though this is supposed to be top secret, I guess we can spill the beans on this."
    asa "Sit back... and watch our amazing pitch video!"

    window hide
    scene crash

    pause 1.0

    window show

    asa "EEEEEHHHHHHHHHH!?"

    return

label devconsoleshow:
    show screen devconsole


