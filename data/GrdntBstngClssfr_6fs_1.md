### 🚀 **GrdntBstngClssfr_6fs_1**

- 🤖 **Model Type**: 
	<class 'sklearn.ensemble._gb.GradientBoostingClassifier'>
- 📊 **Dataset Used**: 
	_Random_
- 🧠 **Number of Features**: 
	32
- 🚫 **Unused Features**: 
	0/32
- ⌛ **Model Train Time**: 
	5.316
- 💬 **SpaCy Preprocessing Model**: 
	`en_core_web_sm`

- 🧬 **Model Hyperparameters**:

	- `n_estimators`: 140
	- `learning_rate`: 0.5
	- `max_depth`: 5
	- `random_state`: 42

### 📊 Scores

| Metric | Train | Dev | Test |
| ------ | ----- | --- | ---- |
| Accuracy | 1.0 | 0.406 | 0.337 |
| Macro F1 | 1.0 | 0.215 | 0.216 |

#### Classification Report (Dev Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.12 | 0.05 | 0.07 |
| Jerry | 0.17 | 0.06 | 0.08 |
| Morty | 0.29 | 0.38 | 0.33 |
| Rick | 0.53 | 0.66 | 0.59 |
| Summer | 0.00 | 0.00 | 0.00 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Beth | 0.18 | 0.14 | 0.16 |
| Jerry | 0.11 | 0.10 | 0.11 |
| Morty | 0.33 | 0.32 | 0.33 |
| Rick | 0.46 | 0.52 | 0.49 |
| Summer | 0.00 | 0.00 | 0.00 |

### 🧠 Feature Extraction Methods

| Method | Importance |
| ------ | ---------- |
| Average Root Verb Embedding (glove-twitter-25) | 0.6467 |
| Average Word Length | 0.1597 |
| Average Tokens Per Sentence | 0.0794 |
| Question Marks Per Sentence | 0.0494 |
| Exclamation Marks Per Sentence | 0.0367 |
| Total Sentence Count | 0.0280 |

### 🚫 Incorrect Predictions

