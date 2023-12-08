### 🚀 **XGBClssfr_6fs_13**

- 🤖 **Model Type**: 
	<class 'xgboost.sklearn.XGBClassifier'>
- 📊 **Dataset Used**: 
	_Random_
- 🧠 **Number of Features**: 
	32
- 🚫 **Unused Features**: 
	0/32
- ⌛ **Model Train Time**: 
	0.235
- 💬 **SpaCy Preprocessing Model**: 
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `random_state`: 42
	- `max_depth`: 4
	- `objective`: multi:softmax
	- `num_class`: 5
	- `n_estimators`: 45
	- `min_child_weight`: 1
	- `gamma`: 0.1
	- `subsample`: 0.5
	- `colsample_bytree`: 0.8
	- `reg_lambda`: 1
	- `reg_alpha`: 0.1
	- `learning_rate`: 0.1
	- `alpha`: 0.8
	- `booster`: gbtree
	- `eta`: 0.4
	- `eval_metric`: <function f1_macro at 0x134263700>

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 0.79 | 0.465 | 0.436 |
| Macro F1 | 0.754 | 0.207 | 0.25 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.00 | 0.00 | 0.00 |
| Jerry | 0.33 | 0.06 | 0.10 |
| Morty | 0.30 | 0.28 | 0.29 |
| Rick | 0.53 | 0.84 | 0.65 |
| Summer | 0.00 | 0.00 | 0.00 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.14 | 0.07 | 0.10 |
| Jerry | 0.20 | 0.10 | 0.13 |
| Morty | 0.56 | 0.36 | 0.43 |
| Rick | 0.48 | 0.76 | 0.59 |
| Summer | 0.00 | 0.00 | 0.00 |

### 🧠 Feature Extraction Methods

