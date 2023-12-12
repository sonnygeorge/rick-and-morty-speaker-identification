### 🚀 **GrdntBstngClssfr_10fs_5**

- 🤖 **Model Type**:
	<class 'sklearn.ensemble._gb.GradientBoostingClassifier'>
- 📊 **Dataset Used**:
	_Random_
- 🧠 **Number of Features**:
	1369
- 🚫 **Unused Features**:
	78/1369
- ⌛ **Model Train Time**:
	176.618
- 💬 **SpaCy Preprocessing Model**:
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `n_estimators`: 180
	- `learning_rate`: 0.24
	- `max_depth`: 4
	- `random_state`: 38

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 1.0 | 0.535 | 0.485 |
| Macro F1 | 1.0 | 0.373 | 0.356 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.40 | 0.20 | 0.27 |
| Jerry | 0.17 | 0.11 | 0.13 |
| Morty | 0.47 | 0.62 | 0.53 |
| Rick | 0.65 | 0.74 | 0.70 |
| Summer | 0.33 | 0.18 | 0.24 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.36 | 0.29 | 0.32 |
| Jerry | 0.12 | 0.10 | 0.11 |
| Morty | 0.56 | 0.50 | 0.53 |
| Rick | 0.53 | 0.69 | 0.60 |
| Summer | 0.50 | 0.14 | 0.22 |

### 🧠 Feature Extraction Methods

