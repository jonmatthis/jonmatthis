# Transcript: 2024-10-29-HMN24 - 05 - Intro to Eye Tracking

## Source Information

- **Source Type:** Local File
- **File Path:** `C:\Users\jonma\syncthing-folders\jon-alienware-pc-synology-nas-sync\videos\video_eater_downloads\playlists\Neural Control of Real-World Human Movement (Fall 2024)\2024-10-29-HMN24 - 05 - Intro to Eye Tracking\2024-10-29-HMN24 - 05 - Intro to Eye Tracking.mp4`

---

**Total Duration:** 01:00:12

---

## Full Transcript

### Chunk 1 [00:00:00 - 00:10:00]

**[00:00:00]** Okay, hello everybody and welcome to Tuesday or whatever.

**[00:00:09]** So today we're gonna do something I guess not that different but with a different piece of equipment. This is an eye tracker. So I'm gonna put it on my face and show you my eyeballs like super close up. And the goal, every time I've come up here I've tried to give a short lecture and then end up talking for a long time and leaving no time at the end. So this time I'm not going to give much of any lecture at all.

**[00:00:37]** I'm going to talk while I'm wearing it, which will take its own time and just give a technical preview. Eye tracking this type of data takes longer to process than the free mocap stuff which I designed intentionally to be easy to sort of pop out cool things in a hurry. So the idea will be several fold. One will be to like just get some data on the machine and then I and Aaron and whatnot can process it within the next week. And then on next Tuesday we can talk about the data and at that time I will say more about ocular physiology and the, you know, visual, visual aspects of your nervous system and things like that.

**[00:01:24]** And so the kind of, it's sort of again in this kind of like flip floppy kind of structure where we're going to start by jumping in the deep end and you're going to watch and you're going to have just all sorts of questions about like what am I doing? What's that thing I said and didn't mention again? And then also just like your own personalized interests in this topic as a whole. And after I get done with that, hopefully on the relatively early side of things, we going to, we're going to do that sort of split off into individualized groups and have just like, kind of just like a couple moments just to sort of like drop some questions into the lecture thing about like, yeah, I'll just do it like that about like the questions that did come up for you and like the things that you want to know more about. And then that will give me the opportunity to scrape that stuff and see it before I actually plan for what I'm going to talk about next week.

**[00:02:28]** We're not going to spend the entire second half of the class doing that, which is why I'm sort of pausing because splitting time is always hard. But I think it's fine if it's sort of like a soft transition. But I will ask you kind of like to put some chats into the relevant lecture, chat about vision and Eye tracking and eye movements and stuff like that specifically. And then sort of I guess like smoothly transitioning from there into a conversation more aligned with the AI scrapey stuff that I have been sort of showing you in various forms. And with now there is sort of.

**[00:03:06]** I did a little bit of extra polishing, but mostly I kind of just like realized that in Obsidian, when you're viewing the sort of scraped data, you can just search for your own member ID on discord and then see all the stuff that you have been talking about and get like a mini little graph. And so that will kind of be your first opportunity to see your own extracted data. And I will sort of ask you kind of take a look at that. Think about what, like how much that actually represents your interests, how much you sort of like thinking about how you might dump other information in there to make it more aligned with your interest. And then specifically kind of like comparing notes with just your local vicinity and specifically trying to find overlap between the topics that you've been discussing.

**[00:03:56]** Sort of like, oh yeah, we're both vaguely interested in this general thing. Or actually even better, there's this kind of empty space between the things that we have been talking about that could sort of link our particular nodes together. So in the spirit of that, I'm going to just quickly show you how to open the data again. So you'll need Obsidian on your computer and then a way to open seven Z files, which I'm actually not sure what is and is not built in these days, but 7zip is the software that we tend to use. I prefer zip files because they're more generally compatible.

**[00:04:35]** But I did this on my Windows partition, so zip files don't work because of that dumb historical limit on path links. So here we are in the server. I changed the picture so you have to scan for it differently. Up here under Resources, there's a thing at the bottom called server scrape. Checkpoints.

**[00:04:57]** Checkpoints and software world and specific like machine learning AI stuff generally means like this is a thing that we're going to keep doing, but this is like a time dated checkpoint. So that's sort of just the terminology there. And so click into that scroll down to the bottom. This is more notes for myself, just so like I can keep track of like, you know, be interesting to see. Like oh yeah, look, a bunch of stuff popped up on this topic because of this lecture, blah, blah, blah.

**[00:05:25]** So click the download thing. It'll download probably into your downloads folder. It will be 7Z.

**[00:05:35]** You might be able to just double click it and it will figure it out. You might have to right click it on a Windows machine on Mac, I guess like double tap click it, go to 7zip and then do extract here, something like that. If you don't have that option, just Google 7 zip. If that doesn't work, open up a chat in the general chat and just ask the bot like how do I open a 7z file on a Mac or whatever kind of computer you have and it will help you. And if you can't figure it out, don't stress, someone will ask a neighbor or just chill and I'll show you later.

