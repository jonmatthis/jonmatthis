# Transcript: 2025-02-03-HMN25-02 - SI Units, Space and Empirical Measurement

## Source Information

- **Source Type:** Local File
- **File Path:** `C:\Users\jonma\syncthing-folders\jon-alienware-pc-synology-nas-sync\videos\video_eater_downloads\playlists\[2025-01-Spring] Neural Control of Real-World Human Movement\2025-02-03-HMN25-02 - SI Units, Space and Empirical Measurement\2025-02-03-HMN25-02 - SI Units, Space and Empirical Measurement.mp4`

---

**Total Duration:** 01:30:22

---

## Full Transcript

### Chunk 1 [00:00:01 - 00:10:00]

**[00:00:01]** Okay. Hello. Hello. Hi. Thank you.

**[00:00:07]** Welcome to whatever this is.

**[00:00:13]** So, yeah, let's. Okay, so let's do the standard check in thing. So I am recording this and we'll be posting it online a couple people. So people have sort of sporadically been contacting me and saying like, hey, I'm sick. I'm not going to make it to class.

**[00:00:28]** Hey, I'm not going to make the deadline. That stuff. I stuff. If you're sick, straight up, don't come to class. Like, we had a whole ass pandemic.

**[00:00:34]** So, like, please let us learn that lesson as a culture. You don't need to check with me. It's totally fine. I trust you. Also, the deadlines are all kind of made up.

**[00:00:42]** So like, you know, I put them on there in the sense of like, I really hope everyone has it done by this point because I like, I use the data from that for each stage, but they're all available until the end of the semester. So with the exception of the poster thing, there's a couple like hard deadlines for that that, like, you know, you have to get it to the printer on time and stuff like that. Everything else just kind of like just get it done as soon as you can. Which I understand is a dangerous thing to say to some people. But I trust you.

**[00:01:09]** I believe in you. Just check all the boxes before the end of the semester. We'll be good to go.

**[00:01:17]** So quick, check in on schedules and stuff. What did we do last Wednesday? Can you remind me? Did I talk or did the group thing? Group thing?

**[00:01:26]** Yeah, group thing was good. Group thing with bot. Yeah. Great.

**[00:01:35]** And then we had something that was due and today, what fun. We're going to be talking about a lecture that I've given a bunch of times and I always enjoy giving it. And it's going to be intro to measurement and concepts and whatnots thereto pertaining.

**[00:02:05]** And check this out. Look what you get to do when you're in charge. No assignment. Great. Feel like we've been doing enough.

**[00:02:13]** You guys are doing great.

**[00:02:17]** Do, do, do, do, do, do. Okay.

**[00:02:21]** Is this the right day? This is the right day. Cool. Oh. So today's lecture is going to be about like measurement and units and things like that.

**[00:02:31]** Sort of like hopefully more. It's got a lot of props and visual aids and whatnot. And I want to do it now because on Wednesday I think we can do a free mocap in class recording, which will be our first relationship with sort of more classical data. I keep referring to the text stuff that you're punching into the server as data and it is data, but it's kind of like if you asked me three years ago if that was data, I'd be like, yeah, I guess technically. But it's only since like AI came online that I think of that as data.

**[00:03:14]** Free mocap is a motion capture sort of free open source thing that I've been building for the past half decade or so of my life. And it's specifically designed to sort of like make good class demos and things like that. So we're going to be recording some data and then talking about it in the context of the kind of concepts we're going to go over today. So. So hopefully we can get some of that in today.

**[00:03:42]** Let's see. Anything else to catch up on? Just for completeness, I will remind everybody, although I didn't. Nothing special has happened with this round. But the server.

**[00:03:53]** So in the server, in the links and resources, find the server scrape checkpoint and there is the same sort of at the bottom 127. So that's the server scraped and analyzed as of this morning. So same thing. Download it, unzip it. If you don't know what unzipping is, it's the thing where you double click it and it makes a folder next door that you can open like a regular thing so you can search for your name in there.

**[00:04:22]** I'm going to be refactoring the way that we do the student profile building thing. So like your individual profiles are going to change probably next week just because I'm going to change the code and prompts that make it. I realized that it would probably give you a much more precise measurement of what you're interested in. If I didn't use everything you put in the server for the profile, but just use the assignment chats. So the ones from your intro and the poster presentation thing.

**[00:04:51]** And I'm also in the process, I might also set something up that you can sort of in a given chat you can like ask the bot to remember you and it will pull that history into the conversation and that will sort of. You don't have to start every conversation from scratch type of thing.

**[00:05:11]** Yeah. Also by just by way of remindering, sort of. What's the word? Helping guys learn the paths and whatnot.

**[00:05:23]** Here we are on the server, same channel up here. Links and resources and course repository. Click on that and something pops up. I don't know why two things pop up. This is the course repository.

**[00:05:37]** This is the sort of the most up to date. Oh, actually I Forgot to use last time. Update syllabus, Abuse commit and sync. Yes, thank you.

**[00:05:55]** Don't break. And now up here, where'd you go? Oh, right, same thing on Firefox. And you see it says update syllabus. That was the thing I just pushed up.

**[00:06:12]** And now the code is not the code, the text, which is code for primates and that's updated. This is GitHub. That's kind of what GitHub does. It's a version control software. It's kind of like track changes, but more sophisticated.

**[00:06:32]** Pretty much every piece of software you've ever used in your life has used Git at some level. And I'm kind of like hijacking it to do text based stuff.

**[00:06:45]** Doo doo doo doo doo doo. So yeah, and also just to be clear, just for fun.

**[00:06:55]** So this site is basically as if it was a folder. The readme Here is the thing that's posted down there.

**[00:07:03]** This is what it looks like formatted.

**[00:07:08]** That's what it looks like raw. This is a honest measurement and record of exactly what my primate body did to a keyboard at some point in time. So it is a truth preserving record of my thoughts in a way that a Docx file or a Google Drive link sort of will never be. So shout out to markdown in raw text formats.

**[00:07:34]** Okay, Right, so on this page, going back to the front page, there we go in the lectures folder in 20250127, Intro to Measurement. Then the top one is called Intro to Measurement. And here we go. It's the. What's it called?

**[00:08:04]** The notes for My notes for the lecture that we're about to give. And with that I'm going to switch away from the GitHub and go to my local version just because I want to.

**[00:08:21]** Local meaning on this machine, not on the Internet, some other server's machine. GitHub is owned by Microsoft, so technically that state data is hosted on Microsoft. This is on my computer. Okay, cool.

**[00:08:45]** This is a brief summary. We'll see how much we get through. I think we'll get through all of it. So here we are in this class extensively to teach y' all what science is, what science looks like, how you might ever do such a wacky thing as to attempt to know the world and do empirical research within it. And there's a lot of things that get taken for granted by when you sort of just live as a human person in a world that you start to find yourself needing to get much more specific about once you actually start to try and start trying to get into the business of knowledge generation.

**[00:09:29]** So the idea as a scientist, is that you are attempting to create new knowledge for humankind, which is a very difficult thing to do. It's hard to know stuff, and there are certain rules for how to do that. So a lot of what we talk about in the sciences, the empirical sciences, is based on the concept of empirical measurement. So there are many ways to know things, the scientific method and the empirical method is one way to know.

---

### Chunk 2 [00:09:45 - 00:19:45]

**[00:09:45]** So a lot of what we talk about in the sciences, the empirical sciences, is based on the concept of empirical measurement. So there are many ways to know things, the scientific method and the empirical method is one way to know the world. It's a very powerful way to know the world because it allows you to do things like make predictions about the future, build tools, heal people when they're sick, things like that.

