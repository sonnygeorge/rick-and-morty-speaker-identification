### 🚀 **XGBClssfr_6fs_11**

- 🤖 **Model Type**: 
	<class 'xgboost.sklearn.XGBClassifier'>
- 📊 **Dataset Used**: 
	_Random_
- 🧠 **Number of Features**: 
	32
- 🚫 **Unused Features**: 
	0/32
- ⌛ **Model Train Time**: 
	0.221
- 💬 **SpaCy Preprocessing Model**: 
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `random_state`: 42
	- `max_depth`: 4
	- `objective`: multi:softprob
	- `num_class`: 5
	- `n_estimators`: 60
	- `min_child_weight`: 1
	- `gamma`: 0.4
	- `subsample`: 0.8
	- `colsample_bytree`: 0.5
	- `reg_lambda`: 1
	- `reg_alpha`: 0.1
	- `learning_rate`: 0.5
	- `alpha`: 0.8
	- `booster`: gbtree
	- `eta`: 0.15
	- `eval_metric`: <function f1_macro at 0x134263700>

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 0.952 | 0.413 | 0.386 |
| Macro F1 | 0.946 | 0.2 | 0.274 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.00 | 0.00 | 0.00 |
| Jerry | 0.00 | 0.00 | 0.00 |
| Morty | 0.25 | 0.31 | 0.28 |
| Rick | 0.53 | 0.72 | 0.61 |
| Summer | 0.14 | 0.09 | 0.11 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.18 | 0.14 | 0.16 |
| Jerry | 0.25 | 0.10 | 0.14 |
| Morty | 0.42 | 0.39 | 0.41 |
| Rick | 0.44 | 0.57 | 0.49 |
| Summer | 0.20 | 0.14 | 0.17 |

### 🧠 Feature Extraction Methods

