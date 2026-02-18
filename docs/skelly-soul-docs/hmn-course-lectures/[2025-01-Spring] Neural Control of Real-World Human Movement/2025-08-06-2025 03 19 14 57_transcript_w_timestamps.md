# Transcript: 2025-08-06-2025 03 19 14 57

## Source Information

- **Source Type:** Local File
- **File Path:** `C:\Users\jonma\syncthing-folders\jon-alienware-pc-synology-nas-sync\videos\video_eater_downloads\playlists\[2025-01-Spring] Neural Control of Real-World Human Movement\2025-08-06-2025 03 19 14 57\2025-08-06-2025 03 19 14 57.mp4`

---

**Total Duration:** 01:30:59

---

## Full Transcript

### Chunk 1 [00:00:01 - 00:09:59]

**[00:00:01]** Okay.

**[00:00:04]** All right. Hello, everybody. And let's see where we're at. So we're here at the end of week 11, and today we're going to be doing kind of like a gap filling sort of conversation. I will talk more about the eye tracking data that we sort of like, looked into last time.

**[00:00:28]** Last time we spent a lot of time talking about the raw data from the eye camera itself, and we'll spend a little bit of time looking at the actual data from the far end of that processing pipeline. Like I said last time, it's not the cleanest data in the world, but it's not the worst either. We can say what we need to say about it and take a look at what eye tracking data looks like in real life and try to get some insights into the various parts of ocular motor control that we clued into.

**[00:01:05]** And yeah, that's the kind of thing that I'm certain I could spend a million years talking about that data. But I want to also spend a little bit of time filling in a bit of gaps. Specifically, I want to spend some time talking about neurons. Neurons themselves. The guy itself, the little weird little cell that likes to spike and has all sorts of strange aspects, which I think we can certainly do both of those things.

**[00:01:42]** I am. So, I call myself a neuroscientist, but, like, obviously my actual background is like this weird, diverse sort of mishmash of things. I think traditional neuroscience, typically, I think the people who have like the most sort of like claim to the, to the title of neuroscience or electrophysiologists, who are the people who are like, putting electrodes into brain tissue and measuring, like, spikes and stuff like that are just, you know, people who are sort of like, interacting with like, individual neurons at some meaningful level, which is not me. I tend to work on a much more zoomed out view of a system. And I've said before, I describe what I do as kind of like where neuroscience overlaps with robotics.

**[00:02:36]** It's definitely neuroscience because if you remove the nervous system, people can't do the behaviors I care about. But I think it's worth thinking about. It's definitely worth thinking about, thinking about the actual kind of like the cellular underpinnings and the sort of the biochemical underpinnings of neural activity, both just to sort of know what that looks like and also to kind of have that grounding. Because I think when we're talking about the sort of like the general philosophical distinction between like, holistic approaches to science by measuring sort of zoomed out organismal scale sort of questions, which is what I tend to focus on versus a more reductionist view of the kind of like really zoomed in like microscopic microscope type of research where you've removed a lot of the things that make the thing that you're studying able to operate in its natural environment. But you have in exchange for removing the kind of ecological validity aspect of the research, you gain a tremendous amount of experimental control and you can start saying much, much more precise things which are realistically much, much more grounded to like empirical measurements and stuff like that.

**[00:03:55]** So in a. What is probably sort of a general flipping of the typical order of teaching, we started with a sort of really zoomed out view of neuroscience and we going to talk a little bit about the actual cellular grounding of where these things come from. We'll talk about my. The sort of the.

**[00:04:21]** Yeah. Biochemical process which has caused me more existential anxiety than any other that I'm aware of, which is the sodium potassium ion pump, which really stresses me out in a pretty serious way by definition, but also like emotionally.

**[00:04:40]** So yeah, so I have a little bit time to talk about that in terms of like course operations. Technically. The full poster draft is due this week. I don't realize I haven't made like an actual assignment submission repository on the canvas. So I'll put that up there.

**[00:05:01]** But it's not like I'm not too stressed about you actually turning in the PowerPoint slide or whatever like that. The most important thing is having it ready to upload to the poster printer by Tuesday of next week. So as I have stated before and well, I guess I won't say it again until we're actually doing it, but Monday of next week is devoted towards just that kind of poster preparation stuff. So you would be wise to show up with your poster done so that we can work on the formatting to a PDF and you know, last minute little fiddly bits and stuff like that before submitting it to print.

**[00:05:41]** Yeah. And then sort of got two planned lectures on, you know, evolution. We're going to talk about that on the previous Wednesday. Autonomic nervous system PTSD on the previous Monday. That Wednesday will be spent doing poster practice stuff.

**[00:05:57]** So like small groups kind of like practicing presenting your poster. I'm kind of imagining we can do some of that with the poster prep stuff too, like depending on where you are as an individual and your sort of development process. Like if you're done with your poster, like it's not actually that much work to convert it to a PDF and submit it. So hopefully you'll have a little bit of time to kind of like go over it with somebody else. There's sort of the two classic methods for finding bugs, which is having somebody else look at it because they will always find all the typos that you somehow gloss over.

**[00:06:33]** And then the other classic method is the rubber ducky approach, which is traditional in the sort of software development world where if you're trying to figure out where the problems are in your code or in things you work on, the game is you try to explain how things work to like a little rubber duck. And typically the process of explaining it uncovers where the problems lie. So, yeah, so my thinking is that in Monday's class we'll be doing, we'll just sort of try to get everybody together so that they can submit as appropriate, sort of doing some last minute cleanup stuff. And then the final class session before the poster presentation week itself, we'll spend doing just demo runs. So just kind of like small groups kind of go around the circle and kind of present your stuff.

**[00:07:28]** Which intention there is to keep is to give you kind of the motor practice of actually presenting your work so that the first time you present it on the actual day itself won't be the first time you've presented it to anyone, which will be beneficial to you. From a. This is not a particularly high stakes type of space. People are going to be friendly and supportive in general, in the sciences, if you're presenting a poster at a conference, everyone's on your side. If they're not on your side, they're an asshole.

**[00:08:02]** There is a base level assumption in the sciences and academia and any kind of setting like this that you're like, you're supposed to criticize the things that you see. Like that's part of the peer review culture, is that if I, if you are showing me your science and I am looking at it and I see a problem with it, I am supposed to say something about that.

**[00:08:27]** Whether or not I will or not is sort of depending on like how much emotional energy I have to have that conversation. But it's kind of, it's part of the game of like how we can attempt to do such a wacky thing as generate real knowledge for other people. Which when we show stuff to other people, you're supposed to kind of help by criticizing the small fiddly bits of it. Yeah, so it's a little unclear in the official instructions and it might sound multiple things in different places. You can kind of, I'll say no just because it's kind of weird when you're doing, like, it's sort of like the structure of the assignment is that you are kind of, you are kind of like, pretending that this is work that you did.

**[00:09:23]** But, you know, I don't think you have to do, like, the full sort of cosplay of being, like, like, oh, yeah, I'm the first author here. That's me. But it's kind of like the intention of the assignment is to sort of give you the experience of, like, preparing a poster and presenting it. So it's kind of like it's, I would sort of say, probably just don't just use, like, third person pronouns and not first person pronouns just because. So if someone asks us a question about, like, the specifics of the methods or whatever, and we don't know that answer could actually.

