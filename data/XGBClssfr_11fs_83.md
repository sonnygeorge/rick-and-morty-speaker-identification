### 🚀 **XGBClssfr_11fs_83**

- 🤖 **Model Type**: 
	<class 'xgboost.sklearn.XGBClassifier'>
- 📊 **Dataset Used**: 
	_Random_
- 🧠 **Number of Features**: 
	1381
- 🚫 **Unused Features**: 
	202/1381
- ⌛ **Model Train Time**: 
	27.312
- 💬 **SpaCy Preprocessing Model**: 
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `random_state`: 48
	- `max_depth`: 4
	- `objective`: multi:softmax
	- `num_class`: 5
	- `n_estimators`: 164
	- `min_child_weight`: 1
	- `gamma`: 0.05
	- `subsample`: 0.8
	- `colsample_bytree`: 0.88
	- `reg_lambda`: 1
	- `reg_alpha`: 0.12
	- `learning_rate`: 0.09
	- `alpha`: 2.16
	- `booster`: gbtree
	- `eta`: 0.48
	- `eval_metric`: map

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 1.0 | 0.574 | 0.505 |
| Macro F1 | 1.0 | 0.402 | 0.298 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.67 | 0.20 | 0.31 |
| Jerry | 0.27 | 0.17 | 0.21 |
| Morty | 0.47 | 0.62 | 0.53 |
| Rick | 0.68 | 0.81 | 0.74 |
| Summer | 0.29 | 0.18 | 0.22 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.33 | 0.14 | 0.20 |
| Jerry | 0.12 | 0.10 | 0.11 |
| Morty | 0.50 | 0.50 | 0.50 |
| Rick | 0.59 | 0.81 | 0.68 |
| Summer | 0.00 | 0.00 | 0.00 |

### 🧠 Feature Extraction Methods

| Method | Importance |
| ------ | ---------- |
| Nghbhood Degrees - Lemmas (.5decay,1topn,5nghbrs)(glove-twitter-25)(Rndm) | 0.9695 |
| Average Root Verb Embedding (glove-twitter-25) | 0.0175 |
| Familial Words & Common Names 1-Gram Counts | 0.0074 |
| Exclamation Marks Per Sentence | 0.0013 |
| Dashes Per Sentence | 0.0011 |
| Average Word Length | 0.0008 |
| Proportion Of Chars That Are Capitalized | 0.0007 |
| Proportion Of Tokens That Are Stop Words | 0.0007 |
| Question Marks Per Sentence | 0.0004 |
| Topical Proximity - Food (glove-twitter-50) | 0.0004 |
| Topical Proximity - Sexual (glove-twitter-25) | 0.0001 |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Uh, what? It was your job, Morty. | Rick | Summer |
| Oh, God, what’s going on now? | Summer | Beth |
| He bails on everybody! He bailed on Mom when she was a kid! He -- He bailed on tiny planet! And in case I never made this clear to you, Summer, he bailed on you. He left you to rot in a world that he ruined because he doesn't care! Because nobody's special to him, Summer, not even himself. So, if you really want your grandpa back, grab a shovel. The one that won't let you down is buried in your backyard! | Jerry | Morty |
| Don't worry about Jerry. He's gonna be fine.You hear me Jerry? You're gonna be fine! | Beth | Rick |
| Hey! I said nobody move, buddy! | Morty | Rick |
| Me. I used to wear blue pants. | Morty | Rick |
| But can you help me get to my family? You know, at my house? | Jerry | Morty |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Morty | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Rick | Jerry |
| Man that guy is the Red Grin Grumble to pretending he knows what's going on.  Oh you agree, huh?  You like that Red Grin Grumble reference?  Well guess what? I made him up. You really are your father's children. Think for yourselves, don't be sheep. | Jerry | Rick |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| I'm sorry. It's just like the end of "Old Yeller. | Rick | Jerry |
| It's the Citadel of Ricks. All the different Ricks from all the different realities got together to hide here from the government. | Rick | Morty |
| How is praying going to help? | Summer | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Morty | Summer |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Morty | Jerry |
| Morty, stay out of this. You are obviously not capable of judging these situations on your own. | Rick | Jerry |
| I mean it's been shot. With a gun. | Morty | Beth |
| No idea what you're talking about. | Jerry | Rick |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Rick | Jerry |
| Grandpa Rick wouldn't put up with this! | Morty | Summer |
| Goldenfold, we're coming out! We just want to talk! | Morty | Rick |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| I don't know. I think like one sixty-fourth of my collars didn't work. It's hard to keep straight now that I have sixty-three other memories of everything. | Rick | Morty |
| - or sister I said any of this, I'll deny it - | Morty | Rick |
| Uh, w-why don't you get it Jerry? you're the man of the house and you don't have a job. | Morty | Rick |
| Well, I'm not calling him that. That's ridiculous. | Morty | Jerry |
| I didn't say my father is perfect, I said his work is important. | Summer | Beth |
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
| Whatever. How petty would I have to be to care less about an animal's life than my own ego? | Rick | Beth |
| What? What kind of monster are you? | Rick | Morty |
| We’ll take our chances raising her without fancy new jobs outside of a potato-based religion.  And you know what? I’m sick of pretending that we’re together because of the kids in the first place! I married you because you’re the love of my life! | Rick | Jerry |
| I'm looking at her. Thanks for F.D.'ing me up like that. | Rick | Jerry |
| Huh, what do you know, it's working | Jerry | Rick |
| Got some of that mermaid puss! | Summer | Rick |
| I never said I was angry at you. | Morty | Summer |
| What? Why didn't you notify us? | Rick | Beth |
| What? Why are you looking at me? You want to go outside? Outside? | Rick | Jerry |
| This article says the reason we weren't involved was... "personality conflicts". | Rick | Morty |
| Man, Grandpa Rick must have gotten shitfaced. | Morty | Summer |
| I AM a baby! I’m a baby NOW! | Morty | Jerry |
| Oldest Rick trick in the book. | Morty | Rick |
| Listen, Rick, if you're gonna stay here rent-free and use my son for your stupid science, the least you could do is put a little bit of it to use for the family. You make that dog smart or Morty's grounded! | Rick | Jerry |
| Oh, for crying out—he's got some kind of disability or something. Is that what you want us to say? | Summer | Jerry |
| Are you guys Power Rangers? But only on one small part of your necks? Hey, do those things need batteries? Were they included? Clean up in the fruit isle! Not in a homophobic way though, they're just fruity necklaces is all I was saying. | Rick | Jerry |
| Hey, I can't help if I can't see. | Beth | Rick |
| There is no helicopter and there is no Cervine Institute. | Rick | Jerry |
| I don’t know what to say. Summer is doing really well here. | Morty | Beth |
| What?! Why would you -- Look, we're running late. We have to go. | Rick | Beth |
| But.. she was trying to kill us! | Rick | Morty |
| What? N-No, I don't want to see your Pog collection. I don't renounce Rick, and I never have. I was just trying to protect my sister. I wanted you to have a normal life. That's something you can't have when Rick shows up. Everything real turns fake. Everything right is wrong. All you know is that you know nothing and he knows everything. And, well -- well, he's not a villain, Summer, but he shouldn't be your hero. He's more like a demon or a super fucked up god. | Rick | Morty |
| But I obviously sort of love you, don't I?  So stop asking and maybe I'll love you more.  Crap, They need me at the horse hospital. | Jerry | Beth |
| Oh, my God! He's trying to tell us something.  That is so awesome. | Morty | Summer |
| Yeah, and what's courageous about eating a hot dog? | Jerry | Morty |
| Now hold on a second, let’s be rational about this. | Rick | Beth |
### 📉 Individual Feature Importances

