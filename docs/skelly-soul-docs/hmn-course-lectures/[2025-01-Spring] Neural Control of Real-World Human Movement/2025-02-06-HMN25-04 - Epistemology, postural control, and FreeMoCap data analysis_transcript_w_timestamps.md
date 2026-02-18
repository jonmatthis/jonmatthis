# Transcript: 2025-02-06-HMN25-04 - Epistemology, postural control, and FreeMoCap data analysis

## Source Information

- **Source Type:** Local File
- **File Path:** `C:\Users\jonma\syncthing-folders\jon-alienware-pc-synology-nas-sync\videos\video_eater_downloads\playlists\[2025-01-Spring] Neural Control of Real-World Human Movement\2025-02-06-HMN25-04 - Epistemology, postural control, and FreeMoCap data analysis\2025-02-06-HMN25-04 - Epistemology, postural control, and FreeMoCap data analysis.mp4`

---

**Total Duration:** 01:33:11

---

## Full Transcript

### Chunk 1 [00:00:00 - 00:10:00]

**[00:00:00]** Try that again. Okay. Hello everybody, and welcome to this. I guess February made it to February, which is great. An additional month.

**[00:00:15]** So last time we recorded a bunch of data and today we're going to look at it sort of at various stages of development. This is kind of the output of one of the recordings that we're going to talk about at the kind of like semantic level. Semantic meaning, like meaning. And then syntactic is like structure. Before we do that, just sort of standard weekly update on the status of my main project for the semester, which is making sense of all the good data you've been pumping into the machine.

**[00:01:01]** So just again, like a standard scrape the server, recalculate stuff, shove it into a zip file, you can open it in Obsidian. This one is slightly different. It's speaking of what I just talked about. Syntactically, these two are exactly the same. They have all the same folders, all the same file names probably.

**[00:01:23]** But semantically, meaning wise, this one, the most recent one, the user profile part that kind of like looks at what you've been talking about and guesses what your interests are, only looks at your chats in the assignments category. So the stuff you've been doing in class and sort of like any of the bot playground stuff is not getting used as part of that calculation. I didn't really check it too closely for how that changed things, but if you don't mind, pop it open, take a look at yours and hypothetically it should be sort of a better match to what your interests are. Also you can check and see if like, if all of. If you have two chats in both places and it's only showing one, I guess let me know from like a bug report perspective.

**[00:02:13]** But like, don't stress too much about it.

**[00:02:17]** Do, do, do. We're not going to look at that right now. Maybe sometime soon. I also have been informed that I am, I am required to give you an exam. But I'm.

**[00:02:28]** So we're going to do another chat thing, if that one's going to be an exam. So you'll get a grade on whether or not you did it. But I think it'll be a little more. I'll put a little more effort into like the prompt to kind of like, it'll. It'll be asking you questions about your chosen topic and sort of relating it to the kind of like empirical sort of stuff we've been doing before of like, okay, for your topic, like, what are the units that are involved?

**[00:02:50]** What are the, like the methodological approaches? Like, what Kind like what do their measurements look like? What do their studies look like? And they'll be asking like what units are relevant to that domain. So asking questions like the bot will interview you about your chosen topic on the sort of relevant to the commerce, the stuff we've been talking about before.

**[00:03:10]** But you've seen how this thing operates now. It's not going to be withholding, it will be asking you those questions but it'll also be like down to help. So if you, you know, if you don't know, just like ask it just and do yourself a favor and look it up and. Yeah. And then so on Wednesday I have a mind for like another kind of group class activity that will be based on again like forming into small groups and then kind of taking turns trying to find an additional paper that's relevant to your chosen topic and sort of basically trying to intentionally kind of like choose papers that are very dissimilar from the ones that you chose initially but are still within the same domain in order to kind of like flesh that stuff out.

**[00:03:59]** And I think after that session I'll do that sort of pseudo exam chat thing in the following week. Yeah. So if anybody asks, it's an exam and you're very stressed out and it's difficult and you feel like pressured to perform and out compete your peers. So you know, just make sure you know, if anybody asks you're being rank ordered by human quality, which is disgusting. But anyways, cool.

**[00:04:34]** Ok, that sound good? Anybody? Any emotional outbursts? Thoughts, feelings? Great, cool.

**[00:04:48]** So last time, last time we recorded.

**[00:05:07]** Okay, let's make our way towards it by way of review.

**[00:05:19]** So a couple of times ago we talked about like units in space and stuff like that and sort of like you know, Euclidean geometry and then three dimensional stuff and SI units in terms of mass and kilograms and seconds which I just every so often I sort of like notice that it's like kilograms is the SI unit like 1000 grams. Like why isn't it grams? I don't know. I think there's some stuff in the history of these things where like they pick a number for like the unit base unit for gram. Then later we decide it's like that's too small, let's make it a kilogram, it's more viable.

**[00:05:57]** Anyways, not relevant to the present conversation. So we talked about mass in kilograms and seconds and derived units like newtons which is like kilogram. Oh derived units like speed, like milligram, like milligrams meters per second and then Newtons which is like kilogram meters per second, and then joules, which is oh, per second squared. Then joules are like kilogram meters squared per second squared or whatever. We talked about all that.

**[00:06:26]** We talked about pendulums as they swing back and forth, and we talked about inverted pendulums in the terms of, like, things that can be balanced above the ground through a sort of minimally hinged jointy type of thing at the ground. And also, I guess while we're here, this is a nice model of person where these two things represent muscles in the ankle joint. So this is you trying to stand up. Look at you go, you're doing great.

**[00:07:02]** Yeah. And so we sort of laid all that stuff out in terms of, like, setting up the landscape of the general study of human movement at this sort of, like, holistic, like, human scale type of approach. So not the sort of zoomed in looking at cells, looking at individual muscles. Much, much more zoomed out. Let's sort of examine this physical system to the level of fidelity that we can sort of record and reconstruct it.

**[00:07:30]** And this is a software. Why am I looking at the screen? This is a software called Blender. It is an animation software. It's free to open source.

**[00:07:43]** You can download it.

**[00:07:46]** I will endeavor by Wednesday to have the data that we recorded in a place and in a sort of format that is easy for y' all to, like, download and look at. It's not there yet, but I'll try to get that up by Wednesday so that you can kind of click around. And then depending on your interests, I think Wednesday we'll try to focus on the paper thing. But then at a later date, we might have some more kind of like individualized work. And you kind of decide if you want to sort of dig deeper into this side of things.

**[00:08:21]** And then.

**[00:08:26]** Right.

**[00:08:29]** And so in service of understanding all of using sort of studying human movement in the natural world, where in this context we are presenting that this sort of rough couple square meters of space is the natural world. This is my ecological niche. This is the space of the environment where this particular organism operates. So it's valid. And I've spent a lot of time in front of cameras, so, you know, not too much artifice there.

**[00:09:03]** But we recorded looks like five separate recordings. 1.

**[00:09:11]** This doesn't zoom in, does it? No, the first one is calibration. That was part where I set up the cameras and I sort of showed it that grid sort of shape thing. An object of known shape and known size that's very easy to track, which I could use to kind of, like, characterize the positions of the cameras and sort of localize them in space, which is a necessary thing. So.

**[00:09:36]** So, again, calibration has the general shape where you set up your equipment, then you measure something that you already know the answer to. The question about, what is that thing that I'm measuring? And if there's a little more going on in this sort of computational step, but that's the general idea, the sort of principle being if I use the tool to measure something where I already know the answer,

---

### Chunk 2 [00:09:45 - 00:19:45]

