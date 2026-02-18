# Transcript: 2025-02-12-HMN25-05 - State spaces, phasic jumping, and FreeMoCap data analysis

## Source Information

- **Source Type:** Local File
- **File Path:** `C:\Users\jonma\syncthing-folders\jon-alienware-pc-synology-nas-sync\videos\video_eater_downloads\playlists\[2025-01-Spring] Neural Control of Real-World Human Movement\2025-02-12-HMN25-05 - State spaces, phasic jumping, and FreeMoCap data analysis\2025-02-12-HMN25-05 - State spaces, phasic jumping, and FreeMoCap data analysis.mp4`

---

**Total Duration:** 01:33:53

---

## Full Transcript

### Chunk 1 [00:00:03 - 00:09:55]

**[00:00:03]** Okay, so catching up. We are here in week five and slowly catching up to reality, I suppose.

**[00:00:16]** So last week we recorded some motion capture data involving standing posture and jumps and repeated jumps and that whole good stuff stuff. And then last time on Monday, we looked pretty closely into that data, focusing on the sort of like the epistemological chain, like the, from, like the, the pipeline from the empirical measurement represented by the video recordings into the sort of like increasingly more complex analyses and sort of processes that produce the data into a format that we could actually start to analyze and understand and sort of make some insights about the thing that we care about, which in that case was standing posture and looking at the differences between the supported versus the unsupported thing and sort of trying to wrap our head around that way of looking at data.

**[00:01:17]** And I hope that was kind of like generally helpful both for like, you know, this specific type of data, but also like that same kind of thought process will be true for any kind of scientific investigation you want to do like any. At some level, if you're looking, if you're trying to derive knowledge about the world on the basis of some kind of empirical measurement, it's going to have some kind of a process that's similar to what we went through last time, where there's going to be some tools that is taking some kind of a measurement from the world. That measurement will be some super basic sort of like some energy in the world that gets transformed into some quantity that is easy for us to sort of record and take a record of. And then generally speaking, that data will not be something that you can just look at and then sort of derive anything interesting about the world. There's going to have to be some kind of a process of calibration and computation and analysis and da, da, da, da.

**[00:02:14]** And at the end of that sort of sometimes very long computational pipeline, you'll be looking at data that will be represented in some way and you'll be trying to generate something resembling knowledge about the world from looking at that. So I think the main point I wanted to make last time is just to think about each stage of that process as a sort of a chain of epistemological grounding where your ability to trust the outcome of that long pipeline is only as strong as the weakest link in that analysis. So if there's some like weird magic step in step 12 of 255, even if every other step in that process is super grounded, truth preserving, like old school reliable computation, if there's some weird step in the Middle there. Everything after that is no longer reliable in terms of its ability to track reality in the way that we want it to.

**[00:03:16]** So today I'm going to do sort of two things, which is historically a mistake, but I think we can do it.

**[00:03:25]** I want to sort of look at, just go back into the data and look at some of the data that we didn't look at, which is the last condition of the repeated jumping, and show an analysis of that data that have generated in previous years and can look at here to make a couple of different points. Both just sort of like that, the different structure of a movement that has that kind of like repetitive phasic kind of aspect to it. So as opposed to being standing posture, which is a continuous control problem, or like a big singular jump, which is like a discrete sort of behavior, the repeated jumping has this kind of phasic thing where it's sort of each stage, I see you, each stage sort of sets each step in the phasic process, sets you up for the next iteration. And so there's just some different ways of analyzing data like that. And there's many, many, many aspects of the natural world that has that sort of property.

**[00:04:33]** Locomotion running is one of them also like your circadian rhythms and you know, like the seasons, a lot of things have this structure of kind of like a pattern that repeats itself in a way that's sort of like related to linear time, but not directly related. So like the seasons is a good example of that actually. Like the year counts up, so 24, 25, 26. But winter comes at its own sort of rate. And we'll just talk a little bit about that.

**[00:05:06]** Hopefully that won't take us all that long. And I want to leave the last sort of optimistically hour, but possibly less to do a little bit of small group work, which I will sort of try to relate to the initial part where that will be forming into small groups of roughly 3ish folks with the intention of sort of doing some work with the bot to find a paper which can complement the paper that you've already chosen for your chosen topic, and specifically trying to find papers on a similar topic, but are that are sort of distinct in some interesting way. So you can start looking at sort of different perspectives on your chosen topic.

**[00:05:57]** Yeah. And then I think that will sort of lead us nicely into kind of like the second half of the semester. And by the end of next week I want to kind of be getting into the space where you have like a more grounded sense of what the the final poster project is really going to look like and sort of, you know, have the ability to start hypothetically making movements in that direction. Realize that there's kind of some weird timing here. But don't, don't stress too much about those things.

**[00:06:23]** We'll make it. We'll make it work.

**[00:06:31]** Right? Yeah. Anyways, just realize that. Yeah. Poster do is look.

**[00:06:37]** It's less of an exclamation point than it appears on the page. This upload poster, this is really the hard deadline. Like you have to upload your poster so it can get printed in time for whatever. Everything before that is a little more squishy. I try to make this do before Spring bake so that you kind of like free from that responsibility.

**[00:06:54]** But there's a little bit of like weird squishiness there.

**[00:07:00]** Okay, cool. Everyone cool with that so far? The assignment anxiety? Yeah. Good.

**[00:07:07]** All right. And there will be a sort of. We're going to call it an exam for bureaucratic reasons but it's really just going to be another one of these like directed bot based conversations where specifically I'm going to be extracting all the like the sort of philosophy of science kinds of aspects of the past several lectures in terms of like units and recordings and empirical this and that's. And you will have a directed conversation with the AI about connecting those types of thoughts to the particular domain that you've chosen to study. I can't imagine any of you have chosen a topic that won't have some relationship with units and measurement and methodology and stuff like that.

**[00:07:48]** So you know, it's not going to be something that you can it. We're going to call it an exam but you can't really get a grade on it because I think it's unethical to use AI to grade things for a lot of reasons. But we will. Yeah, we'll be fine. Okay, so I have to start up discord, which could take a second.

**[00:08:15]** I did move the recordings from the other week into a Google Drive folder so you can download them if you so choose. I'm not going to really going too deep into that aspect of it, but in the server, in the links and resources, there's a Google Drive link that will take you to a page which should show something if this loads. Am I on the Internet? Yeah. So these are all the recordings in some strange order.

**[00:08:51]** Yeah, maybe a different. Maybe later in the semester I'll talk a little more about how to get it and run it. But for now you can kind of the only recommendation I'LL make is if you want to look at any of these on your computer, your best bet is to download the entire folder. So don't download bits and pieces. Download the entire folder, a given recording, and then open up the blend file with Blender and poke around.

**[00:09:20]** And if you don't know how to use Blender, there are many, many, many, many, many tutorials online on how to do that, so you can figure that out on your own.

**[00:09:31]** Okay, so with that said, why do you think it's so hard, buddy?

**[00:09:50]** Let's take a look at this repeated jumps recording.

---

### Chunk 2 [00:09:45 - 00:19:42]

**[00:09:45]** Why are you thinking so hard, buddy?

**[00:09:50]** Let's take a look at this repeated jumps recording.

**[00:10:03]** So if you recall. Let's see here.

**[00:10:13]** So again this is going to come up later. But again noticing that the initial data here is broken garbage because I am not in the scene. Everything gets. This is a very common way that data breaks when you're trying to do 3D stuff with bad input. It just all gets squished into a singular line.

**[00:10:32]** So this will come up later. Just notice that the data starts out as garbage and then it sort of snaps into place when whenever I walk into the scene and I stand here in that sort of calibration sort of pose and I then start bouncing up and down and if we hide this, we can look at that and we can grab. I think we can do network.

