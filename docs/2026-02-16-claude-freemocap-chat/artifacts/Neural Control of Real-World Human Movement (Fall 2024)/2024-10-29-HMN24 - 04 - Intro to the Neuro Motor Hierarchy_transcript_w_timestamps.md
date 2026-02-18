# Transcript: 2024-10-29-HMN24 - 04 - Intro to the Neuro Motor Hierarchy

## Source Information

- **Source Type:** Local File
- **File Path:** `C:\Users\jonma\syncthing-folders\jon-alienware-pc-synology-nas-sync\videos\video_eater_downloads\playlists\Neural Control of Real-World Human Movement (Fall 2024)\2024-10-29-HMN24 - 04 - Intro to the Neuro Motor Hierarchy\2024-10-29-HMN24 - 04 - Intro to the Neuro Motor Hierarchy.mp4`

---

**Total Duration:** 01:20:46

---

## Full Transcript

### Chunk 1 [00:00:01 - 00:10:00]

**[00:00:01]** Okay. Hello everybody.

**[00:00:06]** So today we're gonna talk about actual proper kind of sort of neuroscience for arguably the first time, which is always an exciting point, especially halfway through the semester. Also in line with traditional. I realized when I got in here that I had taken a bunch of notes and written a bunch of stuff up, but then forgot to push it up. So I don't have the most up to date stuff here, but that's fine. Basically this is the point of the semester where the divergence from the plan becomes more noticeable.

**[00:00:44]** So we are here, roughly, and we did some of this stuff, but not all of it. We haven't talked about eyeballs yet, but we'll start talking about vision and stuff probably next time. And yeah, and then the evolution stuff I'll probably combine together and we'll get to it. The sort of soft goal is at some point before the end of the semester to get to a point where I'm talking about my actual proper human scientist research, which has a lot of different sort of background aspects because it's visual control of locomotion of rough terrain. So it's sort of all these things kind of like mushed together and then have enough time to do some additional topic stuff towards the end.

**[00:01:31]** And I think we'll get there. So the.

**[00:01:42]** So catching up with where we currently are, we've done, I guess. So while I'm talking in the server at the top under this resources channel, the same place we talked about last time. So this thread called Server Scrape Checkpoints, click into that. I did figure out what was wrong with the last one. It was a stick.

**[00:02:10]** Stupid Windows things. So Windows has this thing where at some point in its history they decided that 280 characters is as long as a file path ever needs to be, or in fact should be. So it throws an error if your path links get too long, which you can change that setting and say we don't need to do that anymore. But this zip file had long file names. So that's what the error was.

**[00:02:35]** It was like these paths are too long. So this 7Z is a different form of zip that doesn't have that error. So if you want to see where things were last week, this one is the one that's up to date to that one. This one was from this morning. If you download this unzip it, it will still throw two errors saying the PKL and JSON files are unhappy, but just skip those and unpack the rest of it and try to open it up in Obsidian.

**[00:03:06]** And hopefully by the time you get to that point. I will have gotten to that point in my conversation. So give that a shot, see how far you get.

**[00:03:16]** So the. Yeah. So a lot of the stuff we've been doing up until now has been on the kind of like data and computational side of things. So the topic of the course is neural control of real world human movement. And we are going to talk and so we've been focusing more up to this point on basic methods and sort of like the kinds of data that you can collect and sort of the measurements that you can take and a little bit into the sort of more I'll say like high theory side of things.

**[00:03:51]** So all the talk about full body center of mass and sort of those like base level physics and sort of hyper simplified models of the body and sort of as it move, moves around the world is all of those things are kind of about the study of. It's more about the study of the neural control of real world human movement. Basically focusing on the kinds of measurements you can take. The empirical investigation conversations thereto pertaining.

**[00:04:25]** We're going to go back into that methodsy stuff when we talk about vision when it's bring out the eye tracker and do sort of more data looking. But today I want to give more of a sort of focusing more on like the, the landscape of what we think about neural control and what we think about motor control. This is something that I have, I found myself when I was sort of going around in the conversations at the end, at the last, last parts of previous classes, something I sort of found myself referring back to a lot. So it's not directly on the presumed syllabus but I want to talk today about the concept of the motor hierarchy as it pertains to the neural control of movement. Because it's one of those things where it's like.

**[00:05:14]** It's a very fundamental aspect of our neural motor systems that it is arranged in this sort of hierarchical way where the cortex and sort of the lumpy pink thing on top, at the top of the hierarchy and then going down to the various sort of subcortical systems and spinal cord and muscles and sort of at the bottom of that hierarchy would be what you might consider like the base level physics of the world. So we're going to talk about that but we're not going to do particularly deep dives into any aspect of it because I want to give enough time for us to do more of the kind of splitting off into groups and doing our own explorations. This time we're going to do a Little bit more clumping by presumed topic as we chop up the room into sort of like, which part of this hierarchy do we want to talk about today? And then the idea is to sort of try to use your collective efforts to flesh out parts of the brain. Brief overview, brief, fast, dense overview that I'm going to give in a second here.

**[00:06:20]** So we'll get to that in a second. So, yeah, so this kind of exploration of y' all doing some of the work of helping to flesh out the landscape, we've been playing with it a little bit with sort of talking to the bot and sort of asking it questions about your own presumed interests. And as the semester has progressed, I've made more progress into basically updating the code that I have been using to scrape those conversations out of the server and then put them into the. Not the bot, but just another sort of like, configuration of AI stuff and basically asking a different LLM configuration to pull out the topics that you all have been asking about in order to get a landscape of the topics that you have been interested in. So in order to look at that.

**[00:07:31]** Yeah. So on the assumption that you have downloaded the zip file and extracted it, if you're on a Mac, it'll look a little bit different, but at this point in your life, I assume you know how to unzip things. If you don't, ask a neighbor. If your neighbor doesn't know, just chill out and ask me later.

**[00:07:54]** So you want to download it, extract it, and this always gets creaky when I come on. Yeah, and then extract it. So it's just like a regular old folder in here, just anywhere on your computer. And then you should have at some point downloaded Obsidian. ObsidianMD.

**[00:08:24]** Just search for it. It's a free software and when you so get it, download it, double click it. It will look a little bit different the first time you open it, but so weird. Did I do that on this computer yet? I can't remember.

**[00:08:47]** And what you'll want to is.

**[00:08:57]** So for me, it's down here. If you're on a Mac, it might look a little different, but you're going to want to find something that looks something like Manage Vaults or openvault or I think if you do probably Control O, it might give you a screen that looks something like this. And the option that you want is called Open folder as Vault. Upstanding just calls folders Vault faults for whatever reason.

