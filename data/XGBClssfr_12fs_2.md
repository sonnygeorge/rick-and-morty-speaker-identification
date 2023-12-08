### 🚀 **XGBClssfr_12fs_2**

- 🤖 **Model Type**: 
	<class 'xgboost.sklearn.XGBClassifier'>
- 📊 **Dataset Used**: 
	_Random_
- 🧠 **Number of Features**: 
	1649
- 🚫 **Unused Features**: 
	1084/1649
- ⌛ **Model Train Time**: 
	9.348
- 💬 **SpaCy Preprocessing Model**: 
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `random_state`: 42
	- `max_depth`: 3
	- `objective`: multi:softmax
	- `num_class`: 5
	- `n_estimators`: 60
	- `min_child_weight`: 2
	- `gamma`: 0.1
	- `subsample`: 0.8
	- `colsample_bytree`: 0.6
	- `reg_lambda`: 1
	- `reg_alpha`: 5
	- `learning_rate`: 0.3
	- `alpha`: 1.2
	- `booster`: gbtree
	- `eta`: 0.4
	- `eval_metric`: <function f1_macro at 0x12df0d5e0>

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 0.961 | 0.516 | 0.495 |
| Macro F1 | 0.95 | 0.271 | 0.313 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.00 | 0.00 | 0.00 |
| Jerry | 0.38 | 0.17 | 0.23 |
| Morty | 0.38 | 0.47 | 0.42 |
| Rick | 0.61 | 0.84 | 0.71 |
| Summer | 0.00 | 0.00 | 0.00 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.25 | 0.14 | 0.18 |
| Jerry | 0.29 | 0.20 | 0.24 |
| Morty | 0.44 | 0.50 | 0.47 |
| Rick | 0.62 | 0.76 | 0.68 |
| Summer | 0.00 | 0.00 | 0.00 |

### 🧠 Feature Extraction Methods

