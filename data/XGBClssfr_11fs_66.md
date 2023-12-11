### 🚀 **XGBClssfr_11fs_66**

- 🤖 **Model Type**: 
	<class 'xgboost.sklearn.XGBClassifier'>
- 📊 **Dataset Used**: 
	_Random_
- 🧠 **Number of Features**: 
	1355
- 🚫 **Unused Features**: 
	371/1355
- ⌛ **Model Train Time**: 
	13.279
- 💬 **SpaCy Preprocessing Model**: 
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `random_state`: 34
	- `max_depth`: 4
	- `objective`: multi:softmax
	- `num_class`: 5
	- `n_estimators`: 85
	- `min_child_weight`: 1
	- `gamma`: 0.44
	- `subsample`: 0.88
	- `colsample_bytree`: 0.72
	- `reg_lambda`: 1
	- `reg_alpha`: 0.07
	- `learning_rate`: 0.1
	- `alpha`: 0.64
	- `booster`: gbtree
	- `eta`: 0.28
	- `eval_metric`: <function f1_macro at 0x130557310>

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 1.0 | 0.568 | 0.545 |
| Macro F1 | 1.0 | 0.416 | 0.346 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.62 | 0.25 | 0.36 |
| Jerry | 0.21 | 0.17 | 0.19 |
| Morty | 0.49 | 0.69 | 0.57 |
| Rick | 0.67 | 0.76 | 0.71 |
| Summer | 0.40 | 0.18 | 0.25 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.50 | 0.29 | 0.36 |
| Jerry | 0.12 | 0.10 | 0.11 |
| Morty | 0.55 | 0.57 | 0.56 |
| Rick | 0.61 | 0.81 | 0.69 |
| Summer | 0.00 | 0.00 | 0.00 |

### 🧠 Feature Extraction Methods

| Method | Importance |
| ------ | ---------- |
| Nghbhood Degrees - Lemmas (no-decay,1topn,5nghbrs)(glove-twitter-25)(Rndm) | 0.9910 |
| Familial Words & Common Names 1-Gram One Hots | 0.0018 |
| Exclamation Marks Per Sentence | 0.0013 |
| Proportion Of Chars That Are Capitalized | 0.0013 |
| Average Word Length | 0.0011 |
| Dashes Per Sentence | 0.0009 |
| Proportion Of Tokens That Are Stop Words | 0.0007 |
| Topical Proximity - Food (glove-twitter-50) | 0.0006 |
| Topical Proximity - Condescension (fasttext-wiki-news-subwords-300) | 0.0005 |
| Average Tokens Per Sentence | 0.0005 |
| Question Marks Per Sentence | 0.0004 |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Uh, yeah, just a few more design notes.  Um, this guy. The, uh... The, uh... | Jerry | Rick |
| Uh, what? It was your job, Morty. | Rick | Summer |
| Oh, God, what’s going on now? | Summer | Beth |
| He bails on everybody! He bailed on Mom when she was a kid! He -- He bailed on tiny planet! And in case I never made this clear to you, Summer, he bailed on you. He left you to rot in a world that he ruined because he doesn't care! Because nobody's special to him, Summer, not even himself. So, if you really want your grandpa back, grab a shovel. The one that won't let you down is buried in your backyard! | Rick | Morty |
| Don't worry about Jerry. He's gonna be fine.You hear me Jerry? You're gonna be fine! | Beth | Rick |
| Hey! I said nobody move, buddy! | Jerry | Rick |
| Me. I used to wear blue pants. | Morty | Rick |
| But can you help me get to my family? You know, at my house? | Beth | Morty |
| I would have been happy to pay for it, Summer, but they don't exactly sell them at Costco. Besides, there's a larger lesson to be learned here. Get him! | Jerry | Rick |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Morty | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Rick | Jerry |
| You don’t have to be a dick. | Morty | Rick |
| Man that guy is the Red Grin Grumble to pretending he knows what's going on.  Oh you agree, huh?  You like that Red Grin Grumble reference?  Well guess what? I made him up. You really are your father's children. Think for yourselves, don't be sheep. | Jerry | Rick |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| I'm sorry. It's just like the end of "Old Yeller. | Morty | Jerry |
| It's the Citadel of Ricks. All the different Ricks from all the different realities got together to hide here from the government. | Rick | Morty |
| How is praying going to help? | Summer | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Morty | Summer |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Morty | Jerry |
| Morty, stay out of this. You are obviously not capable of judging these situations on your own. | Rick | Jerry |
| I mean it's been shot. With a gun. | Morty | Beth |
| No idea what you're talking about. | Jerry | Rick |
| Sure thing! And I was kinda hoping that I could get a selfie with you? | Rick | Morty |
| Really? You don't say. You would have used a ghost train?  Hey, everybody, the ghost train guy would have used a ghost train! | Jerry | Rick |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Rick | Jerry |
| Grandpa Rick wouldn't put up with this! | Morty | Summer |
| Goldenfold, we're coming out! We just want to talk! | Morty | Rick |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| I don't know. I think like one sixty-fourth of my collars didn't work. It's hard to keep straight now that I have sixty-three other memories of everything. | Rick | Morty |
| - or sister I said any of this, I'll deny it - | Morty | Rick |
| Well, I'm not calling him that. That's ridiculous. | Rick | Jerry |
| I didn't say my father is perfect, I said his work is important. | Jerry | Beth |
| Sure. Why not? I don’t, I don't know. Y-you know what, Mo— | Morty | Rick |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Jerry | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Rick | Summer |
| Just focus on the mission, all right? | Rick | Morty |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Rick | Jerry |
| And then Ethan played guitar and we learned the Seven Contemplations of the Head by singing them. It was really fun. Praise be the head! | Morty | Summer |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Morty | Beth |
| Did he say he never forgets a kid? | Morty | Rick |
| Then what good was the "yes"? | Morty | Beth |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Morty | Beth |
| We’ll take our chances raising her without fancy new jobs outside of a potato-based religion.  And you know what? I’m sick of pretending that we’re together because of the kids in the first place! I married you because you’re the love of my life! | Rick | Jerry |
| I'm looking at her. Thanks for F.D.'ing me up like that. | Rick | Jerry |
| Huh, what do you know, it's working | Jerry | Rick |
| Got some of that mermaid puss! | Summer | Rick |
| I never said I was angry at you. | Morty | Summer |
| What? Why didn't you notify us? | Morty | Beth |
| What? Why are you looking at me? You want to go outside? Outside? | Rick | Jerry |
| This article says the reason we weren't involved was... "personality conflicts". | Rick | Morty |
| Man, Grandpa Rick must have gotten shitfaced. | Morty | Summer |
| Who cares about the  thing you guys are talking about? The whole point of freezing time is to stop giving a fuck. Put a shirt on your dumb dad and let's get this dumb universe rolling. Let's do this thing. | Jerry | Rick |
| I AM a baby! I’m a baby NOW! | Morty | Jerry |
| Oldest Rick trick in the book. | Morty | Rick |
| Listen, Rick, if you're gonna stay here rent-free and use my son for your stupid science, the least you could do is put a little bit of it to use for the family. You make that dog smart or Morty's grounded! | Rick | Jerry |
| Oh, for crying out—he's got some kind of disability or something. Is that what you want us to say? | Rick | Jerry |
| Are you guys Power Rangers? But only on one small part of your necks? Hey, do those things need batteries? Were they included? Clean up in the fruit isle! Not in a homophobic way though, they're just fruity necklaces is all I was saying. | Rick | Jerry |
| Hey, I can't help if I can't see. | Beth | Rick |
| There is no helicopter and there is no Cervine Institute. | Rick | Jerry |
| I don’t know what to say. Summer is doing really well here. | Morty | Beth |
| What?! Why would you -- Look, we're running late. We have to go. | Rick | Beth |
| But I obviously sort of love you, don't I?  So stop asking and maybe I'll love you more.  Crap, They need me at the horse hospital. | Rick | Beth |
| Oh, my God! He's trying to tell us something.  That is so awesome. | Morty | Summer |
| Yeah, and what's courageous about eating a hot dog? | Jerry | Morty |
| Now hold on a second, let’s be rational about this. | Rick | Beth |
### 📉 Individual Feature Importances