---

### Chunk 2 [00:09:45 - 00:19:45]

**[00:09:45]** Don't just use like third person pronouns and not first person pronouns just because. So if someone asks us a question about like the specifics of their methods or whatever, and we don't know that answer could actually choose, what should we say? So this is a very, It's a great question and it's a very. It's a very real question because Q and A always has kind of like a performance aspect to it. Because you're being asked a question in real time and you want to be able to say, oh, yes, the answer to the question that you asked, but reality is that you might not know.

**[00:10:30]** So you should have at this point read your paper enough to be able to either answer to the specificity that they described it or at the very least know sort of where, like where the questions are. Like if they say, you know, what brand of monitor did they use? And you're like, I don't know, it's in the method somewhere. Like, that's a valid response. If they say like, were the people on a treadmill or were they walking outside?

**[00:10:55]** It's like, that one you should probably know the answer to. But I think that, like, you know, if this was a real thing that you had done, or if you're like giving a talk and someone like raises their hand at the end, people will often ask you questions that you don't know the answer to. And if you don't know that answer, that's kind of. It's highlighting a hole in your understanding. And that's not necessarily something that you need to be upset about.

**[00:11:28]** It's more like, oh, that's something. If they ask you a question and it's like a valid, on topic, good kind of question and you don't have the answer to that, you want to lock that away as, like, I should know the answer to that question. And then you might look it up later in the moment. What you say is, that's a really great question. I'm actually not sure.

**[00:11:48]** And then you kind of like vamp. You kind of guess around the answer. And this is where like the strategy of giving a presentation and the strategy of like responding to the Q and A kind of comes up. Assuming that you are feeling like you're in a confrontational place where you want to look like you know what you're doing. Maybe it's like a job interview or something like that.

**[00:12:13]** There is a skill to answering questions that you don't know the answer to and still sort of displaying your expertise while you're doing it. And like, for me like if I'm talking to like grad student or undergrad or something like that, like, of course you don't know the answer to all the questions. You've just sort of started doing this. So if they ask a question that you don't know the answer to, kind of the game is like, you want to be productively confused, right? You want to be like, that's a good question.

**[00:12:42]** Because of this, that and the other thing, because it connects to this other part that I do understand. That's a good trick. Sort of like, oh yeah, that's a great question. Let me talk about, let me connect it to this thing I can say more about, but I think being able to understand why the question is valid and then just kind of connect it to stuff and say, oh, I don't know the specific answer there, but I do know that that's connected to this, that and the other thing. I'm not sure if it was a force instrumented treadmill, but I do know if it was, then we could get the footfalls more accurately.

**[00:13:17]** And so, and that's a totally valid thing to do. No one's going to be sitting there checking off points based on whether or not you gave a valid response.

**[00:13:28]** That's kind of what I mean by posters are kind of practice runs for papers if you go to a conference. Because another thing too is if you're, say you're a grad student and you're working in a lab and you know your stuff inside and out, but then you realize that you know your stuff inside and out relative to the kind of questions that you're going to get from people in your lab or people at your department or people at your school. And then now you go to a conference and that conference has people from all over the place, including people who study, you know, like whatever, some, some little layer of biochemistry that's just not represented in your lab or in your school, and then when those people show up, they ask what's the most obvious question to them? And, and you've never even heard of the things that they're talking about.

**[00:14:17]** That's actually great news for you because you have now had this sort of spotlight shown on a gap in your understanding. And so in that situation you say, I didn't know about that. Can you tell me about it? You seem to know a lot about it and sort of get them talking. And I think that kind of question, I think is where the gap between like the actual operation of science versus like taking classes and getting grades and that kind of thing really starts to break apart because in classes there's this really strange fiction that you're supposed to know all the answers to the things that are being asked of you.

**[00:14:54]** And you are literally given a score based off of like how many of the boxes you get to check In a more collaborative type of arrangement which you know, real life is intended to be be. You kind of get that if someone asks you a question that you don't know the answer to, that's a good thing because it means that that's showing you where to do some work.

**[00:15:20]** Speaking of like long rambling answers to simple questions, does that help? Yeah. Any other questions about that? About the. Does the basic sort of structure of what we're going to do in the poster session itself makes sense?

**[00:15:35]** I haven't assigned you days or anything like that, but yeah, yeah, yeah. And again, I'll just say it again.

**[00:15:51]** The first time you run through your poster with somebody will be the worst time. By the end of the, the whatever hour and 40 minutes of the class period when you've done it 2, 3, 4, 5, 6 times, you'll be so much smoother with it than you thought that you could be. And yeah, if this was an actual, if this was a paper you were planning to publish, the end of a poster session is the absolute best time to sort of take down your notes. In this particular case, you don't really have to stress about that, but it's sort of like you want to think about what your story is in terms of what's the top layer of what is the takeaway? What is the singular message when someone walks away and they say, oh, that poster was cool because they were looking at this.

**[00:16:51]** They did, you know, the people did this experiment and did this method and sort of got this result and sort of like, you know, it's cool because of this, they were, they were studying that. Like that's kind of what you want to focus on. And that is going to be, it's going to be different for every paper. It's going to be different for every person. And yeah, you just want to be able to kind of go.

**[00:17:14]** You want to be able to also go through your story at different levels of abstraction. Like you want to be able to have the, the 32nd, like, oh yeah, this is the general vibe of this thing versus the longer run, 5, 10 minute sort of run through of explaining the details. Yeah.

**[00:17:36]** Okay, let's see here.

**[00:17:46]** Let's look at some eyeballs.

**[00:18:14]** Okay. So trying to remember like where I got to with everything last time.

**[00:18:22]** Yeah. Okay, so here we are. And so that's y'. All. These are my eyes.

**[00:18:36]** And this crosshair is, roughly speaking, the estimate of where my eyeballs are pointing relative to this scene. So you want to think about it in terms of, like, imagine that I had two lasers coming out of each eye, passing through the back of the eye in this sort of fovea. So if that's my eye, that's my, you know, that optic nerve, and then that's my fovea. So that's the. That sort of pit on the back of my retina where I have the highest acuity.

**[00:19:19]** If the system is well calibrated, which it is enough for, you know, close enough for government work, as they say. And if I am fixating as precisely as it feels like I am, which is sort of a secondary question, this point right here in the image is the point that would be projected onto the back of my eye. So if you could put a little camera into my eye and somehow it.

---

### Chunk 3 [00:19:30 - 00:29:30]

**[00:19:30]** It feels like I am, which is sort of a secondary question.

**[00:19:36]** This point right here in the image is the point that would be projected onto the back of my eye. So if you could put a little camera into my eye and somehow image like the light that's hitting the back of my retina, it will look like an inverted version of this picture sort of onto the back of each eye. This circle right here is very, very roughly the size of it's plus or minus one visual degree, which is roughly the size of the fovea in the world. So as I'm looking here, everything that's inside of the circle is sort of again, hypothetically being absorbed and processed by the fovea of my retina.

