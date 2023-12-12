### 🚀 **GrdntBstngClssfr_11fs_4**

- 🤖 **Model Type**:
	<class 'sklearn.ensemble._gb.GradientBoostingClassifier'>
- 📊 **Dataset Used**:
	_Random_
- 🧠 **Number of Features**:
	1348
- 🚫 **Unused Features**:
	12/1348
- ⌛ **Model Train Time**:
	99.876
- 💬 **SpaCy Preprocessing Model**:
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `n_estimators`: 51
	- `learning_rate`: 0.08
	- `max_depth`: 8
	- `random_state`: 34

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 1.0 | 0.548 | 0.495 |
| Macro F1 | 1.0 | 0.395 | 0.297 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.60 | 0.30 | 0.40 |
| Jerry | 0.18 | 0.11 | 0.14 |
| Morty | 0.50 | 0.59 | 0.54 |
| Rick | 0.64 | 0.76 | 0.70 |
| Summer | 0.22 | 0.18 | 0.20 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.33 | 0.14 | 0.20 |
| Jerry | 0.09 | 0.10 | 0.10 |
| Morty | 0.54 | 0.50 | 0.52 |
| Rick | 0.59 | 0.79 | 0.67 |
| Summer | 0.00 | 0.00 | 0.00 |

### 🧠 Feature Extraction Methods