| Method | Importance |
| ------ | ---------- |
| Average Root Verb Embedding (glove-twitter-25) | 0.8242 |
| Dashes Per Sentence | 0.0451 |
| Exclamation Marks Per Sentence | 0.0413 |
| Question Marks Per Sentence | 0.0350 |
| Total Sentence Count | 0.0295 |
| Average Tokens Per Sentence | 0.0249 |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Uh, what? It was your job, Morty. | Rick | Summer |
| Oh, God, what’s going on now? | Rick | Beth |
| He bails on everybody! He bailed on Mom when she was a kid! He -- He bailed on tiny planet! And in case I never made this clear to you, Summer, he bailed on you. He left you to rot in a world that he ruined because he doesn't care! Because nobody's special to him, Summer, not even himself. So, if you really want your grandpa back, grab a shovel. The one that won't let you down is buried in your backyard! | Rick | Morty |
| I'll cover that bet. I get it. | Rick | Morty |
| Whoa! Look! It's that lady with all that shit on her face like Worf from Star Trek! That was getting coffee! How did she get there! | Rick | Morty |
| That's right, Morty. This is gonna be a lot like that, except, you know, it's gonna may--be make sense. | Morty | Rick |
| Aw, geez. Okay. I guess I can skip history. What about Frank? I mean, shouldn't you unfreeze him? | Rick | Morty |
| Because you suck! You've been keeping your lip zipped about it since Grandpa got arrested, but the fact is, you're freaking stoked to bail on him. | Rick | Summer |
| Hey! I said nobody move, buddy! | Morty | Rick |
| Me. I used to wear blue pants. | Morty | Rick |
| Alright! That's enough. You're talking about my species! We understand genocide, we do it sometimes! | Morty | Jerry |
| I am not putting my father in a home! He just came back into my life, and you want to grab him and stuff him under a mattress like last month's Victoria's Secret? | Rick | Beth |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Rick | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Rick | Jerry |
| I don't know, Rick. I can't leave school again. | Rick | Morty |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| Hello? Is anybody here?  Mr. President! | Rick | Morty |
| They're just robots, Morty! It's okay to shoot them! They're robots! | Morty | Rick |
| I'm sorry. It's just like the end of "Old Yeller. | Rick | Jerry |
| It's the Citadel of Ricks. All the different Ricks from all the different realities got together to hide here from the government. | Rick | Morty |
| How is praying going to help? | Summer | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| Aw! Oh, my God! He recognizes the other dogs on TV. | Rick | Summer |
| - Because that's -- that's what this is all about, Morty. | Morty | Rick |
| It's Dimension 35-C, and it's got the perfect climate conditions for a special type of tree, Morty, called a Mega Tree, and there's fruit in those trees, and there's seeds in those fruits. I'm talking about Mega Seeds. They're they're incredibly powerful, and I need them to help me with my research, Morty. | Morty | Rick |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Rick | Summer |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Morty | Jerry |
| I mean it's been shot. With a gun. | Rick | Beth |
| Really? You don't say. You would have used a ghost train?  Hey, everybody, the ghost train guy would have used a ghost train! | Morty | Rick |
| Boom! Told you! In your face! He is ruining our child! Wait, what am I celebrating? | Morty | Jerry |
| Jerry, this was the most romantic weekend I've ever had. | Rick | Beth |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Rick | Jerry |
| Grandpa Rick wouldn't put up with this! | Morty | Summer |
| Oh, man, Rick. What is this place? | Rick | Morty |
| Uh, the adventure is the favor, Morty. Me sleeping on these linens is the favor. I mean, w-w-w-what--what are we vindicating? Comfort? | Morty | Rick |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| Yeah, Rick... I-it's great. Is this the surprise? | Rick | Morty |
| Well, I'm not calling him that. That's ridiculous. | Morty | Jerry |
| I didn't say my father is perfect, I said his work is important. | Jerry | Beth |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Rick | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Rick | Summer |
| I don't care about Jessica! Y-Yyyyyyyyyyou— | Rick | Morty |
| Just focus on the mission, all right? | Rick | Morty |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Morty | Jerry |
| And then Ethan played guitar and we learned the Seven Contemplations of the Head by singing them. It was really fun. Praise be the head! | Rick | Summer |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Rick | Beth |
| Did he say he never forgets a kid? | Morty | Rick |
| Rick, this really bums me out. It-It's embarrassing to find out these guys don't like us. | Rick | Morty |
| Then what good was the "yes"? | Rick | Beth |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Morty | Beth |
| Whatever. How petty would I have to be to care less about an animal's life than my own ego? | Rick | Beth |
| Okay, I only ask, Jerry, because, as you know, my job involves performing heart surgery. | Jerry | Beth |
| What? What kind of monster are you? | Beth | Morty |
| We’ll take our chances raising her without fancy new jobs outside of a potato-based religion.  And you know what? I’m sick of pretending that we’re together because of the kids in the first place! I married you because you’re the love of my life! | Rick | Jerry |
| I'm looking at her. Thanks for F.D.'ing me up like that. | Morty | Jerry |
| I never said I was angry at you. | Morty | Summer |
| What? Why didn't you notify us? | Summer | Beth |
| This better not be a bribe. If I find a single thing out of place in this house, my love of ice cream won't save you. I'll get my jacket. | Rick | Jerry |
| What? Why are you looking at me? You want to go outside? Outside? | Rick | Jerry |
| I don't either. I-I'm just saying, if anything, the drunk version of me is probably so supportive of Israel, he wants what's best for it and... | Summer | Rick |
| Man, Grandpa Rick must have gotten shitfaced. | Morty | Summer |
| Rick? Are you far away, or are you inside something? | Rick | Morty |
| Sir, I need to get to the stage and help Rick get schwifty! | Rick | Morty |
| Time to go another dream deep, Morty! | Morty | Rick |
| Doesn't feel so good, does it? | Rick | Morty |
| Go in the waiting room, Dad. | Rick | Beth |
| I AM a baby! I’m a baby NOW! | Rick | Jerry |
| Listen, Rick, if you're gonna stay here rent-free and use my son for your stupid science, the least you could do is put a little bit of it to use for the family. You make that dog smart or Morty's grounded! | Rick | Jerry |
| Oh, for crying out—he's got some kind of disability or something. Is that what you want us to say? | Rick | Jerry |
| Because Ricks hate themselves the most. And our Rick is the most himself. | Summer | Morty |
| Are you guys Power Rangers? But only on one small part of your necks? Hey, do those things need batteries? Were they included? Clean up in the fruit isle! Not in a homophobic way though, they're just fruity necklaces is all I was saying. | Rick | Jerry |
| There is no helicopter and there is no Cervine Institute. | Rick | Jerry |
| I don’t know what to say. Summer is doing really well here. | Rick | Beth |
| Aw, geez, dad. Y-you know, that's a lot to drop on a kid all at once. | Rick | Morty |
| What?! Why would you -- Look, we're running late. We have to go. | Rick | Beth |
| But.. she was trying to kill us! | Rick | Morty |
| Right, Crocubot. So, you're half-cold, unfeeling reptile, half-also cold, equally-unfeeling machine. | Morty | Rick |
| What? N-No, I don't want to see your Pog collection. I don't renounce Rick, and I never have. I was just trying to protect my sister. I wanted you to have a normal life. That's something you can't have when Rick shows up. Everything real turns fake. Everything right is wrong. All you know is that you know nothing and he knows everything. And, well -- well, he's not a villain, Summer, but he shouldn't be your hero. He's more like a demon or a super fucked up god. | Rick | Morty |
| But I obviously sort of love you, don't I?  So stop asking and maybe I'll love you more.  Crap, They need me at the horse hospital. | Rick | Beth |
| Oh, my God! He's trying to tell us something.  That is so awesome. | Rick | Summer |
| Yeah, and what's courageous about eating a hot dog? | Rick | Morty |
| Now hold on a second, let’s be rational about this. | Rick | Beth |
### 📉 Individual Feature Importances