| Method | Importance |
| ------ | ---------- |
| Nghbhood Degrees - Lemmas (.5decay,1topn,5nghbrs)(fasttext-wiki-news-subwords-300)(Rndm) | 0.9180 |
| Familial Words & Common Names 1-Gram One Hots | 0.0386 |
| Average Word Length | 0.0169 |
| Exclamation Marks Per Sentence | 0.0094 |
| Topical Proximity - Food (fasttext-wiki-news-subwords-300) | 0.0083 |
| Proportion Of Tokens That Are Stop Words | 0.0043 |
| Proportion Of Chars That Are Capitalized | 0.0017 |
| Question Marks Per Sentence | 0.0013 |
| Dashes Per Sentence | 0.0008 |
| Average Tokens Per Sentence | 0.0007 |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Uh, yeah, just a few more design notes.  Um, this guy. The, uh... The, uh... | Morty | Rick |
| Uh, what? It was your job, Morty. | Rick | Summer |
| Oh, God, what’s going on now? | Jerry | Beth |
| He bails on everybody! He bailed on Mom when she was a kid! He -- He bailed on tiny planet! And in case I never made this clear to you, Summer, he bailed on you. He left you to rot in a world that he ruined because he doesn't care! Because nobody's special to him, Summer, not even himself. So, if you really want your grandpa back, grab a shovel. The one that won't let you down is buried in your backyard! | Beth | Morty |
| Don't worry about Jerry. He's gonna be fine.You hear me Jerry? You're gonna be fine! | Beth | Rick |
| Boy, you really got me up against a wall this time, Jerry. | Jerry | Rick |
| Because you suck! You've been keeping your lip zipped about it since Grandpa got arrested, but the fact is, you're freaking stoked to bail on him. | Rick | Summer |
| Hey! I said nobody move, buddy! | Jerry | Rick |
| But can you help me get to my family? You know, at my house? | Jerry | Morty |
| Alright! That's enough. You're talking about my species! We understand genocide, we do it sometimes! | Rick | Jerry |
| I am not putting my father in a home! He just came back into my life, and you want to grab him and stuff him under a mattress like last month's Victoria's Secret? | Rick | Beth |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Morty | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Morty | Jerry |
| You don’t have to be a dick. | Morty | Rick |
| Man that guy is the Red Grin Grumble to pretending he knows what's going on.  Oh you agree, huh?  You like that Red Grin Grumble reference?  Well guess what? I made him up. You really are your father's children. Think for yourselves, don't be sheep. | Jerry | Rick |
| Good job, Morty. Let's go, kids. | Morty | Rick |
| I am sad that I peed. I'm sad that I peed in class instead of a toilet. | Rick | Morty |
| They're just robots, Morty! It's okay to shoot them! They're robots! | Morty | Rick |
| I'm sorry. It's just like the end of "Old Yeller. | Morty | Jerry |
| Is there coffee? Hey, Morty, can you be a pal? Grandpa left his coffee maker on the ship. Y-You know, the French press thing? | Summer | Rick |
| How is praying going to help? | Jerry | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| Aw! Oh, my God! He recognizes the other dogs on TV. | Morty | Summer |
| - Because that's -- that's what this is all about, Morty. | Morty | Rick |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Morty | Summer |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Morty | Jerry |
| Hey, what's wrong Morty? Oh, you're worried about your dad, huh? | Summer | Rick |
| Morty, stay out of this. You are obviously not capable of judging these situations on your own. | Rick | Jerry |
| Out of the frying pan dot, dot, dot, huh, Morty? | Morty | Rick |
| I mean it's been shot. With a gun. | Morty | Beth |
| Sure thing! And I was kinda hoping that I could get a selfie with you? | Jerry | Morty |
| Boom! Told you! In your face! He is ruining our child! Wait, what am I celebrating? | Morty | Jerry |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Rick | Jerry |
| Grandpa Rick wouldn't put up with this! | Morty | Summer |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| I don't know. I think like one sixty-fourth of my collars didn't work. It's hard to keep straight now that I have sixty-three other memories of everything. | Rick | Morty |
| - or sister I said any of this, I'll deny it - | Morty | Rick |
| Uh, w-why don't you get it Jerry? you're the man of the house and you don't have a job. | Morty | Rick |
| Well, I'm not calling him that. That's ridiculous. | Beth | Jerry |
| I didn't say my father is perfect, I said his work is important. | Jerry | Beth |
| Sure. Why not? I don’t, I don't know. Y-you know what, Mo— | Jerry | Rick |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Rick | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Rick | Summer |
| Just focus on the mission, all right? | Rick | Morty |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Rick | Jerry |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Morty | Beth |
| Then what good was the "yes"? | Rick | Beth |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Rick | Beth |
| What? What kind of monster are you? | Rick | Morty |
| I'm looking at her. Thanks for F.D.'ing me up like that. | Beth | Jerry |
| I never said I was angry at you. | Jerry | Summer |
| What? Why didn't you notify us? | Morty | Beth |
| This better not be a bribe. If I find a single thing out of place in this house, my love of ice cream won't save you. I'll get my jacket. | Beth | Jerry |
| What? Why are you looking at me? You want to go outside? Outside? | Rick | Jerry |
| This article says the reason we weren't involved was... "personality conflicts". | Rick | Morty |
| Actually, sorry Summer, I gotta back the M bomb on this one. I remember the conversation. We told Morty to replace all the bank's money with cookies, your job was to put the mattress under Mr. Benson. | Morty | Rick |
| And they'll fall right out of mine. I've done this too many times, Morty. I mean, you're young. Y-y-you've got your whole life ahead of you, and your anal cavity is still taut, yet malleable. You got to do it for grandpa, Morty. Y-  you've got to put these seeds inside your butt. | Summer | Rick |
| Doesn't feel so good, does it? | Rick | Morty |
| Who cares about the  thing you guys are talking about? The whole point of freezing time is to stop giving a fuck. Put a shirt on your dumb dad and let's get this dumb universe rolling. Let's do this thing. | Beth | Rick |
| I AM a baby! I’m a baby NOW! | Morty | Jerry |
| Oldest Rick trick in the book. | Morty | Rick |
| Listen, Rick, if you're gonna stay here rent-free and use my son for your stupid science, the least you could do is put a little bit of it to use for the family. You make that dog smart or Morty's grounded! | Rick | Jerry |
| Oh, for crying out—he's got some kind of disability or something. Is that what you want us to say? | Rick | Jerry |
| There is no helicopter and there is no Cervine Institute. | Morty | Jerry |
| I don’t know what to say. Summer is doing really well here. | Rick | Beth |
| What?! Why would you -- Look, we're running late. We have to go. | Rick | Beth |
| What? N-No, I don't want to see your Pog collection. I don't renounce Rick, and I never have. I was just trying to protect my sister. I wanted you to have a normal life. That's something you can't have when Rick shows up. Everything real turns fake. Everything right is wrong. All you know is that you know nothing and he knows everything. And, well -- well, he's not a villain, Summer, but he shouldn't be your hero. He's more like a demon or a super fucked up god. | Summer | Morty |
| But I obviously sort of love you, don't I?  So stop asking and maybe I'll love you more.  Crap, They need me at the horse hospital. | Rick | Beth |
| Oh, my God! He's trying to tell us something.  That is so awesome. | Rick | Summer |
| Yeah, and what's courageous about eating a hot dog? | Rick | Morty |
| Now hold on a second, let’s be rational about this. | Rick | Beth |
### 📉 Individual Feature Importances

