### 🚀 **XGBClssfr_6fs_6**

- 🤖 **Model Type**: 
	<class 'xgboost.sklearn.XGBClassifier'>
- 📊 **Dataset Used**: 
	_Random_
- 🧠 **Number of Features**: 
	32
- 🚫 **Unused Features**: 
	26/32
- ⌛ **Model Train Time**: 
	0.095
- 💬 **SpaCy Preprocessing Model**: 
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `random_state`: 42
	- `max_depth`: 4
	- `objective`: multi:softprob
	- `num_class`: 5
	- `n_estimators`: 60
	- `min_child_weight`: 1
	- `gamma`: 0.05
	- `subsample`: 0.8
	- `colsample_bytree`: 0.6
	- `reg_lambda`: 0.6
	- `reg_alpha`: 0.1
	- `learning_rate`: 0.1
	- `alpha`: 1.8
	- `booster`: gblinear
	- `eta`: 0.4
	- `eval_metric`: <function f1_macro at 0x134263700>

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 0.426 | 0.477 | 0.416 |
| Macro F1 | 0.119 | 0.129 | 0.117 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.00 | 0.00 | 0.00 |
| Jerry | 0.00 | 0.00 | 0.00 |
| Morty | 0.00 | 0.00 | 0.00 |
| Rick | 0.48 | 1.00 | 0.65 |
| Summer | 0.00 | 0.00 | 0.00 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.00 | 0.00 | 0.00 |
| Jerry | 0.00 | 0.00 | 0.00 |
| Morty | 0.00 | 0.00 | 0.00 |
| Rick | 0.42 | 1.00 | 0.59 |
| Summer | 0.00 | 0.00 | 0.00 |

### 🧠 Feature Extraction Methods