**[00:10:13]** And everything is sort of, in that sort of conception of knowledge is based on, at some level, an empirical measurement of the world. Where, yeah, empirical measurement is. We're going to talk a little bit about what that means, but basically it's the idea that you have done, yeah, you've done some kind of a measurement, and that's what that term measurement is one of those kind of like one of those terms that gets taken for granted, but we'll talk a little bit about what that means. So the most important thing to sort of. I don't know about the most, but one of the most.

**[00:10:46]** One of the very important things to think about when you're thinking about empirical research and the concept of measurement is that everything that you're doing, everything that you're building on has to be built relative to something else. So when you're trying to. If you're trying, like, if you're trying to generate new knowledge, that knowledge that is going to be sort of based on other things, like I used the term earlier of truth preserving. It's a very important term in the sort of philosophy of science because that is the concept of being able to build from one thing that you know another thing that you might know. And everything that you think you know about the world, if you sort of dig into it, is going to be based off some sort of background of.

**[00:11:32]** Well, I think this because. I think because I learned that because I believe this because of all that kind of stuff. So it's helpful when you're sort of trying to learn the concepts of measurement to try to recreate those epistemological chains where epistemology is the study of knowledge and try to ask yourself sort of, where do these things connect to?

**[00:11:56]** If I were to redo this, which I will some other time, I probably would have put this one up top. So where most important thing is that skepticism is the basis of scientific reality, which is the other concept, where skepticism is the idea. Long story short of, you have to. You have to have reasons to believe the things that you believe. You're not allowed to just believe things for no reason.

**[00:12:21]** And everything that you sort of. That you consider has to be kind of, you know, you have to look directly at it and try to boil down sort of what that is connected to.

**[00:12:32]** So given that, it is reasonable to ask about origins and these sort of philosophical. The classical philosophical bedrock of belief we tend to ascribe to this dude, Descartes, who was operating in, like, the 1500s. You've heard of his Cartesian coordinates and other various things which we'll talk about in various points in time. But he is quoted as sort of trying to do this philosophical game of trying to understand what his knowledge of the world is based off of. And came across this wonderful little phrase called cogito ergo sum, which means, I think, therefore I am, which is basically a fancy way of saying there's.

**[00:13:16]** If you really drill down to it, the only thing that you can actually truly know and believe without reference to some other sort of piece of knowledge is that you are having a conscious experience right now, in this very moment. You are having a qualitative state. You are thinking. And nothing in the concept of the universe could ever fake the experience of having a conscious experience in this exact moment. Now, your memories of what you did yesterday, that could be fake.

**[00:13:47]** You could have done hallucinogenics. You could have had. Someone could be poking at your brain, that could all be fake. Your perception of the world around you, that could be fake. I think there's a cup out there, but I could be wearing some sort of crazy VR helmet.

**[00:14:01]** It could be like floating in goop in the Matrix. And so all of these other things that we want to believe are all in some way shape and form subjects of skepticism. You. You could deny, you could doubt that the. The veracity of anything else besides that central nugget of I am having a conscious experience right now in this moment.

**[00:14:23]** Now, if you only want to live with that sort of nihilistic belief, you are left with a rather uninteresting philosophical position called solipsism, which is the belief that you are the only person that exists and everything else around you is fake and all other people, people you see, are just illusions. That is technically, I believe, the only truly defensible philosophical position. It's also not useful or helpful or particularly interesting because we also. Because if you're willing to accept other gradients of belief and gradients of truth into your life, you can start to build what feels like knowledge about the real world as long as you're willing to have things like. You're willing to have things like trust in things like memory.

**[00:15:12]** And if you're willing to sort of smush together all your memory and then believe such thing as statistics. You can actually do quite a lot with that. Because, yes, I can doubt like, I can doubt that there's a cup in front of me right now. But if I keep looking and it keeps happening and I keep moving and it has this sort of like geometrically reasonable deformations, and then I reach out and then I have a cup in my hand and then I put it to my mouth and I get liquid. At a certain point, the accumulation of those sensory experiences starts to really resemble something like knowledge that I might have about the real world.

**[00:15:43]** Like it might. It starts to become increasingly likely that there is in fact something resembling a cup somewhere outside of my conscious experience.

**[00:15:56]** And which is great because that's what allows us to sort of. We match each other in this universe on the basis of our shared memories and statistics. And luckily that doesn't really. It's not really that hard to do, but it is sort of troubling to think too closely about.

**[00:16:17]** So from the epistemological point of view, we're going to base our knowledge on sort of the awareness that we exist, which is good. And then, I really hate to say it, but the only. But the other thing we have is memory and statistics. Not a lot, but we can work from there.

**[00:16:36]** Now with that, I'm going to shift away from that sort of philosophical, epistemological, kind of like fluffy existential crisis Philosophy 101 Type of space and shift back into the more like rigidly sort of empirically grounded world of direct empirical measurements. But we're going to have a similar game to be played there where when we think about something like measurement, we still have to base that measurement on something. So let's talk about. Let's talk about measuring things. And let's start, I think, simply, simply enough with a really basic measurement called distance, spatial distance.

**[00:17:31]** This lecture has a lot of props and visual aids, all made, roughly speaking, out of garbage that I found outside. This is a stick that is kind enough to be roughly a meter long and also can be screwed apart. It was actually this, like the stem of a lamp that I found. And I didn't wind up liking the lamp, but then I realized that if I pulled it apart, then I could stop having to pull a meter long broomstick onto campus once. Oh, once a semester.

**[00:18:13]** So.

**[00:18:17]** So yeah, I see you find one that I can see. A hiking stick could probably do well here. Okay, so this is, this is a stick. This has. Let's say such a thing as measurement as a, as length.

**[00:18:35]** So if you wanted to measure things in the world, you could use something like this. Let's pretend that this is one meter long, even though it's actually slightly longer than that. Let's pretend like it's a meter and we wanted to measure something. So let's see.

**[00:18:53]** This will brought colors today. So we'll see how that goes for us. Rgb. Rgb. Start with black, I guess.

**[00:19:02]** So if we're trying to measure the length of things, let's say we're trying to measure the length of the room or how tall you are, how tall this thing is, whatever. We're going to want to eventually write these numbers. So we're going to have some sort of a measurement tool like this, or what's it called, Tape measure, something like that. And we're going to make some measurements and then we're going to write them down. But when we write them down, we're going to be.

**[00:19:27]** We're writing down a number of some kind.

**[00:19:31]** Let's sort of skip a couple of steps and then get to the place where we've written down a bunch of numbers. Now we want to represent them, sort of to communicate. We've done a scientific study on how long various things are, and we want to present this research to our conspecific.

---

### Chunk 3 [00:19:30 - 00:29:30]

**[00:19:30]** So and let's sort of skip a couple steps and then get to the place where we've written down a bunch of numbers. Now we want to represent them, sort of to communicate. We've done a scientific study on how long various things are and we want to present this research to our conspecifics and colleagues. So we have to write them down. So we have various ways of measuring things like space and time.

**[00:19:55]** And we're going to start with space and then we're going to eventually get to time, which won't take, which is actually not, don't worry about it. So the first thing you might want to in measuring things, you have things like dimensions. You have one dimensional, two dimensional, three dimensional, high dimensional. We'll talk about these things in a second. And in all these cases it's going to start with something resembling an origin.

**[00:20:20]** So this is the origin. It is a zero dimensional object and it contains no real information other than it exists. Right. This is a point that doesn't exist. This is a point that does exist.

**[00:20:37]** So this point conveys the information. Hello, Yes, I exist and not really that much else. Not particularly useful scientifically, but very important when you're trying to figure out, if I come to you and I say, oh, hey, that thing is three and a half sticks long, that is implicitly relative to something which is zero sticks long, which is something that doesn't, which has no extent. So zero dimensional gray. Great, good job.

**[00:21:05]** So now let's think about this dimension and let's call it X, because that's traditionally how we do it. And this is now a one dimensional object. So let's say this is infinitely long and we've measured, this is one stick long. So this stick is there. So there you go.

