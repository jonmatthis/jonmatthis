# Transcript: 2024-11-12-HMN24 - 06 - Intro to Eyeballs

## Source Information

- **Source Type:** Local File
- **File Path:** `C:\Users\jonma\syncthing-folders\jon-alienware-pc-synology-nas-sync\videos\video_eater_downloads\playlists\Neural Control of Real-World Human Movement (Fall 2024)\2024-11-12-HMN24 - 06 - Intro to Eyeballs\2024-11-12-HMN24 - 06 - Intro to Eyeballs.mp4`

---

**Total Duration:** 01:27:14

---

## Full Transcript

### Chunk 1 [00:00:00 - 00:09:57]

**[00:00:00]** And recording great. Hello everybody. Welcome to whatever today may bring.

**[00:00:12]** Yikes. So let's see. A lot of things, a lot of sort of technical things that nobody asked for have been partially completed. So today the topic of the day will be eyeballs. Specifically, like the basic biology, neuroscience of how your eyeballs work and connect to your brain, all that kind of stuff.

**[00:00:39]** And we're going to get to that. But that's going to be another kind of like in the spirit of the motor hierarchy thing where I have less prepared because I was making these things. But this is a topic I know a lot about. And so this is mainly going to be trying to give like a large scale overview of all of the relevant. Of as many of the relevant parts to vision as we can get to and then sort of see where that gets us.

**[00:01:09]** And then next week we'll talk about evolution and then we'll take stock from there because there's a couple other things I want to get done this semester.

**[00:01:21]** At this point in the semester, y' all are probably wondering about your grades. Don't worry about your grades. Just show up check boxes, you're fine. The concept of grading is about ordering you relative to your performance, relative to your peers. And I just don't think that's a valuable form of education.

**[00:01:39]** There's a really awful but very formative paper written in 1970 called Higher Education as a Filter. Written by Kenneth Filter? Kenneth. No, Kenneth Arrow. With the premise being that what we're supposed to do in higher ed is give you guys a chance to out compete your peers so that the purchasers of labor know which one of yous are the good ones who are worth the money.

**[00:02:02]** And fuck that in general. And that's not what I like doing in my job. I do not care about how you perform relative to each other. I don't even know what performance would mean in this context. So don't worry about it.

**[00:02:16]** Talk to the bot. As long as you have at least 1,000 words written in the server, which I'm pretty sure almost all of you already have, you're fine. Even that you'll be fine. If anyone is a problem, I'll let you know and say, hey, just check some boxes so that I don't. So I could stand up to audit, I guess, if I need to.

**[00:02:40]** As long as I don't record it and put it online anywhere. Yeah. So don't stress. Do your thing. I'm sure you have plenty of other parts of your life that are adding stress, so focus on those.

**[00:02:53]** Education doesn't have to hurt. Learning doesn't have to be a painful process if you feel doing great. Okay, where are we now? So I did a big refactor of the AI code. Refactor in the context of code and software basically means redoing it, rewriting it, changing the structure up, cleaning things out.

**[00:03:19]** It was kind of a lot of code that I wrote under duress over the past several years in various classes. So there's a very important rule that you unfortunately are also not really prepared. It's not really a part of the undergraduate education to focus on things that last for longer than a semester. And you guys are really, given this, I think, pretty awful approach to productivity, which is like, here's a short term, hard deadline, get it over the case, throw it away, start again from scratch. And if you're going to be working on something, you work on it a lot for a long time and then it will get better and better and blah, blah, blah.

**[00:03:57]** That's not really how the world tends to work. Typically things are much more iterative and you sort of work on the same thing over and over again. And when that happens, you can kind of get to this point where you're kind of like blocked by your own work. In software, they call it tech debt. Like you have a bunch of like slop that you.

**[00:04:16]** Every little sloppy decision you made along the way kind of builds up. And so it's very important to like often just like take a step back and kind of like restart. It's again a very counterintuitive thing that it like throwing all your work away and starting again from scratch is often a very productive way to live your life. Because often when you start a project, it's more discovery. And then once you kind of know what the structure is, recreating it with the end point and the starting point known can often lead to much cleaner work.

**[00:04:46]** All that is to say, I wrote the code and now it does some neat stuff.

**[00:04:53]** Well, it does the same things. It's one of the frustrating about refactoring code. It actually has very similar functionality, but now it's cleaner and you can build off of it. And one of the things I built off of it was looking per student and then some other stuff which I will show you shortly. So let's take a quick sort of path through that.

**[00:05:21]** Yeah, yeah, I'm not going to get too into the weeds on this, although I desperately want to. So, most recent server thing, same as before, Just download it here. There might be a couple extra things in the zip file but don't stress about that. And so grab that. And if you open it now in Obsidian, open folder as a vault, paste that, go there and probably actually this one.

**[00:06:04]** Yeah, select that. It's white, always white. I don't know why actually not always white. Always white on this computer when I open a new one. Well, my other computer doesn't do that dark mode, because light is effort.

**[00:06:25]** Okay. So it's quite similar to before. The main difference is I also changed the way that I do the call to OpenAI to do the AI analysis stuff. And the new way should be cleaner, it should have less slop, hard to tell numerically, but just generally should be more robust. And also now there's this server, there's this little.

**[00:06:52]** What's it called, folder called by user which is basically I went through and every chat that your ID appeared in is sort of smushed into there. I didn't really do anything beyond that. And so there's a bunch of files in there that are user id_discord user id.

**[00:07:14]** Because the other thing I did is by. So with the way that this weird world of AI text analysis works, you can kind of do the scale of the text is you can be pretty goo ball about it. Like you just make kind of a machine to analyze the text. You just throw different blobs of text into it. So up until this point the only analysis was done at the chat level.

**[00:07:40]** So at the level of those threads you were sort of doing summaries and pulling out things that look like this. But part of the refactoring was making it more generic, which is often what happens. So now it's also set up that instead of dropping in a chat, I can also drop in every blob of text in a person particular category.

**[00:08:03]** So this is actually not sure. So this is basically the summary of the text channels category, which is not a very exciting one. So every folder with a category also has a thing that says category index.

**[00:08:19]** And this is the summary of everything that happened in that category. And then you can also go into individual channels and channel index. So it's the same thing. So it's kind of this. There's this multi scale thing happening here, which I think is kind of a very general idea in a lot of the natural world where you have this kind of like.

**[00:08:38]** The term is like scale free structure where you can do the same analysis on zoomed in version of thing as well as the zoomed out version of the thing.

**[00:08:51]** And then. Yeah, and then that does sort of interesting thing to. Yeah. So and then by user, I don't even know what this is going to look like. Yeah, I don't actually.

**[00:09:04]** This person. See, it looks like this person only has one chat, but I don't trust the code enough to trust that. So if that is you and you have more, we'll probably clean that up.

**[00:09:17]** But. Yeah, so theoretically, you should be in there. So now if you look at the graph view, we again get just the white dots of nothing until we add tags. And now we get this kind of thing. And we can do as well.