**[00:20:25]** And there. So the world camera here is recording at 30 frames per second. The eye cameras are recording at 120 frames per second. There's two eye trackers. So that means for every frame of the, of the video, there's going to be eight of these red crosshairs on, on the, on the world camera because that's, you have, you have many, many more data points from the eye camera than you do from the world camera.

**[00:20:56]** This is a lot of what we're going to see in this data because of the shadowing that's happening here. You'll be able to see these little things circling the people. They'll jump around a little bit and that's where these little spreads come from.

**[00:21:15]** This is one of those places where having a good understanding of the way that eyes actually move helps kind of see through the noise in the recording. I happen to know that eyes do not move fast enough to bounce down here and then bounce back up in the space of the 33 milliseconds of a single frame of this recording. So it's easy for me to label this as like, oh, that's just tracker noise. If I didn't know that, if I was like, oh, our eyes can move infinitely fast and sometimes they do, it would be hard to differentiate between good data and bad data. So knowing what the neural system is capable of is really helpful.

**[00:22:05]** Yeah, yeah. So here's one. So for whatever reason on this frame, the red circle is finding something else. I'm actually not sure what the colors mean. Like what the red versus the yellow.

**[00:22:27]** They're both clearly, one of them is estimating the pupil from the two dimensional image of the eye. The other is representing the three dimensional sort of spherical estimate. I'm not sure which one is which, but you can see how it's kind of off by that frame.

**[00:22:49]** Yeah. So now we are in a good spot where I am calibrating on this ball, this green ball. This is the process where I was doing this with my head, actually. Can I. I wish I hadn't done that, but that's okay.

**[00:23:15]** Oh, there we go. Yeah, Great.

**[00:23:22]** Cool. Now I can use the arrows, right?

**[00:23:43]** So I guess I can just play this. Do I play.

**[00:23:52]** Let's play it full speed. So a little bit jumpy, but more or less tracking.

**[00:24:03]** And this is another one of those cases where, like.

**[00:24:09]** So this is a good example of.

**[00:24:13]** So right now I'm looking at the ball. I know I'm looking at the ball. And then right here, actually.

**[00:24:21]** So as I'm going up, you see, there's still some error there, but it's more or less working.

**[00:24:28]** And so look at this little part where, depending on how we feel about the data, I either make a quick saccade to look at the palm of my hand and then bounce back to look at the ball, which would represent, like, a minor deviation from my task of figuring out, fixate on the ball. And then, like, let me just, like, look at my palm for a moment.

**[00:24:56]** And that's actually.

**[00:25:00]** Yeah, yeah, look. So if you see this, I did move my eye. So that is real data. So that's one. And that remains.

**[00:25:14]** Because this sort of thing, the eye does move like that. I know that. I know that. The eye moves like that.

**[00:25:23]** And it's also. It's recording multiple frames from this location. So even though this is actually not tracking properly on this frame, this is, quote, good data.

**[00:25:39]** Keep track of the time.

**[00:25:48]** Yeah. So now that's me looking at the screen, and then there's me looking out in the world. So a couple things you might notice. One is it's moving really fast. This is just.

**[00:26:01]** There's one of these sort of rules of thumb I have that, like, video from an eye tracker doesn't make sense when played at full speed. It really kind of needs to be slowed down by a factor of like, four to really make sense. And I can't ever figure out if that's interesting or not, because I experienced this at full speed. Like, that's when I. When I was doing this.

**[00:26:27]** Like, I was moving as quickly as the video was playing. But when I watch the video later, I can't make any sense of it. It. So however you want to parse that. And in my personal experience, a slowdown of about 4x is about what I need to make sense of what's going on.

**[00:26:51]** So there is kind of Just a general question about visual processing.

**[00:27:02]** Also, I did try to record the audio. The audio did not record because I'm pretty sure this software just doesn't do that. So I have to kind of make some estimates about what's going on.

**[00:27:26]** Okay, so here you can see me kind of reading, which is.

**[00:27:58]** So this is a very.

**[00:28:01]** What's the word?

**[00:28:05]** The way that we tend to look around the world in natural behavior. There's this guy named Mike Land who did a lot of studies in his kitchen. And Mary Hayhoe was my former advisor, did a lot of studies looking at general tasks and stuff like that. And the way that we tend to navigate and sort of investigate the world is we. If I'm interested in something over there, I will first move my eyes in that direction.

**[00:28:27]** And then I'll point my head, and then I'll point my body. And it kind of tends to happen in that way. So if you're searching around your eyes lead. And then if you find the thing that you're actually looking for, then you might commit a little more to pointing your head. Then you might commit a little more to pointing your body.

**[00:28:42]** Because in general, we like to keep our eyes pretty fixed in the middle of our head. Like, we don't really like to have our eyes anything other than central in our orbits. Because doing so requires muscle activation. And we tend to be pretty stingy about using our muscles if we can avoid it.

**[00:29:03]** So if we do make big eye movements, they're almost always followed up with either a saccade back to center or moving your head so that your eye is back in the orbit. So you can see here. Both my eyes are kind of off to the left, but as I go around, it gets closer. I guess I must be, like, looking off to the side here. But this tends to be the way that we read stuff, is make.

---

### Chunk 4 [00:29:15 - 00:39:15]

**[00:29:15]** Both my eyes are kind of off to the left, but as I go around it gets closer. I guess I must be like looking off to the side here. But this tends to be the way that we read stuff is making saccades. So looking at that and then bouncing down to this was like the list of tasks that I was going to do.

**[00:29:47]** Yeah. So this was a saccade. So this is a single frame. So from frame, where's the number there? I don't see the number.

**[00:29:56]** Anyways, so in this 30 millisecond period between frame one and frame whatever, this is frame 12 and frame 13, I saccade from there to there, which is a fairly large saccade but at roughly the right speed. So I don't know if that's interesting to other people, but it's always, I think things like reading are. It's interesting to look at things like reading because you can see some of the precision that comes out in the eye tracking record. Whereas in the. When I'm just looking around the world, it can be hard to tell how precisely I'm looking at stuff.

**[00:30:43]** But in this case I'm making these saccades and I'm making them very precisely to the points on the board where the information is. Later on, I look at that page and you sort of see some more precision going on there. I'm also. Yeah, there we go. I'm doing it on purpose.

**[00:31:05]** Yeah. Here I'm doing these saccade, like big saccades from the right and left and in a little bit we're going to pull out the actual like time series trace and sort of see what that looks like. But those are big horizontal saccades and then big vertical saccades.

**[00:31:26]** Yeah.

**[00:31:31]** So I wish I had the audio on this, but that's okay.

**[00:31:42]** Yeah.

**[00:31:46]** So I also want to point out, so I talked about VOR vestibular ocular reflex, where that's the one where if you're like looking at yourself in the mirror, you can move your head around and your gaze stays fixed, fixed. Your eyes keep pointing the same direction because your head is sort of counter rotating.

**[00:32:03]** And when I'm making a big turn like this, you can see.

**[00:32:14]** So look at this.

**[00:32:18]** So as I'm turning, I look all the way that way to the left. And as I'm turning, I cannot ignore the head acceleration signal. The VOR is a very, very, very low level reflex that does not turn off. It's actually, it's used as a measure of brain death for sort of.

