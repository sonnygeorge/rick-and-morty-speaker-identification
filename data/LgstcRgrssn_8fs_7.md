### 🚀 **LgstcRgrssn_8fs_7**

- 🤖 **Model Type**: 
	<class 'sklearn.linear_model._logistic.LogisticRegression'>
- 📊 **Dataset Used**: 
	_Random_
- 🧠 **Number of Features**: 
	1331
- 🚫 **Unused Features**: 
	0/1331
- ⌛ **Model Train Time**: 
	0.285
- 💬 **SpaCy Preprocessing Model**: 
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `random_state`: 42

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 0.638 | 0.548 | 0.475 |
| Macro F1 | 0.534 | 0.401 | 0.37 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.62 | 0.25 | 0.36 |
| Jerry | 0.25 | 0.17 | 0.20 |
| Morty | 0.40 | 0.56 | 0.47 |
| Rick | 0.66 | 0.77 | 0.71 |
| Summer | 0.50 | 0.18 | 0.27 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.43 | 0.21 | 0.29 |
| Jerry | 0.50 | 0.30 | 0.37 |
| Morty | 0.33 | 0.39 | 0.36 |
| Rick | 0.59 | 0.71 | 0.65 |
| Summer | 0.25 | 0.14 | 0.18 |

### 🧠 Feature Extraction Methods