**[00:06:16]** Do do do do. So once you have it on your computer and you've extracted it into a regular old folder, it will, the folder will look something like this. I cleaned up some of the pathing like I don't know if you recall, like there used to be like a bunch of like sub paths and stuff like that. And I also there's no raw data in here. It's just the AI processed stuff.

**[00:06:40]** If you don't, you don't remember what that is, does not matter. But you're going to need to know this path. If you're not familiar. I'm sure I've said this before, but bears repeating. Files on your computer are arranged hierarchically.

**[00:06:54]** There's a tree structure where everything is and that sort of C the first one is the specific physical drive and then there's these sort of like slashes that sort of tell you which branch of the tree you're going down. So this thing is called a path. That's sometimes also called a directory or a folder or something like that. And it's just branching to tell you how to get to the particular data blob that we call files. And so in this case I have to go all the way down here.

**[00:07:21]** This thing is called a file MD means it's markdown and its path location address, full pathname is all of these words plus the file name plus the extension at the end. The extension at the end is just sort of a clue for your computer about how the data is going to be structured inside of it. So if the computer tries to open it, it's like oh, it's a md. I know how to handle those md. I could just as these have written txt and that would be raw text and that's about as deep as I feel I need to go down that rabbit hole.

**[00:07:56]** Okay, so in Obsidian, so last time if you followed along you probably opened you did something similar to manage Vault. So I Clicked down here to manage vaults. Probably could have done control N or something like that. Actually, probably not. Doesn't matter.

**[00:08:15]** And we did the open folder as vault and then you opened the last one just to make things easier. Just make a new one to say open folder as vault. Like you could, like you can see like this one is already kind of preloaded with the last one I was looking at. But this is. This is like.

**[00:08:37]** Oh yeah. And it's actually telling me where I was. But this is one of those cases where you can tell that we're not using the tool for its intended purpose because it's not behaving in a way that would be sort of compatible. So that. Because there isn't like an easy way.

**[00:08:53]** Actually there is an easy way, but I'm not going to do it to tell it. Like just update the one that exists with all these ones. Like find the parts that overlap and keep those and add new stuff. I could probably just. Yeah, but it's fine.

**[00:09:09]** So here we are here. Human movement neuroscience fall 24 checkpoint 241022 which is today 639 when I ran it and then AI process. So it's not the raw. Select the folder and for some reason it pops back to light mode.

**[00:09:35]** Indexing complete pops up. Which is kind of interesting for deep reasons which I won't get into.

**[00:09:42]** Here we are again. And once again these top level folders.

**[00:09:49]** Again Obsidian calls vaults folders, just the same sort of branding for them. And you can more easily see kind of like the tree like hierarchy in this.

---

### Chunk 2 [00:09:45 - 00:19:44]

**[00:09:45]** These top level folders again, Obsidian calls vaults folders. Just the same sort of branding for them. And you can more easily see kind of like the tree like hierarchy in this format. Macs kind of have this drop down menu thing in their file system, which is nice. Windows does not.

**[00:10:05]** And then they don't give you the extension here because it's in a software for operating under markdown files. So it doesn't show that by default.

**[00:10:15]** So the code and AI that I. The AI prompting that I use to generate this is almost exactly the same except that I added a little bit of stuff to turn these tags also into backlinks which will. If I click on this, we'll go. Actually I'm not sure what it looks. Oh, it might want double.

**[00:10:35]** Does it want double?

**[00:10:38]** Oops, yeah, it did want double square brackets. So it's fine.

**[00:10:49]** And if you remember last time I think I talked about this, the tags it had were sort of like too disparate. Like it was sort of like they would make one tag for like virtual reality and another tag for like virtual reality questions or something like that. Because it's processing each chat the unit, it's operating under the chat, so it's cycling through each chat object. So I just added a little bit of extra instructions on there that said tags should be one to two words and don't separate them out into things like that. With this type of AI programming prompting often just giving better instructions gives better results.

**[00:11:31]** Kind of like how humans work.

**[00:11:35]** And so if I click on this little graph structure over here, graph looking icon and it pops this out. If I recall correctly, I think There were like 222chats total from y', all, which is nice. I did also now actually this does not include the bot playground chats. So that has now officially been. Even though I thought it was really funny when that they showed up, you can see that none of them are linked together because none of the backlinks because we're not showing tags yet, we're just showing the backlinks.

**[00:12:08]** And the only actual link that we show is this one around here, which is the one that I clicked on as a demo. So it. I think yeah, so it was that one. And then it's trying to click into that one, which is an empty thing. So there's that.

**[00:12:22]** So click on that. And then this is of course the fun part where we say so on this thing in the upper right we do dropdown for filters and then we tell it to show us tags. And these are the tags. So I Don't have like direct data to compare like the last time versus this time. But just like eyeball wise it looks better like you have fewer of these like orphan spots over here and things are just generally more connected.

**[00:12:57]** Neuromechanics. Yeah, so like neuromechanics was a popular thing to talk about, I think just because the name is so cool. So theoretically if I click on this, this will show every chat that has had that the bot has extracted the tag neuromechanics from.