**[00:32:45]** Yeah, like, I don't know, situations where they don't have better tools. If they're trying to see if somebody is like alive, in a coma or just dead, they'll take the head and they'll move it back and forth. And if the eyes counter rotate with the head motion, then that person still has something going on on the inside. If they don't, then that person is no longer living because it is, because the VOR does not. There is no state of your body where your VOR doesn't work and your brain does.

**[00:33:18]** I guess that's probably not fully true, but it is a very, very low level reflex that has been around for about as long as skeletons. Like, we have evidence from like bony fish to 4, 4, 4, 50 million years ago that they had something like the vestibular ocular reflex keeping their gaze stabilized.

**[00:33:38]** But yeah, so see how it kind of.

**[00:33:43]** So first of all, there's this sort of like double tick thing happening. So as I turn, my eyes go forward, they kind of track back and then they bounce back again. And that's because as I'm rotating, my eyes can only go so far. So as I rotate my head, I can turn around in a full circle, but my eyes cannot. So they go to as far as they can in the orbit, they tick back to center, and then they start tracking again with the vor and then they sort of align where they want to go, which is looking at that screen.

**[00:34:27]** So there's me tracking smoothly, tracking my finger. And then I think the next one is I will try to track without that finger and do a bad job.

**[00:34:41]** Yeah. So you can see, try as I might to track smoothly, I am not able to do it without a reference point. So I just make these big saccades along the back wall. Oh, what's that? Okay, and now we bring up the juggling balls.

**[00:35:07]** So I should be writing down these frame numbers. Juggling starts at 2, 9, 7, 8.

**[00:35:31]** So with something like throwing and catching, there's two components of that. One is the throw, the other is the catch. And as we. Do I have any. I do.

**[00:35:42]** I still have them in here. So we have discussed ballistic trajectories in this class and centers of mass and those sort of base level, like Newtonian mechanics.

**[00:35:54]** And one of the nice things about throwing and catching from a sort of perceptual motor research level is that it has a lot of things going on there. So there's the motor aspect of throwing the ball, which is weird, complicated hand trajectories to sort of impart a particular physics on the ball. So that when it leaves my hand, it is following a ballistic trajectory that is going to land it in the place that I want it to. But your motor commands always have noise in them. So as I throw the ball, I desire to throw it in a certain trajectory, but the actual reality is going to differ from that somewhat.

**[00:36:32]** And so I have data, the sensory data off of my hand about how that throw went. That gives me some rough estimate about where the ball will be. But that may or may not be good enough for me to actually catch the ball. Like to actually put my hand at the location where the ball is going to land. So what you see is there's very sort of classic strategy where you let me see if I can find a good one.

**[00:37:06]** Yeah. So in this case, I'm about to throw the green ball. I wish I had tilted the world camera down a little bit so I could see a little more of that, but that's okay. I guess I can do this. Forgot.

**[00:37:22]** That's nice.

**[00:37:26]** And so presumably right around now. Oh, we're not there. Oh, I went the wrong direction.

**[00:37:37]** There's something jumping. Oh, there is. That's fine.

**[00:37:51]** Yeah.

**[00:37:56]** So as. So first of all, just to be clear, one of the things that eye trackers can. Can be misleading about is because there is a crosshairs and because there is a singular point within the crosshairs, it's really easy to think about that in terms of like, if you're not looking at it, you can't see it. But that is obviously not the case. We have a fair amount of peripheral vision.

**[00:38:19]** Like, I can see my hands out to about here, and if I move my fingers, I can see them out to about here. Because we're more sensitive to motion in the periphery, which is its own kind of weird.

**[00:38:34]** But so I don't need to directly fixate the ball in order to see it. Like, I can do a lot of work with peripheral vision. In particular, I can because I've. Now I'm not like, great at juggling, but I've been doing it for long enough that I'm not as like, as you get better at something, you need less and less information to perform it well enough to not drop the balls. But in any case, you can see that there is this kind of predictive saccade.

**[00:39:05]** So as the green ball starts coming up, I make the saccade over to roughly where it's going to roughly where it is sort of.

---

### Chunk 5 [00:39:00 - 00:48:59]

**[00:39:00]** That there is this kind of predictive saccade. So as the green ball starts coming up, I make this saccade over to roughly where it's going to roughly where it is sort of closer to where it is. And typically on the assumption that I am currently gathering information about this green ball during this particular period point of the recording, we tend to look at the ball at its peak. So when it's in this nice ballistic trajectory, we tend to look at it mostly when it's at that sort of apex of its trajectory. Because, because it's a fully defined movement, if you know the position of that apex point, you can fully predict where it's going to be in the, you know, milliseconds after when I'm actually need to get my hand in that location.

**[00:40:01]** So you can, yeah, there's some gaps here.

**[00:40:09]** So you can see this kind of. So as this ball goes through, I cut over to it, sort of would just get the 1, 2, 3, 100 to 150 milliseconds of information that I need to. And then once I sort of have that, presumably I have, presumably I'm already moving my hand in the direction I need to get this ball. But with that last little 100 milliseconds or so of visual information, of precisely fixated information, I get the little last minute of corrections that I need to do to make sure that the hand is in the location that the ball will be at the appropriate time. And then once I'm done with that, I saccade over to this one and I repeat that process.

**[00:41:03]** So there's often this sort of predictive element of vision particular when you're walking over rocks, which I showed at the beginning and I'll show it again at the end of that when I'm talking about my actual research. But when you're walking over rocky terrain, it's very obvious that what you are doing is gathering the visual information for what is going to be happening in the future. So you're typically performing the motor action like you're placing your feet on the ground relative to the place that you looked maybe a second and a half or two seconds prior to that. So there's your nervous system, if you're engaging in a sort of complex perceptual motor task, is typically doing sort of two things at the same time in a kind of overlapping way where you are simultaneously gathering the information that you will need in the future so that you can, so that you can in the moment perform the motor action that is the most appropriate for the way that the world currently is. So if you think about it like the classic example is like slalom skiing.

**[00:42:14]** So if you're coming down, so slalom seems like you go around the flags. Like if you're going down and you know you're going around, you know, 1, 2, 3.

**[00:42:32]** Like if you're going around flag one, if you're only looking at flag one, then by the time you clear it and you start looking for flag two, you're kind of already on the wrong trajectory. So what people have found when you put eye trackers on people doing slalom tasks and stuff like that is typically when we're actually sliding around flag number one, we're already looking ahead to flag number two. And then by the time we sort of get into this terminal phase of going around flag number two, we're already looking ahead to flag number three. So there's often this kind of, this offset between your perceptual system, which is gathering information about the future, and your motor system, which is operating and driving itself on the basis of the information that was gathered at some point in the past. And the time frame of that can vary, but not that much.

**[00:43:26]** For really fine grained motor behaviors like catching a ball or slaloming around flag, your brain can sort of hold on to very precise visual information for about two seconds. So it's about roughly, that's, you know, when we think about memory, there's all sorts of scales. There's long term memory, which is like, you know, years and lifetimes of memory. There's short term memory, which is like, you know, what did you eat for breakfast this morning? Which you will forget in a month, but you'll remember today.