| Method | Importance |
| ------ | ---------- |
| Total Sentence Count | 0.1847 |
| Average Word Length | 0.0515 |
| Question Marks Per Sentence | 0.0000 |
| Exclamation Marks Per Sentence | 0.0000 |
| Average Root Verb Embedding (glove-twitter-25) | -0.0004 |
| Average Tokens Per Sentence | -0.0359 |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Uh, what? It was your job, Morty. | Rick | Summer |
| Oh, God, what’s going on now? | Rick | Beth |
| He bails on everybody! He bailed on Mom when she was a kid! He -- He bailed on tiny planet! And in case I never made this clear to you, Summer, he bailed on you. He left you to rot in a world that he ruined because he doesn't care! Because nobody's special to him, Summer, not even himself. So, if you really want your grandpa back, grab a shovel. The one that won't let you down is buried in your backyard! | Rick | Morty |
| Wow! A whole world populated by intelligent dogs. I wonder what it'll be like, Rick. | Rick | Morty |
| I'll cover that bet. I get it. | Rick | Morty |
| Whoa! Look! It's that lady with all that shit on her face like Worf from Star Trek! That was getting coffee! How did she get there! | Rick | Morty |
| Aw, geez. Okay. I guess I can skip history. What about Frank? I mean, shouldn't you unfreeze him? | Rick | Morty |
| Because you suck! You've been keeping your lip zipped about it since Grandpa got arrested, but the fact is, you're freaking stoked to bail on him. | Rick | Summer |
| No, you can't!  Jessica doesn't even know I exist! But—but, but forget about that, because you can't blow up humanity! | Rick | Morty |
| But can you help me get to my family? You know, at my house? | Rick | Morty |
| Alright! That's enough. You're talking about my species! We understand genocide, we do it sometimes! | Rick | Jerry |
| I am not putting my father in a home! He just came back into my life, and you want to grab him and stuff him under a mattress like last month's Victoria's Secret? | Rick | Beth |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Rick | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Rick | Jerry |
| I don't know, Rick. I can't leave school again. | Rick | Morty |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| Hello? Is anybody here?  Mr. President! | Rick | Morty |
| I'm sorry. It's just like the end of "Old Yeller. | Rick | Jerry |
| It's the Citadel of Ricks. All the different Ricks from all the different realities got together to hide here from the government. | Rick | Morty |
| How is praying going to help? | Rick | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| Aw! Oh, my God! He recognizes the other dogs on TV. | Rick | Summer |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Rick | Summer |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Rick | Jerry |
| Morty, stay out of this. You are obviously not capable of judging these situations on your own. | Rick | Jerry |
| I mean it's been shot. With a gun. | Rick | Beth |
| Sure thing! And I was kinda hoping that I could get a selfie with you? | Rick | Morty |
| Boom! Told you! In your face! He is ruining our child! Wait, what am I celebrating? | Rick | Jerry |
| Jerry, this was the most romantic weekend I've ever had. | Rick | Beth |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Rick | Jerry |
| Grandpa Rick wouldn't put up with this! | Rick | Summer |
| Oh, man, Rick. What is this place? | Rick | Morty |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| I don't know. I think like one sixty-fourth of my collars didn't work. It's hard to keep straight now that I have sixty-three other memories of everything. | Rick | Morty |
| Yeah, Rick... I-it's great. Is this the surprise? | Rick | Morty |
| Man, he sure says "bitch" a lot! | Rick | Morty |
| Well, I'm not calling him that. That's ridiculous. | Rick | Jerry |
| I didn't say my father is perfect, I said his work is important. | Rick | Beth |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Rick | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Rick | Summer |
| I don't care about Jessica! Y-Yyyyyyyyyyou— | Rick | Morty |
| Just focus on the mission, all right? | Rick | Morty |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Rick | Jerry |
| And then Ethan played guitar and we learned the Seven Contemplations of the Head by singing them. It was really fun. Praise be the head! | Rick | Summer |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Rick | Beth |
| Rick, this really bums me out. It-It's embarrassing to find out these guys don't like us. | Rick | Morty |
| Then what good was the "yes"? | Rick | Beth |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Rick | Beth |
| Whatever. How petty would I have to be to care less about an animal's life than my own ego? | Rick | Beth |
| That's enough! Drop the gun, Rick! | Rick | Morty |
| Okay, I only ask, Jerry, because, as you know, my job involves performing heart surgery. | Rick | Beth |
| What? What kind of monster are you? | Rick | Morty |
| We’ll take our chances raising her without fancy new jobs outside of a potato-based religion.  And you know what? I’m sick of pretending that we’re together because of the kids in the first place! I married you because you’re the love of my life! | Rick | Jerry |
| I'm looking at her. Thanks for F.D.'ing me up like that. | Rick | Jerry |
| I never said I was angry at you. | Rick | Summer |
| What? Why didn't you notify us? | Rick | Beth |
| This better not be a bribe. If I find a single thing out of place in this house, my love of ice cream won't save you. I'll get my jacket. | Rick | Jerry |
| What? Why are you looking at me? You want to go outside? Outside? | Rick | Jerry |
| Ow! Ow! You're tugging me too hard! | Rick | Morty |
| This article says the reason we weren't involved was... "personality conflicts". | Rick | Morty |
| Man, Grandpa Rick must have gotten shitfaced. | Rick | Summer |
| Rick? Are you far away, or are you inside something? | Rick | Morty |
| Sir, I need to get to the stage and help Rick get schwifty! | Rick | Morty |
| Doesn't feel so good, does it? | Rick | Morty |
| Go in the waiting room, Dad. | Rick | Beth |
| I AM a baby! I’m a baby NOW! | Rick | Jerry |
| Listen, Rick, if you're gonna stay here rent-free and use my son for your stupid science, the least you could do is put a little bit of it to use for the family. You make that dog smart or Morty's grounded! | Rick | Jerry |
| Oh, for crying out—he's got some kind of disability or something. Is that what you want us to say? | Rick | Jerry |
| Because Ricks hate themselves the most. And our Rick is the most himself. | Rick | Morty |
| Are you guys Power Rangers? But only on one small part of your necks? Hey, do those things need batteries? Were they included? Clean up in the fruit isle! Not in a homophobic way though, they're just fruity necklaces is all I was saying. | Rick | Jerry |
| There is no helicopter and there is no Cervine Institute. | Rick | Jerry |
| I don’t know what to say. Summer is doing really well here. | Rick | Beth |
| Aw, geez, dad. Y-you know, that's a lot to drop on a kid all at once. | Rick | Morty |
| What?! Why would you -- Look, we're running late. We have to go. | Rick | Beth |
| But.. she was trying to kill us! | Rick | Morty |
| What? N-No, I don't want to see your Pog collection. I don't renounce Rick, and I never have. I was just trying to protect my sister. I wanted you to have a normal life. That's something you can't have when Rick shows up. Everything real turns fake. Everything right is wrong. All you know is that you know nothing and he knows everything. And, well -- well, he's not a villain, Summer, but he shouldn't be your hero. He's more like a demon or a super fucked up god. | Rick | Morty |
| But I obviously sort of love you, don't I?  So stop asking and maybe I'll love you more.  Crap, They need me at the horse hospital. | Rick | Beth |
| Oh, my God! He's trying to tell us something.  That is so awesome. | Rick | Summer |
| Yeah, and what's courageous about eating a hot dog? | Rick | Morty |
| Now hold on a second, let’s be rational about this. | Rick | Beth |
### 📉 Individual Feature Importances