**[00:13:19]** And now if you want to start looking at your space within that, I think you might. So you might have to go into user settings and do developer mode. Come on buddy, Advanced and turn on developer mode, which I think is not on by default. And then right click on your name or double click on your name and go down to copy user id. I think if that doesn't show up, then you have to go turn on advanced mode.

**[00:13:55]** So click on that. It's now in your clipboard, which is just like a thing your computer keeps track of for you. Go into here and I can search for filters or in the filters box I could do specific looking for a different. So I could look for a given path. So I could say, hey, only give me stuff from the path that includes the chats from whatever category or whatever channel and that would filter at that sort of tree level.

**[00:14:24]** I could search by tag and then I think the one that's actually coming up is by line or just, I don't know, just raw paste. So your ID is going to be a big number like that. That seems wrong, I think, because I haven't, I got myself and I haven't really been in here. So let's see which unfortunate soul Catherine has been discussing these things. And this is.

**[00:14:59]** So there's nothing that's happening here where the you're supposed like, it's like you're playing like video games or complicated things and it starts out simple and then gets complicated and so that by the time it's complicated, you're sort of acclimated to it. This is what your graph stuff is supposed to look like when you start and you start adding notes. So old Catherine has had 1, 2, 3, 4, 5 chats, which 222 by 40 is like pretty much smack dab on average. So good job there, minus any bot playground stuff. I'm not sure why there's no tags showing up here, which could just be a problem.

**[00:15:45]** I'm not sure why the tags aren't showing up here. Maybe it's because it's stupid.

**[00:15:52]** Anyways, so I can also go down into the second one called groups. I cannot search for two at once for whatever reason because it's actually just. There's nothing really explicitly tagging it to you. Except that when I made the code to actually put the raw conversations out, it happens to show the user id, which is like.

**[00:16:17]** I don't know if that would technically count as identifying information, but it's certainly not useful for most humans. And then this one is the bot, so every chat will have this one in it.

**[00:16:30]** So yeah, luckily I happened to put that tag in there. So you can just like manually search for stuff. Search for stuff? Yeah, for folks. So that's a good way to see like your own stuff, just to kind of like get a sense of what that, that landscape that you are making of interested topics is and looks like.

**[00:16:53]** But to compare it against your friends and neighbors, that's not going to be super helpful just for user interface purposes. So in the second tab down here we can do groups and then I can assign a color to Catherine's chats and then do that and then see them within the larger space and I can add a new group and I can look at Karina, put them yellow and kind of blends in with the green. So let's turn off the tags and then actually that doesn't really help anymore anyway.

**[00:17:47]** So yeah, so yellow is a bad color for this case. So let's do like, I don't know, blue and then.

**[00:18:03]** Yeah, so then this will be a case where you could start looking for stuff. And this is one of those, like many cases. This is one of those things where there's an automated way to do this that's kind of hard to do. There's also like a dumb, dumb human way that you just kind of like look at it and click on stuff, which is easier to do but harder to do on scale. So this is kind of a way to look at things in that way.

**[00:18:27]** Okay, so we'll get back into that. But that's just sort of try to get to roughly this point while I'm talking. So that way when the actual second half kicks in, only people who are having trouble with this need instruction. Ok. Questions?

**[00:18:47]** Probably. Yeah, great, cool. We'll come back to it.

**[00:18:54]** Okay, so eye trackers. This is an eye tracker. Well, this is a box, but it has an eye tracker in it.

**[00:19:04]** So several lectures ago now we did the thing where I set up cameras, then the cameras recorded me and then we extracted data from that and we talked about that. Data and sort of things like that. This object, a piece of equipment, is similar in many ways. It is a camera based system. The term would be.

**[00:19:33]** Oh, also, while you're in Obsidian land, if you want to just like pop open a note and just like write down your questions as they come up, you can do that as well. You probably also know how to take notes because you're like, here.

---

### Chunk 3 [00:19:30 - 00:29:10]

**[00:19:30]** System, the term would be. Oh also while you're in Obsidian land, if you want to just like pop open a note and just like write down your questions as they come up, you can do that as well. You probably also know how to take notes because you're like here, but follow your heart. So this is also a camera based tracking system. It has three cameras.

**[00:19:55]** One camera right here, camera here, and then a camera here. So two cameras pointed in at my eyes and one camera pointing out at the world. The general, the specific term here is video oculography. Video is video, oculo is eyeball. O graphy is like measurement and actually not measurement.

**[00:20:17]** O metry would be measurement. O graphy would be. I don't know, whatever that word is.

**[00:20:24]** And also like before, the cameras are relatively independent of each other. They're all going to go through the same wire to be recorded, but they're not rigidly attached to each other. So there's going to have to be a calibration process like we showed before in order to be able to make sense of these things. Also, like before, it is a pain to work with actually, and I'm actually not 100% convinced it will work. Let me rephrase that.

**[00:21:01]** I know it's not going to work to its fullest extent right now because I have already tried that earlier today and it didn't.