**[00:09:45]** About what is that thing that I'm measuring. And if there's a little more going on in this sort of computational step. But that's the general idea, the sort of principle being if I use the tool to measure something where I already know the answer, if it gives me the answer that I know is right, then that's some indication that the tool is actually measuring the world in a way that I care about. And so from there I can move on to measuring slightly stuff in the world where I don't know the answer, which is, in this case, a human moving around in space. So from there we started.

**[00:10:18]** There were these two kind of matched. This is like a little mini baby experiment where the first recording was standing balance, sort of a control.

**[00:10:45]** And that was split into three phases. One is sort of two feet, one foot left, and then one foot right. So standing on two feet, standing on one foot, standing on. Standing on one foot, which is my left foot, and standing on the other foot, which is my right foot. And then the sort of, kind of more experimental condition which is, you know, it's not a particularly, like, exciting experiment, sort of.

**[00:11:14]** This is like a classic case where I'm like, I'm choosing the experiment that I. Where I'm pretty sure I know what the answer will be, because I'm trying to make a particular point in relation to this sort of particular theoretical description of the desideratum of my research study, which in this case is the explication of the neural control of human balance. So this one is, I called it Standing with Support.

**[00:11:45]** And these has matched conditions where I do all the same things in the manipulated condition.

**[00:11:58]** I forget the control is the one where you didn't change anything. I forget the name of the one where you changed something. But in this one, I am doing the same behaviors, except now I'm using that stick as a point of support.

**[00:12:15]** With this difference in the behaviors and the measurement fidelity that I expect to be able to get, and the theoretical framework of this strange idea that we can boil down a human into a singular point mass, since that might be informative about the behavior in question. These things all kind of like form into something where you can make predictions about the future, and then we can, using the data that we have, sort of check those predictions. So I'm not going to spoil the game just yet, but I'll bet you can make some guesses about how these conditions will vary. Oh, and importantly for the two feet standing, I didn't just stand here straight. I was like leaning as far as I Could in all the directions that I could.

**[00:13:06]** Sort of based off of my internal sense of like how far I could lean without having to go so far that I need to take a step to stay upright.

**[00:13:17]** Then there are these two other conditions. One which I call three Big Jumps.

**[00:13:27]** Putting three in the title is just kind of like a hint for me because eventually you want to chop this up into smaller pieces. So telling myself that there are three here helps me know how many to look for. And then the second one is repeated jumps for some amount of time. I don't know. Also, just to be clear, I am calling out the fact that I'm calling this Three Big Jumps.

**[00:13:55]** Not to say this is a good way to name your trials and recorded data. This is actually not a good way to. You don't want to bake that kind of stuff into the title of it. But this is kind of just easy.

**[00:14:12]** I'm allowing it because I'm doing it. And you can do it too. And you will discover through practice why it's not a good idea. And I'll leave that as an exercise to your future.

**[00:14:27]** Great.

**[00:14:32]** Do you feel caught up? Do we feel aware of the situation? Great, I'll leave that there.

**[00:14:47]** So today I think I'm going to focus on the two standing ones. We'll see how far we get with that. We talked. I showed the jumping data from last time, at least the big jump data, but we'll get sort of back to it.

**[00:15:10]** Actually, there's one more distinction I want to highlight here. And this is less about the data that we recorded and sort of like the purposes for recording it and more just something I want to point out about like a difference between these behaviors. So specifically the balance and posture behavior versus like a jumping behavior. And then it gets from the big jumps versus the repeated jumps where with the standing posture it's like a continuous control problem. So I'm standing here, my feet are on the ground, my base of support is a certain space.

**[00:15:50]** And I'm continuously trying to keep my center of mass sort of within that base of support by using sort of whatever I'm doing with my leg muscles. In my sort of equilibrium sense, it's a continuous over time behavior. This is different from something like a jump where a jump is a more of like a discrete momentary behavior. Like there's a period of time before, there's the thing itself and then there's a period of time after. So this is like the wind up, this is the jump itself.

**[00:16:27]** And this is landing.

**[00:16:31]** Unlike this one where it's sort of like you're controlling it continuously over time. With this one, there's a discrete behavior that you're doing once. In this case it's jumping off the ground. And so there's, there's all the physics, there's the moment of liftoff, there's the moment of contact.

**[00:16:47]** But you could compare that to something like throwing something in the air. Either throwing it and then catching it, or just throwing it at a target where that's more of a discrete singular targeted behavior where if I'm trying to throw this at a target and hit the target, I aim, I set up, I wind up, I throw and then at some point the thing leaves my hand and then it's off, it's out of my control, versus more of a pin the tail on the donkey where I might be trying to steer it in, where I'm sort of controlling it the entire time.

**[00:17:27]** There's a lot of deeper layers there. That's one of those things that's like. It's a very intuitive distinction, but there's a lot of differences. Once you start getting down to thinking about this in terms of robotics and kind of like control systems, this starts getting you into continuous control, starts getting into things like feedback control versus this more discrete control stuff, gets you into feed forward control and model based predictions and blah blah, blah, blah. None of which we're really going to talk much about.

**[00:17:55]** But just so you know, those are the deeper layers there.

**[00:18:02]** And also just in a distinction between three big discrete jumps, right? Sort of wind up, put everything I can into the ground, land reset and then do it again, versus a repeated jump thing where it's sort of a continuous process where the force of compression from landing of the previous jump becomes the force that will carry me onto the next one. So there's not that period of kind of like reset and re establish. With the three big jumps, you can look at each of them individually. Aside from fatigue factors and stuff like that, with things like repeated jumps, they carry into each other so well that you can't consider one without considering the thing that came before it.

**[00:18:43]** So this is more think like walking or running or juggling or some kind of continuous behavior. Running in particular also has this case where you are coming off of the ground and at discrete intervals. And then the force of landing from one step compresses the spring of your body, which is part of the energy that sort of bounces you into the next step.

**[00:19:07]** And yeah, a lot of deep layers there. There's sort of at a layer of sort of the motor, the neural control of, like, movement and motor control. There are distinctions and sort of thoughts about where different of these types of control may live in your cortex, in your subcortex and your sort of spinal regions. And, you know, like the thing of, like, the compression from one jump leading you into the next one, the forces from one step setting you up for the next step that comes after it. That sort of stuff is very.

**[00:19:41]** Gets very close to the physics. And the closer you are to the physics, the.

---

### Chunk 3 [00:19:31 - 00:29:30]

**[00:19:31]** The thing of the compression from one jump leading you into the next one, the forces from one step setting you up for the next step that comes after it. That sort of stuff gets very close to the physics. And the closer you are to the physics, the lower in that motor hierarchy you tend to operate. So a lot of things like locomotion are thought to have a lot of their control down at the spinal level, like in spinal central pattern generators, which are thought to be kind of like the upper. The higher regions of your motor hierarchy kind of are thought to the camera speaking in cartoon terms, kind of like they kick off a process that kind of.

**[00:20:13]** Then once it's started, it gets kind of like shunted down to the lower layers of your nervous system. So things like walking, for example, as far as I understand, haven't checked in a while. The thinking this is like one of my sort of pet questions as a grad student was like, how much of things, like, how much of things like locomotion are controlled by the motor cortex versus being controlled by, like, the lower, lower levels of the nervous system? And I believe the last I last I checked in my sort of, you know, in that exploration, I think it was like, when you start, like gait initiation, like when you start walking, you see a lot of activity in the motor cortex. But during continuous locomotion, when you're walking from one part of campus to the other, you're happily in locomotion mode, moving at a relatively constant preferred walking speed.

**[00:21:04]** There's not a lot happening in the cortex at that point. If you start getting onto rocky trains, where you're picking your step, it might show back up. But the idea is that the motor cortex initiates the gait behavior, terminates the gait behavior. So you start walking, you come to a stop. But during standard operation, a lot of the basic control is handled by lower parts of your nervous system.

