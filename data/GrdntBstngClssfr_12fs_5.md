### 🚀 **GrdntBstngClssfr_12fs_5**

- 🤖 **Model Type**: 
	<class 'sklearn.ensemble._gb.GradientBoostingClassifier'>
- 📊 **Dataset Used**: 
	_Random_
- 🧠 **Number of Features**: 
	3799
- 🚫 **Unused Features**: 
	2997/3799
- ⌛ **Model Train Time**: 
	96.721
- 💬 **SpaCy Preprocessing Model**: 
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `n_estimators`: 68
	- `learning_rate`: 0.3
	- `max_depth`: 3
	- `random_state`: 48

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 1.0 | 0.568 | 0.475 |
| Macro F1 | 1.0 | 0.397 | 0.269 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.80 | 0.20 | 0.32 |
| Jerry | 0.20 | 0.11 | 0.14 |
| Morty | 0.46 | 0.53 | 0.49 |
| Rick | 0.67 | 0.84 | 0.74 |
| Summer | 0.30 | 0.27 | 0.29 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.22 | 0.14 | 0.17 |
| Jerry | 0.00 | 0.00 | 0.00 |
| Morty | 0.50 | 0.61 | 0.55 |
| Rick | 0.57 | 0.69 | 0.62 |
| Summer | 0.00 | 0.00 | 0.00 |

### 🧠 Feature Extraction Methods

| Method | Importance |
| ------ | ---------- |
| Nghbhood Degrees - Lemmas (.5decay,4topn,8nghbrs)(glove-twitter-50)(Rndm)(-blacklist) | 0.6328 |
| All 2-Gram Counts (Normalized) | 0.1544 |
| Average Root Verb Embedding (fasttext-wiki-news-subwords-300) | 0.1483 |
| Familial Words & Common Names 1-Gram Counts | 0.0229 |
| Average Word Length | 0.0141 |
| Exclamation Marks Per Sentence | 0.0120 |
| Topical Proximity - Food (glove-wiki-gigaword-50) | 0.0083 |
| Proportion Of Tokens That Are Stop Words | 0.0046 |
| Proportion Of Chars That Are Capitalized | 0.0013 |
| Dashes Per Sentence | 0.0013 |
| Average Tokens Per Sentence | 0.0000 |
| Question Marks Per Sentence | 0.0000 |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Uh, what? It was your job, Morty. | Rick | Summer |
| Oh, God, what’s going on now? | Summer | Beth |
| He bails on everybody! He bailed on Mom when she was a kid! He -- He bailed on tiny planet! And in case I never made this clear to you, Summer, he bailed on you. He left you to rot in a world that he ruined because he doesn't care! Because nobody's special to him, Summer, not even himself. So, if you really want your grandpa back, grab a shovel. The one that won't let you down is buried in your backyard! | Rick | Morty |
| Don't worry about Jerry. He's gonna be fine.You hear me Jerry? You're gonna be fine! | Morty | Rick |
| Whoa! Look! It's that lady with all that shit on her face like Worf from Star Trek! That was getting coffee! How did she get there! | Rick | Morty |
| Hey! I said nobody move, buddy! | Morty | Rick |
| Me. I used to wear blue pants. | Morty | Rick |
| I would have been happy to pay for it, Summer, but they don't exactly sell them at Costco. Besides, there's a larger lesson to be learned here. Get him! | Jerry | Rick |
| Alright! That's enough. You're talking about my species! We understand genocide, we do it sometimes! | Morty | Jerry |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Rick | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Morty | Jerry |
| You don’t have to be a dick. | Summer | Rick |
| Man that guy is the Red Grin Grumble to pretending he knows what's going on.  Oh you agree, huh?  You like that Red Grin Grumble reference?  Well guess what? I made him up. You really are your father's children. Think for yourselves, don't be sheep. | Jerry | Rick |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| I'm sorry. It's just like the end of "Old Yeller. | Rick | Jerry |
| It's the Citadel of Ricks. All the different Ricks from all the different realities got together to hide here from the government. | Rick | Morty |
| Aw! Oh, my God! He recognizes the other dogs on TV. | Morty | Summer |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Morty | Summer |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Morty | Jerry |
| Morty, stay out of this. You are obviously not capable of judging these situations on your own. | Summer | Jerry |
| I mean it's been shot. With a gun. | Morty | Beth |
| No idea what you're talking about. | Morty | Rick |
| Sure thing! And I was kinda hoping that I could get a selfie with you? | Rick | Morty |
| Boom! Told you! In your face! He is ruining our child! Wait, what am I celebrating? | Morty | Jerry |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Rick | Jerry |
| Grandpa Rick wouldn't put up with this! | Morty | Summer |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| I don't know. I think like one sixty-fourth of my collars didn't work. It's hard to keep straight now that I have sixty-three other memories of everything. | Rick | Morty |
| - or sister I said any of this, I'll deny it - | Morty | Rick |
| Well, I'm not calling him that. That's ridiculous. | Rick | Jerry |
| Sure. Why not? I don’t, I don't know. Y-you know what, Mo— | Morty | Rick |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Rick | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Rick | Summer |
| I don't care about Jessica! Y-Yyyyyyyyyyou— | Summer | Morty |
| Just focus on the mission, all right? | Rick | Morty |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Rick | Jerry |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Jerry | Beth |
| Then what good was the "yes"? | Jerry | Beth |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Rick | Beth |
| Whatever. How petty would I have to be to care less about an animal's life than my own ego? | Rick | Beth |
| Okay, I only ask, Jerry, because, as you know, my job involves performing heart surgery. | Jerry | Beth |
| What? What kind of monster are you? | Rick | Morty |
| We’ll take our chances raising her without fancy new jobs outside of a potato-based religion.  And you know what? I’m sick of pretending that we’re together because of the kids in the first place! I married you because you’re the love of my life! | Rick | Jerry |
| I never said I was angry at you. | Morty | Summer |
| What? Why didn't you notify us? | Summer | Beth |
| What? Why are you looking at me? You want to go outside? Outside? | Rick | Jerry |
| I don't either. I-I'm just saying, if anything, the drunk version of me is probably so supportive of Israel, he wants what's best for it and... | Summer | Rick |
| This article says the reason we weren't involved was... "personality conflicts". | Summer | Morty |
| Man, Grandpa Rick must have gotten shitfaced. | Morty | Summer |
| Doesn't feel so good, does it? | Rick | Morty |
| Who cares about the  thing you guys are talking about? The whole point of freezing time is to stop giving a fuck. Put a shirt on your dumb dad and let's get this dumb universe rolling. Let's do this thing. | Beth | Rick |
| Go in the waiting room, Dad. | Morty | Beth |
| I AM a baby! I’m a baby NOW! | Morty | Jerry |
| Listen, Rick, if you're gonna stay here rent-free and use my son for your stupid science, the least you could do is put a little bit of it to use for the family. You make that dog smart or Morty's grounded! | Rick | Jerry |
| Oh, for crying out—he's got some kind of disability or something. Is that what you want us to say? | Rick | Jerry |
| Because Ricks hate themselves the most. And our Rick is the most himself. | Rick | Morty |
| Are you guys Power Rangers? But only on one small part of your necks? Hey, do those things need batteries? Were they included? Clean up in the fruit isle! Not in a homophobic way though, they're just fruity necklaces is all I was saying. | Rick | Jerry |
| Hey, I can't help if I can't see. | Morty | Rick |
| There is no helicopter and there is no Cervine Institute. | Rick | Jerry |
| I don’t know what to say. Summer is doing really well here. | Jerry | Beth |
| What?! Why would you -- Look, we're running late. We have to go. | Morty | Beth |
| But.. she was trying to kill us! | Rick | Morty |
| What? N-No, I don't want to see your Pog collection. I don't renounce Rick, and I never have. I was just trying to protect my sister. I wanted you to have a normal life. That's something you can't have when Rick shows up. Everything real turns fake. Everything right is wrong. All you know is that you know nothing and he knows everything. And, well -- well, he's not a villain, Summer, but he shouldn't be your hero. He's more like a demon or a super fucked up god. | Rick | Morty |
| But I obviously sort of love you, don't I?  So stop asking and maybe I'll love you more.  Crap, They need me at the horse hospital. | Jerry | Beth |
| Yeah, and what's courageous about eating a hot dog? | Rick | Morty |
| Now hold on a second, let’s be rational about this. | Jerry | Beth |
### 📉 Individual Feature Importances