**[00:11:24]** I never know how to make that work. It's fine. Okay, so grab you. We're going to say round frame. We're going to do two seconds before and not after and then calculate the whole recording.

**[00:11:40]** Then we're going to hide the keyframes, show a custom color, make it, make it pink and. Yeah, and so there we go. So here I am jumping for some amount of time and I guess let's get to that when we get to that and let's look at the graph editor. Let's turn. So with the standing posture stuff I was, we were looking at like the projection of the center of mass onto the floor relative to the base of support.

**[00:12:29]** And so in that for that task the height of the center of mass is not relevant to that analysis. We only really care about where I am, where that, where that center of mass position is on the ground plane which we're going to define as xy. And then Z is going to be up this world. So that balance task, X and Y are relevant dimensions. Z is not a relevant dimension for the model of standing that we're looking at.

**[00:12:57]** If we were looking at a more complex model of standing that had things like joint angles and stuff like that, we might care about the Z axis. But because we're living in a sort of hyper simplified world, we basically get to throw away the height of the center of mass. And now we boil down this entire, entire complex being data object into two singular points.

**[00:13:24]** With something like jumping it's the opposite. When I'm jumping around, we're thinking about that as something like I'm putting force into the ground that is fighting against gravity. And if I put more force into the ground than I weigh, where weight is measured in Newtons So it's mass. My body mass times gravity gives you my Newton force. If I put more than that force into the ground, I will temporarily leave the ground.

**[00:13:51]** As gravity sucks that energy away from me, I will reach a certain height and then come back to the ground. So that behavior is defined relative to this inertial reference plane. And specifically, inertial reference frame is basically CO code for the ground is at zero and some direction points up. And so that jumping behavior, if I'm jumping here or jumping there, or jumping there or jumping there, it's the same process either way. So for this behavior, for this task, we actually don't care about the x and Y axis and we only care about the Z axis, the vertical axis.

**[00:14:30]** If this was a different task around going from stepping stones, if I'm jumping, if the task said jump in place and don't shift around, then the ground plane becomes important. But if we're just thinking about the base level physics of it, the physics are the same in one part of the room or the other. All of which is basically a long winded way of saying that I can turn off the x and Y data from this viewer and normalize that it's not actually what I wanted. And oh, what is going on there?

**[00:15:09]** Not sure why that looks like that, but okay. And we get this. Nice. So this data here, so this shows the sort of vertical motion of my center of mass. So the x axis here, hypothetically is meters.

**[00:15:42]** So from. Except it's upside down. Why is it upside down? I don't know why it's upside down.

**[00:16:00]** These units are confusing me a little bit. I think it kind of loses track of some of that because it's. This is negative 0.85 and this is negative 0.9. So that's kind of down. But this is.

**[00:16:20]** Yeah, that says, this one says 1.43 meters, which is probably about this high. This is 1.8. So let's call this 1.4.

**[00:16:34]** I could probably jump. That seems right. So I don't know why these units are happening. This is sort of a thing that I've noticed, like Blender is not a scientific tool. Blender is an animation artistic tool.

**[00:16:47]** So sometimes things like, oh, let's make sure all the units are correct. They're a little more fudgy on that than you would expect from a scientific tool. But this is sort of a, it's more of a cultural thing than anything real. Like in order to do this type of stuff right, they have to be doing the math correctly and they have to be keeping track of units here and there or the other. But the user base of this software are more concerned with just like the general shapes of the data and sort of.

**[00:17:12]** And things were like, oh, these numbers don't actually match those numbers. It's first of all almost certainly like a setting that I'm not doing properly. But a scientific tool wouldn't do this. An artistic tool would. Luckily, in this context, I similarly don't really care about the values, I only care about the shapes.

**[00:17:31]** But this is sort of a nice opportunity to look at how this non dimensionalization, so dropping the X and Y axis, the X and Y data from this plot makes it so that the data becomes this much simpler one dimensional time series. Because the X axis represents time, specifically it represents frame number where if you wanted to calculate the clock time, we could convert that using our knowledge of the frame rate and that stuff like that.

**[00:18:10]** But if you'll notice as I'm sort of so down here at the bottom of the jump, like jump up in the actual 3D data, I'm kind of shifting around in space. Like I'm not bouncing over the origin the whole time I'm shifting around, my X and Y values are changing. But we don't have to care about that if we're just looking at the height. So in terms of the mechanics of the situation, we could convert this into Newtons by just multiplying, by getting the potential energy here and just saying, okay, the Z height is height and then mass doesn't change, gravity doesn't change. So this, if we wanted to convert this plot into a plot of the potential energy of the physical system, we could do that by just basically scaling it by my mass and the gravity on Earth.

**[00:19:04]** At which point again, if we did that, these numbers would change, but the shape would not because there's nothing interesting happening there.

**[00:19:14]** So there's a lot of things that we could look at here. If we had more time and research funding and stuff like that.

**[00:19:26]** One of which would be like, let's assume if we were like sports biomechanists and we wanted to know about the force production that leads into jumping, we might want to look at how this sort of phase on the ground. Can I zoom in there more?

---

### Chunk 3 [00:19:30 - 00:29:29]

**[00:19:30]** Mechanism. We wanted to know about the force production that leads into jumping. You know, we might want to look at, you know, how this sort of phase on the ground. Can I zoom in there more?

**[00:20:02]** So here I am up at the top of the jump.

**[00:20:06]** Then as I come down, like so, looking at the video back there, you can tell right around there. So I'm off the ground. And then this is around. This frame is where I hit the ground. No, wait, no, that's not right.

**[00:20:31]** That's the opposite.

**[00:20:38]** Okay, right around there. So this whole phase here where I'm on the ground, this first part you can see I'm kind of. I'm compressing, like, I have a lot of energy in, like, mechanical energy in the system. It has to go somewhere. And so I bend my legs.

**[00:21:02]** I'm not. I don't have like EMG recording the muscles on my quadriceps and hamstrings or whatever, but they're on. I promise you that they're on because I don't collapse to the ground. My legs just kind of deform a little bit and then I push off and I come back into. I go back into the air.

**[00:21:20]** So this is where I think we've come across the term, like neuromechanics before. This is kind of at that level. We could ask questions at that level here about like, you know, how efficient am I as an organism at taking advantage of the fact that the force of gravity is preloading my muscles with all this, like, nice spring force. Then how, how efficiently do I utilize that spring force in order to launch myself off the ground for the next jump? Because clearly when I push off, I am using, you know, something from on high is sending the signal down to trigger a muscle firing that will allow me to bounce off the ground.

**[00:22:01]** But unlike that standing high jump thing, I don't have to generate all that force on my own. I have some of the force from the previous jump preloading my limbs so that when I actually take off in the next jump, the force from my muscles is going to be presumably sort of like efficiently combined with the spring force from the previous jump, which is also. It gets very complicated very quickly.

**[00:22:33]** So, yeah, like, so we could look at sort of, you know, how efficiently I'm doing that translation from one jump to the other. We could also look at things like fatigue. So if we were looking, if we expected that over the course, like, these jumps look pretty similar, but it might be the case that if you looked at the time between the peaks, might get longer as I get more Tired. The peak height might get a little bit less as I get tired. I wasn't really pushing myself all that hard.

**[00:23:04]** So it wasn't a particularly long recording. So if those numbers are there, they might be more subtle.

**[00:23:14]** But there's a lot of sort of potential analyses and potential kind of just ways of considering this data that would not be sort of possible. It's only possible because of the sort of repetitive aspect of it. And again, like I said before, the stuff for bouncing in place is kind of like a proxy for what it would look like if this was like, if I was running or jogging or walking or something, one of those kind of repeated sort of behaviors there.

