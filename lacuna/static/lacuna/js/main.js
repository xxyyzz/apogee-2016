// Array for game
var cur_pos = 0;
// var game_seq = ["dashboard","story01","story02","story03","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",]


var story_seq=[
		{
			name:"dashboard",
			type:"game_start",
			img:"",

		 },
		{	
			name:"story01",
			type:"story",
			img:'img/story/story01.png',
			text:'“Hello, Mr. Holmes,” said the bearded old man who had just entered The Stranger’s Room at The Diogenes.<br>The older and comparatively less famous Holmes brother looked up in surprise. He had never before been interrupted at this establishment. It had been a long time since someone took him by surprise. Sipping his Earl Grey as calmly as ever, Mycroft looked questioningly at the intruder. Seeking an answer to the obvious, and realizing that he would receive none till he asked, he said, “Hello. Who might you be?”',
			func: moveto_story,
		 },
		{	
			name:"story02",
			type:"story",
			img:'img/story/story02.jpg',
			text:'“Maupertuis,” he replied. Responding to Mycroft’s continued expression of confusion, Maupertuis went on in a voice which reeked of egomania, “Perhaps you know me better as ‘The Baron’.”',
			func: moveto_story, 
		 },
		{	
			name:"story03",
			type:"story",
			img:'img/story/story03.jpg',
			text:'The grimace on Mycroft’s face didn’t go unnoticed by the Baron, though he still felt disappointed at not having been recognized immediately. Surely the buffoons at MI6 were not, well, buffoons. Well, he had to make sure. Just in case. He couldn’t possibly have somebody this incompetent as his business partner. Definitely not after the fruitful partnership that was brought to an abrupt end due to the demise of his colleague. “Mr. Holmes. You’re one of the few people lucky enough to hear the words I am about to say. However, I do question your competence, considering you did not recognize me. But before we discuss business, you must first prove your mettle to me.”',
			func: moveto_story, 
		},
		{	
			name:"puzzle01",
			type:"puzzle",
			img:'img/story/story04.png',
			text:'Sherlock took another puff of his pipe as he stared out into the busy bustling marketplace of Baghdad. He was bored. Bored. How could I not be bored? My brother asks me to stay here pretending to be dead. Sherlock winced at the bitter irony. Of all the things he had in his previous life, the one thing he missed the most after he had to fake his death was John. His first friend. His only friend. And he had had to betray him. Sherlock had faked his death to protect John, but that didn’t lessen the pain of lying to him',
			func: moveto_story, 
		 },	
		{	
			name:"story04",
			type:"story",
			img:'img/story/story04.png',
			text:'Sherlock took another puff of his pipe as he stared out into the busy bustling marketplace of Baghdad. He was bored. Bored. How could I not be bored? My brother asks me to stay here pretending to be dead. Sherlock winced at the bitter irony. Of all the things he had in his previous life, the one thing he missed the most after he had to fake his death was John. His first friend. His only friend. And he had had to betray him. Sherlock had faked his death to protect John, but that didn’t lessen the pain of lying to him',
			func: moveto_story, 
		 },
		{	
			name:"story05",
			type:"story",
			img:'img/story/story05.jpg',
			text:'His reverie was interrupted by his phone beeping. He could feel adrenaline pumping through his veins as his hand crept forward to pick up the phone. Only Mycroft had the number to this phone. One message, an unknown number. Was this another message from the telecom service providers or was this Mycroft keeping his promise? Hopefully the latter. Hopefully this was a clue to one of Moriarty’s henchmen. Maybe, just maybe. One can only have so much fun in a mind palace, grinned Sherlock as he opened the message.',
			func: moveto_story, 
		 },
		{	
			name:"crypt01",
			type:"crypt",
			img:'img/story/story04.png',
			text:'Sherlock took another puff of his pipe as he stared out into the busy bustling marketplace of Baghdad. He was bored. Bored. How could I not be bored? My brother asks me to stay here pretending to be dead. Sherlock winced at the bitter irony. Of all the things he had in his previous life, the one thing he missed the most after he had to fake his death was John. His first friend. His only friend. And he had had to betray him. Sherlock had faked his death to protect John, but that didn’t lessen the pain of lying to him',
			func: moveto_story, 
		 },	
		{	
			name:"story06",
			type:"story",
			img:'img/story/story06.jpg',
			text:'Big brother really loves playing his games, smiled Sherlock as he celebrated another of his small victories. He had never settled in this shady hotel, always yearning to leave. Even if home was naught but a memory now. At least now he had something to keep his mind occupied. Something to keep his guilty conscience silent. None of that matters now. Moriarty’s web must be dismantled for Moriarty’s death to have any finality, any meaning. And Mycroft had just guided him towards the first thread in the web. The first one to be broken.',
			func: moveto_story, 
		 },
		{	
			name:"story07",
			type:"story",
			img:'img/story/story07.jpg',
			text:'A month had passed now, and Sherlock had been inducted into the ranks of the silent monks at the temple. Only this final test remained to prove that he had achieved inner peace and could be one of them. After this test was done, he could unveil Moriarty’s accomplice. Disguised as a monk, she smuggled drugs right under their very noses. Drugs that had once funded Moriarty’s plans. Not anymore though. Once Sherlock had cleared this test and earned the brotherhood of the monks, her game was up.',
			func: moveto_story, 
		 },
		{	
			name:"story08",
			type:"story",
			img:'img/story/story08.jpg',
			text:'Sherlock entered the test chamber to find all the monks seated on the stone floor in a circle. He sat gracefully in the centre at the place designated for him. A monk rose up silently and offered him a bowl with a sweet smelling fluid in it. Sherlock looked at his reflection in the clear green liquid, and drank it without a second thought.',
			func: moveto_story, 
		 },
		{	
			name:"puzzle02",
			type:"puzzle",
			img:'img/story/story04.png',
			text:'Sherlock took another puff of his pipe as he stared out into the busy bustling marketplace of Baghdad. He was bored. Bored. How could I not be bored? My brother asks me to stay here pretending to be dead. Sherlock winced at the bitter irony. Of all the things he had in his previous life, the one thing he missed the most after he had to fake his death was John. His first friend. His only friend. And he had had to betray him. Sherlock had faked his death to protect John, but that didn’t lessen the pain of lying to him',
			func: moveto_story, 
		 },	
		{	
			name:"story09",
			type:"story",
			img:'img/story/story09.jpg',
			text:'The monks would carry out their own brand of justice. The possibility of her escaping was nil. This route for drugs was now closed. However, this felt too simple. None of Moriarty’s panache was visible. Smuggling drugs and making money from it seemed too mundane for a man of Moriarty’s personality. Was there another game afoot? Sherlock hoped not. He would just have to look through her sleeping chambers and make sure to find anything that could lead him to anything else. Crush every plot and subplot Moriarty had laid out before killing himself that fateful day on the rooftop at Bart’s. He could almost see that sick man smile that sick smile of his before him, basking in his victories, bathing in the chaos that he had created.',
			func: moveto_story, 
		 },
		{	
			name:"story10",
			type:"story",
			img:'img/story/story10.jpg',
			text:'Sherlock had been in her chamber for a few minutes and was certain the only thing of interest or value in the room was the scroll he held in his hand. A scroll disguised to look old, but no technique this primitive could fool him. The scroll was new, and what it contained must be important.',
			func: moveto_story, 
		 },
		{	
			name:"crypt02",
			type:"crypt",
			img:'img/story/story04.png',
			text:'Sherlock took another puff of his pipe as he stared out into the busy bustling marketplace of Baghdad. He was bored. Bored. How could I not be bored? My brother asks me to stay here pretending to be dead. Sherlock winced at the bitter irony. Of all the things he had in his previous life, the one thing he missed the most after he had to fake his death was John. His first friend. His only friend. And he had had to betray him. Sherlock had faked his death to protect John, but that didn’t lessen the pain of lying to him',
			func: moveto_story, 
		 }, 
		{	
			name:"story11",
			type:"story",
			img:'img/story/story11.png',
			text:'An address in New Delhi? Things were getting interesting. Maybe a shipment was due here. Maybe a new deal to be struck? Maybe another one of Moriarty’s seemingly unrelated preposterous plots? The possibilities were endless, and Sherlock was determined to see this out to the very end.',
			func: moveto_story, 
		 },
		{	
			name:"story12",
			type:"story",
			img:'img/story/story12.jpg',
			text:'Sherlock was here. An old dilapidated and seemingly abandoned house awaited him. Looking around the neighbourhood to check for lookouts and praying to God that the door wasn’t booby trapped, he entered the place. He searched room after room, surprised that the house was empty, but even his trained eyes could not make out any stashes of drugs or weapons or technology that could possibly entertain Moriarty’s consciousness. Did they know he was coming? Surely, they must have guessed someone was on their trail once the woman in the monastery had been dealt with. Had they escaped? He knew it was too much to hope that they had abandoned their plans in fright of him. If only they realized how much of a threat I am.',
			func: moveto_story, 
		 },
		{	
			name:"story13",
			type:"story",
			img:'img/story/story13.jpg',
			text:'He came back to the living room. Nothing seemed out of place. Almost nothing. He walked up to the cold fireplace and bent down to inspect it and with a proud egotistic smirk, he removed the false wall behind the fireplace to reveal a door, enforced with steel, sleek and modern unlike the rest of the house. And guarding the door was the most ridiculous lock Sherlock had ever seen.',
			func: moveto_story, 
		 },
		{	
			name:"puzzle03",
			type:"puzzle",
			img:'img/story/story04.png',
			text:'Sherlock took another puff of his pipe as he stared out into the busy bustling marketplace of Baghdad. He was bored. Bored. How could I not be bored? My brother asks me to stay here pretending to be dead. Sherlock winced at the bitter irony. Of all the things he had in his previous life, the one thing he missed the most after he had to fake his death was John. His first friend. His only friend. And he had had to betray him. Sherlock had faked his death to protect John, but that didn’t lessen the pain of lying to him',
			func: moveto_story, 
		 },	 
		{	
			name:"story14",
			type:"story",
			img:'img/story/story14.jpg',
			text:'With the door now open, Sherlock crawled through to what resembled a dusty store room. Empty weapon crates. So Sherlock’s fears had not been ill founded. Drugs were not the only thing that were being smuggled. Moriarty had been planning on war in South Asia. And if weapons were being smuggled, it wasn’t too much to assume the same about explosives.',
			func: moveto_story, 
		 },
		{	
			name:"story15",
			type:"story",
			img:'img/story/story15.jpg',
			text:'What interested Sherlock more than the weapons, however, was a small map chucked hastily into the dustbin. He picked it up, mentally laughing at Moriarty’s men for leaving such an easy trail of breadcrumbs to follow. A small house in a locality for the wealthy had been marked in red. A posh residence, no doubt, but an explosion here would not lead to many casualties. Maybe this was an assassination. Maybe this wasn’t even a bombing. Too many possibilities. Not enough breadcrumbs.',
			func: moveto_story, 
		 },
		{	
			name:"story16",
			type:"story",
			img:'img/story/story16.png',
			text:'Sherlock disembarked from the cab, and looked around. Just another society where the rich fed off the poor and lived in style, with the poor serving them in the menial positions they were assigned. Nothing surprising here. However, the house Sherlock was interested in looked ominously quiet. Not even any security personnel. This house looked promising, but Sherlock needed to be careful here. Examining the open gate for any traps, he stepped inside. Picking the lock of the front door was easy, and Sherlock opened the door. The house was bare, and the only thing in it that wasn’t the floor or the walls was one of the biggest bombs Sherlock had ever seen. It was a miracle that Moriarty’s men had managed to assemble it in here without the authorities finding out.',
			func: moveto_story, 
		 },
		{	
			name:"crypt03",
			type:"crypt",
			img:'img/story/story04.png',
			text:'Sherlock took another puff of his pipe as he stared out into the busy bustling marketplace of Baghdad. He was bored. Bored. How could I not be bored? My brother asks me to stay here pretending to be dead. Sherlock winced at the bitter irony. Of all the things he had in his previous life, the one thing he missed the most after he had to fake his death was John. His first friend. His only friend. And he had had to betray him. Sherlock had faked his death to protect John, but that didn’t lessen the pain of lying to him',
			func: moveto_story, 
		 },  
		{	
			name:"story17",
			type:"story",
			img:'img/story/story17.jpg',
			text:'His job here seemed to be done. The bomb was defused. Sherlock looked around the house but could find nothing else of any interest whatsoever. He had a million burning questions in his mind but no answers whatsoever. The only fact about the situation clear to Sherlock was that someone wanted to start a war. War was profitable for people of Moriarty’s stature and acumen. But who planted this bomb? How did they manage to accomplish it without the authorities finding out? The frustration of not knowing was almost unbearable. Worse than that, he could almost see Moriarty haunting him, laughing at his inadequacy. So Sherlock did what he always did when he was frustrated, which was to actually do his job as a consultant detective in whatever part of the world he happened to be in. All he could do now was wait for big brother to send him a lead. And maybe help the Delhi police out with some of their cases.',
			func: moveto_story, 
		 },
		{	
			name:"story18",
			type:"story",
			img:'img/story/story18.jpg',
			text:'It had been just a week. But a week can be so long. Sherlock was already bored out of his wits. There were no interesting murders happening around town which could tax some of his mental facilities. Boring. He kept checking the dark corners of the Internet, waiting for a message from his brother. Waiting. He checked and rechecked for a message, and soon his patience was rewarded. He got a call from the UK Embassy saying they had a package waiting for him. Mycroft should have sent me what he wanted to send me electronically. Who uses the mail these days? A short visit and a flash of his fake passport later, he had the package in his hands. When he opened the parcel once he was back at the hotel, he found a box sealed with another of his brother’s mischievous puzzles. Oh, Mycroft, when will you ever grow up?',
			func: moveto_story, 
		 },
		{	
			name:"puzzle04",
			type:"puzzle",
			img:'img/story/story04.png',
			text:'Sherlock took another puff of his pipe as he stared out into the busy bustling marketplace of Baghdad. He was bored. Bored. How could I not be bored? My brother asks me to stay here pretending to be dead. Sherlock winced at the bitter irony. Of all the things he had in his previous life, the one thing he missed the most after he had to fake his death was John. His first friend. His only friend. And he had had to betray him. Sherlock had faked his death to protect John, but that didn’t lessen the pain of lying to him',
			func: moveto_story, 
		 },	 
		{	
			name:"story19",
			type:"story",
			img:'img/story/story19.jpg',
			text:'Dearest baby brother,<br>I hope my letter finds you in good health. Surely you must be enjoying your stay in India. Sadly for us, your visit must be cut short. We have urgent business to deal with. We have a chance to put down another of Moriarty’s lieutenants, Herr Trepoff. Luckily for us, he has just killed his lovely wife, may her soul rest in peace. Considering his influential position in Germany, the lads at MI6 are certain he will get away with it. However, I have called in several favours to get you into the jury that shall decide Trepoff’s fate. It is imperative that you convince the jury of Trepoff’s guilt. Pack your things and get to Hamburg immediately, little brother. May luck be with you, because God only knows how much you might need it.<br>Yours truly,<br>Mycroft<br><br>Sherlock was on the next flight to Hamburg. It was seldom that you got the opportunity to take down one of Moriarty’s men this easily. Never did they provide themselves on a silver platter. Prove Trepoff guilty and he would be done with. He would no longer be able to serve in the position that he was currently in. But that was obviously easier said than done, considering this was one of Moriarty’s elite. Sherlock knew that everything could go wrong in the blink of an eye. He had to proceed with caution.',
			func: moveto_story, 
		 },
		{	
			name:"story20",
			type:"story",
			img:'img/story/story20.jpg',
			text:'Sherlock looked around the room. He had broken into the offices of the law firm that was representing Trepoff, and was now in the room of the man that was representing him in court. Why can’t I remember his name? He reminds me of someone back home. But I’ll be damned if I can’t remember who that is either. Sherlock had long since figured out how Trepoff planned to evade justice. Rather than focusing on trying to hide the evidence, all he was doing was making sure the jury did not pass a guilty verdict.<br> Trepoff’s lawyer had started scaring the jury into submission and unless Sherlock was able to get some leverage on the lawyer, Trepoff would surely walk free. None of the members of the jury seemed to be of particularly strong will, and it was up to him to rid them of this danger lurking over their heads. Breaking into the lawyer’s office was easy, and so was breaking into his laptop. Logging into his email, Sherlock looked over the conversation history that the lawyer and his murderous client shared. Strange. Just one mail.',
			func: moveto_story, 
		 },
		{	
			name:"crypt04",
			type:"crypt",
			img:'img/story/story04.png',
			text:'Sherlock took another puff of his pipe as he stared out into the busy bustling marketplace of Baghdad. He was bored. Bored. How could I not be bored? My brother asks me to stay here pretending to be dead. Sherlock winced at the bitter irony. Of all the things he had in his previous life, the one thing he missed the most after he had to fake his death was John. His first friend. His only friend. And he had had to betray him. Sherlock had faked his death to protect John, but that didn’t lessen the pain of lying to him',
			func: moveto_story, 
		 },  
		{	
			name:"story21",
			type:"story",
			img:'img/story/story21.jpg',
			text:'This was all the leverage Sherlock needed. Trepoff’s lawyer would no longer pose a threat to the case. He had him now. If only I could remember his name too. Sherlock enjoyed a rare moment of satisfaction. He headed back to his hotel, and just a few days later, the judge declared Trepoff guilty.<br><br>Sherlock was satisfied with this victory but he thirsted for more. There had been no word from Mycroft, so Sherlock deduced that his elder brother had no leads either. He didn’t really want to go this way, but the desperation was getting to him. He would have to talk to Irene. He needed to go to Amsterdam.',
			func: moveto_story, 
		 },
		{	
			name:"story22",
			type:"story",
			img:'img/story/story22.png',
			text:'Irene was being her usual dominating self. She could dominate the entire human race if she just chose to do so. Up to her usual ploys, she had a big smile on her face, and her eyes sparkled with mischief. Showing him the love he yearned for but just not enough. Never enough. Sherlock knew that thing with her could never work. So he tried to focus on the business at hand and not her lovely, lovely lips. Irene. How do you do this? How do you make me so weak? Sherlock weakly cleared his throat and said, “Irene. I’m here because I need something.”<br><br>The spark in Irene’s eyes refused to go away. “Isn’t everyone?” she asked him in the sweetest voice Sherlock had ever heard. Why does every word you say sound sweeter than the last? Sherlock could no longer help it. He was trapped. <br><br>Irene could sense the helplessness Sherlock was experiencing, and she loved every minute of it. Putting the poor boy out of his misery, she handed him a phone and asked him to solve her problem. “Oh come on, Sherlock. Do something clever.”',
			func: moveto_story, 
		 },
		{	
			name:"puzzle05",
			type:"puzzle",
			img:'img/story/story04.png',
			text:'Sherlock took another puff of his pipe as he stared out into the busy bustling marketplace of Baghdad. He was bored. Bored. How could I not be bored? My brother asks me to stay here pretending to be dead. Sherlock winced at the bitter irony. Of all the things he had in his previous life, the one thing he missed the most after he had to fake his death was John. His first friend. His only friend. And he had had to betray him. Sherlock had faked his death to protect John, but that didn’t lessen the pain of lying to him',
			func: moveto_story, 
		 },	 
		{	
			name:"story23",
			type:"story",
			img:'img/story/story23.jpg',
			text:'Sherlock looked up from the puzzle she had given him, almost like a school child looking up for praise from his schoolmaster. Oh, the magic you hold over me. “Oh Sherlock, did you not want to talk business?” she laughed, relenting and letting her hold over Sherlock go, after which he seemed to come out of his trance, stammering out his request for information on any of Moriarty’s remaining men, and Irene obliged him. <br><br>If Sherlock acted quickly, he could bring an end to Moriarty’s entire empire with a single blow. Irene had information on Moriarty’s second in command, a man feared by the few who knew of his existence, a man referred to as the Baron. He was an old man named Maupertuis and having spent the last fifteen years masquerading as the respectable business head of the Netherland-Sumatra Company, he had made the mistake of keeping the company going after he went on the run. A new branch of the firm had suddenly opened in Romania, so it seemed likely that he was somewhere nearby. He wouldn’t be stupid enough to actually base himself near the offices but he must be somewhere in that part of Europe. Irene had an informant in Brussels who could give Sherlock Maupertuis’ location. <br><br>Sherlock left the next morning for Brussels. Irene had already arranged for her informant to drop off all relevant information, and just for the fun of it, she had asked him to put it in the form of a puzzle. As soon as Sherlock reached Brussels, he headed to the drop point, a park close to the railway station. He sat inconspicuously on the third bench from the right, the bench that they had decided on. Reaching under his seat, he extracted the envelope waiting for him. He smiled fondly as he opened it, excited about the future.',
			func: moveto_story, 
		 },
		{	
			name:"crypt05",
			type:"crypt",
			img:'img/story/story04.png',
			text:'Sherlock took another puff of his pipe as he stared out into the busy bustling marketplace of Baghdad. He was bored. Bored. How could I not be bored? My brother asks me to stay here pretending to be dead. Sherlock winced at the bitter irony. Of all the things he had in his previous life, the one thing he missed the most after he had to fake his death was John. His first friend. His only friend. And he had had to betray him. Sherlock had faked his death to protect John, but that didn’t lessen the pain of lying to him',
			func: moveto_story, 
		 }, 
		{	
			name:"story24",
			type:"story",
			img:'img/story/story24.jpg',
			text:'Sherlock had all that he needed. The Baron would soon come to justice. He was headed to Belgrade International Airport. However, at the airport, the customs officials had other plans. This was unacceptable. His passport had worked flawlessly this far. Mycroft had arranged for the passport himself and it had gotten him in and out of more countries than he cared to count. What could possibly have gone wrong tis time?<br><br>Sherlock’s thoughts were interrupted by a customs official, “Call for you, Mr. Bronson.” So there was no problem with his fake identity. Why then was he in a small cell at the airport? Sherlock picked up the phone and was lewdly surprised to find his brother on the other end. <br><br>“Mycroft, get me out of here this instant,”said Sherlock into the receiver.”<br><br>“I’m sorry, little brother. Of course you can leave. Just not to Serbia. You can’t have Maupertuis.”',
			func: moveto_story, 
		 },
		{	
			name:"story25",
			type:"story",
			img:'img/story/story01.png',
			text:'Sherlock was stunned. How was Mycroft possibly in cahoots with The Baron? This seemed to make no sense. Mycroft continued, “He helped us eliminate everyone else Moriarty trusted. We must let him be.” And just like that, the line was dead. Just like Sherlock’s faith in his brother.<br><br>Sherlock entered his small cell a different man from the one who had exit it. He sat there quietly as the official restrained him to his chair. He was in total despair. The official then, to Sherlock’s great surprise, brought in a package and placed it quietly within his handcuffed arms’ reach. The man then just as silently removed Sherlock’s restraints and left the room. Sherlock ripped open the package with trembling fingers, the fingers of a man who no longer has anything to lose.',
			func: moveto_story, 
		 },
		{	
			name:"puzzle06",
			type:"puzzle",
			img:'img/story/story04.png',
			text:'Sherlock took another puff of his pipe as he stared out into the busy bustling marketplace of Baghdad. He was bored. Bored. How could I not be bored? My brother asks me to stay here pretending to be dead. Sherlock winced at the bitter irony. Of all the things he had in his previous life, the one thing he missed the most after he had to fake his death was John. His first friend. His only friend. And he had had to betray him. Sherlock had faked his death to protect John, but that didn’t lessen the pain of lying to him',
			func: moveto_story, 
		 },
		{	
			name:"story26",
			type:"story",
			img:'img/story/story26.png',
			text:'Sherlock was stunned at the message he had just received. He rushed out of his cell out into a surprisingly empty corridor. Not a single guard or official was in sight. Retrieving his belongings from the empty guard’s desk, he started sprinting. He ran to hangar number 3, which was also very conveniently unguarded, and hid on board the aircraft. And waited. And waited. And fell asleep.<br><br>Sherlock woke up with a jerk. The aircraft was up in the sky, he was sure of it. Cursing himself inwardly, he tried to analyse the situation. Apparently Maupertuis had boarded the plane and they were flying to Siberia. This was the worst possible situation he could be in. Judging by how rich The Baron was, there must be attendants on board. Two attendants maybe. Not more. ',
			func: moveto_story, 
		 },
		{	
			name:"story27",
			type:"story",
			img:'img/story/story27.jpg',
			text:'He exited the luggage cabin with a fire in his eye. This was it. Moriarty’s last thread. Break this, and his whole web would be unravelled. He needed to take down everyone on board the aircraft, and even then, the craft would land in Siberia. There was no way to reach the pilot’s cabin from the passengers’ cabin in this model. The rich do believe in keeping their affairs private, Sherlock noted grimly. He was now in the attendants’ room, with both the attendants engrossed in conversation, probably cursing their rich employer from the tone of their voices. Taking them down was easy; none of them was trained in combat. The odds were slightly better now.',
			func: moveto_story, 
		 },
		{	
			name:"story28",
			type:"story",
			img:'img/story/story28.jpg',
			text:'Sherlock walked into the cabin like he owned the place, making The Baron almost spill his drink in surprise. The Baron reached for the drawer in the table next to him, but Sherlock was quicker. Grabbing a hold of The Baron’s wrist, Sherlock broke it with a twist of his arm. Looking into the drawer, Sherlock found a Magnum .52. Sherlock looked in horror at the weapon in his hand.',
			func: moveto_story, 
		 },
		{	
			name:"story29",
			type:"story",
			img:'img/story/story29.jpg',
			text:'This was Moriarty’s last agent. Surely he deserved this. Surely. The last thread in the intricate web that Moriarty had spun. This man needed to die for the good of the rest of the world. But Sherlock just couldn’t bring himself to do it. He couldn’t pull the trigger. Maupertuis saw Sherlock hesitating, and tried to capitalize on the situation. The duo struggled for supremacy, and this struggle ended only once Sherlock pulled the trigger.<br><br>This was no time to panic. The plane was going to land in Serbia. He would surely be caught and tortured. He could not escape once he landed. All he could do now was send a message for help to his brother from Maupertuis’ computer. And wait. He was surprised by his brother’s quick reply.',
			func: moveto_story, 
		 },
		{	
			name:"crypt06",
			type:"crypt",
			img:'img/story/story04.png',
			text:'Sherlock took another puff of his pipe as he stared out into the busy bustling marketplace of Baghdad. He was bored. Bored. How could I not be bored? My brother asks me to stay here pretending to be dead. Sherlock winced at the bitter irony. Of all the things he had in his previous life, the one thing he missed the most after he had to fake his death was John. His first friend. His only friend. And he had had to betray him. Sherlock had faked his death to protect John, but that didn’t lessen the pain of lying to him',
			func: moveto_story, 
		 },  
		{	
			name:"story30",
			type:"story",
			img:'img/story/story01.jpg',
			text:'Sherlock couldn’t help but laugh. His brother was sending him puzzles even at a time like this. He would find his brother in Serbia now, all he needed to do was get captured. It was all going to be okay.<br><br>John sighed with relief as his fingers typed out the last few words of his latest blog. After months of heckling, Sherlock had finally told him about how he had dismantled Moriarty’s network. But he knew that Sherlock wasn’t sharing his whole story. There were a few loopholes and inconsistencies. Though John respected Sherlock too much to question his story, he couldn’t possibly write a lie in his memoirs of Sherlock’s life. He inhaled deeply. This is the only possible way, he thought as he selected',
			func: moveto_story, 
		 },
		{	
			name:"story31",
			type:"story",
			img:'img/story/story30.jpg',
			text:null,
			func: moveto_story, 
		 },
		{	
			name:"story32",
			type:"story",
			img:'img/story/story01.png',
			text:null,
			func: moveto_story, 
		 },
		{	
			name:"story33",
			type:"story",
			img:'img/story/story01.png',
			text:null,
			func: moveto_story, 
		 },
		{	
			name:"story34",
			type:"story",
			img:'img/story/story01.png',
			text:null,
			func: moveto_story, 
		 },
];

