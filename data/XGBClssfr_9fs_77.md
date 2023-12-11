### 🚀 **XGBClssfr_9fs_77**

- 🤖 **Model Type**: 
	<class 'xgboost.sklearn.XGBClassifier'>
- 📊 **Dataset Used**: 
	_Random_
- 🧠 **Number of Features**: 
	1323
- 🚫 **Unused Features**: 
	801/1323
- ⌛ **Model Train Time**: 
	7.279
- 💬 **SpaCy Preprocessing Model**: 
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `random_state`: 30
	- `max_depth`: 4
	- `objective`: multi:softmax
	- `num_class`: 5
	- `n_estimators`: 110
	- `min_child_weight`: 1
	- `gamma`: 0.1
	- `subsample`: 0.72
	- `colsample_bytree`: 0.72
	- `reg_lambda`: 1
	- `reg_alpha`: 4
	- `learning_rate`: 0.45
	- `alpha`: 0.64
	- `booster`: gbtree
	- `eta`: 0.66
	- `eval_metric`: mphe

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 0.988 | 0.561 | 0.515 |
| Macro F1 | 0.986 | 0.435 | 0.348 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.64 | 0.35 | 0.45 |
| Jerry | 0.33 | 0.22 | 0.27 |
| Morty | 0.43 | 0.62 | 0.51 |
| Rick | 0.68 | 0.73 | 0.70 |
| Summer | 0.40 | 0.18 | 0.25 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.50 | 0.29 | 0.36 |
| Jerry | 0.22 | 0.20 | 0.21 |
| Morty | 0.50 | 0.50 | 0.50 |
| Rick | 0.59 | 0.76 | 0.67 |
| Summer | 0.00 | 0.00 | 0.00 |

### 🧠 Feature Extraction Methods

| Method | Importance |
| ------ | ---------- |
| Nghbhood Degrees - Lemmas (.5decay,1topn,5nghbrs)(glove-twitter-50)(Rndm)(-blacklist) | 0.9917 |
| Proportion Of Tokens That Are Stop Words | 0.0017 |
| Average Word Length | 0.0014 |
| Exclamation Marks Per Sentence | 0.0014 |
| Dashes Per Sentence | 0.0012 |
| Question Marks Per Sentence | 0.0009 |
| Proportion Of Chars That Are Capitalized | 0.0008 |
| Topical Proximity - Intoxication (fasttext-wiki-news-subwords-300) | 0.0007 |
| Average Tokens Per Sentence | 0.0002 |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Uh, yeah, just a few more design notes.  Um, this guy. The, uh... The, uh... | Jerry | Rick |
| Uh, what? It was your job, Morty. | Rick | Summer |
| Oh, God, what’s going on now? | Summer | Beth |
| He bails on everybody! He bailed on Mom when she was a kid! He -- He bailed on tiny planet! And in case I never made this clear to you, Summer, he bailed on you. He left you to rot in a world that he ruined because he doesn't care! Because nobody's special to him, Summer, not even himself. So, if you really want your grandpa back, grab a shovel. The one that won't let you down is buried in your backyard! | Jerry | Morty |
| Don't worry about Jerry. He's gonna be fine.You hear me Jerry? You're gonna be fine! | Beth | Rick |
| Whoa! Look! It's that lady with all that shit on her face like Worf from Star Trek! That was getting coffee! How did she get there! | Rick | Morty |
| Hey! I said nobody move, buddy! | Morty | Rick |
| Me. I used to wear blue pants. | Morty | Rick |
| I would have been happy to pay for it, Summer, but they don't exactly sell them at Costco. Besides, there's a larger lesson to be learned here. Get him! | Jerry | Rick |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Rick | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Rick | Jerry |
| You don’t have to be a dick. | Morty | Rick |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| I'm sorry. It's just like the end of "Old Yeller. | Rick | Jerry |
| It's the Citadel of Ricks. All the different Ricks from all the different realities got together to hide here from the government. | Rick | Morty |
| How is praying going to help? | Summer | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| Aw! Oh, my God! He recognizes the other dogs on TV. | Morty | Summer |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Morty | Summer |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Morty | Jerry |
| Morty, stay out of this. You are obviously not capable of judging these situations on your own. | Rick | Jerry |
| I mean it's been shot. With a gun. | Morty | Beth |
| No idea what you're talking about. | Morty | Rick |
| Sure thing! And I was kinda hoping that I could get a selfie with you? | Jerry | Morty |
| Really? You don't say. You would have used a ghost train?  Hey, everybody, the ghost train guy would have used a ghost train! | Jerry | Rick |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Morty | Jerry |
| Grandpa Rick wouldn't put up with this! | Morty | Summer |
| Goldenfold, we're coming out! We just want to talk! | Morty | Rick |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| I don't know. I think like one sixty-fourth of my collars didn't work. It's hard to keep straight now that I have sixty-three other memories of everything. | Rick | Morty |
| - or sister I said any of this, I'll deny it - | Morty | Rick |
| Uh, w-why don't you get it Jerry? you're the man of the house and you don't have a job. | Morty | Rick |
| Well, I'm not calling him that. That's ridiculous. | Rick | Jerry |
| Sure. Why not? I don’t, I don't know. Y-you know what, Mo— | Morty | Rick |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Jerry | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Rick | Summer |
| Just focus on the mission, all right? | Rick | Morty |
| Seems like you guys need some privacy. I'll, uh -- I'll be in the garage. | Morty | Rick |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Rick | Jerry |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Morty | Beth |
| Did he say he never forgets a kid? | Morty | Rick |
| Yup, it really makes you appreciate how fickle the universe can be.   One minute you're falling off a roof for six months, the next minute, bam! | Jerry | Rick |
| Then what good was the "yes"? | Morty | Beth |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Rick | Beth |
| What? What kind of monster are you? | Beth | Morty |
| We’ll take our chances raising her without fancy new jobs outside of a potato-based religion.  And you know what? I’m sick of pretending that we’re together because of the kids in the first place! I married you because you’re the love of my life! | Rick | Jerry |
| I'm looking at her. Thanks for F.D.'ing me up like that. | Rick | Jerry |
| Huh, what do you know, it's working | Morty | Rick |
| Got some of that mermaid puss! | Summer | Rick |
| I never said I was angry at you. | Morty | Summer |
| What? Why didn't you notify us? | Rick | Beth |
| Whoa, whoa, whoa. Hold on, Vance. He said you'd die if you tried to leave. That means there's booby traps. | Morty | Rick |
| What? Why are you looking at me? You want to go outside? Outside? | Rick | Jerry |
| This article says the reason we weren't involved was... "personality conflicts". | Rick | Morty |
| Man, Grandpa Rick must have gotten shitfaced. | Morty | Summer |
| Doesn't feel so good, does it? | Rick | Morty |
| I AM a baby! I’m a baby NOW! | Morty | Jerry |
| Oldest Rick trick in the book. | Morty | Rick |
| Listen, Rick, if you're gonna stay here rent-free and use my son for your stupid science, the least you could do is put a little bit of it to use for the family. You make that dog smart or Morty's grounded! | Rick | Jerry |
| Oh, for crying out—he's got some kind of disability or something. Is that what you want us to say? | Rick | Jerry |
| Hey, I can't help if I can't see. | Beth | Rick |
| There is no helicopter and there is no Cervine Institute. | Morty | Jerry |
| I don’t know what to say. Summer is doing really well here. | Morty | Beth |
| What?! Why would you -- Look, we're running late. We have to go. | Jerry | Beth |
| Oh, my God! He's trying to tell us something.  That is so awesome. | Morty | Summer |
| Yeah, and what's courageous about eating a hot dog? | Beth | Morty |
| Now hold on a second, let’s be rational about this. | Rick | Beth |
### 📉 Individual Feature Importances