**[00:23:48]** And again, just kind of like highlighting. While this data in the middle looks nice, just looking at what bad data looks like, sort of. Because one of the real advantages of this type of data is it is directly coupled and tied to, like a thing that we have very, very strong intuitions about because it's. It's human movement, it's video. Like, we kind of have some sense of what that data looks like.

**[00:24:14]** If this was a measurement off of an accelerometer, if it was a measurement off of mass spectrometer or something that is less tied to our kind of like the part of the world that we tend to operate and have a lot of intuitions about, it might not be as obvious when the data is good and viable versus when it's being sort of busted out because of some methodological thing. So.

**[00:24:42]** So this is just your reminder when you're thinking about data that you always have to be asking the question. When you're looking at a data source from a piece of equipment or wherever you get it from, you always have to be asking the question, am I looking at signal or am I looking at noise? Signal to noise ratio is kind of like a whole other conversation. But this is where kind of like building intuitions, building understanding, and just really like having that kind of gut check of like, am I looking at something that's worth analysis or am I looking at some sort of noise and bug in the system? And that, yeah, that figuring that out can be often a challenging part.

**[00:25:27]** Also noticing, because this will also come up later, this moment here, where. Where at some point on my way out, there's like a spike which can also happen where, like, for one frame, everything is jumped over here. So there is one data point that is way outside the actual expected range, which will come up in a bit.

**[00:26:05]** Okay, that'll make rough sense. Following along, jumping in space. Get that? No one's mind is blown yet. Okay, okay, so now let's look at ways of representing this data that can sort of help us understand and sort of starting to torture the data into a shape that's more amenable to that kind of like phase based analysis.

**[00:26:34]** And for that I'm also going to show you just a little bit of code. This code is on the course repository. Now if you're familiar with Python code and particularly jupyter notebooks, it's in there. It's not particularly like, well set up for sort of student consumption, but it's available, it's on there if you want to find it. It's in the repo, in the cold fold code folder, in the Python code folder.

**[00:27:04]** We're looking at jumping center of mass and this should run.

**[00:27:16]** Yeah, so I'm not going to go too much into the Cody code parts of it. I will just first of all, will this run? No, thank you. It's kind of just like doing a quick pass through. Just interested parties can pay attention.

**[00:27:34]** Uninterested parties can just wait for the squiggly line, some pretty pictures.

**[00:27:39]** But you'll hear me talk a lot about just like writing code and doing analysis and doing this and that. And just FYI, this is what that looks like. So the first thing you do is you install a bunch. So this is Python code and so the first thing you do is you install a bunch of packages. And packages like numpy are for numerical computations, scipy for things like scientific analysis of this, that and the other.

**[00:28:04]** And then plotly is for making the visual plots and squiggly lines and stuff like that. These are all packages that were made by people, many, many people. Many of these packages, numpy and scipy to some extent. But Numpy in particular has a lineage that goes all the way back to the sort of the first history of computing. There is always at every point in the history of our actually in the history of our sort of like long scale civilization, but specific specifically in the computational world there has always been kind of like the de facto best numerical computation package.

**[00:28:40]** And I think these days numpy is probably the most widely used, at least in the sort of data analysis world. But this is the one that does like vector or sort of like matrix computation, does linear algebra. A lot of like the big number crunching of the world is done sort of in numpy or related types of packages. I just want to point these out because this is very easy to skip over. It's not relevant particularly to this course.

**[00:29:07]** But this is one of those places that if you really sit and think about just the volume of human effort and human labor that went into this import numpy line of code, it's really staggering. Many thousands of people over decades working very, very hard over a very long amount of time to make these things happen.

---

### Chunk 4 [00:29:15 - 00:39:15]

**[00:29:15]** Effort and human labor that went into this import numpy line of code is really staggering. Like many thousands of people over decades working very, very hard over a very long amount of time to make these things happen. And invisibly and for free, you can just import all of that labor. And now all the stuff that we get to do is built off of that work that was done by these many folks over the history of their own time. Anyway, this is also a very important stage of every data analysis pipeline's life.

**[00:29:53]** This is loading the data in. And this is literally just the path to the folder on the computer and then specifically the path to the body 3D data and then the center of mass, XYZ data. These are not actually the CSV sort of data files that I showed last time, but they are equivalent. So this is the part where that data gets into the program. It's then the RAM and the memory of the system.

**[00:30:25]** And so when we want to look at it, this is the part where the computer has loaded that data in. So those big infinite sort of piles of numbers that I was showing last time, this is the part where those numbers now enter into the system's memory. And now we can sort of look at them.

**[00:30:45]** Load that up. Yeah, you can load and look at its shape. Where this shape is, we're looking at the center of mass. So it's 1370 by three. So it's 1,370 frames at 30 frames per second, three columns, so X, Y and Z.

**[00:31:04]** And when we talk about the shape of the data, that's kind of what we're talking about, like how many frames, how many dimensions. If it had rotation, so this would have to be 6, so XYZ position, XYZ rotation, this would be 1370 by 6 and what everything is here, blah, blah, blah. Yeah, you get different data points there, different data points there.

**[00:31:38]** And now this is the part I think I'm going to have to restart it when I run this because I think it's basic enough that it happens. This is now the data has shown up into the system and this is a very basic plot of that. So this is the raw data in like, I think it's plotly or something like that. This is the very same data that you see in Blender, except in a much more impoverished form. Like one of the main kind of like, you know, labors and wins of the FreeMap software was figuring out how to adapt the sort of the low level scientific code so it can be shoved into this animation software so that you can do all these nice things and like have all this very easy way of clicking around and showing stuff without having to write the actual code.

**[00:32:33]** But again, because this is an artist tool, it's not really set up for doing kind of like deeper layers of analysis.

**[00:32:42]** So this is, I think it just. Oh, does it just play through?

**[00:32:48]** Yeah. So this is sort of. This is what most. Like, for a lot of scientific analysis, this would already be pretty good because it's an animation in 3D. But you can very easily see how this is sort of not as useful of an interrogatory tool as something like a professional animation software designed for like 3D animations at a very interesting sort of layer of our society because they are artists and they think like artists, but it's also super heavy, technical, like computational 3D math.

**[00:33:22]** So that kind of like that boundary layer that is represented by something like Blender, Blender in particular being like a free open source software. So it has that layer of it as well. It's kind of like, I think, one of the interesting interfaces here, this is also a useful way to sort of confirm to yourself that you've loaded the data correctly, that up is in fact this direction. Very, very, very common. Very, very easy to load the data.

**[00:33:50]** And A, it's just a snowstorm, the dots are flying around all over the place, or B, that person's jumping like this to the side because you haven't rotated things or you haven't rotated them properly so that Z is up. Because remember, a lot of things we're talking about here assumes that there is a, that one of these X, Y's and Z's is aligned with the gravity vector. But there's nothing in the raw geometry that has such a thing as gravity. Cameras don't know what gravity is unless you have a secondary sensor in them, which we don't. So this type of thing sort of gets into overlap between, like, on the one hand, this is not a.

**[00:34:30]** Like, this kind of visualization is not a necessary step of the analysis pipeline. But on a very practical level, it absolutely is a necessary step to have what we would call observability in your pipeline, where the observability is the part where you can just, you know, you're crunching big numbers with fancy code. And the observability is a part where it produces something that you can use your human eyeballs and big human brain to just look at it and say, oh, yeah, that looks right, that looks like a person jumping. They look like they're oriented with Gravity. And now because of that, I am now confident to move on to the next stages of the pipeline and start analyzing data.