| Method | Importance |
| ------ | ---------- |
| Average Root Verb Embedding (glove-twitter-25) | 0.8392 |
| Exclamation Marks Per Sentence | 0.0413 |
| Question Marks Per Sentence | 0.0363 |
| Average Word Length | 0.0304 |
| Dashes Per Sentence | 0.0286 |
| Proportion Of Tokens That Are Stop Words | 0.0242 |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Uh, what? It was your job, Morty. | Morty | Summer |
| Oh, God, what’s going on now? | Morty | Beth |
| He bails on everybody! He bailed on Mom when she was a kid! He -- He bailed on tiny planet! And in case I never made this clear to you, Summer, he bailed on you. He left you to rot in a world that he ruined because he doesn't care! Because nobody's special to him, Summer, not even himself. So, if you really want your grandpa back, grab a shovel. The one that won't let you down is buried in your backyard! | Summer | Morty |
| Wow! A whole world populated by intelligent dogs. I wonder what it'll be like, Rick. | Rick | Morty |
| Whoa! Look! It's that lady with all that shit on her face like Worf from Star Trek! That was getting coffee! How did she get there! | Rick | Morty |
| That's right, Morty. This is gonna be a lot like that, except, you know, it's gonna may--be make sense. | Morty | Rick |
| Aw, geez. Okay. I guess I can skip history. What about Frank? I mean, shouldn't you unfreeze him? | Rick | Morty |
| Because you suck! You've been keeping your lip zipped about it since Grandpa got arrested, but the fact is, you're freaking stoked to bail on him. | Rick | Summer |
| Me. I used to wear blue pants. | Morty | Rick |
| Alright! That's enough. You're talking about my species! We understand genocide, we do it sometimes! | Rick | Jerry |
| I am not putting my father in a home! He just came back into my life, and you want to grab him and stuff him under a mattress like last month's Victoria's Secret? | Rick | Beth |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Rick | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Morty | Jerry |
| I don't know, Rick. I can't leave school again. | Jerry | Morty |
| Man that guy is the Red Grin Grumble to pretending he knows what's going on.  Oh you agree, huh?  You like that Red Grin Grumble reference?  Well guess what? I made him up. You really are your father's children. Think for yourselves, don't be sheep. | Morty | Rick |
| Good job, Morty. Let's go, kids. | Morty | Rick |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| Hello? Is anybody here?  Mr. President! | Rick | Morty |
| They're just robots, Morty! It's okay to shoot them! They're robots! | Morty | Rick |
| I'm sorry. It's just like the end of "Old Yeller. | Morty | Jerry |
| It's the Citadel of Ricks. All the different Ricks from all the different realities got together to hide here from the government. | Rick | Morty |
| How is praying going to help? | Summer | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| It's Dimension 35-C, and it's got the perfect climate conditions for a special type of tree, Morty, called a Mega Tree, and there's fruit in those trees, and there's seeds in those fruits. I'm talking about Mega Seeds. They're they're incredibly powerful, and I need them to help me with my research, Morty. | Morty | Rick |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Rick | Summer |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Morty | Jerry |
| Hey, what's wrong Morty? Oh, you're worried about your dad, huh? | Beth | Rick |
| Morty, stay out of this. You are obviously not capable of judging these situations on your own. | Beth | Jerry |
| Out of the frying pan dot, dot, dot, huh, Morty? | Morty | Rick |
| I mean it's been shot. With a gun. | Rick | Beth |
| Really? You don't say. You would have used a ghost train?  Hey, everybody, the ghost train guy would have used a ghost train! | Morty | Rick |
| Boom! Told you! In your face! He is ruining our child! Wait, what am I celebrating? | Morty | Jerry |
| Jerry, this was the most romantic weekend I've ever had. | Rick | Beth |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Rick | Jerry |
| Grandpa Rick wouldn't put up with this! | Rick | Summer |
| That’s planning for failure, Morty. Even dumber than regular planning.  Balls. | Beth | Rick |
| Oh, man, Rick. What is this place? | Rick | Morty |
| Uh, the adventure is the favor, Morty. Me sleeping on these linens is the favor. I mean, w-w-w-what--what are we vindicating? Comfort? | Morty | Rick |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| I don't know. I think like one sixty-fourth of my collars didn't work. It's hard to keep straight now that I have sixty-three other memories of everything. | Rick | Morty |
| Yeah, Rick... I-it's great. Is this the surprise? | Rick | Morty |
| - or sister I said any of this, I'll deny it - | Morty | Rick |
| Uh, w-why don't you get it Jerry? you're the man of the house and you don't have a job. | Morty | Rick |
| Well, I'm not calling him that. That's ridiculous. | Morty | Jerry |
| I didn't say my father is perfect, I said his work is important. | Morty | Beth |
| Sure. Why not? I don’t, I don't know. Y-you know what, Mo— | Morty | Rick |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Rick | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Rick | Summer |
| I don't care about Jessica! Y-Yyyyyyyyyyou— | Rick | Morty |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Rick | Jerry |
| And then Ethan played guitar and we learned the Seven Contemplations of the Head by singing them. It was really fun. Praise be the head! | Rick | Summer |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Jerry | Beth |
| Did he say he never forgets a kid? | Morty | Rick |
| Rick, this really bums me out. It-It's embarrassing to find out these guys don't like us. | Rick | Morty |
| Then what good was the "yes"? | Morty | Beth |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Morty | Beth |
| Whatever. How petty would I have to be to care less about an animal's life than my own ego? | Rick | Beth |
| That's enough! Drop the gun, Rick! | Rick | Morty |
| Okay, I only ask, Jerry, because, as you know, my job involves performing heart surgery. | Rick | Beth |
| What? What kind of monster are you? | Rick | Morty |
| We’ll take our chances raising her without fancy new jobs outside of a potato-based religion.  And you know what? I’m sick of pretending that we’re together because of the kids in the first place! I married you because you’re the love of my life! | Rick | Jerry |
| I'm looking at her. Thanks for F.D.'ing me up like that. | Morty | Jerry |
| Got some of that mermaid puss! | Summer | Rick |
| I never said I was angry at you. | Rick | Summer |
| What? Why didn't you notify us? | Morty | Beth |
| This better not be a bribe. If I find a single thing out of place in this house, my love of ice cream won't save you. I'll get my jacket. | Rick | Jerry |
| What? Why are you looking at me? You want to go outside? Outside? | Rick | Jerry |
| I don't either. I-I'm just saying, if anything, the drunk version of me is probably so supportive of Israel, he wants what's best for it and... | Summer | Rick |
| This article says the reason we weren't involved was... "personality conflicts". | Summer | Morty |
| Man, Grandpa Rick must have gotten shitfaced. | Rick | Summer |
| Sir, I need to get to the stage and help Rick get schwifty! | Rick | Morty |
| Little extra  snippy this morning, aren't you? | Beth | Rick |
| Time to go another dream deep, Morty! | Morty | Rick |
| Go in the waiting room, Dad. | Rick | Beth |
| I AM a baby! I’m a baby NOW! | Morty | Jerry |
| Listen, Rick, if you're gonna stay here rent-free and use my son for your stupid science, the least you could do is put a little bit of it to use for the family. You make that dog smart or Morty's grounded! | Rick | Jerry |
| Oh, for crying out—he's got some kind of disability or something. Is that what you want us to say? | Rick | Jerry |
| Because Ricks hate themselves the most. And our Rick is the most himself. | Summer | Morty |
| Are you guys Power Rangers? But only on one small part of your necks? Hey, do those things need batteries? Were they included? Clean up in the fruit isle! Not in a homophobic way though, they're just fruity necklaces is all I was saying. | Rick | Jerry |
| Hey, I can't help if I can't see. | Morty | Rick |
| There is no helicopter and there is no Cervine Institute. | Rick | Jerry |
| I don’t know what to say. Summer is doing really well here. | Rick | Beth |
| Aw, geez, dad. Y-you know, that's a lot to drop on a kid all at once. | Rick | Morty |
| What?! Why would you -- Look, we're running late. We have to go. | Morty | Beth |
| Right, Crocubot. So, you're half-cold, unfeeling reptile, half-also cold, equally-unfeeling machine. | Morty | Rick |
| What? N-No, I don't want to see your Pog collection. I don't renounce Rick, and I never have. I was just trying to protect my sister. I wanted you to have a normal life. That's something you can't have when Rick shows up. Everything real turns fake. Everything right is wrong. All you know is that you know nothing and he knows everything. And, well -- well, he's not a villain, Summer, but he shouldn't be your hero. He's more like a demon or a super fucked up god. | Rick | Morty |
| But I obviously sort of love you, don't I?  So stop asking and maybe I'll love you more.  Crap, They need me at the horse hospital. | Jerry | Beth |
| Oh, my God! He's trying to tell us something.  That is so awesome. | Rick | Summer |
| Yeah, and what's courageous about eating a hot dog? | Rick | Morty |
| Now hold on a second, let’s be rational about this. | Jerry | Beth |
### 📉 Individual Feature Importances