| Utterance | Predicted Speaker | Actual Speaker |
| --------- | ----------------- | -------------- |
| Uh, yeah, just a few more design notes.  Um, this guy. The, uh... The, uh... | Morty | Rick |
| Uh, what? It was your job, Morty. | Morty | Summer |
| Oh, God, what’s going on now? | Rick | Beth |
| He bails on everybody! He bailed on Mom when she was a kid! He -- He bailed on tiny planet! And in case I never made this clear to you, Summer, he bailed on you. He left you to rot in a world that he ruined because he doesn't care! Because nobody's special to him, Summer, not even himself. So, if you really want your grandpa back, grab a shovel. The one that won't let you down is buried in your backyard! | Summer | Morty |
| Wow! A whole world populated by intelligent dogs. I wonder what it'll be like, Rick. | Rick | Morty |
| I'll cover that bet. I get it. | Rick | Morty |
| Whoa! Look! It's that lady with all that shit on her face like Worf from Star Trek! That was getting coffee! How did she get there! | Rick | Morty |
| That's right, Morty. This is gonna be a lot like that, except, you know, it's gonna may--be make sense. | Morty | Rick |
| Aw, geez. Okay. I guess I can skip history. What about Frank? I mean, shouldn't you unfreeze him? | Rick | Morty |
| Because you suck! You've been keeping your lip zipped about it since Grandpa got arrested, but the fact is, you're freaking stoked to bail on him. | Rick | Summer |
| Full disclosure, Morty it's not. Temporary superintelligence is just a side effect of the mega seeds dissolving in your rectal cavity. | Beth | Rick |
| Hey! I said nobody move, buddy! | Morty | Rick |
| Me. I used to wear blue pants. | Morty | Rick |
| But can you help me get to my family? You know, at my house? | Rick | Morty |
| Alright! That's enough. You're talking about my species! We understand genocide, we do it sometimes! | Rick | Jerry |
| I am not putting my father in a home! He just came back into my life, and you want to grab him and stuff him under a mattress like last month's Victoria's Secret? | Rick | Beth |
| Morty, Mom's talking. I'm sorry, I suppose that's a good segue into our little discipline cases here. | Rick | Beth |
| Yeah, we missed you so much. Too much to hug you though. | Rick | Summer |
| Yes I will! That's right, assholes, take my penis, TAKE IT ALL! And tell Shrimply Pimples that when the galaxy came calling Jerry Smith from Earth didn't flinch! | Rick | Jerry |
| You don’t have to be a dick. | Jerry | Rick |
| I don't know, Rick. I can't leave school again. | Rick | Morty |
| Good job, Morty. Let's go, kids. | Morty | Rick |
| Hello? Is anybody here?  Mr. President! | Rick | Morty |
| I'm sorry. It's just like the end of "Old Yeller. | Summer | Jerry |
| It's the Citadel of Ricks. All the different Ricks from all the different realities got together to hide here from the government. | Rick | Morty |
| How is praying going to help? | Morty | Beth |
| You don't need to say anything. We got you, dawg. | Rick | Morty |
| Aw! Oh, my God! He recognizes the other dogs on TV. | Morty | Summer |
| It's Dimension 35-C, and it's got the perfect climate conditions for a special type of tree, Morty, called a Mega Tree, and there's fruit in those trees, and there's seeds in those fruits. I'm talking about Mega Seeds. They're they're incredibly powerful, and I need them to help me with my research, Morty. | Morty | Rick |
| I don't know yet. I'll make it up as I go. That's what Grandpa Rick does. That's what heroes do. | Rick | Summer |
| Okay, with all due respect, Rick— what am I talking about? What respect is due? How is my son supposed to pass his classes if you keep dragging him off for high-concept Sci-Fi rigamarole? | Morty | Jerry |
| Hey, what's wrong Morty? Oh, you're worried about your dad, huh? | Beth | Rick |
| Out of the frying pan dot, dot, dot, huh, Morty? | Morty | Rick |
| If it takes nine seasons, I want my McNugget dipping sauce, Szechuan sauce, Morty. | Beth | Rick |
| I mean it's been shot. With a gun. | Morty | Beth |
| Boom! Told you! In your face! He is ruining our child! Wait, what am I celebrating? | Morty | Jerry |
| Jerry, this was the most romantic weekend I've ever had. | Rick | Beth |
| Summer, listen carefully. I stole a paper clip and I have it in my cheek but I don’t know what to do with it and it hurts. | Rick | Jerry |
| Grandpa Rick wouldn't put up with this! | Rick | Summer |
| That’s planning for failure, Morty. Even dumber than regular planning.  Balls. | Beth | Rick |
| Oh, man, Rick. What is this place? | Rick | Morty |
| He got wrapped up in an experiment. He's a scientist. Like, legit, like on an inter-galactic, sci-fi level. His work is very -- | Rick | Beth |
| I don't know. I think like one sixty-fourth of my collars didn't work. It's hard to keep straight now that I have sixty-three other memories of everything. | Rick | Morty |
| Yeah, Rick... I-it's great. Is this the surprise? | Rick | Morty |
| - or sister I said any of this, I'll deny it - | Summer | Rick |
| Well, I'm not calling him that. That's ridiculous. | Morty | Jerry |
| I didn't say my father is perfect, I said his work is important. | Morty | Beth |
| Sure. Why not? I don’t, I don't know. Y-you know what, Mo— | Morty | Rick |
| Nobody needs anything! Okay, it's fine. I mean, you should just stay here and figure out how to stop being a pickle, okay? | Rick | Beth |
| We're miserable, Morty! There's a mandatory curfew, their weird calendar made me 47, and they weaponized the Eiffel Tower! | Beth | Summer |
| I don't care about Jessica! Y-Yyyyyyyyyyou— | Rick | Morty |
| When we get to customs, I'm gonna need you to take these seeds into the bathroom, and I'm gonna need you to put them way up inside your butthole, Morty. | Jerry | Rick |
| Don't praise him now, Morty! He just peed on the carpet! Bad dog! Bad! | Morty | Jerry |
| And then Ethan played guitar and we learned the Seven Contemplations of the Head by singing them. It was really fun. Praise be the head! | Rick | Summer |
| And I‘m lucky to have you and I never tell you that! You know, we will come out of this stronger as a family! | Rick | Beth |
| Did he say he never forgets a kid? | Morty | Rick |
| Then what good was the "yes"? | Summer | Beth |
| So what are you thinking, like, Smokey's Tavern? Maybe Shoney's? | Morty | Beth |
| Whatever. How petty would I have to be to care less about an animal's life than my own ego? | Rick | Beth |
| Okay, I only ask, Jerry, because, as you know, my job involves performing heart surgery. | Rick | Beth |
| What? What kind of monster are you? | Beth | Morty |
| We’ll take our chances raising her without fancy new jobs outside of a potato-based religion.  And you know what? I’m sick of pretending that we’re together because of the kids in the first place! I married you because you’re the love of my life! | Rick | Jerry |
| I'm looking at her. Thanks for F.D.'ing me up like that. | Morty | Jerry |
| Got some of that mermaid puss! | Summer | Rick |
| I never said I was angry at you. | Morty | Summer |
| This better not be a bribe. If I find a single thing out of place in this house, my love of ice cream won't save you. I'll get my jacket. | Rick | Jerry |
| Yikes. Yeah, things did feel less diverse in there. | Morty | Rick |
| What? Why are you looking at me? You want to go outside? Outside? | Rick | Jerry |
| Ow! Ow! You're tugging me too hard! | Summer | Morty |
| I don't either. I-I'm just saying, if anything, the drunk version of me is probably so supportive of Israel, he wants what's best for it and... | Summer | Rick |
| Man, Grandpa Rick must have gotten shitfaced. | Rick | Summer |
| Rick? Are you far away, or are you inside something? | Jerry | Morty |
| Sir, I need to get to the stage and help Rick get schwifty! | Rick | Morty |
| Uh, I kind of am. I saved the goddamn universe. | Morty | Rick |
| Time to go another dream deep, Morty! | Morty | Rick |
| You have to turn them on, Morty! The shoes have to be turned on! | Jerry | Rick |
| Go in the waiting room, Dad. | Morty | Beth |
| I AM a baby! I’m a baby NOW! | Morty | Jerry |
| Oldest Rick trick in the book. | Morty | Rick |
| Listen, Rick, if you're gonna stay here rent-free and use my son for your stupid science, the least you could do is put a little bit of it to use for the family. You make that dog smart or Morty's grounded! | Rick | Jerry |
| Oh, for crying out—he's got some kind of disability or something. Is that what you want us to say? | Rick | Jerry |
| Alright. I'll-I'll land. I'll land. I'll land. I'll land the thing. I’ll land the thing. Big tough guy all of a sudden. | Beth | Rick |
| Because Ricks hate themselves the most. And our Rick is the most himself. | Summer | Morty |
| Are you guys Power Rangers? But only on one small part of your necks? Hey, do those things need batteries? Were they included? Clean up in the fruit isle! Not in a homophobic way though, they're just fruity necklaces is all I was saying. | Rick | Jerry |
| Hey, I can't help if I can't see. | Morty | Rick |
| There is no helicopter and there is no Cervine Institute. | Rick | Jerry |
| I don’t know what to say. Summer is doing really well here. | Rick | Beth |
| What?! Why would you -- Look, we're running late. We have to go. | Morty | Beth |
| What? N-No, I don't want to see your Pog collection. I don't renounce Rick, and I never have. I was just trying to protect my sister. I wanted you to have a normal life. That's something you can't have when Rick shows up. Everything real turns fake. Everything right is wrong. All you know is that you know nothing and he knows everything. And, well -- well, he's not a villain, Summer, but he shouldn't be your hero. He's more like a demon or a super fucked up god. | Rick | Morty |
| But I obviously sort of love you, don't I?  So stop asking and maybe I'll love you more.  Crap, They need me at the horse hospital. | Rick | Beth |
| Oh, my God! He's trying to tell us something.  That is so awesome. | Rick | Summer |
| Now hold on a second, let’s be rational about this. | Jerry | Beth |
### 📉 Individual Feature Importances