**[00:21:30]** And then your vision is kind of like. I think it's sort of. It's thought that a lot of that, the vision goes through subcortical pathways, like keep looking for tripping hazards and some avoiding stepping on the stick type of stuff. There's some indication, like keeping balance, not falling over. There's some indication that that visual path, it goes subcortical.

**[00:21:54]** So it doesn't actually go into the pink wrinkly thing up top. It kind of bypasses that. But now we are, I think, directly at the forefront of how much we know about that kind of stuff. So I'll just leave it.

**[00:22:19]** Yeah, great question.

**[00:22:25]** So there's such a thing as what's called the startle response. And it's the thing that we all know. It's kind of like. And I think that's.

**[00:22:36]** That's one of those places where, like, this, the cartoon kind of starts to break down, but you between like, oh, this part is controlled by the higher level, this part's controlled by the lower level. Because things like a startle response is very basic. All vertebrates startle. And it's one of those things, like, it's triggered by these sort of like looming objects and sort of like, oh, no, I'm slipping kind of things, which would make you think that it's sort of like a lower level of control. But it has these sort of characteristics that are more sophisticated than you expect.

**[00:23:08]** Like, I'm falling, I reach out and I grab something. So whatever system is controlling those kind of startle responses and balance correction responses has some access to the things we tend to associate with the high levels.

**[00:23:24]** And so it's just kind of. It starts to get like. That's one of those questions that you could ask the bot more a lot about it, and it would say a lot of things, but I wouldn't trust anything it says in the specifics. Because that's the kind of question that's like, as an expert in that area, I'm like, that gets complicated and murky and try to find recent papers about it. You could probably find stuff in rodents about startle responses.

**[00:23:49]** But then when you start looking at stuff in humans, just the quality of research, it's just harder to study that because it's hard to study humans and you can't crack them open. But, yeah, it's that. Yeah, that's. There's some. There's a study that I saw that was looking at.

**[00:24:09]** It was like walking in VR and every so often the VR world would just like rotate as if you were falling over. And they measured, like, responses like, you know, at the full body level, at the muscular level, stuff like that. And they found that there were these responses in the ankle musculature that happened like 120 milliseconds after the perturbation, which is way too fast to go through the visual cortex because that's thought to be a much slower process. There's also some people running on a treadmill and they sort of drop a plate that they have to step over and you see responses within like 50 to 100 milliseconds, which, again, is kind of evidence that there's a sort of like subcortical path, subcortical meaning below the cortex. So bypassing the pink wrinkly thing.

**[00:24:59]** But these are cartoons. These are never. It's never like, we're talking about, like, bundles of, like, millions of fibers of neurons. Like, and we say, oh, it bypasses this part of the cortex. We mean most of those fibers don't project onto the cortex.

**[00:25:14]** But, you know, if 20,000 fibers go back to, like, you know, it's like we're talking in statistics here. So it gets really murky really fast. So, yeah, I don't know. That's like, a great question that I don't have a great answer to because I don't think anyone does. There might be, like, some people who could give you, like, a few extra layers, but very quickly you get into, I don't know, space, which is a great space to be.

**[00:25:42]** That's where all the work is.

**[00:25:47]** Okay, cool. Any other thoughts? Questions? Yes. Great.

**[00:25:56]** So let's look at standing the noblest of behaviors outstanding in our fields.

**[00:26:12]** So first things first, let's look at. Actually, first things first, let's take a moment to mourn the reality that we will never actually know the true answers to what it was that I was doing here or here. These are. We are going to be looking at and sort of thinking about and analyzing and sort of considering events that happened, like, last week. They're gone.

**[00:26:42]** We are going to try to be making inferences about things like what was my musculature doing? What was my nervous system doing? Where was the state of my body? And sort of, what was the mass distribution at different points in time? These are the questions you want to answer, but the reality is that the true answer to those questions is lost.

**[00:27:00]** It's gone. It happened and then it's gone. Dissolves it into the past. Thermodynamic foam and all that good stuff. And so any questions that we might want to ask about it, there will be many questions we might want to ask about that, where we can never know the answer to what that event of the past was.

**[00:27:22]** And the only reason why we can say anything about it is that we happened to have a empirical apparatus set up, calibrated, and recording. And that recording was able to save some bare shadows of data that we believe are correlated to the hypothetical true fact of the universe of what I was doing in this space in that point of the past. In this particular case, the data that we collected is in the form of videos, where a video is one of these things. I don't know if you've heard of them. They're great, super useful, super dark.

**[00:28:11]** So the recordings themselves were not my greatest work. Some of the camera setups were not great. It's super dark, which I think. So the fidelity of the data that we're getting is not going to be the best in the universe, but it's fine enough. And so this is a video.

**[00:28:33]** This is a record of the data that we recorded. And the empirical measurement that this represents is samples from a particular cone of light from a particular location in space. So a video, this is 30 frames per second, which is pretty slow for scientific data, but standard for most sort of videos that you encounter. 30 frames per second, 720p.

**[00:29:05]** Hey, hey, calm down.

**[00:29:10]** So the video is, let's see, 720p by 1280p. 1280p, meaning pixels. So if you see things like HD high def, 1080p by 1924k.

---

### Chunk 4 [00:29:16 - 00:39:15]

**[00:29:16]** By 1280p, meaning pixels. So if you see things like HD high def, 1080p by 1924k is like whatever, whatever 1080 times two is divided by whatever 1920 by two is. And this is a raster plot, a raster recording raster Image where the 720 is. If you count, if you zoom way into these tiny little pixels and you count them, there will be 720 in this direction and then there will be 1,280 in that direction. And at each of these little squares, there's actually three recordings.

**[00:30:08]** One is in the red channel, one is in the green channel, one is in the blue channel. And the pixel itself represent a number between 0 and 255, which is 2 to the 8th. And if it's 0, it means that that tiny little section of that whatever sensor is on the back of the camera recorded zero intensities of photons. I guess the SI unit would be candelas. I don't really know how that works.

**[00:30:40]** But this little. The number in this spot, it will be between zero and some. Let's even, let's not worry about the number. Let's just say between 0 and 1. If that seems too complicated to you, we can say between 0 and 100% or 100% is the maximum value that that little sensor at that little section of this, of the video was able to record.

**[00:31:03]** So this is roughly speaking white. So that's going to be 100% active. This is, roughly speaking black. That's going to be 0% active. So we get one of these images every 33 milliseconds, which at the end results in a weird thing called a video MP4, where the MP4 is just a file format.

**[00:31:29]** It's just like an instruction set that the computer uses to be able to turn this into something that our primate eyes like to look at.

**[00:31:39]** Yeah, and then there's three of them. And sort of analogously to the way that I've talked about vision before, and these train ductive moments where environmental energy gets transduced into sort of a different form of energy in your eyes, that's light gets absorbed by the opsins and converted into like electrochemical potentials or whatever in a camera, the light is absorbed by some weird crystal of silicone and then turned into a pattern of voltages that gets measured and recorded and converted into this picture. And we believe that there's something in the pattern of activation on the back of the camera sensor at the different time points of recording that is correlated with the realities of what's going on in the real world. The reason why we believe that is because when we look at it, we say, yeah, that looks like a person. Not only does that look like a person, it looks like the person that was standing in front of the camera at the time that I saw the person in front of the camera standing there.

**[00:32:43]** And then the person pushed record. So I look at it and I say, yeah, that seems right. I, I think that I understand how cameras roughly work. And it's that sort of weird intuitive gut check of, yeah, this seems like a vaguely valid recording. That's the empirical basis of everything that's going to come after this.