| Method | Importance |
| ------ | ---------- |
| Nghbhood Degrees - Lemmas (.5decay,1topn,5nghbrs)(glove-twitter-25)(Rndm)(-blacklist) | 0.9615 |
| Familial Words & Common Names 1-Gram One Hots | 0.0117 |
| Exclamation Marks Per Sentence | 0.0068 |
| Dashes Per Sentence | 0.0054 |
| Average Word Length | 0.0053 |
| Proportion Of Tokens That Are Stop Words | 0.0038 |
| Proportion Of Chars That Are Capitalized | 0.0032 |
| Topical Proximity - Intoxication (glove-twitter-50) | 0.0011 |
| Question Marks Per Sentence | 0.0006 |
| Average Tokens Per Sentence | 0.0006 |
| Total Sentence Count | 0.0000 |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Uh, what? It was your job, Morty. | Rick | Summer |
| Oh, God, what’s going on now? | Summer | Beth |
| He bails on everybody! He bailed on Mom when she was a kid! He -- He bailed on tiny planet! And in case I never made this clear to you, Summer, he bailed on you. He left you to rot in a world that he ruined because he doesn't care! Because nobody's special to him, Summer, not even himself. So, if you really want your grandpa back, grab a shovel. The one that won't let you down is buried in your backyard! | Summer | Morty |
| I told the both of you school is stupid. It's not how you learn things. Morty's a gifted child. He has a special mind. That's why he's my little helper. He's like me. He's gonna be doing great science stuff later in his life. He's too smart for school. He needs to keep hanging out and helping me. | Jerry | Rick |
| Don't worry about Jerry. He's gonna be fine.You hear me Jerry? You're gonna be fine! | Beth | Rick |
| Hey! I said nobody move, buddy! | Jerry | Rick |
| Me. I used to wear blue pants. | Beth | Rick |
| But can you help me get to my family? You know, at my house? | Jerry | Morty |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Rick | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Rick | Jerry |
| You don’t have to be a dick. | Morty | Rick |
| Man that guy is the Red Grin Grumble to pretending he knows what's going on.  Oh you agree, huh?  You like that Red Grin Grumble reference?  Well guess what? I made him up. You really are your father's children. Think for yourselves, don't be sheep. | Jerry | Rick |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| I'm sorry. It's just like the end of "Old Yeller. | Rick | Jerry |
| How is praying going to help? | Rick | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| Aw! Oh, my God! He recognizes the other dogs on TV. | Rick | Summer |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Morty | Summer |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Morty | Jerry |
| Morty, stay out of this. You are obviously not capable of judging these situations on your own. | Rick | Jerry |
| I mean it's been shot. With a gun. | Morty | Beth |
| No idea what you're talking about. | Jerry | Rick |
| Sure thing! And I was kinda hoping that I could get a selfie with you? | Rick | Morty |
| Boom! Told you! In your face! He is ruining our child! Wait, what am I celebrating? | Morty | Jerry |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Rick | Jerry |
| Grandpa Rick wouldn't put up with this! | Morty | Summer |
| Goldenfold, we're coming out! We just want to talk! | Beth | Rick |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| I don't know. I think like one sixty-fourth of my collars didn't work. It's hard to keep straight now that I have sixty-three other memories of everything. | Rick | Morty |
| - or sister I said any of this, I'll deny it - | Morty | Rick |
| Uh, w-why don't you get it Jerry? you're the man of the house and you don't have a job. | Morty | Rick |
| Man, he sure says "bitch" a lot! | Jerry | Morty |
| Well, I'm not calling him that. That's ridiculous. | Rick | Jerry |
| I didn't say my father is perfect, I said his work is important. | Summer | Beth |
| Sure. Why not? I don’t, I don't know. Y-you know what, Mo— | Jerry | Rick |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Morty | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Rick | Summer |
| Just focus on the mission, all right? | Rick | Morty |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Rick | Jerry |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Morty | Beth |
| Did he say he never forgets a kid? | Jerry | Rick |
| Then what good was the "yes"? | Jerry | Beth |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Summer | Beth |
| Whatever. How petty would I have to be to care less about an animal's life than my own ego? | Rick | Beth |
| We’ll take our chances raising her without fancy new jobs outside of a potato-based religion.  And you know what? I’m sick of pretending that we’re together because of the kids in the first place! I married you because you’re the love of my life! | Rick | Jerry |
| I'm looking at her. Thanks for F.D.'ing me up like that. | Rick | Jerry |
| I never said I was angry at you. | Morty | Summer |
| Whoa, whoa, whoa. Hold on, Vance. He said you'd die if you tried to leave. That means there's booby traps. | Morty | Rick |
| Yikes. Yeah, things did feel less diverse in there. | Morty | Rick |
| What? Why are you looking at me? You want to go outside? Outside? | Rick | Jerry |
| Ow! Ow! You're tugging me too hard! | Rick | Morty |
| This article says the reason we weren't involved was... "personality conflicts". | Rick | Morty |
| Man, Grandpa Rick must have gotten shitfaced. | Morty | Summer |
| And they'll fall right out of mine. I've done this too many times, Morty. I mean, you're young. Y-y-you've got your whole life ahead of you, and your anal cavity is still taut, yet malleable. You got to do it for grandpa, Morty. Y-  you've got to put these seeds inside your butt. | Summer | Rick |
| Who cares about the  thing you guys are talking about? The whole point of freezing time is to stop giving a fuck. Put a shirt on your dumb dad and let's get this dumb universe rolling. Let's do this thing. | Summer | Rick |
| Go in the waiting room, Dad. | Morty | Beth |
| I AM a baby! I’m a baby NOW! | Morty | Jerry |
| Oldest Rick trick in the book. | Morty | Rick |
| Listen, Rick, if you're gonna stay here rent-free and use my son for your stupid science, the least you could do is put a little bit of it to use for the family. You make that dog smart or Morty's grounded! | Rick | Jerry |
| Oh, for crying out—he's got some kind of disability or something. Is that what you want us to say? | Rick | Jerry |
| Are you guys Power Rangers? But only on one small part of your necks? Hey, do those things need batteries? Were they included? Clean up in the fruit isle! Not in a homophobic way though, they're just fruity necklaces is all I was saying. | Rick | Jerry |
| Hey, I can't help if I can't see. | Beth | Rick |
| There is no helicopter and there is no Cervine Institute. | Morty | Jerry |
| I don’t know what to say. Summer is doing really well here. | Morty | Beth |
| But.. she was trying to kill us! | Rick | Morty |
| What? N-No, I don't want to see your Pog collection. I don't renounce Rick, and I never have. I was just trying to protect my sister. I wanted you to have a normal life. That's something you can't have when Rick shows up. Everything real turns fake. Everything right is wrong. All you know is that you know nothing and he knows everything. And, well -- well, he's not a villain, Summer, but he shouldn't be your hero. He's more like a demon or a super fucked up god. | Summer | Morty |
| Oh, my God! He's trying to tell us something.  That is so awesome. | Rick | Summer |
| Yeah, and what's courageous about eating a hot dog? | Rick | Morty |
| Now hold on a second, let’s be rational about this. | Rick | Beth |
### 📉 Individual Feature Importances

