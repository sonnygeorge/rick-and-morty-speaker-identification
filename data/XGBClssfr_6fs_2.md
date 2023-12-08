### 🚀 **XGBClssfr_6fs_2**

- 🤖 **Model Type**: 
	<class 'xgboost.sklearn.XGBClassifier'>
- 📊 **Dataset Used**: 
	_Random_
- 🧠 **Number of Features**: 
	32
- 🚫 **Unused Features**: 
	0/32
- ⌛ **Model Train Time**: 
	4.732
- 💬 **SpaCy Preprocessing Model**: 
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `random_state`: 42
	- `max_depth`: 4
	- `objective`: multi:softmax
	- `num_class`: 5
	- `n_estimators`: 100
	- `min_child_weight`: 1
	- `gamma`: 0.1
	- `subsample`: 0.8
	- `colsample_bytree`: 0.8
	- `reg_lambda`: 1
	- `reg_alpha`: 0.1
	- `learning_rate`: 0.4
	- `alpha`: 0.5
	- `booster`: dart
	- `eta`: 0.3
	- `eval_metric`: map

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 0.99 | 0.387 | 0.386 |
| Macro F1 | 0.989 | 0.196 | 0.305 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.00 | 0.00 | 0.00 |
| Jerry | 0.10 | 0.06 | 0.07 |
| Morty | 0.21 | 0.22 | 0.22 |
| Rick | 0.50 | 0.69 | 0.58 |
| Summer | 0.14 | 0.09 | 0.11 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.30 | 0.21 | 0.25 |
| Jerry | 0.22 | 0.20 | 0.21 |
| Morty | 0.39 | 0.39 | 0.39 |
| Rick | 0.43 | 0.52 | 0.47 |
| Summer | 0.33 | 0.14 | 0.20 |

### 🧠 Feature Extraction Methods