| Feature | Importance |
| ------- | ---------- |
| deg_of_presence(morty)_norm | 0.017367471009492874 |
| count(jerry) | 0.007385819684714079 |
| deg_of_presence(mildew)_norm | 0.0072138747200369835 |
| deg_of_presence(nelly)_norm | 0.006888942327350378 |
| deg_of_presence(hell)_norm | 0.0065929461270570755 |
| deg_of_presence(complete)_norm | 0.006137897726148367 |
| deg_of_presence(shit)_norm | 0.004983606748282909 |
| deg_of_presence(babble)_norm | 0.004923453088849783 |
| deg_of_presence(underside)_norm | 0.004864016082137823 |
| deg_of_presence(involve)_norm | 0.004715544171631336 |
| deg_of_presence(newman)_norm | 0.004702858626842499 |
| deg_of_presence(fear)_norm | 0.004693714436143637 |
| deg_of_presence(saget)_norm | 0.004691950511187315 |
| deg_of_presence(smart)_norm | 0.004609482362866402 |
| deg_of_presence(pentagon)_norm | 0.003954547923058271 |
| deg_of_presence(singing)_norm | 0.0038649379275739193 |
| deg_of_presence(amulet)_norm | 0.003834696486592293 |
| deg_of_presence(dafoe)_norm | 0.0038234922103583813 |
| ... | ... |
| deg_of_presence(giving)_norm | 0.0 |
| deg_of_presence(give)_norm | 0.0 |
| deg_of_presence(girl)_norm | 0.0 |
| deg_of_presence(keyboard)_norm | 0.0 |
| deg_of_presence(kick)_norm | 0.0 |
| deg_of_presence(mind)_norm | 0.0 |
| deg_of_presence(mad)_norm | 0.0 |
| deg_of_presence(milk)_norm | 0.0 |
| deg_of_presence(mess)_norm | 0.0 |
| deg_of_presence(mean)_norm | 0.0 |
| deg_of_presence(mattress)_norm | 0.0 |
| deg_of_presence(them)_norm | 0.0 |
| deg_of_presence(matter)_norm | 0.0 |
| deg_of_presence(man)_norm | 0.0 |
| deg_of_presence(thing)_norm | 0.0 |
| deg_of_presence(think)_norm | 0.0 |
| deg_of_presence(make)_norm | 0.0 |
| deg_of_presence(long)_norm | 0.0 |
| deg_of_presence(knock)_norm | 0.0 |
| deg_of_presence(thread)_norm | 0.0 |
| deg_of_presence(little)_norm | 0.0 |
| deg_of_presence(literally)_norm | 0.0 |
| deg_of_presence(listen)_norm | 0.0 |
| deg_of_presence(lick)_norm | 0.0 |
| deg_of_presence(tie)_norm | 0.0 |
| deg_of_presence(let)_norm | 0.0 |
| deg_of_presence(leave)_norm | 0.0 |
| deg_of_presence(learn)_norm | 0.0 |
| deg_of_presence(late)_norm | 0.0 |
| deg_of_presence(try)_norm | 0.0 |