**[00:21:10]** But the problem I had was that it wasn't recording from both eyes at the same time. Like it was having some process issues. But that's okay because for our purposes here, like one eye versus two eyes is fine. I have healthy stereo vision. I do not have strabismus, which is the sort of technical term for what people call like lazy eye, where your eyes are not like, oh, like your eyes aren't aligned when you fixate.

**[00:21:38]** Which means that you can generally use like the behavior of one eye to tell you about both eyes.

**[00:21:45]** Yeah, if I had, if I did have strabismus, I would just tell it to point at my dominant eye, which is the one that people who have strabismus just naturally align with. Everybody has a dominant eye. Like you have dominant hands. Yours is probably your right eye, but it may not be. We'll talk about that.

**[00:22:03]** Well, if there is sufficient interest in the server chats, we will talk about it. Da da da da da da. So there are many eye trackers in this world. My favorite at the moment is the one made by Pupil Labs, which is a German company, a spin off of an academic group. I like them because they are very open source friendly.

**[00:22:28]** All their code is open source. I have a lot of complaints about the specifics of that code and the software associated with it. But also at this point in my life, I have now written enough of this software that I could not possibly understand more why it is the way it is. So search for People labs. You can find their front page and find the GitHub page if you're curious about what that code looks like.

**[00:22:56]** And then there's videos and stuff like that, which is nice.

**[00:23:02]** A lot of their newer stuff has a very machine learning bent to it. Like they use machine learning to track the pupil and the eyes, which I really don't like because this is their old system, which all the tracking is old school, classical computer vision stuff, which means it is more on that space of direct computation of available data and basically no machine learning inference step. So, so the process between the empirical measurement that happens on the cameras and the sort of resulting data that I want to analyze to do science is rigid. It may not work all the time, but at least I know what each step is. Anytime you have a system that uses machine learning as part of its core processing pipeline, there is an inherent stochastic nature to the outcome because there is a step that uses machine learning.

**[00:23:54]** And machine learning algorithms always are inference rather than direct computation. It's a probabilistic matching type of thing. But that's not important right now. Let's see. So capture.

**[00:24:11]** Let's see. So it's 2:16, want to be done within half an hour. Okay, There you go.

**[00:24:23]** Yeah, as I thought. So we're not going to look at both eyes. It's also like a little reassuring now that I've like written enough of specifically like camera code to see. Like I. Now it's like, oh, I know what that problem is like.

**[00:24:43]** And they also have it, which means I may not be a total dummy. Okay, so that's you. Behold. This is the world camera. It is meant to mimic, but is obviously not exactly the same as my viewpoint.

**[00:25:00]** So we're pretending that this view is my eye view. However, we know that that's not the case because my eye is here and the camera is here. So there's at least a centimeter or so misalignment between this world camera view and my actual eyeball view.

**[00:25:20]** And as much as I want to talk about that because I think it's cool, I'm going to also leave that for the future. And of course, the star of the show, let's do my left eye.

**[00:25:34]** That's My right eye. Wait, why is it. Oh, is that why it's wrong?

**[00:25:45]** Excuse me.

**[00:25:49]** Did I just.

**[00:25:52]** Is this the same one I took off this side for anyone watching? Okay. The other. I put the other one down. Then I was like, wait, is this the same?

**[00:26:02]** I don't know. We're gonna find out.

**[00:26:06]** Welcome to life as a scientist with adhd. It's like, did I take notes? No. Do it again. Fine.

**[00:26:18]** Luckily, that's the way. I also don't work with expensive equipment. Okay, so this. Yeah. Wrong.

**[00:26:29]** I don't think this will make a difference. But. But it is like. It's like I. I did this earlier. Like, I swapped the cameras out, and I just noticed that the.

**[00:26:37]** The right eye was I one. And I. I happened to know that it should be the other way around. I don't think there's anything that would make that cause the problems we just saw. But we're going to see. Okay, this is now my left eye.

**[00:26:48]** Yeah. All right. And when in doubt, shut it down.

**[00:26:55]** There's two white bishops. If you know that. Have I said that before? If you're playing chess and you look at the board and both of your bishops are on the white squares, there are no legal moves you can make to fix it. So just wipe the board and reset it up again.

**[00:27:10]** That's why you shut things down. Okay.

**[00:27:15]** Q. Cap. Cap. Cap. Cap.

**[00:27:20]** Cher. I also noticed today that I think I am recording this at 60fps, which means I am asking the computer to work. There's no. There's no reason that this needs to be 60fps.

**[00:27:33]** Yeah, it's still failing. So anyways, that's your intro to technical troubleshooting. Okay. So now they don't go on the arms. Right.

**[00:27:53]** See, it was the right way before, actually. Still doesn't make sense. Why are they backwards? Because the. It was pointing them out when I put them on the little arms.

**[00:28:18]** Some of you might have been perturbed by the fact that I just dropped this unceremoniously, which is fair. But also, this camp. This one at this point, is kind of like my demo one. And also, I know enough about this technology to know that it's not gonna be. Well, I shouldn't say that on camera.

**[00:28:38]** It's fine. Not really. Okay, shut it down, turn it off, turn it back on again. That's the classic tech joke. It's because of the white bishops thing.

**[00:28:54]** Okay.