**[00:09:23]** So open that and navigate to the folder that you just extracted. There's a bunch of unnecessary subfolders in that zip file, which I figured out this morning. It doesn't matter which one you pick, but just to make it a little bit cleaner, I'm going to click in through top level into AI Processed. This server scrapes is just the raw data, so it's effectively the MD markdown file that's attached to the top of each.

---

### Chunk 2 [00:09:45 - 00:19:44]

**[00:09:45]** Through top level into AI processed. This server scrapes is just the raw data. So it's effectively the MD markdown file that's attached to the top of each chat. This is basically a folder full of those things laid out in a similar structure to the server. So I'm just going to click through that into AI processed.

**[00:10:09]** And then this is the stuff where they're not necessarily way too many stuff in there. So I'm in here. And you will notice that these folder names correspond to the same categories that we have in the actual server. And then if you click into that, these will correspond to the names of the. So that's in topics vision.

**[00:10:37]** And then it's got the same names as all the channels. And then where'd it go? Oh, I'm getting distracted, as I often do. Okay, so in here I'm going to select this folder, let Obsidian open it up.

**[00:11:03]** It's white for some reason. I don't know why it decided to be light mode for me. But that's fine enough for now.

**[00:11:12]** There's a lot of stuff in here. And basically, if you click through this every. So now, in addition to the raw conversation, which is attached to the bottom and you've got links here, if you click on the link, it'll take you to that message in the server, probably on the browser version of the server. And then up here is sort of an extracted summary of the topics covered in this conversation, which was presumably about eye tracking and VR, whoever it was that had that conversation.

**[00:11:45]** And there's a lot of like, art to how to figure out, like sort of the right way to tell an LLM to chew on a big blob of text in order to pull out topics. But in this particular case I was mostly focused on just getting raw topics covered. So I gave it the structure of like, pull out a title. A extremely short summary highlights a very short summary. A short summary and a detailed summary.

**[00:12:15]** Sort of like different levels of abstraction to sort of make that do its thing. And then importantly, I also added pull out tags. So these tags are just sort of hashtag. This is called kebab case because it's dash. It's lowercase numbers with little strings between them or hyphens between them.

**[00:12:37]** And what the tags allow us to do is click on this little graph view thing over here. And that gives us this fun thing here. So these dots are all of the. So each one of these dots corresponds to one of the chats that was had. And if we go over to filters and turn on tags These are all the tags that were covered.

**[00:13:07]** So there's a couple things to note here. First of all, this is fun. I love this type of thing and I think I can. There's a lot of options for the display. I don't know why it's in light mode, but that's fine.

**[00:13:21]** Let the text be a little there, let the nodes be a little smaller noise be a little less thick, so you can sort of navigate around in here. The green ones are the tags and the black ones are the notes. This is the kind of thing, like, I don't want to belabor this particular point too deeply and sort of get too, too hard into the technical aspects of how to use this type of stuff. Obsidian is nice because there's a lot of tutorials and stuff. So if you're curious about how to take notes like this and sort of have your general notes that you're taking in your life, have this sort of nice internalized structure, just hop on YouTube and search for Obsidian and you'll find lots of good stuff there.

**[00:14:12]** But the basic idea is so there's certain tags. So like biomechanics. Can I do it? Doesn't really help much, but that's okay. So we've been doing.

**[00:14:27]** So this is the biomechanics tag. So we've been doing a lot of talking about the biomechanics of the situation. So unsurprisingly, that tag is present in a lot of your conversations. And so if I click on that, it will show me all of the tags that have been discussed. And so you can look up, let's say impact of knee injuries on biomechanics.

**[00:14:54]** And so I can click on there. And this is a conversation that one of y' all had about knee injuries and biomechanics. And this is what was discussed in there. And you can click on this and it will take me to the server version or the online browser version has to load up.

**[00:15:14]** Yeah, so this was Grace, if you're in here, do, do, do. Where'd you go? Yeah, is that the right one? Wait, no, it's a different thing.

**[00:15:31]** Yeah, yeah. So biomechanics is very well connected. Straight neuroscience is obviously well connected. Neural control is well connected. There's also some like orphans out here that are not connected.

**[00:15:49]** So mathematical ambiguity and interpretations, sometimes these are caused by like just like a conversation that's super short. So it's not actually there's not much content there. But AI has people pleaser energy. So if you tell it to summarize something that only has someone saying hello and then nothing else. It will still try to come up with the full summary, even though that's not valid to do in this particular case.

**[00:16:16]** Someone was asking mathematics, order of operations, something like that. Oh, actually, no. Remember how I told you that I was not going to scrape the plug Playground channel? I lied. It is in here because it's easier to not.

**[00:16:27]** It's easier to just not ignore it. So there are occasionally some of these that are like it's doing its best to pull a reasonable summary out of a conversation that is intentionally misleading. So.

**[00:16:44]** Okay. And so I'm going to leave that roughly there. Feel free. I guess another thing to say is you'll notice too that a lot of these tags are orphan tags. This is being included only in one conversation.

**[00:17:03]** This thing saccades is something that would probably be. It'll probably be connected more once we finish talking about eye movements. But some of these two, like trust. Trust doesn't need to be a tag in this class. And so that's something.

**[00:17:19]** The way that I wrote the prompt, I didn't do any cleanup after the fact. It just pulled stuff that really shouldn't be there. Brain computer interfaces probably should be in there.

**[00:17:33]** Seeds in body. Someone was talking about eating plants. I remember that. That was a. Yeah.

**[00:17:43]** There's some things here where you can kind of tell that the way that it is extracted the information makes it more. Actually didn't do a terrible job this time. So consciousness variations. That tag should really be consciousness. And then anyone else who talked about that, which I know there's at least a couple of you would get matched in there.

**[00:18:10]** So this is the case where the way that the bot extracted the tags, if that was done more sort of skillfully or carefully, it would be a more connected system of topics and content. So some of that is about having more conversations to get more connections. Some of it's about making the prompt a little better. And then anytime you're doing anything with AI and language generation, there's always needs to be kind of like a human cleanup step. So I could go through and clean this up.

**[00:18:42]** I could ask you to clean it up and maybe we'll do that. We're going to be using Musikin money. What are you talking about? Yeah. So figuring out how to explore this stuff, you all can jump in there and look at what your classmates have been talking about.

**[00:19:03]** We're going to be doing in the latter part of the class sort of a little bit more in the direction of y' all producing more like curated BLOBS of text that are sort of designed to help pull together some of these disparate, disconnected things. And I will be continuing over the course of the semester to sort of increase the sophistication of this extraction. And the idea is to sort of find a way to let all of you kind of have the ways that you have been exploring this topic and this space cohere into a sort of a navigable landscape of this sort of.

---

### Chunk 3 [00:19:30 - 00:29:20]

**[00:19:30]** And the idea is to sort of find a way to let all of you kind of like have the ways that you have been exploring this topic in this space cohere into a sort of a navigable landscape of this sort of comedically vast topic.