| Feature | Importance |
| ------- | ---------- |
| deg_of_presence(morty)_norm | 0.08554166490610962 |
| deg_of_presence(nelly)_norm | 0.06075939109171917 |
| deg_of_presence(complete)_norm | 0.01285899178940085 |
| deg_of_presence(pentagon)_norm | 0.012496609422101405 |
| deg_of_presence(calypso)_norm | 0.011932187278145445 |
| deg_of_presence(turd)_norm | 0.011768602546327911 |
| deg_of_presence(hologram)_norm | 0.011681180800492632 |
| deg_of_presence(kitten)_norm | 0.011546175574958562 |
| deg_of_presence(grandson)_norm | 0.011336705654281546 |
| deg_of_presence(decker)_norm | 0.010590435252646952 |
| deg_of_presence(smith)_norm | 0.009920504889934472 |
| has(jerry) | 0.009900883119685974 |
| deg_of_presence(trash)_norm | 0.009457178640138564 |
| deg_of_presence(beth)_norm | 0.009376360692008229 |
| deg_of_presence(amulet)_norm | 0.008280376889875696 |
| deg_of_presence(husband)_norm | 0.008271835958426402 |
| deg_of_presence(knob)_norm | 0.008232035380533095 |
| deg_of_presence(hotel)_norm | 0.00801406957120472 |
| ... | ... |
| deg_of_presence(replace)_norm | 2.6754822572855916e-08 |
| deg_of_presence(far)_norm | 2.2793771086670147e-08 |
| deg_of_presence(friend)_norm | 2.0872470151482215e-08 |
| deg_of_presence(wrong)_norm | 1.9462763659948358e-08 |
| deg_of_presence(gonna)_norm | 1.4318219968864563e-08 |
| deg_of_presence(try)_norm | 1.2076291985219732e-08 |
| has(uh) | 1.0906094374904737e-08 |
| deg_of_presence(yard)_norm | 8.954320717385202e-09 |
| deg_of_presence(huge)_norm | 7.451004095704821e-09 |
| deg_of_presence(angry)_norm | 6.529628218704021e-09 |
| deg_of_presence(fast)_norm | 3.79628225370385e-09 |
| deg_of_presence(long)_norm | 3.540486205849309e-09 |
| has(smith) | 2.378431210643395e-09 |
| deg_of_presence(close)_norm | 1.173186286639503e-09 |
| deg_of_presence(easy)_norm | 6.610136930306914e-10 |
| has(father) | 4.988120662752207e-10 |
| deg_of_presence(set)_norm | 3.110544920800328e-10 |
| deg_of_presence(answer)_norm | 6.004223829427437e-12 |
| has(wong) | 0.0 |
| has(sister) | 0.0 |
| has(son) | 0.0 |
| has(grampa) | 0.0 |
| has(parents) | 0.0 |
| has(mother) | 0.0 |
| deg_of_presence(running)_norm | 0.0 |
| has(mom) | 0.0 |
| has(honey) | 0.0 |
| has(grandson) | 0.0 |
| has(daughter) | 0.0 |
| has(married) | 0.0 |