**[00:09:33]** Let's see. So we can do groups, new group. And then we look for file colon, user id.

**[00:09:48]** And then we can look for file, channel, channel index,

---

### Chunk 2 [00:09:48 - 00:19:45]

**[00:09:48]** And then we can look for file channel, index, actually just do index.

**[00:10:18]** And we're getting sort of this interesting kind of structure. There's still not a ton of navigability here, largely, I think, because of just how Obsidian works. But basically, actually I can do now a search. So in the filters I do file colon user id. User is just kind of a generic term for anybody using a thing.

**[00:10:43]** In this context, user kind of means student. I'm also in there. But yeah. So now these. So the blue dots here are the chats for a given one of you.

**[00:10:58]** And I think if you just search for a user id, you'll find yourself. And I'll make better ways to navigate this, but with. Oh, come on now.

**[00:11:10]** Dang it.

**[00:11:20]** Right, so groups file user. Pink. Bright pink.

**[00:11:37]** So theoretically here, this is also a place that I wish that I had more control over, like what is visible at which point. And you know, like, I wish I could make the tags have less pole than the other ones, but that's kind of a limitation of Obsidian. But this is a text. Fade, distance, be brighter. Okay, center force.

**[00:12:21]** So this is now starting to get at like a map of y' all's actual proper interests. So if I hover over one of these pink ones, which are the students this particular person has interest in. So things like neuroscience are obviously very highly connected because everyone has been talking about neuroscience stuff. And just again, just to be clear, this sort of summary of a given person is every single chat, all the text of every chat that they have even been tangentially a part of. So if you Even just sent one message in one in like a 50 message chat, that's all in here.

**[00:13:02]** And then it runs through and says, hey, give me a title, give me an extremely short summary, give me some highlights, give me a very short summary, blah, blah, blah, blah, blah. So these are the things. So for you, these are the things that just emerge from the statistics of what you were talking to the machine about.

**[00:13:22]** And did I delete again? Damn it, that is so annoying.

**[00:13:31]** File user.

**[00:13:37]** User.

**[00:13:43]** It's fine. Apologies for any red, green, colorblind people in the room.

**[00:13:50]** So, for example, good old user 1283-090545-34595-3792 has the main tags that came out of them, which again, if your favorite thing didn't come out, if you don't think this is a good representation of, you just know that the bot's kind of dumb. It doesn't know. It can't tell if you're Excited. It can't tell if you said something and it said a bunch of stuff about something you don't care about. It can't tell that because those words are in the data.

**[00:14:27]** So this whole person, so 53792 is the last digits, has interest in neuroscience, epidemiology, public health and hallucinations. This is one of those where like that's the only epidemiology which I know isn't true because I know that y' all been talking about that. But like this person over here, you know, so they, so they, they're now. So the motor hierarchy tag is connecting these two people. And you know, so like all of these people have said enough about biomechanics that it showed up in their message or in their summary.

**[00:15:09]** It's just one motor control. So theoretically not quite yet, but this is kind of a, it's a landscape of like an interest map. So this is sort of, it's different I think like these are. Because if you're guys. Because there's in the larger scale thing in all of this, this is everything that was discussed at all.

**[00:15:30]** Like this was the total conversation and a lot of this could be cleaned up, blah, blah, blah. Here the gray dots are just any chat, but once you start looking at the statistics of the user based stuff, we start to get the things that hypothetically if you are going around and every time you're in a chat you mention epidemiology, it's going to show up here differently than it would show up in the general statistics because we're now grouping by particular factors and that particular factor is roughly one per human.

**[00:16:04]** So that's cool. So you can navigate that. And I need to make a better interface for navigating that. But it is technically there. The other thing that I did is related to this concept.

**[00:16:26]** This is the place where I'm not going to go down this rabbit hole, although I will do it later in the semester. We've talked a bit about 3D space and objects exist in 3D space and you can have XYZ data and in spatial dimensions, if you're thinking about data, if you have up to three dimensions, you can plot that spatially by just putting XYZ as length, width, height or whatever. And so if you have two data points in a three dimensional space, you can measure distances between them, which is Euclidean geometry. Not particularly exciting. Or it is exciting, but it's probably not.

**[00:17:05]** It's probably familiar. There's a strange corollary to that. In this world of AI natural language processing that relates to the concept of an embedding. And basically, in the same way that each one of those blobs of text can be attached to, can be run through that summarization scheme, you can also get the embedding of that blob of text within the very high dimensional space of the language that the language model has access to.

**[00:17:41]** I'm not going to be able to say this in any way that makes sense in the short briefly, but basically, Instead of being three dimensional things, each blob of text that an OpenAI LLM processes is embedded in a 1532 dimensional space. So1532, a given blob of text gets put into that space. And that location in that super high dimensional space has something to do with its meaning. And in that space you can also do things like measure distances and see like things that are close together are similar in meaning and things that are far or dissimilar in meaning. This is kind of how like search engines work.

**[00:18:22]** It's a little goofy, but what that means is that you can take all of the text that was generated and get these embedding vectors, which are these 1500 long numbers, do some weird math to collapse it down into three dimensions, and then look at the sort of space of conversations that we've been having within that sort of strange spatial dimension.

**[00:18:55]** So I did that. Again, this is not going to make a ton of sense. It's going to make a strange, abstract kind of sense. But we'll come back to this and I'll make it a little bit better. But basically, this strange orb, one of the many strange orbs I've shown you this semester.

**[00:19:15]** But this orb represents the, the three dimensional projection of the 1500 dimensional vectors associated with each of the chats that have happened in this class. So each one of these little markers and dots represents one chat and sort of its position and the. I think, how do I do this?

---

### Chunk 3 [00:19:30 - 00:29:29]

**[00:19:30]** Chats that have happened in this class. So each one of these little markers and dots represents one chat and sort of its position. And the. I think. How do I do this?

**[00:19:45]** I think it's color. Oh, I think each channel category pair is a unique color symbol pair. So all of the blue dots are things that happened in the general text channel. All of the purple squares are the center of mass balance channel. In the lectures category.

**[00:20:11]** You can see that they kind of lump together. So the purples are all close to each other and sort of some of the overlaps are knowable. So this. Or interpretable. I guess so this orange is from the motor hierarchy lecture.

**[00:20:26]** It's a chat about motor hierarchies and basal ganglia from the motor hierarchy lecture which shows up here by the way, in the zip file there's an HTML which will open up the sphere part of that. It won't do this part because I don't know how to. That runs from my computer. I will figure out how to share that. But if you just open that HTML, it'll just be that and it won't have this associated with it.

**[00:20:51]** But. So this is a chat in that channel about motor hierarchies and basal ganglia. This one right next door to it. I don't know what it is, but it's going to be similar ish, Huntington's disease and motor control happening in the general text channel. So there's like down here I have.

**[00:21:08]** I lost some time to it this morning. This is the sea of bot playground because I, I tried to remove it and it caused some problems. And so now there's this blob of chats that are not about the topic of the course. And you can see they're all kind of like stuffed down here in this sad little zone. So I want to remove them because that is like real estate that's not being taken care of.