**[00:44:04]** And then there's shorter time scales which we tend to call visual memory or sensory memory, which is kind of the, like, if I throw the ball and look at it, I can catch it and sort of operate on that timescale of like, the level of precision that is necessary to guide really fine grained motor tasks tends to live for about a second and a half or two seconds in your brain. So there's this point I'm trying to make here is just that there is that kind of temporal offset between the perceptual system and the motor system. Not always, though. Sometimes you are guiding things in more directly. Like if you're threading a needle, that's a feedback system.

**[00:44:49]** So you're not, you know, like, you're like you're staring at the thing the whole time. So you're getting information in sort of a real time feedback loop. But anyways, this is where things get complicated. This is where you could spend several lifetimes studying the details. But my goal is just to let you see how weird it is and then you can deal with it later.

**[00:45:12]** Okay, so juggle, juggle, juggle.

**[00:45:19]** That's too long.

**[00:45:25]** Too long. That's enough. Okay. Four, three, eight, four.

**[00:45:48]** Okay. Yeah. So here's me reading. And so 4873.

**[00:46:10]** So this is a Wikipedia article about vestibular ocular reflex. And I am reading it dutifully. It's not tracking super great, but you can see that reading involves little saccades across the line. I think I was getting flustered at this point, so I don't think I was actually reading very well.

**[00:46:39]** So looking at the data, it looks like I'm just going across the top row. And it's possible that I was. But also, sometimes the vertical position of the eye tracker is dependent on depth, which I'm not going to focus on that. But, yeah, you can actually see me failing to read this as I start skipping around and going back to other parts. But if I was reading this very carefully, we tend to make little saccades.

**[00:47:24]** So, like, from here to here to here, back to here.

**[00:47:32]** So because I don't have to read word by word, if it was a language that didn't speak very well, if it was. If I was just learning how to read, I probably would be looking at each individual word one at a time. But because I speak English and I can sort of scan pretty well, I can make bigger jumps and sort of chunk the world out differently. This is another thing that you tend to see when you start talking about expertise development, which is a really common thing to look at with eye tracking. As you get better and better at a given task, your ability to chunk it out gets better.

**[00:48:14]** When you're first starting to read, you're thinking about it on the letter by letter level. When you start getting better, you start thinking about it word by word until eventually you start thinking about reading in terms of, you know, it's not like, not necessarily sentence by sentence. Maybe phrase by phrase, you start learning. You gain the ability to scan and skim in a way that you couldn't if you were a beginner.

**[00:48:40]** Yeah, expertise development. It's the whole thing.

**[00:48:45]** Five, three, five, six.

**[00:48:53]** Yeah. And so you see me as I'm looking around the room.

**[00:48:57]** This is another place where the.

---

### Chunk 6 [00:48:45 - 00:58:44]

**[00:48:45]** Five, three, five, six.

**[00:48:53]** Yeah. And so you see me as I'm looking around the room.

**[00:48:57]** This is another place where the.

**[00:49:05]** It's actually not necessary. Basically, this is my eye. This is the camera of the world. And then let's say this is the depth that I calibrated at. The way that the calibration works is my eye is looking at this point and we calibrate it so that the camera is also displaying the dot at that location.

**[00:49:30]** But the reason why, but because the camera is not actually on my eyeball's axis. It's offset by a little bit. There is a vertical offset there. So if this is the distance that I calibrated at, if I'm going to look at something in front of that, the estimate is going to be above the location that I thought it would be. Whereas if it's something farther than that, it's going to be below.

**[00:49:58]** So if I calibrate it at arm's length and I look out into the world, the estimates are going to be off a little bit downward, I think. Or the opposite I might have gotten. That should be right. The people have cameras do try to do a little bit of correction for what's called vergence. So when, if I'm looking at something, it's easier to notice if I'm looking at it directly in front of me.

**[00:50:25]** If both my eyes are looking at my finger, they're crossed inwards in order to keep the image sort of aligned. And that remains true, even sort of out to a certain depth. But at farther distances, the angle that I'm tilting in is tiny, tiny, tiny. So this eye tracker does attempt to look at the vergence signal between the two eyes in order to estimate the depth that I'm looking at and then correct for this type of a thing. But I never know how much to trust that correction.

**[00:51:00]** So I can tell you, yeah, actually you can see it like I am looking at your faces, but it's showing me looking at like desk level because of the distances there.

**[00:51:23]** And okay, I think that's everything I did that's worth noting. So now I'm going to look at the actual data trace. But before I do that, I'm going to finish grabbing these frames. So VOR from 346. So I'm measuring just the frame numbers that the behaviors are happening.

**[00:51:52]** So that way later, when we're looking at the actual data.

**[00:51:56]** Oh, wait, is that going to work though?

**[00:52:13]** Be proportional.

**[00:52:17]** 693. Because I realized I'm pulling the frames from the world camera But I think the plot that I'm going to show you are in eye tracker timestamp coordinates.

**[00:52:31]** Okay. Then I do the finger thing, I think.

**[00:52:48]** Okay, so from 1141 to 1200, I was doing the horizontal saccades. And then I do 14 4. So let's say, let's say 1250 to 1400, I'm doing vertical. Okay. I think that's enough to work with.

**[00:53:33]** Yeah.

**[00:53:36]** So now let's look at the actual data. So everything we've talked about up until now. Well, so the RAW videos are raw data, and this video is not. This is not really data in the sense of what I usually mean as a scientist when I talk about data. This is a visualization of data, but it's not really.

**[00:54:04]** It's not set up to do like proper science about like you can't really do statistics on this kind of thing. So I'm going around saying, oh, yeah, look, I'm looking here, I'm looking there. I say, oh, you can see me make a saccade. I'm moving my ass from there to there. But I'm kind of just, I guess, for lack of a better term, eyeballing what's happening on the screen.

**[00:54:22]** I don't have the precision to actually do analyses here. And I don't have the kind of numbers I would need to be able to say things about, like the eye movements. In order to do that, I would have to look into the actual data traces and sort of look at the things that are sort of more better suited to actually extract things like statistics and velocities and positions in a more precise way. And in this case, let's see, that's going to look like looking at.

**[00:55:27]** Copy this path.

**[00:55:30]** So this thing which I did show last time, I'll show it again.

**[00:55:37]** Yes.

**[00:55:41]** So these are. This is some like this folder of exports is the derived data of the recording, which we derived, computed, whatever you want to say. This is the. When we got the raw data of the I videos and we did the analyses to track the pupil and all that good stuff.

**[00:56:06]** We basically, we can get those numbers from. For each recorded frame and then we'd write them down according to where we got them. So this is the data from the eye cameras and you see here, this world index, that's the frame of the world camera that we were looking at. So earlier when we were looking through the videos and there's a bunch of red crosshairs on a single frame of the video that happens because there is 1, 2, 3, 4, 5, 6, 7, 8, samples pulled from the eye videos for each frame of the world video. As we talked about last time, these numbers, basically each row is one observation of the eye.

**[00:56:55]** The eye ID is either 0 or 1 for the right or left eye. And then you have the confidence value and the position on the screen and stuff like that. So the video that I was showing is a data visualization. It's not set up to do like proper science about, but it is a representation of this data that is sort of better suited for our human brains. Right.