**[00:33:03]** Everything else I'm going to show you are going to be computations that happen on top of, on the basis of these sort of base level initial empirical measurements. And it's kind of fun to talk about this in the context of low quality videos from webcams, but I promise you, every empirical investigation you do from here on out will have a similar form where there is some empirical measurement. Unless it's like a computational study, which a whole other thing. Well, whatever, different thought, there will be some piece of equipment that you will have calibrated against some known value. It will be recording some, either a singular or a time series of empirical measurements that you will have some degree of trust about whether or not that thing maps onto some true fact reality of the world, which typically speaking, will be some true fact reality of the world that has gone into the past and may or may not be able to be recorded again.

**[00:34:05]** In this case, you could record me doing the same behavior again, but you will never again have the opportunity to record this particular moment in time. So this is sort of just like, practically speaking, as a researcher, this is not particularly precious data because I can just always do it again. If this was like a patient, like an amputee that I had to recruit and they sort of came across town and they came and stand in front of the thing, I did the recording. And if I did that one and it was too dark and I had the cameras kind of in the wrong spot, that's a much bigger bummer because that's a much harder data recording to recreate. But yeah, so, yeah, learn your equipment.

**[00:34:51]** Learn your equipment because when you get to the place where you're recording data you really care about, you want to know all the ways it can go wrong.

**[00:35:03]** Okay, great.

**[00:35:07]** So. Oh yeah, I have some other. Technically speaking, there's another empirical measurement here which is in the form of the timestamps from the videos. So I have measures of the computer's hypothetically nanosecond scale timestamps from each one of the recorded frames. I don't trust it down to nanoseconds, but I do trust it down to like, milliseconds, microseconds.

**[00:35:30]** Question mark. Who knows? This is another thing where if I deleted these timestamps, I could also never recreate those timestamps because videos tend not to actually encode the specific time that the image was recorded. They tend to just sort of say, this is a 30fps video and then play it at 30 frames per second, regardless of the variations in time. So there's many, many deeper layers of the free mocap software, which we will never bring up in this context, relate to this stupid timestamp recording and getting everything nicely temporally synced between the multiple cameras.

**[00:36:10]** So this is the base data, videos from multiple locations. We also have this calibration data, which tells us where the cameras were in space. So camera one was. Translation is like position, rotation is rotation. Put them together, you have something like orientation, six degrees of freedom.

**[00:36:37]** And this is the positions of the cameras. This is another one of those cases where if I didn't have the calibration data for where those cameras were, I can't recreate.

**[00:36:48]** Would be very difficult to recreate. I actually, if I really desperately needed to, I could write some code that would allow me to reconstruct the camera positions without the checkerboard, just using a bunch of like. I could use, like, marks on the board and stuff like that, but I really don't want to do that. So I consider this to also kind of be part of the base data here. Like, if I hadn't done the calibration or if I had done the calibration wrong, very difficult to recreate that.

**[00:37:18]** So, for example, if I was using the wrong checkerboard, or if I had mistakenly had another checkerboard in the background and not noticed it, then that process would break and I would either have to come through and figure out how to fix it or record the data again. So this is another thing that someday this may come up in your life. But my personal belief and advice to you is it is typically speaking a much, much better idea. If you record some data and it's not good data, learn the lesson and record it again. Don't spend a lot of time trying to fix bad data if you can at all avoid it.

**[00:37:54]** You can't always avoid that, but in general, given the option, just figure out what you did wrong, and then record it again. That's my personal advice as a beleaguered scientist. Okay, so let's forget all those and just say the base data is the videos. So if that's the base data, and then this is the other side of that equation. This is the output data.

**[00:38:27]** This is the approximation. Let's turn off the mesh, which is mostly for visuals. And this is the.

**[00:38:42]** That's this guy.

**[00:38:45]** Roughly speaking, this is the level of fidelity that we have reconstructed the human body to. And look, there was a lot of work that went into creating it to this level. Like, it was years of my life, and years to come was to produce this data. And I'm quite proud of it. But also, it's garbage.

**[00:39:07]** There is nothing. This is such an impoverished recreation of this. This thing is like a couple.

---

### Chunk 5 [00:39:00 - 00:48:59]

**[00:39:00]** It was years of my life, in years to come was to produce this data and I'm quite proud of it. But also it's garbage. There is nothing. This is such an impoverished recreation of this. This thing is like a couple chunks of wood.

**[00:39:16]** And I am several trillion cells and billions of neurons and thoughts, dreams and histories and stuff like that. The feet here are just like solid blocks, whereas my feet have this like very complicated musculoskeletal structure. And you know, this thing doesn't have any neurons. It's all very, it's extremely impoverished, but it's the best we got. Yeah.

**[00:39:48]** And then all of this, this point is not worth the time I'm taking to make it.

**[00:40:25]** Yeah, yeah. And then this, this is the actual data model that we're looking at here. This is the whole thing boiled down to a singular center of mass. It doesn't even have rotation, it just has position. And so this is the.

**[00:40:52]** It's a long way to break it down to an extremely condensed form, extremely low dimensional representation of something that is reality infinitely dimensional. You would require like, I don't know how many numbers. So this thing requires three numbers to perfectly define its position in space at any moment in time. I don't know how many numbers it would take to define me as a person at any moment in time. But it's a very, very large number.

**[00:41:22]** This thing, I think. 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14. 14 times 3, 42. So this is 13 joints, 3 degrees of freedom. This requires 42 numbers to define at any moment in time.

**[00:41:43]** So if you want to know questions about things like joint angles, this is not sufficient. But if you're just looking at things like center of mass versus base of support, it's nice to have the low dimensional output. And then I do that. Come back.

**[00:42:06]** Go away. Great.

**[00:42:10]** Okay, so how do we sort of get from point A to point B here?

**[00:42:16]** Well, the first thing we have to do is just like a little bit of magic. Just like a tiny chunk of magic.

**[00:42:26]** Where by magic of course, I mean some form of stochastic process involving machine learning. These days in year of our Lord 2025, a lot of AI talk everywhere. If you've been paying attention, there's been a lot of machine learning talk for quite a long time since then, for as long as you've been alive easily. But I think if you're looking for a specific date, like 1986, Rommel, Hart and some other guy came up with back propagation, which is a very important technique. That basically makes neural networks sort of work.

**[00:43:06]** And so there's a lot. So in everything since then and sort of now, now everything has the term AI in it, which is basically just like a marketing term that means a neural network that has language capacity.

**[00:43:22]** And this is kind of a problem, like I obviously like AI we're using in this class, like a lot. But it's a problem, it's a problem empirically because machine learning will sort of, I think by definition involve some form of trained networks, trained neural network where there's some form of empirical data that gets smushed together with some machine learning processes and it produces a neural network that produces an output of some kind. So when you talk to the bot on Discord and behind the scenes, several, many layers behind the scenes, the thing that's actually producing the words that come back onto the screen and sort of feel like a human like response. Those words are being generated probabilistically from a neural network that was trained on language data.

**[00:44:16]** And importantly, I'm saying probabilistically because the neural networks, machine learning algorithms, machine learning, neural network based computations only operate in that probabilistic stochastic space. They do not do hard computation that will give you deterministic responses. So an example of a deterministic thing is the distance between 2 points. Use Pythagorean theorem for that. Whatever is that X, Y, Z, L?

**[00:44:50]** Sure. And then L equals the square root of X squared minus Y squared. Right. That's A squared plus B. I don't know. Pythagorean theorem.

**[00:45:03]** Right. So you want to measure the distance between these two points. You can do this computation and it is like a, like you will always get the same number if you put in the same numbers here.

**[00:45:15]** Machine learning algorithms, neural networks, any AI based solution, as the marketing folks would like to say, does not have that characteristic. There's always going to be some squishiness and stochastic aspect to it. In this pipeline I have very carefully. There's only a singular point in the process that involves a machine learning algorithm. And it is this part right here, the step of the process where we convert the video into something that's a lower dimensional and directly related to the thing that we care about involves bit of jargon here.