**[00:21:38]** So this is the general space here is called cluster analysis. I'm looking for lumps and clusters and large unstructured data.

**[00:21:47]** And I think the next phase of this will be to try to clean up some of the technical stuff. But also now that we have. So this is just the chats, but as I just mentioned before, we also have your actual individual student, self, User self. So it would not be too hard. But I wasn't able to do it today to basically take each of your associated text gooball and calculate the vector embedding of it and then plop those markers on this sphere and then look for some distance score and say, okay, Students that are within this range of each other have similar interests that chats that are kind of.

**[00:22:38]** It'd be kind of like if I plop. Like if one of you plopped up here, then there would be this sort of group of chats that are like, hey, these things are probably relevant to you. This is basically like a recommendation system, now that I say it out loud. It's kind of how like Netflix and stuff works like that.

**[00:22:53]** But yeah, so these are also chats. I want to also plot the individual messages within the chat. Specifically like the what I've been calling couplets, which is like you say something and the bot responds. So that two message couplet would be interesting to put on here.

**[00:23:13]** This is my homework assignment of trying to figure out basically how to wrangle the very large unstructured stuff. Another thing I could definitely do, which I've mentioned before, it's like do a second pass through because right now it's processing each text blob kind of independently, where it's saying for a given blob of text, it's like extracting all these things independently. And specifically it's extracting the tags independently, which is not really ideal because it means that there's some. There's probably some synonyms happening that could have been the same tag that would lead to better structure. One second.

**[00:24:03]** But yeah, so I think if I were to go through and do the first pass, get all the tags and then run that through and say, hey, AI, condense these down into like 40 or 50 and then replace the ones that are sort of covered so that there's a total of like 50 total tags. Then this would be a much more sort of structured mess. But yeah. Is that a hand?

**[00:24:33]** What's that? So the red dots are what happens if I hit groups, new group. And in the group I type file User id, which is basically just coloring all the dots associated with files that have user ID and the name as read. And if I filter by that and I say only show those, then this is showing the red dots are the notes. Dammit, I always do that.

**[00:25:06]** It doesn't remember. And then the green ones are the tags. So the hashtag words.

**[00:25:17]** Yes, yes. So each I checked the number I didn't check. I didn't actually like connect it to your actual identities. So I don't know which one of these is which. But that is hypothetically, there's one dot per human and then there's also one dot per markdown file in this by user folder.

**[00:25:44]** And if I turn on the tags so just view the tags, those will show up as green. And so the ones that are connecting are ones that are shared. So all of these connected red dots. The AI says that when it's looking for tags associated with the words. These are all people who talked about neuroscience enough to get a neuroscience tag.

**[00:26:07]** And so yeah, again, there's just the limitations in how. There's only so much I can do with the visualization here. But the big ones are ones that are more connected and the small ones are the ones that are like. This would be called an orphan because it only has. Actually it's not an orphan, it's just.

**[00:26:26]** It's not a connected thing. Only this user has me told talked about surgery enough for that to be extracted as a tag.

**[00:26:36]** So if you're like, what does that all mean? It's like, I don't know. Working on that. This is part of the joy of discovery is. I don't know either.

**[00:26:48]** This whole thing is basically an experiment in like experimental. The term is pedagogy, which means the teaching of children. I don't like that term because it's weird. Andragogy is the teaching of adults, which I think is. When I think about it, that distinction is like.

**[00:27:02]** I think pedagogy is much more handholdy. And andragogy I think of as like, I'm going to teach you how to do stuff and then you do that stuff. So it's. Andragogy is like adults. So I don't know.

**[00:27:14]** So this is basically trial four in my continued exploration of how can we use AI to teach better and burn the world to the ground. That's later. Not out of scope for this class.

**[00:27:36]** Great. Ok. So yeah, so you can explore the Obsidian stuff. You can also theoretically open this HTML file and it will open partially that sphere.

**[00:27:57]** You are supposed to be confused at this point. There is not. If you're like, I don't know what's going on. That's correct. We are exploring and confusion is the proper state when examining anything related to the natural world.

**[00:28:13]** Okay.

**[00:28:18]** Oh, and if you're a Cody person, this. Oh, you actually may not have this.

**[00:28:31]** Never mind. The full server Data is now 180Giga or sorry, megabytes of just numbers and letters which is not currently available to you. But I wouldn't really recommend trying to dig through it anyway. It's mostly like repeated text and like those many instances of that 1500 digit number. Okay, cool.

**[00:29:00]** So eyeballs. Right? Got that.

**[00:29:08]** I realized that I actually have a. Where would you go?

**[00:29:17]** I have a video of myself wearing an eye tracker from a previous life that I can share to sort of, like, remind ourselves how.

---

### Chunk 4 [00:29:17 - 00:39:15]

**[00:29:17]** I have a video of myself wearing an eye tracker from a previous life that I can share to sort of like remind ourselves how eyeballs look.

**[00:29:34]** So I put a lot of stuff on this YouTube account, John Mathis. It probably linked in the server somewhere. It's kind of a way for me to communicate with other researchers. Like, the numbers are small but consistent. But there was a time in my life when I was making more Internet sort of public, appealing stuff.

**[00:29:56]** And one of them was this video of me playing Overwatch in my living room in Texas that got have 300,000 views. And I think it's like from a different iteration of my life where I was like, much worse at making these kind of visuals. But it is playing, I guess it's playing at full speed. So this is same basic eye tracker, slightly different visual. And I'm in my apartment in Austin, Texas, as a postdoc and I am calibrating to this.

**[00:30:34]** I have a laser pointer, so I'm just looking at that and I calibrate it after the fact. And then this is the data that I wish I had been able to show in real time last time. And it shows the X position. So the horizontal position is blue. So if I look go left to right, the blue will go up and down and the orange is Y in that direction there.

**[00:30:56]** And I'm playing a git. Playing Overwatch is a game where you shoot people with cartoons. I don't know. And I'm playing around as Roadhog. Who is a character in that game?

**[00:31:13]** Someone played Overwatch. Anyone? Please. Thank you. Great, Appreciate it.

**[00:31:19]** So video games are a really interesting, I think just like perceptual motor task because they are very visually complex, but the motor commands are quite limited and the task is often very well defined. Like you have a certain. This is a competitive game where you have people trying to shoot each other and you go out and so you have. This is where the bullets go. This is your health bar.

**[00:31:44]** And these are your abilities. And they use them and they cool down. And this particular character is like big and slow and has like a powerful thing here so you can see there's kind of like. So the task is very clear of, like, win the game, don't get shot so much that your health goes to zero, and then use the abilities to stay alive. So first of all, you're seeing a lot of this.

**[00:32:07]** I mentioned people don't blink when they're doing stuff that's hard. So all of these kind of gaps here is what's happening before the game really starts. And you can see I'm blinking all over the place. Eventually people will show up and I have to play the game and I start blinking a lot less.

