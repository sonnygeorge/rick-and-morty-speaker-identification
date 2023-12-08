### 🚀 **XGBClssfr_6fs_5**

- 🤖 **Model Type**: 
	<class 'xgboost.sklearn.XGBClassifier'>
- 📊 **Dataset Used**: 
	_Random_
- 🧠 **Number of Features**: 
	32
- 🚫 **Unused Features**: 
	0/32
- ⌛ **Model Train Time**: 
	0.360
- 💬 **SpaCy Preprocessing Model**: 
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `random_state`: 42
	- `max_depth`: 4
	- `objective`: multi:softprob
	- `num_class`: 5
	- `n_estimators`: 80
	- `min_child_weight`: 2
	- `gamma`: 0.05
	- `subsample`: 0.8
	- `colsample_bytree`: 0.8
	- `reg_lambda`: 0.8
	- `reg_alpha`: 0.3
	- `learning_rate`: 0.5
	- `alpha`: 0.5
	- `booster`: gbtree
	- `eta`: 0.2
	- `eval_metric`: map

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 0.994 | 0.458 | 0.376 |
| Macro F1 | 0.992 | 0.306 | 0.23 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.25 | 0.10 | 0.14 |
| Jerry | 0.20 | 0.11 | 0.14 |
| Morty | 0.36 | 0.44 | 0.39 |
| Rick | 0.55 | 0.69 | 0.61 |
| Summer | 0.33 | 0.18 | 0.24 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.10 | 0.07 | 0.08 |
| Jerry | 0.12 | 0.10 | 0.11 |
| Morty | 0.45 | 0.46 | 0.46 |
| Rick | 0.46 | 0.55 | 0.50 |
| Summer | 0.00 | 0.00 | 0.00 |

### 🧠 Feature Extraction Methods

| Method | Importance |
| ------ | ---------- |
| Average Root Verb Embedding (glove-twitter-25) | 0.8762 |
| Exclamation Marks Per Sentence | 0.0339 |
| Question Marks Per Sentence | 0.0310 |
| Average Word Length | 0.0231 |
| Total Sentence Count | 0.0187 |
| Average Tokens Per Sentence | 0.0172 |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Okay, hold on just a second, Morty. | Morty | Rick |
| Uh, what? It was your job, Morty. | Rick | Summer |
| Oh, God, what’s going on now? | Rick | Beth |
| Whoa! Look! It's that lady with all that shit on her face like Worf from Star Trek! That was getting coffee! How did she get there! | Rick | Morty |
| That's right, Morty. This is gonna be a lot like that, except, you know, it's gonna may--be make sense. | Morty | Rick |
| Aw, geez. Okay. I guess I can skip history. What about Frank? I mean, shouldn't you unfreeze him? | Rick | Morty |
| No, you can't!  Jessica doesn't even know I exist! But—but, but forget about that, because you can't blow up humanity! | Rick | Morty |
| Hey! I said nobody move, buddy! | Morty | Rick |
| Me. I used to wear blue pants. | Morty | Rick |
| Alright! That's enough. You're talking about my species! We understand genocide, we do it sometimes! | Rick | Jerry |
| I am not putting my father in a home! He just came back into my life, and you want to grab him and stuff him under a mattress like last month's Victoria's Secret? | Rick | Beth |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Rick | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Beth | Jerry |
| You don’t have to be a dick. | Jerry | Rick |
| Good job, Morty. Let's go, kids. | Morty | Rick |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| Hello? Is anybody here?  Mr. President! | Rick | Morty |
| It's the Citadel of Ricks. All the different Ricks from all the different realities got together to hide here from the government. | Rick | Morty |
| How is praying going to help? | Morty | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| It's Dimension 35-C, and it's got the perfect climate conditions for a special type of tree, Morty, called a Mega Tree, and there's fruit in those trees, and there's seeds in those fruits. I'm talking about Mega Seeds. They're they're incredibly powerful, and I need them to help me with my research, Morty. | Morty | Rick |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Rick | Summer |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Morty | Jerry |
| Hey, what's wrong Morty? Oh, you're worried about your dad, huh? | Beth | Rick |
| Out of the frying pan dot, dot, dot, huh, Morty? | Morty | Rick |
| If it takes nine seasons, I want my McNugget dipping sauce, Szechuan sauce, Morty. | Beth | Rick |
| I mean it's been shot. With a gun. | Rick | Beth |
| Really? You don't say. You would have used a ghost train?  Hey, everybody, the ghost train guy would have used a ghost train! | Morty | Rick |
| Boom! Told you! In your face! He is ruining our child! Wait, what am I celebrating? | Rick | Jerry |
| Jerry, this was the most romantic weekend I've ever had. | Rick | Beth |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Rick | Jerry |
| Grandpa Rick wouldn't put up with this! | Morty | Summer |
| Oh, man, Rick. What is this place? | Rick | Morty |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| Yeah, Rick... I-it's great. Is this the surprise? | Summer | Morty |
| - or sister I said any of this, I'll deny it - | Morty | Rick |
| Uh, w-why don't you get it Jerry? you're the man of the house and you don't have a job. | Morty | Rick |
| Well, I'm not calling him that. That's ridiculous. | Morty | Jerry |
| Are you kidding me? This again? Oh, man, it looks like we've hit dream bedrock here, Morty. | Morty | Rick |
| I didn't say my father is perfect, I said his work is important. | Jerry | Beth |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Rick | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Rick | Summer |
| When we get to customs, I'm gonna need you to take these seeds into the bathroom, and I'm gonna need you to put them way up inside your butthole, Morty. | Jerry | Rick |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Morty | Jerry |
| And then Ethan played guitar and we learned the Seven Contemplations of the Head by singing them. It was really fun. Praise be the head! | Rick | Summer |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Rick | Beth |
| Rick, this really bums me out. It-It's embarrassing to find out these guys don't like us. | Rick | Morty |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Morty | Beth |
| Whatever. How petty would I have to be to care less about an animal's life than my own ego? | Rick | Beth |
| That's enough! Drop the gun, Rick! | Rick | Morty |
| Okay, I only ask, Jerry, because, as you know, my job involves performing heart surgery. | Jerry | Beth |
| What? What kind of monster are you? | Beth | Morty |
| We’ll take our chances raising her without fancy new jobs outside of a potato-based religion.  And you know what? I’m sick of pretending that we’re together because of the kids in the first place! I married you because you’re the love of my life! | Rick | Jerry |
| I'm looking at her. Thanks for F.D.'ing me up like that. | Morty | Jerry |
| Come on, Morty. Please, Morty. You have to do it, Morty. | Jerry | Rick |
| I never said I was angry at you. | Morty | Summer |
| This better not be a bribe. If I find a single thing out of place in this house, my love of ice cream won't save you. I'll get my jacket. | Beth | Jerry |
| What? Why are you looking at me? You want to go outside? Outside? | Rick | Jerry |
| There she is. All right. Come on, Morty. Let's go. | Morty | Rick |
| I don't either. I-I'm just saying, if anything, the drunk version of me is probably so supportive of Israel, he wants what's best for it and... | Summer | Rick |
| This article says the reason we weren't involved was... "personality conflicts". | Summer | Morty |
| Man, Grandpa Rick must have gotten shitfaced. | Rick | Summer |
| Sir, I need to get to the stage and help Rick get schwifty! | Rick | Morty |
| Uh, I kind of am. I saved the goddamn universe. | Morty | Rick |
| Time to go another dream deep, Morty! | Morty | Rick |
| Doesn't feel so good, does it? | Rick | Morty |
| You have to turn them on, Morty! The shoes have to be turned on! | Jerry | Rick |
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
| Aw, geez, dad. Y-you know, that's a lot to drop on a kid all at once. | Rick | Morty |
| What?! Why would you -- Look, we're running late. We have to go. | Jerry | Beth |
| What? N-No, I don't want to see your Pog collection. I don't renounce Rick, and I never have. I was just trying to protect my sister. I wanted you to have a normal life. That's something you can't have when Rick shows up. Everything real turns fake. Everything right is wrong. All you know is that you know nothing and he knows everything. And, well -- well, he's not a villain, Summer, but he shouldn't be your hero. He's more like a demon or a super fucked up god. | Rick | Morty |
| But I obviously sort of love you, don't I?  So stop asking and maybe I'll love you more.  Crap, They need me at the horse hospital. | Morty | Beth |
| Oh, my God! He's trying to tell us something.  That is so awesome. | Rick | Summer |
| Now hold on a second, let’s be rational about this. | Jerry | Beth |
### 📉 Individual Feature Importances

