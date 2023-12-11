### 🚀 **GrdntBstngClssfr_7fs_1**

- 🤖 **Model Type**: 
	<class 'sklearn.ensemble._gb.GradientBoostingClassifier'>
- 📊 **Dataset Used**: 
	_Random_
- 🧠 **Number of Features**: 
	4666
- 🚫 **Unused Features**: 
	3386/4666
- ⌛ **Model Train Time**: 
	78.264
- 💬 **SpaCy Preprocessing Model**: 
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `n_estimators`: 45
	- `learning_rate`: 0.2
	- `max_depth`: 5
	- `random_state`: 42

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 1.0 | 0.561 | 0.475 |
| Macro F1 | 1.0 | 0.436 | 0.296 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.50 | 0.20 | 0.29 |
| Jerry | 0.22 | 0.11 | 0.15 |
| Morty | 0.43 | 0.62 | 0.51 |
| Rick | 0.67 | 0.76 | 0.71 |
| Summer | 0.62 | 0.45 | 0.53 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.33 | 0.29 | 0.31 |
| Jerry | 0.00 | 0.00 | 0.00 |
| Morty | 0.54 | 0.54 | 0.54 |
| Rick | 0.59 | 0.69 | 0.64 |
| Summer | 0.00 | 0.00 | 0.00 |

### 🧠 Feature Extraction Methods

| Method | Importance |
| ------ | ---------- |
| Nghbhood Degrees - Lemmas (.5decay,1topn,5nghbrs)(glove-twitter-50)(Rndm) | 0.7456 |
| Average Root Verb Embedding (fasttext-wiki-news-subwords-300) | 0.1755 |
| All 2-Gram One Hots | 0.0538 |
| Average Word Length | 0.0102 |
| Proportion Of Tokens That Are Stop Words | 0.0079 |
| Exclamation Marks Per Sentence | 0.0067 |
| Dashes Per Sentence | 0.0003 |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Uh, yeah, just a few more design notes.  Um, this guy. The, uh... The, uh... | Morty | Rick |
| Uh, what? It was your job, Morty. | Rick | Summer |
| Oh, God, what’s going on now? | Summer | Beth |
| He bails on everybody! He bailed on Mom when she was a kid! He -- He bailed on tiny planet! And in case I never made this clear to you, Summer, he bailed on you. He left you to rot in a world that he ruined because he doesn't care! Because nobody's special to him, Summer, not even himself. So, if you really want your grandpa back, grab a shovel. The one that won't let you down is buried in your backyard! | Jerry | Morty |
| Don't worry about Jerry. He's gonna be fine.You hear me Jerry? You're gonna be fine! | Beth | Rick |
| I'll cover that bet. I get it. | Rick | Morty |
| Hey! I said nobody move, buddy! | Morty | Rick |
| Me. I used to wear blue pants. | Morty | Rick |
| But can you help me get to my family? You know, at my house? | Beth | Morty |
| Alright! That's enough. You're talking about my species! We understand genocide, we do it sometimes! | Morty | Jerry |
| I am not putting my father in a home! He just came back into my life, and you want to grab him and stuff him under a mattress like last month's Victoria's Secret? | Rick | Beth |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Morty | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Morty | Jerry |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| I'm sorry. It's just like the end of "Old Yeller. | Rick | Jerry |
| Is there coffee? Hey, Morty, can you be a pal? Grandpa left his coffee maker on the ship. Y-You know, the French press thing? | Summer | Rick |
| It's the Citadel of Ricks. All the different Ricks from all the different realities got together to hide here from the government. | Rick | Morty |
| How is praying going to help? | Morty | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Morty | Summer |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Morty | Jerry |
| Morty, stay out of this. You are obviously not capable of judging these situations on your own. | Rick | Jerry |
| I mean it's been shot. With a gun. | Morty | Beth |
| No idea what you're talking about. | Jerry | Rick |
| Sure thing! And I was kinda hoping that I could get a selfie with you? | Jerry | Morty |
| Boom! Told you! In your face! He is ruining our child! Wait, what am I celebrating? | Beth | Jerry |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Morty | Jerry |
| Grandpa Rick wouldn't put up with this! | Morty | Summer |
| Goldenfold, we're coming out! We just want to talk! | Morty | Rick |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| I don't know. I think like one sixty-fourth of my collars didn't work. It's hard to keep straight now that I have sixty-three other memories of everything. | Rick | Morty |
| - or sister I said any of this, I'll deny it - | Morty | Rick |
| Well, I'm not calling him that. That's ridiculous. | Morty | Jerry |
| Sure. Why not? I don’t, I don't know. Y-you know what, Mo— | Morty | Rick |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Rick | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Rick | Summer |
| Just focus on the mission, all right? | Rick | Morty |
| Seems like you guys need some privacy. I'll, uh -- I'll be in the garage. | Morty | Rick |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Rick | Jerry |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Jerry | Beth |
| Did he say he never forgets a kid? | Morty | Rick |
| Then what good was the "yes"? | Morty | Beth |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Rick | Beth |
| Whatever. How petty would I have to be to care less about an animal's life than my own ego? | Rick | Beth |
| Okay, I only ask, Jerry, because, as you know, my job involves performing heart surgery. | Jerry | Beth |
| What? What kind of monster are you? | Rick | Morty |
| We’ll take our chances raising her without fancy new jobs outside of a potato-based religion.  And you know what? I’m sick of pretending that we’re together because of the kids in the first place! I married you because you’re the love of my life! | Rick | Jerry |
| I'm looking at her. Thanks for F.D.'ing me up like that. | Morty | Jerry |
| Huh, what do you know, it's working | Morty | Rick |
| I never said I was angry at you. | Morty | Summer |
| Whoa, whoa, whoa. Hold on, Vance. He said you'd die if you tried to leave. That means there's booby traps. | Morty | Rick |
| What? Why are you looking at me? You want to go outside? Outside? | Rick | Jerry |
| This article says the reason we weren't involved was... "personality conflicts". | Rick | Morty |
| And they'll fall right out of mine. I've done this too many times, Morty. I mean, you're young. Y-y-you've got your whole life ahead of you, and your anal cavity is still taut, yet malleable. You got to do it for grandpa, Morty. Y-  you've got to put these seeds inside your butt. | Summer | Rick |
| Little extra  snippy this morning, aren't you? | Jerry | Rick |
| Who cares about the  thing you guys are talking about? The whole point of freezing time is to stop giving a fuck. Put a shirt on your dumb dad and let's get this dumb universe rolling. Let's do this thing. | Beth | Rick |
| Go in the waiting room, Dad. | Morty | Beth |
| Oldest Rick trick in the book. | Morty | Rick |
| Listen, Rick, if you're gonna stay here rent-free and use my son for your stupid science, the least you could do is put a little bit of it to use for the family. You make that dog smart or Morty's grounded! | Rick | Jerry |
| Oh, for crying out—he's got some kind of disability or something. Is that what you want us to say? | Rick | Jerry |
| Are you guys Power Rangers? But only on one small part of your necks? Hey, do those things need batteries? Were they included? Clean up in the fruit isle! Not in a homophobic way though, they're just fruity necklaces is all I was saying. | Rick | Jerry |
| Hey, I can't help if I can't see. | Morty | Rick |
| There is no helicopter and there is no Cervine Institute. | Rick | Jerry |
| I don’t know what to say. Summer is doing really well here. | Morty | Beth |
| What?! Why would you -- Look, we're running late. We have to go. | Rick | Beth |
| Yeah, and what's courageous about eating a hot dog? | Jerry | Morty |
| Now hold on a second, let’s be rational about this. | Rick | Beth |
### 📉 Individual Feature Importances

