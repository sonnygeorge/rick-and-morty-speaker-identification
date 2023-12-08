### 🚀 **XGBClssfr_6fs_9**

- 🤖 **Model Type**: 
	<class 'xgboost.sklearn.XGBClassifier'>
- 📊 **Dataset Used**: 
	_Random_
- 🧠 **Number of Features**: 
	32
- 🚫 **Unused Features**: 
	0/32
- ⌛ **Model Train Time**: 
	0.337
- 💬 **SpaCy Preprocessing Model**: 
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `random_state`: 42
	- `max_depth`: 4
	- `objective`: multi:softprob
	- `num_class`: 5
	- `n_estimators`: 100
	- `min_child_weight`: 3
	- `gamma`: 0.3
	- `subsample`: 0.8
	- `colsample_bytree`: 0.8
	- `reg_lambda`: 1
	- `reg_alpha`: 0.3
	- `learning_rate`: 0.4
	- `alpha`: 0.5
	- `booster`: gbtree
	- `eta`: 0.4
	- `eval_metric`: mphe

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 0.954 | 0.413 | 0.386 |
| Macro F1 | 0.95 | 0.235 | 0.243 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.12 | 0.05 | 0.07 |
| Jerry | 0.11 | 0.06 | 0.07 |
| Morty | 0.30 | 0.34 | 0.32 |
| Rick | 0.53 | 0.68 | 0.59 |
| Summer | 0.17 | 0.09 | 0.12 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.25 | 0.14 | 0.18 |
| Jerry | 0.08 | 0.10 | 0.09 |
| Morty | 0.44 | 0.39 | 0.42 |
| Rick | 0.47 | 0.60 | 0.53 |
| Summer | 0.00 | 0.00 | 0.00 |

### 🧠 Feature Extraction Methods