| Method | Importance |
| ------ | ---------- |
| Average Root Verb Embedding (glove-twitter-25) | 0.8726 |
| Dashes Per Sentence | 0.0295 |
| Exclamation Marks Per Sentence | 0.0285 |
| Question Marks Per Sentence | 0.0276 |
| Average Word Length | 0.0217 |
| Total Sentence Count | 0.0201 |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Okay, hold on just a second, Morty. | Jerry | Rick |
| Uh, what? It was your job, Morty. | Rick | Summer |
| Oh, God, what’s going on now? | Rick | Beth |
| He bails on everybody! He bailed on Mom when she was a kid! He -- He bailed on tiny planet! And in case I never made this clear to you, Summer, he bailed on you. He left you to rot in a world that he ruined because he doesn't care! Because nobody's special to him, Summer, not even himself. So, if you really want your grandpa back, grab a shovel. The one that won't let you down is buried in your backyard! | Rick | Morty |
| Wow! A whole world populated by intelligent dogs. I wonder what it'll be like, Rick. | Rick | Morty |
| Whoa! Look! It's that lady with all that shit on her face like Worf from Star Trek! That was getting coffee! How did she get there! | Rick | Morty |
| Aw, geez. Okay. I guess I can skip history. What about Frank? I mean, shouldn't you unfreeze him? | Rick | Morty |
| Because you suck! You've been keeping your lip zipped about it since Grandpa got arrested, but the fact is, you're freaking stoked to bail on him. | Rick | Summer |
| No, you can't!  Jessica doesn't even know I exist! But—but, but forget about that, because you can't blow up humanity! | Rick | Morty |
| Hey! I said nobody move, buddy! | Morty | Rick |
| Me. I used to wear blue pants. | Morty | Rick |
| Alright! That's enough. You're talking about my species! We understand genocide, we do it sometimes! | Rick | Jerry |
| I am not putting my father in a home! He just came back into my life, and you want to grab him and stuff him under a mattress like last month's Victoria's Secret? | Morty | Beth |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Rick | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Rick | Jerry |
| You don’t have to be a dick. | Jerry | Rick |
| I don't know, Rick. I can't leave school again. | Jerry | Morty |
| Man that guy is the Red Grin Grumble to pretending he knows what's going on.  Oh you agree, huh?  You like that Red Grin Grumble reference?  Well guess what? I made him up. You really are your father's children. Think for yourselves, don't be sheep. | Morty | Rick |
| Good job, Morty. Let's go, kids. | Morty | Rick |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| Hello? Is anybody here?  Mr. President! | Rick | Morty |
| They're just robots, Morty! It's okay to shoot them! They're robots! | Morty | Rick |
| It's the Citadel of Ricks. All the different Ricks from all the different realities got together to hide here from the government. | Rick | Morty |
| How is praying going to help? | Morty | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| It's Dimension 35-C, and it's got the perfect climate conditions for a special type of tree, Morty, called a Mega Tree, and there's fruit in those trees, and there's seeds in those fruits. I'm talking about Mega Seeds. They're they're incredibly powerful, and I need them to help me with my research, Morty. | Morty | Rick |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Rick | Summer |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Rick | Jerry |
| Hey, what's wrong Morty? Oh, you're worried about your dad, huh? | Beth | Rick |
| Morty, stay out of this. You are obviously not capable of judging these situations on your own. | Beth | Jerry |
| Out of the frying pan dot, dot, dot, huh, Morty? | Morty | Rick |
| If it takes nine seasons, I want my McNugget dipping sauce, Szechuan sauce, Morty. | Beth | Rick |
| I mean it's been shot. With a gun. | Rick | Beth |
| Really? You don't say. You would have used a ghost train?  Hey, everybody, the ghost train guy would have used a ghost train! | Morty | Rick |
| Boom! Told you! In your face! He is ruining our child! Wait, what am I celebrating? | Morty | Jerry |
| Jerry, this was the most romantic weekend I've ever had. | Rick | Beth |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Rick | Jerry |
| Grandpa Rick wouldn't put up with this! | Morty | Summer |
| Oh, man, Rick. What is this place? | Rick | Morty |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| I don't know. I think like one sixty-fourth of my collars didn't work. It's hard to keep straight now that I have sixty-three other memories of everything. | Rick | Morty |
| Yeah, Rick... I-it's great. Is this the surprise? | Rick | Morty |
| - or sister I said any of this, I'll deny it - | Morty | Rick |
| Uh, w-why don't you get it Jerry? you're the man of the house and you don't have a job. | Morty | Rick |
| Well, I'm not calling him that. That's ridiculous. | Morty | Jerry |
| I didn't say my father is perfect, I said his work is important. | Jerry | Beth |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Jerry | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Rick | Summer |
| I don't care about Jessica! Y-Yyyyyyyyyyou— | Rick | Morty |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Morty | Jerry |
| And then Ethan played guitar and we learned the Seven Contemplations of the Head by singing them. It was really fun. Praise be the head! | Rick | Summer |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Rick | Beth |
| Did he say he never forgets a kid? | Morty | Rick |
| Rick, this really bums me out. It-It's embarrassing to find out these guys don't like us. | Rick | Morty |
| Then what good was the "yes"? | Morty | Beth |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Morty | Beth |
| Whatever. How petty would I have to be to care less about an animal's life than my own ego? | Rick | Beth |
| That's enough! Drop the gun, Rick! | Rick | Morty |
| Okay, I only ask, Jerry, because, as you know, my job involves performing heart surgery. | Summer | Beth |
| What? What kind of monster are you? | Rick | Morty |
| We’ll take our chances raising her without fancy new jobs outside of a potato-based religion.  And you know what? I’m sick of pretending that we’re together because of the kids in the first place! I married you because you’re the love of my life! | Rick | Jerry |
| I'm looking at her. Thanks for F.D.'ing me up like that. | Morty | Jerry |
| Come on, Morty. Please, Morty. You have to do it, Morty. | Jerry | Rick |
| I never said I was angry at you. | Jerry | Summer |
| What? Why didn't you notify us? | Summer | Beth |
| This better not be a bribe. If I find a single thing out of place in this house, my love of ice cream won't save you. I'll get my jacket. | Rick | Jerry |
| What? Why are you looking at me? You want to go outside? Outside? | Rick | Jerry |
| There she is. All right. Come on, Morty. Let's go. | Morty | Rick |
| I don't either. I-I'm just saying, if anything, the drunk version of me is probably so supportive of Israel, he wants what's best for it and... | Summer | Rick |
| This article says the reason we weren't involved was... "personality conflicts". | Summer | Morty |
| Man, Grandpa Rick must have gotten shitfaced. | Rick | Summer |
| Rick? Are you far away, or are you inside something? | Jerry | Morty |
| Sir, I need to get to the stage and help Rick get schwifty! | Rick | Morty |
| Little extra  snippy this morning, aren't you? | Summer | Rick |
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
| What?! Why would you -- Look, we're running late. We have to go. | Morty | Beth |
| But.. she was trying to kill us! | Rick | Morty |
| What? N-No, I don't want to see your Pog collection. I don't renounce Rick, and I never have. I was just trying to protect my sister. I wanted you to have a normal life. That's something you can't have when Rick shows up. Everything real turns fake. Everything right is wrong. All you know is that you know nothing and he knows everything. And, well -- well, he's not a villain, Summer, but he shouldn't be your hero. He's more like a demon or a super fucked up god. | Rick | Morty |
| But I obviously sort of love you, don't I?  So stop asking and maybe I'll love you more.  Crap, They need me at the horse hospital. | Rick | Beth |
| Oh, my God! He's trying to tell us something.  That is so awesome. | Rick | Summer |
| Yeah, and what's courageous about eating a hot dog? | Rick | Morty |
| Now hold on a second, let’s be rational about this. | Jerry | Beth |
### 📉 Individual Feature Importances