**[00:19:49]** Yeah. So yeah, I tried to get it not to do this. I told it like, don't use names. But one's like, this topic is about Carolyn's interest in human anatomy and surgery. It's like that should not.

**[00:20:03]** That's the bad. That's a bad title there. But it's not Carolyn's fault. That's just the way, like being more careful with the prompting to like make sure that it doesn't do that stuff and keeping the style consistent. Because I also just to make it run fast and cheap, I.

**[00:20:21]** This one was. Was processed by GPT 3.5, who is dumber than 3.4 or GPT 4 and the latter ones. But it is also like very, very, very fast and effectively free at this point. So with this thing, we're processing high enough volume of text that the cost becomes noticeable if you use the bigger stuff. And if you use the bigger models, it would take half an hour to an hour or more to process all these things.

**[00:20:52]** Whereas with 3.5, it's effectively free and processes in 30 seconds as opposed to 30 minutes for stuff like extracting summaries. It's smart enough for that. That's what. Natural language processing has been doing that for 20 years. But you do get some dumb, dumb behavior where it's like, that's not even the right capitalization there.

**[00:21:18]** Okay, cool. So yeah, so if that makes sense, great. If it doesn't make sense, also fine. If you have technical issues getting it running and sort of getting the point where you can look at it. We'll handle that in a little bit here.

**[00:21:41]** But yeah, there's no real obligations for you with this side of class. Right now. This is more of a. I am giving you updates on my homework and this is where we're at with it because real work is typically speaking, iterative in nature.

**[00:22:00]** Okay, so.

**[00:22:22]** So this is the place where, if I had successfully pushed my notes to GitHub, I would be looking at them right now. But they weren't particularly extensive anyway, so. So I'll take this as an opportunity to show a little bit about how bot work.

**[00:22:41]** So with something like, I'm giving an undergraduate lecture on the neural motor hierarchy in your nervous system. That is such a well trod topic. That's like sort of intro level to any Class that talks about motor neuroscience is going to talk about the motor hierarchy. So if I ask the bot to say, give me a lecture outline for the motor motor hierarchy hirer key, it'll give me something good. Especially because it already has the syllabus of the class kind of baked into it with that sort of the top level prompt.

**[00:23:25]** I have this other sort of.

**[00:23:30]** Yeah, see, perfect.

**[00:23:35]** I have this other sort of channel over here where I just use AI for my own purposes, which you can make your own as well if you want, but we'll talk about that later. Or maybe not. So in that server, if I wanted to, because it isn't prompted in the same way that this class is, if I gave it that simple of a preamble, it wouldn't do as good of a job. But because this one is already in the context of having the syllabus of the server, the class already baked into itself, it does a decent job.

**[00:24:17]** Give me the order from highest to lowest, because it did that the other way.

**[00:24:28]** Great.

**[00:24:32]** So there you go. Now you have everything you need to know about the motor hierarchy, not really this type of thing. And give me an additional outline about the corticospinal.

**[00:24:55]** Corticospinal tract.

**[00:25:03]** Yeah, so that's another sort of area. I wonder if it. Did it mention that in the original. Yeah, it did mention it briefly, but that's. This is another kind of thing.

**[00:25:12]** So like when you're, when you're navigating this kind of like AI mediated language space, there's often kind of a balance you want to strike between like what I think of as like top down versus bottom up types of investigations. So where a bottom up approach is kind of like giving it a very loose instruction set and just saying, just seeing what it pops out at you. So like, tell me about neuroscience. Don't give you a broad scoped thing versus more of a top down approach, which is where you as the human give it more structure and you say no, give me more specifically this type of thing and you get different responses that way and they both can be quite useful. So the analogy, and this is a sort of recurring theme when working with AI is oftentimes the strategies that work well with AI are also kind of like sort of funhouse versions of things that just generally work when you're talking to humans, if for no other reason than it was trained on human data.

**[00:26:17]** So like in this course when we started, you know, I said, hey, go have an introductory talk, ask the bot about whatever you want. That's a very bottom up approach. So I'm just saying, hey, room full of people, ask this thing a bunch of questions just based on whatever you are interested in talking about. And so when I do that. And a lot of the early part of this class sort of had that structure, the ones that are kind of driven by lectures, a little more structured.

**[00:26:44]** But a lot of the conversations so far have been very bottom up. And this meaning that I am not imposing a structure from the top down. And so the like the topics that are covered and that sort of graph that was shown is sort of a result of kind of that bottom up type of approach if I were to. So like, I guess in contrast if we think about like the kind of conversations that happen in this channel where this was the one that happened after the center of Mass basis Support lecture last time. This is.

**[00:27:17]** And I said, hey, now, ask the bot questions, have conversations about this lecture. That's implo. That's sort of, it's more structured, but it's still fairly open.

**[00:27:30]** Which, and then that would be contrasted with like saying, you know, write a class, write a paper about this topic. So when you're working with AI and you're trying to sort of steer it and you're trying to make it generate something that you feel like has some relationship to like your internal state, like something that you are trying to bring out into the world, it's often very beneficial to sort of switch back and forth between these two modes of thinking. So saying hey, give me an outline of this topic without a bunch of structure to it, and then taking that structure that it gives you, cleaning it up, altering it, editing it, and then giving it back and say, hey, give me some information about this outline. Flesh out this outline. And oftentimes it's not even worth doing that first step, if you already know what you're interested in, just ask it specific questions and you'll get specific answers.

**[00:28:22]** So it's sort of a. There's just like different modes of using this thing. And a thing I've mentioned a lot is sort of like, I think one of the best things that these AIs are really good for is helping you flesh out your unknown unknowns. Like you know, you have an interest in a topic, but you don't even know enough to know the parts that you have questions about. So just ask it generally tell me more about this, it'll give you a bunch of stuff and then you'll say I didn't even know what these words are.

**[00:28:47]** And then ask it about those words and kind of navigate it that way, but you also want to be able to drive the conversation a bit.

**[00:28:57]** Anyway, so I mostly asked to give me this just to have a cheat sheet of the actual parts I wanted to talk about.

**[00:29:19]** I always have to do this, right?

---

### Chunk 4 [00:29:19 - 00:39:05]

**[00:29:19]** I always have to do this, right?

**[00:29:30]** Okay, so do it like that.

**[00:29:39]** I guess I could do that like that.

**[00:29:45]** This is the part where I get mad at discord for its poor use of space.

**[00:30:01]** Okay. So the motor hierarchy, broadly speaking, corresponds to the basically the organization of responsibilities that within your motor cortex, sorry, not your motor system.

**[00:30:24]** From the high level abstract sort of thoughts of things like, I'm thirsty, I wish I had water, I'm hungry, I want to eat. Very abstract thoughts down to the level of like, I am trying to put force into the world so that I can move my body in the direction of water, in the direction of food.

