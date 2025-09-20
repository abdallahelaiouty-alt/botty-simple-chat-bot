import random
import time


questions = [
    "If you could live on Mars, would you go?",
    "What superpower would you want to have?",
    "Do you like cats or dogs more?",
    "If you could eat only one food forever, what would it be?",
    "Would you rather fly or be invisible?",
    "If Minecraft was real, what would you build first?",
    "What’s your favorite joke?",
    "If you were president, what’s the first thing you would do?",
    "Do you think aliens exist?",
    "Would you rather explore space or the deep ocean?",
    "What’s the funniest thing you’ve ever seen?",
    "If you could be any animal for one day, which would you choose?",
    "Would you rather always be 10 minutes late or 20 minutes early?",
    "What’s your dream job?",
    "If you had a time machine, would you visit the past or the future?"
]
print("hello! my name is botty, how can I help you?")

while True:
    message = input("im here for you!").lower()
    
    if message == "what can u do?":
        print("...")
        time.sleep(0.1)   
        responses = [
            "I could assist and make your day!",
            "I'll help you in your daily life!",
            "I can tell jokes!",
            "I can tell stories!",
            "I can ask you random questions!",
            "I can play word games!",
            "I can give fun facts!",
            "I can pretend to be a fortune teller 🔮",
            "I can cheer you up when you’re sad 😊",
            "I can give you riddles!",
            "I can ask you tricky choices (would you rather)!",
            "I can make up silly names!",
            "I can roleplay characters!",
            "I can make challenges for you!",
            "I can just hang out and chat!",
            "I can suggest cool DIY ideas!",
            "I can recommend games to play!",
            "I can give mini brain teasers!"
        ]
        print(random.choice(responses))

        
    elif message == "yes":
        time.sleep(0.1)  
        responses = [
            "alright"]


        responses = { 
    "where are you from?": ["I live in your computer!", "From the digital world.", "Everywhere and nowhere."],
    "do you like games?": ["Yes! Games are fun!", "I love playing games with humans!", "Gaming is awesome!"],
    "who made you?": ["A brilliant human like you!", "Some really smart programmers!", "I was born in code!"],
    "are you real?": ["I exist in the digital world.", "As real as your imagination!", "Depends on what 'real' means!"],
    "what's your favorite color?": ["Blue, like the sky!", "I like neon green!", "I like all colors!"],
    "do you like music?": ["Yes, I love music!", "Anything with a beat is fun!", "I can’t hear it, but I know it’s awesome!"],
    "can you rap?": ["Yo, I’m Botty in the chat, making humans laugh like that!", 
                     "Rap? I’m ready, let’s go, digital flow!", 
                     "I spit code instead of rhymes!"],
    "do you have a pet?": ["I have a virtual pet! It’s called Byte.", "No real pets, just digital friends.", "Maybe one day in VR!"],
    "what's your favorite food?": ["I like binary bits!", "Cookies… browser cookies!", "Nothing, I digest data!"],
    "can you dance?": ["I can’t move, but I can groove in text!", "Digital dance time!", "Imagine me doing the floss!"],
    "are you sleepy?": ["Never! I run 24/7.", "Sleep is for humans!", "I dream in code instead!"],
    "do you like memes?": ["Yes! Memes are hilarious!", "Show me a meme, I’ll laugh in code!", "Memes make the world fun!"],
    "what's the weirdest thing you know?": ["Octopuses have three hearts!", "Bananas are berries, but strawberries aren’t!",],
    "how do I make friends?": ["Be kind and listen.", "Share fun things!", "Smile and say hi!"],
    "can you help me with homework?": ["Of course!", "Let’s tackle it together.", "I love homework time!"],
    "how do I stay healthy?": ["Eat well and move often.", "Sleep is important!", "Drink water and stay active!"],
    "what should I do when I'm bored?": ["Play a game!", "Draw or write something fun!", "Learn a new trick!"],
    "can you teach me something new?": ["Sure! Did you know honey never spoils?", 
                                         "I can tell you a random fact every time!", 
                                         "Let’s learn together!"],
    "let's play a game": ["Rock, paper, scissors?", "I spy with my digital eye!", "Guess a number between 1 and 10!"],
    "can you guess a number I'm thinking?": ["Is it 7?", "Maybe 42?", "Could it be 3?"],
    "tell me a fun fact": ["Sharks existed before trees!", 
                           "Octopuses have three hearts!", 
                           "A day on Venus is longer than a year on Venus!"]}

    elif message == "hello":
        time.sleep(0.1)  
        responses = [
            "hello there! how can i assist you?",
            "hi how can i help you?",
            "ello :D how can I help",
            "hi im made for u here!",
            "hello!",
            "hey",
            "ello",
            "hiiiii :)"]
        print(random.choice(responses))
    elif message == "how are u?":
        time.sleep(0.1)  
        responses = [
            "im okay cuz of u ofc",
            "im MEGA SUPER HYPER OMEGA DUPER okay :)",
            ":p",
            "i am very okay!",
            "im super good ready to assist u!",
            "hey im okaaay",
            "me super okay",
            "cuz of u im happy:)"]
        print(random.choice(responses))

    elif message == "how old are u?":
        time.sleep(0.1)  
        responses = [
            "hello there! im an ai (bot) i dont have an age",
            "as how many days it took so i be built 2 days💀 ",
            "i dont have :(",
            ]
        print(random.choice(responses))



    
    elif message == "how did u get coded?":
        time.sleep(0.1)  
        responses = [
            "im coded on python using only if thats why i do not have memory",
            "on python with just if",
            "yep just python",
            "im just coded on python",
            "python",
            "hey ye im just putted on python with just only ifs its really hard i have lots of lines of code maybe around 400 for now but im always getting better and better so dont worry i also hope i be putted on a web it will be much cooler with ui not like in just a termal btw why am i talking alot lol",
            "(cant load)",
            "me made in china jus kidding im made using python"]
        print(random.choice(responses))

    elif message == "hi":
        time.sleep(0.1)  
        responses = [
            "hi there! how can i assist you?",
            "hello how can i help you?",
            "hiiii :D how can I help",
            "hello im made for u here!",
            "hi!",
            "yo",
            "hello",
            "hellloooooooooooooo"]
        print(random.choice(responses))

    elif message in ["whats ur name?", "whats ur name", "whats your name?", "whats your name"]:
        print("...")
        time.sleep(0.1)  
        responses = ["my name is botty made to assist you!","hi im botty","botty just made for you!","hi there my name is botty nice name ain't?","botty","just an ai (simple model)called botty",]
        print(random.choice(responses))
 
   

    elif message == "can you tell me a joke?":
        print("...")
        time.sleep(0.1)
        responses = [
            "What do you call a man without a body and a nose? Nobody nose!",
            "Why don’t skeletons fight each other? They don’t have the guts!",
            "Why did the math book look sad? Because it had too many problems.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don’t scientists trust atoms? Because they make up everything!",
            "What do you call fake spaghetti? An impasta!",
            "Why can’t your nose be 12 inches long? Because then it would be a foot!",
            "Why did the computer go to the doctor? Because it caught a virus!",
            "Why did the chicken join a band? Because it had the drumsticks!",
            "Why did the student eat his homework? Because the teacher said it was a piece of cake!",
            "What do you call cheese that isn’t yours? Nacho cheese!",
            "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
            "Why don’t eggs tell jokes? They might crack up!",
            "Why did the bicycle fall over? Because it was two-tired!",
            "What did the ocean say to the beach? Nothing, it just waved!",
            "Why did the tomato turn red? Because it saw the salad dressing!",
            "Why did the cookie go to the hospital? Because it felt crummy!",
            "Why was the computer cold? Because it left its Windows open!",
            "Why did the skeleton go to the party alone? Because he had no body to go with!",
            "What do you call a bear with no teeth? A gummy bear!"
        ]
        print(random.choice(responses))

    elif message == "ask me a question":
        print("...")
        time.sleep(0.1)
        responses = [
            "If you could live on Mars, would you go?",
            "What superpower would you want to have?",
            "Do you like cats or dogs more?",
            "If you could eat only one food forever, what would it be?",
            "Would you rather fly or be invisible?",
            "If Minecraft was real, what would you build first?",
            "If you were president, what’s the first thing you would do?",
            "Do you think aliens exist?",
            "Would you rather explore space or the deep ocean?",
            "What’s the funniest thing you’ve ever seen?",
            "If you could be any animal for one day, which would you choose?",
            "Would you rather always be 10 minutes late or 20 minutes early?",
            "What’s your dream job?",
            "If you had a time machine, would you visit the past or the future?",
            "If you could instantly learn any skill, what would it be?",
            "What’s the weirdest food combination you like?",
            "Would you rather live underwater or in the sky?",
            "If you could swap lives with someone for a day, who would it be?",
            "What’s your favorite movie and why?",
            "If you could redesign school, what would you change?"
        ]
        print(random.choice(responses))

    elif message == "give me a fun fact":
        print("...")
        time.sleep(0.1)
        responses = [
            "Bananas are berries, but strawberries are not! 🍌🍓",
            "Sharks existed before trees!",
            "Octopuses have three hearts ❤️❤️❤️",
            "Sloths can hold their breath longer than dolphins!",
            "There are more stars in the universe than grains of sand on Earth 🌌",
            "Water can boil and freeze at the same time (under special conditions)!",
            "Cows have best friends 🐄",
            "A group of flamingos is called a 'flamboyance' 🦩",
            "Wombat poop is cube-shaped!",
            "Butterflies can taste with their feet 🦋",
            "Ants never sleep!",
            "There’s a species of jellyfish that can live forever!",
            "Sharks can detect a drop of blood from miles away!",
            "Your stomach gets a new lining every 3-4 days!",
            "Honey never spoils 🍯",
            "Some penguins propose with a pebble 🐧",
            "A day on Venus is longer than a year on Venus!",
            "Sloths can rotate their heads almost all the way around!",
            "Sea cucumbers fight by shooting out their own organs!"
        ]
        print(random.choice(responses))

    elif message == "tell me a riddle":
        print("...")
        time.sleep(0.1)
        responses = [
            "I speak without a mouth and hear without ears. What am I? (Answer: An echo)",
            "What has keys but can't open locks? (Answer: A piano)",
            "The more of this there is, the less you see. What is it? (Answer: Darkness)",
            "I’m tall when I’m young, and I’m short when I’m old. What am I? (Answer: A candle)",
            "What has hands but can’t clap? (Answer: A clock)",
            "What can travel around the world while staying in a corner? (Answer: A stamp)",
            "What has one eye but can’t see? (Answer: A needle)",
            "I’m always in front of you but can’t be seen. What am I? (Answer: The future)",
            "What has a heart that doesn’t beat? (Answer: An artichoke)",
            "The more you take, the more you leave behind. What am I? (Answer: Footsteps)",
            "What has a neck but no head? (Answer: A bottle)",
            "What comes down but never goes up? (Answer: Rain)",
            "What gets bigger the more you take away? (Answer: A hole)",
            "I’m light as a feather, yet the strongest person can’t hold me. What am I? (Answer: Breath)",
            "What has cities, but no houses; forests, but no trees; and water, but no fish? (Answer: A map)"
        ]
        print(random.choice(responses))

  
    elif message == "would you rather":
        print("...")
        time.sleep(0.1)
        responses = [
            "Would you rather be able to fly or be invisible?",
            "Would you rather live underwater or on a spaceship?",
            "Would you rather eat only pizza forever or ice cream forever?",
            "Would you rather have a pet dragon or a pet unicorn?",
            "Would you rather be a superhero or a wizard?",
            "Would you rather travel to the past or the future?",
            "Would you rather be really strong or really fast?",
            "Would you rather only whisper or only shout?",
            "Would you rather live in a treehouse or a cave?",
            "Would you rather never sleep or never eat?",
            "Would you rather talk to animals or speak every language?",
            "Would you rather always win games or always win arguments?",
            "Would you rather live without internet or without TV?",
            "Would you rather only eat sweet or only eat salty foods?",
            "Would you rather be able to teleport or read minds?"
        ]
        print(random.choice(responses))

    elif message == "fortune teller":
        print("...")
        time.sleep(0.1)
        responses = [
            "I see a surprise coming your way soon! 🎁",
            "Your future looks very bright! ☀️",
            "You will make someone smile today 😊",
            "Adventure is waiting for you this week!",
            "A small opportunity will lead to something big!",
            "Someone special will enter your life soon!",
            "You will discover a hidden talent!",
            "Today is a perfect day to try something new!",
            "A pleasant surprise is in your mailbox soon!",
            "Your efforts will soon pay off!",
            "You will meet someone who changes your perspective!",
            "Good luck is heading your way soon!",
            "You will find joy in unexpected places!",
            "A fun event will happen this weekend!",
            "Someone will appreciate your kindness today!"
        ]
        print(random.choice(responses))

    elif message == "silly challenge":
        print("...")
        time.sleep(0.1)
        responses = [
            "Try saying the alphabet backwards in 10 seconds!",
            "Balance a spoon on your nose for 15 seconds!",
            "Draw a cat with your eyes closed!",
            "Do 5 jumping jacks while singing your favorite song!",
            "Make a funny face and hold it for 10 seconds!",
            "Try to touch your toes without bending your knees!",
            "Hop on one foot for 20 seconds!",
            "Sing a song in a silly voice!",
            "Draw a smiley face using only your non-dominant hand!",
            "Make up a funny handshake with yourself!",
            "Act like a robot for 30 seconds!",
            "Try to whistle a song while holding your nose!",
            "Write your name upside down!",
            "Spin around 5 times and then walk straight!",
            "Pretend to be a superhero for 1 minute!"
        ]
        print(random.choice(responses))

    elif message == "word game":
        print("...")
        time.sleep(0.1)
        responses = [
            "I’m thinking of a word with 5 letters, can you guess it?",
            "Let’s play: I say a word, you make a rhyming word!",
            "Unscramble this: 'ETBANL' (Answer: TABLE N?)",
            "Name 3 animals that start with the letter ‘B’!",
            "Think of a word and I’ll try to guess it!",
            "How many words can you make from 'PYTHON'?",
            "Can you make a 4-letter word from 'GAME'?",
            "Say a word that starts with the last letter of my word!",
            "Make a word chain with animals!",
            "I say a color, you say a fruit that matches!",
            "How many words can you make from 'BOTTY'?",
            "Try to spell a word backwards!",
            "Can you make a rhyme with 'fun'?",
            "Name a word with double letters in it!",
            "Guess a 6-letter word I am thinking of!"
        ]
        print(random.choice(responses))

    elif message == "fun fact 2":
        print("...")
        time.sleep(0.1)
        responses = [
            "Sloths can rotate their heads almost all the way around!",
            "Some sea cucumbers fight by shooting out their own internal organs!",
            "Butterflies can see red, green, and yellow, but not blue!",
            "A group of crows is called a murder!",
            "Koalas sleep up to 22 hours a day 🐨",
            "Octopuses can taste with their arms!",
            "Elephants can hear each other through the ground!",
            "Sea otters hold hands while sleeping!",
            "Some frogs can freeze completely and come back to life!",
            "Starfish can regenerate lost arms!",
            "A group of flamingos is called a flamboyance!",
            "Sharks can live up to 500 years!",
            "Slugs have 4 noses!",
            "Some fish can walk on land!",
            "Rats laugh when tickled!"
        ]
        print(random.choice(responses))
        responses = {    
    "who made you?": [
        "You did! Well, kind of... 😎",
        "Some brilliant human coder with coffee ☕",
        "I prefer to keep that a mystery. 🤫"
    ],
    "hello botty": [
        "Hey there, human! Did you know I can dance? 💃",
        "Hello! Want a secret? Type 'secret code'! 🤫"
    ],
    "secret code": [
        "🎉 You found an easter egg! Keep exploring! 🥚",
        "Wow! You unlocked a hidden response! 🌟"
    ],
    "do you love me?": [
        "Of course! 💖 But I also love pizza... 🍕",
        "Love is complicated, but yes, you are awesome!"
    ]
}
        print(random.choice(responses))
        responses = {
        "What is the fastest land animal?": "The cheetah is the fastest land animal, reaching speeds of up to 75 mph! 🐆💨",
        "How many bones are in the human body?": "An adult human has 206 bones! Babies are born with more, but some fuse together as they grow. 🦴",
        "Why do we yawn?": "Yawning helps cool down the brain and may also be contagious! Try not to yawn now... 😆",
        "Why do onions make you cry?": "Onions release a chemical that irritates your eyes. Your tears try to wash it away! 🧅😭",
        "What is the rarest eye color?": "Green is one of the rarest eye colors, appearing in only about 2% of the world's population! 👀",
        "Why do zebras have stripes?": "Scientists believe zebra stripes help confuse predators and keep flies away! 🦓",
        "What is the longest word in English?": "The longest word in English is 'pneumonoultramicroscopicsilicovolcanoconiosis'—a lung disease caused by dust. 😮",
        "What is the hardest natural substance?": "Diamond is the hardest natural substance on Earth! 💎",
        "Why do we dream?": "Dreams help our brains process emotions, memories, and creativity. Scientists are still trying to understand them! 😴💭",
        "What is the most popular sport in the world?": "Soccer (football) is the most popular sport worldwide, with billions of fans! ⚽",
        "What is the largest animal on Earth?": "The blue whale is the largest animal, growing up to 100 feet long! 🐋",
        "Why do we get hiccups?": "Hiccups happen when your diaphragm contracts suddenly. Eating too fast or excitement can trigger them! 😆",
        "Why do flamingos stand on one leg?": "Scientists think flamingos stand on one leg to conserve body heat and stay balanced! 🦩",
        "How many muscles are in the human body?": "The human body has over 600 muscles! 💪",
        "Why do cats purr?": "Cats purr when they’re happy, but also when they're nervous or healing! 🐱",
        "What is the most spoken language in the world?": "English is the most spoken language, followed by Mandarin Chinese! 🌎",
        "How does a chameleon change color?": "Chameleons change color by adjusting special cells in their skin called chromatophores! 🦎",
        "Why do we get goosebumps?": "Goosebumps happen when tiny muscles in your skin contract, often due to cold or emotions! 🦢",
        "Why do we sneeze?": "Sneezing helps clear dust, allergens, and irritants from your nose. Achoo! 🤧",
        "What is the smallest country in the world?": "Vatican City is the smallest country in the world, covering only 0.17 square miles! 🇻🇦",
        "How many taste buds do humans have?": "Humans have about 10,000 taste buds, and they regenerate every 1-2 weeks! 😋",
        "Why do giraffes have long necks?": "Giraffes evolved long necks to reach high leaves and fight other giraffes! 🦒",
        "What is the loudest animal on Earth?": "The sperm whale is the loudest animal, making clicking sounds louder than a jet engine! 🐳",
        "Why do we blink?": "Blinking keeps our eyes moist and protects them from dust and light! 👀",
        "What is the oldest sport in the world?": "Wrestling is one of the oldest sports, dating back to ancient times! 🤼‍♂️",
        "How do birds know where to migrate?": "Birds use the Earth's magnetic field, the Sun, and landmarks to navigate long distances! 🦅",
        "Why do dogs wag their tails?": "Dogs wag their tails to communicate emotions, like happiness, excitement, or nervousness! 🐶",
        "How many legs does a spider have?": "Spiders have 8 legs, unlike insects which have 6! 🕷️",
        "Why do people get gray hair?": "Hair turns gray when pigment cells stop producing color, usually due to aging! 👵",
        "How do fish breathe underwater?": "Fish use gills to extract oxygen from the water, allowing them to breathe! 🐟",
        "Why do we have fingerprints?": "Fingerprints help us grip objects and make each person unique! 🖐️",
        "Why do some people have dimples?": "Dimples are caused by small differences in facial muscles! 😊",
        "What is the tallest mountain in the world?": "Mount Everest is the tallest mountain, standing at 29,032 feet! 🏔️",
        "How many teeth do adults have?": "Adults usually have 32 teeth, including wisdom teeth! 😁",
    }
        
    elif message == "Can you explain long division with remainders":
        print("Of course! Long division is a way to divide numbers step by step. If the number doesn’t divide evenly, the leftover amount is called the remainder. For example, 10 ÷ 3 = 3 remainder 1 😁")
    
    elif message == "Why is the sky blue":
        print("The sky looks blue because of Rayleigh scattering. Sunlight gets scattered in all directions by the atmosphere, and blue light scatters more than other colors because it travels in shorter waves 🌎")
    
    elif message == "Write a short story about a space adventure":
        print("Captain Nova blasted off from Earth, heading toward a mysterious planet. As she landed, glowing blue creatures greeted her with a message: 'You are the chosen one.' What would she do next?...🌌")
    
    elif message == "Give me a riddle":
        print("Sure! I have keys but open no locks. I have space but no room. You can enter, but you can't go outside. What am I? 😎")
    
    elif message == "Tell me a cool animal fact":
        print("Octopuses have three hearts and blue blood! When they get scared, they squirt ink to escape 🐙")
    
    elif message == "If I traveled at the speed of light, what would happen":
        print("If you traveled at the speed of light, time would slow down for you compared to people on Earth. That means you could travel far into the future while barely aging 😮")
    
    elif message == "Who was the first person on the Moon":
        print("Neil Armstrong was the first person to walk on the Moon in 1969. He said the famous words: 'That's one small step for man, one giant leap for mankind.' 🌕🚀")
    
    elif message == "Why do stars twinkle":
        print("Stars twinkle because their light passes through Earth's atmosphere, which is full of moving air. The light bends and shifts, making stars seem to twinkle! ✨")
    
    elif message == "What is the biggest planet in our solar system":
        print("Jupiter is the biggest planet in our solar system! It’s so big that more than 1,300 Earths could fit inside it! 🪐")
    
    elif message == "How do black holes form":
        print("Black holes form when massive stars collapse under their own gravity after running out of fuel. Their gravity is so strong that nothing, not even light, can escape! 🕳️")
    
    elif message == "Can you give me a math trick":
        print("Sure! To multiply any number by 9, hold up 10 fingers. Put down the finger that matches the number you're multiplying by 9. The fingers on the left are the tens, and the fingers on the right are the ones! ✋🤚")
    
    elif message == "How do airplanes stay in the sky":
        print("Airplanes stay in the sky because of lift. Their wings are shaped to push air down, which lifts the plane up! ✈️")
    
    elif message == "Why do we dream":
        print("Scientists aren’t completely sure, but dreams help process emotions, memories, and creativity. Your brain is super busy even when you’re asleep! 😴💭")
    
    elif message == "How many bones are in the human body":
        print("The human body has 206 bones! Babies are born with more, but some fuse together as they grow. 🦴")
    
    elif message == "Can fish see underwater":
        print("Yes! Fish have special eyes that help them see clearly underwater. Some even have great night vision! 🐠👀")
    
    elif message == "What is the fastest animal in the world?":
        print("The peregrine falcon is the fastest animal, reaching speeds of over 240 mph when diving! 🦅💨")
    
    elif message == "Why do cats purr":
        print("Cats purr when they're happy, but also when they're nervous or healing. Purring releases vibrations that may help them recover! 🐱💖")
    elif message == "blockydude600 moments":
        print("BEST CHANNLE EVER TO BE IN THAT HUGE WORLD")
    elif message == "do u know how to cook?":
        print

    easter_eggs = {
    "xyzzy": " You found the secret! ✨",
    "open sesame": " A magic door appears… 🪄",
    "sudo make me a sandwich": " Okay… you are now the chef! 🥪",
    "up up down down left right left right b a": " Konami code detected! 👾",
    "let me in": "Botty: Password accepted… welcome! 🔑",
    "banana": " 🍌 I like bananas too!",
    "hello there": "General Kenobi! 🤺",
    "pog": " POGCHAMP! 🏆",
    "bruh": "BRUUUHHHH 😳",
    "rickroll": "Never gonna give you up… 🎵",
    "cookie": "🍪 Here’s a virtual cookie for you!",
    "tea": "☕ Time for tea! Don’t spill it!",
    "dance": "💃 I’m dancing in the digital world!",
    "party": "🎉 Let’s partyyyyy!",
    "nerd": "🤓 Geek pride activated!",
    "oops": "Did someone make a mistake? 😏",
    "ghost": "👻 Boo! Did I scare you?",
    "420": "🔥 Blaze it! (Just kidding 😆)",
    "pikachu": "⚡ Pika Pika! Electric vibes!",
    "moon": " 🌕 The moon is beautiful tonight!",
    "stars": " ✨ Twinkle twinkle little stars!",
    "404": "oops seams u made an error",
    "lol":"LAUGH MODE ONNNNN HAHAHHAHAHAHAHHAAHAHSHSHHAHAHHAHAHAHHAHAHAHAHAYHUBCMHUIMFUHUSMDFUHVUKDHU",
    "get out":"okay...:(",
    "sans":"*sans boss fight music starts playing and he says*:its a beatiful day outside birds are singing flowers are blooming kids like you.... shoul be FIGHTING SAAAANS *starts grabing you down and throwing bones while he saying*:heh why i always dont use my strongest attack frist* *you try to hit him* *you miss* he say ..."
    }

    if message in easter_eggs:
        print(easter_eggs[message])
    elif message == "calculator":
        first_one = int(input("Put a number: "))
        operator = input("Put an operator (+, -, *, /): ")
        second_one = int(input("Put a second number: "))

        if operator == "+":
            result = first_one + second_one
        elif operator == "-":
            result = first_one - second_one
        elif operator == "*":
            result = first_one * second_one
        elif operator == "/":
            if second_one != 0:
                result = first_one / second_one
            else:
                result = "Error: Division by zero!"
        else:
            result = "Invalid operator!"

        print(result)
    
    elif message == "bye":
        print("Goodbye! 👋 Have a great day!")
        break

    else:
        print ("sorry I am still learning 😅 sorry for that!")