| Feature | Importance |
| ------- | ---------- |
| dashes_per_sentence | 0.0450655035674572 |
| exclamation_marks_per_sentence | 0.04131896048784256 |
| avg_root_verb_embedding_24 | 0.036867305636405945 |
| avg_root_verb_embedding_20 | 0.036057423800230026 |
| question_marks_per_sentence | 0.03502907603979111 |
| avg_root_verb_embedding_23 | 0.03492084518074989 |
| avg_root_verb_embedding_5 | 0.03483080863952637 |
| avg_root_verb_embedding_14 | 0.03470446541905403 |
| avg_root_verb_embedding_4 | 0.033768121153116226 |
| avg_root_verb_embedding_21 | 0.03354650363326073 |
| avg_root_verb_embedding_15 | 0.033310551196336746 |
| avg_root_verb_embedding_9 | 0.03293968364596367 |
| avg_root_verb_embedding_17 | 0.032055310904979706 |
| avg_root_verb_embedding_19 | 0.03158891946077347 |
| avg_root_verb_embedding_22 | 0.03134528920054436 |
| avg_root_verb_embedding_6 | 0.03115132264792919 |
| avg_root_verb_embedding_18 | 0.03112431801855564 |
| avg_root_verb_embedding_12 | 0.030928170308470726 |
| avg_root_verb_embedding_0 | 0.030256878584623337 |
| avg_root_verb_embedding_8 | 0.030167000368237495 |
| avg_root_verb_embedding_16 | 0.030144350603222847 |
| avg_root_verb_embedding_13 | 0.03002806007862091 |
| avg_root_verb_embedding_11 | 0.029960626736283302 |
| total_sentence_count | 0.029491715133190155 |
| avg_root_verb_embedding_2 | 0.029308101162314415 |
| avg_root_verb_embedding_10 | 0.028509046882390976 |
| avg_root_verb_embedding_1 | 0.028338056057691574 |
| avg_root_verb_embedding_7 | 0.027730854228138924 |
| avg_root_verb_embedding_3 | 0.025830481201410294 |
| avg_tokens_per_sentence | 0.024871446192264557 |
| n_root_verbs | 0.023469706997275352 |
| n_root_verbs_embedded | 0.011341162025928497 |