**[00:21:26]** So one stick long and then I can measure two sticks, three sticks, etc.

**[00:21:41]** That's way better.

**[00:21:44]** So now if I'm going around measuring things, I can keep track of the length of the thing. But again, this is not particularly exciting. There's not really a point of drawing that you just write down the number. You don't gain anything by looking at that number relative to zero other than just the knowledge of how numbers work.

**[00:22:08]** So I'm going to call that X. We're also going to call that length. Great. So now we want to measure such, and that's good for measuring things like string or distances from here to your house or height of a person. But now we want to go around, we want to measure different things.

**[00:22:29]** We're still doing stuff in we're still measuring length and distances. And now we're going to split and have a second dimension that we'll call Y, we'll also call that height. And it uses the same unit. So you can still be one stick tall, you can be two sticks tall, things like that. And so now you can measure things like boards and desks and floors.

**[00:22:55]** And if you measure something and it's two units long and then one unit tall, then that's a point in that space and that is a two dimensional point. Two dimensional, meaning it's got two numbers you have to use to define it in the robotics world someday, like we're going to. I know this is basic, we will be ramping up from here. But another way to think about this is it's two degrees of freedom, meaning that if you want to know the area of something, you need to know two numbers. To be able to define that entirely, you need length, you need width, and you could do that in various other ways, but this is a two dimensional number.

**[00:23:38]** So now you want to measure things, you want to keep going. So you want to keep measuring something in a higher dimensional space. So you've got length, you've got area, area is length times width or something like that. And, and so now you want to also measure volume. And with that I have run out of dimensions on the board.

**[00:23:58]** I can no longer. So this is an accurate one to one representation of the two dimensional point xy. If I want to make a three dimensional space, I no longer have enough dimensions on this board because this board is a two dimensional object. So we can fake it and do this kind of like right angle thing. Let's call this guy back here, Z and think about how do we do this?

**[00:24:23]** So we go so 1, 2 and then 1, 2, 3.

**[00:24:35]** So this is XZ and then we can also make that up.

**[00:24:45]** That's a little screwy, but it's fine. You get it? X, Y, Z. Great. This is a three dimensional point.

**[00:24:54]** We've done it. That's great. So this is how you can measure. If you're trying to categorize objects according to their volume, you need three degrees of freedom. You need three numbers to define that volume specifically and you can represent that spatially in this nice sort of three dimensional grid here.

**[00:25:13]** Now I don't want to belabor this point too much because it will sort of get there. But. So this is three dimensions. Traditionally, if you ever, if you're going to touch engineering, this is the international symbol for three dimensional space. X, X, Y, Z.

**[00:25:33]** This is the Right hand rule. So I'm doing it backwards here, but it would be. Yeah, it's like this. So X, Y, Z, X, Y, Z. This is a left handed coordinate system.

**[00:25:48]** It is illegal. Don't do this just because of the rules. Actually there's more to be said there, but we can skip past it.

**[00:26:00]** And so three dimensions is how many we have in this in space, in three dimensional space. In humans we are super good at a lot of spatial estimates and we really are very good at making things, making very quick calculations of things like the cup is in front of the bottle, the cup is near the edge of the table. Those kind of spatial, what's the word? Computations are very easy for us. Now there's nothing special about three dimensions except for that that's how many you need to define space and time.

**[00:26:37]** But you can keep going with these numbers if you're trying to define something that requires more than three numbers to define. And again, I don't want to blame this point too much, but I will say that it has to do with Pythagorean theorem and how you measure things like distance. Because in one dimension, the distance from a point to the origin is trivially sort of 2. So Pythagorean square is the one that's ABC. So A squared plus B squared equals C squared.

**[00:27:14]** So C equals square root of A plus B, B A squared plus B squared, whatever. So this is how you do distance. You've all seen this, I'm sure, at various points in your high school career. This is the particular case of doing Pythagorean theorem for two dimensions. You replace the A and B with X and Y and then you have a way to measure distance in a two dimensional space.

**[00:27:39]** In a one dimensional space it's very. The square root of two to the second is just two. So that's easy to do in two dimensional space. It's just that in three dimensional space, to measure distance you just add a Z, you just do the measure. The distance in 3D space is the square root of x squared plus y squared plus z squared.

**[00:28:01]** And then you can just keep going. There's nothing special about two. You can add a W, you can add a L, you can add A, I don't know and just keep going and keep. And you lose the ability to plot it in a way that makes sense. But you can keep doing all the same math that you were doing with three dimensions up to umpteen million dimensions.

**[00:28:24]** And a lot of the AI stuff, the way that that works is it is it uses that same kind of like spatial math, but it's doing it in like very, very high dimensional spaces, which is one of those terms that you keep. You hear people say things like high dimensional mathematics and it's like, oh my God, it's so crazy. It just means that you keep adding numbers to the Pythagorean theorem to measure distance and everything else is pretty much the same. I will say too, there's a lot of we're going to do general mathy stuff here, but luckily you don't have to do any of the math, you just have to understand it, which is so much easier because I know that there's a part where I say, oh, look, you can have two XY things like that. And that makes some intuitive sense.

**[00:29:05]** And I just need to promise you that that intuitive gut check of like, yeah, that makes rough sense. That's the vast, vast, vast majority of the things that you actually need to know about mathematics, like being able to do it on paper helps. The guy who taught the class before this, I'm sure would have many things to say about what I'm about to say, but I firmly believe that being able to do the math and.

---

### Chunk 4 [00:29:16 - 00:39:14]

**[00:29:16]** Mathematics, like being able to do it on paper helps. The guy who taught the class before this, I'm sure would have many things to say about what I'm about to say, but I firmly believe that being able to do the math on paper is just. It's an extra layer of understanding on top of the gut check intuitions that will get you most of the way towards where you need to go.

**[00:29:42]** Okay. Yeah. So right now we're talking about, let's make this simpler and just go back down to two dimensions because it's easier.

**[00:29:54]** There we go. Two da da da da da. Great.

**[00:30:00]** So this is. We call these cartesian coordinates because of Descartes, because western side science and math likes to name things after the people that discovered them, which is annoying as hell, because the same people discover so many things that you end up replace using all these words all over again. It's really obnoxious. But these are called cartesian coordinates, ostensibly named for Descartes, who the story is that he was like a sickly guy and he was in his bed and was watching a fly crawling on window and realized that he could define the fly's position by just looking at the intersection point between the fly and these two points on the windowsill. And then thus made some formalisms and then get to name a hole.

**[00:30:44]** You get to name the concepts of a grid after this guy, which is annoying. But. So this cartesian space is typically defined by things like it's got straight lines, it's got grids, it's got squares. If you go, you know, go from two dimension to three dimension, you go from a square square to a cube, things like that. You could also define this type of stuff in angular coordinates.

**[00:31:05]** So if I care about this point in space, I could define it using these sort of like straight line, you know, right. Right angle projections onto these basis vector axes. I could also say that it's, you know, this far away at that angle off of zero. So I start by. I start from this sort of.

**[00:31:30]** We'll call it X. And then we go up by this angle, which can be degrees or radians or whatever you want. Then we go out by this number R by some distance and we still get to the same spot in 2D space.

**[00:31:47]** Instead of defining this in terms of XY, I could also define it in terms of theta rho, which rho is just like the distance rho, like radius. Like if this was a circle, it would be whatever. That's not actually what rho means, but that's fine. So again, Noticing that this is a two dimensional point, two degrees of freedom. And I can define it either in these linear XY coordinates or I could define it in these angular theta rho coordinates because yeah, you need two numbers to define its position.