**[00:29:04]** And watch. It broke. That'd be really funny.

**[00:29:10]** It.

---

### Chunk 4 [00:29:30 - 00:39:15]

**[00:29:30]** So here I'm shutting it down less powerfully.

**[00:29:45]** I do not want to turn off the computer, but I will if I have to.

**[00:30:14]** Come on, buddy.

**[00:30:31]** Wait, What?

**[00:30:39]** People cam id 2. People cam 1.

**[00:31:04]** I happen to know that one of the things that makes this type of stuff hard is device management. Like your computer figuring out what camera is attached to what. So I had shut down the software, but I hadn't unplugged the cable.

**[00:31:20]** You may not like this, but this is actually what most of research is like.

**[00:31:27]** Come on.

**[00:31:40]** Hey, there you go. Great.

**[00:31:45]** It even says I1. So there you go. All right. Anyways, that's my I.

**[00:31:52]** So we are recording. This is 400 by 400 resolution and 90 FPS. So 90 frames per second, which means that every frame that comes off of this thing, so you're getting 90 measurements per second off of this camera. And so it's. If it was 100, it would be 10 milliseconds per frame.

**[00:32:14]** It's 90. So it's a little bit more than that. No one can do that math.

**[00:32:22]** Yeah. So look at that weird eyeball. Look how weird it is.

**[00:32:30]** So it's a little stretched now because it's 400 by 400. So it should be square. And they don't protect the aspect ratio, which they should, but that's fine. So I will actually manually scale it. Do.

**[00:32:42]** Do.

**[00:32:45]** This is one of these things. Like, so if you take a square video and you play it through like a standard video player, you'll get wrong data because it will be skewed, because most of our videos are skewed like that. But this is actually just the display, which is fine. And see anything else I want to show you down here?

**[00:33:05]** I think I can do this. What?

**[00:33:14]** I'm not going to try to do this on the fly. I can do this. Next time I'll show you the 3D stuff, like how the imodel actually is built. Basically, it pretends like it's a sphere. And I can show you the algorithm.

**[00:33:31]** Ooh, someday this will show up. Come on.

**[00:33:37]** Reset window size.

**[00:33:41]** Oh, that doesn't work.

**[00:33:48]** I tell you guys, this old code.

**[00:33:53]** Okay, so that is my eyeball. You may recognize it. You may have. On average, each of you will have slightly less than 2 of these, and they will work roughly similar to that. There's a number of interesting parts.

**[00:34:11]** So you can see that kind of like. This is my contact lens. This part here is the iris, easily one of the top ten human sphincters, irises. And they're basically a hole that will sort of contract in response to things such as light.

**[00:34:45]** Yeah.

**[00:34:50]** But also to things like emotional arousal and cognitive load and stuff like that. So there is some research called pupillometry that basically just looks at eye trackers and looks entirely at the behavior of your pupil and the size and shape of your pupil, how it changes on different tasks. I'm going to talk some shit right now. The majority of research involving eye tracking is pupilometry because the majority of scientists are lazy cowards. I think that it is.

**[00:35:17]** Not that it's not an interesting symbol, not that it's not an interesting signal to look at, but it is not as interesting as the volume of research would suggest. So why do we look at it? Because it doesn't require you to properly calibrate your equipment. It doesn't require you to think about, like, things in the world and sort of feel, you know, feedback loops and stuff like that. So when you look for research on eye tracking, the majority of it is going to be pupilometry.

**[00:35:41]** I'm not saying don't look at that, but I am saying. I'm not saying. I'm not saying anything.

**[00:35:49]** So you will also. Yeah. So you're gonna. So, yes, you got the iris, good old iris. You got the eyelid, an important, important guy.

**[00:36:01]** Eyelid's job is mainly to keep it moist. Blinking is one of those behaviors that we don't think is interesting, but it's actually a lot that goes into when we should blink. In your normal everyday life, you blink when your eyes are dry, whatever, like a cup every. I don't know, actually don't know what the normal cadence is, but you blink when your eyes are dry. No big deal.

**[00:36:25]** If you start doing really difficult visual tasks like landing a plane or something like that, or walking over rocky terrain, like the research I've done, you blink far, far less often. Because if you're doing a really difficult task, then the cost of being blind for 50 milliseconds goes up. And so you'll see this really interesting behavior when people do hard tasks where, like, it's like my. My research walking with people, walking over rocky terrain. They would be standing at the front, they go, blink, blink, blink, blink.

**[00:36:52]** Then they'd walk and they would blink, almost not at all. And then when they got to the end, they go, blink, blink, blink, blink, blink. And the only times you really saw blinks was when they were. When they were looking from the ground up to the goal and then back. Because that amount of time is like sort of dead time.

**[00:37:07]** So people not cognitively, not like consciously, but whatever the visual nervous system is sort of, whatever clever part handles blinking, sort of knows that that's a good time. And there's a scheduling, whatever omnipause neurons are relevant to that anyway. 25. So class is over at 125. Great.

**[00:37:32]** Doing great.

