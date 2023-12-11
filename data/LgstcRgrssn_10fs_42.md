### 🚀 **LgstcRgrssn_10fs_42**

- 🤖 **Model Type**: 
	<class 'sklearn.linear_model._logistic.LogisticRegression'>
- 📊 **Dataset Used**: 
	_Random_
- 🧠 **Number of Features**: 
	1347
- 🚫 **Unused Features**: 
	1095/1347
- ⌛ **Model Train Time**: 
	37.038
- 💬 **SpaCy Preprocessing Model**: 
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `penalty`: elasticnet
	- `C`: 1.8
	- `solver`: saga
	- `random_state`: 34
	- `max_iter`: 1400
	- `l1_ratio`: 0.5

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 0.651 | 0.568 | 0.525 |
| Macro F1 | 0.526 | 0.42 | 0.366 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.45 | 0.25 | 0.32 |
| Jerry | 0.29 | 0.11 | 0.16 |
| Morty | 0.44 | 0.56 | 0.49 |
| Rick | 0.65 | 0.81 | 0.72 |
| Summer | 0.75 | 0.27 | 0.40 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.67 | 0.14 | 0.24 |
| Jerry | 0.57 | 0.40 | 0.47 |
| Morty | 0.41 | 0.50 | 0.45 |
| Rick | 0.59 | 0.79 | 0.67 |
| Summer | 0.00 | 0.00 | 0.00 |

### 🧠 Feature Extraction Methods

| Method |
| ------ |
| Total Sentence Count |
| Average Tokens Per Sentence |
| Average Word Length |
| Question Marks Per Sentence |
| Exclamation Marks Per Sentence |
| Dashes Per Sentence |
| Familial Words & Common Names 1-Gram One Hots |
| Proportion Of Tokens That Are Stop Words |
| Proportion Of Chars That Are Capitalized |
| Nghbhood Degrees - Lemmas (.5decay,no-topn,5nghbrs)(glove-twitter-25)(Rndm)(-blacklist) |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Uh, what? It was your job, Morty. | Rick | Summer |
| Oh, God, what’s going on now? | Morty | Beth |
| He bails on everybody! He bailed on Mom when she was a kid! He -- He bailed on tiny planet! And in case I never made this clear to you, Summer, he bailed on you. He left you to rot in a world that he ruined because he doesn't care! Because nobody's special to him, Summer, not even himself. So, if you really want your grandpa back, grab a shovel. The one that won't let you down is buried in your backyard! | Rick | Morty |
| Don't worry about Jerry. He's gonna be fine.You hear me Jerry? You're gonna be fine! | Morty | Rick |
| I'll cover that bet. I get it. | Rick | Morty |
| Boy, you really got me up against a wall this time, Jerry. | Beth | Rick |
| Aw, geez. Okay. I guess I can skip history. What about Frank? I mean, shouldn't you unfreeze him? | Rick | Morty |
| Hey! I said nobody move, buddy! | Morty | Rick |
| But can you help me get to my family? You know, at my house? | Beth | Morty |
| I would have been happy to pay for it, Summer, but they don't exactly sell them at Costco. Besides, there's a larger lesson to be learned here. Get him! | Beth | Rick |
| Alright! That's enough. You're talking about my species! We understand genocide, we do it sometimes! | Morty | Jerry |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Rick | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Beth | Jerry |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| I'm sorry. It's just like the end of "Old Yeller. | Rick | Jerry |
| It's the Citadel of Ricks. All the different Ricks from all the different realities got together to hide here from the government. | Rick | Morty |
| How is praying going to help? | Summer | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Morty | Summer |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Morty | Jerry |
| Hey, what's wrong Morty? Oh, you're worried about your dad, huh? | Morty | Rick |
| Morty, stay out of this. You are obviously not capable of judging these situations on your own. | Rick | Jerry |
| I mean it's been shot. With a gun. | Rick | Beth |
| Sure thing! And I was kinda hoping that I could get a selfie with you? | Rick | Morty |
| Boom! Told you! In your face! He is ruining our child! Wait, what am I celebrating? | Morty | Jerry |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Rick | Jerry |
| Grandpa Rick wouldn't put up with this! | Morty | Summer |
| Goldenfold, we're coming out! We just want to talk! | Morty | Rick |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| I don't know. I think like one sixty-fourth of my collars didn't work. It's hard to keep straight now that I have sixty-three other memories of everything. | Rick | Morty |
| - or sister I said any of this, I'll deny it - | Morty | Rick |
| Uh, w-why don't you get it Jerry? you're the man of the house and you don't have a job. | Morty | Rick |
| Well, I'm not calling him that. That's ridiculous. | Rick | Jerry |
| I didn't say my father is perfect, I said his work is important. | Jerry | Beth |
| Sure. Why not? I don’t, I don't know. Y-you know what, Mo— | Morty | Rick |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Rick | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Rick | Summer |
| Just focus on the mission, all right? | Rick | Morty |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Rick | Jerry |
| And then Ethan played guitar and we learned the Seven Contemplations of the Head by singing them. It was really fun. Praise be the head! | Rick | Summer |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Morty | Beth |
| Did he say he never forgets a kid? | Morty | Rick |
| Rick, this really bums me out. It-It's embarrassing to find out these guys don't like us. | Rick | Morty |
| Yup, it really makes you appreciate how fickle the universe can be.   One minute you're falling off a roof for six months, the next minute, bam! | Morty | Rick |
| Then what good was the "yes"? | Jerry | Beth |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Rick | Beth |
| Whatever. How petty would I have to be to care less about an animal's life than my own ego? | Rick | Beth |
| Got some of that mermaid puss! | Morty | Rick |
| I never said I was angry at you. | Morty | Summer |
| What? Why didn't you notify us? | Rick | Beth |
| This better not be a bribe. If I find a single thing out of place in this house, my love of ice cream won't save you. I'll get my jacket. | Beth | Jerry |
| What? Why are you looking at me? You want to go outside? Outside? | Morty | Jerry |
| This article says the reason we weren't involved was... "personality conflicts". | Rick | Morty |
| I AM a baby! I’m a baby NOW! | Morty | Jerry |
| Oldest Rick trick in the book. | Morty | Rick |
| Listen, Rick, if you're gonna stay here rent-free and use my son for your stupid science, the least you could do is put a little bit of it to use for the family. You make that dog smart or Morty's grounded! | Rick | Jerry |
| Oh, for crying out—he's got some kind of disability or something. Is that what you want us to say? | Rick | Jerry |
| Are you guys Power Rangers? But only on one small part of your necks? Hey, do those things need batteries? Were they included? Clean up in the fruit isle! Not in a homophobic way though, they're just fruity necklaces is all I was saying. | Rick | Jerry |
| Hey, I can't help if I can't see. | Jerry | Rick |
| There is no helicopter and there is no Cervine Institute. | Beth | Jerry |
| What?! Why would you -- Look, we're running late. We have to go. | Morty | Beth |
| What? N-No, I don't want to see your Pog collection. I don't renounce Rick, and I never have. I was just trying to protect my sister. I wanted you to have a normal life. That's something you can't have when Rick shows up. Everything real turns fake. Everything right is wrong. All you know is that you know nothing and he knows everything. And, well -- well, he's not a villain, Summer, but he shouldn't be your hero. He's more like a demon or a super fucked up god. | Rick | Morty |
| But I obviously sort of love you, don't I?  So stop asking and maybe I'll love you more.  Crap, They need me at the horse hospital. | Jerry | Beth |
| Oh, my God! He's trying to tell us something.  That is so awesome. | Morty | Summer |
| Yeah, and what's courageous about eating a hot dog? | Jerry | Morty |
| Now hold on a second, let’s be rational about this. | Rick | Beth |
### 📉 Unused Features

