### 🚀 **LgstcRgrssn_9fs_108**

- 🤖 **Model Type**: 
	<class 'sklearn.linear_model._logistic.LogisticRegression'>
- 📊 **Dataset Used**: 
	_Random_
- 🧠 **Number of Features**: 
	1449
- 🚫 **Unused Features**: 
	82/1449
- ⌛ **Model Train Time**: 
	6.811
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
| Accuracy | 0.873 | 0.555 | 0.515 |
| Macro F1 | 0.862 | 0.425 | 0.405 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.36 | 0.25 | 0.29 |
| Jerry | 0.29 | 0.28 | 0.29 |
| Morty | 0.51 | 0.59 | 0.55 |
| Rick | 0.71 | 0.73 | 0.72 |
| Summer | 0.27 | 0.27 | 0.27 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.36 | 0.29 | 0.32 |
| Jerry | 0.12 | 0.10 | 0.11 |
| Morty | 0.52 | 0.46 | 0.49 |
| Rick | 0.62 | 0.74 | 0.67 |
| Summer | 0.43 | 0.43 | 0.43 |

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
| Nghbhood Degrees - Lemmas (.5decay,4topn,5nghbrs)(glove-wiki-gigaword-50)(Rndm)(-blacklist) |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Uh, yeah, just a few more design notes.  Um, this guy. The, uh... The, uh... | Morty | Rick |
| Uh, what? It was your job, Morty. | Rick | Summer |
| Oh, God, what’s going on now? | Summer | Beth |
| He bails on everybody! He bailed on Mom when she was a kid! He -- He bailed on tiny planet! And in case I never made this clear to you, Summer, he bailed on you. He left you to rot in a world that he ruined because he doesn't care! Because nobody's special to him, Summer, not even himself. So, if you really want your grandpa back, grab a shovel. The one that won't let you down is buried in your backyard! | Summer | Morty |
| I'll cover that bet. I get it. | Rick | Morty |
| Boy, you really got me up against a wall this time, Jerry. | Beth | Rick |
| Because you suck! You've been keeping your lip zipped about it since Grandpa got arrested, but the fact is, you're freaking stoked to bail on him. | Rick | Summer |
| Hey! I said nobody move, buddy! | Morty | Rick |
| Me. I used to wear blue pants. | Beth | Rick |
| But can you help me get to my family? You know, at my house? | Beth | Morty |
| I would have been happy to pay for it, Summer, but they don't exactly sell them at Costco. Besides, there's a larger lesson to be learned here. Get him! | Jerry | Rick |
| Alright! That's enough. You're talking about my species! We understand genocide, we do it sometimes! | Morty | Jerry |
| I am not putting my father in a home! He just came back into my life, and you want to grab him and stuff him under a mattress like last month's Victoria's Secret? | Rick | Beth |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Summer | Jerry |
| You don’t have to be a dick. | Jerry | Rick |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| Hello? Is anybody here?  Mr. President! | Summer | Morty |
| I'm sorry. It's just like the end of "Old Yeller. | Rick | Jerry |
| It's the Citadel of Ricks. All the different Ricks from all the different realities got together to hide here from the government. | Rick | Morty |
| How is praying going to help? | Summer | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| Aw! Oh, my God! He recognizes the other dogs on TV. | Morty | Summer |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Morty | Summer |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Morty | Jerry |
| Hey, what's wrong Morty? Oh, you're worried about your dad, huh? | Beth | Rick |
| Morty, stay out of this. You are obviously not capable of judging these situations on your own. | Rick | Jerry |
| I mean it's been shot. With a gun. | Morty | Beth |
| No idea what you're talking about. | Jerry | Rick |
| Sure thing! And I was kinda hoping that I could get a selfie with you? | Rick | Morty |
| Really? You don't say. You would have used a ghost train?  Hey, everybody, the ghost train guy would have used a ghost train! | Summer | Rick |
| Boom! Told you! In your face! He is ruining our child! Wait, what am I celebrating? | Morty | Jerry |
| Jerry, this was the most romantic weekend I've ever had. | Rick | Beth |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Rick | Jerry |
| Grandpa Rick wouldn't put up with this! | Morty | Summer |
| Goldenfold, we're coming out! We just want to talk! | Summer | Rick |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| I don't know. I think like one sixty-fourth of my collars didn't work. It's hard to keep straight now that I have sixty-three other memories of everything. | Jerry | Morty |
| - or sister I said any of this, I'll deny it - | Morty | Rick |
| Uh, w-why don't you get it Jerry? you're the man of the house and you don't have a job. | Morty | Rick |
| I didn't say my father is perfect, I said his work is important. | Jerry | Beth |
| Sure. Why not? I don’t, I don't know. Y-you know what, Mo— | Morty | Rick |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Jerry | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Rick | Summer |
| Seems like you guys need some privacy. I'll, uh -- I'll be in the garage. | Jerry | Rick |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Rick | Jerry |
| And then Ethan played guitar and we learned the Seven Contemplations of the Head by singing them. It was really fun. Praise be the head! | Rick | Summer |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Morty | Beth |
| Then what good was the "yes"? | Jerry | Beth |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Jerry | Beth |
| What? What kind of monster are you? | Rick | Morty |
| I'm looking at her. Thanks for F.D.'ing me up like that. | Rick | Jerry |
| Huh, what do you know, it's working | Morty | Rick |
| I never said I was angry at you. | Morty | Summer |
| Whoa, whoa, whoa. Hold on, Vance. He said you'd die if you tried to leave. That means there's booby traps. | Morty | Rick |
| What? Why are you looking at me? You want to go outside? Outside? | Beth | Jerry |
| This article says the reason we weren't involved was... "personality conflicts". | Rick | Morty |
| Doesn't feel so good, does it? | Jerry | Morty |
| I AM a baby! I’m a baby NOW! | Beth | Jerry |
| Oldest Rick trick in the book. | Morty | Rick |
| Listen, Rick, if you're gonna stay here rent-free and use my son for your stupid science, the least you could do is put a little bit of it to use for the family. You make that dog smart or Morty's grounded! | Rick | Jerry |
| Alright. I'll-I'll land. I'll land. I'll land. I'll land the thing. I’ll land the thing. Big tough guy all of a sudden. | Jerry | Rick |
| Alan, I'm not proud of what's happening here, but if you keep coming at me, there's gonna be another passenger on that ghost train. | Beth | Rick |
| Hey, I can't help if I can't see. | Beth | Rick |
| There is no helicopter and there is no Cervine Institute. | Beth | Jerry |
| What?! Why would you -- Look, we're running late. We have to go. | Morty | Beth |
| But I obviously sort of love you, don't I?  So stop asking and maybe I'll love you more.  Crap, They need me at the horse hospital. | Jerry | Beth |
| Yeah, and what's courageous about eating a hot dog? | Summer | Morty |
| Now hold on a second, let’s be rational about this. | Rick | Beth |
### 📉 Unused Features

82/1449 features were unused.

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