**[00:37:36]** Okay, so here we have an eyeball. Here we have a world. We believe that these two things are connected in some way. But what we want to be able to see is like something that tells you where in this image I am looking at. Based off of the data that's available from this image.

**[00:37:57]** I have no idea why this is not showing the overlay there, but again, I understand.

**[00:38:20]** So let me real quick, just dump a little more. This is the drink from the fire hose phase of the. Where I just say a bunch of stuff and then you try to notice which parts of it were interesting. You'll notice that the eye moves in strange ways, right? Sometimes it does these like jerky movements like that.

**[00:38:38]** Those are called saccades. I'm looking there. I'm going to look there. Finger to finger. Those are called saccades.

**[00:38:45]** Saccade is French for jerk because they're jerky little eye movements. It is the fastest movement that your body can make.

**[00:38:54]** And yeah, it's wild. Oh, also, those two little lights there are infrared emitters. IREDs. Infrared emitting diode, like an LED, but for IR, you can see the reflection there. If I cover them up, my eye gets very dark.

**[00:39:13]** You can actually see my finger.

---

### Chunk 5 [00:39:00 - 00:49:00]

**[00:39:00]** Emitters IREDs, infrared emitting diode, like an LED. But for IR, it's. You can see the reflection there. If I cover them up, my eye gets very dark. You can actually see my finger reflected there.

**[00:39:17]** And then the thing that I find even more interesting than that is you see that kind of ghosty. So eyeball. The thing that you're. When you look at the eyeball, the first thing you see is technically contact lens. And then behind the contact lens you see cornea, which is the clear thing on the outside.

**[00:39:38]** If you not right now, but later pick a friend and try to look at their eye from the side, you'll see like a little bulbous, clear dome. That's your cornea. The majority of the bending of the light that has to happen for your image, image to be in focus happens at the cornea. When you wear something like a contact lens, you're changing that refractive index to make things line up. Because your eyes are not shaped.

**[00:40:02]** The shape of your eyes is something, something you get past the cornea, you sort of go. The pupil, if not is just a void. It's just an empty hole. Behind that you have the lens. The lens is like something that you like, got muscles attached to it and it stretches.

**[00:40:21]** So if you look at something close by and if you are able to like fuzz it out, like, just make your eyes go out of focus, that activity is the activity of sort of like changing the shape of your lens to break the sort of automated focusing systems that are going on at various stages of your nervous system. Because, like, how do we know how to focus? How do we know to focus? Oh, I'm looking close. I should make my lens one shape.

**[00:40:53]** Oh, I'm looking far. I should make my lens a different shape. Somewhere in the goop there is some part which has. Which is functionally similar to the autofocus on a camera, although very different in every other aspect.

**[00:41:08]** And then you go back behind the lens.

**[00:41:15]** Sus.

**[00:41:18]** So then it goes back through the lens. Then there's kind of like empty sort of. What is it called? Like the vitreous humor, which is this, like clear goop. And then you hit the retina, which is backwards for some reason.

**[00:41:29]** Because when we crawled out of the ocean, a lot of things inverted. And one of the things is our eyes. So our eyes are backwards on the inside. Our retina are backwards. And then you hit the pigment epithelium, which is like a dark thing on the back.

**[00:41:43]** If you have albinism, you don't have. You'd Have a hard time making melanin. So you don't get that. And then you have problems with your vision. And then you hit the back of your eye, which is the sclera.

**[00:41:53]** The white part is the sclera. And then you get optic nerves and all that good stuff. So if you notice those two white glowy spots, we're hiccuping again.

**[00:42:17]** Oops.

**[00:42:20]** That's the first reflection of the infrared, the IR8 reds. Like the brightest part is the part where it bounces off the front of the contact and cornea.

**[00:42:32]** And then probably mention very briefly next time Snell's Law. When light hits a surface, it can do one of three things. It can reflect, which is bounce off, it can be absorbed, or it could refract, which is change direction. Someone nodded, which makes. Someone took a class maybe.

**[00:42:52]** It's one of the things I learned it recently and I only very recently learned that that thing is called Snell's law. So I was kind of guessing, so nailed it. And so you get these sort of ghosty other reflections there.

**[00:43:10]** You can see some of which move like in phase, some which move antiphase. Those are going to be some version of the first, second, third and fourth Purkinje images, which is basically the reflection as the eye, as the light moves the different moves through those different tissues. So from the cornea to the front of the lens to the back of the lens, every time it hits it, the reflection part bounces back out. And because the camera is so close, we can see sort of where that's happening, which is interesting. And there's some like, some very, very high end eye trackers will use that, those like secondary tertiary and quadrantary Purkinje images to do very, very high accuracy eye tracking.

**[00:43:57]** But we don't do that here. And okay, so we're hiccuping. Another thing to note about software, I happen to know that the people who write this code do it on Linux. So this is a Windows machine. So generally if you code in Mac, in Linux, it works well on Linux and Macintosh.

**[00:44:14]** But Windows is such a different system that we get those errors.