| Feature | Importance |
| ------- | ---------- |
| deg_of_presence(morty)_norm | 0.09195188121384618 |
| deg_of_presence(rick)_norm | 0.07471611109757552 |
| avg_token_length | 0.014137848698063952 |
| count(jerry) | 0.01364163113524206 |
| deg_of_presence(evangelical)_norm | 0.013423259277319253 |
| exclamation_marks_per_sentence | 0.011992092306204846 |
| deg_of_presence(akbar)_norm | 0.011914983822472008 |
| deg_of_presence(domination)_norm | 0.010202445200179336 |
| avg_root_verb_embedding_91 | 0.009876047359431763 |
| deg_of_presence(drunkenly)_norm | 0.009784391122183728 |
| deg_of_presence(grandson)_norm | 0.009408392011909369 |
| deg_of_presence(murder)_norm | 0.00874459993285493 |
| avg_root_verb_embedding_4 | 0.00832751696251013 |
| topical_proximity_food | 0.00829078650498553 |
| deg_of_presence(garcia)_norm | 0.008140139882249894 |
| deg_of_presence(nurse)_norm | 0.007739203031906339 |
| deg_of_presence(ricks)_norm | 0.007323913955810459 |
| deg_of_presence(yike)_norm | 0.007312624602559446 |
| ... | ... |
| count(negative nelly) | 0.0 |
| count(nelly morty) | 0.0 |
| count(nervous schwifty) | 0.0 |
| count(new adam) | 0.0 |
| count(new machine) | 0.0 |
| count(nailed time) | 0.0 |
| count(na wanna) | 0.0 |
| count(na able) | 0.0 |
| count(<START> smart) | 0.0 |
| count(na adam) | 0.0 |
| count(na best) | 0.0 |
| count(na clear) | 0.0 |
| count(na customs) | 0.0 |
| count(na die) | 0.0 |
| count(na dressed) | 0.0 |
| count(na fine) | 0.0 |
| count(na good) | 0.0 |
| count(na great) | 0.0 |
| count(na help) | 0.0 |
| count(na touch) | 0.0 |
| count(na home) | 0.0 |
| count(na interdimensional) | 0.0 |
| count(na let) | 0.0 |
| count(<START> shut) | 0.0 |
| count(na need) | 0.0 |
| count(na real) | 0.0 |
| count(na soon) | 0.0 |
| count(na stand) | 0.0 |
| count(na tell) | 0.0 |
| count(rage gets) | 0.0 |