**[00:32:19]** And so two numbers you get, once you start, if you were to go from. So this is a good way to draw circles. If you go from 2D to 3D, they become spheres. And the important thing to know is that you can always switch back and forth between the linear coordinate systems or the spherical coordinate systems, the sort of. We call these polar coordinates versus Cartesian coordinates.

**[00:32:39]** And in practice when you're doing stuff, you wind up just switching back and forth depending on what you're doing in the math. Like, you know, if I'm looking at things like joint angles, it's really helpful to look at it in terms of polar coordinates because there's already got angles in it. In fact, it's even easier than that because for looking at one of these guys, this distance we can just assume never changes. So now if I'm looking at something like joint angles, if I assume that these are rigid bodies and the R doesn't change, and now I only need one number to define where it is. So now you have one less number to deal with, which is great because we have too many numbers already.

**[00:33:21]** That doesn't make sense. It might tomorrow.

**[00:33:28]** Let's see, I'm going to skip some of this because it gets to. We're getting pretty mathy pretty quick and this is going to, I think make more sense once there's data to look at. But the other thing, I guess I'll say just by way of completeness, we've been talking about ways of measuring space and we also should talk about ways of measuring time. You hear terms like spatiotemporal coordinates, space, spatiotemporal calibration, whatnot. Remember, that's an O term.

**[00:34:09]** So spatiotemporal is just spatial temporal. It just means you're thinking about both space and time. And when you're looking at data like this, it's very common to see in 2D plots. Want to keep that? I don't think I need to keep that.

**[00:34:30]** You see, it's really common to see stuff presented like this where this X axis is time and then the Y axis is some measurement over time. So if we're thinking that Y is going to be, let's say it's height of my hand off the ground and then at time zero, we're going to measure it and it's one. So there we go, time zero. That's, that's me at one. And then we're going to wait, let's say a second and then we're going to measure it.

**[00:35:01]** Let's say it's now one and a half units off the ground. Then I have time one doing there. If I keep moving up, it's going to keep going up. And if I wind up doing this with my hand, then you're going to see dots doing like that. And then if you connect all those dots and you'll start seeing things like squiggles.

**[00:35:25]** And this is called a time series because it's a series of measurements over time. So this is a one dimensional measurement. So I'm just getting height and I'm measuring it once per time unit, which could be seconds. It could be. If it's a video like this, then it's going to be 30 frames per second.

**[00:35:41]** So it's once every 33 milliseconds. You know, if it's a microphone that records at 44 kilohertz, then it's once every one over 44,000, 44,000 over one or one over 44,000 seconds. But that's how you get measurements over time. And the important thing to see is you'll often see this presented as connect, as a straight, as a connected line. But that's not actually what you're measuring.

**[00:36:09]** You're only ever going to be measuring something at time intervals. You're going to be getting one measurement per time interval. And so this is what your data actually looks like. So we have to assume that the movement between the measured intervals is kind of like coherent, like what we'd expect it to be. And if we do that, then we can connect the lines and get a nice time series.

**[00:36:34]** But if this is one measurement every second and I'm doing this with my hand, then it actually doesn't look like that under the hood.

**[00:36:44]** If these intervals is like one every millisecond, then we can trust that if it's one every second, I could just as easily be doing this with my hand. And we only get these measurements every second. So if we interpolate we're going to be missing a lot of the story.

**[00:37:02]** Yeah. So that's time and I'll just say it just because it's on the. Things similar to space, time can also be thought of in two basic forms. Linear time, sort of like a stopwatch, and phasic time, which is like a clock where it resets to zero every circle through the available values that will become important in the future.

**[00:37:37]** Blah, blah, blah. If you care about calculus, if this is the position, the slope is the velocity because it's the change in position over time. If you do that again, you get acceleration. So velocity is the derivative of position, acceleration is the derivative of velocity. Then you go back with the integrals.

**[00:37:56]** That's all the calculus you ever need to know, as far as I care.

**[00:38:02]** Okay, so, yeah, so that's measurement, right? And we've been talking about these measurements in terms of kind of these like, abstract units. So, you know, singular sticks, whatever. Doesn't really. It doesn't matter.

**[00:38:20]** Like in the same sort of methods of plotting will work, no matter what it is that you're. No matter what units you're looking at. If you're measuring distance, we might use meters. If we're measuring temperature, we might use Celsius or Kelvin. If you're measuring weight, you might use kilograms.

**[00:38:37]** And the same sort of plotting representations will sort of work throughout.

**[00:38:44]** Now, this is a practical thing that you should keep in mind and will come up at some point in your future. But when we're talking about the sciences, there's rules about the units that we're allowed to use. We're here in America where we have things like imperial units, where it's like, you know, feet and inches and stuff like that, which are often kind of. People talk about them as like, these are bonkers, worthless measurements. And they kind of.

**[00:39:08]** There's a good argument for that. But the reality is that a lot of our imperial. The imperial.

---

### Chunk 5 [00:39:00 - 00:49:00]

**[00:39:00]** Like feet and inches and stuff like that, which are often kind of. People talk about them as like, these are bonkers, worthless measurements. And they kind of. There's a good argument for that. But the reality is that a lot of our imperial.

**[00:39:14]** The imperial measurements that we tend to use are based on very factorable numbers like 12 and 16, because it is easier to do that kind of math in like a home environment. Whereas metric is based off of tens, which is very good for things like decimal points and precision, but kind of harder to cut into. Even so, 10, you only get to cut into 2 and 5, whereas 12, you get 2 or 5. Before you start needing things like fractions, 12, you have 1, 2, 3, 4, 6 and 12. So if you're imagining that you're like a vendor in some medieval town and you have a bunch of weights that you have to bring to measure out your stuff, it's easier to have stuff weighed in terms of 16s and twelfths.

**[00:39:57]** Like things like baking and stuff like that is easy because it's really easy to cut things in half and by third and stuff like that. But in the sciences, we are required by law to use SI units.

**[00:40:11]** By law I mean convention. SI units stands for Standard Internationale. It's a French term that means international standards.

**[00:40:24]** And there are a set number of them. So here is the Wikipedia page, and these are all of the base SI units. For time we have seconds. For meters, we have for length, we have meters. For mass, we have kilograms.

**[00:40:38]** For electrical currents, we have amperes. For thermodynamic temperature, we have Kelvin. For amount of substance we have mole. And for luminous intensity, we have candela.

**[00:40:52]** For the most part around here, we're going to be mostly thinking about these ones. Center, second meter kilogram.

**[00:41:04]** Now this is one of the. Now we get to the first visual aid. Now, one of the cool things about the metric system is that a lot of the parts match up. So this is if this was 1 meter, which it's not, but let's pretend that it was. If this was one meter and this was one liter, which it claims to be, this is everything we would need to recreate the majority of the metric system.

**[00:41:33]** So the way that it's defined, a. A liter is a thousand milliliters. A milliliter is a cubic centimeter of water. In a cubic centimeter of water weighs 1 gram. So if you have a centimeter, and you better get a.

**[00:41:52]** Make a cube of that, of that shape and put water in that cube and measure the weight of it, that is defined as Defined as. But it's that cubic centimeter of water weighs one gram. If you were to then get a thousand of those things together, it would weigh 1kg and a thousand of those centimeters, cubic centimeters of water ccs would equal one liter, and one liter weighs one kilogram. So you get. It's kind of this fun sort of correspondence there where you get a lot of the.

**[00:42:25]** If you know how long a meter is and you have standardized water, you can recreate a lot of the units that we. We wind up using here.

**[00:42:40]** Yeah, yeah. And then the meter stick, it turns out traditionally it was measured as this.

**[00:42:55]** This stick in France. It used to be. There used to be, like, an actual stick like this, but I guess it, like, rusted away over time. So now it just represents some markings on a stone. We have since moved away from this method of determining a meter and now use it as we measure it in terms of the.

**[00:43:16]** Like, the distance that light travels. So I can't remember exactly how we used to do seconds, but it was something to do with, like, the period of a pendulum of a given length.

