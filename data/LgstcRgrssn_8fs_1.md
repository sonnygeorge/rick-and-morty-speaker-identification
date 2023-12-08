### 🚀 **LgstcRgrssn_8fs_1**

- 🤖 **Model Type**: 
	<class 'sklearn.linear_model._logistic.LogisticRegression'>
- 📊 **Dataset Used**: 
	_Random_
- 🧠 **Number of Features**: 
	1370
- 🚫 **Unused Features**: 
	316/1370
- ⌛ **Model Train Time**: 
	0.345
- 💬 **SpaCy Preprocessing Model**: 
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `random_state`: 42

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 0.863 | 0.503 | 0.505 |
| Macro F1 | 0.831 | 0.347 | 0.372 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.80 | 0.20 | 0.32 |
| Jerry | 0.25 | 0.06 | 0.09 |
| Morty | 0.37 | 0.53 | 0.44 |
| Rick | 0.57 | 0.73 | 0.64 |
| Summer | 0.40 | 0.18 | 0.25 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.50 | 0.21 | 0.30 |
| Jerry | 0.25 | 0.20 | 0.22 |
| Morty | 0.43 | 0.43 | 0.43 |
| Rick | 0.57 | 0.79 | 0.66 |
| Summer | 1.00 | 0.14 | 0.25 |

### 🧠 Feature Extraction Methods

| Method |
| ------ |
| Total Sentence Count |
| Average Tokens Per Sentence |
| Average Word Length |
| Exclamation Marks Per Sentence |
| Dashes Per Sentence |
| All 1-Gram One Hots (-blacklist) |
| Proportion Of Tokens That Are Stop Words |
| Proportion Of Chars That Are Capitalized |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Uh, yeah, just a few more design notes.  Um, this guy. The, uh... The, uh... | Morty | Rick |
| Uh, what? It was your job, Morty. | Rick | Summer |
| Oh, God, what’s going on now? | Summer | Beth |
| He bails on everybody! He bailed on Mom when she was a kid! He -- He bailed on tiny planet! And in case I never made this clear to you, Summer, he bailed on you. He left you to rot in a world that he ruined because he doesn't care! Because nobody's special to him, Summer, not even himself. So, if you really want your grandpa back, grab a shovel. The one that won't let you down is buried in your backyard! | Rick | Morty |
| That's right, Morty. This is gonna be a lot like that, except, you know, it's gonna may--be make sense. | Morty | Rick |
| Boy, you really got me up against a wall this time, Jerry. | Beth | Rick |
| Aw, geez. Okay. I guess I can skip history. What about Frank? I mean, shouldn't you unfreeze him? | Rick | Morty |
| Hey! I said nobody move, buddy! | Morty | Rick |
| Me. I used to wear blue pants. | Morty | Rick |
| Alright! That's enough. You're talking about my species! We understand genocide, we do it sometimes! | Rick | Jerry |
| Come on, Morty! We got to get the hell out of here! | Morty | Rick |
| I am not putting my father in a home! He just came back into my life, and you want to grab him and stuff him under a mattress like last month's Victoria's Secret? | Rick | Beth |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Rick | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Rick | Jerry |
| You don’t have to be a dick. | Morty | Rick |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| They're just robots, Morty! It's okay to shoot them! They're robots! | Morty | Rick |
| I'm sorry. It's just like the end of "Old Yeller. | Morty | Jerry |
| It's the Citadel of Ricks. All the different Ricks from all the different realities got together to hide here from the government. | Rick | Morty |
| How is praying going to help? | Summer | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| Aw! Oh, my God! He recognizes the other dogs on TV. | Morty | Summer |
| The day I invented the portal gun is the day I lost her. | Morty | Rick |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Rick | Summer |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Rick | Jerry |
| Hey, what's wrong Morty? Oh, you're worried about your dad, huh? | Summer | Rick |
| There's just one problem, Morty one little hang-up. The dimension I visited was so advanced, that  they had also halted the aging process, and everyone there was young, Morty, and they had been forever. I was the only old person there, Morty.  It was like I was some sort of, you know, celebrity, walking around. I-I was fascinating to them. There were a lot of attractive women there, Morty, and they-they-they— they all wanted time with me. I had a lot of fun with a lot of young ladies, but I spent so much time there, my interdimensional portal device it's got no charge left, Morty. It's got no charge left. | Jerry | Rick |
| Morty, stay out of this. You are obviously not capable of judging these situations on your own. | Rick | Jerry |
| I mean it's been shot. With a gun. | Morty | Beth |
| No idea what you're talking about. | Morty | Rick |
| Boom! Told you! In your face! He is ruining our child! Wait, what am I celebrating? | Morty | Jerry |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Rick | Jerry |
| Grandpa Rick wouldn't put up with this! | Morty | Summer |
| Oh, man, Rick. What is this place? | Rick | Morty |
| Goldenfold, we're coming out! We just want to talk! | Morty | Rick |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| I don't know. I think like one sixty-fourth of my collars didn't work. It's hard to keep straight now that I have sixty-three other memories of everything. | Rick | Morty |
| Yeah, Rick... I-it's great. Is this the surprise? | Rick | Morty |
| - or sister I said any of this, I'll deny it - | Morty | Rick |
| Well, I'm not calling him that. That's ridiculous. | Rick | Jerry |
| I didn't say my father is perfect, I said his work is important. | Jerry | Beth |
| Sure. Why not? I don’t, I don't know. Y-you know what, Mo— | Morty | Rick |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Jerry | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Morty | Summer |
| Just focus on the mission, all right? | Rick | Morty |
| Seems like you guys need some privacy. I'll, uh -- I'll be in the garage. | Morty | Rick |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Morty | Jerry |
| And then Ethan played guitar and we learned the Seven Contemplations of the Head by singing them. It was really fun. Praise be the head! | Rick | Summer |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Morty | Beth |
| Rick, this really bums me out. It-It's embarrassing to find out these guys don't like us. | Rick | Morty |
| Then what good was the "yes"? | Morty | Beth |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Rick | Beth |
| Whatever. How petty would I have to be to care less about an animal's life than my own ego? | Rick | Beth |
| What? What kind of monster are you? | Rick | Morty |
| I'm looking at her. Thanks for F.D.'ing me up like that. | Rick | Jerry |
| Got some of that mermaid puss! | Morty | Rick |
| I never said I was angry at you. | Rick | Summer |
| What? Why didn't you notify us? | Rick | Beth |
| This better not be a bribe. If I find a single thing out of place in this house, my love of ice cream won't save you. I'll get my jacket. | Rick | Jerry |
| What? Why are you looking at me? You want to go outside? Outside? | Rick | Jerry |
| This article says the reason we weren't involved was... "personality conflicts". | Rick | Morty |
| Rick? Are you far away, or are you inside something? | Rick | Morty |
| You have to turn them on, Morty! The shoes have to be turned on! | Morty | Rick |
| I AM a baby! I’m a baby NOW! | Morty | Jerry |
| Oldest Rick trick in the book. | Morty | Rick |
| Listen, Rick, if you're gonna stay here rent-free and use my son for your stupid science, the least you could do is put a little bit of it to use for the family. You make that dog smart or Morty's grounded! | Rick | Jerry |
| Oh, for crying out—he's got some kind of disability or something. Is that what you want us to say? | Rick | Jerry |
| Are you guys Power Rangers? But only on one small part of your necks? Hey, do those things need batteries? Were they included? Clean up in the fruit isle! Not in a homophobic way though, they're just fruity necklaces is all I was saying. | Rick | Jerry |
| Hey, I can't help if I can't see. | Morty | Rick |
| There is no helicopter and there is no Cervine Institute. | Rick | Jerry |
| What?! Why would you -- Look, we're running late. We have to go. | Morty | Beth |
| What? N-No, I don't want to see your Pog collection. I don't renounce Rick, and I never have. I was just trying to protect my sister. I wanted you to have a normal life. That's something you can't have when Rick shows up. Everything real turns fake. Everything right is wrong. All you know is that you know nothing and he knows everything. And, well -- well, he's not a villain, Summer, but he shouldn't be your hero. He's more like a demon or a super fucked up god. | Rick | Morty |
| But I obviously sort of love you, don't I?  So stop asking and maybe I'll love you more.  Crap, They need me at the horse hospital. | Rick | Beth |
| Oh, my God! He's trying to tell us something.  That is so awesome. | Morty | Summer |
| Yeah, and what's courageous about eating a hot dog? | Rick | Morty |
| Now hold on a second, let’s be rational about this. | Rick | Beth |
### 📉 Unused Features

