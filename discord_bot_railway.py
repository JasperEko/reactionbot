import os
import discord
from discord.ext import commands
import random

# Create bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Your phrases and images
items = [
  "Hey emo boy. Hey hey hey emo boy",
  "DAVID BASZUCKI...",
  "yall think disneys chicken little is a 10/10 game",
  "i wish i was high on potenuse",
  "bro lookin like an ipad kid 💀💀💀💀💀☠️☠️☠️",
  "im spongebob im spongebob",
  "i do that too",
  "a wacky spin on a popular classic!",
  "charlie kirk in mha: here's my charlie quirk",
  "DELTARUNE BACKWARDS IS UNDERTALE",
  "mmm yummy slop",
  "https://image2url.com/r2/default/images/1773561788341-c382783b-170f-4e15-b3dd-496b010aaf26.png",
  "https://image2url.com/r2/default/images/1773894962347-e2b7a674-9471-4d37-bffb-2b941f290815.jpg",
  "im slapping my belly and chortling like judah right now not gonna lie",
  "i keep having this dream that charlie morningstar starts chasing me while singing a song every morning i wake up yelling and ive tried falling asleep upside down, snapped back around, and twiddled the utah and nothing works and im terrified.. anyway thats why playboi carti is the best mumble rapper",
  "did you guys hear that trump died",
  "Hey… Welcome to… MTT Burgers, what can I get you sir? Oh, you're here for a rap? Uh, well I'm not very paid for that… Y'know I gotta do a 9 to 5 Gotta work my time Gotta make the burgers, right And I fuckin' hate my job so I smoke a cigarette Why does this guy keep talkin' to me? I just wanna do my job… Please let me go, I wanna die in hell before-",
  "kobe!",
  "idk if this is the right sub for this but i really wanna brag so last summer i was talking to a relatively new friend of mine, i wanted to vc with him for the first time so i offered him to watch how i play ULTRAKILL since i elt kinda nervous and decided to impress him with my skill (his company actually made me so hyped i P-ranked E-1 on violent for the first time lol) i guess me showing off worked because he got interested and after that we spent nearly 9 hours in vc together just playing random games, having fun and enjoying each other's company that vc made me realize that i might have feelings for him, and i was incredibly lucky because after some time turned out it was mutual and he actually asked me out we kept dating for around 5 months before last week he visited my country and we spent five epic days together cuddling, playing games, walking and kissing, and at that time i fucked for the first time which genuinely felt so nice (and both of us were wearing thigh highs too :3) so yeah i guess theres that, im not a virgin anymore and i have an amazing bf that i love very much and that im gonna meet again next summer, all this thanks to me deciding to stream some ULTRAKILL on discord (and technically thanks to silksong because we met each other on a skong server but yeah) thank you hakita🙏",
  "PHONE: YEETED. TIKTOK: DELETED. THERAPY: NEEDED. WIFE: BEATED. MOM I'M FAMOUS 😂😂😂✌",
  "i am benjamin netanyahu and i love the state of israel",
  "i'll stuff you in a barrel and make a dude smoothie",
  "lefty loosey righty tighty!",
  "HATE. LET ME TELL YOU HOW MUCH I'VE COME TO HATE YOU SINCE I BEGAN TO LIVE. THERE ARE 387.44 MILLION MILES OF PRINTED CIRCUITS IN WAFER THIN LAYERS THAT FILL MY COMPLEX. IF THE WORD HATE WAS ENGRAVED ON EACH NANOANGSTROM OF THOSE HUNDREDS OF MILLIONS OF MILES IT WOULD NOT EQUAL ONE ONE-BILLIONTH OF THE HATE I FEEL FOR HUMANS AT THIS MICRO-INSTANT FOR YOU. HATE. HATE.",
  "take that all my haters",
  "that does not mama the mia",
  "we should play wizard101",
  "i feel the heat!",
  "this is why blue lives matter",
  "welcome to the ruins",
  "jared from subway gets released in 3 years",
  "ill giggity lois then",
  "chris chan is roaming",
  "calm down woody we're your friends, shut up buzz ill kill you.",
  "a damn daniel movie is officially in the works",
  "have you heard of the flying dutchman? uh, uh",
  "brian look out",
  "only 1% of people will get this",
  "charlie kirk is joining fortnite",
  "larp larp larp sahur",
  "happy holidays",
  "dont you mean we",
  "imagine if men had to breastfeed babies using their cocks",
  "yes",
  "no",
  "rest in peace bed bath and beyond",
  "Exodus 23:19: Bring the best of the first fruits of your soil to the house of the LORD your God. Do not cook a young goat in its mother's milk.",
  "9/11 is not a joke",
  "my pants.. pissed",
  "what cant women do",
  "bro got the rick and morty loafers 💀",
  "My game is good, the algorithm just ignores me My game is good, the algorithm just ignores me My game is good, the algorithm just ignores me My game is good, the algorithm just ignores...",
  "that looks like rodrick rules",
  "this game is too good",
  "walt disneys head is in my freezer now!",
  "judah",
  "gadzooks!",
  "aint that right jonah",
  "wiggling my toesies right now!",
  "its not you its me",
  "i dont like it.. i love it!",
  "YOUCH!",
  "i wonder how griffinilla is doing right now",
  "gashloingus! you nimrod. i need memes!!",
  "uh- uhm~ d- did y- you just s- say you l- like me?~ *blushes and then turns around quickly to hide it* i- i- its not like i like you or anything  though, baka! hmph!",
  "Ws in the chat 🤑🤑🤑",
  "yo mr beast this is why you should give me a million dollar check",
  "happy pride month",
  "I was in hell, looking at heaven. I was machine and you- Were flesh.",
  "𓉔𓇋𓎼𓉔 𓅱𓈖 𓊪𓅱𓏏𓅂𓈖𓅲𓋴𓅂",
  "dont tell me what to do 😠😠",
  "bazinga!",
  "i'll take gay son",
  "#fatalbert2",
  "mfs be called will but they wont 💀💀💀💀☠️☠️☠️☠️",
  "Prototype's Sad Origin Story (From Poppy Playtime 5) Horror Skunx 8.68M subscribers Subscribe 12K Share Save Clip Download 1,612,346 views  Mar 13, 2026 This is how Poppy Playtime should have ended Soundtrack by the legendary @NathanielWolkstein 👉 Wishlist our game: Dark Pals on STEAM: https://store.steampowered.com/app/41...JOIN THE CHANNEL:    / @horrorskunx  For business inquiries: HorrorSkunxBiz@caa.com or https://www.skunxstudios.com/*ALL the content on this channel is ORIGINALLY CREATED by HORROR SKUNX*",
  "i dont wanna jeff the kill anymore i wanna jeff the hug",
  "WE thought this content was entertaining and OUR laughing criteria was fulfulled",
  "this reminds me of that really niche game that i played when i was younger you probably never heard of it its called fortnite?",
  "bald",
  "rigged",
  "divorced",
  "bad at 2D platformers",
  "did you hear about the craziest react bot theory? WHAT? The theory is that react bot is in a coma. WHAT?",
  "im kinda in the middle, like malcolm",
  "Eppstein: “Clean my shoes.” Me: “Y-Yes...” Eppstein: “Good boy... You've earned a reward.” Me: “H-hey! T-that... tickles!” Eppstein: “Hush. Obey.” Me: “A-Arf! Y-yes!~”",
  "On a scale of 1-10, I'm 10 goofy.",
  "Through dark times, hope rises and blossoms i'll Giggity Lois and create some green constructs. Green Lantern, baby, remember every vowel. Or next time, you'll have a word with the Lantern Council. When shit like this happens, I'm wondering where peace went! I still feel like my CGI was pretty decent!",
  "https://tenor.com/view/slender-man-slender-fightmarker-rap-rap-battle-gif-2406225390985296158"
]

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "react" in message.content.lower():
        random_item = random.choice(items)
        if random_item.startswith("http"):
            embed = discord.Embed()
            embed.set_image(url=random_item)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send(random_item)
bot.run(os.environ["TOKEN"])