| Feature | Importance |
| ------- | ---------- |
| avg_token_length | 0.15974617793366014 |
| avg_tokens_per_sentence | 0.07944845973488518 |
| question_marks_per_sentence | 0.04942798498763458 |
| avg_root_verb_embedding_24 | 0.04627408133285222 |
| avg_root_verb_embedding_0 | 0.03814385468907989 |
| avg_root_verb_embedding_20 | 0.03678253907803817 |
| exclamation_marks_per_sentence | 0.036705082840091295 |
| avg_root_verb_embedding_5 | 0.03395179914789656 |
| avg_root_verb_embedding_1 | 0.03134521016230084 |
| avg_root_verb_embedding_11 | 0.029365369093014952 |
| total_sentence_count | 0.027953417832388153 |
| avg_root_verb_embedding_4 | 0.027687155612294477 |
| avg_root_verb_embedding_17 | 0.027113790239559517 |
| avg_root_verb_embedding_6 | 0.026806358268586773 |
| avg_root_verb_embedding_12 | 0.026802463974357246 |
| avg_root_verb_embedding_21 | 0.025400452111404678 |
| avg_root_verb_embedding_2 | 0.02482865829010627 |
| avg_root_verb_embedding_23 | 0.024138269103195456 |
| avg_root_verb_embedding_14 | 0.023567990463750594 |
| avg_root_verb_embedding_7 | 0.022502187484519605 |
| avg_root_verb_embedding_9 | 0.021493856269225602 |
| avg_root_verb_embedding_18 | 0.021490935932508382 |
| avg_root_verb_embedding_22 | 0.020769930203232586 |
| avg_root_verb_embedding_10 | 0.020610901647758605 |
| avg_root_verb_embedding_3 | 0.019670646675026913 |
| avg_root_verb_embedding_16 | 0.01904849908339039 |
| avg_root_verb_embedding_15 | 0.016172701626528715 |
| avg_root_verb_embedding_8 | 0.015094898462463152 |
| avg_root_verb_embedding_19 | 0.015025788964397773 |
| n_root_verbs | 0.014256027407968169 |
| avg_root_verb_embedding_13 | 0.01351195534990428 |
| n_root_verbs_embedded | 0.004862555997978829 |