| Method | Importance |
| ------ | ---------- |
| Average Root Verb Embedding (glove-twitter-25) | 0.8507 |
| Exclamation Marks Per Sentence | 0.0410 |
| Question Marks Per Sentence | 0.0342 |
| Average Word Length | 0.0291 |
| Total Sentence Count | 0.0225 |
| Average Tokens Per Sentence | 0.0224 |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Okay, hold on just a second, Morty. | Morty | Rick |
| Uh, what? It was your job, Morty. | Rick | Summer |
| Oh, God, what’s going on now? | Morty | Beth |
| He bails on everybody! He bailed on Mom when she was a kid! He -- He bailed on tiny planet! And in case I never made this clear to you, Summer, he bailed on you. He left you to rot in a world that he ruined because he doesn't care! Because nobody's special to him, Summer, not even himself. So, if you really want your grandpa back, grab a shovel. The one that won't let you down is buried in your backyard! | Rick | Morty |
| Wow! A whole world populated by intelligent dogs. I wonder what it'll be like, Rick. | Rick | Morty |
| Whoa! Look! It's that lady with all that shit on her face like Worf from Star Trek! That was getting coffee! How did she get there! | Rick | Morty |
| That's right, Morty. This is gonna be a lot like that, except, you know, it's gonna may--be make sense. | Morty | Rick |
| Aw, geez. Okay. I guess I can skip history. What about Frank? I mean, shouldn't you unfreeze him? | Rick | Morty |
| Because you suck! You've been keeping your lip zipped about it since Grandpa got arrested, but the fact is, you're freaking stoked to bail on him. | Rick | Summer |
| No, you can't!  Jessica doesn't even know I exist! But—but, but forget about that, because you can't blow up humanity! | Rick | Morty |
| Hey! I said nobody move, buddy! | Morty | Rick |
| Me. I used to wear blue pants. | Morty | Rick |
| Alright! That's enough. You're talking about my species! We understand genocide, we do it sometimes! | Rick | Jerry |
| I am not putting my father in a home! He just came back into my life, and you want to grab him and stuff him under a mattress like last month's Victoria's Secret? | Rick | Beth |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Rick | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Rick | Jerry |
| You don’t have to be a dick. | Jerry | Rick |
| Good job, Morty. Let's go, kids. | Morty | Rick |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| Hello? Is anybody here?  Mr. President! | Rick | Morty |
| They're just robots, Morty! It's okay to shoot them! They're robots! | Morty | Rick |
| I'm sorry. It's just like the end of "Old Yeller. | Rick | Jerry |
| It's the Citadel of Ricks. All the different Ricks from all the different realities got together to hide here from the government. | Rick | Morty |
| How is praying going to help? | Morty | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| The day I invented the portal gun is the day I lost her. | Summer | Rick |
| It's Dimension 35-C, and it's got the perfect climate conditions for a special type of tree, Morty, called a Mega Tree, and there's fruit in those trees, and there's seeds in those fruits. I'm talking about Mega Seeds. They're they're incredibly powerful, and I need them to help me with my research, Morty. | Morty | Rick |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Morty | Summer |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Morty | Jerry |
| Hey, what's wrong Morty? Oh, you're worried about your dad, huh? | Beth | Rick |
| Out of the frying pan dot, dot, dot, huh, Morty? | Morty | Rick |
| If it takes nine seasons, I want my McNugget dipping sauce, Szechuan sauce, Morty. | Beth | Rick |
| I mean it's been shot. With a gun. | Rick | Beth |
| Really? You don't say. You would have used a ghost train?  Hey, everybody, the ghost train guy would have used a ghost train! | Morty | Rick |
| Boom! Told you! In your face! He is ruining our child! Wait, what am I celebrating? | Morty | Jerry |
| Jerry, this was the most romantic weekend I've ever had. | Rick | Beth |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Rick | Jerry |
| Grandpa Rick wouldn't put up with this! | Rick | Summer |
| That’s planning for failure, Morty. Even dumber than regular planning.  Balls. | Beth | Rick |
| Oh, man, Rick. What is this place? | Rick | Morty |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| I don't know. I think like one sixty-fourth of my collars didn't work. It's hard to keep straight now that I have sixty-three other memories of everything. | Rick | Morty |
| Yeah, Rick... I-it's great. Is this the surprise? | Rick | Morty |
| - or sister I said any of this, I'll deny it - | Morty | Rick |
| Don't worry about it, Morty. Just come help me get these seeds, all right, buddy? | Jerry | Rick |
| Uh, w-why don't you get it Jerry? you're the man of the house and you don't have a job. | Morty | Rick |
| Well, I'm not calling him that. That's ridiculous. | Morty | Jerry |
| I didn't say my father is perfect, I said his work is important. | Jerry | Beth |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Morty | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Rick | Summer |
| Just focus on the mission, all right? | Rick | Morty |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Beth | Jerry |
| And then Ethan played guitar and we learned the Seven Contemplations of the Head by singing them. It was really fun. Praise be the head! | Rick | Summer |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Rick | Beth |
| Rick, this really bums me out. It-It's embarrassing to find out these guys don't like us. | Rick | Morty |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Morty | Beth |
| Whatever. How petty would I have to be to care less about an animal's life than my own ego? | Rick | Beth |
| Okay, I only ask, Jerry, because, as you know, my job involves performing heart surgery. | Jerry | Beth |
| What? What kind of monster are you? | Beth | Morty |
| We’ll take our chances raising her without fancy new jobs outside of a potato-based religion.  And you know what? I’m sick of pretending that we’re together because of the kids in the first place! I married you because you’re the love of my life! | Rick | Jerry |
| I'm looking at her. Thanks for F.D.'ing me up like that. | Morty | Jerry |
| Come on, Morty. Please, Morty. You have to do it, Morty. | Jerry | Rick |
| I never said I was angry at you. | Jerry | Summer |
| What? Why didn't you notify us? | Summer | Beth |
| This better not be a bribe. If I find a single thing out of place in this house, my love of ice cream won't save you. I'll get my jacket. | Beth | Jerry |
| What? Why are you looking at me? You want to go outside? Outside? | Rick | Jerry |
| There she is. All right. Come on, Morty. Let's go. | Morty | Rick |
| I don't either. I-I'm just saying, if anything, the drunk version of me is probably so supportive of Israel, he wants what's best for it and... | Summer | Rick |
| This article says the reason we weren't involved was... "personality conflicts". | Summer | Morty |
| Man, Grandpa Rick must have gotten shitfaced. | Jerry | Summer |
| Sir, I need to get to the stage and help Rick get schwifty! | Rick | Morty |
| Uh, I kind of am. I saved the goddamn universe. | Morty | Rick |
| Time to go another dream deep, Morty! | Morty | Rick |
| Doesn't feel so good, does it? | Rick | Morty |
| Go in the waiting room, Dad. | Rick | Beth |
| I AM a baby! I’m a baby NOW! | Morty | Jerry |
| Listen, Rick, if you're gonna stay here rent-free and use my son for your stupid science, the least you could do is put a little bit of it to use for the family. You make that dog smart or Morty's grounded! | Rick | Jerry |
| Oh, for crying out—he's got some kind of disability or something. Is that what you want us to say? | Rick | Jerry |
| Alright. I'll-I'll land. I'll land. I'll land. I'll land the thing. I’ll land the thing. Big tough guy all of a sudden. | Beth | Rick |
| Because Ricks hate themselves the most. And our Rick is the most himself. | Summer | Morty |
| Are you guys Power Rangers? But only on one small part of your necks? Hey, do those things need batteries? Were they included? Clean up in the fruit isle! Not in a homophobic way though, they're just fruity necklaces is all I was saying. | Rick | Jerry |
| Hey, I can't help if I can't see. | Morty | Rick |
| There is no helicopter and there is no Cervine Institute. | Rick | Jerry |
| I don’t know what to say. Summer is doing really well here. | Rick | Beth |
| What?! Why would you -- Look, we're running late. We have to go. | Rick | Beth |
| But.. she was trying to kill us! | Rick | Morty |
| What? N-No, I don't want to see your Pog collection. I don't renounce Rick, and I never have. I was just trying to protect my sister. I wanted you to have a normal life. That's something you can't have when Rick shows up. Everything real turns fake. Everything right is wrong. All you know is that you know nothing and he knows everything. And, well -- well, he's not a villain, Summer, but he shouldn't be your hero. He's more like a demon or a super fucked up god. | Rick | Morty |
| But I obviously sort of love you, don't I?  So stop asking and maybe I'll love you more.  Crap, They need me at the horse hospital. | Morty | Beth |
| Oh, my God! He's trying to tell us something.  That is so awesome. | Rick | Summer |
| Now hold on a second, let’s be rational about this. | Jerry | Beth |
### 📉 Individual Feature Importances