| Feature | Importance |
| ------- | ---------- |
| total_sentence_count | 0.18471549451351166 |
| avg_token_length | 0.05154585838317871 |
| n_root_verbs | 0.0006229778518900275 |
| n_root_verbs_embedded | 0.0005087554454803467 |
| avg_root_verb_embedding_6 | 5.760421117884107e-05 |
| avg_root_verb_embedding_1 | 1.891073588922154e-05 |
| question_marks_per_sentence | 0.0 |
| exclamation_marks_per_sentence | 0.0 |
| avg_root_verb_embedding_9 | 0.0 |
| avg_root_verb_embedding_8 | 0.0 |
| avg_root_verb_embedding_7 | 0.0 |
| avg_root_verb_embedding_5 | 0.0 |
| avg_root_verb_embedding_4 | 0.0 |
| avg_root_verb_embedding_3 | 0.0 |
| avg_root_verb_embedding_24 | 0.0 |
| avg_root_verb_embedding_0 | 0.0 |
| avg_root_verb_embedding_22 | 0.0 |
| avg_root_verb_embedding_21 | 0.0 |
| avg_root_verb_embedding_20 | 0.0 |
| avg_root_verb_embedding_2 | 0.0 |
| avg_root_verb_embedding_19 | 0.0 |
| avg_root_verb_embedding_18 | 0.0 |
| avg_root_verb_embedding_17 | 0.0 |
| avg_root_verb_embedding_16 | 0.0 |
| avg_root_verb_embedding_15 | 0.0 |
| avg_root_verb_embedding_14 | 0.0 |
| avg_root_verb_embedding_13 | 0.0 |
| avg_root_verb_embedding_11 | 0.0 |
| avg_root_verb_embedding_10 | 0.0 |
| avg_root_verb_embedding_23 | 0.0 |
| avg_root_verb_embedding_12 | -0.0015625841915607452 |
| avg_tokens_per_sentence | -0.035907041281461716 |
### 📉 Unused Features

26/32 features were unused.

| Feature | Coefficient |
| ------- | ----------- |
| avg_root_verb_embedding_0 | 0.0 |
| avg_root_verb_embedding_1 | 0.0 |
| avg_root_verb_embedding_10 | 0.0 |
| avg_root_verb_embedding_11 | 0.0 |
| avg_root_verb_embedding_12 | 0.0 |
| avg_root_verb_embedding_13 | 0.0 |
| avg_root_verb_embedding_14 | 0.0 |
| avg_root_verb_embedding_15 | 0.0 |
| avg_root_verb_embedding_17 | 0.0 |
| avg_root_verb_embedding_18 | 0.0 |
| avg_root_verb_embedding_19 | 0.0 |
| avg_root_verb_embedding_2 | 0.0 |
| avg_root_verb_embedding_20 | 0.0 |
| avg_root_verb_embedding_21 | 0.0 |
| avg_root_verb_embedding_22 | 0.0 |
| avg_root_verb_embedding_23 | 0.0 |
| avg_root_verb_embedding_24 | 0.0 |
| avg_root_verb_embedding_3 | 0.0 |
| avg_root_verb_embedding_4 | 0.0 |
| avg_token_length | 0.0 |
| avg_tokens_per_sentence | 0.0 |
| exclamation_marks_per_sentence | 0.0 |
| n_root_verbs | 0.0 |
| n_root_verbs_embedded | 0.0 |
| question_marks_per_sentence | 0.0 |
| total_sentence_count | 0.0 |