| Feature | Importance |
| ------- | ---------- |
| deg_of_presence(saget)_norm | 0.1187325268983841 |
| deg_of_presence(nelly)_norm | 0.01857340708374977 |
| deg_of_presence(sorry)_norm | 0.014341295696794987 |
| deg_of_presence(big)_norm | 0.012641431763768196 |
| deg_of_presence(thermodynamics)_norm | 0.01205807738006115 |
| deg_of_presence(nut)_norm | 0.011000052094459534 |
| deg_of_presence(lamer)_norm | 0.009999843314290047 |
| deg_of_presence(arbitrary)_norm | 0.009264955297112465 |
| deg_of_presence(wonderful)_norm | 0.007969235070049763 |
| deg_of_presence(vance)_norm | 0.00679662125185132 |
| deg_of_presence(shut)_norm | 0.00669774180278182 |
| deg_of_presence(hassle)_norm | 0.006446948274970055 |
| deg_of_presence(villain)_norm | 0.006137792486697435 |
| deg_of_presence(mutant)_norm | 0.00612489040941 |
| deg_of_presence(aw)_norm | 0.00604455778375268 |
| deg_of_presence(god)_norm | 0.0060051120817661285 |
| deg_of_presence(naked)_norm | 0.005995095241814852 |
| deg_of_presence(visualization)_norm | 0.005896575748920441 |
| ... | ... |
| deg_of_presence(month)_norm | 0.0 |
| deg_of_presence(morning)_norm | 0.0 |
| deg_of_presence(michael)_norm | 0.0 |
| deg_of_presence(create)_norm | 0.0 |
| deg_of_presence(mad)_norm | 0.0 |
| deg_of_presence(mention)_norm | 0.0 |
| deg_of_presence(make)_norm | 0.0 |
| deg_of_presence(mammal)_norm | 0.0 |
| deg_of_presence(man)_norm | 0.0 |
| deg_of_presence(manage)_norm | 0.0 |
| deg_of_presence(manager)_norm | 0.0 |
| deg_of_presence(crystal)_norm | 0.0 |
| deg_of_presence(cry)_norm | 0.0 |
| deg_of_presence(cruel)_norm | 0.0 |
| deg_of_presence(mate)_norm | 0.0 |
| deg_of_presence(crowd)_norm | 0.0 |
| deg_of_presence(matter)_norm | 0.0 |
| deg_of_presence(mattress)_norm | 0.0 |
| deg_of_presence(maybe)_norm | 0.0 |
| deg_of_presence(cross)_norm | 0.0 |
| deg_of_presence(meal)_norm | 0.0 |
| deg_of_presence(mean)_norm | 0.0 |
| deg_of_presence(measuring)_norm | 0.0 |
| deg_of_presence(medical)_norm | 0.0 |
| deg_of_presence(medicine)_norm | 0.0 |
| deg_of_presence(meet)_norm | 0.0 |
| deg_of_presence(creature)_norm | 0.0 |
| deg_of_presence(melt)_norm | 0.0 |
| deg_of_presence(mentally)_norm | 0.0 |
| deg_of_presence(learn)_norm | 0.0 |