| Method |
| ------ |
| Total Sentence Count |
| Average Tokens Per Sentence |
| Average Word Length |
| Exclamation Marks Per Sentence |
| Dashes Per Sentence |
| Proportion Of Tokens That Are Stop Words |
| Proportion Of Chars That Are Capitalized |
| Nghbhood Degrees - Lemmas (.5decay,4topn,5nghbrs)(glove-twitter-50)(Rndm) |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Uh, yeah, just a few more design notes.  Um, this guy. The, uh... The, uh... | Morty | Rick |
| Uh, what? It was your job, Morty. | Rick | Summer |
| Oh, God, what’s going on now? | Morty | Beth |
| Don't worry about Jerry. He's gonna be fine.You hear me Jerry? You're gonna be fine! | Morty | Rick |
| Whoa! Look! It's that lady with all that shit on her face like Worf from Star Trek! That was getting coffee! How did she get there! | Rick | Morty |
| Boy, you really got me up against a wall this time, Jerry. | Morty | Rick |
| Aw, geez. Okay. I guess I can skip history. What about Frank? I mean, shouldn't you unfreeze him? | Rick | Morty |
| Because you suck! You've been keeping your lip zipped about it since Grandpa got arrested, but the fact is, you're freaking stoked to bail on him. | Rick | Summer |
| Hey! I said nobody move, buddy! | Morty | Rick |
| But can you help me get to my family? You know, at my house? | Beth | Morty |
| I would have been happy to pay for it, Summer, but they don't exactly sell them at Costco. Besides, there's a larger lesson to be learned here. Get him! | Jerry | Rick |
| Alright! That's enough. You're talking about my species! We understand genocide, we do it sometimes! | Morty | Jerry |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Morty | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Morty | Jerry |
| Man that guy is the Red Grin Grumble to pretending he knows what's going on.  Oh you agree, huh?  You like that Red Grin Grumble reference?  Well guess what? I made him up. You really are your father's children. Think for yourselves, don't be sheep. | Jerry | Rick |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| I'm sorry. It's just like the end of "Old Yeller. | Rick | Jerry |
| It's the Citadel of Ricks. All the different Ricks from all the different realities got together to hide here from the government. | Rick | Morty |
| How is praying going to help? | Summer | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| The day I invented the portal gun is the day I lost her. | Jerry | Rick |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Morty | Summer |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Morty | Jerry |
| Morty, stay out of this. You are obviously not capable of judging these situations on your own. | Rick | Jerry |
| I mean it's been shot. With a gun. | Rick | Beth |
| Sure thing! And I was kinda hoping that I could get a selfie with you? | Rick | Morty |
| Boom! Told you! In your face! He is ruining our child! Wait, what am I celebrating? | Summer | Jerry |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Morty | Jerry |
| Grandpa Rick wouldn't put up with this! | Morty | Summer |
| Goldenfold, we're coming out! We just want to talk! | Morty | Rick |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| I don't know. I think like one sixty-fourth of my collars didn't work. It's hard to keep straight now that I have sixty-three other memories of everything. | Rick | Morty |
| - or sister I said any of this, I'll deny it - | Morty | Rick |
| Uh, w-why don't you get it Jerry? you're the man of the house and you don't have a job. | Morty | Rick |
| Well, I'm not calling him that. That's ridiculous. | Rick | Jerry |
| I didn't say my father is perfect, I said his work is important. | Jerry | Beth |
| Sure. Why not? I don’t, I don't know. Y-you know what, Mo— | Morty | Rick |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Rick | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Rick | Summer |
| Just focus on the mission, all right? | Rick | Morty |
| Seems like you guys need some privacy. I'll, uh -- I'll be in the garage. | Morty | Rick |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Rick | Jerry |
| And then Ethan played guitar and we learned the Seven Contemplations of the Head by singing them. It was really fun. Praise be the head! | Morty | Summer |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Morty | Beth |
| Did he say he never forgets a kid? | Beth | Rick |
| Yup, it really makes you appreciate how fickle the universe can be.   One minute you're falling off a roof for six months, the next minute, bam! | Morty | Rick |
| Then what good was the "yes"? | Jerry | Beth |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Rick | Beth |
| What? What kind of monster are you? | Rick | Morty |
| Huh, what do you know, it's working | Morty | Rick |
| I never said I was angry at you. | Morty | Summer |
| What? Why didn't you notify us? | Rick | Beth |
| What? Why are you looking at me? You want to go outside? Outside? | Morty | Jerry |
| This article says the reason we weren't involved was... "personality conflicts". | Rick | Morty |
| I AM a baby! I’m a baby NOW! | Morty | Jerry |
| Listen, Rick, if you're gonna stay here rent-free and use my son for your stupid science, the least you could do is put a little bit of it to use for the family. You make that dog smart or Morty's grounded! | Rick | Jerry |
| Oh, for crying out—he's got some kind of disability or something. Is that what you want us to say? | Rick | Jerry |
| Alright. I'll-I'll land. I'll land. I'll land. I'll land the thing. I’ll land the thing. Big tough guy all of a sudden. | Morty | Rick |
| Because Ricks hate themselves the most. And our Rick is the most himself. | Rick | Morty |
| Are you guys Power Rangers? But only on one small part of your necks? Hey, do those things need batteries? Were they included? Clean up in the fruit isle! Not in a homophobic way though, they're just fruity necklaces is all I was saying. | Rick | Jerry |
| Hey, I can't help if I can't see. | Jerry | Rick |
| There is no helicopter and there is no Cervine Institute. | Beth | Jerry |
| I don’t know what to say. Summer is doing really well here. | Jerry | Beth |
| What?! Why would you -- Look, we're running late. We have to go. | Morty | Beth |
| What? N-No, I don't want to see your Pog collection. I don't renounce Rick, and I never have. I was just trying to protect my sister. I wanted you to have a normal life. That's something you can't have when Rick shows up. Everything real turns fake. Everything right is wrong. All you know is that you know nothing and he knows everything. And, well -- well, he's not a villain, Summer, but he shouldn't be your hero. He's more like a demon or a super fucked up god. | Rick | Morty |
| But I obviously sort of love you, don't I?  So stop asking and maybe I'll love you more.  Crap, They need me at the horse hospital. | Jerry | Beth |
| Oh, my God! He's trying to tell us something.  That is so awesome. | Morty | Summer |
| Yeah, and what's courageous about eating a hot dog? | Jerry | Morty |
| Now hold on a second, let’s be rational about this. | Rick | Beth |