**[00:30:49]** And the ways that we kind of like the way that like the needs of like, in order to complete a given task, you have to have a combination of those different levels. Because if you're only thinking about the motor system as like a thing that's attached to your muscles, that puts forces into the world in order to like pick up objects and push on the ground and do things like that, you're never actually going to get like coordinated behavior as you're moving in the direction of goals and stuff like that. At the same time, if you're only thinking about stuff in the context of like high order volitional desires of I prefer fruit to wheat, I get thirsty when I talk a lot or something like that, then you're not going to have the kind of goal driven behaviors that actually make coordinated movement actually meaningful and produce actual results.

**[00:31:46]** So I want to zoom in here. Yeah, sure.

**[00:31:58]** So again, I think I did a picture kind of like this at the beginning, but I'm just going to try to give you more of like an atlas of these parts and how they connect to each other and then work together on like fleshing out the details. And specifically today I want you guys to start use like looking at papers and looking up papers on these topics and then using the bot to help you like chew on some of the deeper stuff there. So again, moving away from like asking the raw AI to tell you sort of textbook level stories about, you know, high level stuff, basically like if Wikipedia could talk and start using it more as like a tool that you can use to navigate waters that are deeper than you can navigate on your own.

**[00:32:47]** So let's start with the brain. So first thing you got to do is draw a brain. Do it roughly like that. It's a brain, specifically. That's a mammalian brain.

**[00:32:58]** Mammalian brain.

**[00:33:09]** So this is not a brain. Someone asked an AI to draw a brain for them. That's not what a Brain looks like this is an inside of a brain.

**[00:33:21]** Yeah. What are the pictures I'm looking for?

**[00:33:27]** They all look roughly similar, but the main part that I try to draw when I'm just doing that sketch is this part right here is the. That lumpy part going down. That's your temporal lobe by your temple. And then the rest is kind of squiggly. It's.

**[00:33:47]** I've mentioned this before, but, like, you eventually start to learn that, like, all these little, like, squishes and folds and stuff like that, they all have names and they're not random. And you can kind of start to tell when you see brains in popular media, if it was based off of an actual brain or if it's just someone who is just like. It's just a bunch of squishy red stuff. Oh, yeah, this is the picture I was looking for. So it's all a little bit different.

**[00:34:10]** They're all rough. They're not shaped all the same. But they all have this. See, this is not a real brain that are missing some important parts, which is not great for an actual part there, but that's fine. And this is an object of pure horror.

**[00:34:28]** So.

**[00:34:31]** So your.

**[00:34:36]** So there you go. You got. This is your temporal lobe, and then this stuff up here is the front. Give yourself some eyeballs and that sort of goes in. That's forward, which is actually.

**[00:34:53]** No, it's fine for English speakers. We tend to put things point the other way. But that's okay. I always. I always.

**[00:35:03]** I don't know, I was raised speaking Arabic, so I learned sometimes right to left comes more naturally. And I'm just like. I don't know if that's actually normal or if that's just. I don't know, who cares?

**[00:35:17]** So don't put that one up. Let's put something like this one. Give us a proper actual brain, please. Oh, yeah, there we go.

**[00:35:36]** So this frontal lobe here is. All mammals have it. I don't want to really talk about mammalian brains here because I don't know how any of the rest of them work. Birds in particular, I'm very curious about, but they can be very intelligent with very strange. With very different nervous systems, and I don't want to know much about that.

**[00:35:57]** But the. The frontal lobe is sort of like the traditionally most human part. There's a lot of parts of our brain that are quite different from other animals. It's often just in terms of, like, the raw volume, but particularly when you start going into, like, you know, the. Our dumber mammal friends, like, Your cats and your rats and whatnot.

**[00:36:22]** The biggest differences tend to be a lack of that very pronounced bulbous frontal lobe. And where is that stupid thing? Oh, there it is.

**[00:36:37]** And so this part here is also, roughly speaking, generally speaking, the very top of the motor hierarchy is that frontal lobe executive function.

**[00:36:50]** And yeah, and so typically speaking, anytime someone's giving you any kind of specific words about how the brain works, please understand it is a cartoon version of reality. And reality is always weirder, more abstract and less understood than anything anyone could ever say while standing in a space talking to you in a room. But generally speaking, it is thought that like, that is where your sort of, your volitional control comes from. Volition is like root of voluntary. It's like the voluntary aspects of things.

**[00:37:25]** Like, I want to pick up this box and so I will pick up this box. That that initial desire is the volitional aspect of things. And that is sort of, you know, cartoon wise thought to. To sort of originate here in the prefrontal cortex, you know, frontal prefrontal cortex and the.

**[00:37:52]** Yeah, so that's where those sort of like the most abstract form of your motor desires originate in that sort of frontal lobe area. This is where the description of the content of the neural activity or the patterns of neural activity that we call motor control there is abstract, to the point of not even really referencing the body. Like, it's sort of like, I wish I had water, I wish I had food, or something like that.

**[00:38:26]** And yeah, and so that again, cartoon wise, is sort of passed back through like frontal prefrontal pre motor motor. And then this part here, sort of like on either side of your head, is the part we traditionally call the primary motor cortex, which will look something like.

**[00:39:03]** This is the part that tends to not get drawn.

---

### Chunk 5 [00:39:03 - 00:49:00]

**[00:39:03]** This is the part that tends to not get drawn.

**[00:39:15]** Yeah, there we go. That's what I was looking for before.

**[00:39:20]** Again, cartoon versions of reality. It's not based on nothing. There's a reason why we draw this cartoon and not some other cartoon. But nothing is this clean.

**[00:39:33]** And the basic trajectory is that those original high level volitional aspects of control are sort of. They get passed through different sub regions of that brain.

**[00:39:50]** This part is sort of roughly your premotor cortex, which sort of starts to get more specific. And then by the time you get to the motor cortex, that's where things are thought to start having a resemblance to your body. So you have. This is again another. This is the kind of picture that you will see in a lot of textbooks about neuroscience.

**[00:40:11]** You may have seen it before. It's also the kind of thing that you will never see in a talk about motor cortex. This is the kind of thing where this picture of. So this is sort of the idea that like, you know, different parts of your brain handle the movement of different parts of your body. And so you get this very over representation of things like your hands, which has a lot of motor control associated with it and much less representation of things like your hip and leg, which are sort of more simplified.

**[00:40:43]** And then you know, over representation of things like the face, because we do things like talking about. And so the idea is that the, again, the cartoon version of the story is that the high level desires to grab a cup of water or something like that gets passed through to the lower. From the high level at the frontal lobes and then passed through to the more specific areas of the motor cortex and then translated into sort of a more body mapped description of how to move from one place to the other.