1095/1347 features were unused.

| Feature | Coefficient |
| ------- | ----------- |
| avg_tokens_per_sentence | 0.0 |
| deg_of_presence(abandon)_norm | 0.0 |
| deg_of_presence(abide)_norm | 0.0 |
| deg_of_presence(ability)_norm | 0.0 |
| deg_of_presence(able)_norm | 0.0 |
| deg_of_presence(absolutely)_norm | 0.0 |
| deg_of_presence(accomplish)_norm | 0.0 |
| deg_of_presence(ace)_norm | 0.0 |
| deg_of_presence(actually)_norm | 0.0 |
| deg_of_presence(add)_norm | 0.0 |
| deg_of_presence(adult)_norm | 0.0 |
| deg_of_presence(advice)_norm | 0.0 |
| deg_of_presence(affair)_norm | 0.0 |
| deg_of_presence(age)_norm | 0.0 |
| deg_of_presence(agony)_norm | 0.0 |
| deg_of_presence(ahhh)_norm | 0.0 |
| deg_of_presence(aid)_norm | 0.0 |
| deg_of_presence(air)_norm | 0.0 |
| ... | ... |
| deg_of_presence(wrong)_norm | 0.0 |
| deg_of_presence(y)_norm | 0.0 |
| deg_of_presence(yank)_norm | 0.0 |
| deg_of_presence(yard)_norm | 0.0 |
| deg_of_presence(year)_norm | 0.0 |
| deg_of_presence(young)_norm | 0.0 |
| deg_of_presence(zero)_norm | 0.0 |
| has(grampa) | 0.0 |
| has(grandpa) | 0.0 |
| has(grandson) | 0.0 |
| has(jessica) | 0.0 |
| has(married) | 0.0 |
| has(mother) | 0.0 |
| has(sister) | 0.0 |
| has(smith) | 0.0 |
| has(son) | 0.0 |
| has(um) | 0.0 |
| question_marks_per_sentence | 0.0 |