| Feature | Importance |
| ------- | ---------- |
| deg_of_presence(straw)_norm | 0.05118880949725938 |
| deg_of_presence(timeline)_norm | 0.026309023895128122 |
| has(morty) | 0.022711862402168576 |
| deg_of_presence(dis)_norm | 0.0192285074139077 |
| deg_of_presence(grandpa)_norm | 0.018266185007176458 |
| avg_token_length | 0.016932978225399433 |
| deg_of_presence(vet)_norm | 0.014902709557358229 |
| deg_of_presence(tron)_norm | 0.014458019017124773 |
| deg_of_presence(vincent)_norm | 0.014116811244876602 |
| deg_of_presence(w)_norm | 0.014044909228414348 |
| deg_of_presence(mannequin)_norm | 0.013966101603393202 |
| deg_of_presence(wong)_norm | 0.013030193067126963 |
| deg_of_presence(friend)_norm | 0.011634691148330432 |
| deg_of_presence(girl)_norm | 0.010680681522172115 |
| deg_of_presence(head)_norm | 0.010556414886203657 |
| deg_of_presence(vat)_norm | 0.009591619236337025 |
| exclamation_marks_per_sentence | 0.009432632546177454 |
| deg_of_presence(beth)_norm | 0.009350344060873856 |
| ... | ... |
| deg_of_presence(reasoning)_norm | 0.0 |
| deg_of_presence(scary)_norm | 0.0 |
| deg_of_presence(arm)_norm | 0.0 |
| deg_of_presence(happen)_norm | 0.0 |
| deg_of_presence(satisfying)_norm | 0.0 |
| deg_of_presence(hassle)_norm | 0.0 |
| deg_of_presence(class)_norm | 0.0 |
| deg_of_presence(build)_norm | 0.0 |
| deg_of_presence(perfectly)_norm | 0.0 |
| deg_of_presence(goner)_norm | 0.0 |
| deg_of_presence(nurse)_norm | 0.0 |
| deg_of_presence(get)_norm | 0.0 |
| deg_of_presence(gentleman)_norm | 0.0 |
| deg_of_presence(imagine)_norm | 0.0 |
| deg_of_presence(miracle)_norm | 0.0 |
| deg_of_presence(idea)_norm | 0.0 |
| deg_of_presence(trip)_norm | 0.0 |
| deg_of_presence(student)_norm | 0.0 |
| deg_of_presence(normal)_norm | 0.0 |
| deg_of_presence(uhh)_norm | 0.0 |
| deg_of_presence(grandson)_norm | 0.0 |
| deg_of_presence(creator)_norm | 0.0 |
| deg_of_presence(create)_norm | 0.0 |
| deg_of_presence(weird)_norm | 0.0 |
| deg_of_presence(crawl)_norm | 0.0 |
| deg_of_presence(horror)_norm | 0.0 |
| deg_of_presence(cranial)_norm | 0.0 |
| deg_of_presence(pack)_norm | 0.0 |
| deg_of_presence(pair)_norm | 0.0 |
| deg_of_presence(comfort)_norm | 0.0 |