**[00:45:54]** A convolutional neural network which is basically lives in the. It's a trained model that was trained on many, many, many hand labeled videos, hand labeled images where people went through images of people and then marked out. These are where the shoulders are. This is where the Hips are, this is where the wrist is. And so the neural network and the convolutional part just means that it's sort of like running this kind of like search pattern over the image, looking for something.

**[00:46:23]** So like the ankle detector is just looking for ankles at all times. And when it gets down here, it's actually more, it's like a right ankle. They have like a right ankle detector and a left ankle detector. And so it says, oh, there's probably a, an ankle in this part of the screen. And then you take the peak of that probability curve, you draw a dot on it, and then we say that's where the ankle is.

**[00:46:46]** This is weird magic. This is one of those things that like, shouldn't be possible. And yet here we are. Before 2007, it wasn't, sorry, 2017, it wasn't possible. You couldn't do this.

**[00:46:58]** Then in 2017, some folks from Carnegie Mellon published a paper called Open Pose, released a model called Open Pose. And it was the first. They were building on existing models and existing techniques and they produced an output that sort of could reliably draw a two dimensional stick figure on a picture of a person in the screen. If you just Google Open Pose now, you'll find the repo, it's a bit of a nightmare to use, but very useful thing to come out.

**[00:47:29]** And so that is the weird jump in technology that makes any of the rest of this possible. Because video has always been kind of been a very strange form of data because for us as visually gifted primates, we are exceptionally good at looking at videos and extracting a lot of information. You do that all the time. When you're looking at a video, you're looking at a rectangle of light and flickering around and thinking, oh yeah, that person is petting a cat, that person is riding a bike. Like, you're very, very good at that.

**[00:48:05]** And you can say, you can tell, you can say many, many truth preserving things about an image with your giant human brain. So scientifically, video has been used for a long time, but it's always been very challenging to convert that sort of qualitative, gut checky sense of what's going on in the video into something that's empirically grounded enough to actually do scientific investigations on it. Historically, one of the best methods that we had was hand coding. So you would train a group of typically, like undergraduates to look at videos. A lot of like, developmental psychology involves like just watching videos of babies doing stuff and having undergrads who just are like watching, okay, at time equals 12 seconds.

**[00:48:51]** The baby grabbed the toy at 13 seconds. They handed it to the mom at 14. 14 seconds. So you have that sort of, like, manual.

---

### Chunk 6 [00:48:45 - 00:58:44]

**[00:48:45]** Stuff and having undergrads who just are like watching, okay, at time equals 12 seconds, the baby grabbed the toy at 13 seconds, they handed it to the mom at 14 seconds, you know, da, da, da, da. So you have that sort of like manual labeling of videos as the thing that produces the base data of like, oh, babies like to reach to toy. Is this child looking at their mother? And what's the odds of sort of autism spectrum on the basis of like shared attention and da da da.

**[00:49:16]** So valid, but obviously huge bottleneck. Like if for us to look at this data, if we had to give it to a human and have them hand draw points on the screen, that's a massive bottleneck. But because of the advent of that sort of convolutional neural network stuff, we can now send Our images at 30F, 30 frames per second from multiple cameras to the machine and it will draw the dots on the screen. And then critically, for the sort of empirical validity of this thing, that step, which is the only sort of machine learning stochastic magic box step, produces data that lives in the form of a stick figure drawn on top of a picture of a person. So if you are trying to evaluate how well this thing did at drawing a stick figure on this image of a person, you can tap back into that several billion years of evolution of your visual cortex to look at it and say, oh yeah, that's doing a pretty good job.

**[00:50:17]** And so now even though we have the magic box step in our process, we can gut check ourselves and sort of like regain some of the trust that we have in processes like Pythagorean theorem that, that we do not have with processes involving a neural network or a machine learning algorithm or an AI or something like that. So this is sort of part of the epistemology of it. So epistemology, study of knowledge, study of like, how do you feel like you know things? And the reason why I trust this data is because the step of the process that I trust the least is visually verifiable. And I have looked like, because I know this process well enough, I no longer have to spot check all the videos to trust them.

**[00:51:08]** Because I've done that enough that I can say, okay, this is a vaguely big word here, not important term here. This is a truth preserving process. I believe that this step is not throwing fake bullshit into my computational engine, so I now trust the output. There's a lot of, there are other paid softwares that do marketless motion capture, and as far as I understand it, most or all of them we don't really know because they're closed source. But I have various people on the inside.

**[00:51:40]** They have a step in their process where they use a machine learning algorithm to clean their data. So where there's like jiggles and wiggles and weird stuff going on, they have a neural network that is trained to clean that data for them and, and produce data that doesn't have that noise in it. That is a non truth preserving process because you can't spot check it. But that's okay for them because they're generally producing this for like artists and stuff like that. But you cannot do that if you want the data to come out scientifically and empirically valid.

**[00:52:11]** Anyways, moving on. So great. So we've done this. This is the high technology part, this is the weird magic box part. And the output of that is where are we, we crashing?

**[00:52:35]** What's going on?

**[00:52:40]** Great.

**[00:52:45]** Oh well. So the output of that is going to be. That's ignoring the face, it's going to be XY positions of. I think it's, I forget how many. There are like 32, not counting the face and hands.

**[00:53:03]** I think there's like 32 points in this particular stick figure guy. And so on each frame of each video there's going to be 32 times two numbers produced. And those numbers are going to be with an image. 0, 0, it's the upper left. So you sort of, you count, you start here and you count that way.

**[00:53:33]** So that's why we tend to think of X as this way and Y as that way. But for image coordinates it's X is this way and Y is that way. So it's confusing because the top left corner is 0 and then the bottom corner is 1280. So you count upwards going down. You get used to it like that.

**[00:53:57]** So the Z is the depth plane into the thing.

**[00:54:06]** X, Y pixel X, pixel Y. So for one frame for one joint you get, you know the, the position of that joint in two dimensions with the units in this case are pixels.

**[00:54:24]** You then do.

**[00:54:36]** Once you have that two dimensional data and you already have the position of the cameras, that's when you can do the triangulation step. Where you've got camera one, camera two. So camera one, two, three, this is me. And then camera one sees the position of this there. Camera two sees it there, camera three sees it there.

**[00:55:07]** And then using epipolar geometry, which is, you know, this is like old school geometry, I'm not sure where epipolar geometry exactly what era that is from, but this gets down to like similar triangles and like Euclid and like, like old school geometry is how you sort of, you do this kind of like triangulation math where you find out like, because you know the position of each camera, if you can identify the location of the pixel from the point of view of that camera, you can do the math and figure out the 3D location. So the way to think about that is like imagine you're standing on a rooftop somewhere and you have a laser pointer and you're pointing it at some target you can know from your position. It's like, okay, I had to move like over this far and then down this far. So you know the direction that that thing is in, but you can't tell how far away it is because your laser doesn't tell you that. So if you have a friend on another rooftop and they are also pointing their laser at that target, they know that I had to turn this way and down that way.

**[00:56:13]** They also know the direction of the target, but they don't know the depth. So now imagine it's like a foggy night and you're standing on still another third rooftop and you can see those two laser paths and you can see where they cross over that place where those two lasers cross over. That's the position of the thing that they're targeting. And so if you know where those two people are in space and you know the direction that they're pointing their lasers, you can calculate the X, Y, z three dimensional position of the object in question. And then again, you do that 30 times per second, several hundred times per frame and you get these numbers out.

**[00:57:00]** So again, this part is all, this is all computation. This is truth preserving math. This is, yeah, hard numbers, hard math. Do the same thing. You'd get the same answer every time.

