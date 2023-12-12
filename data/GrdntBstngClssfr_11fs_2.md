### 🚀 **GrdntBstngClssfr_11fs_2**

- 🤖 **Model Type**:
	<class 'sklearn.ensemble._gb.GradientBoostingClassifier'>
- 📊 **Dataset Used**:
	_Random_
- 🧠 **Number of Features**:
	1605
- 🚫 **Unused Features**:
	122/1605
- ⌛ **Model Train Time**:
	123.885
- 💬 **SpaCy Preprocessing Model**:
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `n_estimators`: 45
	- `learning_rate`: 0.21
	- `max_depth`: 8
	- `random_state`: 38

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 1.0 | 0.548 | 0.535 |
| Macro F1 | 1.0 | 0.405 | 0.379 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.29 | 0.20 | 0.24 |
| Jerry | 0.14 | 0.06 | 0.08 |
| Morty | 0.52 | 0.50 | 0.51 |
| Rick | 0.63 | 0.80 | 0.70 |
| Summer | 0.56 | 0.45 | 0.50 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.43 | 0.21 | 0.29 |
| Jerry | 0.00 | 0.00 | 0.00 |
| Morty | 0.64 | 0.50 | 0.56 |
| Rick | 0.61 | 0.81 | 0.69 |
| Summer | 0.30 | 0.43 | 0.35 |

### 🧠 Feature Extraction Methods