| Feature | Importance |
| ------- | ---------- |
| avg_root_verb_embedding_23 | 0.04900630936026573 |
| avg_root_verb_embedding_0 | 0.043660156428813934 |
| avg_root_verb_embedding_24 | 0.038588497787714005 |
| avg_root_verb_embedding_2 | 0.03811066597700119 |
| avg_root_verb_embedding_15 | 0.03715832158923149 |
| avg_root_verb_embedding_14 | 0.03712986782193184 |
| avg_root_verb_embedding_11 | 0.03693297877907753 |
| avg_root_verb_embedding_17 | 0.03656110540032387 |
| exclamation_marks_per_sentence | 0.03387414664030075 |
| avg_root_verb_embedding_10 | 0.0322696790099144 |
| avg_root_verb_embedding_13 | 0.032229192554950714 |
| avg_root_verb_embedding_22 | 0.03191047161817551 |
| avg_root_verb_embedding_9 | 0.03173267841339111 |
| avg_root_verb_embedding_18 | 0.0315154492855072 |
| question_marks_per_sentence | 0.030950112268328667 |
| avg_root_verb_embedding_4 | 0.03076738305389881 |
| avg_root_verb_embedding_3 | 0.03074970655143261 |
| avg_root_verb_embedding_12 | 0.030653810128569603 |
| avg_root_verb_embedding_21 | 0.030507994815707207 |
| avg_root_verb_embedding_8 | 0.030168116092681885 |
| avg_root_verb_embedding_16 | 0.02911127544939518 |
| avg_root_verb_embedding_5 | 0.028874702751636505 |
| avg_root_verb_embedding_19 | 0.028642484918236732 |
| avg_root_verb_embedding_1 | 0.028135398402810097 |
| avg_root_verb_embedding_20 | 0.02754364162683487 |
| n_root_verbs | 0.026726335287094116 |
| avg_root_verb_embedding_6 | 0.026617899537086487 |
| avg_root_verb_embedding_7 | 0.026202687993645668 |
| n_root_verbs_embedded | 0.024676520377397537 |
| avg_token_length | 0.023112131282687187 |
| total_sentence_count | 0.01868492178618908 |
| avg_tokens_per_sentence | 0.01719527691602707 |