**[00:57:19]** Like, you can look at this all day and not see me make a saccade because these numbers are. There's too many of them and they're too precise. There's too many of them. But you put it as red crosshairs on top of a video and all of a sudden it makes sense to us.

**[00:57:36]** So, yeah, there's just always a sort of complex relationship between the intuitive interpretability of data and the hard level precision of it.

**[00:57:47]** And typically you want to have a little bit of both.

**[00:57:52]** With any luck, I should be able to process this. I realize I really should have done this. I did do that.

**[00:58:14]** Okay. I did do that. And.

**[00:58:26]** Okay, so this is a little piece of code that I wrote up to help me basically clean up this data. Because this data output has a lot of stuff in it. The different eyeballs are interleaved with each other. There's a bunch of information.

---

### Chunk 7 [00:58:30 - 01:08:29]

**[00:58:30]** Is a little piece of code that I wrote up to help me basically clean up this data. Because this data output has a lot of stuff in it. Like the different eyeballs are interleaved with each other. There's a bunch of information about the 2D estimates versus the 3D estimates and things like that. And so what I really want to see is just a singular trace that says this is what your, let's say right eye was doing at each sort of recorded frame of the, of the video.

**[00:59:01]** And the reason why I want to see that is because there are certain shapes that I expect to see when I look at those data. So time wise, doing all right, so if this is a plot that I, a plot that I've already generated, but let's do some sort of predictions here. And then this horizontal axis is time, which can be measured in frames, it can be measured in seconds, it could be measured whatever you want. And then let's say that this vertical axis is the horizontal position. So I'm looking from a top down from looking here versus looking there.

**[00:59:59]** You know, that's gonna, if I'm looking all the way to the left, let's say that's gonna be over here. Looking all the way to the right, let's say that's gonna be over here. Then when I'm looking, when I'm doing those saccades in this sort of phase of the recording where I'm sort of bouncing back and forth to the, from the different points on my finger, that's going to look like I'm bouncing here. And then I shoot over here, hang out there for a while, shoot over here, hang out there for a while, shoot out here, hang out there for a while. And so you're going to get these step functions here.

**[01:00:29]** And the fact that this slope is so steep is a testament to how fast your eyes move. If my eyes move slower. So for example, in the calibration part where I'm sort of smoothing my head, we're doing horizontal. If I'm moving my head back and forth like this, it's not going to look like these big square wave step functions. It's going to look more like a smooth transition because that's what my eyes are doing.

**[01:00:57]** And so you can kind of tell which system, which part of my oculomotor system is driving the eye movement by the shape that gets traced out when we look at the data on the plot that make rough sense. And then you know, similar stories. For the horizontal, there is actually this, this, this gets to a level of the oculomotor system that I personally am not aware of. I don't know, I can't tell you the details here, but I do know that we apparently handle horizontal eye movements in a different part of our brain than we handle vertical eye movements, which kind of weirds me out. And if I wanted to tell stories about that, I could say that, you know, horizontal eye movements have a lot of like, you're like generally searching around for stuff versus vertical ab movements is kind of like you're walking, you're kind of looking ahead.

**[01:01:51]** So when you're walking on the ground, you know, most of the ab movements are upwards. Like you saccade ahead, you track the point down. You saccada head, you track the point down. But anyways, just say that. Yeah.

**[01:02:09]** So without any further ado, let's look at these data so we can leave enough time to talk about neurons.

**[01:02:20]** So this CSV is the filtered data. So I have.

**[01:02:26]** Is that the right one? Let's preplay data. Yeah. So I just went through and what the code was doing was pulling stuff out of the previous, bigger recording folder. And so now there's only I0, which is my right eye.

**[01:02:47]** And that might be part of the problem. I do that really quick. Can I do that in a hurry?

**[01:02:57]** Filter df. Oh, okay, okay. I might be making a horrible mistake here, but that's okay. Just go ahead and do it.

**[01:03:27]** So I just realized by looking at it that I hadn't. I was going to say that I filtered out the eye and I also filtered out the method. And I was like, oh, wait, no, I didn't, because it's still in there. And then I realized that I had done that in two steps and hadn't cleaned up the step properly. So the data might actually be cleaner than I originally thought it was if and only if this actually runs in this moment, which we'll find out in a second if it does.

**[01:03:57]** Unbelievable.

**[01:04:01]** That never happens.

**[01:04:05]** So, yeah, so there you go. So there's the data.

**[01:04:12]** Any questions?

**[01:04:16]** Probably, yeah. Disappointing, right? Too much like, what's going on here? I promise you these nice, pretty square functions and square waves and swoopy things, and instead I get all this junk.

**[01:04:30]** Why is it so noisy when it could have been cleaner?

**[01:04:37]** What is the horizontal axis time? And so how long does it take to make a saccade? So if I'm talking about, you know, let's say we're looking at the part of the video where I'm doing big horizontal saccades. And so it's supposed to look like this, right?

**[01:05:03]** How big of a duration should this be?

**[01:05:08]** Like a minute? Is that an hour? Like a day? Am I going? Am I hotter or colder?

**[01:05:18]** Short. Yeah. Like, it's like less than a second. And so if you look at these, this is frame number. I really should have converted it seconds, but it's frame number and you probably maybe can't see it, but this is 25.

**[01:05:31]** So this is 25,000 frames on this horizontal axis. So the reason why it looks so noisy is because it's zoomed way, way out. And so this is the trace for the entire recording, as opposed to from this particular point where I'm doing that. Luckily for me, I know where that was happening so I can zoom in. And thankfully, I am using a method that does that.

**[01:05:58]** So I'm plotting theta and phi. Some people say phi, I say phi. I think theta is horizontal and phi is vertical. Pretty sure that's the case. But if I'm not, it's either that or the other way around.

**[01:06:21]** So I don't know if these are locked either. So let's zoom in that spot right there. I don't know why it's so slow. Yeah. So there you go.

**[01:06:36]** So now you can see the numbers are a little more tractable. We now have got from 1600 to 3200. So if you want to divide that by 120 frames per second, you can sort of figure out that time interval. And you see the noise, but you also see this shape. And so this shape happens.

**[01:07:01]** So in the vor, this is the problem with, oh, I got these numbers. Because this is where, like, these numbers, you have to, like, multiply them by four, I guess. So four would be down to, like 1200 to 700 would be for 4200. So, yeah, you know, so this is the part of doing this is the horizontal. This is the vertical vor.

**[01:07:32]** This is another one of those cases. Like, because I know how eyes move, I know that this is junk in noise. And I know that if I had a perfect eye tracker that was tracking perfectly with no error in noise, it would give me a signal that looks something like this. But this is giving me noise on top of that.

**[01:07:55]** And so basically, because of my knowledge of how the system works, I can. With my. It's hard because we have so many visual analogies, I can eyeball the data and know, okay, I need to clean out this noise here. However, what I cannot do is I'm not quite able to make that same kind of claim about this little chunk of data. Why are you so slow?

**[01:08:21]** So this is now a much smaller interval, so we got 820 to 1920. So this is about one second of data.

---

### Chunk 8 [01:08:15 - 01:18:14]