**[00:41:16]** And that is there's this horrible little man sensori motor homunculus that sometimes gets drawn as the. This is what you look like on the inside. This is your body map of yourself. This is basically your body, well, not necessarily yours, but mapped to the sort of the cortical magnification of the different parts of your movement. This is clearly the sensory homunculus.

**[00:41:51]** If you can't figure out why, that's a lesson to the reader. But the idea is that if you were to map out your motor awareness and your sensory specificity, this is what you would look like. However, this is also the kind of thing, as I mentioned that. Yeah, and so there's the sensory core. The motor cortex is sort of very close to the sense the somatosensory cortex, which is sort of like the sensory aspect of things.

**[00:42:24]** So in the same way that we would move our elbows, wrists, and hands, we also have sensations from those areas, and they are sort of right next to each other.

**[00:42:35]** But again, I have seen many, many talks from many, many people, often on the topic, who study things like motor control and sensory motor control. And the topic of those talks is typically trying to say, please stop showing this to students. It is not an accurate representation of reality. But then. And then they say a bunch of much, much more complicated stuff about how it's not really how it is.

**[00:42:58]** But this is the easiest way to discuss things like cortical magnification at the motor and sensory levels. Just understand that it is not a nice, clear, clean map. It is not the type of thing like, oh, here's where your wrist is, here's where your hand is. It's much more complex. It's much more spread out.

**[00:43:18]** It's much less organized.

**[00:43:22]** But if you sort of zoom out and squint and turn your head, this cartoon version of reality is a good place to start. This is also the kind of thing where, if you wanted to look up more recent papers about the structure and organization of the motor cortex, sensory motor cortex, you'll find a lot of good stuff, people actually doing that work. It's also the kind of thing where if you ask the bot to tell you about this, it will probably tell you this part, and you might have to push it to be like, is that really what people think? And you might be like, ah, I actually don't know what it would do. I think that is getting to the level of specificity and contemporariness of research, where the fact that the bot has eaten every textbook might make it harder for it to deviate from the cartoonized version of reality that we tend to put into textbooks.

**[00:44:10]** So this would be. If you wanted to sort of try to push the bot until it breaks, you might try to find a more recent paper on this topic and then find places where the bot gives you stuff that is not actually aligned with what we think in reality.

**[00:44:28]** It's kind of had a brief moment of thinking about how that relates to things like Wikipedia, But I think Wikipedia is famously fast. So Wikipedia tends not to sort of hold on to wrong thoughts for very long. So I think Wikipedia would probably give you, like, quicker and directer sort of summary overviews of more modern thinking, but I'm actually not sure that's one of those spots. Anyways, motor hierarchy. Here we are.

**[00:44:55]** We're starting in the frontal cortex, going back to the motor cortex. Later, when we talk about vision, vision tends to start here in the occipital lobe. There is this sense of this chunk of the brain is for sensory information, and this chunk is for high level thoughts and abstraction and motor cortices and stuff like that. And then this part down here is weird. And we don't talk about it.

**[00:45:21]** I don't talk about it because that's more about like recognizing a cup for more like memory and sort of more like contentful thinking. But I don't know much about that. But that's why. I don't know about why, but like the motor cortex being here and the somattery cortex being there. The way that I can remember that, it's because the somatic cortex is closer to the visual cortex because that's like the vision side of things, which only helps if you know where the visual cortex is.

**[00:45:48]** But they sort of meet here.

**[00:45:55]** And I'm going to continue the story, but just so you know, from this juncture is there's also a path that says that sort of bypasses the route that I'm about to tell you that things tend to go. So we started out saying, hey, I wish I had water that gets sort of trundled along and gets converted into something like a motor plan in the motor cortex that says, oh, hey, there's water right there. Let's assume, I don't care about the fact that it's not mine. I could reach out and grab that, which would require taking a couple steps, moving my arm out and sort of grabbing the thing, notwithstanding the complexity of the fact that there was steps involved. So that's sort of, that's a whole other conversation.

**[00:46:44]** And I think that's also where a lot of the question marks in the, in the research live right now is like what happens when you have a motor plan that needs to sort of evolve over time. Like I need to walk over there and then do a behavior that's, I think, an area of neuroscience that we really don't know as much about. And that's where the specific tagline of this course being about the neural control of human movement in the real world is where it starts to touch parts of neuroscience that we just don't really know much about. Because if you think about the methods involved, the vast, vast, vast majority of neuroscience research, I call it psychological research, is done of people sitting in chairs, doing stuff on a tabletop, doing single joint movements, and our ability to measure the neural activity of humans in general. But animals, specific animals at all moving around in a space while also recording the brain is we basically can't.

**[00:47:41]** We can start to. We have we have been starting to be able to do that over the past like decade or so but still a lot of the theories that we have are based on research that does not involve the animals being able to like move through the world and actually sort of have multi step processes. So if you have questions about how that works the answer is we largely don't know but find some papers and you might find people who are working on those questions.

**[00:48:10]** So all of this is happening in the cortex the big lumpy pink thing on the top and there's a bunch of other stuff that we tend to call that sort of a lot of other parts of your central nervous system that we lump together under the heading of subcortical regions and personal favorite is the cerebellum which is this sort of lumpy part down there.

**[00:48:41]** Cerebellum, cerebellum little brain great but and I was.

---

### Chunk 6 [00:48:48 - 00:58:44]

**[00:48:48]** Cerebellum, little brain. Great, but. And I'm going to talk about that in just a second. But there's another component that I want to at least mention. Honorable mentions of a particular piece that sort of lives in the middle.

**[00:49:14]** We're doing a side view. All these parts are doubled on either side. And for some reason, your left side control the left side of your brain, controls the right side of your body. Don't ask me why, just how we evolved. But there's this very important part called the basal ganglia.

**[00:49:33]** And this is particularly interesting for those of you all that are interested in things like movement disorders, because it's a part that can go wrong in various interesting ways. Because the idea is that when you have this, when you have that high level thought of like, I want to be. I wish I was holding this, this box. And I'm sitting here and I'm looking at the box, there's a lot of different ways that my body could solve that problem. I could grab it with my dominant hand.

**[00:50:01]** I could grab it with my non dominant hand. I could grab it with my dominant hand. In a weird way, I could move over here and grab it with my dominant hand. All of these are options that would satisfy that high level volitional desire to be holding this box in my hand. And so with any kind of a network.

**[00:50:18]** So we often talk about the brain as kind of like serial processing, kind of like computer analogy. This is in line with our general approach of just humans, a general approach of always describing the nervous system in the context of the most advanced piece of technology that we have. If you go back to history, we tend to always do that.