| Method | Importance |
| ------ | ---------- |
| Nghbhood Degrees - Lemmas (.5decay,4topn,5nghbrs)(glove-twitter-50)(Rndm)(-blacklist) | 0.7278 |
| Average Root Verb Embedding (fasttext-wiki-news-subwords-300) | 0.2546 |
| Question Marks Per Sentence | 0.0033 |
| Proportion Of Chars That Are Capitalized | 0.0029 |
| Exclamation Marks Per Sentence | 0.0026 |
| Proportion Of Tokens That Are Stop Words | 0.0023 |
| Average Word Length | 0.0017 |
| Average Tokens Per Sentence | 0.0017 |
| Dashes Per Sentence | 0.0015 |
| Familial Words & Common Names 1-Gram One Hots | 0.0011 |
| Topical Proximity - Condescension (fasttext-wiki-news-subwords-300) | 0.0005 |
| Total Sentence Count | 0.0000 |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Uh, what? It was your job, Morty. | Rick | Summer |
| Oh, God, what’s going on now? | Morty | Beth |
| He bails on everybody! He bailed on Mom when she was a kid! He -- He bailed on tiny planet! And in case I never made this clear to you, Summer, he bailed on you. He left you to rot in a world that he ruined because he doesn't care! Because nobody's special to him, Summer, not even himself. So, if you really want your grandpa back, grab a shovel. The one that won't let you down is buried in your backyard! | Rick | Morty |
| Don't worry about Jerry. He's gonna be fine.You hear me Jerry? You're gonna be fine! | Morty | Rick |
| Whoa! Look! It's that lady with all that shit on her face like Worf from Star Trek! That was getting coffee! How did she get there! | Rick | Morty |
| Aw, geez. Okay. I guess I can skip history. What about Frank? I mean, shouldn't you unfreeze him? | Rick | Morty |
| Because you suck! You've been keeping your lip zipped about it since Grandpa got arrested, but the fact is, you're freaking stoked to bail on him. | Beth | Summer |
| Hey! I said nobody move, buddy! | Morty | Rick |
| Me. I used to wear blue pants. | Morty | Rick |
| But can you help me get to my family? You know, at my house? | Beth | Morty |
| Alright! That's enough. You're talking about my species! We understand genocide, we do it sometimes! | Morty | Jerry |
| I am not putting my father in a home! He just came back into my life, and you want to grab him and stuff him under a mattress like last month's Victoria's Secret? | Rick | Beth |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Morty | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Rick | Jerry |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| I'm sorry. It's just like the end of "Old Yeller. | Rick | Jerry |
| It's the Citadel of Ricks. All the different Ricks from all the different realities got together to hide here from the government. | Rick | Morty |
| How is praying going to help? | Summer | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| Aw! Oh, my God! He recognizes the other dogs on TV. | Morty | Summer |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Morty | Summer |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Morty | Jerry |
| Morty, stay out of this. You are obviously not capable of judging these situations on your own. | Rick | Jerry |
| I mean it's been shot. With a gun. | Rick | Beth |
| Sure thing! And I was kinda hoping that I could get a selfie with you? | Rick | Morty |
| Really? You don't say. You would have used a ghost train?  Hey, everybody, the ghost train guy would have used a ghost train! | Morty | Rick |
| Boom! Told you! In your face! He is ruining our child! Wait, what am I celebrating? | Beth | Jerry |
| Jerry, this was the most romantic weekend I've ever had. | Rick | Beth |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Rick | Jerry |
| Grandpa Rick wouldn't put up with this! | Morty | Summer |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| I don't know. I think like one sixty-fourth of my collars didn't work. It's hard to keep straight now that I have sixty-three other memories of everything. | Jerry | Morty |
| - or sister I said any of this, I'll deny it - | Morty | Rick |
| Uh, w-why don't you get it Jerry? you're the man of the house and you don't have a job. | Morty | Rick |
| Well, I'm not calling him that. That's ridiculous. | Rick | Jerry |
| I didn't say my father is perfect, I said his work is important. | Jerry | Beth |
| Sure. Why not? I don’t, I don't know. Y-you know what, Mo— | Morty | Rick |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Jerry | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Rick | Summer |
| Just focus on the mission, all right? | Rick | Morty |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Rick | Jerry |
| And then Ethan played guitar and we learned the Seven Contemplations of the Head by singing them. It was really fun. Praise be the head! | Rick | Summer |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Jerry | Beth |
| Then what good was the "yes"? | Morty | Beth |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Rick | Beth |
| Whatever. How petty would I have to be to care less about an animal's life than my own ego? | Rick | Beth |
| Okay, I only ask, Jerry, because, as you know, my job involves performing heart surgery. | Morty | Beth |
| What? What kind of monster are you? | Rick | Morty |
| I'm looking at her. Thanks for F.D.'ing me up like that. | Rick | Jerry |
| Huh, what do you know, it's working | Morty | Rick |
| I never said I was angry at you. | Morty | Summer |
| What? Why didn't you notify us? | Rick | Beth |
| I don't either. I-I'm just saying, if anything, the drunk version of me is probably so supportive of Israel, he wants what's best for it and... | Morty | Rick |
| This article says the reason we weren't involved was... "personality conflicts". | Rick | Morty |
| Man, Grandpa Rick must have gotten shitfaced. | Morty | Summer |
| Doesn't feel so good, does it? | Rick | Morty |
| Go in the waiting room, Dad. | Summer | Beth |
| I AM a baby! I’m a baby NOW! | Morty | Jerry |
| Oldest Rick trick in the book. | Beth | Rick |
| Listen, Rick, if you're gonna stay here rent-free and use my son for your stupid science, the least you could do is put a little bit of it to use for the family. You make that dog smart or Morty's grounded! | Rick | Jerry |
| Oh, for crying out—he's got some kind of disability or something. Is that what you want us to say? | Rick | Jerry |
| Because Ricks hate themselves the most. And our Rick is the most himself. | Rick | Morty |
| Are you guys Power Rangers? But only on one small part of your necks? Hey, do those things need batteries? Were they included? Clean up in the fruit isle! Not in a homophobic way though, they're just fruity necklaces is all I was saying. | Rick | Jerry |
| Hey, I can't help if I can't see. | Morty | Rick |
| There is no helicopter and there is no Cervine Institute. | Rick | Jerry |
| I don’t know what to say. Summer is doing really well here. | Morty | Beth |
| What?! Why would you -- Look, we're running late. We have to go. | Rick | Beth |
| But.. she was trying to kill us! | Rick | Morty |
| Not until I finish what I started. And that is how you get level-nine access without a password. | Morty | Rick |
| What? N-No, I don't want to see your Pog collection. I don't renounce Rick, and I never have. I was just trying to protect my sister. I wanted you to have a normal life. That's something you can't have when Rick shows up. Everything real turns fake. Everything right is wrong. All you know is that you know nothing and he knows everything. And, well -- well, he's not a villain, Summer, but he shouldn't be your hero. He's more like a demon or a super fucked up god. | Rick | Morty |
| But I obviously sort of love you, don't I?  So stop asking and maybe I'll love you more.  Crap, They need me at the horse hospital. | Jerry | Beth |
| Oh, my God! He's trying to tell us something.  That is so awesome. | Morty | Summer |
| Yeah, and what's courageous about eating a hot dog? | Rick | Morty |
| Now hold on a second, let’s be rational about this. | Rick | Beth |
### 📉 Individual Feature Importances