| Feature | Importance |
| ------- | ---------- |
| avg_root_verb_embedding_23 | 0.050402842462062836 |
| avg_root_verb_embedding_0 | 0.04132680594921112 |
| exclamation_marks_per_sentence | 0.04100651293992996 |
| avg_root_verb_embedding_24 | 0.03851857781410217 |
| avg_root_verb_embedding_17 | 0.03686260059475899 |
| avg_root_verb_embedding_14 | 0.03594079241156578 |
| avg_root_verb_embedding_4 | 0.035049017518758774 |
| avg_root_verb_embedding_2 | 0.03444584831595421 |
| question_marks_per_sentence | 0.034201789647340775 |
| avg_root_verb_embedding_20 | 0.0341934859752655 |
| avg_root_verb_embedding_18 | 0.03248269110918045 |
| avg_root_verb_embedding_22 | 0.0324280746281147 |
| avg_root_verb_embedding_11 | 0.03234546631574631 |
| avg_root_verb_embedding_5 | 0.03214891254901886 |
| avg_root_verb_embedding_12 | 0.031286682933568954 |
| avg_root_verb_embedding_16 | 0.030441878363490105 |
| avg_root_verb_embedding_6 | 0.03003554977476597 |
| avg_root_verb_embedding_3 | 0.030030477792024612 |
| avg_root_verb_embedding_9 | 0.029668698087334633 |
| avg_root_verb_embedding_15 | 0.02949419990181923 |
| avg_token_length | 0.02914395183324814 |
| avg_root_verb_embedding_7 | 0.029104510322213173 |
| avg_root_verb_embedding_10 | 0.02824745886027813 |
| avg_root_verb_embedding_21 | 0.028143594041466713 |
| avg_root_verb_embedding_13 | 0.027866153046488762 |
| avg_root_verb_embedding_19 | 0.02714376151561737 |
| avg_root_verb_embedding_8 | 0.027132708579301834 |
| avg_root_verb_embedding_1 | 0.024921802803874016 |
| total_sentence_count | 0.02254405803978443 |
| avg_tokens_per_sentence | 0.022381270304322243 |
| n_root_verbs_embedded | 0.021221626549959183 |
| n_root_verbs | 0.019838204607367516 |