**[00:50:39]** So anytime you're talking about a network, the thinking is. And again, this is deep into the cartoon version of stories that when I have the desire to pick up a certain object or pick up a pen or whatever, the motor network components that would generate that action all get activated a little bit, and they get activated to the point, and then they engage in a kind of like competition with each other. Motor plan competition, I think, is a term you can look up for that.

**[00:51:21]** But it wouldn't really work if every time I had a thought, all of the possible options to make that thing happen were activated at the same time. That's where this little superior colliculus guy, his presumed cartoonized role is to suppress your motor commands until they reach a certain threshold of activation. And in this very abstract sense, the best motor command wins out. And then that one crosses the threshold, and then that's the one that gets triggered and actually moves through. So in this case, it's closest to my dominant hand.

**[00:52:01]** I like using my dominant hand. This is a comfortable strategy. This is a not comfortable strategy. So this motor command wins the fight between all the possible ways I could solve that problem, and that's the one that occurs.

**[00:52:19]** You can talk for days about the details there, the substantial Niagara and blah, blah, blah. But the point I wanted to point out here is that there are at least two ways that that process could go wrong.

**[00:52:36]** One way is that the gating, like the suppression that the superior click list does, can be too strong to the point where none of those commands actually make it through the gate. And I'm sitting here wanting to move, but I can't actually initiate the action. And that way of things going wrong is typically what happens in things like Parkinson's disease. Parkinson's is complicated, but one of the family of symptoms is things, things like freezing, freezing in gate, freezing in motor command. And people, they see what they want to do and they can't initiate the action.

**[00:53:15]** And that is thought to be related to the superior colliculus sort of gating the problem too hard. So none of the available motor commands are able to sort of trip over the gate and actually make things initialized.

**[00:53:30]** And there's interesting stuff there. Another way that that can go wrong is the thing I said before of like, it would be bad if all the motor commands happened all at once. And that's another thing that can happen in, specifically in a disease called Huntington's disease, which is a famously, famously genetically predictable motor disease. It's like one of these things, it's very heritable. And if you have, it's like a 50, 50 shot of inheriting it from a given parent.

**[00:54:06]** So if one of your parents has Huntington's disease, you have a 25% chance of having Huntington's disease. And we can just look at your genome and be like, oh yeah, you got it, or oh yeah, you don't. So it's a sort of socially horrible thing. And there's like, I think there's like episodes of like House or things where it's like, what are the ethics of a, having a kid? If you know there's a 25%, they're going to have this degenerative disorder.

**[00:54:30]** And B, what are the ethics of checking if you have it? And if you get some assay of tests, it may happen that the doctors just know the answer to whether or not you are going to have a degenerative mortar disorder later in your life. And so all sorts of not so fun conversations there. But people with Huntington's disease exhibit spastic behavior where they basically have, like, movements that they didn't really intend to initiate that sort of make it over the hump before they were able to be sort of stopped. And that's where you get strange behaviors where, like, if you show.

**[00:55:10]** If you hold, like, a cup with a handle in front of somebody who has things like Huntington's disease, they have a very hard time not reaching out and grabbing it, because they see it. They see the possibility of grabbing it, and their superior colliculus or whatever, or cartoons, whatever, is not able to suppress that behavior. So they just reach out and grab things that they weren't intending to. So, anyways, there's a lot more going on in there. But I did want to mention that just because I know that there's a general good chunk of y' all are pre med, so a good chunk of y' all are interested in movement disorders.

**[00:55:51]** And a lot of movement disorders tend to live in and around that area anyway. So once those motor. But once the motor can have been connected or sort of chosen or selected or sort of made it over that hump, that's where there's a cascade of activations that sort of happen from that point. And generally speaking, that will then sort of leave the brain and sort of first. Well, I don't know about first, but it will sort of get into the cerebellum and then into the brain stem and then into the spinal cord.

**[00:56:35]** Cerebellum. Very complicated thing, Very complex thing. Roughly 3.5 as many. 3.5 times as many neurons in your cerebellum as there are in the rest of your central nervous system combined. They tend to be very small, very, you know, specific or not specific.

**[00:56:54]** They're very small neurons, like granule cells, but also very large neurons called pyramidal cells. I will look at primal cells because they're beautiful pyramidal cells, neurons.

**[00:57:24]** So you get these. Oh, this is the one I was looking for. This is the kind of thing you win a. You win Nobel prizes for pictures like that back in, you know, 1800s. But these are the type of neurons that you get.

**[00:57:40]** This might actually be in your motor cortex, but these, like, highly. Highly synaptic, like. Like massive synaptic forests where the output of the neuron, whether or not it's spiking, is dependent on this massive network of connections to other parts of your body or other parts of your nervous system versus more. Yeah. Anyways, your cerebellum is thought to be the area that sort of handles things like motor coordination, and that's coordination that happens at different levels.

**[00:58:24]** Like most of your nervous system, there's sort of an inside out structure where the inner parts of your cerebellum, like the inner parts of your brain, is the most phylogenically ancient. It's the oldest part. And as you sort of go outwards, you get more and more evolutionarily new stuff until you get out to the.

---

### Chunk 7 [00:58:30 - 01:08:29]

**[00:58:30]** Of your cerebellum, like the inner parts of your brain, is the most phylogenically ancient. It's the oldest part. And as you sort of go outwards, you get more and more evolutionarily new stuff until you get out to the neocerebellum, which is the outer. This, it looks like a lump, but it's kind of folded up in on itself. And the neocerebellum is on the outside.

**[00:58:55]** And that's the part that's thought to be associated with things like tool use. And the fact that I can pick up an object that's not a part of my body and sort of like wave it around and then oh yeah, I've sort of like internalized some of the physics of this thing. And that ability to internalize the physics and sort of utilize external objects as if they were a part of my body is thought to be related to the neocerebellum. And there's some interesting studies in FMRI where they have people like playing with tools and stuff like that.

**[00:59:27]** And I always get like stuck on these little side quests because I just have to tell the story because it's so interesting.

**[00:59:37]** Not all animals can use tools, obviously, but there's a concept in neuroscience called your peripersonal space. We tend to chop up the world into spots. And you know, out there that's like far away stuff. In here, this is like, this is my actual body part. And then there's the peripersonal space, which is like close by areas like roughly speaking, things that I can reach with my sort of, with my current body.

**[01:00:09]** And so anything that's on this table is peripersonal space. And if you take a monkey, like a macaque monkey or non human primate, one of the few that we study, and you can get certain. So you can lesion the brain in various ways and you get various types of blindness. And it's possible to get a type with a particular damage in a particular area. Actually, I don't know that level.

**[01:00:37]** You can get a blindness in peripersonal space. So you basically there's just like, you can't see things that are sort of within a certain range of you. And there's a crazy study where they took a macaque and they were able to give it like a reversible lesion. So they put a chemical in that part of the brain. So it just stops working for a little while, but then after a while it comes back and they trained the monkey to use a grabber, like a grabber thing to reach out and grab things that are farther away than their arms reach.