**[00:57:21]** I guess I should say, assuming perfect data from the two dimensional stuff, the accuracy of this data is going to be dependent on the accuracy of your calibration. So if you were off in the calibration, then you're going to be off in the position of the cameras and so you're going to be off in the predisposition of the estimated position of the three dimensional object.

**[00:57:46]** That's called, what do we call that?

**[00:57:52]** Accumulating error. It's not accumulating error, but yeah, it's, it's whatever the veracity, the truth value of this measurement derives its truthiness from the validity of the camera position estimation and the validity of the position in the image.

**[00:58:23]** Yeah, and let's not even start asking questions around when you say that my shoulder is here. Why? Is it here? Or is it here? Or is it here?

**[00:58:33]** Or is it here? What are we targeting there? Is it some anatomical thing? Is it the. Is it the muscle?

**[00:58:37]** Is it the meat? Is it. Let's not even ask those questions yet.

**[00:58:44]** Or ever.

---

### Chunk 7 [00:58:30 - 01:08:30]

**[00:58:30]** Why? Is it here or is it here? Or is it here or is it here? What are we targeting there? Is it some anatomical thing?

**[00:58:37]** Is it the muscle? Is it the meat? Is it. Let's not even ask those questions yet.

**[00:58:44]** Or ever. Well, maybe someday.

**[00:58:53]** So now after all of this, we have the. On every frame, why am I looking over there?

**[00:59:15]** We have the 3D position of the body in space. And it looks something like that, not like that. So actually I wanted to see the mesh. Where's the mesh? Mesh, mesh.

**[00:59:38]** And so looking at this point, that point, and then the point over there, triangulated, gives you this point right here, which is the XYZ position of my shoulder, which in this particular case looks like its position is 1.6 meters up and then 0.27, 0.28 meters on the ground. So I'm like roughly 1.8 meters tall. So seems to check out there. Oh, I didn't mention there's a conversion into meters step. That comes from the fact that I know the size of the squares on that board.

**[01:00:21]** Otherwise these would come out in like arbitrary numbers that are based off of pixels and stuff like that actually would come out in units of the size of the square on that board. So at some point in the process, I literally just multiply the numbers that come out of the triangulation by 58, which is the millimeter distance, millimeter scale of that square, and then divide that by 1000 and you get meters. So roughly accurate. But also for most of the things that I do in my life, the number doesn't super matter. Like the specific units.

**[01:00:55]** The number doesn't really matter. What matters is like, where is it on frame 1 versus frame 10 and what's the relative difference? Like this one is twice as many as that one, and stuff like that. Okay, so now this is also one of those places where there's a certain intuition thing that I did, which you may or may not have been offended by, where I was talking about these computational measurements. And then I said, and here you go, that's the data.

**[01:01:25]** And I pointed to the output of what is clearly a visualization software. This is not data in the sense of like, I can't do math on this. This is like a dot floating in space. You can tell that it's related to some, like, hard numbers, which must come from somewhere. But this is not the data.

**[01:01:43]** This is a visual representation of the data, which is a very, very, very useful thing to have. But the actual data in this particular case lives in this such a thing. Let's make this.

**[01:02:05]** This type of a file called a CSV, which stands for comma separated value, which is.

**[01:02:18]** There you go. So knows X, knows Y, knows Z. There's a number, there's a comma, there's a number, there's a comma, there's a number, there's a comma, and there's. There's a lot of these things. There's a lot of these numbers.

**[01:02:35]** Look at all these numbers. Oh, boy. And so we have. And then. So CSV is a very standard data format.

**[01:02:46]** You probably know it in its Microsoft proprietary form, which is xls, which is an Excel spreadsheet. An Excel spreadsheet under the hood is just CSVs with a bunch of formatting. So in the same way that I rail against what's it called, a docx file, and I say I prefer things like markdown, this is where I rail against things like XLSX and say, I prefer CSV. But it is also kind of annoying to view it like that. So we can open it.

**[01:03:18]** And this is LibreOffice version of Excel. I don't really use Excel or Excel like objects for anything except for once or twice a year opening it up to show to a room full of undergrads and be like, ooh, look at all the numbers. Default file format's not whatever. Go to town. Oh, why am I looking over there?

**[01:03:46]** So again, so LibreOffice, CALC, Microsoft Excel, Google Sheets, sheets, these are all applications that can slurp up. So CSV is comma separated value, can also have tab separated value. These are all just delimited values. Whatever, doesn't matter. And so this is just a nice format that takes the values where the columns are the names of one of the kinds of data that you have.

**[01:04:19]** And then in this case, the row is the frame number. Although I'm looking at this now, it's like this shouldn't be there. And there should be a column called frame number and another one called timestamp. But we'll get there.

**[01:04:37]** And yeah, and then there's as many rows as there are frames in the video. And the reason why I like sort of pulling this stuff up is to do kind of like this little journey we're going on is meant to kind of do multiple things to your brain. One is that there should be a level of this that just makes total sense. Sure. Maybe the geometry, maybe you don't know the math, you know, maybe you're not familiar with how convolutional neural networks work.

**[01:05:06]** But generally speaking, it's like okay, sure. Like what you're describing makes some vague kind of sense. If I desperately needed to, I could go through with a marker and just mark frame by frame and measure the distance from the sides and the pixels. And if I desperately needed to, I could do that by hand. I could go through and I could figure out this geometry and calculate it out by hand.

**[01:05:27]** I could do all that kind of stuff.

**[01:05:31]** But never in 100 lifetimes could I do it this many times, could I do it this fast.

**[01:05:41]** And I certainly couldn't then take that and then draw whatever 3092 images that I can then flip book from as many angles as I want so I can look at the data and interrogate the data. This is just. Long story short, why computers are very useful things to have. It's not because they're smart, it's because they're dumb. Super fast.

**[01:06:07]** Like they can only do exactly what you tell them to do, but they can do it very, very quickly. So for those of y' all who may encounter some depths of computers at some point in your life, if you write programs, write code, stuff like that, there will come a time, actually not all of you, there will come a time when you think, man, this computer is really. Either this computer is really smart, in which case it's not humans were smart and they made the dumb box of rocks do very clever things, or if you're writing code, you'll be mad at the computer because it did something you didn't want it to do. I am here to promise you the computer did exactly what you told it to. It followed its instructions precisely to the letter and it, the output was not what you wanted.

**[01:06:53]** It is in fact your fault.

**[01:06:59]** So, yeah, so these are, this is a big wad of numbers. And, and that's not even all of them. That's just the body. There are other similar data structures for the face, the left hand, the right hand, and then still another for the center of mass where this one is.

**[01:07:34]** Trying to remember if I did that. Yeah, so this is the center of mass data. Just the center of mass data. And this one, instead of being a big square of numbers, this is just a three column vector, three column thing. We saw the same number of rows as there are frames in the video, but now there's only center of mass X, Y and Z.

**[01:07:54]** So it's again, we have, when I say we've, we've, we've decreased the dimensionality. This is what I mean. This is instead of being so 720 by, let's see. Actually 720 times 12720 times 1280 is 921,600 pixels per image, per frame, perhaps.

---

### Chunk 8 [01:08:15 - 01:18:14]

**[01:08:15]** 720 times 1280 is 921,600 pixels per image, per frame, per camera. And so for each of those pixels, you need three numbers to define its state, because red, green and blue.

**[01:08:39]** So we go from that unbelievably high dimensional data down to this much smaller but still fairly intractable amount of data here. She really like. This here is a zoomed out picture of the full document. So each of these columns is one of the data types there. And so from all of that we go down even further to this.

**[01:09:13]** There you go.