| Feature | Importance |
| ------- | ---------- |
| avg_root_verb_embedding_0 | 0.04335137829184532 |
| n_root_verbs_embedded | 0.04061690345406532 |
| avg_root_verb_embedding_20 | 0.037841007113456726 |
| avg_root_verb_embedding_23 | 0.03772348165512085 |
| avg_root_verb_embedding_5 | 0.03710485249757767 |
| avg_root_verb_embedding_15 | 0.03602198138833046 |
| avg_root_verb_embedding_24 | 0.035659607499837875 |
| avg_root_verb_embedding_16 | 0.035001594573259354 |
| avg_root_verb_embedding_12 | 0.03496214747428894 |
| avg_root_verb_embedding_18 | 0.034953467547893524 |
| avg_root_verb_embedding_21 | 0.034238629043102264 |
| avg_root_verb_embedding_22 | 0.03421974182128906 |
| avg_root_verb_embedding_14 | 0.034113429486751556 |
| avg_root_verb_embedding_4 | 0.033170487731695175 |
| avg_root_verb_embedding_19 | 0.031652435660362244 |
| avg_root_verb_embedding_11 | 0.031614597886800766 |
| avg_root_verb_embedding_2 | 0.03155898675322533 |
| avg_root_verb_embedding_9 | 0.031260423362255096 |
| avg_root_verb_embedding_13 | 0.030415771529078484 |
| avg_root_verb_embedding_17 | 0.030071541666984558 |
| dashes_per_sentence | 0.029508231207728386 |
| exclamation_marks_per_sentence | 0.028525520116090775 |
| avg_root_verb_embedding_8 | 0.027819551527500153 |
| avg_root_verb_embedding_1 | 0.027644677087664604 |
| question_marks_per_sentence | 0.027635451406240463 |
| avg_root_verb_embedding_6 | 0.027524935081601143 |
| avg_root_verb_embedding_7 | 0.02737962268292904 |
| avg_root_verb_embedding_3 | 0.025154296308755875 |
| avg_root_verb_embedding_10 | 0.022721610963344574 |
| avg_token_length | 0.02172134816646576 |
| total_sentence_count | 0.020050188526511192 |
| n_root_verbs | 0.018762173131108284 |