**[00:35:09]** Whoever wrote this, I can't remember who wrote this originally, but I always notice stuff like this. This is the British spelling of analyzing with an S instead of a Z. So I don't know. Could have been me, could have been someone else. Hard to say.

**[00:35:27]** Okay, so we've talked about time series. This is not a time series. This is a spatial representation of the data. There is actually nothing in this data that tells you what time is. If you.

**[00:35:50]** It just happens to over time plot the data from the next frame at roughly 30 frames per second. So you can see time in the movement by looking at it. But there's nothing in this. This is a spatial representation. There's nothing in there.

**[00:36:07]** Sort. None of these axes are T. They are X, Y and Z.

**[00:36:16]** So we can also. We can take that and then we can also represent it in this time series format. Right. So this. Now we have to split it up so it can be flat.

**[00:36:27]** So we have X, Y and Z. And then this axis is time. Again, specifically, it's frame number. So we're not in SI units here. We're in.

**[00:36:37]** We don't. This to be SI units, this would have to be seconds. But this is frames. So if you want to convert this to frames, multiply this number by 0.033 or something, which is the number of seconds per frame. Right, Frames per second.

**[00:36:58]** And then you can do some sort of nonsense and you get seconds per frame. This is one of the weird things about this part of calculus, I don't know, is realizing that you can do the same kind of like fraction math for units that you would for numbers. And it's valid to do that. So frames per second is. You can do that math and get 33 milliseconds per frame from 30fps.

**[00:37:35]** Yeah, right.

**[00:37:48]** Yes. So before, when I was showing this, I had already truncated the end frame to be. Before the actual end of the recording. Remember when I said to notice this one weird spiky dot at the end of the recording? If I don't account for that and I just plot all of the data, at some point something on this computer is going to crash.

**[00:38:13]** This is what it looks like because I just said plot X, plot Y, plot Z relative to the frame number and it says, sure, no problem, I'll do that for you. And because I'm such a friendly computer, I'll be smart about how to do the axes, specifically how to do this. Y axis so that you can see all the data that you asked me to plot. But there's this huge spiky outlier here that sort of ruins that. So this spiky outlier.

**[00:38:40]** So this plot goes from 0 to 15,000, which I don't know if you remember from last time. I did not actually fly 15,000 meters into the sky and then back. That actually didn't happen. Oh, sorry. Millimeters.

**[00:38:54]** So 15,000 millimeters into the sky. This is a blobby data spike. So I could fix this by sort of using my intuition and saying, oh, let me tell the code to only have the Y limit show this range of numbers, but I don't know what that range should be. So the other thing I can do.

---

### Chunk 5 [00:39:00 - 00:48:59]

**[00:39:00]** So I could fix this by sort of using my intuition and saying, oh, let me tell the code to only have the Y limit show this range of numbers. But I don't know what that range should be. So the other thing I can do is I can go up here and I can say, okay, the start frame is zero. The end frame negative one means just like the last frame. But I can also, this is again where the observability becomes super helpful.

**[00:39:29]** I can just go into this code and say, okay, let's see. So this first chunk is sloppy data of nothing until let's say frame 118.

**[00:39:44]** Let's see. Yeah, let's say 150 is when the good data starts and it stays pretty good until say 12.

**[00:40:05]** Let's say 1213. So let's say 150 to 1213. So start frame 150, end frame 1213.

**[00:40:18]** And. And then I plot it again. Instead of looking like that weird spike, it looks like this. So oftentimes when you do data collection, you're trying to like, if you're doing data collection, you're typically going to be doing the same thing over and over again. Like multiple participants, multiple conditions, multiple days, da, da da.

**[00:40:39]** So you really want your pipelines to have as little as possible of you. The human have to go in and look at something and sort of figure out, figure out like what I just did of like, oh, let's see, frame, blah blah blah. To frame, blah, blah, blah. That's a manual labor step that requires me to like do stuff with my human brain. I can't just load the data, click go, come back tomorrow, record new data, change the path, and then click go.

**[00:41:03]** I have to look at it and sort of pull out a number, then write that down somewhere. So you want to minimize those steps. But practically speaking, there's almost always going to be some amount of that kind of like data cleaning, data preparation. And so if this was going to be part of a longer study, I would have some place to write down for data collection day, whatever, for participant, whatever, for condition, whatever. The start frame is 150.

**[00:41:30]** The end frame is 1213. And I would have some place to record those numbers so that as I keep collecting data, I'll be able to keep track of this when I do the main analysis. I can know that I'm only getting the good stuff. Yeah. If you were going to do like a long list section of your insight, would you want to pick like a frame to start and end on every time or would you want to know so it would be really hard to pick a frame number.

**[00:41:59]** You could do something more kind of like what we did, where it's like I picked a duration of time of like I want to do 30 seconds and then that would correspond to 30 seconds times 30 frames per second. It's like 900 frames or something like that. But I wouldn't be able to necessarily say on frame 150 to frame 932. That's something that you couldn't really do. Something that's much more common to do is first of all picking durations and secondly deciding a behavior that will make the data easy to chop out, oftentimes in an analytical way.

**[00:42:36]** So with this, if I said, okay, stand here, don't move for five seconds, jump, jump, jump, jump, jump. And at the end, stand here, don't move for five seconds. Then in the data when we look back at it, there would be these flat spots right here to right here. Didn't really wait too long at the end. But this is the kind of thing that would be pretty easy to write some bit of code where you're looking at the velocity of the blah, blah, blah, and then just find something that sort of automatically goes through and chunks out the first step from the last step.

**[00:43:13]** And I would, you know, at this point in my life I could write that code pretty easily and trust it pretty easily.

**[00:43:21]** But that was kind of sort of like a hard earned ability to do that. And also anytime you're doing that, like if you record enough data, then that automated pipeline is going to work like 90% of the time. And then that 10th time it's going to find something weird in the middle and then chop one of your participants data in half and then you're not going to notice that until way too late, blah, blah, blah, blah. So there's always a very complex dance between I'm trying to automate every part of this pipeline so I can operate really efficiently versus the most efficient thing I can do is just manually define these data points for each participant and then write it down somewhere and then have just another CSV that just says for a participant, one condition, block two, whatever, start frame this, end frame that, and then at the end of each recording session I just write down those numbers and then I never have to think about it again. I don't have to write any fancy code code to do it.

**[00:44:25]** Sort of, that's one of those like no right answers thing. And many of you go to grad school, you will lose significant hours of your life on that sort of like, should I automate this or do it manually? Stage. It's a very classic brain trap that it has no true escape.

**[00:44:50]** Yeah, yeah, that's a good question. As there they are. Okay, so.

**[00:45:00]** Okay, yeah. So this part is now.

**[00:45:09]** So again, looking at this as a behavior, looking at the X, the Y and the Z, we can see again that the task is very well defined in that Z axis. And you can see this nice regularity of the data there. And you and your brain saying, oh, yeah, there's something I can pull out of this. There's enough regularity here that there's something that I can pull out scientifically. Like, this is tractable, this type of data.

**[00:45:44]** There's just more noisy. So there's nothing obvious jumping out like this one. Oh, there's a structure here. It's a repeating structure. It's like a cyclical thing.

**[00:45:51]** There's some kind of sine cosine nonsense going on. I could probably do. It's oriented relative to gravity. So there's just all these kind of like knobs that you can like sync your scientific teeth into to try to figure out what's going on here. Whereas these.

**[00:46:06]** The structure is not quite as obvious. You can still see something of the jumping just in that shape. But that might actually be an error elsewhere in the pipeline. But you can see I'm kind of like shifting around. There's nothing super obvious there and there's nothing in the task that really makes these dimensions important.