**[01:08:15]** About this little chunk of data. Why are you so slow? So this is now a much smaller interval. So we got 820 to 1920. So this is about one second of data.

**[01:08:30]** And you can see here, here, and then we bounce down here for a while. It's noisy in that phase, and it bounces back up. And you have a similar thing happening on the horizontal.

**[01:08:44]** This is tiny, and it's got these noise in it. So I actually can't tell you if this is real data or noise by looking at it. If I go back to the video and I do that sort of frame thing, I can look with my human eyes. I can look at the video of the eyes and sort of try to determine if it's moving. But even then, I don't know if this is within my range of my ability to tell the difference.

**[01:09:10]** And this kind of, like bouncing around noise, this could very easily be tracker error and not an actual eye movement. So this is a very common thing that happens where, like, for a certain level of precision, the data that you get is enough to make certain claims. But as you sort of zoom in and it zoom in more and more, you start to get to a point where I know that we do make tiny, tiny saccades. Like, we make teensy, teensy tiny saccades. Next time you have the misfortune of having, like, a coin in your life, just look at the coin and then notice that you can look at different parts of the coin.

**[01:09:51]** So, like, if you're looking at Abraham Lincoln, you can choose to look at his eye or his ear or his nose. And I will have to promise you that if you were in a sufficiently advanced eye tracker, your eye does move down to the level of, like, arc seconds. Arc minutes, maybe. Arc minutes. So an arc minute is 60 chunks of a degree.

**[01:10:12]** An arc second is things out there. And I think that we measure, like, micro saccades happen at the scale of like, a dozen arc minutes, I think even below. So my visual system does produce saccades that are on this scale. But. But I can't tell from this data set if this is a real one of those or if this is just tracker noise.

**[01:10:35]** And this is, again, something that has to sort of come out of a knowledge of the system that you're measuring and the precision of the data that you get out of the technology that you have available to you, given your budget and year of living. Yeah. In 20 or 30 years, I could tell you with very high confidence whether or not this was, like, with the eye trackers of the future, I could tell you with high confidence, but with the eye tracker that I had, with the calibration that I had, this is sort of within. At what we might call the noise floor of the recording.

**[01:11:18]** Okay, we are running out of time, as is tradition.

**[01:11:31]** But, yeah, and so these right here, these are the. And quite noisy, unfortunately. But, yeah, there we go.

**[01:12:15]** So these are again, it's very noisy, and I apologize for that.

**[01:12:26]** But this is also. I think this is a decent representation of what an eye tractor looks like, of what a saccade looks like with this type of an eye tracker. So. So this is the rough position of my eye. I make this big saccade, and then this little slope right here means that I probably made a saccade and then, like, move my head to catch up with it.

**[01:12:52]** And that's kind of a thing. Like, we tend not to hold our heads fixed. We tend to move our heads, and if we move our heads, our eyes counter rotate. That's the vestibular ocular reflex. So this type of thing where you see like a saccade and then kind of like a relaxation is very common.

**[01:13:10]** Where I kind of like. It's like move my eyes and then kind of move my head to fit, and then move my eyes and move my head to fit. Like, that's what you're kind of seeing here. Then I keep that fixation. Then I bounce down here.

**[01:13:21]** This is another sort of case where, like, I have no idea if this is real eye movements or if this is tracker noise. It's just that that's below the scale that we can make that estimate. But I can say that I'm looking. This is where my eye was in the head, like this. I trust this.

**[01:13:39]** I don't know.

**[01:13:42]** And then back and forth and back and forth, blah, blah, blah. And again, you can kind of see. So with eye movements, you have these saccades that look like square waves, and you have these slow, swoopy movements that are caused by the vestibular ocular reflex. And in. In the case where we're doing these, like, prescribed motions and trying to keep my head fixed, you see some sort of super, super supervenience of where, like, the.

**[01:14:14]** The two. The two types of movements are kind of like on top of each other. So even though I am maintaining fixation here, I'm moving my head. So the actual trace that you see is sort of like a combination of these two things sort of added together.

**[01:14:30]** Sorry, I'm kind of.

**[01:14:33]** My mustache is tickling my nose. Sorry.

**[01:14:40]** And I'm trying to find some Other stuff again, noisy, Noisy.

**[01:14:49]** Yeah.

**[01:14:52]** This right here. Where'd it go?

**[01:14:58]** This right here.

**[01:15:01]** This, gut wise, feels like a real eye movement to me. Like, this is probably around the smallest saccade I would expect, I would reliably believe the system could measure. And mostly it's because the data are kind of all in the same place.

**[01:15:25]** So looking at the difference here, like, even though it is small, it's consistent. And compare that to.

**[01:15:46]** Ah, come on. Why are you so slow?

**[01:16:00]** There's really no excuse for this to be running this slowly, like there's something weird going on. But. Yeah, so compare that, this little jump right here to like, this little spiky stuff right here where the data that's coming out of the eye tracker is jumping around from frame to frame. So each one of these Data points represents 8 milliseconds. So if this was a real eye movement, then my eye would have to be moving at that speed of like, jumping from one place to another within the space of 8 milliseconds.

**[01:16:32]** Which again, eyeballs just don't do that.

**[01:16:40]** Yeah, we're down here is back to the space where, like, I don't really know about this because also, yeah, you start getting, like, time scales and sort of a lot of complicated stuff.

**[01:16:52]** Okay, so where I want to get to now. Okay, I. Once again, probably not. We're not going to get to talk about neurons, because I someday in my life will learn the lesson that if my lesson plan involves the word. And it will not happen.

**[01:17:14]** But not today, apparently, because I want to find.

**[01:17:25]** I gotta fix this. Why is it so goddamn slow?

**[01:17:37]** Try to find some of the juggling stuff in the middle. Yeah, there you go.

**[01:17:44]** Oh, actually, you know what I just realized? Because the eye. The data in the eye is shaded on the. On the outer sides of it. I'll bet the horizontal eye movements are noisier than the vertical.

**[01:17:55]** Because. Because the gradient in luminance that I think is the cause of a lot of this error is a horizontal gradient, not a vertical gradient. So I should probably be looking at these vertical movements in the blue, but anyway.

---

### Chunk 9 [01:18:00 - 01:27:59]

**[01:18:00]** That I think is the cause of a lot of this error is a horizontal gradient, not a vertical gradient. So I should probably be looking at these vertical movements in the blue. But anyway, there we go.

**[01:18:18]** So this, this, despite the noise and the jitter and the goop, this is what eyes tend to look like during natural behavior. And this, honestly, even with the noise, because this noise is cleanable. Like, if I was to spend a little more time with this data, I could probably get a lot of this noise out of there and sort of get a cleaner signal out. But this is where you can start to see these kind of shapes on top of each other.

**[01:18:56]** This might be a blink or it might be a saccade, hard to say.

**[01:19:02]** But you can see how there's kind of these shapes. And then this is the horizontal, because I'm moving my head more. So you can see that these swoops are more sort of noticeable in that direction. And so like big saccade up here, head rotation down there. Saccade.

**[01:19:22]** So you can see like there are these saccades. Like I am moving my head quickly there, but then this swoop downwards, that's from my head rotating the other direction.