**[00:32:23]** So here you have also in YouTube you can go frame by frame with period and comma, if you didn't know that.

**[00:32:34]** So you see kind of like as I'm coming around this corner here, I sort of over look through that thing. You can see the jumps down here. I guess I'm recording this at 30fps, which is unfortunate. So. So those little jumps are saccades.

**[00:32:51]** And so yeah, so you see here coming here's a big jump in X and Y at the same time, which is a diagonal. So it's going to be positive X, negative Y. So it's going to be I guess in that direction.

**[00:33:10]** Yeah, so that's. Yeah, that's. So this is the first time I look down here at the ability. So this shape is going to become more familiar because this is a diagonal down to this way.

**[00:33:27]** And then making a blink during a saccade like we do. And then this is checking the other side, which is the health bar and then back to center.

**[00:33:41]** We tend to really like our eyes to be in the middle of our head. This is our strong preference. So when we're making eye movements in the real world, there is a pattern that is a stereotype pattern of if I'm trying to redirect my body in a particular direction, my eyes will go there, then my head will go there and then my body will go there and then I'll move. So there's kind of a trade off there where you want to get the information before you initiate the action and you move the fastest moving things first.

**[00:34:11]** But this is. Yeah, then so oops, I'm shooting this guy here.

**[00:34:22]** See another one of those shapes coming up. That's going to be. Because they tend to start from the middle that actually those are positional so that. So if the two dots are here and here, that's going to be the same place every time. So this one is going to be to the same location as that one.

**[00:34:39]** And this saccade, you could, you know, 33 milliseconds per gap there.

**[00:34:47]** So because I think I had already like thrown the hook and so I'm fighting this big scary one and I have to like, am I ready? Can I do it again? So I looked down and then. Yeah, actually that's that same pattern. So it's like center to the bottom, left to the.

**[00:35:06]** Yeah. And then making these saccades here. So this four in a Row is a big jump happening. So that's 120 milliseconds and you're sort of traveling. So that's a big saccade.

**[00:35:19]** The actual image on my retina is blurring when that happens because of just the movements happening there.

**[00:35:28]** Okay, I'll let this play a little more. Here we have 1, 2, 3, 3 little saccades.

**[00:35:41]** Oh, so this is as I'm turning around the corner.

**[00:35:50]** So another thing I find. I mentioned this before. The amount of information we get in a very small amount of time is enough to change our behavior. So each of these Little Steps has four dots on it, which is again right about 150 milliseconds, which is about as fast as you can move your eyes, but enough time to get the information from that part of the visual field. And here we are blinking.

**[00:36:17]** I'm in this empty space. I'm like, there's nothing going on. I have time to blink.

**[00:36:23]** So now we have also this little curve which the curve, I'm not moving my head, so it's not vor, but I am moving the stick on the controller. So the world is moving smoothly. And I'm going to be tracking probably whatever this is as that happens. Nope, guess not.

**[00:36:46]** But yeah. So running up here, then this guy runs out. Get him, shoot him. And so this kind of stuff here, like the swoopy things, like small saccada, like small sort of rolls back, I started to associate this with. It's kind of like a vorish type of thing.

**[00:37:05]** VOR is the head stabilization one where it's sort of. It's not a big saccade, it's not even a small saccade. It's more of a tracking behavior. There is some object on the screen that I am tracking smoothly and then making these little things, little dinky saccades here. Hard to know exactly what that is, but yeah, sort of a little.

**[00:37:33]** Those are sometimes called catch up saccades in the context of smooth pursuit. Your eyes can track the thing, but sometimes they track it a bit slightly slower. So you'll periodically make little catch up saccades to sort of like, you know, I'm tracking this and as it moves over, my eye lags behind, so I'll jump ahead to get on top of it. You can kind of see that happening here as I'm again coming around this corner because I want to shoot this mean ninja.

**[00:38:04]** Here's that same pattern again, double checking. And then we don't need to watch the whole thing necessarily. But so again, so this is like, this is behavior. This is a task that I performed, a visual motor task that I performed at this point several years ago. Actually, don't even know what that was.

**[00:38:36]** 20 something that doesn't start with a 2. And the sort of the nature of the data gives us this really interesting insight into the kind of the cognitive task that was being performed. You can see this was something I had this sort of, like, vague intuition, this intention to, like, do this for different characters and sort of, like, get different patterns for each of the different sort of, like, play styles and stuff like that. And it didn't quite work out because for most of the players, you're mostly just, like, staring at the center of the screen the whole time, so you don't get the big jumps. This guy in particular, just because he has huge health pool.

---

### Chunk 5 [00:39:00 - 00:49:00]

**[00:39:00]** Like get different patterns for each of the different sort of like play styles and stuff like that. And it didn't quite work out because for most of the players you're mostly just like staring at the center of the screen the whole time. So you don't get the big jumps. This guy in particular, just because he has huge health pool and slow cooldowns, you get that really standard sort of triangle shape that I really enjoy.

**[00:39:23]** But it's this interesting thing where ability to just like point a camera at your eyes and the screen gives you this readout of the physical movements associated with the information gathering process that your visual system is made for and the specific sort of like tying in. So yeah, here I am blinking a lot is.

**[00:39:52]** This is an interesting one. Little jaggedy bits here. This is what it looked like when I was doing those big turns. This is what that looks like. Again, my head is not actually moving.

**[00:40:04]** So it's not the same behavior, but it is sort of related. I am turning in this case, but it's kind of like my eye is attaching to a particular part of the world and then sort of shifting around there.

**[00:40:19]** And so I'll let this play out because it's only a couple more minutes and I'll just talk over it. But part of the. I think, like, I like approaching the question of how vision works from this perspective of looking at it, how it's actually used in real life, or not real life, but sort of simulated real life. I was alive. I did do that.

**[00:40:44]** But in that approach is very. Sorry, it's hard not to look at it. But the concept of looking at the. I'm going to shout out my postdoctoral advisor who taught me how to use an eye tracker and also came up with the idea sort of. Her name is Mary Hayhoe and her main focus is kind of on task dynamics and how the.

**[00:41:09]** So Mary is been around for a while. I think she's in her 70s at this point, possibly late 70s. And she kind of was one of the first people to really start trying to study natural behavior. And people moving. We won, I think.

**[00:41:27]** Right. And so notice now too is like now that I'm not engaged. So Mary studied natural behavior. Still does. And when she started studying it in like 80s, she had a lot of people telling her that it's not possible.

**[00:41:43]** You cannot study natural behavior. It's too noisy, it's not controlled. The data you're going to get is going to be some messy nonsense and there's not going to be any way to interpret it because at the time still now, but doubly so. Back then, the standard mode of research was highly controlled experiments. People, people in dark rooms, head attached to a vise of some kind, fixating and doing very, very simple experiments of like, look to the left if the thing is blue, look to the right if the thing is red.