**[00:46:26]** Again, if you had given me the task of I'm going to put a penny on the ground and you have to jump up and down only on that penny, then now the deviations from that point in the X and Y become a part of the behavior. And maybe you could look at sort of, you know, how I'm meandering relative to this and that. But in this particular analyses, we are going to ignore X and Y and then focus on Z, which is vertical height.

**[00:47:00]** Yeah. So this term here, kinetics, this is one of those many kind of like Latin root terms. A lot of science is really built on this. Like, let's find two Latin words that sound very similar and then build an entire field on separating them apart in this. In human movement.

**[00:47:16]** It's kinematics versus kinetics. So kinematics is kind of like this stuff. It's kind of the kinematics is like related to movement. So things like joint angles and position and sort of like body, body posture. The kind of like the geometry aspects of things is wrapped up in kinematics.

**[00:47:34]** Kinetics is related to forces. So that's where you start thinking things like force plates and stuff like that. Joint torques and stuff like that. And in this case, because we're looking at the Z direction in the vertical, which aligns with the sort of kinetic potential energy, sort of trade off this kind of. When we continue to look at that vertical dimension, that counts as a kinetic analysis because the units are newtons.

**[00:48:04]** Yeah. So then we clean it up. This is a Butterworth filter. Don't stress about that. It just is a smoother and a cleaner and a.

**[00:48:14]** Well, ask the bot about Butterworth filters if you're into it. One of those like. Yeah, this is not the class for that.

**[00:48:27]** Oh, yeah, look, this is. I think. I can't remember exactly who wrote this code. It wasn't me. It was my former lab manager, Michael.

**[00:48:33]** But you can see here, time equals one over 30. Something is now going to come through and convert those frame numbers into seconds, because later on we're going to. Down here, we're going to be calculating from those Z positions. We're going to be calculating Z velocity and Z acceleration. And so particularly once you get to things like acceleration, you kind of want the units to be seconds because meters per frame is.

---

### Chunk 6 [00:48:45 - 00:58:44]

**[00:48:45]** We're going to be calculating from those Z positions. We're going to be calculating Z velocity and Z acceleration. And so particularly once you get to things like acceleration, you kind of want the units to be seconds because meters per frame is a measure of velocity, but it's not a particularly useful one. Well, it's useful in that it gives you scale. But this is also a hard coded number.

**[00:49:09]** So you're just writing the number 30. This is anytime you're in code, if you see someone writing a specific number, like 3, 0, you want to be careful about that. I would prefer to pull the frame rate from the data store somewhere. So that way, if sometime later I start using 60 frames per second cameras or 120 frames per second cameras, I don't have to go searching for all the places that I wrote the number 30. I want to just be able to pull that out of the data.

**[00:49:38]** But in this case, we're just kind of playing around. So we're fine. What are we doing here? Normalizing stuff and doing stuff where we get velocity. Oh yeah.

**[00:49:53]** Oh yeah. And this.

**[00:49:56]** So we're getting velocity and acceleration by just taking the diff. This is your calculus real quick. So X whatever. So if this is the time and this is z height, this is the position in height, in space, off the ground, you can diff. NP diff is a very, very stupid.

**[00:50:30]** Like it's a dumb, dumb calculation that basically just takes the difference. So it literally just says, okay, for frame, this one, subtract this one from that one, subtract this one from that 1, subtract this one from that 1. And then instead of having the Z position on each frame, you have the difference between each data point and the one that came before it. So you have the change in z position over the duration of time defined by one frame. And so that is now delta.

**[00:51:02]** If we're doing meters, delta meters over some measure of time, that's velocity and that's calculus for you. And if you do that same NP diff to the velocity, now you're getting change in velocity over a frame duration of time. That's acceleration. Again, this is NP diff, is the numerical derivative, I guess, like for discrete time intervals, that's the same thing. When you do calculus, you do like the limits and the smooth.

**[00:51:34]** This guy. But in computational numerical land, we just do that and call it good.

**[00:51:44]** And then the integral is the same way. It's sort of the opposite thing. But anyways.

**[00:51:53]** So yeah, so then if you plot it again.

**[00:51:59]** Oh, we still don't have those numbers.

**[00:52:19]** And I need to propagate this thing.

**[00:52:32]** Okay, so we want that to be start. Oh, wait, 150 and equals. Was it 1200 ish or whatever. And then total body center of mass will be start frame to end frame. And then all.

**[00:53:17]** Everything if I do that. And that will be a smaller number. Yes.

**[00:53:29]** That's another really common thing to do accidentally, which is I had changed that start and end frame stuff for the visualization, but I hadn't actually clipped out the actual data. So when it got to the next part where it was calculating the velocities, it was including all those wacky velocities, those wacky sort of garbage frames. And if you think about velocity is the change in position over the unit in time. The that one frame where I jumped off to 15,000 millimeters and back, the velocity on that frame is through the roof in the same way. Because the jump in position is also crazy.

**[00:54:08]** Literally through the roof. I suppose. So now if we do this again, that. There you go. So now it's more cleaned up.

**[00:54:24]** Can I look at this?

**[00:54:42]** Let's look at this area right around 400. So this is the Z position. So this is that true of the height position going on there. This.

**[00:54:59]** This is what the velocity of that looks like. So roughly aligned there.

**[00:55:08]** And this is what the Z, the acceleration looks like. So. And then this is what they look like overlaid. So this is one of those places where I think we're going to get a chance to do this later. But if this was a perfect measurement, then there should be frames like the frames where I'm off the ground.

**[00:55:43]** The acceleration should be negative 10 meters per second down. I'm pretty sure that this actually, I can tell you that. So 398 is a peak. 398 is down here. Yeah.

**[00:56:03]** So this sort of the low part here is the part where I'm in ballistic flight. And the fact that there's a little hump there tells you that the data is sort of incorrect in some way. Either my center of mass is not being calculated perfectly, or in this case, I think that the world is tilted a little bit. Like, the ground plane is not actually flat here, it's slightly tilted, which I think is also the reason why you're getting this sort of like the jump squiggles are sort of still present in the X and Y. Because if you think about jumping on a slanted ground plane, then even though you're moving up and down in space, you're going to sort of see some of that in the X and Y axis.

**[00:56:44]** And I know that because I wrote this code and I know that that is the sort of. That part of the code has some slop to it.

**[00:56:53]** But yeah, so this is. So we can now sort of chunk this out and start looking at like using this data can start to like get particular layers of. I don't know why I always like anytime I have a plan that involves the word and I should just scrap it and have two things, like it's already 4o'. Clock, like we're not going to have time for this, but like, are we going to do this and that? I'm starting to recognize it, but I don't use it to change my behavior.

**[00:57:33]** So we'll figure that out. But yeah, so using this. So for example, one of the things you might want to know when you're jumping, very, very simple dumb analysis is how many times did I jump? Right. If you're just saying, say the task was jump as many times as you can in 30 seconds or jump as many times as you can until you want to stop or something like that, just being able to count these jumps would be something really helpful.

**[00:57:58]** You could just go through and eyeball it, just count them by hand. But that's first of all not going to be very reliable. And secondly won't scale. Like, if you're doing a bigger analysis, you want to be able to automate that.

**[00:58:12]** And yeah, various ways of doing that. And in this particular case, I'm pretty sure now this was Michael writing this code. He's identifying peaks in that jump as zero crossings in the velocity in particular, looking at this stage, because if you think about.

---

### Chunk 7 [00:58:30 - 01:08:29]

**[00:58:30]** Jump as zero crossings in the velocity in particular looking at this stage. So because if you think about the velocity of a curve like this. Can I zoom in on that?