316/1370 features were unused.

| Feature | Coefficient |
| ------- | ----------- |
| has('em) | 0.0 |
| has(100) | 0.0 |
| has(4) | 0.0 |
| has(47) | 0.0 |
| has(72) | 0.0 |
| has(access) | 0.0 |
| has(afraid) | 0.0 |
| has(ago) | 0.0 |
| has(agreed) | 0.0 |
| has(alan) | 0.0 |
| has(animal) | 0.0 |
| has(anti) | 0.0 |
| has(anymore) | 0.0 |
| has(appointment) | 0.0 |
| has(aroused) | 0.0 |
| has(arrested) | 0.0 |
| has(article) | 0.0 |
| has(ass) | 0.0 |
| ... | ... |
| has(victoria) | 0.0 |
| has(vole) | 0.0 |
| has(wall) | 0.0 |
| has(weaponized) | 0.0 |
| has(wear) | 0.0 |
| has(weekend) | 0.0 |
| has(weep) | 0.0 |
| has(weirder) | 0.0 |
| has(whistle) | 0.0 |
| has(wiggly) | 0.0 |
| has(wildlife) | 0.0 |
| has(wire) | 0.0 |
| has(woman) | 0.0 |
| has(working) | 0.0 |
| has(wristwatch) | 0.0 |
| has(yeller) | 0.0 |
| has(yelling) | 0.0 |
| has(zipped) | 0.0 |