**[00:43:31]** And we now measure seconds in terms of the oscillation of a cesium atom because it's some sort of quantum thing. They oscillate at a very regular interval. And then we measured meters by the distance that light travels in so many oscillations of a cesium atom. And that measurement was basically designed as the time it takes for light to travel this distance so that we could be more precise with our more modern measurements and whatnot.

**[00:44:18]** Yeah. And then these. Yeah. So these are the only base units that we have to do proper science. So if you're ever doing a scientific study or measurement or you have to report numbers, you're not allowed to use inches, you have to use meters.

**[00:44:36]** You can choose to use things like centimeters and millimeters or cut kilometers or whatever unit, whatever number of zeros makes sense for your measurement. But you're not allowed to use inches or feet or. And if you're measuring mass, you're not allowed to use pounds, you have to use kilograms. And if you are. And when I say allowed, I mean like the scientific community has decreed.

**[00:44:57]** It's like if you're publishing a paper in a scientific journal, they should. If you were. If you present stuff with your numbers and things like feedback feet and pounds, they should send it back to you and say, convert these to SI units and send it back. And if they don't, then I would consider that to be a failure of the peer review. Process, which is its own conversation.

**[00:45:18]** There.

**[00:45:21]** Now a thing to notice about this rather terse list of possible units is why is just asking yourself, like, why is it so constrained? Why are these the numbers that we have? And the answer is, if you sort of drill down into it, like, these are what we consider to be like the short list of measurable things, everything that we can measure with our basic sort of tools can boil down to either these basic quantities or derived, more complicated combinations of these quantities. Quantities. So you have time, you have spatial extent, you have mass, we have electrical current.

**[00:46:09]** Kelvin temperature is just Kelvin is just Celsius, where zero is at absolute zero mole is some countable amount. And then candela is light. So earlier when we were talking about transduction and things like that in terms of environmental energies and things that the nervous system wants to take in in order for us to perceive something about the world. This is sort of a roundabout way of thinking about, like, if you're measured, if you're thinking about a sensory system and you're thinking about the energy that it absorbs, to give you a empirical estimate about what's in the world, you can think about how that, you know, how does sight, how does sound, how does touch, how does taste boil down to these basic units.

**[00:46:58]** You will also quickly discover that if you're trying to do anything of interest, you're going to. These are not really going to cut it for you for very long because there's just not much. You're going to have to eventually come up with new units to measure more interesting things. For example, if you want to measure something like velocity, going to measure how fast something is moving through the world. You can't do it with these alone, but you can do it by starting to squish some of them together.

**[00:47:27]** So with velocity, we can measure that in terms of meters per second by look, which is. The units are just meters per second is the same as meters divided by second. So every time there is a second, every time a second passes, you move this many meters, that's your velocity. This is. And so the SI units for velocity are meters per second, unless you're going very slow, in which case you might use millimeters per second, or if you're going very fast, you might want to use kilometers per second.

**[00:47:52]** But it's still going to boil down to these SI units there.

**[00:47:59]** And this is where it's going to start getting towards neuroscience. This is where we're rapidly approaching the topic of this course, which I probably should have sort of specified beforehand. So one of the main sort of nodules in that interest space of the class is biomechanics. Sort of a lot of y' all asked about biomechanics, like, what does that mean? And, you know, whatever, whatever conversations you had with the bot.

**[00:48:29]** Biomechanics is, roughly speaking, good old fashioned Newtonian physics, except as it applies to a wobbly biological system, typically one that has something like a musk, like a musculoskeletal system.

**[00:48:48]** And we will soon be sort of getting to the biomechanics and next week the data that we're going to be collecting in class is going to involve things like the. It's going to involve standing back.

---

### Chunk 6 [00:48:48 - 00:58:44]

**[00:48:48]** And we will soon be sort of getting to the biomechanics. And next week, the data that we're going to be collecting in class is going to involve things like the. It's going to involve standing balance. So things like, look at this wacky thing that I'm doing with my body. I'm carrying the majority of my mass, some hundred kilograms of salty meat, like a meter and a half above the ground, which is a really insane thing to do.

**[00:49:14]** And I can hold. I can even go onto one foot. And now that's. This is a lot of mass being supported on a couple of wiggly joints, some variable stiffness, electric strings called muscles, and a base of support that's like this big. If I ever come in.

**[00:49:30]** If I came in here with, like 200 kilograms of steel and I put it on something that was that small, raise it up this tall, that would be a very dangerous thing to do. But it's something that we do with our bodies. A healthy person will do it a million times per year. So if you. 10,000 steps a day, let's say 20,000 steps a day, because Yale undergrad, you walk a lot.

**[00:49:53]** 20,000 times, 365 is approaching a million steps per day. And so that is a period of time where the big mass of your body is being supported by above the ground, because your nervous system is electrifying and firing your muscles in the right way at the appropriate intervals to keep you from falling over. And so this is one of those things that we just. We don't really think about it, but once you start thinking about it, there's a lot going on there. And my particular approach to studying this stuff involves kind of like boiling it down to those first principles, measuring the behavior in those basic units of geometry and physics, and then trying to figure out what we can infer about the unmeasurable parts of that system, which is like the neural firings based off of the physics and geometry of the measurable components, which is like, where is my body at any given point in space?

**[00:50:46]** So this type of thing.

**[00:50:54]** Yeah. And so when we talk about things like biomechanics, we're talking about, like, the physics of biology, Physics as applied to organisms. In biology, the units we're going to start talking about are in terms of position. Where am I in space? Velocity.

**[00:51:16]** How am I moving in space? And then we start getting into sort of fancier terms like force. Like, what forces am I applying to the world? Like, if I'm standing right here and I push with my toes, I will tilt Backwards.

**[00:51:32]** If I push off the table, I'll go that way. So I'm applying forces into the world. And because I am a massive object putting force into the world, that will cause me to move. The units for force are Newtons, which is kilograms times meters times seconds squared. So that's kilogram meters per second squared.

**[00:51:56]** So if you remember, we had acceleration, so we had. Position is in meters, velocity is in meters per second. How many, what did your position change? How many meter in one second? How many meters did you change velocity?

**[00:52:14]** Sorry, acceleration is meters per second per second. So you're, you're speeding up. How much faster are you going a second from now versus right now? That's acceleration.

**[00:52:29]** And then if we sort of jump ahead to sort of Newton's laws, Newton's laws of motion, you. Force equals mass times acceleration. We've all heard that one before. And I'll leave this as an exercise to the reader, I guess if you sit down and if you do force equals mass times acceleration, if you do mass, which is in kilograms times acceleration, which is meters per second squared, you will get this unit, and we call that unit Newtons. And then if we sort of apply a force over a given distance, we have something we call work.

**[00:53:06]** Work is just force applied over distance. That gives you kilograms times meters squared times seconds squared squared. And that gives, and that is, we call that a joule, which is a unit of energy. Energy is the ability to do work, eg, the thing that is conserved. And we're talking about the conservation of energy.

**[00:53:29]** So if you. Another famous equation, E equals MC squared. If you do that units out, you will find that energy in that equation is, you know, E equals MC squared. So energy equals mass in kilograms times C, which is the speed of light in meters per second squared. You'll wind up with one of these things.

**[00:53:53]** So just a good example of how that stuff boils down to SI units. And once you've gotten to energy, we now have, now we're touching this sort of, this classic physics, things of the conservation of energy. And this winds up being a very good. Like this is a physics, a law of physics that if you're observing a system that's a closed system, energy is neither created nor destroyed, it just changes form. And that's a really strong belief that, that I have, that we have.

**[00:54:26]** Physics has been very racist. Physics has been very adamant that that conservation of energy is generally true. And so that winds up being a very strong assumption that I can use as a scientist to try to make sense of the wacky data that we're going to be measuring when we start actually looking at the weird, goopy complexity of a person moving through space.