**[00:58:53]** Up, down. So I'm accelerating upwards, so it's positive velocity. And then I hit the apex and then I'm going downwards. So it's negative velocity. So there's a zero crossing there between positive velocity and negative velocity that corresponds to the peak of that jump.

**[00:59:16]** And that's nice to have because if you're trying to identify the peak of this jump, you can actually. Looking at this data, you can actually do that pretty easily. But there's always going to be a point for this data point here. This one's pretty obvious. This is probably the one you want to pick.

**[00:59:36]** But if you're trying to pick just the highest one, there can be these ambiguous moments because you're looking for. It needs to be a particular number. So that's where things like converting into something like velocity allows you to look for something like a zero crossing where the data goes from positive number to a negative number. And then that becomes a very easy thing to pick out of the data.

**[01:00:00]** And representing this is also, I think if I recalculate this. Yeah. Here's another quick tip for data visualizations. This is a bad representation of data. It's fine.

**[01:00:18]** And this is him showing. Okay, using that velocity analysis, you can find the peaks of each jump. Then you can just count the number of those and know how many times you jumped. But this yellow on white, no one not doing anyone any favors. So we are going to go in here.

**[01:00:34]** This is high level program. You see where it says yellow, we change that to a different color. Say magenta. Magenta. Magenta.

**[01:00:47]** There we go. Or let's say red.

**[01:00:53]** Sure, yeah. And so now we have the number of steps here. Just gonna say this out loud. When you're doing data, if you have healthy color vision, you will very quickly go to red and green as the colors to show two different groups. You're not allowed to use red and green.

**[01:01:12]** 10% of the population is colorblind. So if these were green lines with red dots, then 10% of my audience cannot see that color distinction. So just look for any other. So red, blue is good. Blue, yellow.

**[01:01:27]** Well, not that yellow. Blue, orange. Anyways, think about colorblind people. This is also a good example of. Despite the fact that we had that pretty nice algorithm for finding the peaks of those jumps, it finds a bunch of jumps right here.

**[01:01:45]** Because it found. Because the algorithm's kind of dumb, it's just looking for zero crossings. And so when I am just standing here, I'm moving a little bit and it's finding those points. And so if we're naive in the way that we do this, we're going to count five extra jumps at the beginning that didn't actually occur. And then if you wanted to look at an analysis of like, okay, you know, is there a fatigue effect where the jumps are getting slower over time?

**[01:02:13]** Let's take the, let's look at the average height of the first half of the jumps and the last half of the jumps. If you're not careful, then you're going to include these three fake jumps in your calculation of mean height. And now you're going to get a really wacky result, which is that the first, the average jump height of the first half of the recording is super low and then the second half is super high because you have not appropriately cleaned out the false data here. So, you know, this is one of those things that's super obvious when you're looking at it, but less so if you're not careful about how you do your analyses. So, so you would want to have a different way of clipping off and sort of tip the question from before.

**[01:02:56]** This is one of those cases too. If I am writing an automated algorithm to clip off the beginning and end of the data, it's really hard to write that kind of analysis in a way that's going to get this. I can just go through and say, oh, yeah, right, it's, it's here. You can just look at it and say, this is where the data should start. And so I can just go through and find that frame.

**[01:03:22]** Whereas if I'm writing some sort of algorithm that's saying, oh, look for this flat part in the middle, how confident am I that I'm going to be able to get it right there and not right there. That's going to leave two of these fake jumps in there. Alternatively, I can have a more robust method for finding those peaks that has, in addition to that, like velocity zero crossing, it also just has a minimum threshold height. So the threshold, you have to be above a certain height and doing a zero crossing for it to count as a jump. But then you have to ask the question, how do you know what that height is?

**[01:03:53]** And da, da, da, da, da, da. It's a whole part of the game. We'll figure it out.

**[01:04:03]** Yes. And then again, those red stars, he. Yeah, so we believe that those red stars correspond to the apex of the jump.

**[01:04:22]** And this is that same data in the acceleration space.

**[01:04:31]** There we go. Yeah. So this little humpy thing at the bottom here is in fact the. The ballistic flight phase. So this is again showing that there's some sort of squish in the data.

**[01:04:44]** Now, again, from a data visualization perspective, Michael was not doing you guys any favors because he. Well, he was doing you many, many favors, I suppose. But one of the things he didn't do is maintain a consistent representation of. Maintain consistent coloring. Because here he established this sort of like, position is red, velocity is green, acceleration is blue.

**[01:05:10]** But then when he plotted it later, blue is the default color. So he didn't maintain those colors throughout. So this one. Oh, this is actually. Is this velocity?

**[01:05:22]** I think that's labeled wrong. What is velocity anyways? It doesn't matter. So that was now velocity, which is blue, and this is now acceleration, which is blue, which from a visualization perspective, there's nothing different about it. The shapes aren't different.

**[01:05:42]** But in terms of like, if you're trying to use this data to communicate a particular thing to an audience, maintaining those color consistencies can be really friendly on the brain.

**[01:05:54]** But for now, we don't have to worry about it.

**[01:05:58]** Okay, so now we get to the end. Figure it out.

**[01:06:15]** Okay, so now I'm going to take a bit of a. A spin here. So this is again, just a part of the analyses that you can look at all the time. So say, like, you know, these just different ways of interrogating the data, putting things into position, velocity, acceleration, and sort of finding these. I think one of the things that's happening with the red stars is finding particular features in, say, the velocity signal, identifying those frame numbers as saying, oh, this is where the peak of the jump is, and then plotting those same points overlaid on different analyses.

**[01:06:52]** So the red star. So it's hard to determine in actually. Yeah, so he didn't. You could have done a similar analysis. So this is basically liftoff.

**[01:07:04]** Oh, yeah, it says right there, liftoff. So this frame, or close to it, is the part where the feet left the ground. You could do a similar type of analysis to get touchdown. And that would then tell you that everything between liftoff and touchdown is on the ground. So now, even though we know that the.

**[01:07:25]** That sort of ballistic data is like, not accurate in some way because, you know, the. This wiggle cannot be. Physics says that didn't happen. So if this is there, that means there's something wrong with the data representation, which is fine. But we could look at, if we knew the contact portion of the jumps, then this part of the curve is the place where my nervous system is putting force into the ground.

**[01:07:56]** This is the part where I'm landing and absorbing force, and this is the part where I'm taking off again. So using this kind of way of doing the data, you could chop out all of those contact phases and sort of do some estimations and analyses of the processes going in there.

**[01:08:21]** Yeah. And then keep on doing that forever, and then the rest of this.

---

### Chunk 8 [01:08:15 - 01:18:15]

**[01:08:15]** Processes going in there.

**[01:08:21]** Yeah. And then keep on doing that forever.

**[01:08:28]** And then the rest of this starts getting into a place that I find particularly fun and evocative and pretty, which starts to show. So everything up until this point, even though the behavior, as we know, has this kind of repetitive phasic structure, we've been representing time linearly. And so by phase, I mean just literally, like there is a contact phase and there is a flight phase. So there's two phases. You might.

**[01:09:00]** Or you might chop it up even more than that. Say the contact phase has two phases. There is the compression and then there's the extension phase. You could say that the flight phase has a rising phase and a falling phase. But you could also, if you wanted to, you could chunk out these times and use that to sort of break down the.

**[01:09:24]** Sorry, let me back up a bit.

**[01:09:28]** So we know that the behavior has this kind of like phasic, kind of cyclic, sort of circular type of structure to it. But the representation we have here isn't showing that time is progressing linearly from start to end. So from time equals zero to time equals bigger than zero in that direction. So if we wanted to convert that into a more phasic structure that sort of represents that repeated behavior more, we have to do some trickery. Step one is identifying.