**[01:01:11]** And after the monkey was trained in using the grabber arm, and they did the cortical legion, their peripersonal space extended to include the regions that they could reach with the grabber. So there's just this strange implication of how we tend to view the world and how we tend to carve it up into things that are me, things that are not me, and then things that I can directly manipulate. And for certain types of mammals, that question of what part of the world is my body and what part of the world can interact with my body includes things like tools, includes things that are not necessarily part of the raw biology, which gets into the philosophy of things, Especially when we start extending the concept of tools and away from things like grabbers and hammers and sharp pointy rocks and into things like laptops and the Internet and large language models. Like, these are all these things. Like, we tend to really prioritize, like the meatware and do things like make you take tests on pen and paper, even though who gives a shit about what you can, like, recall under duress.

**[01:02:27]** But there's a whole concept of, like, embodied cognition which sort of tries to extend that notion that, like, we really are like ourselves, plus our tool set, plus, you know, our community of people who can help us with things. And that's anyways. Gets complicated and philosophical very quickly.

**[01:02:51]** So. Yeah, and then the lower parts of the cerebellum, the older parts handle things like motor coordination. And so things like if I want to. So you have your flexion parts and you have your extension parts, your muscles, these ones, like the flexion tends to move you towards the fetal position. Extension tends to move you opposite of that.

**[01:03:14]** And in order for a movement to be smooth, those things like the flexor extensor groups have to fire in a very tight temporal loop. And if you. If they misfire, then you get, again, kind of like spastic behavior. Kind of like, you know, I hate doing, like, I hate simulating it because it sort of feels weird. But, like, you can imagine sort of like seeing people with movement disorders.

**[01:03:42]** They have this kind of like, jerky movements that can be. It can come from a lot of different places, but it can be associated with basically, like, misfiring, where you're like, if I'm extending my arm, then my flexor of my. Then the triceps should be engaging and the biceps should be loose. But if my biceps kept firing while I'm trying to extend my arm, then you get this kind of like jerkier behavior.

**[01:04:11]** And that's coupled with like another type of disorder which can happen, which can lead to sort of what they call like the drunkard's wobble. Like when you like where you sort of like, it's more of a swimier type of thing, where it's like, this is like my, my postural control system is firing, but it's like slow, so you get this kind of like more of a soupy type of movement. So those are all just different parts of the cascade of things that can go wrong in the motor system.

**[01:04:44]** Cerebral bellar ataxia is one of those terms you can look up. Anyway, so, yeah, that's in your cerebellum. Your brain stem is kind of hanging out here. Brainstem is honestly a part that I know least about. It's sort of a level below the cerebellum.

**[01:05:08]** It sort of has to do more with like, it's thought to be related to sensory integration, but it's kind of like in my understanding of this space, I kind of lump it in with that host of very low level integrations between that sort of flexor extensor groups and timing and integration of sensory information, where that sensory information, meaning the forces that are happening at your joints, less than like the visual information.

**[01:05:44]** So, you know, if you wanted to look up how the brainstem interacts with stuff that you could do that. But I don't have as much information there.

**[01:05:54]** The part that I do know more about is the spinal cord, which is we tend to think of in common parlance, like people like oftentimes when we draw the nerve, the central nervous system, we draw it like this and we cut off the spinal cord. This is wrong. This is incorrect. Your spinal cord is a part of your central nervous system and it does a lot of really interesting and important aspects of your motor control.

**[01:06:25]** Your spinal cord.

**[01:06:28]** Spinal cord.

**[01:06:34]** Yeah, there we go.

**[01:06:39]** Wikipedia.

**[01:06:45]** So your spinal cord doesn't go all the way down your spinal column. Spinal column is the bone part. It stops around here. So like right below your rib cage. And then the rest is like peripheral nerves that sort of go in and out to the actual innervating the muscles.

**[01:07:07]** It flips inside out. So your, your, your cortex has the, the gray matter, which is all the bodies of the neurons on the outside and all the, the wires and the white matter, which is like the glial cell wrapped things on the inside. Spinal cord flips that around so all the goopy wiring stuff is on the outside. And this is where you sort of this blue stuff here is the same gray matter that's on the outside of your cortex. And the kinds of.

**[01:07:39]** I never have enough time to talk.

**[01:07:44]** The like, your spine is. We're now getting down to, like, the very the very bottom of that motor hierarchy. And the kinds of controls you get at the spinal level are still definite in the space of what we would call, like, processing.

**[01:08:02]** But there's very little abstraction, if anything, down there. So that's where your spinal cord handles things like your reflexes. So, like, if you ever go to the doctor and they hit you on the knee, and then it kicks your hits you on the knee, the tendon, and it kicks your knee out, they're testing your spinal reflexes. And one of the most low level ones is the monosynaptic stretch reflex, which is if this muscle is stretched.

---

### Chunk 8 [01:08:15 - 01:18:13]

**[01:08:15]** And then it hits you on the tendon and it kicks your knee out. They're testing your spinal reflexes and one of the most low level ones is the monosynaptic stretch reflex, which is if this muscle is stretched, there is a reflex that makes it contract, sort of a protective thing. So when you hit the tendon, it stretches the muscle and then that goes up to the spine. And the reflex there is, if that muscle stretched, then compact it, and that's why you kick out. However, it's not as simple as just a sort of.

**[01:08:50]** There's a reflex that's there and it's always there, because if that reflex was always active, then you wouldn't be able to do things like move your leg, because every time you moved it, it would stretch and then that would make it contract. So your spine handles what's called reflex gating. And where in order to engage a given motor plan, the reflexes have to be configured in a certain way. And the most sort of famous, and my personal favorite example of that is in the context of the locomotor gait cycle, where when you're walking, you're sort of going back and forth between each leg is sort of going back and forth between stance phase, where in stance phase you're holding the entire weight of your body on a very stiff leg. If you're running or something like that, when you impact the ground, you're impacting it with like 1.4 or more times your body weight.

**[01:09:48]** So your leg has to be very stiff in that moment when it hits the ground. Someone I think, asking about, like, if you step off of a stair and you think there's going to be another stair there or there's one more, one fewer stairs, then you, you expect you have that kind of like very unpleasant moment where the limb was preparing for the ground that was not at the right level. So, sorry. So when you're stepping back and forth, your legs are going back and forth between stance phase, where all of your reflexes are sort of cranked down to let your leg be very stiff and support your whole weight of your body. And then swing phase, where the.