**[00:54:49]** That doesn't make sense. It might later or it might not. We'll find out as a group.

**[00:54:56]** Yeah, normalized units, too, we can talk about.

**[00:55:02]** Yeah, So I won't say too much about this. I'll just say it in passing. But even though there are things. Even though, like SI units, use SI unit for things like kill for things like mass. If you're doing something like measuring a person moving through space and you're measuring like, this is me walking around and this is me, like pushing off the ground, and one second, you know, putting force into the ground, stuff like that, it might stop.

**[00:55:35]** It might like measuring everything in terms of kilograms starts to get annoying because it's like, oh, I'm 100 kilograms or whatever. I think I said 200. But it's not that, because we're thinking about. We're studying a person, so. So we can make our math and our lives much easier by just dividing all of our mass measurements by my personal body weight, like how much my mass is in kilograms.

**[00:56:02]** And so then we're no longer using things like kilograms everywhere. We're now talking about things like body masses, body weights or whatever. Weight is actually a measure of force, not mass. And so we can do, basically so that we would say we would normalize mass by the participant, by the subject, by the person's body mass. So now we have a one.

**[00:56:25]** When we're looking at our units, we get the number one, which is a very convenient unit because you can kind of. It makes the math sort of work out easier.

**[00:56:37]** Okay, so now we have.

**[00:56:44]** Okay, so we're going to. Now we're inching our way towards a human.

**[00:56:52]** The conception of a human as one of these approximations, not one of these. This is too complicated. We're going to stick with this.

**[00:57:01]** And we've gotten through all that spatial stuff, all that measurement stuff, all that unit stuff, and now we can start thinking in terms of physics. Now, physics is just. It's the sort of the math description of how objects move through the world. And there's all sorts of different layers of physics. And the layer that I tend to hang out in is what's called classical mechanics, where classical mechanics is basically Newton's three laws as they apply to simple sort of mechanical objects.

**[00:57:35]** So it's basically like cannonball physics.

**[00:57:40]** Now this is also a fun example of like a philosophy of science concept, which is that all of our theories are wrong at all points, at all points in time. So Newton's laws came about in, I want to say, like, 1700s or something like that. And he was trying to understand the motion of the planets. And so he came up with these simple rules of sort of how mechanics tends to work. And it was very useful.

**[00:58:15]** And it explains a lot of the physical world. It explains a lot of sort of simple objects in the world, and you can derive their trajectories through space using Newtonian mechanics, and it explains the majority of the planetary motions, but it doesn't do a good job of predicting the movement of a planet like Mercury. And it was actually so even in that day, if they applied the.

---

### Chunk 7 [00:58:30 - 01:08:30]

**[00:58:30]** Majority of the planetary motions. But it doesn't do a good job of predicting the movement of a planet like Mercury. And it was actually so even in that day, if they applied the Newtonian predictions for planet trajectories, it didn't. Mercury's orbit didn't line up with the prediction. So they actually postulated for a long time that there was another planet that between Mercury and Venus that could be making sense of the weird anomalies in Mercury's orbit.

**[00:59:04]** And that planet was called Vulcan, which is where that term comes from. Eventually, time passed and such a guy as Einstein came on the picture and sort of started kicking out all these wacky ideas around relativity theory. And it's much harder math, but if you apply that theoretical framework to the emotions of the planet and you now account for the fact that the sun is so massive that it warps space time and all that kind of wacky nonsense, now all of a sudden, Mercury's orbit starts to make sense, and you no longer need to posit the existence of some of some unknown, undiscovered planet called Vulcan. And so we know from measurements that Newton's laws of mechanics are not an accurate representation of the physical universe that we inhabit. We also know that in any location that we tend to care about as human beings on a planet, the accuracy that you get when you use Newton's laws is like nine decimal.

**[01:00:08]** It's like decimal place, like nine, ten decimal places out. So you start like, the difference between the prediction of this ball's motion in Newtonian mechanics and the same prediction in relativistic mechanics is so far below our ability to measure the position of a ball in space that it just doesn't make sense to use those numbers. You only need things like relativity theory when you start looking at things like planets and on the scales of, you know, stars and stuff like that. So we still use Newtonian mechanics for almost everything that we do in our daily lives, even though we know that that is not as accurate as something like relativistic physics. And there's a lot to be said there, but let's keep moving.

**[01:00:58]** So, yeah, so Newton's laws, there's three of them. The first law is a body in rest or in motion tends to stay in rest or in motion. So that's inertia. Things in motion tend to stay in motion unless acted upon by a force. The second one, arguably my favorite, is force equals mass times acceleration.

**[01:01:19]** Or if you're in rotational space, it's torque equals moment of inertia times angular acceleration. But don't worry about that. So F equals MA is a very, very useful equation, basically. So if you look at me, I am a mass. My mass is not changing.

**[01:01:37]** So. So let's ignore the M of that because it's not doing anything. It's a constant. So let's divide by my body weight, and then we have force equals acceleration. So I'm not moving, I'm not accelerating.

**[01:01:52]** That means that the sum of forces acting on my body has to equal zero. If it didn't, I would be moving. Now. I'm going to. So all the pluses and the minus have to add up to zero in order for that to work.

**[01:02:12]** And you can see if I soften my. Let me do this backwards. The third law is for every action, there is an equal and opposite reaction. So you have an action and a reaction force. So here I am standing.

**[01:02:31]** Look, we're officially doing neuroscience. That's me. I'm standing, and I'm standing on the ground. And I weigh one body mass, and I am being pulled down by this horrible planet at a rate of G. If you drop me from a certain. From a place up high, I would accelerate downward at 9.8 meters per second squared.

**[01:02:55]** Squared, let's call it 10.

**[01:03:00]** And that's always happening at all times. So this force, So G is 9.8 meters per second squared.

**[01:03:15]** So that's the A and the F equals ma. And so I'm being pulled down by that amount, but I'm not moving. So there must be something else pushing back with exactly the same force, and that's our good friend the ground. The ground is a very useful object. It allows us to complete most of our goals.

**[01:03:39]** And as I am pushing, this is the action. I am pushing into the ground with mass times gravity force. And the ground is dutifully pushing back with exactly negative mass times gravity force. Great. If I ever decide to break this equation, I can push.

**[01:04:00]** If I decide to push off the ground with more than that, more than gravity is pulling me, then I can do such a wacky thing as jump. So I put force into the ground. It's more than I weigh. I briefly airborne, and then gravity pulls me back down. And that winds up being important for a lot of stuff.

**[01:04:27]** Okay, I need to speed up here.

**[01:04:40]** Okay.

**[01:04:46]** Okay. I think I know how this is going to go.

**[01:04:51]** So great. So this is your preview of high level human movement neuroscience. But we got to do a little more work before we can get into the meat there. Let's go back to thinking about simple spheroids. Such as brightly colored juggling balls.

**[01:05:25]** So when you're doing empirical studies, you're doing empirical measurements, you always have to make assumptions. That's always going to be a thing that you're doing. You have to make assumptions that your senses aren't lying to you at all times. You make assumptions that when you read papers that the people who did that study are not actively lying to you and falsifying all their data, you have to make assumptions about.

**[01:05:51]** And every time you make an assumption, you get a little bit more predictive power.

**[01:05:56]** So if I'm trying to measure my body moving through space, I know that this is like a wobbly meaty thing, and I know that the distance between my elbow and my wrist changes ever so slightly because I am made of squishy meat. But if I just assume that that's just not happening and that I'm actually composed of rigid bodies that don't change length, then I get a lot. I get a lot. My math gets easier because now I don't have to measure the length between these things. I only have to measure the, the angles between them.