**[01:10:06]** Yeah, identifying a discrete moment. In particular, if there's a phasic thing happening, like repeating structure, you want to have some way of defining the beginning of a phase. Like what is. So for going from like 0 to PI, 0 to 2 PI, or going in a circle or something like that. What is zero in that phasic structure?

**[01:10:30]** With a calendar, we call that zero. January 1st, that's the time of the calendar where the number resets. For a clock, we call that time midnight. It resets and it goes back. If you're counting in military time, it goes from like 23, 59, 59 back to zero again.

**[01:10:51]** In this case, it's pretty reasonable to. You could pick any number, you could pick any point in this, but picking that lift off as time equals zero seems like a reasonable place to do that chopping. So we can go through if we wanted to, and take all of these, take all of these cycles and clip them according to their starting time and then overlay them on top of each other. And then you would see, you know, it would look something.

**[01:11:51]** So if you were to overlay all those jumps on top of each other and call. Now, zero is just this star. You'd see this kind of repeating structure on top of itself. And then sort of, then you could try to line things up that way. You can also start representing this stuff in a non spatial way.

**[01:12:09]** So this is actually a time series, so it's actually not spatial. But the skeleton guy and the dot guy, those are all kind of spatial representations. But when we were talking about representing stuff with plots, I talked about like you can do X, Y and Z to do two dimensions and three dimensions. But then at some point I said that using spatial dimensions to represent the data is not really necessary. You can do any number of things on the plot and you can start representing this.

**[01:12:47]** Okay, I'm going to talk about this just so you know. This is like, this gets into the kind of like roboticsy engineering Y stuff that like you're unlikely to encounter again for a while unless you seek it out. But this starts getting into like state space representation where if you can define the state of the system in a small number of numbers, then you can represent those numbers in a plot and sort of see the relationship between them. And so what does that mean? Exactly?

**[01:13:25]** Let's think about this in terms of the jumping behavior and the numbers that we have decided are important for that behavior. So there is this stage where we have to use our big human brains to decide what are the relevant measurable numbers in the system that I'm currently looking at. And this one of the jumping has this nice feature where we actually kind of boiled it down to the point where there's only a singular sort of basic number that we really care about, and, and that's the Z position. However, we then made these kind of like derived numbers of velocity and acceleration, which we also think are very important for understanding the kind of like the physics and the mechanics of this jumping behavior.

**[01:14:14]** So if we're thinking about the jumping human, we want to say, okay, at any given moment in time, what are some numbers that I really want to know about this object that will help me sort of understand what it's doing? We can start by saying I want to know the position and I want to know the velocity and we'll get to the acceleration in a second.

**[01:14:41]** And so then just in the same way that if we wanted to plot this spatially, we could take the XYZ position of the center of mass and put it in some sort of three dimensional representation. We can also make a plot where the X axis we're going to call position and the Y axis we're going to call velocity. And so at any moment in time you can say, okay, your z position is 12 and your velocity is 3. And so this is your current state at that moment in time. Then we could look at the next time step and say, ok, well your position, let's see, your velocity is positive, so your position is going to be up, but your velocity is also going to be dropping because you're on the air.

**[01:15:27]** And so now you're going to be there. And so you can go through each frame and sort of identify the state and then put a data, put a point on there and then connect the dots because you know what time is. Yeah, I promise you it's not. Are we just. Obviously not actually, but are we just innately kind of really good at like calculus?

**[01:15:50]** Not really. I think so, yeah. Like, there's a lot of things like spatial intuition, we're very good at that.

**[01:16:03]** Understanding ballistics and understanding velocity. Like there is this very deep intuitive gut checky level where we are all super, super good at that. Like your ability to like, jog up the stairs, catch a ball, like all of those things. It's kind of like. So that, like the language that you use, like, are we really good at calculus?

**[01:16:26]** It's like, no, no, no, we're not all really good at calculus because calculus is this weird and specific formalism where there's all these like, rules of like, symbols and stuff like that. But we are good at what calculus is attempting to represent, which is like values that change over time. And so this is something that I'm always kind of trying to present in these types of sort of weird conversations, is trying to hit that intuitive level of these things without getting bogged down in the numbers and the math and the sort of like the testable values. I think this is one of the main harms that we do with our stupid way of doing education is because we have this kind of filtration model where education is meant to filter out people who can't hack it. We present this stuff in a way that's hard on purpose so that we can tell who can pass through the filters, that we've arbitrarily defined this stuff.

**[01:17:25]** And so people kind of have this sense of like, oh, the math is hard, calculus is hard, these sort of weird values are difficult. But that's something that we did as a society because we're bad at educating en masse. Or rather, I think we've outgrown older forms of education on math. But that's like, I said this a couple of classes ago. Like, if you're like, if you're like, oh, this makes sense to me, you do understand calculus, you may not know all the formalisms of it.

**[01:17:55]** You may not know how to make your calculus professor happy. But if change in position over time equals velocity makes sense. If change in velocity over time is acceleration makes sense, that is calculus. And everything else beyond that is just like weird syntactic formalisms. And it's.

---

### Chunk 9 [01:18:00 - 01:28:00]

**[01:18:00]** If change in position over time equals velocity makes sense. If change in velocity over time is acceleration makes sense, that is calculus. And everything else beyond that is just like weird syntactic formalisms. And it's sort of one of these, like, you hear roboticists talking about this a lot of like, you know, here we are with billion dollars worth of military funds trying to make a robot do the most basic thing in the world. And then here we, and then, and yet we have like three and four year olds just zipping around a playground doing all this stuff.

**[01:18:34]** Like, once you really start, this is also kind of like, you know, human as robot is kind of like a way that I try to make sense of like the complexity of human movement. Is this kind of like weird, this weird activity of like trying to boil down these really basic, really intuitive behaviors and really think about those low level physics as if you were to build a robot that could do this. And oftentimes you just like, how do we know that this is stable, but that is less stable? How do you know that this is more likely to fall than that?

**[01:19:14]** We all do. But actually nailing that down in some way that's interpretable and grounded, very, very difficult. This thing's even transparent. So like, who even knows? There's fluids in it.

**[01:19:27]** Jesus.

**[01:19:30]** The world is too complicated. Needs to be simplified.

**[01:19:35]** Okay, so state space, right? At any moment in time there is a state. And if you can define that state in a small number of numbers, then for every moment in time you can put a dot on this thing that represents this is where I am at time equals 12. And this is where I am at time equals 13. And this is where I am @ time equals 14.

**[01:19:57]** This is where I am at time equals 16. And so you can basically draw these trajectories in state space that hypothetically represent the relationship between these values. And so in particular, and so things can kind of emerge from that when you plot that stuff that will sort of highlight intuitions that could be hard to identify in other formats. So like, we know because we have these sort of gut checks of physics and because we've been talking about like ballistic movement and stuff like that, that there is a relationship between the position and height and the, and the velocity. Like the z height and z position, z velocity are related to each other in some way.

**[01:20:42]** And so we kind of eyeball it in this time series format. But what would it look like if we could just plot position on one axis and velocity on the other axis, especially during this type of behavior?

**[01:20:57]** And the answer, hypothetically plot this here is that. Okay, so this, I don't know why it's showing up like that.

**[01:21:27]** So this is this representation for the jump stuff. And so, and I guess the velocity here is on the x axis and the position is on the Y is on the z position is on the vertical axis. And the pink dots here are the apex of the jump. So that's at your highest position. And then the hard to see maroon dot here is the bottom of the jump.

**[01:21:57]** And then this green dot here is the liftoff phase. And so you can see. So this is a state space representation because every dot on this curve represents the state of the center of mass system at a particular moment in time. But it's not a spatial representation. There's nothing in space here because the x axis is velocity.