**[00:44:23]** It's hiccuping there. So. Okay, okay, let's get close to done. So what I'm going to do now, I'm going to try to calibrate the eye tracker so that we can get some, some real time measurement of where I'm looking in real time. It's not going to be as good as it could be, but I'm going to do some post process so we can get A better calibration after the fact.

**[00:44:52]** So I'm going to hit C and I think if I do, I think it'll pop up there. I look at the thing and come on, buddy.

**[00:45:22]** So I'm looking at the bull's eye. Not sufficient pupil data. Oh, it may not happen because of.

**[00:45:36]** Okay, so I'm going to record some of this data later.

**[00:46:00]** You just die.

**[00:46:05]** Restart default settings. But I will show you the kinds of stuff.

**[00:46:14]** Oh, there it goes.

**[00:46:18]** So that's me. That's actually tracking my eye.

**[00:46:27]** And 490 manual mode.

**[00:46:48]** That's probably good. Okay, so, all right, so eye movements there. So sometimes you see these really jerky eye movements. Those are called saccades. Those are usually voluntary.

**[00:47:06]** Sometimes you also see these like smooth eye movements. So I'm fixating on the camera, moving my head and my eyes moving nice and smooth. Those are sometimes called smooth eye movements. But more specifically, those eye movements are the result of the vestibular ocular reflex, which is one of the lowest level and it's extremely old reflex. We have evidence back to Bony fish, which is like 450 million years ago.

**[00:47:34]** And it is basically a very short feedback loop connecting the vestibular system, which measures head acceleration and rotation that counter rotates the eye relative to my head movement so that I can fixate objects in the world even as I'm jump sort of moving around. And the image on my retina remains clear because, yeah, the chemical that involved, if there's any biology majors in the room, the actual biochemistry of how vision works happens on the basis of opsins, which are strange chemicals that are photobiochemical electrically active, meaning that if they absorb a photon, they change shape and that changes their electrical properties. And that's what sets off the sort of neural cascade. And so that's how vision actually happens. But those opsins are relatively slow.

**[00:48:36]** Like they take like 10 to 15 milliseconds to respond to light, which is slow enough to cause problems and certainly slow enough if you fixate your thumb and move your head around, the blur in the background is the world moving too fast for your opsins to keep up. So we have a lot of gay stabilization.

---

### Chunk 6 [00:48:45 - 00:58:45]

**[00:48:45]** Enough like if you, like if you fixate your thumb and move it, move your head around, the blur in the background is the world moving too fast for your opsins to keep up? So we have a lot of gay stabilization mechanisms sort of very fundamental to our nervous system that allows us to basically like pick objects that we're looking at and keep them stabilized on the back of our retina in order to give our opsins and whatnot time to react to the light and send images back that are clear enough to work with.

**[00:49:24]** So yeah, so quick eye movements, you basically are blind during those movements because the world moves too fast. So there's a lot of complicated stuff about why we can't see during saccades. But like. Yeah, but then when you're actually sort of fixating something and moving your head around, that sort of stabilization aspect happens on the basis of things like vestibular ocular reflex and optokinetic nystagmus.

**[00:49:57]** And the other type of eye movements are called smooth pursuit eye movements, which is so I cannot, with my normal healthy human nervous system, move my eyes smoothly across the world. It's just not a thing I can do. I'm going to try to move my eyes in a smooth line along the back of the room and it's going to look like that, which you could probably tell is like jerky. Because even as I'm trying to do that, I'm making small saccades because of all the different clamps that happen, I cannot make a smooth movement, except that I can, if I am fixating a target, smoothly pursue that, but only if I have a target. So that's called the smooth pursuit eye movements.

**[00:50:45]** They are very phylogenetically recent. They're very strange.

**[00:50:52]** And they're strange because it's like it's dependent on the fact that I'm looking at something. Like I have chosen to look at this and so I can now do smooth eye movements. But if I'm not, I can't. There's some like, there's interesting study that like if I'm in a completely pitch dark room where I can't see my hand, I can still make a smooth pursuit eye movement. Tracking my thumb, but only my thumb, which.

**[00:51:21]** Chew on that. Another personal favorite is this eye movement which is torsional eye movement. So it's. Sorry, torsional. It's a torsional eye movement.

**[00:51:33]** Right. So you have three three dimensional object called an eye. It can move left, right, up and down, but can also rotate around its central axis. And you can see as I rotate my head, I am stabilizing it in that direction, but not that much. You can see kind of like trying to keep up, which is always fun.

**[00:51:59]** So this is, let's see, what am I doing? So I'm looking at the eye. What am I? Eye movements are weird because it's one of the very. We have voluntary control over many parts of our bodies, but not all of them.

**[00:52:14]** Like you can control your breathing, but you can't control your heart rate, but you usually don't control your breathing. It's under partial voluntary control. Our eye movements are like that. We can control them, but we typically don't. Typically just sort of, they do their thing and if we want to sort of like pay attention to them and sort of clamp down on them, like with sort of cognitive voluntary control, we can.

**[00:52:36]** But there's an effort there. What is that effort? Hard to know.