| Feature | Importance |
| ------- | ---------- |
| deg_of_presence(shoney)_norm | 0.01767701469361782 |
| deg_of_presence(cognition)_norm | 0.017611170187592506 |
| deg_of_presence(sterilize)_norm | 0.01588663086295128 |
| deg_of_presence(applause)_norm | 0.011099888943135738 |
| deg_of_presence(crystal)_norm | 0.01075745653361082 |
| deg_of_presence(nelly)_norm | 0.010517852380871773 |
| deg_of_presence(morty)_norm | 0.010399780236184597 |
| deg_of_presence(pistol)_norm | 0.008228939957916737 |
| deg_of_presence(rick)_norm | 0.008104439824819565 |
| deg_of_presence(babble)_norm | 0.007816796191036701 |
| deg_of_presence(urgent)_norm | 0.0075474451296031475 |
| deg_of_presence(assemble)_norm | 0.006634843535721302 |
| deg_of_presence(evangelical)_norm | 0.006487778387963772 |
| deg_of_presence(pancakes)_norm | 0.006125528831034899 |
| avg_root_verb_embedding_167 | 0.006123257335275412 |
| deg_of_presence(nut)_norm | 0.006115827243775129 |
| deg_of_presence(hitler)_norm | 0.006067240610718727 |
| deg_of_presence(hell)_norm | 0.005981068592518568 |
| ... | ... |
| deg_of_presence(feel)_norm | 0.0 |
| deg_of_presence(fine)_norm | 0.0 |
| deg_of_presence(find)_norm | 0.0 |
| deg_of_presence(film)_norm | 0.0 |
| deg_of_presence(figure)_norm | 0.0 |
| deg_of_presence(fever)_norm | 0.0 |
| deg_of_presence(festival)_norm | 0.0 |
| deg_of_presence(feral)_norm | 0.0 |
| deg_of_presence(federation)_norm | 0.0 |
| deg_of_presence(family)_norm | 0.0 |
| deg_of_presence(fear)_norm | 0.0 |
| deg_of_presence(favorite)_norm | 0.0 |
| deg_of_presence(favor)_norm | 0.0 |
| deg_of_presence(fault)_norm | 0.0 |
| deg_of_presence(fast)_norm | 0.0 |
| deg_of_presence(fart)_norm | 0.0 |
| deg_of_presence(far)_norm | 0.0 |
| total_sentence_count | 0.0 |
