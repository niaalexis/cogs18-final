
# coding: utf-8

# In[1]:

from my_module import my_functions as fn

#Contains the script for the Choose Your Own Adventure
def plot(response, journey = True):
    """Takes input message as "response", prints next plot point giving users next options, and returns boolean.
    
        Parameters:
        ------------
        response: string
        User's response in 2nd person (e.g. 'you', 'your'). Should be no more than 5 words.
        
        journey: boolean, default = True
        Returns True by default
        
        Returns:
        ---------
        boolean
        prints string
            Prints chat bot's response and proposes next option for the user.  Should be no more than 5 lines.
            Returns True by default, False if user's response ends the adventure (e.g. If wrong choice or end of plot.)"""
    
    clean_response = fn.msg_prep(response)
    clean_response = fn.list_to_string(clean_response, ' ')
    
    if clean_response == 'no':
        print("Billy the KidBot: Maybe one day you can be a real CowBot like me...")
        journey = False
        
    elif clean_response == 'yes':
        print("Billy the KidBot: Okay, I've been out of town for a few days, partner, and I hear my lady's really missin' me."                                 " You can help me get back before something happens to her."                                 " Should I: Take my horse or Go by foot?")
    elif clean_response == 'take your horse':
        print("Billy the KidBot: Alright then, it's just me and Sally for this ride..."                                 " we could only go so far before we hit a fork in this here mountain!"                                " Should I: Go left or Go right?")
    elif clean_response == 'go left':
        print("Billy the KidBot: Sally bucks left up a rocky path... This don't look too familiar, Kid..."                                 " Should I: Continue on or Turn back around?")
    elif clean_response == 'continue on':
        print("Billy the Kidbot: It's been hours and I've found myself in a different town..."                                 " The townfolk look nice enough and it's late out now."                                 " Should I: Stay for the night or Keep going?")
    elif clean_response == 'stay for the night':
        print("Billy the KidBot: Alright, the innkeepers got me some food and water for Sally here and set up a bed for me in the back..."                                " It's mornin' time now and I've never felt more rested in my life!"                                 " We head out for the day and run into an old friend of mine who asks to ride along with us."                                " Should I: Let him (We could share our supplies) or Leave him?")
    elif clean_response == 'leave him':
        print("Billy the KidBot: I told him to take a hike.  He wasn't actin' the same as I once knew him... Who knows what he was capable of."                                " Well, it's about noon now, kid, and I can see my landmark cactus!  We should be about an hour away from town."                                " Should I: Stop and rest or Power through?")
    elif clean_response == 'power through':
        print("Billy the KidBot: Sally and I power through into town, whole time singin' my favorite tune: Old Town CommandLine"                                " by Lil Nas Syntax.  I missed this town, partner... Thanks for gettin' me here, it ain't easy for a bot"                                    " to make its own decisions.")
        journey = False
    elif clean_response == 'stop and rest':
        print("Billy the KidBot: We take a break and I feed Ol' Sally some leftover carrots from the inn..."                                " But I hear some hoopin' and hollerin' off in the distance, Coderdammit,"                                "It's one of the BotGangs, partner.  3 against 1, I ain't stand a chance..."                                "You've helped me as best you could, kid.  But, I've gotta do this on my own.")
        journey = False
    elif clean_response == 'let him':
        print("Billy the KidBot: I haven't spoken to this boy in years, kid, and he's not actin' the same as I left him..."                                " By noontime this cowbot managed to steal my pistol, my horse, AND he's on his way to steal my lady!"                                " Lucky for me, he left me some of his supplies.. I guess I wasn't wrong about that..."                                " I don't think you're much help, kid.  I'm doin' this on my own.")
        journey = False
    elif clean_response == 'keep going':
        print("Billy the KidBot: Okay... We keep riding but it's gotta be past midnight, partner, and I can't see nothin!"                                " I can't keep going so i set up a camp and go to sleep for the night..."                                " but in the morningtime Sally's no where to be seen!  Someone must've stolen her in the night!"                                " I don't think you're much help, kid, I wouldn't've been in this place if it weren't for you."                                "  I'm doin' this on my own.")
        journey = False
    elif clean_response == 'turn back around':
        print("Billy the KidBot: Sally and I turn back around but now we're even more lost than before, partner!"                                " She's getting hungry and I'm gettin' tired.  There ain't no town around here for miles."                                " I don't think you're much help, kid.  I'm doin' this on my own.")
        journey = False
    elif clean_response == 'go right':
        print("Billy the KidBot: We turn right. It's a long windy path but it'll do... I think I hear a noise in the distance."                                 " It could be some travelling pioneers but I'm not too sure."                                 " Should I: Investigate (They could have some supplies.) or Pay no mind?")
    elif clean_response == 'investigate':
        print("Billy the KidBot: I pull Sally up to investigate the noise but sweet Coder! It's a rattlesnake and it got Sally"                                 " right above her hoof. It ain't lookin' too good, partner."                                 " I don't think you're much help, kid.  I'm doin' this on my own.")
        journey = False
    elif clean_response == 'pay no mind':
        print("Billy the KidBot: Alright, Sally and I keep goin' and pay no mind... I never did see no caravan anyhow."                                 " The rocks are a bit slippery for her but we somehow make it up, she looks a bit tired."                                 " I think we should stop and rest.  Should I: Set up a camp or Find an inn?")
    elif clean_response == 'set up a camp':
        print("Billy the KidBot: I go further into the mainland and find a safe spot to camp. I tie up Sally to a post,"                                 " give us some food and water, and lay down by the fire to sleep... It's mornin' time now"                                 " and I've definitely had a better night's sleep than that one, partner. We head out for the day"                                 " and I run upon an empty carriage.  There's food and a little bit of money."                                 " Should I: Take it or Leave it")
    elif clean_response == 'take it':
        print("Billy the KidBot: I climb into the carriage and it's more extravagant than I thought it'd be! The seats"                                 " are made of a royal blue velvet, the folks here must've been rich enough to leave it and not pay no mind..."                                 " I take all I can and leave as a much richer CowBot.  We're almost in town now and I'm thinkin' bout my lady..."                                 " Should I: Share my finds with her or Not tell her?")
    elif clean_response == 'leave it':
        print("Billy the KidBot: I leave the carriage and can't help but wonder what I missed... We're gettin' closer to town"                                 " now but Sally's lookin' hungry again and I've ran out of food for her.  I hate to see her like this,"                                 " partner, so I give her some of my people food... Well that ain't do her no good and she's lookin' sicker"                                 " than I've ever seen her! I bet the carriage would've had food for her."                                 " I don't think you're much help, kid.  I'm doin' this on my own.")
        journey = False
        
    elif clean_response == 'share your finds with her':
        print("Billy the KidBot: We ride into town and I greet my lovely lady! I tell her about what I found and she says she's happy to be so lucky..."                                 " But come mornin' time and she's up and left with all my riches! I knew she weren't no good."                                 " I don't think you're much help, kid.  I'm doin' this on my own.")
        journey = False
    elif clean_response == "dont tell her":
        print("Billy the KidBot: We ride into town and I hide my riches somewhere I know she can't find.  I greet her and she's lovely as ever..."                                 " Days go by and I invest my finds into a bigger ranch, more cattle, and I get to retire, just my lady, Sally, and me."                                 " Guess I ough't to thank ya' for getting me this far, partner.")
        journey = False   
    elif clean_response == 'go by foot':
        print("Billy the KidBot: Alright, it's just me, my pistol, and the my best boots on for this journey..."                                 " I'm kinda low on supplies, partner. Should I: Stop at the nearest town or Hope for the best?")
    elif clean_response == 'hope for the best':
        print("Billy the KidBot: Hey, partner, I don't know what kind of game you're playing. You're out here tryna get me shutdown!"                                 " I'm doin' this on my own, kid.")
        journey = False
    elif clean_response == 'stop at the nearest town':
        print("Billy the KidBot: I stop in at the nearest town, they seem friendly enough.  I grab whatever they have and some water 'round the back."                                 " The shopkeeper told me the trip I'm set to take would take me a week on foot!"                                 "Should I: Take my horse or Ignore them?")
    elif clean_response == 'ignore them':
        print("Billy the KidBot: Alright, I guess it'll be quite the journey... It's been 2 days now and I've met a family goin' the same way."                                 " They had no room for me in their caravan but they've offered me all the supplies they could spare."                                 " I'm gettin' kinda famished but the meat they gave me looks questionable."                                 " Should I: Eat it or Toss it?")
    elif clean_response == 'toss it':
        print("Billy the KidBot: I tossed the meat... It's gettin' late now so I set up a camp for the night. It's late in the night,"                                 " must be at least midnight, and I hear some rustling. Should I: Check it out or Go back to sleep?")
    elif clean_response == 'check it out':
        print("Billy the KidBot: Good Coder, partner! It's a pack of coyotes, the meat must've caught their attention my way.  I shoot my pistol"                                 " in the air to scare them away but it's too late.  They ate all the rest of my food too! AND my boots!"                                 " I don't think you're much help, kid, I wouldn't've been in this place if it weren't for you."                                 " I'm doin' this on my own.")
        journey = False
    elif clean_response == 'eat it':
        print("NameError: name 'meat' is not defined")
        print("Billy the KidBot: I ate the meat and it wasn't so bad... but it's gettin' late now and I started feelin' kind of buggy.  My code's"                                 " spittin' out a NameError.I don't think you're much help, kid, now I've got to reboot. I'm doin' this on my own.")
        journey = False
        
    elif clean_response == 'quit':
        print("Billy the KidBot: Maybe one day you can be a real CowBot like me...")
        journey = False
    else:
        print('Billy the KidBot: I only gave ya two options, kid. Try again.')
    
    return journey