**[01:06:33]** And so those assumptions that we make. The only measurement you can make without making assumptions is that you are having a conscious experience at this exact moment. And that's just not very useful. So this is where we come back to what I was talking about earlier, where the idea of a conservation of energy winds up being one of those very, very powerful and very, very useful assumptions that can really get us a lot of the way towards understanding the things that we care about, the desiderata of our research goals, the things that is desired in our research activity.

**[01:07:10]** Because again, looking at this object, there's a lot, like if my desire is to understand something like standing posture or God forbid, locomotion, there's a lot, there are many, many aspects of that question that I cannot measure empirically. I, I just don't have the technological capacity to measure the firing in my cerebellum or the stretch forces in my muscles. I can't measure that. But I can measure things like the sort of the stick figure position of my body 33 times per second using something like a motion capture system that I built over time in my house. And so by using that thing that I can measure in these certain assumptions about conservation of energy, I can start to have, I can start to try to understand like the, what we'll just call the technical term is the fiddly bits.

**[01:08:02]** And this is going to fuzz out, I think, in a bit that will sort of like, will pick up again probably around here next week. But I'm going to get through it all so that at least you will have experienced it at least one time.

**[01:08:16]** So. So when you're thinking about, when you're doing sort of a mechanical analysis of a person, you want to think about what are the forms of energy that are relevant to this task that I'm at looking.

---

### Chunk 8 [01:08:17 - 01:18:14]

**[01:08:17]** So when you're thinking about, when you're doing sort of a mechanical analysis of a person, you can. You want to think about what are the forms of energy that are relevant to this task that I'm looking at here. And in this part of the class, we're just measuring movement, the motor control part. We're not looking at perception, we're not looking at vision. So we get to ignore things like light and we get to focus on just the simple physics of being a massive object in a world that has such things as ground and gravity.

**[01:08:53]** And so the forms of energy that we can really measure and we can really care about are mostly potential energy and kinetic energy. And there's a lot of forms of potential energy. The most obvious and easy one is graduation gravitational potential energy, which is the distance. So this is the ground, we'll call that the height is zero. We got to do that.

**[01:09:18]** Doesn't matter where we are horizontally, but it does matter where we are vertically. And so potential energy, gravitational potential energy equals mass times gravity times height. So which again, mass is kilogram meters per second squared. Height is again in meters. You can do the math and figure out that this, the units will be Newtons when you do that.

**[01:09:42]** And so the potential energy is basically a measurement of if I had this object and I dropped it, the force that it would. If I put like a scale underneath it, the force that it would put into that scale is this many Newtons.

**[01:10:01]** Yeah. Other forms of potential energy which we're not really going to talk as much about are things like spring potential energy. So if, like stretchiness of a spring, also chemical potential energy, which is like food and bombs and gasoline and stuff like that. A lot of the sort of, the deeper level biology, you can start getting into chemical potential energy. And that's when you start seeing things like the ion charges don't line up, so there's X that's you start measuring into the coulombs or whatever that electrical unit is.

**[01:10:28]** So that's the potential energy is like a mismatch between the way that the world would really prefer to be and the way that the world currently is. So the low energy state, if I wasn't holding this, the low energy state of the world would be this on the ground. And so if I let go, then I know how much energy is going to be hit there.

**[01:10:51]** The other one to think about is kinetic energy, which is the physics of movement. So if you were to measure. So kinetic energy is 1/2 kinetic energy, 1/2 meters MV squared, 1/2 MV squared at mass is kilograms, velocity is meters per second. Do the math. I promise you it will turn out to be Newtons because it's a measure of force.

**[01:11:21]** And it is the amount of force that would be hit. Like if I were to drop this, the instantaneous moment before it hits the ground, it would be having.

**[01:11:33]** It would have a certain amount of kinetic energy. How much kinetic energy would it have? It would have exactly the same amount of kinetic energy as it had potential energy before I dropped it. And if you add these things together, do I not sound too bad yet? And yeah.

**[01:11:58]** And so using that type of analysis, potential kinetic energy is where you get things like the parabolic flow flight of the object through space. Because as it leaves my hand, it has the instantaneous moment that it breaks contact with my hand and it's in free flight. It has a certain amount of kinetic energy. It has the most kinetic energy that it's going to have for this entire trajectory has maximum kinetic energy, minimum potential energy. And it goes up through space.

**[01:12:35]** The kinetic energy, it slows down as it goes up and it gets higher. So the potential energy increases until it reaches a point where it's at the apex. And the potential energy is now at the max because it's as high as it's going to get. The kinetic energy is at the minimum because it briefly has zero velocity when it goes from moving up to moving down.

**[01:13:03]** And then it's going to come back the other way. And when it gets right, the moment right before it hits the ground, hits my hand again, it will have the same amount of kinetic energy as it had when it started. So you get this nice sort of trade off there. So this is a much. So when I talked about things like transduction for vision or for olfaction or for somatosensation or things like that, we're talking about a transfer of energy from one form for light, let's say candelas, into another form, which is a pattern of neural activity measured by voltages and electron ion mismatches and stuff like that.

**[01:13:45]** There's. There's so much that's not measurable in that conversion. But physics would have us believe that if you could tally up every ion and every sort of quantum of energy, the math of that conversion would match. Would work out as perfectly as the cannonball physics of simple ballistic motion does. Because this transition from kinetic potential energy is also transduction.

**[01:14:13]** That is also a transfer of energy from one form to another.

**[01:14:19]** Yeah, we're ignoring. If I was a bird, I could flap my wings and push against air sufficiently to get a reaction force to sort of counteract gravity. If I, if this was a pogo stick and I sort of compressed it and then threw it, then it hit, then it would have a bunch of spring potential energy that when it hit the ground it might bounce additionally. But if we assume the simple rigid body physics, then that kinetic and potential energy is going to sort of have this nice conservative trade off. This will become important later.

**[01:15:03]** So now we get to my favorite part, which I will only be just a little taster. And then we will talk at about this at length next time. And that's the concept of the center of mass. The center of mass is a term in physics. You've probably heard it in some.

**[01:15:23]** It comes up a lot in like sports and especially anything related like gymnastics and balance, stuff like that. You hear people talk about the center of mass as like the position of your body run out of time. Here, I'll just do it.

**[01:15:45]** So the center of mass is the average position of all of the.

**[01:15:58]** Is the average position of all of the objects, of all the components of the larger object. So if I were to take this tube and cut it up into 1cm long sections and then took the position of those sections relative to a zero point or any zero point and took the average of all of them, it would be in the middle of the thing and that is the center of mass. And it turns out that when you're supporting something above the ground, you do it by supporting the center of mass of the thing. So if I were to hold it over here, then the center of mass would fall and it wouldn't stay on my hand if I were to put a weight.

**[01:16:48]** So these are like ankle weights. They look like they're from like the 90s. I also found them on the street near my house. There's like a place for people in the neighborhood just like put sort of like garbage before, like before it goes away. And I found these and they're sort of useful for this.

**[01:17:05]** So by putting this, it weighs like a pound, I think so like half a kilogram. And so now before it was on here, this thing was of uniform density. So the center of mass was in the middle of it. Now it's not of uniform density. So the center of mass shifts to here.

**[01:17:25]** Now this is the center of mass of the system. So now when I want to support the system, I have to take into account the shift in density of all the things that are a part of that system.

**[01:17:40]** And so if we really wanted to, we could determine how much this thing weighs in units of stick by measuring the distance between this balance point and. And the center of the stick, which is where we would balance it on if it was symmetrically oriented like that.

**[01:18:01]** I don't want to, but we could.

**[01:18:05]** And that concept of balance as the relationship between.

---

### Chunk 9 [01:18:01 - 01:28:00]

**[01:18:01]** I don't want to, but we could.

**[01:18:05]** And that concept of balance as the relationship between the center of mass and the base of support is something we're going to talk about a lot.