| Feature | Importance |
| ------- | ---------- |
| deg_of_presence(shoney)_norm | 0.11177044919033756 |
| deg_of_presence(rick)_norm | 0.05073881886155905 |
| deg_of_presence(nelly)_norm | 0.020631439003653433 |
| deg_of_presence(jerry)_norm | 0.013726034813907531 |
| deg_of_presence(evangelical)_norm | 0.013117145343099958 |
| deg_of_presence(nuke)_norm | 0.012063297859976643 |
| deg_of_presence(caesar)_norm | 0.011442552967601795 |
| avg_token_length | 0.010222138285253732 |
| deg_of_presence(hole)_norm | 0.01014705250210086 |
| deg_of_presence(art)_norm | 0.009955522932264305 |
| avg_root_verb_embedding_71 | 0.009272930801718373 |
| deg_of_presence(grampa)_norm | 0.008793672730137227 |
| proportion_stop_words | 0.007949862043885956 |
| deg_of_presence(wong)_norm | 0.007779093919798389 |
| deg_of_presence(parent)_norm | 0.00745435879882945 |
| deg_of_presence(honey)_norm | 0.0068459809723353865 |
| exclamation_marks_per_sentence | 0.0067275955605181495 |
| deg_of_presence(choice)_norm | 0.006084472147544807 |
| ... | ... |
| has(come help) | 0.0 |
| has(come hotel) | 0.0 |
| has(clear communication) | 0.0 |
| has(cleaning <END>) | 0.0 |
| has(chance dud) | 0.0 |
| has(classes dragging) | 0.0 |
| has(chance eventually) | 0.0 |
| has(chance sort) | 0.0 |
| has(changed <END>) | 0.0 |
| has(changing zero) | 0.0 |
| has(character miniature) | 0.0 |
| has(charge left) | 0.0 |
| has(cheap insect) | 0.0 |
| has(check gear) | 0.0 |
| has(chemical thing) | 0.0 |
| has(cherry garcia) | 0.0 |
| has(child needs) | 0.0 |
| has(children honor) | 0.0 |
| has(choking death) | 0.0 |
| has(choose c) | 0.0 |
| has(chores complete) | 0.0 |
| has(christmas <END>) | 0.0 |
| has(citadel place) | 0.0 |
| has(citadel stupid) | 0.0 |
| has(city atlantis) | 0.0 |
| has(class <END>) | 0.0 |
| has(class instead) | 0.0 |
| has(class look) | 0.0 |
| has(classes <END>) | 0.0 |
| has(code uploaded) | 0.0 |