**[00:52:45]** Okay, 2, 45, 1245. So I'm going to try. I'm just going to go ahead and record the data even though I don't think it's going to work. So I'll record this, I'll record some stuff later and I'll bring it back in next time. So we're now recording from both the eye and the world camera.

**[00:53:09]** They are time synchronized so the frames will line up in time, but they're not spatially calibrated yet.

**[00:53:22]** And I don't like their automated calibration system. So I'm going to do a separate calibration which is going to involve. So I'm going to be looking at the, the nail of my thumb looking at that there, sort of rotating it. So I'm giving myself a reference point in the image that I know that I am looking at because of the instructions that I gave to myself. And I can use that to calibrate it after the fact.

**[00:53:50]** And then I will importantly not keep my thumb in the screen when I'm not doing that task because I won't be able to tell otherwise. I'm also, I'm calibrating. So I'm also going to look at the recording symbol over there and sort of do that same kind of movement. Because the calibration is somewhat distance dependent.

**[00:54:14]** So giving myself a short target and a long target will be helpful in that way. So the measure the things I want to do. So again, just let's test that it's actually working. So looking at there, looking at there, I don't know from the direct data which one I am looking at, but I know that I'm Looking at one of those.

**[00:54:38]** So I can. I just cheated. And look at this. Look at the computer screen. So that will be a way to kind of like identify what's looking like there.

**[00:54:47]** Ask yourself what you think the data will look like if you were. If we could see the track of my eye. Like what does that look like in the data trace? What does that look like in the data trace? And what does this look like in the data trace?

**[00:55:04]** This is a visual motor task and I'm going to see if I can close my eyes and do it. And I can't.

**[00:55:20]** Oh yeah. So now I'm going to try to trace something in the back and we know that I can't. And now I'm going to try to trace this. And we know that I can. And was there any way to tell from my eyeballs the difference between this and this?

**[00:55:38]** Maybe not.

**[00:55:42]** And just for fun, look at the screen. Classic calibration.

**[00:55:50]** Okay. That's roughly three minutes of recorded data, which is more than enough to spend several careers analyzing because we just produce. It's just so complicated. Guys, anything else? Oh, I'm going to do.

**[00:56:15]** So here I am walking here. I'm going to turn around there.

**[00:56:22]** Oh, you can't actually see my eye.

**[00:56:27]** I'm not going to recalibrate it because I'm going to choose the same calibration which is safe enough. This is the thing I noticed when I was doing my walking studies is you could tell just from the eye data like when the person turned around because you see this kind of like tick, tick, tick, tick. Because my head is rotating and the VR is trying to make it align but it gets to like a limit on the side so it sort of gets to the edge and ticks back. Is it happening?

**[00:57:00]** Does it happen like tick, tick, tick. Okay, cool. Nervous system works. VOR is such a low level reflex that it's used as a proxy for brain death in emergency situations. Like if you are looking at someone and you don't know if they're alive, you can rotate their head.

**[00:57:16]** If their eyes don't counter rotate, that's it. Like that's not a, that's not a reflex that can fail while the rest of the body is working.

**[00:57:26]** Kind of a cob, but there you go.

**[00:57:36]** Great. Another minute of data. Whole other career and yeah. Okay, take these off.

**[00:57:49]** Luckily we can't see infrared. There's a lot of sort of. We use the fact that we can't see infrared in specifically in human movement studies, but in a lot of cases because if these were visible light, I couldn't use them because I would be blinded. So instead, they're infrared, which is both like a low energy wavelength, so it's hopefully not doing too much tissue damage. But also, you can basically blast my eyes with light and then just have a camera that records in that wavelength and sort of make your life work that way.

**[00:58:22]** Okay, great. I hope that was sufficiently enticing and confusing. I think we can call it there.

**[00:58:35]** Please dump your questions into the machine. See how well it does. I'll be really interested because this is now getting closer to, like, my actual proper area.

---

### Chunk 7 [00:58:30 - 01:00:12]

**[00:58:30]** Using, I think we can call it there.

**[00:58:34]** Please dump your questions into the machine. See how well it does. I'll be really interested because this is now getting closer to, like, my actual proper area of, like, literal expertise. So I'll be really interested to see, like, how the bot does as you ask it questions. It will probably get it, like, totally good at the level that you really need to worry about it, especially because we're not giving you tests or anything like that.

**[00:59:00]** But I'm really curious about the nuances. Like, sometimes when you ask it, if you push it to sort of details, you push it on specifics, it will probably give you really good best guesses. But I'm guessing that there's going to be places where it actually misaligns with what I know about how the field is going, my personal beliefs, which is, like, I believe things about the nervous system which I cannot prove and are not written down anywhere, and other experts may disagree with me. So I'll be really interested to see kind of like, first of all, what y' all are interested in, and secondly, how a bot that has been trained by eating the Internet does when you get to those sort of, like, limitations on the sort of specifics of knowledge. Because as I said before, I think it tends to nail anything at the level of textbook.

**[00:59:50]** And then it starts to fuzz out as you get into sort of the parts of the conversation that have less of a footprint on the data set that this bot ate.

**[01:00:05]** Okay, that's not bad. I have a whole half an hour. All right, bye.

---
