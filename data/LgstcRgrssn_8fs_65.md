### 🚀 **LgstcRgrssn_8fs_65**

- 🤖 **Model Type**: 
	<class 'sklearn.linear_model._logistic.LogisticRegression'>
- 📊 **Dataset Used**: 
	_Random_
- 🧠 **Number of Features**: 
	110
- 🚫 **Unused Features**: 
	82/110
- ⌛ **Model Train Time**: 
	0.189
- 💬 **SpaCy Preprocessing Model**: 
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `penalty`: l2
	- `C`: 1.94
	- `solver`: lbfgs
	- `random_state`: 36
	- `max_iter`: 1400

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 0.57 | 0.516 | 0.525 |
| Macro F1 | 0.425 | 0.36 | 0.355 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.67 | 0.20 | 0.31 |
| Jerry | 0.50 | 0.06 | 0.10 |
| Morty | 0.37 | 0.53 | 0.44 |
| Rick | 0.57 | 0.76 | 0.65 |
| Summer | 1.00 | 0.18 | 0.31 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 1.00 | 0.14 | 0.25 |
| Jerry | 0.33 | 0.10 | 0.15 |
| Morty | 0.52 | 0.50 | 0.51 |
| Rick | 0.52 | 0.83 | 0.64 |
| Summer | 0.50 | 0.14 | 0.22 |

### 🧠 Feature Extraction Methods

| Method |
| ------ |
| Average Word Length |
| Question Marks Per Sentence |
| Exclamation Marks Per Sentence |
| Dashes Per Sentence |
| Familial Words & Common Names 1-Gram One Hots |
| Hand-Selected POS-Tag N-Gram Counts |
| Proportion Of Tokens That Are Stop Words |
| Proportion Of Chars That Are Capitalized |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Uh, yeah, just a few more design notes.  Um, this guy. The, uh... The, uh... | Morty | Rick |
| Uh, what? It was your job, Morty. | Rick | Summer |
| Oh, God, what’s going on now? | Morty | Beth |
| He bails on everybody! He bailed on Mom when she was a kid! He -- He bailed on tiny planet! And in case I never made this clear to you, Summer, he bailed on you. He left you to rot in a world that he ruined because he doesn't care! Because nobody's special to him, Summer, not even himself. So, if you really want your grandpa back, grab a shovel. The one that won't let you down is buried in your backyard! | Rick | Morty |
| That's my one-armed man! I'm not driven by avenging my dead family, Morty! That was fake. I-I-I'm driven by finding that McNugget sauce. | Morty | Rick |
| I'll cover that bet. I get it. | Rick | Morty |
| Boy, you really got me up against a wall this time, Jerry. | Beth | Rick |
| Aw, geez. Okay. I guess I can skip history. What about Frank? I mean, shouldn't you unfreeze him? | Rick | Morty |
| Hey! I said nobody move, buddy! | Morty | Rick |
| Alright! That's enough. You're talking about my species! We understand genocide, we do it sometimes! | Rick | Jerry |
| Come on, Morty! We got to get the hell out of here! | Morty | Rick |
| I am not putting my father in a home! He just came back into my life, and you want to grab him and stuff him under a mattress like last month's Victoria's Secret? | Morty | Beth |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Rick | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Beth | Jerry |
| I don't know, Rick. I can't leave school again. | Rick | Morty |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| They're just robots, Morty! It's okay to shoot them! They're robots! | Morty | Rick |
| I'm sorry. It's just like the end of "Old Yeller. | Rick | Jerry |
| Is there coffee? Hey, Morty, can you be a pal? Grandpa left his coffee maker on the ship. Y-You know, the French press thing? | Morty | Rick |
| It's the Citadel of Ricks. All the different Ricks from all the different realities got together to hide here from the government. | Rick | Morty |
| How is praying going to help? | Rick | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| Aw! Oh, my God! He recognizes the other dogs on TV. | Morty | Summer |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Rick | Summer |
| Hey, what's wrong Morty? Oh, you're worried about your dad, huh? | Morty | Rick |
| Morty, stay out of this. You are obviously not capable of judging these situations on your own. | Rick | Jerry |
| I mean it's been shot. With a gun. | Rick | Beth |
| Boom! Told you! In your face! He is ruining our child! Wait, what am I celebrating? | Morty | Jerry |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Rick | Jerry |
| Grandpa Rick wouldn't put up with this! | Morty | Summer |
| Goldenfold, we're coming out! We just want to talk! | Morty | Rick |
| Uh, the adventure is the favor, Morty. Me sleeping on these linens is the favor. I mean, w-w-w-what--what are we vindicating? Comfort? | Morty | Rick |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| I don't know. I think like one sixty-fourth of my collars didn't work. It's hard to keep straight now that I have sixty-three other memories of everything. | Rick | Morty |
| - or sister I said any of this, I'll deny it - | Morty | Rick |
| Uh, w-why don't you get it Jerry? you're the man of the house and you don't have a job. | Morty | Rick |
| Well, I'm not calling him that. That's ridiculous. | Rick | Jerry |
| I didn't say my father is perfect, I said his work is important. | Jerry | Beth |
| Sure. Why not? I don’t, I don't know. Y-you know what, Mo— | Morty | Rick |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Rick | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Rick | Summer |
| I don't care about Jessica! Y-Yyyyyyyyyyou— | Rick | Morty |
| Just focus on the mission, all right? | Rick | Morty |
| Seems like you guys need some privacy. I'll, uh -- I'll be in the garage. | Morty | Rick |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Morty | Jerry |
| And then Ethan played guitar and we learned the Seven Contemplations of the Head by singing them. It was really fun. Praise be the head! | Rick | Summer |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Morty | Beth |
| Did he say he never forgets a kid? | Morty | Rick |
| Rick, this really bums me out. It-It's embarrassing to find out these guys don't like us. | Rick | Morty |
| Then what good was the "yes"? | Morty | Beth |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Rick | Beth |
| Whatever. How petty would I have to be to care less about an animal's life than my own ego? | Rick | Beth |
| We’ll take our chances raising her without fancy new jobs outside of a potato-based religion.  And you know what? I’m sick of pretending that we’re together because of the kids in the first place! I married you because you’re the love of my life! | Rick | Jerry |
| I'm looking at her. Thanks for F.D.'ing me up like that. | Rick | Jerry |
| Got some of that mermaid puss! | Morty | Rick |
| I never said I was angry at you. | Rick | Summer |
| What? Why didn't you notify us? | Morty | Beth |
| This better not be a bribe. If I find a single thing out of place in this house, my love of ice cream won't save you. I'll get my jacket. | Rick | Jerry |
| What? Why are you looking at me? You want to go outside? Outside? | Morty | Jerry |
| This article says the reason we weren't involved was... "personality conflicts". | Rick | Morty |
| Rick? Are you far away, or are you inside something? | Rick | Morty |
| You have to turn them on, Morty! The shoes have to be turned on! | Morty | Rick |
| I AM a baby! I’m a baby NOW! | Morty | Jerry |
| Oldest Rick trick in the book. | Morty | Rick |
| Listen, Rick, if you're gonna stay here rent-free and use my son for your stupid science, the least you could do is put a little bit of it to use for the family. You make that dog smart or Morty's grounded! | Rick | Jerry |
| Oh, for crying out—he's got some kind of disability or something. Is that what you want us to say? | Rick | Jerry |
| Are you guys Power Rangers? But only on one small part of your necks? Hey, do those things need batteries? Were they included? Clean up in the fruit isle! Not in a homophobic way though, they're just fruity necklaces is all I was saying. | Rick | Jerry |
| There is no helicopter and there is no Cervine Institute. | Rick | Jerry |
| What?! Why would you -- Look, we're running late. We have to go. | Morty | Beth |
| What? N-No, I don't want to see your Pog collection. I don't renounce Rick, and I never have. I was just trying to protect my sister. I wanted you to have a normal life. That's something you can't have when Rick shows up. Everything real turns fake. Everything right is wrong. All you know is that you know nothing and he knows everything. And, well -- well, he's not a villain, Summer, but he shouldn't be your hero. He's more like a demon or a super fucked up god. | Rick | Morty |
| But I obviously sort of love you, don't I?  So stop asking and maybe I'll love you more.  Crap, They need me at the horse hospital. | Rick | Beth |
| Oh, my God! He's trying to tell us something.  That is so awesome. | Rick | Summer |
| Yeah, and what's courageous about eating a hot dog? | Rick | Morty |
| Now hold on a second, let’s be rational about this. | Rick | Beth |
### 📉 Unused Features