| Method | Importance |
| ------ | ---------- |
| Nghbhood Degrees - Lemmas (.5decay,4topn,8nghbrs)(fasttext-wiki-news-subwords-300)(Rndm) | 0.8950 |
| Familial Words & Common Names 1-Gram One Hots | 0.0488 |
| POS-Tag 2-Gram Counts | 0.0347 |
| Average Word Length | 0.0102 |
| Exclamation Marks Per Sentence | 0.0053 |
| Proportion Of Chars That Are Capitalized | 0.0023 |
| Dashes Per Sentence | 0.0019 |
| Proportion Of Tokens That Are Stop Words | 0.0013 |
| Question Marks Per Sentence | 0.0003 |
| Topical Proximity - Intoxication (fasttext-wiki-news-subwords-300) | 0.0001 |
| Average Tokens Per Sentence | 0.0000 |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Uh, yeah, just a few more design notes.  Um, this guy. The, uh... The, uh... | Morty | Rick |
| Uh, what? It was your job, Morty. | Morty | Summer |
| Oh, God, what’s going on now? | Rick | Beth |
| He bails on everybody! He bailed on Mom when she was a kid! He -- He bailed on tiny planet! And in case I never made this clear to you, Summer, he bailed on you. He left you to rot in a world that he ruined because he doesn't care! Because nobody's special to him, Summer, not even himself. So, if you really want your grandpa back, grab a shovel. The one that won't let you down is buried in your backyard! | Summer | Morty |
| I'll cover that bet. I get it. | Rick | Morty |
| Boy, you really got me up against a wall this time, Jerry. | Beth | Rick |
| Aw, geez. Okay. I guess I can skip history. What about Frank? I mean, shouldn't you unfreeze him? | Jerry | Morty |
| Because you suck! You've been keeping your lip zipped about it since Grandpa got arrested, but the fact is, you're freaking stoked to bail on him. | Rick | Summer |
| Me. I used to wear blue pants. | Beth | Rick |
| But can you help me get to my family? You know, at my house? | Beth | Morty |
| Alright! That's enough. You're talking about my species! We understand genocide, we do it sometimes! | Morty | Jerry |
| I am not putting my father in a home! He just came back into my life, and you want to grab him and stuff him under a mattress like last month's Victoria's Secret? | Jerry | Beth |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Morty | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Morty | Jerry |
| You don’t have to be a dick. | Morty | Rick |
| Man that guy is the Red Grin Grumble to pretending he knows what's going on.  Oh you agree, huh?  You like that Red Grin Grumble reference?  Well guess what? I made him up. You really are your father's children. Think for yourselves, don't be sheep. | Jerry | Rick |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| Hello? Is anybody here?  Mr. President! | Rick | Morty |
| I'm sorry. It's just like the end of "Old Yeller. | Rick | Jerry |
| It's the Citadel of Ricks. All the different Ricks from all the different realities got together to hide here from the government. | Rick | Morty |
| How is praying going to help? | Summer | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| Aw! Oh, my God! He recognizes the other dogs on TV. | Morty | Summer |
| - Because that's -- that's what this is all about, Morty. | Morty | Rick |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Rick | Jerry |
| Hey, what's wrong Morty? Oh, you're worried about your dad, huh? | Beth | Rick |
| Morty, stay out of this. You are obviously not capable of judging these situations on your own. | Rick | Jerry |
| I mean it's been shot. With a gun. | Rick | Beth |
| No idea what you're talking about. | Jerry | Rick |
| Sure thing! And I was kinda hoping that I could get a selfie with you? | Rick | Morty |
| Really? You don't say. You would have used a ghost train?  Hey, everybody, the ghost train guy would have used a ghost train! | Summer | Rick |
| Boom! Told you! In your face! He is ruining our child! Wait, what am I celebrating? | Morty | Jerry |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Rick | Jerry |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| I don't know. I think like one sixty-fourth of my collars didn't work. It's hard to keep straight now that I have sixty-three other memories of everything. | Rick | Morty |
| Uh, w-why don't you get it Jerry? you're the man of the house and you don't have a job. | Morty | Rick |
| Well, I'm not calling him that. That's ridiculous. | Summer | Jerry |
| I didn't say my father is perfect, I said his work is important. | Rick | Beth |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Rick | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Rick | Summer |
| All right, all right, calm down. Listen to me, Morty. I know that new situations can be intimidating. You're looking around, and it's all scary and different, but, you know, m-meeting them head on, charging right into them like a bull that's how we grow as people. I'm no stranger to scary situations. I deal with them all the time. Now, if you just stick with me, Morty, we're gonna be— | Morty | Rick |
| Just focus on the mission, all right? | Beth | Morty |
| Seems like you guys need some privacy. I'll, uh -- I'll be in the garage. | Jerry | Rick |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Rick | Jerry |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Morty | Beth |
| Then what good was the "yes"? | Rick | Beth |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Rick | Beth |
| What? What kind of monster are you? | Rick | Morty |
| We’ll take our chances raising her without fancy new jobs outside of a potato-based religion.  And you know what? I’m sick of pretending that we’re together because of the kids in the first place! I married you because you’re the love of my life! | Rick | Jerry |
| I never said I was angry at you. | Jerry | Summer |
| What? Why didn't you notify us? | Morty | Beth |
| This better not be a bribe. If I find a single thing out of place in this house, my love of ice cream won't save you. I'll get my jacket. | Rick | Jerry |
| What? Why are you looking at me? You want to go outside? Outside? | Rick | Jerry |
| This article says the reason we weren't involved was... "personality conflicts". | Rick | Morty |
| Doesn't feel so good, does it? | Rick | Morty |
| Go in the waiting room, Dad. | Rick | Beth |
| I AM a baby! I’m a baby NOW! | Beth | Jerry |
| Oldest Rick trick in the book. | Morty | Rick |
| Listen, Rick, if you're gonna stay here rent-free and use my son for your stupid science, the least you could do is put a little bit of it to use for the family. You make that dog smart or Morty's grounded! | Rick | Jerry |
| Oh, for crying out—he's got some kind of disability or something. Is that what you want us to say? | Rick | Jerry |
| Alan, I'm not proud of what's happening here, but if you keep coming at me, there's gonna be another passenger on that ghost train. | Morty | Rick |
| Are you guys Power Rangers? But only on one small part of your necks? Hey, do those things need batteries? Were they included? Clean up in the fruit isle! Not in a homophobic way though, they're just fruity necklaces is all I was saying. | Beth | Jerry |
| Hey, I can't help if I can't see. | Beth | Rick |
| There is no helicopter and there is no Cervine Institute. | Beth | Jerry |
| I don’t know what to say. Summer is doing really well here. | Rick | Beth |
| What? N-No, I don't want to see your Pog collection. I don't renounce Rick, and I never have. I was just trying to protect my sister. I wanted you to have a normal life. That's something you can't have when Rick shows up. Everything real turns fake. Everything right is wrong. All you know is that you know nothing and he knows everything. And, well -- well, he's not a villain, Summer, but he shouldn't be your hero. He's more like a demon or a super fucked up god. | Rick | Morty |
| But I obviously sort of love you, don't I?  So stop asking and maybe I'll love you more.  Crap, They need me at the horse hospital. | Rick | Beth |
| Yeah, and what's courageous about eating a hot dog? | Beth | Morty |
| Now hold on a second, let’s be rational about this. | Rick | Beth |
### 📉 Individual Feature Importances