function go_to_pos(ch){
	cur_pos = cur_pos + ch;
	if(story_seq[cur_pos]['type']=='story')
	{
		console.log('yo');
		$('#game_loader').fadeIn(200);
		var $downloadingImage = $("<img>");
		$downloadingImage.load(function(){	
		    story_seq[cur_pos]['func'](story_seq[cur_pos]['img'],story_seq[cur_pos]['text']);
			$('#game_loader').fadeOut(200);
		});
		$downloadingImage.attr("src", story_seq[cur_pos]['img']);
	}
}

function moveto_story(img,text){
	console.log('in');
	$('.story_container').css({'background-image':'url('+img+')'});
	$('.text_container').html(text);
}

$('.story_but').click(function(){
	if($(this).hasClass('story_prev'))
	{
		go_to_pos(-1);
	}
	else if($(this).hasClass('story_next'))
	{
		go_to_pos(1);
	}

});

// PUZZLE 5
function puzzle5init()
{	var grid= [
		[3,2,1,3,2,1,3,1,3],
		[1,2,3,3,1,2,2,2,2],
		[3,2,1,2,1,3,1,3,1],
		[3,1,2,2,3,1,1,2,3],
		[2,1,3,1,1,2,3,2,1],
		[2,3,1,3,2,3,1,2,3],
		[1,3,2,2,3,1,2,3,1],
		[1,2,3,1,1,3,3,2,2],
		[3,2,1,3,2,2,1,1,3],
	];
	var row=grid.length,col=grid[0].length;
	var count=0;


	function GenerateGrid()
	{
		var html = '<div class="puzzle5grid">';
		for(i=0;i<grid.length;++i)
		{
			for(j=0;j<grid[i].length;++j)
			{
				
				html+='<div class="puzzle5box" data-x="'+i+'" data-y="'+j+'">'+grid[i][j]+'</div>';
			}
		}
		html+='</div>';
		$('#puzzle5 .puzzle_deti').html(html);
		var initbox = ((row - 1) * col) + 1;
		// $('.puzzle5box:nth-child('+initbox+')').trigger("click");
		// setTimeout(function(){
		// 	$('.puzzle5grid').css({height:row*70,width:col*70});
		// },200);
		
	}		
	GenerateGrid();
	function CheckSurrounding()
	{
		var box=$('.puzzle5box.sel');
		var x=box.data('x'),y=box.data('y');
		var arr = [
					$('.puzzle5box[data-x="'+x+'"][data-y="'+(y-1)+'"]')[0],
					$('.puzzle5box[data-x="'+(x+1)+'"][data-y="'+y+'"]')[0],
					$('.puzzle5box[data-x="'+x+'"][data-y="'+(y+1)+'"]')[0],
					$('.puzzle5box[data-x="'+(x-1)+'"][data-y="'+y+'"]')[0],
				];
		// console.log(pos,arr);
		for(i=0;i<arr.length;++i)
		{
			if( !($(arr[i]).hasClass('visited')) && (((count+1)%3)==(parseInt($(arr[i]).html()))%3))
			{
				return true;
			}
		}
		return false;
	}
	function CheckMovePossible()
	{
		if(!CheckSurrounding())
		{
			if($('.puzzle5box:not(.visited)')[0]==undefined)
				win();
			else
				lost();
		}
	}

	function CheckIsNeighbor(prev,cur)
	{
		var dx=Math.abs($(prev).data('x') - $(cur).data('x')),  dy=Math.abs($(prev).data('y') - $(cur).data('y'));
		if((dx==1 && dy==0) || (dx==0 && dy==1))
		{
			$(prev).removeClass('sel');
			$(cur).addClass('visited sel');
			CheckMovePossible();
		}
		else
		{
			--count;
			alert('not neightbor');
		}	
	}

	$('.puzzle5box').click(function(){
		++count;
		// console.log(count);
		if((count%3) == (parseInt($(this).html())%3) &&  !($(this).hasClass('visited'))  )
		{
			if(count>1)
				CheckIsNeighbor($('.puzzle5box.sel')[0],this);
			else
			{
				$('.puzzle5box.sel').removeClass('sel');
				$(this).addClass('visited sel');
			}
		}
		else
		{
			alert('can only click in order 1..2...3 or it is already selected');
			--count;
		}	
	});

	function  lost()
	{
		alert('lost');
	}
	function win()
	{
		if(count==row*col)
			alert('win');
	}

}
puzzle5init();