**[01:09:16]** And the nice thing about this is that this starts to get to the place where your brain might start thinking, yeah, I can, okay, I can handle this. This is more tractable. This is something I can fit into my head.

**[01:09:34]** And so from that place of kind of like mental comfort, you can start asking scientific questions that sort of relate to the thing that you actually care about, which is how does this thing stand upright? Let's make some assumptions that somewhere between this hyper simplified model of the thing and the true facts of reality, there is such a thing as a nervous system and that has such characteristics as peripheral and central and motor hierarchy and cortex and cerebellums and brainstems and all that stuff. Let's assume that this is sort of happening in the context of all that sort of fancy neuroscience stuff, which luckily we in this room, we don't have to do all that research ourselves because we can go and look at what other people have said about it. I don't have to do research on the cerebellum directly. I can just read about the people who are doing the much more constrained kind of biological wetwear, like let's look at rabbits in uncomfortable positions.

**[01:10:40]** Sort of like hardcore low level reductionist neuroscience. And I can incorporate what they tell me about these sort of neural systems and subsystems into my attempts to understand and represent this data at a scale that's just not amenable to that level of sort of like neural biological precision.

**[01:11:09]** Let's do it. So, okay, so with all of that context, I have 20 minutes left, which I think is just barely enough time to kind of like make the main point of differentiation between the data from those two recordings. So before we do that, I think that's enough time to do that. Does anyone have, is there anything to say about all the nonsense I said before this?

**[01:11:45]** A lot of it's kind of like intuition pump there, a little bit of like, there's like a song and dance happening again kind of in that space of like I'm trying to say a bunch of stuff that just makes sense and kind of you already knew at some intuitive level, but just like making that very, very specific point about the data flow and sort of the computational pipeline from the sort of empirical measurement in the form of this transduction of environmental energy into electrons and voltages, and then the various sort of conversions and computations and calculations that we have to take that sort of base data to, to get it to the place where we can sort of start doing the actual empirical research investigation. And again, that's not sort of. Let's not also shy away from the fact that I skipped an unbelievable number of steps at a lot of that part. Not just in the part where I'm actually doing the calculations myself, but just in the basics of like how a freaking camera works. Like the.

**[01:12:45]** I know vaguely how a camera works at an engineering level, but not, not that specifically, let alone like how it sends signals down like a wire and that gets absorbed by the USB port, which is handled by the USB foundation, which is some unknown cabal of probably hundreds to thousands of humans who have been working on how do you read data out of a voltage pin of a little rectangular port on a computer for decades now. Then it goes into the computer and there's CPUs and there's RAM and there's hard drives, like the processes that go into all of this stuff. This is why, you know, this is, this is why, like no human ever operates alone. Because we are all standing on each other's shoulders and we are all using the lifetimes of labor of other people in our vicinity to be able to, with any luck, ignore that part and focus on the things that we're actually looking at. Also, let's not speak about Blender itself, this visualization software, which is an open source software that's been developed in public by mostly volunteers for free since like 1993.

**[01:13:59]** Or Python, which is the code that I use to write the analysis code, which is another open source project that's been around for decades, or any of the history of computation and sort of how we got to that point, or the metallurgy to make the stand, or the plastic or the glass. God even knows, it's overwhelming. So we boil it down and we move on.

**[01:14:30]** Yes, great.

**[01:14:34]** The existential crises where the real learning happens.

**[01:14:45]** Okay, here I am, a fun little skeleton.

**[01:14:52]** And let's say in range around frame, say 150 to 150 display, custom color. Great, okay, so look at me go. Here I am, I am standing this is Skelly. This is Skelly. Skelly's the logo Freemocat Foundation.

**[01:15:28]** Good job, buddy. I have roughly similar bones in my body. So there you go.

**[01:15:37]** And this is a mesh. It's sort of like an animation thing. It's not really data, it's more just for eyeballs. But these are the rigid bodies. So these are the, the simplified sort of chunk segments that we're going to call those parts of my body.

**[01:16:01]** And then this is my center of mass calculated with those anthropometry tables we talked about prior.

**[01:16:08]** And then this sort of red line here, let's make that pink. Yeah.

**[01:16:19]** This represents the vertical projection of that three dimensional point. Now you see these terms like vertical projection, it sounds very mathy and complex. It kind of is. But also, this is the ground. Let's say the ground is where Z is zero.

**[01:16:40]** You can just define anything the way you want. Let's just say the ground is zero height. And so if I am here and I have X, Y, Z location, let's say Z is like whatever, 1 or 1.2 height. If I want to know the vertical projection of that thing, I just say X, Y, 0. So that's how I take the vertical projection of that.

**[01:17:04]** I just set X, I set the height to zero. And now this has the same ground XY horizontal position, but it's just directly underneath the thing that I care about. Why do I want to see that? It's like. Well, because I'm talking about balance.

**[01:17:18]** Whenever I talk about balance, I keep using these terms like, you know, center of mass and base of support. And base of support is on the ground. So I'm curious. I'm not. I don't really want to.

**[01:17:31]** I don't. I can even. I'm boiling this down even farther. I can say I actually don't care for this task. For the jumping task, I care very much about the height of it.

**[01:17:40]** For the balance task, I don't care about the height at all. I only care about its position on the ground plane. So I'm going to project it down onto the ground plane and then I want to compare it to the base of support. Where. What is the base of support here?

**[01:17:57]** There's a thing that's supposed to make it show up here, but I just can never make that work. Maybe next semester. But in here, very intuitively, the base of support is where my feet are. It's the extent of where my feet are. Behold my base of support on the ground.

**[01:18:14]** And so.

---

### Chunk 9 [01:18:00 - 01:28:00]

**[01:18:00]** Can never make that work. Maybe next semester. But in here, very intuitively, the base of support is where my feet are. It's the extent of where my feet are. Behold my base of support on the ground.

**[01:18:14]** And so everywhere I can sort of. Yeah, that's where my feet go. That's the region of the ground where I can observe pressure and sort of change the forces to sort of affect my center of mass. I can push it outside of my center of my base of support. But when I do that, I have to move my other foot or I will hit the deck.

**[01:18:36]** And for this task as we have defined it, I told myself as a research participant that my goal was to lean without moving my feet. So we can assume in this context that if my feet move, then I have failed the task at hand. And so we can assume that the neural control that I am exhibiting is in the service of completing that task. So we've defined success and failure in this task, again, giving us a little bit more leverage to interpret this weird, squiggly, wiggly line here in terms of how it relates to things like balance and posture.

**[01:19:15]** I'm going to say.

**[01:19:19]** I'm going to say 300 00, update all paths. Great.

**[01:19:28]** So the pink line now is showing the previous 10 seconds. That's too many.

**[01:19:41]** Hi.

**[01:19:44]** Moving face to support. No nervous system. Nice fault.

**[01:19:52]** Okay. I'm trying to. I brought a mouse today because it's hard enough to navigate these 3D spaces, but with a trackpad, it's like, Jesus Christ.

**[01:20:03]** So this is also. So I start out outside of the screen. This is what we call invalid data. This is not. I didn't do this.

**[01:20:16]** You were all here. If I did, you would have noticed. But this is what happens when there's nothing in the screen. On the CSV thing. This data looks just the same as the data where it's actually like a stick figure.

**[01:20:33]** It's just not real.

**[01:20:38]** And so I come in and I say, oh, yeah. Then it snaps on top of me. And let's see here.

**[01:20:49]** And so here I am standing and leaning forward, and there's something. Oh, let's do it like that. Oh, there we go.

**[01:21:03]** And so I'm leaning all the way over. It's a little bit outside. So there's another layer of this where I'm like. There's a calculation here of figuring out how to orient myself on the ground, which I don't 100% trust. So I don't 100% trust these data.