| Feature | Importance |
| ------- | ---------- |
| deg_of_presence(morty)_norm | 0.014775383286178112 |
| deg_of_presence(visualization)_norm | 0.011431975290179253 |
| deg_of_presence(rick)_norm | 0.0076606906950473785 |
| deg_of_presence(nelly)_norm | 0.00734155485406518 |
| deg_of_presence(cronenberg)_norm | 0.006593062076717615 |
| deg_of_presence(saget)_norm | 0.006558060180395842 |
| deg_of_presence(marriage)_norm | 0.006259429734200239 |
| deg_of_presence(vincent)_norm | 0.0061722989194095135 |
| deg_of_presence(patriarch)_norm | 0.004378678277134895 |
| deg_of_presence(garage)_norm | 0.00410905247554183 |
| deg_of_presence(arbitrary)_norm | 0.004026189912110567 |
| deg_of_presence(machine)_norm | 0.0040224106051027775 |
| deg_of_presence(student)_norm | 0.0039942022413015366 |
| deg_of_presence(smirky)_norm | 0.003983804490417242 |
| deg_of_presence(cycle)_norm | 0.003947474993765354 |
| deg_of_presence(decker)_norm | 0.003913551103323698 |
| deg_of_presence(domination)_norm | 0.003879980882629752 |
| deg_of_presence(nancy)_norm | 0.0038722618483006954 |
| ... | ... |
| deg_of_presence(scotch)_norm | 0.0 |
| deg_of_presence(nice)_norm | 0.0 |
| deg_of_presence(night)_norm | 0.0 |
| deg_of_presence(dollar)_norm | 0.0 |
| deg_of_presence(hair)_norm | 0.0 |
| deg_of_presence(naked)_norm | 0.0 |
| deg_of_presence(defy)_norm | 0.0 |
| deg_of_presence(definitely)_norm | 0.0 |
| deg_of_presence(somebody)_norm | 0.0 |
| deg_of_presence(solid)_norm | 0.0 |
| deg_of_presence(snowball)_norm | 0.0 |
| deg_of_presence(crowd)_norm | 0.0 |
| deg_of_presence(hate)_norm | 0.0 |
| deg_of_presence(cry)_norm | 0.0 |
| deg_of_presence(hard)_norm | 0.0 |
| deg_of_presence(happen)_norm | 0.0 |
| deg_of_presence(sleepy)_norm | 0.0 |
| deg_of_presence(murderous)_norm | 0.0 |
| deg_of_presence(handle)_norm | 0.0 |
| deg_of_presence(sit)_norm | 0.0 |
| deg_of_presence(sister)_norm | 0.0 |
| deg_of_presence(day)_norm | 0.0 |
| deg_of_presence(dead)_norm | 0.0 |
| deg_of_presence(deal)_norm | 0.0 |
| deg_of_presence(mysterious)_norm | 0.0 |
| deg_of_presence(deep)_norm | 0.0 |
| deg_of_presence(sick)_norm | 0.0 |
| deg_of_presence(deer)_norm | 0.0 |
| deg_of_presence(hand)_norm | 0.0 |
| deg_of_presence(joke)_norm | 0.0 |