**[01:19:40]** Yeah. And then these are sort of the corresponding vertical eye movements. And these will tend to overlap each other probably mostly, although not necessarily, because like I said, sometimes we're generally not great at making diagonal saccades. We often will make left horizontal, then vertical, sort of vice versa, like that.

**[01:20:09]** But, yeah.

**[01:20:18]** Is there anything else I want to look at? Oh, it could be, yeah. So, yeah. So despite the noise in the data, you can still kind of see some ghosts in the fog here. And you can see like some of the trace of the nervous system of interest generating behaviors that were measurable, which is a lot, I want to point out, even though it's something that bears repeating and bears belaboring that we are.

**[01:20:58]** Now. I took some cameras on a 3D printed glasses frame, pointed them at my eyes, pushed record, ran some computer vision algorithms on it, and now we're looking at this data, which, noisy though it may be, it's valid. We could work with this. If this was the best we could do, we could work with this and we could generate the kind of data that you would need to do to get a publication and sort of contribute to human knowledge. And we're seeing shapes and patterns that correspond to neural activity in very specific parts of your nervous system or of my nervous system, I suppose.

**[01:21:41]** And that's just something, I think, kind of mind blowing, baffling about it, like how like Just the idea that you can. Like if I wanted to say that the people who have the most claim on neuroscience are the ones who are cracking open the skull and sort of putting electrodes into cortex, that's a pretty bold move on its own, but it's not surprising that you can do that and say things about what's happening in the brain, because it's a very, very direct measurement. This is not a direct measurement. This is a direct measurement of the position of my eyes. But the ability to interpret it in the context of eye movements requires a lot of.

**[01:22:29]** A lot of assumptions and a lot of knowledge. Like, I was trained in eye movement studies by people who have been. Who've been working on this for their whole lives and who were trained by people who've been working on it for their whole lives. And it sort of travels back through time and sort of like the ability to interpret these kind of noisy signals is not. I don't know, not to be taken for granted.

**[01:22:54]** It also is like a convenient. I don't want to say convenient, but the fact that we can measure eye movements with a camera didn't have to be the case. Like, it didn't. It's sort of. I don't know, you might call, like, convergent technological evolution there where, like the fact that we have this very particular way that we move our eyes, humans in particular, but primates and humans, primates, mammals, animals, anything with vision.

**[01:23:32]** The reality is the specifics about that visual system happens to have this effect that you can use a camera to measure the output and sort of the output of whatever part of the nervous system handles eye movements. And so, because we are clever, clever humans, we built tools that take advantage of that in order to give us a window into the nervous system that we wouldn't have otherwise if we had a different kind of visual system. Like if we were birds. And birds don't really move their eyes and their heads very much. They do a little bit, but their eyes tend to be an appreciable percentage of the mass of their heads as a whole.

**[01:24:20]** So they tend to move their vision around using their neck. That's like the chicken sort of stabilization thing. If we had a visual system like that, then the visual neuroscience of the chicken world would probably have a much, much more precise way of measuring head position, because that would have been the place that the insight comes from. So, yeah, it's a very.

**[01:24:51]** I spend a lot of time kind of thinking about the fact that I've built something of a career on the strange convenience of having the type of nervous system that produces a movement, that a readout that can be measured with a camera and some 80s, 1980s era computer vision. That's probably unfair, but relatively basic computer vision algorithms can track the eyes and give you a readout of the cognitive system and allows me to have something like throwing a ball back and forth and, and I can get data that tells me not only sort of where my body is moving, but also the information not only where my body is moving, not only the information that was available to me visually, but the location that my nervous system wanted to get the information from. When I make an eye movement, there's a decision that was made. I didn't.

**[01:25:58]** The level of my consciousness that's sitting here saying English words and thinking like that, I didn't make that decision. That level of my consciousness did not make the decision to move my eyes from here to there. But nonetheless the decision was made. And that decision was based off of whatever 40 years of experience of living in a world constrained by physics and however many years of experience throwing and catching balls was somehow baked into the nervous system enough that my, at this point in time, my oculomotor visual system said the best place for you to move your eyes in order to get the information you need to complete the task is here. And that decision happened hundreds of times in the several minutes of recording.

**[01:26:52]** And it happens continuously, you know, 100,000, 200,000 times a day. For us, we make these eye movements that sort of are based off of these, like little invisible decisions inside of our nervous system. So I think that's where we're going to probably leave that for now.

**[01:27:16]** But, you know, we'll talk when we get to this part where we're talking about my particular research. I'll show you some of the things that I've done using data like this to try to gain actual insight. In this particular case, the first thing I would do is record it again and try to get cleaner data. But this is, despite the jaggedy ness here, this is the kind of data that I have used to get like sort of real data and produced what could optimistically be called new knowledge, which I then took and threw on the giant pile of human knowledge and then went back and.

---

### Chunk 10 [01:27:45 - 01:30:59]

**[01:27:45]** Real data and produced what could optimistically be called new knowledge which I then took and threw on the giant pile of human knowledge and then went back and started doing it again. So yeah, I think we'll call that there.

**[01:28:08]** So yeah. So I'll see you all next week. Try to get your poster done by Monday. I also wanted to say I'm. Apparently the schedule is out and I am teaching a class next semester which I will be teaching the class.

**[01:28:27]** It's like a once a week elective class and the topic will be pretty much the same as this. Like I only really teach one class and it's this one over and over and over again.

**[01:28:40]** So if you are interested in this stuff I do encourage you to take it. There will be a lot of things that look familiar but it will kind of be at a higher sort of level and less of a focus on this like the poster project itself and more of a focus on like actually like gathering data and like trying to do something more resembling like an empirical research study with this. I think I'll probably get you all set up doing Skelly Bots, like building your own skelly bot thing on the first day and kind of have more of a back and forth between kind of lecture y stuff and sort of more nitty gritty hands on looking at recording data and looking at it, trying to generate insights from that. So if that is interesting to you, go ahead and sign up. I don't know if it will fill up but I think I might ask them to increase the class size or just whatever because you know, I think the way that I teach these classes like the size of the group doesn't really constrain very much because it's like either lecture or like small group kind of going around.

**[01:29:45]** So yeah, and you know it's like a lot of the way we teach classes is kind of like this very step wise thing of like you do this and then you're ready for the next level, then you're ready for the next level. And I think that's a little, it's a little bonkers. And I really kind of like just like, you know, if I, if I gave you like the exact same lecture again you would get different things out of it. So I think repetition is a very useful thing. So that's a little pitch.

**[01:30:12]** I don't know why, I don't really need to pitch. You can take your own classes. But just to answer the question of like because the topic is so similar, should you take it again? And that's kind of. It's obviously up to you, but, like the topic.

**[01:30:25]** I feel like these topics and the way that I teach are beneficial.

**[01:30:31]** I learn new things every time I give the lecture, and I'm sure you would, too, and you would have more of an opportunity to kind of like, dig into data and try to think about building actual empirical studies using this type of stuff. Small scale, obviously, because it's like a once a week class, but we'll do what we can.

**[01:30:52]** All right. And I didn't talk about neurons. I'll. I'll put that in at some point. It's.

**[01:30:57]** It's good stuff, but it doesn't have to take that long.

---