**[00:42:15]** So the idea that Mary was going to try to study people who were less constrained was met with derision, because the idea was that you're never going to be able to get anything meaningful out of data like this. Natural behavior is too complex. And so Mary's idea was to focus on the task dynamics, which is to basically, rather than focusing on the biological system on its own. Think about it in the context of what is the task that this organism is trying to actually compete, and what are the things that define success and failure on that task. And if we think about things in that context, then the data all of a sudden starts to make a lot more, more sense.

**[00:42:56]** Like, if I didn't know that the health bar was down here and the cooldowns were down here, this weird shape that keeps showing up would just be a weird shape that keeps showing up. But because I know the task, I can sort of interpret what that is. And then if we wanted to, we could sort of look at how that corresponds to different sort of this, that's. And the others and also start asking questions about, like. Like the speed at which these saccades happen can sort of like, oh, the fastest saccades are only at this 150 millisecond rate.

**[00:43:30]** It's like, oh, well, there's people doing the proper neuroscience to tell us that. But if it's moving that fast, then that means that it's more important to get information from multiple places than it is to get really good information from one place. And I wanted to show this thing at the end here. So now here that I'm actually not really engaged in a particular task, my eye movements are way more all over the place. They're far less stereotyped.

**[00:43:57]** You don't see the same shape showing up. And if you wanted to, you could definitely come up with stories about what I'm looking at. But even here, in the same exact task, same exact environment, you have to start making a bunch of different guesses about why I'm choosing to look one place versus the other. Because we always have a task. Every time you're anywhere, you have a task that you're performing.

**[00:44:22]** But if the task is not difficult and time constrained, you're not going to be able to really interpret why things.

**[00:44:33]** People like looking at faces. Then I'm looking at his hands. People like looking at faces and hands, looking at the rest of the kit and body and whatnot. And now it's kind of like looking here. And so there's a lot of research that kind of tries to interpret data like this, of just watching complicated tasks and watching videos and watching people do things.

**[00:44:55]** And this is kind of like your pupillometry stuff where people, you can get the data and you can look at it. It's the same data type, but actually interpreting it becomes much more difficult because you don't actually know the context of what people were doing.

**[00:45:15]** Okay, 2:30, 12:30. What am I trying to do in time wise? Let's try to. Yeah, okay. So task dynamics in the study of neuroscience Natural behavior.

**[00:45:27]** Mary hey, ho. All good terms to look up and.

**[00:45:34]** Yeah, so now let's look. So looking at how the. So there's kind of these two sides to the question. One is like, how is the physiological system of vision used in natural tasks? And the other is what is the actual structure of that thing?

**[00:45:52]** And how do these two sort of how does the structure of the visual system play into the usage of it in the real world and vice versa? And I think that's probably why I often tend to struggle with ordering in this class. It's like these are all chicken and egg questions. Like there is no real linear progression that I think makes sense. And I think that talking about the physiology absent of the behavior is sort of just as lost as the other way around.

**[00:46:22]** So looking.

**[00:46:29]** So let's think about eyeballs.

**[00:46:34]** Should I draw this? I'll get a picture before I draw it.

**[00:46:48]** Why are you going so slow? Oh, it's coming.

**[00:46:53]** Come on, man. Oh, wait. Yeah.

**[00:47:03]** So open images, new tab.

**[00:47:17]** So that's an eyeball. That's the side view cutout of the thing we've been looking at from the front.

**[00:47:26]** And the most important thing that you'll notice when you look at human eye tracking data is that we point our eyes at things and we move them a lot and we point the center little cross we tend to put on the thing that we care the most about.

**[00:47:41]** Where's this one? Not sure what that line is, but this line here. So this is called the fovea centralis. Your fovea is a very important part of your visual system. When you point your eyes at something, you're pointing this at that thing.

**[00:47:54]** It is a area of extremely high density of visual fovea.

**[00:48:12]** Yeah.

**[00:48:20]** So your fovea Fovea means pit, and it's basically a place where we've moved the goop out of the way so that we have a better view of the actual photoreceptors at the eye. I mentioned one point that your eyes are backwards, which is true. Rods and cones.

**[00:48:53]** So we've heard of rods and cones. These are the things that are sort of. Let me do this. Let's zoom back out.

---

### Chunk 6 [00:48:53 - 00:58:45]

**[00:48:53]** So we've heard of rods and cones. These are the things that are sort of.

**[00:48:58]** Let's zoom back out here.

**[00:49:04]** Okay, so you got your eyeball, you got your pupil, and light comes into the pupil and hits the back of your eye. And so the rods and cones are basically like. Your rods are basically little sticks. The cones are a little bit pointier, and inside of them, they have a bunch of things, but the most important one. Okay, I gotta turn this off.

**[00:49:45]** I was still running that other thing.

**[00:49:49]** So the opsins in your eye are the chemicals that actually respond to the light. And they look like the little hexagons, your standard hexagon, with, like a sort of long tail coming off of it. And you have different types of opsins that respond to different types of light. And when a photon comes and hits it, the opsin changes shape. And so one of the sections become whatever, chiral or whatever, and sort of changes shape, and it gets this kink in it.

**[00:50:30]** Actually, I think I did this backwards. I think it starts with a kink, and it straightens out when it absorbs a light. But the idea is that the energy of the photon of the light induces this change in the physical structure, the physical chemical structure of the opsin, and that changes its charge. And so that charge is what sort of becomes the neurochemical cascade that. Sorry, the cascade of neural firings that sort of leads to your perception of light.

**[00:51:03]** This is a weird process. There's many options. There's sort of. You have short, medium, and long cones that correspond roughly to red, blue, and green. Your rods don't have the three colors, but they only respond to green.

**[00:51:21]** And it's. Your night vision is your rods, and there's a purkinje shift that happens when they're trading off from each other. It's a whole thing.

**[00:51:30]** But so basically, it's the lumpy part of the rods and the cones that actually house those opsins in this sort of peaky part here. And so you might, if you were reasonable person, assume that we would want to point that part, the photosensitive part, towards where the light comes from. But that is not actually how our eyes are set up. The photoreceptors are actually pointing back, and then the wiring that comes off of it goes back out through. And so when the light is coming in, it has to pass through the axons of the neurons attached to the rods and cones before it can actually be absorbed by the actual opsins in your eye.

**[00:52:33]** And so that is why the fovea. So basically, every Part of your visual system is worse than it could be because the light that you were trying to focus has to pass through all of these neural bodies, the sort of the. These middle layers that have ganglion cells, stuff like that. There's a whole, whole lot going on there. The light has to pass through that before it can get to the actual photosensitive area.

**[00:53:06]** And so the fovea, we push that goop to the side so that there's an unobstructed path that the light can get through. The idea of why this stuff is that way is thought to be related to when we crawled out of the ocean and our eyes kind of had to. We had to carry some water along with us so we could focus the light better. And something in that process inverted things. I don't really understand that.

**[00:53:29]** But cephalopods, like squids and octopuses and cuttlefish, their eyes face. It's faced the right way. Like their photoreceptors face towards the source of light.