**[01:10:26]** They're all kind of turned off, basically to let your leg be much more floppy and loose so it can swing through and basically utilize its own momentum to allow it to sort of move forward without having to like burn a bunch of muscles, burn a bunch of energy, like moving it directly. And so that transition from, like stance to swing phase, which happens roughly every 450 milliseconds, roughly a million times per year. For a healthy undergraduate human, that transition is happening at the level of the spine. And that specifically the timing of transitioning from one to the other is handled by things called central pattern generators, which is where a lot of the basic rhythmicity of motor control comes from. Most of your motor system is rhythmic in nature.

**[01:11:19]** So you're walking, you're chewing, you're scratching, you're doing things that are kind of like, have a rhythmic aspect to it. And that's kind of handled by these central pattern generators. But then where the hierarchy kind of comes in, the sort of motor hierarchy tends to come in. In order for movements to be graceful and coordinated and smooth, they have to be appropriate for the world as it lays out. So if I'm stepping up onto a step or stepping down at something or from interacting with the world, there is a supervenience that happens where those high level volitions, those high level desires attached, coupled with visual information or sort of sensory information, what's out in the world gets translated into basically a set of instructions for how we should lay out the reflexes and what the timing and the strength and the gains of all these reflexes should be in order to generate movements that are appropriate for the world that's around you.

**[01:12:28]** So the idea is down here, at the lowest level of the nervous system, these very, very low level things are happening on the basis of instruction sets that come from the top down. But then if you. But then also like the signals from the world also go in the other direction. So there's this kind of like, it's a communication that's a two way communication, but it's not symmetric. So it's sort of, that's where the concept of the hierarchy comes in.

**[01:12:57]** Because the top tends, it tends to be. The top tends to tell the top. The high level stuff tends to tell a low level stuff what to do. But if the low level stuff says, oh wait, no, I actually hit something, then if you're nervous the high level stuff will sort of take that into account and handle things appropriately.

**[01:13:18]** Never have time. I am just going to briefly mention. So the little story we've been telling now about hierarchy and things like that is the general, again, cartoonized version of the motor hierarchy. And it tends to be played out. This tends to be how like mammalian nervous systems at least tend to be organized.

**[01:13:44]** I sort of skipped a aspect here of like muscle synergies, of sort of like, you know, like my arm, all the muscles in my arm are handled kind of like in conjunction with each other. So I'M not doing things like controlling each muscle individually. I'm not controlling each degree of freedom individually. They're handled more at this, what's called like a synergistic level. And for most mammals that's what you get.

**[01:14:09]** You get this kind of like the front, the high level stuff sort of activate these like motor planes which activate these motor hierarchies. And that's about where things tend to end, however, for a small subset of animals, specifically tool using mammals. But I again, I'm not sure where things like corvids and stuff play into this, but we have a freaky special other tract called the corticospinal tract where we have parts of the nervous system that bypass all of this other stuff and kind of go down and directly innervate the spine. So corticospinal tract, so cortex to spinal spine. And again, I think that's an area where basically by saying what I just said, I'm roughly exhausting my knowledge on the topic.

**[01:15:07]** I think it's an area of very active research in terms of which animals have a corticospinal tract, which ones and which ones don't. I think with biology it's never a case of yes or no, it's always a matter of degree. But it is again one of those places that is thought to be related to our ability to be magnificent adaptation engines where we can control our body and basically an arbitrary level of ways. And this very high level of precision and fine control is thought to be related to, in addition to things like the neocortex which is handling this tool using stuff. Also the corticospinal tract which is sort of giving like I think about things like learning like gymnastics and stuff like that, where you're doing something and then someone says oh no, no, not like that, like that.

**[01:15:58]** Like your heel is off by an inch and a half in this direction. Change the motor plan on the basis of like words that I'm saying to you. And I think like when I philosophically, poetically think about the nervous system, I think that it's that type of control that's being sort of implicated by, in things like the corticospinal tract and stuff like that. Because I just think that like, you know, comparing human movement to other types of animal movement, like one of the main questions of like what makes us different is related to our infinite adaptability relative to most other animals. It's, you know, talk a bit about that in the evolution phase of life.

**[01:16:44]** And that goes out to your limbs and does muscle stuff.

**[01:16:51]** Okay, I that's about as quick as I can ever make anything, I guess. So anyways, that's roughly speaking your nervous system, at least the motor control parts of it.

**[01:17:06]** And yeah, obviously covered a lot of ground, said a lot of things. And so for the rest of the class, I guess I'll just let you be like locally clumped. At this point, I might just have to have a whole classroom, I don't know, because there's so much I want to say to you, but I also want to give you time to explore on your own. So we'll figure that out. Probably not time for code stuff.

**[01:17:42]** This time around, I will say let's do roughly like we did last time, where we pop into a channel in the lectures area called 20, 24, 10, 15.

**[01:18:04]** Motor hierarchy.

**[01:18:08]** I don't know if I spelled hierarchy correctly, but any of this.

---

### Chunk 9 [01:18:00 - 01:20:46]

**[01:18:00]** 20, 24, 10, 15.

**[01:18:04]** Motor hierarchy.

**[01:18:08]** I don't know if I spelled hierarchy correctly, but any of this.

**[01:18:16]** There you go. Doop. Perfect. No question.

**[01:18:25]** Yeah, and just kind of do what we did last time. So pop open some chats and just ask it some questions. And what I'll specifically ask you to do this time, which I haven't done in the past, is rather. So follow your heart. So if you wanted to ask sort of more of this kind of like high level, give me the textbook version of the story, go ahead and do that.

**[01:18:49]** If you want to dive deeper into the nitty or grittier side of things, where the cartoons break down, ask the bot for keywords that you can punch into, things like PubMed or Google Scholar. And look for papers on the topic that it's questioned for. Don't ask it for specific papers. It will either give you papers that are old or it will give you papers that don't exist, slash, chat.

**[01:19:19]** And so ask it for keywords and then go search for those papers. You can ask for things like review articles, but just ask it for keywords that you can search for. And then when you find the paper, copy the entire abstract and paste the abstract into the chat and then ask it to explain that to you. Because obviously you could read the abstract and figure it out for yourself, but abstracts are necessarily and intentionally extremely dense linguistic blobs. So there's pretty much no abstract on the planet that you couldn't spend several lifetimes trying to parse out all of the details and all the words and all the unfamiliar phrases and let's do that for, Jesus Christ, 13 minutes.

**[01:20:06]** And yeah, I'll say so obviously that's not much to get into, so just. I'm not going to make it an official assignment, but continue this conversation with the bot throughout the day and throughout the week. Just like every so often, just pop open a chat and just ask it a question.

**[01:20:24]** I'm not going to necessarily make that an assignment. I'll make assignments later. But anytime you have a thought, just pull it out and ask it the question. Because I will be doing the scrape and pull stuff throughout the week and then I'll do it again before next week. So if you want to have some ability to steer what that content is, ask it questions about the things that you care about.

---