| Feature | Importance |
| ------- | ---------- |
| deg_of_presence(rick)_norm | 0.06039502875518364 |
| has(morty) | 0.02836318205696125 |
| deg_of_presence(arc)_norm | 0.02664670943761585 |
| deg_of_presence(grandpa)_norm | 0.025345599452676826 |
| deg_of_presence(kool)_norm | 0.019741180285198695 |
| deg_of_presence(sanchez)_norm | 0.01928849566604045 |
| has('PUNCT PROPN') | 0.01554673449097489 |
| deg_of_presence(phone)_norm | 0.015228922333918836 |
| has(jerry) | 0.013419838530317616 |
| deg_of_presence(vance)_norm | 0.012917492670052195 |
| deg_of_presence(privately)_norm | 0.011880358733470608 |
| deg_of_presence(darkest)_norm | 0.011504600050387689 |
| deg_of_presence(miniature)_norm | 0.01130450762713272 |
| deg_of_presence(a-)_norm | 0.01023182501565262 |
| avg_token_length | 0.010194901919941074 |
| deg_of_presence(ha)_norm | 0.008186387442113544 |
| deg_of_presence(gaga)_norm | 0.008111867957250872 |
| deg_of_presence(open)_norm | 0.008030939132084948 |
| ... | ... |
| has('DET SPACE') | 0.0 |
| has('SPACE ADJ') | 0.0 |
| has('SCONJ VERB') | 0.0 |
| has('SCONJ SPACE') | 0.0 |
| has('SCONJ SCONJ') | 0.0 |
| has('SCONJ PUNCT') | 0.0 |
| has('DET ADJ') | 0.0 |
| has('DET DET') | 0.0 |
| has('SCONJ NUM') | 0.0 |
| has('SCONJ NOUN') | 0.0 |
| has('SCONJ DET') | 0.0 |
| has('DET NUM') | 0.0 |
| has('SCONJ ADV') | 0.0 |
| has('DET PUNCT') | 0.0 |
| has('PUNCT X') | 0.0 |
| has('NOUN SCONJ') | 0.0 |
| has('DET VERB') | 0.0 |
| has('DET X') | 0.0 |
| has('INTJ ADJ') | 0.0 |
| has('INTJ ADP') | 0.0 |
| has('INTJ ADV') | 0.0 |
| has('INTJ AUX') | 0.0 |
| has('INTJ DET') | 0.0 |
| has('INTJ NUM') | 0.0 |
| has('INTJ PROPN') | 0.0 |
| has('INTJ VERB') | 0.0 |
| has('NOUN ADJ') | 0.0 |
| has('NOUN NOUN') | 0.0 |
| has('NOUN PRON') | 0.0 |
| has('PRON PROPN') | 0.0 |