**[00:53:44]** There's another sort of troubling aspect of this, which is that if all of the wiring coming off of the back of your photoreceptors sort of goes back onto the top of your retina, the thing on the back with the photoreceptors is called the retina. At some point, it has to punch back through in order to become the optic nerve. That actually takes the data, the neural. The call it data, who cares? The pattern of neural activity associated with the light in the environment has to punch back through your retina in order to get back to the rest of your nervous system.

**[00:54:21]** So that means that there is a blind spot on your retina where you don't actually have vision and you can find it. So if you close your left eye and then look at your.

**[00:54:36]** So close your left. So right eye open, look at your thumb at arm's length. And then with your other hand, with your thumb up, put it like this. And then move your thumb to where your knuckle is and maintain your fixation on that thumb. So watch me.

**[00:54:55]** So I'm looking at the thumb, and I never stop looking at the thumb. I line up my thumb here and then I move my thumb to where my knuckle was. And if you do it right, your thumb will disappear.

**[00:55:13]** Yeah, it takes a little practice, but for me. So if I'm looking at this thumb and my thumb is not visible to me right here, it's just an empty block in space. So that's another way to do it. Just hold your thumbs together so look at. Pick the left one.

**[00:55:30]** So with your right eye, focus on this one and then slowly move the other one out while maintaining fixation on that thumb and it should disappear. Anyone getting it? Yeah, it just sort of like evaporates. It's hard to maintain fixation on the thing without looking over. And also your brain fills in the gap, so you kind of have to notice that it isn't there.

**[00:55:58]** When you're done here, just look up like a blind spot demo. And there's some other stuff that it will show you there, but it's sort of one of these main. It's like a classic thing to show of this blind spot where you don't get visual information, but you get information from all around it. But because we have two blind spots and they're not over the same area, we can fill in the gaps. There's interesting research on if you give people patterns in the blind spot, how will the brain fill in the pattern?

**[00:56:29]** Because it tends to.

**[00:56:40]** So here's just another example of that. So this chunky bit right here is your optic nerve. And that's the part that goes from your. That takes. So you're.

**[00:56:55]** When you're looking at stuff, you're looking at it with your fovea.

**[00:56:59]** Peripheral. Peripheral vision. Wikipedia. I'm looking for a particular image here.

**[00:57:15]** This is roughly speaking your field of view. For I think this is per eye.

**[00:57:25]** And this central zone right here, it's actually not going to be visible here. So this is 30, 20, 10, probably 5. So probably right around this circle here. That's roughly speaking your fovea. You also have your foveola, which is like a smaller area within that space and then sort of other zones from there.

**[00:57:44]** So we have pretty wide vision. I mean, I can see my hands out to here and if I wiggle my fingers. You can. It's like interesting games you can play with yourself. Just kind of like move your hands until you can't see them and then wiggle your fingers and then you can see them.

**[00:57:59]** Because we are more sensitive to motion in the periphery. And also notice that this is not a circle. It's not a ISO. Like the central part is circular, but the whole field of view is laterally oriented. Because we live in a world that tends to be laterally oriented.

**[00:58:17]** And so our sensitivity is sort of. It's not arranged in a sort of circle around our fovea. It is horizontally distributed. We are also vision oriented predators. So we have a different field of view than if we were rodents or equines like goats have the rectangular eyes.

**[00:58:37]** Mice have the eyes that point out to the side. All these cases of the ecology of how the animal uses.

---

### Chunk 7 [00:58:30 - 01:08:30]

**[00:58:30]** So we have a different field of view than if we were rodents or equines like goats have the rectangular eyes, mice have the eyes that point out to the side. All these cases of the ecology of how the animal uses vision in its ecological niche shapes the way that the information that the visual system is set up. And as I said before, I'm not sure if I said it today, but bears repeating, that fovea is again roughly the size of your thumbnail. At arm's length, it takes up roughly 1% of your visual field. Roughly 50% of your visual cortex is devoted to processing the information from that small spot there.

**[00:59:12]** So that concept is called cortical magnification. And it's kind of why I feel somewhat comfortable with these representations that as I've said, this circle is roughly the size of the fovea plus or minus one visual degree. And I think representations like this overemphasize that foveal perspective because we are getting information from the whole thing, from the whole field of view. But it is nonetheless, I think it's valuable to look at the location of that sort of directed visual focus because that is basically an indication of this is the part of the visual field that my nervous system wanted information from at this time. I think that concept is very important because it's like I could have looked anywhere, but I have to look somewhere.

**[01:00:08]** And so my cognitive system sort of makes these little decisions about where the information. Like where in the world do I want to pull information from?

**[01:00:19]** And if I'm just sitting around doing not so much. Those decisions are not particularly costly. But as the task becomes more hard and as you start doing more and more complex and difficult behavior, the choices of where to look one place versus the other can be is very critical. This briefly, we're doing on time. I won't show this.

**[01:00:46]** I'll come back to it later in the semester. When we look back at the. My main research from this era was visual control of foot placement and looking at the patterns of scan path on the ground. When you're choosing footholds, walking over rough terrain in that kind of context, you only have about 400 milliseconds per step. And you have to find a location on very rough terrain that you can support your whole body or you'll fall into a river and break your leg.

**[01:01:12]** So that the niceness that there is a aspect where you can get basically a readout of that cognitive question of where in the environment do I want information from? Because we are highly foveated eye focused predators we have this nice feature where we can point a camera at the eyeballs, do some old school computer vision to get the pupil center here and then get a measure both of where the eyes are pointing. Not, not only where the eyes are pointing, but where in the environment did my central nervous system want to get information about to complete whatever task it is? I'm.

**[01:02:00]** Yeah. So I don't think I can draw fast enough for this.

**[01:02:11]** The Internet has already drawn all the pictures I could care about.

**[01:02:17]** Optic chiasm.

**[01:02:21]** Stop it with the AI.

**[01:02:25]** So, so you got your eyeballs and you got the optic nerves that come in, and there's this part in the middle here where things kind of split apart. And that is called the optic chiasm. It is optic chiasm.

**[01:02:52]** Ibn Haith.

**[01:03:00]** So Ibn Al Haitham was an Islamic scholar in 7th century Iraq and he discovered optic chiasm by doing just old school physiology. So Ibn Al Haytham has been called the father of optics. He basically invented optics. He is credited as the person who discovered optics, that light was a thing that you can like measure and do science about, like refraction and stuff like that. And it was later.

**[01:03:28]** His work was later rediscovered by good old Descartes and translate one of Descartes. So Descartes of Cartesian coordinates fame. One of his main things was he was a polyglot, he spoke a ton of languages. And so a lot of his claim to fame was that he would find these old records written in Arabic and translate them into Latin. And then once it's Latin, all the Europeans are like, wow, Descartes, you're so smart.

**[01:03:58]** So this is the model of the eye you can sort of see. It's got vitreous humor, cornea. This was the. So the lens. So Ibn Al Haitham got everything basically right, but he didn't understand how the lens worked.