**[01:21:19]** But theoretically, the theory predicts that I should be Right at the edge of my foot when I'm leaning all the way this way.

**[01:21:28]** Although, again, if we look at the data of what's being tracked on my feet, it's like, okay, but it's a very, very, very impoverished model of the foot. I have heel, I have toe. I don't have this outer extent of my foot. So even though I can put force into the ground all the way out to here, the data that we have show of my foot as just being a thin line on the ground. And furthermore, because, you know, this was not really made to be like a scientific software, those predictions are going to be slightly different for each of the viewpoints of the cameras.

**[01:22:09]** So there's a whole layer upon layer of, like, how much do you trust things like the very specific data about, like, where the feet are versus the full body data where the body is.

**[01:22:23]** But, you know, we kind of. It's, like, close enough.

**[01:22:31]** It's also kind of hard because. Well, it's hard for a lot of reasons.

**[01:22:37]** Okay. So generally speaking, when you're studying human behavior, the harder the task is, the easier it is to interpret, because the harder the task is, the fewer options are available that complete the task. So if you assume that I can do the task, then the harder it is, the easier it is to interpret. So, for example, standing on two feet is easier than standing on one foot. Because of that, the base of support is larger.

**[01:23:05]** So making predictions about where that center of mass is going to be within that base of support necessarily more difficult because you're picking from a larger region. When I'm on one foot, base of support is much smaller, like this big. And so the ability to predict. Assuming that I'm successfully standing on one foot, the ability to predict where the center of mass will be in this region is easier because it's a smaller region, and there's just. There's fewer things that I could be doing that would successfully complete the task because the task is harder.

**[01:23:38]** And so in this case, if we look here at this sort of nice moment where I'm standing on my right foot, and you look at that vertical projection of the center of mass. Let's see. So here.

**[01:23:59]** Okay, so, 1137. 1137. So from frame 1137, rice picked up my foot to, let's say, 2058.

**[01:24:20]** So for these thousand frames, I am standing over my right foot, and what do you know? The vertical projection is right over my right foot. Hooray. Science works, Physics works. Mechanics are true.

**[01:24:36]** You can. This isn't enough to tell me about like my hip torques, like the center of mass on its own isn't going to tell me about things like my hip torque or my knee flexion and stuff like that. But in terms of like the base level task of am I keeping my foot in the right location relative to my body to keep upright? Sure enough, am. And there we go.

**[01:24:58]** And you can see again, this is sort of like easy to belittle. Are easy to sort of not like, this is cool, this is a cool thing. Just so you know. This is very cool and I'm proud of it. So you're welcome.

**[01:25:17]** Sorry I said that. Okay, so base standing posture. We could look at the left foot, but I don't really. We're running out of time very quickly. And let's assume for practical purposes that the left side of my body and the right side of my body are similar enough that we don't have to care about the left side versus the right side.

**[01:25:41]** That's not true because there's handedness and footedness and I think I'm better on my right foot than I am on my left foot or vice versa, I can't remember. But for the sake of expedience, this is what it looks like when I'm standing under my own powers and my own sort of like anatomical base of support. So prediction wise, how might this change if I'm holding something additional, like something else outside of my body? Well, you can ask the question what aspects of the description of this physical model no longer apply when there's something that I'm touching that's outside of my body?

**[01:26:26]** So there's a lot of things. One of them is that first thing that I said, where my ability to put force into the world, to move my body is constrained to that where my feet are when I'm standing on the ground like this, that my base of support is defined by my feet because that's where I can put force. That's Newton's third law. For every I put action into the world, the world does a reaction pushes me back. In this context, that's called the ground reaction force, which is very, very useful.

**[01:26:55]** You use it every day.

**[01:27:00]** And so I say because of that constraint on my ability to put force in the world, sort of being attached to where my feet are, in order for me to stay upright, I have to keep my center of mass above the base of support.

**[01:27:15]** If now touching something else, that thing that I just said is no longer true. I can now get force in reaction force from the table, which is not noticeably where my foot is. And also in this data recording, I have no record of where the table was. So if I'm looking at this, I can't make that same prediction about where the center of mass would be. I can make a prediction about which direction I am allowed to go out of that base of support from, and which direction would require me to fall over real quick.

**[01:27:53]** I'll just say it, even though I don't have any time. 2,015. They had a DARPA robotics challenge. Bunch of bipolar.

---

### Chunk 10 [01:27:45 - 01:33:11]

**[01:27:45]** Of that base of support from and which direction would require me to fall over real quick. I'll just say it, even though I don't have any time. 2015, they had a DARPA robotics challenge. A bunch of bipeds walking around. They did.

**[01:28:01]** Sort of hilariously bad, but it was still a big advance for the field. One of the things that they really struggled with was calculating the reaction forces because they had really good sensors on the ground, but they didn't have good sensors elsewhere. So there was at least one case where one of the robots was, like, standing in a doorway trying to figure out what to do. And they're calculating the forces it needs to put to sort of move in the right direction. And they didn't realize that its arm was touching the door frame.

**[01:28:30]** And so when they're calculating the forces that it needed, they weren't accounting for this force. And so then when they tried to sort of make the right step, it, like, it fell over and then had, like, a balanced response, which was also wrong because that also didn't have this calculated into it. And then if you just Google 2015 DARPA robotics challenges, there's a lot of, like, really great blooper reels of bipeds falling over dramatically and reminding us how. How powerful of a motor you need to move something with such an incredible mechanical disadvantage. Anyway, three minutes, not enough time.

**[01:29:15]** But we'll do it anyways real quick. Hopefully. Get this in.

**[01:29:24]** Yeah. Center of mass. Sorry. Standing supported. So this is now the other recording.

**[01:29:36]** Same basic structure, except now I am holding this stick and I'm holding it on my. Well, let's see where I'm holding it.

**[01:29:50]** I think it was on my right hand.

**[01:29:54]** And.

**[01:29:57]** Yeah, so my right hand. So I do hide you. I hide you. I say I do this. Yes.

**[01:30:08]** And I grab. I don't think we need the tails.

**[01:30:14]** And so now we should be able to make a nice prediction, especially because I was. There we go.

**[01:30:24]** So let's see. 1182. 1182 to.

**[01:30:32]** Oh, actually, I do want that. About 2000.

**[01:30:39]** I do want to put.

**[01:30:48]** Okay. Around frame 500 before 0 after, calculate the whole thing and display no keyframes. Color is going to be green. Great.

**[01:31:13]** And what do you know? Sure enough, it's on the outside of the foot. So understandably, before we said this, it's like, oh, we don't really trust the locations of the foot to this high of a level of fidelity, which is a fair point. But we also saw in that control condition that when I'm standing on one foot, it's pretty close to that, like, line between the heel and the toe. And now that I have this unmeasured balance support over here, my actual base of support is no longer foot.

**[01:31:50]** It's foot plus little balance point over there. And the reality is, is that, like, you know, I weigh like 200 ish pounds of person. That's a lot of force. I can't really put an appreciable percentage of that force into that little, little weenie stick. So it's not like the.

**[01:32:11]** The point is as good as the foot, but mathematically, I can pull some force from this direction. So my actual effective base of support is going to extend outside of my foot in the direction of that support.

**[01:32:30]** And there you go. Empirical measurement result on the fly. In person. Hooray.

**[01:32:41]** And.

**[01:32:43]** Yeah. Okay, that's.

**[01:32:48]** Yeah. Cool. Feel good about that. Very close timing. We'll probably talk about this just a touch more on next Wednesday, and then we'll do that, that work, that group thing.

**[01:33:03]** Keep an eye on the Discord server if I announce anything. But I probably won't before Wednesday, so enjoy the rest of your lives. Thank you. I.

---