**[01:18:27]** Yeah, but, yeah, so similarly. So we talked a little bit about the concept of reductionist approaches to scientific studies, which is like trying to nail down the problem I said before of like, I want to measure this thing that I care about, but I don't have the ability to measure all the parts of it with the precision that I need to do that. One approach to dealing with that problem is to narrow your focus. And rather than trying to explain the entire complexity of the thing that's moving, which is not available for empirical measurement, you can look at a smaller and smaller and smaller piece of it. And so instead of looking at the whole body, you might sort of look at just the movement of like a single joint or something like that, or the single arm or something like that, and keep that same sort of full level of fidelity of still thinking about this weird shape in terms of a thing that has all of these joint angles that can define its position at a given point in time.

**[01:19:35]** But even for something like this, which is a massive simplification of a human, this is still a pretty complex object, physically speaking. There's still a lot of joints that can vary, and you have as many degrees of freedom as you have joints times two or three, depending on how you count. So to define the position of this kinematic object in space requires a lot of different numbers, and that's going to be sort of hard to deal with. The other approach is to just simplify down the system that you're looking at into a massive oversimplification and try to do that in such a way that still allows you to say things about the system as a whole. So like, and that's basically what the idea of the center of mass is.

**[01:20:22]** So rather than thinking about this whole complex thing with all the joints and all the muscles and all the blood pumping and all the sort of the biological realities going on there, we can instead condense it down into a simplified system. So this is something I made some years ago, and this is just showing a guy doing a handstand. It's a French parkour vista named Simonster. And the X here is his full body center of mass, which is measured as the weighted sum of each of these body segment. So the segment of the forearm, the upper arm, the head, the chest, the legs, we take the average of all those positions weighted by the mass of that Object.

**[01:21:19]** So, like the forearm weighs a lot less than the legs, for example. This is the position that you get. And then if you measure the limits of the base of support here as the distance between the tips of his fingers to the heel of his hand, which those are the places where you can put force into the ground, the center of mass always stays within that space. So you can know that even though there's a lot going on here biologically from a physics perspective, that you can define the task of balance using these sort of very hyper simplified models of the body, which take the entire complexity of a human person and boil it down to a singular point mass, which in this case is in two dimensions, but it could be in three dimensions. And we have now simplified the world down to a place that starts to feel more tractable.

**[01:22:09]** I can handle this many numbers. I can kind of handle this many numbers, but not really. But this is a place where, if you, by the way, on the list on the notes, if you click on this. Where is it?

**[01:22:31]** Com gifs, it goes to a link to a bunch of those types of animations that I made. We'll talk about them more later. Oh, do that.

**[01:22:42]** There we go.

**[01:22:48]** Yeah. And so.

**[01:22:51]** So you can reduce down this complex object of a human down to a singular point mass. And physics has told us, I believe it's like the finite element theorem or something like that, but I'm not really 100% sure on that. It basically says that things that you say about the center of mass of a system are true to some extent of the other object of all the objects in that system. So talking about the center of mass of that person is a valid approximation of what the full picture would be if I was measuring every single sort of cube of his body at the same time. You're obviously going to be losing a lot of information.

**[01:23:36]** So if I'm only thinking about where did it do the shimmer, this one's another wacky guy. So I'm boiling down this guy's entire body to this singular mass. I can no longer really say things about the joint angles or the forces at the elbow, stuff like that. But I can determine whether or not he's in a stable regime or an unstable regime. And I can measure things like what's happening at the physics level when he shifts hands from one position to the other.

**[01:24:06]** And I can use this belief about the physics of his body to start trying to infer what some of these wiggles and movements actually mean. So, like, when it. Why, like, without this sort of center of mass analysis, it might be hard to explain why his arm is out here. They might not have much to say about that. But when you're thinking about it like this, it becomes very easy.

**[01:24:28]** Like, he sticks his arm out so that his center. Like, if I move my arm and leg like this, the average of them keeps my body over my foot. And I can do this, but I can't. I can't do that. It's.

**[01:24:45]** Anyway, you'll figure it out. I'll show you visual representations of this once you actually get the numbers next week.

**[01:24:56]** Right. And then.

**[01:25:01]** Yeah.

**[01:25:04]** And you might ask the question of how do we do these measurements? How do we get these numbers? And so how do I know where to draw the segment center of mass for his torso versus how? Like, what percentage of a body weight is a forearm? Like, how do you get those numbers?

**[01:25:25]** What. Well, it turns out we have these lookup tables. This is called anthropometry.

**[01:25:49]** Yeah. And these are just. This is statistics. Oh, wrong way.

**[01:26:05]** So these particular lookup tables come from a guy named David Winter. This is copied from a textbook of his from like 1995 or something like that. And it shows these measurements of the shoulder is 0.129 h, where h is the body height. And so he. And then these are the lookup table for these segments.

**[01:26:34]** So the forearm is defined as the distance, the space between the elbow axis and the ulnar styloid, I guess, is here. Here it's.028 of an M, which is a body mass. And the center of mass is 0.436% of the way from the proximal joint, which is the one towards the middle, towards the distal joint, which is the one that's farther away. So if you add these two numbers up, they add. They equal one.

**[01:27:04]** So you kind of. You can use these numbers to calculate these values. And these numbers were basically statistics of they chopped up a bunch of dead people and measured. It was like Air Force research, I believe. And there's a lot of so.

**[01:27:31]** And they were all like older men. So there are other newer tables now that have people of different ages and, you know, different genders and things like that. In the end, it doesn't super matter for a lot of, like, the numbers are slightly different. You know, women have a lower center of mass than, you know, blah, blah, blah. But for the levels of analysis that we tend to be looking at in terms of like, this type of physics or like, you know, where your.

**[01:27:58]** Where your body mass is going to.

---

### Chunk 10 [01:27:45 - 01:30:22]

**[01:27:45]** A lot of, like, the numbers are slightly different. You know, women have a lower center of mass than, you know, blah, blah, blah. But for the levels of analysis that we tend to be looking at in terms of like, this type of physics or like, you know, where your, where your body mass is going when you're moving your feet around the distances, the differences between those estimates for the different sort of categories of human are just not. They're below the level of precision that we have for our measurements for most cases. So I tend to just keep using these because, you know, it's available and I don't have to.

**[01:28:21]** If you, if you look up papers on anthropometry tables, you'll find all sorts of new stuff about, oh, we chopped up a bunch of athletic people and non athletic people and older people and younger people, and da, da, da, da, da. And great, good job for them.

**[01:28:42]** Yeah. Okay. Pendulae. Pendulae are my favorite thing. We'll talk about them next week.

**[01:28:51]** Balance, we'll talk about. And then this is color light.

**[01:29:04]** There we go. And then someday we'll also talk about projective geometry, which is the same. This is what cameras and vision and stuff is. And they are.

**[01:29:16]** It's the same math, except this one is about light instead of physics. But it's the same kind of idea. You project stuff in this whole thing and then eyeballs and stuff like that. So, okay, that was a lot. Hope you got something out of.

**[01:29:33]** Will not be on the test. There is no test. It's just, it's much more. Try to internalize it, try to conceptualize it. Try to think more about the concepts than the details and think it's better to think about, like, how would you recreate this story when you're telling it to someone else than it is to remember anything specific about what I said?

**[01:29:52]** Because notice a lot of it was just kind of like reconstructed from first principles. And. And so it's useful to be able to do that. So try to tell the story to someone else that you know later. And then when you hit parts, it's like, wait, how did you get from there to there?

**[01:30:06]** Think about it. Ask those questions. Okay, cool. Thank you. We'll talk more about this next week.

**[01:30:13]** And we'll talk about pendulae, which is the best pendulums. They're my favorite. We'll talk all about it. Okay. Hi.

---