**[01:04:19]** So he just had some comment in this thing that there's probably some demon that lives in there and bends the light. Because back in the day when you didn't know how something worked, you just said the little demon does that part. Like the rest of it I can do math about. But that part there's some demon doing stuff, but you can see kind of all these parts and then these.

**[01:04:39]** What's it called? These are like the muscles and stuff like that.

**[01:04:45]** And. Yeah, and he's on money in Iraq. Good for him.

**[01:04:53]** Ibn Al Haitham is his Arabic name. You'll often see Alhazen is for some reason the English term.

**[01:05:03]** But yeah, so this is a good representation. So showing how things split. And so there's this distinction between your visual fields and how they map to different parts of your brain. So this part I will draw because I think it's helpful, but because we tend to think of as, like. Because we have a right eye and a left eye.

**[01:05:32]** Right. Shocking.

**[01:05:52]** Okay, so that's one eye, that's the other eye. Oops.

**[01:06:03]** And this is our brain as seen from above.

**[01:06:14]** So you have left hemisphere, right hemisphere. I don't know why this is. My tech stack is struggling.

**[01:06:26]** And so there's lateralization in the brain. So your right hand is controlled by your left hemisphere for some reason. And so sort of a naive view might be to think that it's just like the same for your eyes. Like, your left eye connects to your right hemisphere, but it is not actually how that works, because your left hemisphere, so your visual cortex is here in the back, and your left hemisphere handles the right visual field, not the right eye. So if I want to know about the things that are over here, I don't necessarily want to know about what's going on in this eye.

**[01:07:16]** But as they project, let's pretend I move my eyes, they're going to project on. So from the right side, it's going to project onto the left side of each eyeball. And so we need. So this is the right. I'm super dyslexic, so this is hard.

**[01:07:37]** So the right. The projections from the right visual field need to make it to the left visual cortex. So these ones can go straight back, and these ones have to cross over.

**[01:07:55]** And so then if you want to know about stuff going on from the left visual field. So I got to figure out how this stupid thing works. Come on.

**[01:08:12]** So this is. So this is an object in my left visual field, and that's projecting onto the right side of each eye. So that is the left has to get to the right hemisphere. So these ones can go straight back and this one can cross over, and that's this.

---

### Chunk 8 [01:08:15 - 01:18:15]

**[01:08:15]** Left visual field and that's projecting onto the right side of each eye. So that is the left has to get to the right hemisphere. So these ones can go straight back and this one can cross over. And that's this crossing over point there. That's called, that's the optic chiasm.

**[01:08:39]** The chiasm is actually the crossing part. But the. Yeah, so this is the, this is how those literal wiring, like literal, like IMN Al Haitham back in the 7th century was just cutting open heads and looking at where the optic nerve is. Like a tough thing. Like if you ever find yourself in a butcher shop or a pig roast and you feel like being like weird and gross, you can go check it out.

**[01:09:06]** But it's a very fibrous and dense thing. So if you just like open up the head and just see where it goes, you can see that it splits apart and then crosses over. And then these little guys right here are the thalamus.

**[01:09:21]** I think that is the thalamus which is kind of like a way station. All your senses go through the thalamus except for smell, because smell is chemo sensation, sensation of chemicals in the environment. The story is that that is the oldest sense sense that bacteria have, smell because they're detecting chemical gradients. And so that is the only one that doesn't go through the whatever the thalamus stuff. But anyways it goes through here.

**[01:09:48]** There's weird stuff that happens here, like motion sensitivity stuff can happen there. The whole thing of you're more sensitive to this or that. There's also some tracks that sort of. Now so these ones are going back to the visual cortex proper, which is the thing that lives on the back of your brain. And then this is where you also get.

**[01:10:07]** Actually some of these tracks don't go to your cortex. I don't think some of them don't even go to the thalamus. Some of them go like straight into the spine and straight into like they bypass cortex and give you things like the startle response that happen where visual information makes you move and do like, ah, stuff like that. A lot of like balance stuff has subcortical pathways that bypass the brain and just go straight down to the spine. Oh, this is a good image.

**[01:10:39]** This is what I was looking for.

**[01:10:43]** Oh, lateral geniculate body. My bad.

**[01:10:48]** But yeah, so this is, this is what you will generally see as the visual path. But there are subcortical pathways that bypass all of the big pink wrinkly bed on top. Oh yeah. You also have a blind spot because you have A nose. There's just a part of your visual field that just like never really has anything going on.

**[01:11:13]** So that's kind of, I find funny.

**[01:11:18]** Doo, doo, doo. Yeah.

**[01:11:22]** Subcortical pathways are interesting.

**[01:11:28]** And what else did I want to show here? Kind of trying to checkbox some things here just because the main thing to sort of remember here is this concept of visual field kind of quadrants sort of, or not quite as necessary, but just the idea that the retina and the visual fields have kind of a complicated relationship that is sort of. There are a lot of mirroring that happens where you see the picture of. Now the tree is upside down because of how lenses work. So you can see the lower visual field here is on the top down there.

**[01:12:08]** So there's this sort of spatial correspondence between. There's a bunch of different angles going on here. One is the anatomical structure of the eye itself. The other is like the visual field relative to your body, I guess. So like if I'm sitting here moving my eyes around, like my visual field kind of moves with my eyes, but my visual environment does not.

**[01:12:33]** So there's sort of complicated playoff there. And that structure is kind of maintained as it gets back into. Back through the good old fashioned just physics and optics and into the weird goopy electric meatloaf. That spatial structure of the visual environment is sort of maintained in these kind of weird like splits apart and stuff like that. So that by the time you get Back to the V1.

**[01:13:00]** Visual Cortex.

**[01:13:08]** Visual cortex.

**[01:13:12]** What was I gonna look for? Cortical expansion.

**[01:13:33]** What am I looking for here?

**[01:13:46]** Why am I not finding this picture?

**[01:13:59]** I feel like I'm being let down by people who put pictures from neuroscience books on.

**[01:14:22]** What am I missing here?

**[01:14:36]** I feel like, why am I not being able to find this retinotopic. That's retinotopy. That's the term I was looking for. Sorry, Retinotopy. That's the term I was looking for and not able to find.

**[01:15:11]** So the main concept to about think about here is that there is a retinotopic map, kind of similar to the cartoon of the motor. The sensory motor Homunculus, the horrible guy that lives in your motor cortex who has giant hands and giant mouth. Because that's where we have our most sensitivity in terms of sensation and movement. There is also a kind of map in your visual cortex that corresponds to your visual field. And they're sort of the cartoons that we draw about it look a lot like this and similar to the horrible man that lives in your head.

**[01:15:47]** Horrible person. That lives in your head and sort of is the sort of the cartoon monster that represents your sensory motor sensitivities. This is also not. It's like, we love this story. It's a great story.

**[01:16:01]** It's in every textbook. And it's true to a certain extent that. But the data looks more goopy than that. It's not this perfect, beautiful map. It's more of this type of thing was.