82/110 features were unused.

| Feature | Coefficient |
| ------- | ----------- |
| 'ADJ NOUN PUNCT' | 0.0 |
| 'ADJ NOUN' | 0.0 |
| 'ADJ PUNCT' | 0.0 |
| 'ADP ADJ PUNCT' | 0.0 |
| 'ADP DET NOUN' | 0.0 |
| 'ADP DET' | 0.0 |
| 'ADP NOUN PUNCT' | 0.0 |
| 'ADP PRON ADV' | 0.0 |
| 'ADP PRON NOUN' | 0.0 |
| 'ADP PRON' | 0.0 |
| 'ADP PROPN PUNCT' | 0.0 |
| 'ADP PUNCT' | 0.0 |
| 'ADP VERB' | 0.0 |
| 'ADV ADV SCONJ' | 0.0 |
| 'ADV ADV' | 0.0 |
| 'ADV PUNCT' | 0.0 |
| 'ADV VERB' | 0.0 |
| 'AUX ADP PRON' | 0.0 |
| ... | ... |
| 'PUNCT PRON AUX' | 0.0 |
| 'PUNCT PRON PROPN' | 0.0 |
| 'PUNCT PRON VERB' | 0.0 |
| 'PUNCT PRON' | 0.0 |
| 'PUNCT PROPN PUNCT' | 0.0 |
| 'PUNCT PROPN' | 0.0 |
| 'PUNCT VERB' | 0.0 |
| 'SCONJ PRON' | 0.0 |
| 'VERB ADJ NOUN' | 0.0 |
| 'VERB ADP' | 0.0 |
| 'VERB ADV SCONJ' | 0.0 |
| 'VERB PART PUNCT' | 0.0 |
| 'VERB PART VERB' | 0.0 |
| 'VERB PRON ADV' | 0.0 |
| 'VERB PRON NOUN' | 0.0 |
| 'VERB PRON' | 0.0 |
| 'VERB PROPN' | 0.0 |
| 'VERB PUNCT' | 0.0 |