**[01:22:23]** That's not. You can't do that. Like in space you can kind of cheat, but otherwise not. But you can see that this, there's something intuitive about this representation. This thing that we always, that we knew that there's a repeated cycle going on is now represented here.

**[01:22:40]** And we can see for example, that the peaks are much more lined up than the liftoffs. Right? Because this liftoff is being defined. There's something in my nervous system that's deciding this. There's something in the complicated stuff going on here.

**[01:22:57]** And we could, if we really wanted to convert this from a state space to a proper phase space, where now the phase space will be something that actually sort of rotates around the unit circle and has sort of like, you know, thetas and phis in it and stuff like that.

**[01:23:18]** Or we could just keep going and make things even wackier and just keep adding numbers because this is a two dimensional state space. But there's obviously way more possible numbers we could bake in to the state of a system. Remember, this thing has probably like 43 numbers you would need to define its state because it's got, you know, joint number times three or whatever. But in this case we have an obvious third number and that's acceleration. And we believe for good reasons that things like the Z position, the Z velocity and Z acceleration are all coupled in some way.

**[01:23:55]** And lucky for us, we have an additional spatial dimension to plot. And this two dimensional plot can become a three dimensional plot where now the third axis will be acceleration. And that I believe will show up here. I really wish this would show. Make this.

**[01:24:21]** I don't know how to make that show up.

**[01:24:29]** I don't know why this is.

**[01:24:32]** Anyways, do this. Yeah, there we go.

**[01:24:40]** And so there bouncing around. So that's what that looks like we were getting off of Michael's map too. That's where you got question marks there. And I wish I could put this in a more visible space, but this is one of those. So the height here is acceleration.

**[01:25:07]** Oh, Jesus.

**[01:25:16]** Sure.

**[01:25:19]** And so now this is a 3D state space representation of that repeatable jumping behavior.

**[01:25:32]** Oh, I see this.

**[01:25:38]** And I wish I had set this up to plot in a bigger format, but that's fine. I personally really hate jupyter notebooks, but they are useful in some cases.

**[01:25:50]** But yeah, so this, this is the.

**[01:25:55]** This is a three dimensional state space plot of the center of mass kinetics over this repeated jumping pattern. And this, if we wanted to, we could look and analyze aspects of this shape in similar ways that we would analyze three dimensional spatial trajectories and say things that may or may not be related to the actual behavior. Now for this particular behavior, I kind of think this is where the analysis tends to kind of peter out. Like just the quality of the data is not particularly great. The experimental design left something to be desired.

**[01:26:32]** But I do think that this is sort of like, Jesus. Other than the technical issues, there's like something beautiful about this and just the way that it represents this kind of like in intuitive sense of what was going on in that behavior. Like you can look at it, you can say, okay, there's a repeated thing happening, there's a cycle that's occurring and I want to know things about that cycle and how that relates to some other factors that are going on. And what we just went through in the full class time, because that's how it always tends to go, was again a series of analyses. All of these analyses, by the way, on the back end of the other pipeline that we described last time to represent the data in a format that kind of captures that cyclical structure.

**[01:27:24]** And if we really wanted to, we could kind of look at this in other formats and keep going from there. But because we were so careful and to maintain that sort of like epistemological chain from the base sort of voltages on the back of the camera through each stage of the pipeline, through the magic box step of the tracking the person in the image, and through all the other geometry and computation and unit conversion and stuff like that, we can believe that there is, in the same sense that we believe that there is some relationship between the image that.

---

### Chunk 10 [01:27:45 - 01:33:53]

**[01:27:45]** The person in the image, and through all the other geometry and computation and unit conversion and stuff like that, we can believe that there is in the same sense that we believe that there is some relationship between the image from the camera and the reality of what happens at that point in time. Now, two weeks ago, where the organism in question was behaving in space, we can believe that the, the shape and structure of this representation also has that grounding in this relationship to that behavior that we recorded some weeks ago.

**[01:28:25]** Yeah, and so this type of, this sort of state space representation, again, like, I don't know how much it's going to come up in your daily lives for a little while unless you sort of stick into the gritty parts of science. But you see this method for representing complex high dimensional data or behaviors or sort of questions in a lot of different places. You see it in robotics. So oftentimes with robotics, if you think about a multi joint arm, and you think about shoulder, shoulder angle, elbow angle, wrist angle, and you sort of plot those onto this thing, then a given arm trajectory will map a given trajectory in that space. So even if you have a high dimensional sort of robotic element, I think these days there are, people are getting, people are really into like reinforcement learning stuff like that.

**[01:29:27]** But oftentimes like robotic movements are defined within the sort of state spaces and phase spaces. And again, there is nothing special about the number three other than that's how many spatial dimensions we have. If we wanted to plot a 45 dimensional state space, we could do that. We just can't look at it all at the same time. And so robotics trajectories are often plotted in those spaces.

**[01:29:54]** You also see it in neural data. So if you're recording from, you know, a hundred, a thousand neurons in the visual cortex, while you're displaying something or another to the monkey, you might want to know about the, the firing of each of those neurons relative to each other. So you could again define a certain state space and say, okay, for neurons 1 through 100, you know, on the scale from resting firing rate to maximum firing rate, where is each neuron in that space? If you think about a simple case, we only have three neurons. If you show a stimulus to the monkey, you can look at how the different neurons firing rates relate to each other and look at the structures that come around from these types of plots and sort of try to use that to interpret what's going on at the neural level.

**[01:30:43]** Before we go just, I'm going to drop some just jargon terms real quick. If you're interested in this stuff. Poincare sections is a classic term. It's been. A Poincare section is basically, if you take a slice through this, this sort of donut shape, the Poincare section is sort of like where all those points connect.

**[01:31:06]** So if you were to basically take a slice here, then the shape of, of the sort of intersections with that plane would be the Poincare section. You could also do like time locking. So this one is just sort of allowed to swing around. You could also chop it down so that, let's say each of these green dots is sort of like slammed to zero. And then see how the shape changes.

**[01:31:35]** Oftentimes when you do that, like if you align the time base to some relevant sort of feature feature, different things will emerge. Sometimes things will clean up and sort of condense. And you can sort of look at things that way.

**[01:31:51]** And yeah, this is when we, when we show up before class and then the previous class has all like the crazy math on the board. That's differential equations. That's kind of like, that's what this stuff starts to get into pretty quickly. But just to be clear, I can't do any of that math, any of that board math. I got nothing on that.

**[01:32:11]** I can probably write code that does similar things to that board math. But if you sat me down and said calculate the integral of some, this, that or the other, like I got, I, I got nothing. You can all probably, if any of you have taken a math class in the past five years, actually, probably not five. You're pretty young. But if you've taken a math class at this school, you could probably math me out, out of the water on paper.

**[01:32:35]** I just never learned how to do that. My bachelor's degree is in philosophy. But you can back your way in with the intuition and you can learn how to do it in code. And eventually. The nice thing about math is once you get good enough at it, you don't have to do it anymore.

**[01:32:51]** You can just kind of write the code that does it. And the phase of that process where you actually, I am now back to the point where I, I write the math on paper to help me write the code better. But I promise you I wasn't doing that for the first like, decade or so that I was converting my life from philosophy major to science person.

**[01:33:16]** Okay, cool. So that's data, that's movement data. That's probably, that's the last Mocap Y stuff we're going to look at. Unless somebody wants to dig deeper into it. I think next week, we're going to focus more on the honing your ideas.

**[01:33:33]** And I want to end next week with y' all having, like, three papers on your topic versus the one. And then probably after that, we'll move into vision and eyeballs, and I'll bring in an eye tracker, and you'll look at my eyeballs, and it'll be weird. Yeah.

---