**[01:16:17]** I know this person. And so if you.

**[01:16:22]** So this representation of the brain, by the way, the black spots are the pits, and then the white spots are the tops. So if you basically take the brain and expand it out, that's what this represents. And so this is stimulating in the visual field. And having this. Not particular.

**[01:16:41]** Not my favorite color map. You can see that there is kind of a striation that happens there. Where there is that. Different parts tend to correspond to different parts of the visual field.

**[01:16:54]** But it is complicated.

**[01:17:03]** This is a very famous image. I think it may have won a Nobel Prize. I'm not quite sure. But this is showing the superior colliculus of a monkey. And they.

**[01:17:15]** Yeah, retinotopic organization.

**[01:17:21]** And what they did is they were stimulating in the monkeys. So superior colliculus handles eye movements. And they stimulated, like, little electrical signals to the cortex and generated eye movements that sort of mapped that pattern. So also, in the same way that there's, like, both the sensory cortex and the motor cortex and they're kind of paired to each other, the visual perception system and the ocular motor movement system are also kind of paired through these retinotopic maps. Because if I have.

**[01:17:57]** If I'm looking here and there's something in the periphery that I want to see, this retinotopic location, sort of I'm fixating here, but there's some bright little shiny thing that shows up in the upper right that is also the coordinates that I need to know to make an eye movement, to fixate on that thing. So there's this.

---

### Chunk 9 [01:18:00 - 01:27:14]

**[01:18:00]** I want to see this retinotopic location sort of. I'm fixating here, but there's some bright little shiny thing that shows up in the upper right that is also the coordinates that I need to know to make an eye movement to fixate on that thing. So there's a linked map I've been talking about V1, which is. That's the stuff in the back of the brain. That's your perceptual system.

**[01:18:24]** That is not your oculomotor system. The oculomotor system is more spread out and weird. We're going to talk more about that during next class. We talk about, we're going to briefly talk about it in the evolution chat. Here's a nice sort of different animals have different sort of shaped visual fields and stuff like that.

**[01:18:48]** But yeah, so, so, yeah, so there's kind of a general, sort of like a complicated relationship between the physiology of the eye in terms of the optical characteristics of how the light bends and all that kind of stuff. The physiology of the retina, which is the part of your visual, the part of your eye that actually responds to. That's the part where you have neurons in your eye. There's an argument that your eyeball should be considered a part of your central nervous system because even though we think of them as kind of peripheral, they do computation on the retinal ganglia cells.

**[01:19:51]** So there is processing that happens in these, the middle layer. So if you want to know, that's the term there. So in the retina you have the photoreceptors, you have the optic nerve and then you have these middle layers. So there's something like 60 some odd different cells, cell types in the middle layers. Some of them are connecting the photoreceptors to the optic nerve bodies, some of them are connecting to each other.

**[01:20:21]** Some of them have long, short, middle term distances. Recently was discovered that some of these middle layer cells are sensitive to light, specifically blue light. And they're thought to be related to our circadian rhythms. But there's. Yeah, and then retinal ganglion cells.

**[01:20:43]** Retinal ganglion. Ganglion cells.

**[01:20:57]** Yeah, so horizontal cells which connect them to each other. And so there is like processing that happens on here. And it has to do with a number of different sort of like. It's a little mysterious about what all is actually happening in there. But it leads to a lot of famous illusions, Herman grid illusions, which for some of you all with Mac computers will have this directly available.

**[01:21:24]** So stuff like this, which you may have Seen before. Open image in etab.

**[01:21:34]** So each one of these circles is white, but as you are looking at one of them, the periphery will be dark. Hermann grid famous illusion. That illusion is happening at the level of your retina because of lateral inhibition. And sort of in the periphery, the black of the square kind of overlaps with the white. So there's suppression that happens, but only in the periphery.

**[01:21:57]** Because when you're fixating on it, your fovea is small enough to have enough resolution there, but bunch of weird little illusions happening there. So yeah, 110.

**[01:22:15]** I think I'll probably leave that brain dump there. That's probably enough to chew on and enough sort of relevant terms there. So you got the task dynamics thing in terms of the actual usage. You have the physiology of the eye. You have this concept of lateralization and the optic chiasm and the retinotopic mapping between your visual fields and your visual cortex.

**[01:22:47]** Got the middle layers going on in the strange cacophony of your retina. You have the blind spot, you have all the neurons there.

**[01:22:59]** And. Yeah, and you have the oculomotor system. And in particular, if you want to know more about that superior colliculus which handles the oculom. Oculomotor retino toppy.

**[01:23:27]** Yes.

**[01:23:29]** And so like that relationship between the retinotopic aspects of your perceptual system and then the retinotopic aspects of your oculomotor system and sort of how those things play together.

**[01:23:41]** And none of that has anything to do with movement. I guess eye movements have stuff to do with movement. And oftentimes people will talk about eye movements as body movements, and they technically are. But the question of sort of how this information actually makes it into your body and actually allows.

**[01:24:01]** How does the information get from your visual system down to whatever system is handling throws and catches and stuff like that.

**[01:24:12]** We can. It has to do with your parietal lobe, probably parietal cortex also has to do with a bunch of subcortical pathways and also your. The corticospinal tract, which I realized I said wrong about that. I said like only humans have it. It's not true.

**[01:24:28]** A lot of animals have it. It's just that we have. It's a greater or lesser extent. So like quadrupeds in particular, like cats and dogs have a very minimal one. And more complex.

**[01:24:41]** Not complex, but animals that use their forelimbs more tend to have more. And something I was going to say there. And it has to do with sensation. It's apparently a direct mapping from your motor cortex corticospinal tract. So it's a direct mapping from your motor cortex down to your spine.

**[01:25:01]** So you have a very short synaptic loop between the sensory information that you get from your body and your motor commands to sort of respond quickly to things that don't have to route all the way through the weird, complex wetware because that's a very slow route. Like things that go through the cortex take about 200ish milliseconds to really like get all the way through. And this is that. This is the visual representation of how that thing mentioned before. Okay, all right, I'm going to stop there and let's do what has now become somewhat stereotyped behavior of 2024 11.

**[01:25:47]** No, not dash 1105. Visual neuroscience. And yeah, in the 10 minutes we have left, please just do the thing we've been doing of just pop in there and just ask the bot about the stuff that I've been saying. I said a lot of stuff on a lot of different, many different layers of sort of clarity.

**[01:26:16]** But you can kind of see how this game is going now. It's. This is less about trying to get specific, high quality text written in there and more an opportunity for me to filter the stuff that I've been saying through your individual nervous system so I can get a sense of where people's interests are. Also, as we have learned, it tends to gum up when it gets slammed like this. So just give it a second to catch up and let's do that for 10 minutes.

**[01:26:48]** I've noticed that some of you all are not all the chats come from class time, which I appreciate. So feel free to go and dump data into the machine as much as you can. And I think by the end of the semester we're getting some good structures out. Okay, cool.

---