| Feature | Importance |
| ------- | ---------- |
| avg_root_verb_embedding_4 | 0.04313747212290764 |
| exclamation_marks_per_sentence | 0.041281454265117645 |
| question_marks_per_sentence | 0.03634284436702728 |
| avg_root_verb_embedding_23 | 0.0358017235994339 |
| avg_root_verb_embedding_5 | 0.03507401794195175 |
| avg_root_verb_embedding_24 | 0.034696731716394424 |
| avg_root_verb_embedding_19 | 0.03468102589249611 |
| avg_root_verb_embedding_9 | 0.03342854976654053 |
| avg_root_verb_embedding_12 | 0.0329759307205677 |
| avg_root_verb_embedding_15 | 0.03266092389822006 |
| avg_root_verb_embedding_8 | 0.03190089762210846 |
| avg_root_verb_embedding_2 | 0.031885914504528046 |
| avg_root_verb_embedding_10 | 0.03185541182756424 |
| avg_root_verb_embedding_20 | 0.031705308705568314 |
| avg_root_verb_embedding_0 | 0.03161843493580818 |
| avg_root_verb_embedding_22 | 0.03145897760987282 |
| avg_root_verb_embedding_11 | 0.03139543533325195 |
| avg_root_verb_embedding_14 | 0.03110980987548828 |
| avg_root_verb_embedding_6 | 0.030695931985974312 |
| avg_root_verb_embedding_3 | 0.030494093894958496 |
| avg_token_length | 0.030389996245503426 |
| avg_root_verb_embedding_13 | 0.02956297993659973 |
| avg_root_verb_embedding_21 | 0.02947315201163292 |
| avg_root_verb_embedding_17 | 0.0287762638181448 |
| dashes_per_sentence | 0.028551308438181877 |
| n_root_verbs_embedded | 0.027585037052631378 |
| avg_root_verb_embedding_7 | 0.02654349058866501 |
| avg_root_verb_embedding_1 | 0.02626142092049122 |
| avg_root_verb_embedding_16 | 0.02623819373548031 |
| avg_root_verb_embedding_18 | 0.025833267718553543 |
| proportion_stop_words | 0.024190444499254227 |
| n_root_verbs | 0.022393565624952316 |