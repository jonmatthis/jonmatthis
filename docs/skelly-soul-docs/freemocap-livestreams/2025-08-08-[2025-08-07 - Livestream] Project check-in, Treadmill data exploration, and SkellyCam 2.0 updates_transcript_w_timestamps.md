# Transcript: 2025-08-08-[2025-08-07 - Livestream] Project check-in, Treadmill data exploration, and SkellyCam 2.0 updates

## Source Information

- **Source Type:** Local File
- **File Path:** `C:\Users\jonma\syncthing-folders\jon-alienware-pc-synology-nas-sync\videos\video_eater_downloads\playlists\[2025+] FreeMoCap Livestreams\2025-08-08-[2025-08-07 - Livestream] Project check-in, Treadmill data exploration, and SkellyCam 2.0 updates\2025-08-08-[2025-08-07 - Livestream] Project check-in, Treadmill data exploration, and SkellyCam 2.0 updates.mp4`

---

**Total Duration:** 02:47:06

---

## Full Transcript

### Chunk 1 [00:00:02 - 00:09:59]

**[00:00:02]** Mm, okay. That looks better.

**[00:00:10]** I think I was recording or streaming at 4K, which is too many.

**[00:00:18]** Do I have sound?

**[00:00:22]** Probably. Hello, Hello, Hello, Hello, Hello, Hello, hello, hello, hello, hello. Ah, looks like I have sound.

**[00:00:43]** That seemed good. I think we're good. I think we're going. Oh man, it's been a second since I have done this. It's like a whole headspace that I gotta get back into.

**[00:01:00]** Don't want to be looking at obs. I think I don't. Wait, I want to look at the stats for obs, which look like this. Doing fine right now. Put those up there.

**[00:01:15]** And then I guess I can put. Put this on top of that or. Cuz I need to see chat. Right.

**[00:01:31]** And.

**[00:01:36]** Let's see. What am I doing?

**[00:01:45]** Okay, I can't see.

**[00:02:04]** Okay, I think I'm here.

**[00:02:09]** Do I get to see who?

**[00:02:21]** Okay, I think I am. Okay. So you're probably wondering why I called you all here today.

**[00:02:41]** Yeah, I think we're doing. I think we're in. Is there anything else weird that happens when I do that? It's been so long since I've clicked the stream button that I just kind of don't remember what the process is. I'm also, I'm afraid of like any like automated things I may have set up like years ago and then forgotten about.

**[00:03:07]** I don't think any of that's triggering. Okay.

**[00:03:23]** Okay. Yeah, let's go ahead and get started. What are we doing?

**[00:03:33]** Start drawing on this. Okay, so let me reset Wacom mapping to that one. Now I can draw like that.

**[00:03:47]** Okay, see, so 1100-021000-31000. Okay, so like 4, 1, 4 1000, 4, 4, 4 seconds of lag roughly between when I do something in real life and when it shows up on the stream, which is about what I have come to expect. So.

**[00:04:16]** Such a strange little headspace. You're just like sitting alone in a room with a. A couple lights blinking and you're broadcasting your life out into the world. So today we're going to talk about a variety of things.

**[00:04:33]** Going to give an update on Freemo Cap as a project. Just kind of like talk about where we're at with it. I'm going to show off some data that we got recently that kind of like represents about like a. Like a high watermark of, I think what we can do with just current status of Freemo Cap. I guess it's not technically the current status because it's using new stuff, but it looks like, hey, here's the data we can produce.

**[00:05:02]** So we'll do that. I'll talk a little bit about like Some roadmap to 2.0, which is very exciting because FIMO Cap has been sort of chugging along and it's like, you know, I guess V1 status and doing a good job. But we are, we have, we've, we're better now. We know, we know more, we can do more. And I am very excited to take the whole current code base and throw it into the garbage and replace it with a complete new from scratch refactor, which is ongoing and kind of like partially updated and stuff like that.

**[00:05:43]** So it will have many cool characteristics, including most importantly to me, at an emotional and spiritual level, real time processing. That says Real time processing. I guess I should probably spell that in a legible way. Real, Real time processing. Good enough.

**[00:06:13]** And then after that I will. I don't want to spend too much time on this and then I want to spend most of the time here talking about the current state of Skellycam 2.0 update, demo and etc.

**[00:06:40]** Because basically Skellycam, which is like the camera part of your mocap, is more or less working. Obviously there's always more that can be done, but. And it works. And it's kind of like it is the basis upon which the 2.0 software will be built. So the fact that Skellycam is working means that the rest of the situation should hopefully resolve itself without too much difficulty.

**[00:07:17]** Okay, All right, let's go ahead and get started.

**[00:07:40]** So Freemo capped the whole project.

**[00:07:45]** I don't know how long it's been since I've done one of these kinds of updates. It's probably years and so I don't remember where to start. So basically the situation as it stands right now is that freemo Cap is chugging right along. We have a extant version of the software. We've got, I don't know, something like three some odd thousand stars on GitHub.

**[00:08:08]** We got a Discord server with 2000ish people in it and like it's active now. People are in there doing stuff, talking about, you know, the work they're doing and there's people asking for questions and other people helping them out. And it's really amazing. We have received from the little like send anonymous data thing for all the people who have not unchecked that box. We have received, I think last I checked, like close to like 8500 unique IP addresses which are sort of proxied to hypothetical unique users.

**[00:08:42]** And from 120 or 130 something countries which is. That's the very exciting part for me so we got a lot of stuff going on and yeah we've been sort of just like. So there's the two versions of the software right now or I guess the two sort of main thrusts of the project there's kind of the existing 1.0 which has been. That's the one that's being. That's in use if you do pip install free mocap that's the one you get it's probably 1.6 something I think at this point and a lot of the work we've been doing in there is sort of a combination of sort of.

**[00:09:31]** It's mostly like maintenance work at this point like we're not really adding a lot of new functionality to it we're mostly like fixing bugs and kind of like making sure that people can use it in the in the main like the main user base and has a lot of little parts which I can talk about later but the yeah mostly it's been. It's like.

---

### Chunk 2 [00:09:45 - 00:19:40]

**[00:09:45]** The main user base and has a lot of little parts which I can talk about later. But the.

**[00:09:55]** Yeah, mostly it's been. It's like, you know, it's gone through a lot of changes, but it's also kind of roughly in the same. Using the same BASIC architecture that I was using when I sort of first wrote this code at this point years ago, which is basically, you know, a bunch of PI, qt, Python, QT gui. And it's like. It works, but it's clunky.

**[00:10:21]** It's kind of like the first one of these apps that I've really made. So just, you know, mistakes were made that kind of limit some of the development and.

**[00:10:41]** What.

**[00:10:46]** I don't know what that was about.

**[00:10:52]** Yeah, so it's kind of. It is what it is. And it's pretty sort of like, plateaued. And like, there's. There's some things that, like, should be easy fixes, but they're not just because.

**[00:11:02]** Because of the structure of the code. In addition to that, there is also the. Not yet fully extant. Sorry, one second.

**[00:11:34]** Yeah, I don't know what's going on there.

**[00:11:46]** Somebody's having a. I don't know what's going on. Sorry, one second.

**[00:11:57]** I've lost my momentum. I didn't really have any. Okay.

**[00:12:06]** Hello, welcome. Welcome. Neon X Death.

**[00:12:14]** Can you.

**[00:12:20]** I don't really know how to look at this.

**[00:12:28]** I wonder what just happened, but I just saw the viewer count just popped up to five, which is plenty. Hello.

**[00:12:44]** I don't know if there's a way to, like, see a list of people who's in there. I'm just curious if those five people are actually people or if they are, like, weird bots.

**[00:12:59]** Yeah. So this is what we're going to be talking about today.

**[00:13:06]** Guess I'm kind of restarting a little bit, but.

**[00:13:12]** This is why I can't look at chat.

**[00:13:21]** Okay, so let's move on. Yes. So FreemoCap 1.0 is extant and exists and works. Okay. Does its job decently, but is plateaued.

**[00:13:34]** Plateaued in its development and is, you know, like, it's. It's doing a good job. It does the work, but it's kind of like. It kind of is what it is at this point. And most of the work now is kind of.

**[00:13:46]** It's sort of twofold. There's like, maintenance on the 1.0. There's kind of like, a lot of polishing and honing of the output in terms of, like, making sure that the data that comes out of the 1.0 is like the highest quality for motion capture we can get, which I'm going to show some of that in a second here. And then there's also the ongoing development of the 2.0 architecture, which is going to be a wildly different situation from the 1.0. And I'll show a little bit of demo around that, mostly in the context of like where it's come to with skellycam.

**[00:14:23]** So let's. Without any further ado, let's guess I'll for good measure and we'll show the current state of the situation. So I'll just. I'll show Free mocap as it exists on kind of the main branch of the repository, which if you are, there's probably a link around here somewhere.

**[00:15:04]** There it is. GitHub.com freemocap freemocap this is the main code. This is the main branch. There's a lot. There are many other branches.

**[00:15:12]** There are many other repos, but this is the main one. And let's pull the most recent changes. Oh, not push. Nothing to push Friendo.

**[00:15:32]** And God damn it.

**[00:15:51]** If I join that from here, then I. That's in Free mocap. I type Free mocap. I mean, I might need to do other things first, but I think that'll do it. It should run.

**[00:16:01]** It does a bunch of this, like, goopy nonsense that the problem. It's like the good and bad thing about like doing proper version control. That didn't run, did it? Why not? Wow.

**[00:16:18]** God, that's old. What the hell is this error? I don't know.

**[00:16:30]** Oh, I probably need to nuke this.

**[00:16:45]** Probably should nuke this, but maybe that will be okay.

**[00:17:03]** Doing all sorts of stuff there, there on the screen. I can make you bigger.

**[00:17:10]** Okay, try it again. Free mocap.

**[00:17:19]** Doing a bunch of stuff.

**[00:17:23]** Might start yelling in a second. Nope, someone's mad about something.

**[00:17:31]** No videos found. That's fine. That's expected. Slot. Okay, so yeah, this main freemo cap and you know, it connects to the cameras.

**[00:17:38]** I'm not going to do that now because I don't really want to. Can I do this? No cameras connected. God, it's been a while.

**[00:17:54]** Since I've used this, but it'll be fine.

**[00:18:12]** Yeah, there you go. Look at that. Okay. Busted ass viewer. But it does do the job.

**[00:18:20]** Man, I can't wait to nuke this entire code base and replace it with 2.0. It's like. It does. It does fine, but it is just. It is like every.

**[00:18:30]** Every error I made at the beginning is now like the reason why it's not moving forward. And this is the reality of code and software and stuff like that. Is that it? The decisions you make first are the ones that kind of like, set the stage. So, God, I just can't wait to nuke this thing from orbit and replace it with something.

**[00:18:52]** Replace it with something else.

**[00:18:58]** Okay. But anyways, it works. Look at that. Look at that guy. Beautiful.

**[00:19:04]** So cursed as it may be, I've used it. I used it recently. It does the job. It's a good. It's a good software.

**[00:19:13]** I would be proud of it if I was capable of that emotion. But all I see with it now is, like, the things that could be better. And I'm happy that people, like, there's a lot of people out there using this right now, and there are a lot of people out there getting good results. Like, it does give good results. I'm very happy with the results.

**[00:19:29]** But as, like, a software, I have a lot of complaints. So. But let's look at. Let's look at some of the data that it produces.

---

### Chunk 3 [00:19:30 - 00:29:30]

**[00:19:30]** As like a software, I have a lot of complaints. So. But let's look at, let's look at some of the data that it produces.

**[00:19:46]** So I'm going to show you some hate computers.

**[00:19:58]** I'm going to show you some data that we recorded a couple days ago in the lab. And by we, I mean me and my grad student Aaron, who if you are in the server, is floating around asking questions under the name of Ron tc.

**[00:20:31]** And Aaron is doing his dissertation on getting his PhD in bioengineering and his writing dissertation basically on the challenging task of validating a scientific software, specifically markerless motion capture for use during biomechanics clinical research. And even more specifically than that, free mocap and whether or not it actually does a good enough job to be useful as a scientific and clinical research tool. So let's look at what we got here. So this was recorded from. So this was recorded with the new version of skellycam.

**[00:21:14]** So Skellycam 2.0.

**[00:21:18]** Which that.

**[00:21:24]** And yeah, but it is sort of backwards compatible with, you know, regular female cap. Because in the end it is a. Producing synchronized videos that get processed into the motion capture stuff. There's a lot to be said about that. But I'm not going to talk about that for now.

**[00:21:43]** Get into that some other future day. So let's look at the output. So this is a video of me walking on a treadmill using six USB webcams. The cameras are these little cheapo. I think I bought them in bulk for like 10 bucks a pop some years ago.

**[00:22:07]** And yeah, they are not good cameras, but they, they are cameras and they record at. I think they go up to 1080p. They do go up to 1080p but it gets weird around there. So we like. There's something, I don't know, I think they're faking it on the board or something like that.

**[00:22:24]** So this is recorded in 720p at 30 frames per second from six different cameras.

**[00:22:33]** By no means would you need six cameras. I think it's actually in many in this cases some of these views, like this back view I think is not doing anybody any favors.

**[00:22:46]** But we, we did six. Just to kind of like have a good representation of six camps of. Yeah, of like we recording with six both as a kind of way to like stress test the recording apparatus. And also the idea is that we'll be able to kind of like cross. Cross, what's the word?

**[00:23:10]** Like we were able to recreate the data with like different subsets of those cameras. To see kind of like how many are. To give some advice around how many cameras you should use, what configurations we should use. Although I know the answer is you should mostly do them from the front. So this is the Blender output there it is, I guess backwards for now, but we can flip that around by going into here.

**[00:23:31]** I don't think I can make this bigger for you unfortunately, but that's okay. Select the video parent. Make it visible. Select the video parent. Rotate in Z around.

**[00:23:44]** Rotate around Z by 180 degrees. Wait, not 1180. 80. There you go. And now it's not.

**[00:23:54]** No, it's looking that way. And let's turn it on. Yeah. So 6,000 frames, 30 frames per second. You can do the math of how long it is.

**[00:24:08]** I don't know. What is that, 2000 seconds? 200 seconds? 200 seconds sounds about right. Couple minutes.

**[00:24:18]** Yeah. And yeah, looks pretty good. So this visualization, the blender output here is. We've been working on it for a long time recently. Lion's share of credit should go to ajc27 who's been really doing some amazing stuff in here.

**[00:24:42]** Not going to go into all the details of like what's, what's present here, but this is the freemocat blender add on who lives@GitHub.com freemocat freemocat blender add on. It's kind of automatically installed to your version of the version of Blender that you specify.

**[00:25:07]** The free mocap thing, process data export, data export to Blender and you can choose your executable and then part of the standard processing pipeline creates this Blender file and then it also installs this. So if you, if You've ever processed FreeMap data with your, with a version of Blender you can go, go into your add ons and it'll be in there. You just have to activate it and then this thing will pop out and it will allow you to do a bunch of things that you can turn the armature on and off, track points on and off. There's a skelly mesh. So these are just the rigid bodies.

**[00:25:42]** That's kind of more of the, the base data that we're dealing with.

**[00:25:49]** And you can do a bunch of other fun stuff too. So real quick, I'm going to turn on this system console.

**[00:26:01]** And by the way, in this recording, I was walking on the treadmill and it started out at 0.5 meters per second, then it was bumped to every 30 seconds. It was bumped half a meter per second. So it's 0.5, 1.0, 1.5, 2.0, 2.5, and then back down to zero. So I can't remember what, what this would be, but probably around 2.0 at this point. And it should loop at the end.

**[00:26:25]** So, yeah, so. And then this, this little guy right here, that's my center of mass calculated from winter anthropometry tables relative to these rigidified bone segments. Much to be said, much could be said about the calculation of this data. God help us all. We use rigid body assumptions, kind of this basic model.

**[00:26:52]** And then.

**[00:26:55]** Jesus Christ.

**[00:27:00]** Do, do, do, do. And yeah, you can do all sorts of stuff. Let's. This is one I like a lot is. Oh, you can see me slowing down now.

**[00:27:11]** Let's look at the.

**[00:27:15]** Let's add a motion path to the center of mass. 30 before, 30 after. Oh, nice. It remembers that. And then we got that and I'm on a treadmill.

**[00:27:25]** So, like relatively constrained, but you can see the path there. And as I start walking, let's see. Can I do this? I can do this. Can I look at this?

**[00:27:44]** Hey, I don't think that'll work. I have to look at the empty.

**[00:27:54]** Aha.

**[00:27:56]** Normalize. Yeah, sure. Let's look at only the vertical height of the center of mass. Look at that. Cool.

**[00:28:10]** Wish it didn't look like that, but it does.

**[00:28:14]** Yeah. So that's. That's me walking. You can see there's this, like, really, there's. I mean, there's a lot of cool stuff you can do.

**[00:28:21]** So this, like, it should be pointed out that this is pretty much default, default of all the output aspects. Like the recordings are, I think, pretty good. I think we did a good job with like, the camera placement and the lighting and all that good stuff. It is using the new version of Skelly Cam, which has a, like a much, much higher synchronization between the cameras than the previous version, which I will talk about shortly.

**[00:28:49]** And.

**[00:28:56]** What was I saying? Yeah, but this is like, roughly speaking, like, straight out of the box in terms like, this is like, this is the kind of data that gets produced and the scientist in me has a whole lot of fun, mechanical conversations that we could have around this sort of, of like center of mass trajectory during the gate cycle. And. But I'm going to not do too much with it. I think I can do this.

**[00:29:18]** So I'm going to try to turn on the base of support. There's a bunch of really cool stuff again that Andres added, including this base of support calculator which uses a simple.

---

### Chunk 4 [00:29:15 - 00:39:14]

**[00:29:15]** But I'm going to not do too much with it. I think I can do this. So I'm going to try to turn on the base of support. There's a bunch of really cool stuff again that Andres added, including this base of support calculator which uses a simple like linear threshold of the feet. So basically, if the foot goes.

**[00:29:35]** If the foot is below a certain height, in this case 0.02 meters, which is 2 centimeters below the ground. No, if it's, if it's between 0 and 2 centimeters, it counts as on the ground. If it is. Whoa. What's all that?

**[00:29:54]** Why did that happen? Oh, because I clicked the wrong thing.

**[00:29:59]** If. Yeah, if it's above, it's not. And then it draws this fun little like, I think it uses geometry nodes for it.

**[00:30:07]** But you can see it kind of makes more sense when I'm standing there. And then you get this kind of vertical projection of the center of mass there.

**[00:30:17]** It works pretty well for how simple. Like a simple like linear threshold on the feet is like a famously error prone method of detecting foot contact, but it does a decent enough job and you kind of see how the base of support transitions from one foot to the other. So you got your single support phase of gait, you can see the center of mass. Because I'm moving at such a slow speed that it. Yeah, kind of like, it's like at slow speeds, walking is kind of like stepping on this one leg at a time without really a lot of like dynamics going on.

**[00:30:57]** At faster speeds, you start to built up more momentum and there's kind of a lot more sort of physics happening. So at the slow speed, you can see how the center of mass, the vertical projection and center of mass just sort of transitions from foot to foot. And the base of support transition from single support to stubble support is kind of like really interestingly shown there. You can see how like, at this speed, I'm maintaining like sort of static stability, you might call it, pretty much at all times. Oh, I think there's actually even a color coding.

**[00:31:27]** Yeah, it goes red to blue when it's in or out of the base of support, which is really fun. Oh, hey, Jawa. How you doing? Yeah, it's been a, been a long time, but we're, we're here trying to do stuff. Well, what's gonna happen here?

**[00:31:43]** Something's gonna pop up for a second. Oh, I know I'm gonna lift my arm, aren't I? Hey, hey, look at me go. See, I, I lifted my arm, which raised my center of Mass, which you can see in that output, which is always fun.

**[00:31:56]** And then if the walking speed goes. Oh, that's cool. So you can definitely tell this is probably another, like, arm raise moment. And then this is almost certainly the transition from a walk to a run.

**[00:32:14]** And then this is probably me hopping around. Yeah, yeah, I'm trying to. It's like I've been kind of, you know, working without the camera on. Well, the cameras have been on, but they haven't been streaming. But boom, there we go.

**[00:32:33]** I love it for a while, but I'm trying to. I'm gonna try to start getting into a more regular streaming schedule, which I feel like I always say, but it remains true.

**[00:32:44]** But yeah, see now, as I'm going into this run, the sort of mechanical definition of a walk versus a run is that a walk has a double support phase, meaning a point where both feet are on the ground. A run has a doot, doot, doot, doot, doot. Flight phase. Look at me go up in the air. We.

**[00:33:06]** How can I do this? Okay, shift S. No, shift A. Oh, wait. Also screencast keys. Come on. Come on, buddy, turn them on.

**[00:33:20]** No, turn on. Great. Shift a mesh plane. I know how to do this. I've done this before.

**[00:33:31]** Scale. Actually, I don't use scale. It's a treadmill. And I give it a color, give it a surface.

**[00:33:44]** I've done this before. I've done this before. Principal. Oh, there it is. Checker texture.

**[00:33:52]** And, er, this is going to be blue. And this is going to be also blue, but darker again. This like weird optical illusion space where the color stop making any kind of sense. But that's okay.

**[00:34:12]** Darker, Very dark. Look at you go. Then I make it. Oh, like that. And then I make it.

**[00:34:25]** Yeah, like that. Great. And then I go back to where you're standing still and I zoom in to your footsies and. Nope, click on that. Hey, calm down, calm down.

**[00:34:39]** Click on that. Ah, yeah. Yeah, that works. This has also been. The ground plane has been aligned using the new Charuco ground plane alignment method, which we have for finally.

**[00:34:57]** What's the word? Implemented. And by we, I mean Aaron. But I asked him to do it, so I get credit. Which basically is now in addition to our standard calibration pipeline.

**[00:35:08]** Oh, man, look, this thing is literally dusty. It's been a second. In addition to the traditional charcoal dance, if you. I think it wants to see, if you put the board on the ground, it will use that detected location to like, define the ground plane. So before we.

**[00:35:31]** We didn't really know where the ground was and we would detect it from where the feet were, which can be okay, but it's a little bit. It's screwy for a number of reasons. Now we actually detect the ground plane and we will be. I think all the changes are actually in the main branch right now. Actually I can check real quick here if I check process data.

**[00:35:53]** Yeah. Uchiruko born as ground plane right there.

**[00:35:58]** This needs to be changed. This is a task. This is like a front end task. We need to change the text here first of all so it's not cut off and secondly so that it says something like use first frame of charuco ground plane because like there are docs, they are elsewhere. They are not visible from here nor from here.

**[00:36:20]** And there's no way to know from looking at this that you have to have the board on the ground at the beginning of the recording. I can't remember if he, Aaron had something that was like it might, it might be clever about the way it detects the board. It might look for it to have like low velocities or beginning and end but I can't remember.

**[00:36:45]** And.

**[00:36:50]** Yeah, but we should, we should change that and we will.

**[00:36:56]** But yeah, it does a good job. There's the ground plane and what was I doing this to begin with? I was doing this to begin with so that I could look at this and say, hey look, there's a flight phase.

**[00:37:24]** We'll leave it for now.

**[00:37:31]** Let's plot some more trajectories. What do you say? I like trajectories. Trajectories are fun. They show you what's going on.

**[00:37:39]** So that. So we're looking at the center of mass trajectory. We can also. Oh, we can't do this from God, look at that. That's so cool.

**[00:37:49]** Look at me go. I'm standing on the ground. So as I go forward there's this kind of. So it looks like I'm on just my toe here, which I guess we can check into. The image may or may not be true.

**[00:38:10]** In that case it looks like I'm pretty flat footed. But you know, this is the problem of a linear threshold. And I bumped it down dramatically. I think it was originally at like 0.1, but then everything was showing as ground contact. So then I.

**[00:38:25]** It's now erring on the side of not enough.

**[00:38:29]** Famously difficult task to determine if the feet are on the ground. But the linear threshold is the classic response.

**[00:38:43]** But yeah, there we go. So as I go forward. Yeah, I think it detects it when I first hit the ground. And then there must be some wobble either from, like, my actual foot motion or possibly, like, you know, as the feet start to cross over in the back. There might be some, like, weirdness in there going on, but I just like it because it's like, as I hit the ground, boom.

**[00:39:04]** It's, like, pretty close. Underneath where I'm standing, you can see the center of mass, the vertical projection. Center of mass right there in the base of support, which is where it needs to be so I can bounce around.

---

### Chunk 5 [00:39:01 - 00:49:00]

**[00:39:01]** But I just like it because it's like as I hit the ground, boom. It's like pretty close underneath where I'm standing. You can see the center of mass, the vertical projection. Center of mass right there in the base of support, which is where it needs to be so I can bounce around. Speaking of that, I'm going to turn this on.

**[00:39:18]** This is not connected to this, to the motion trajectory thing, although it should be. It might be a little bit tricky to do, but I can do this and then do this. Around frame, same vibe, 30 by 30. That's probably more than it needs to be, but that's okay. Calculate around frame, scene frame.

**[00:39:41]** Don't show the keyframes. And then. Yeah, so now you get to see that this is the trajectory of, ah, this. No, this, that of the center of mass projecting on the ground, which is it? During like on a treadmill, it's sort of, it's like very constrained.

**[00:40:05]** But if you go back to the slower phases of the thing, you can see it's kind of like transitioning from back to back to forth as it's going into the base of support for each foot as I take steps on the thing.

**[00:40:26]** Love that. Look at it go. So yeah, I mean, so we got, we stopped to keep doing the validation and all that kind of stuff. But as a professional research scientist who has studied gait for some number of less than two, but more than one decades, this is like absolutely. Oh, there's got, there's an ad coming.

**[00:40:47]** I can't smooth. I've been snoozing the ads, but I can't snooze them anymore. So there's gonna, an ad's gonna play in five minutes. And I'm sorry, But yes, I will say as a researcher, as a scientist, as a peer who has reviewed various things, this is absolutely like scientifically usable data. Like obviously we will continue to do the validation, but I'm telling you this is as good.

**[00:41:18]** I mean like, I don't have a lot of respect for traditional motion capture. Like I'm, I'm doing it like I'm wearing it. Like we're recording like qualysis data and we'll do the comparisons. But like, I'll tell you this right now, we're still working on cleaning up that fucking data so that we can even look at it. Whereas this came out of the pipe the second you push the button.

**[00:41:41]** Well, the second you push the button and wait like an hour. But beside the point, like zero manual labor to get this data versus whatever garbage you're going to get out of the stupid Qualysys system, which, just to be clear, cost a quarter million dollars in equipment and software. Whereas free. Mocap, as you may have inferred from the name, is actually free. Software is free.

**[00:42:01]** Cameras cost money. You got to buy your own. But we will soon. We'll sell you cameras soon. There's a shop.

**[00:42:07]** We're making it. It's a whole thing.

**[00:42:12]** But yeah, look. Look at me go. Okay, let's add yet another trajectory. Specifically, let us examine the heel. I'm not sure if it will let me do this without the markers visible.

**[00:42:31]** Let's try. No track points now. Let's try and let's change the color so this color of blue to. So blue is before and then say orange is after. So the blue part.

**[00:42:52]** Can I do that?

**[00:42:56]** Yes.

**[00:42:59]** I don't like it. It's ugly.

**[00:43:04]** Let's do this color and.

**[00:43:10]** Maybe green. Sure. Still ugly, but we can live with it. What are they saying?

**[00:43:22]** Trajectories? Yep, that's a heel trajectory, all right.

**[00:43:30]** Like that's roughly what they look like. Again, there's a little bit of this warble down here, which I suspect is being caused largely by like the feet crossing over. And like, you know, the weird like, like this is not like we're still using media pipe, which is, you know, not the best in the world, but it's also markerless, which has its own sort of situation. And as you can see as it like, like the feet kind of swim around on each individual track and then they get particularly warbly when the legs cross over. Like from the point of view of that camera, there are many, many layers of post processing between these images, the 2D data and then like the finalized 3D data you're getting here that mostly clean up a lot of that.

**[00:44:16]** But you know, we still got to take some account for that. But so in terms of like the data that we're getting, and this might be where the validation stuff really helps. Like there's some warbling on the ground during that step flight phase, which is probably not real, but it's also not particularly pronounced. Look at it. When slower phases dwink, Normalize, then zoom in.

**[00:44:57]** Hey, there's probably a keyboard shortcut that does this for me, but yeah, so again, I've been. Yeah, as you can see, this is a little more pronounced. So you can see that kind of these little like, like the little waves it does on the ground. I mean, it's possible that that's an actual foot. That's like this is like.

**[00:45:22]** So this is where you get into the space of like it's possible that's what my, my foot was actually doing. But it's also sort of like possible that's an artifact of the data. And seeing as how we're using this tool as a way to measure what my foot was doing, you kind of get stuck in a difficult spot there. But. So when we get the data back from the Qualysys marker based system which uses markers on the body, we'll be able to compare those trajectories and then I trust those differently I guess than to the regular, than to the sort of whatever the mediapipe marker list derived foot trajectories.

**[00:46:05]** Look at the toe. Left heel, left left foot index. Hate that stupid name for a thing, but that's okay. Blue and red and add motion trajectory.

**[00:46:25]** And let's take the heal off.

**[00:46:32]** Yeah, it's a little more. It's a little bit of a stranger shape but generally speaking looks quite good.

**[00:47:10]** Okay. God, I hate ads. And I'm so sorry. I want to learn how to. I'm going to figure out how to multi stream to YouTube as well as Twitch.

**[00:47:19]** So you don't have to watch ads to watch me. Although I will say having 30 seconds where you know people aren't watching you is not the worst thing for the old psyche waiky, if you know what I mean.

**[00:47:33]** What was I gonna do here? I think I was just gonna say how. Yeah, I'm excited. I'm excited about this. For the animators in the room.

**[00:47:43]** There's this whole sort of business down here in the add on around retargeting to different armatures and you can set different source bones and sort of all sorts of stuff going on here. I don't really know how to do that. It's kind of like Andres has explained it to me. I've seen him do it. I may have even done it myself at one point in my life.

**[00:48:04]** But like I'm not, I'm not the guy I talk to about that. He is, he's in the server and he answers a lot of questions. Kind of seems so grateful for his presence in general, both in terms of the work he does and also just like the way he helps out in the server. But people have been successfully using that to retarget the free mocap data with the standard the way that we made it, which is loosely based on Rigify. But we kind of have started doing our own thing.

**[00:48:37]** People have. Oh wait, people can still watch if they have a prime subscription during the commercial. That's okay. I think that's. You get to see me go.

**[00:48:49]** That's your. You can buy that with money. But, yeah, people have been successfully using this retargeting stuff to.

---

### Chunk 6 [00:48:45 - 00:58:44]

**[00:48:45]** Think that's. You get to see me go.

**[00:48:49]** That's your. You can buy that with money. But yeah, people have been successfully using this retargeting stuff to retarget the. The Freemo cap armature data onto Mixamo unreal. Probably some others.

**[00:49:10]** You know, it's kind of. I check in on what's going on in the server and I occasionally see these conversations around like, hey, I'm trying to retarget this to that. And then Andres comes in or someone else comes in, like, here's how you can do that. And then typically those conversations resolved by them saying, okay, great, it worked. And then they just disappear and never come back.

**[00:49:27]** So I hope it worked and I hope they did something cool and I hope they come back and show it to us someday. People do show it to us sometimes and when they do, I am very grateful for it. But, you know, who knows?

**[00:49:40]** Look at him go. Look at this. Look at this absolute darling, this skeleton friend. What a friendly skeleton. Look at him go.

**[00:49:55]** $0. There's all these systems out there that like they charge you so much money and I. Their data. I mean, I don't know, I've never, I haven't actually like, like deeply examined the kind of data that comes out of one of like the paid markerless MOCAP systems. But I would not expect it to be like empirically valid.

**[00:50:14]** I think they very explicitly utilize like non truth preserving data cleanup methods.

**[00:50:27]** And you know, I guess I'll judge them for that. I was gonna say we. I was gonna say something a little more magnanimous. But I think at this point, I think at this point I have beef with the paid people. Not because I think they're bad people, but because I'm morally opposed to their business model.

**[00:50:47]** Like so, yeah, Skelly champion king skeleton or queen pronouns he. They. In my particular case, it's a he skeleton. I really wish, someday, I hope that someday we'll be able to have kind of like a hot swappable sort of. What would be the right way to say this not gendered skeleton, but skeletons associated with pubescent experiences of different combinations of androgenic hormones.

**[00:51:28]** That's not right. Anyways, it mostly would just be like a bigger or smaller pelvis with a larger or smaller opening. But for now it's just a generic skeleton who is, you know, somewhere in the middle.

**[00:51:44]** Thank you.

**[00:51:49]** Look at the knees, man. Look at them go. They're so good. It's a. It's really fun to me because the.

**[00:51:56]** So in terms of the recording Pipeline it goes record the raw videos. You do the 2D tracking on the videos, you triangulate the data and so you get. Oh, not those wink. So you get these guys.

**[00:52:14]** And so those are the triangulated points mostly. And then you connect the dots and you do a. What's called a.

**[00:52:32]** Human generator and editor. Looking at this thing you just sent me.

**[00:52:39]** Yeah, we could probably utilize that thing that very well. Oh, make human. I see. Yeah, yeah, it would be. Yeah.

**[00:52:53]** Right now we're kind of focused on Skelly. The Skelly meshes because it's easier. But yeah, we can definitely like the idea is to make, to make it kind of hot swappable for different armatures and meshes and all that good stuff. What was I saying? I was blathering about something or other.

**[00:53:13]** Yeah. So we get the joint centers which are roughly sort of correspond to the dots on the tracker and then we compute these rigid bodies which basically is we do some cleanup and sort of, you know, gap filling and you know, Butterworth filtering. And then we do a rigidification process where we as the data is noisy, we sort of fix the distance between the markers so that the segments are fixed length. And then we. And again, when I say we, I mean mostly Andres have some complex system to scale the mesh to fit the data.

**[00:54:03]** And I'm actually not this, this is not yet in the main add on. It's in, it's in the main add on. It's not in the version of the add on that's being called from the. The standard GUI yet. Although when we push this new version that this, this is from.

**[00:54:20]** This is running from the source code on the main branch. Once we push this to pip, we will have updated the version of the blender add on that it uses. And that version has a pretty significant upgrade in the way that it does the mesh scaling to fit the data. And it's pretty nice. Like you'll be able to tell like, looks like the mesh looks a little smoother.

**[00:54:47]** Like it's more sort of like the topology is a bit nicer but you'll also be able to tell because like the joints look better. Like in the previous one. Like the femurs were flipped or there was something going on, but now they look really nice and like, can I do this?

**[00:55:10]** I like it because the bone arrangement is not like we didn't really carefully control that too much. It just controlled like the head and the tail and kind of. It just kind of lines up because of course it does. Because it has to because that's the rigid body assumption. We kind of pretend like we're tracking this complicated skeleton structure when in fact we're actually tracking, like a bunch of connect the dots points.

**[00:55:38]** And so, again, this is where you kind of have to rely a little bit on, like, my experience as a. As a. As a researcher. But the movement of the knee during gait here is like. Is pretty good.

**[00:55:51]** Like, I would not expect to see better results from, like, open sim. Like, I would not expect to see better results from kind of. Kind of anything. So just like, the way, like, the patella isn't really following, obviously, because it's rigidly attached to the femur, but the way it kind of swings forward, like. That's.

**[00:56:18]** That's correct. That's how it should be in the way that the. This. God, what's it called? The.

**[00:56:24]** So this guy here is called the greater Trochanter. This guy here is, I think, just called the femoral head. The way the femoral head fits into the hip socket and the way that the. The femur sits on the tibial shelf. Like, it is, like, frankly, kind of shocking to me how close to, like, the anatomical reality it is, considering that we're only tracking it from just two points.

**[00:56:53]** Look at him go. Okay, and then the center of mass is just always a lot of fun.

**[00:57:03]** I guess I do a little bit of jumping here at the end.

**[00:57:08]** Jumping is kind of always a nice way to show what the center of mass is doing. But I'm also on a treadmill, so.

**[00:57:16]** Dwink.

**[00:57:32]** Wiggle, wiggle, wiggle, wiggle, wiggle, wiggle, wiggle. Bounce, bounce, bounce, bounce, bounce. Yeah, so you can see it's like this. So this is the vertical. Vertical trajectory.

**[00:57:43]** A time series of the vertical projection. No, not the vertical projection. A time series of the vertical position of the center of mass in the recording. So each little, like, hump, there is one sort of cycle of gate. And then you can see it kind of as things start slowing down, I kind of start wobbling around.

**[00:58:07]** And then right around here, I'll start hopping because I'm wee. Because why.

**[00:58:24]** Yeah, nice trajectory.

**[00:58:34]** Oh, you know what I could do? I'm going to do this one thing, and then I'm going to transition over into Skelly. Skelly cam territory because I could.

---

### Chunk 7 [00:58:34 - 01:08:29]

**[00:58:34]** Oh, you know what I could do? I'm going to do this one thing and then I'm going to transition over into Skelly. Skelly cam territory because could grab. Okay. I'm going to grab the origin of the whole business and I'm going to go.

**[00:58:58]** Go back to the beginning.

**[00:59:06]** Yes, I can do that. And I'm going to say grab. You can. I do. I want to do timeline and I want to do auto keying.

**[00:59:18]** Don't want auto keying. Yes. And then.

**[00:59:35]** Hello, Micah. I knew you'd show up eventually and called me a legend. I knew it would happen.

**[00:59:45]** Bye, Megan. Thank you. Yeah, we're back. We're doing it. We're streaming.

**[00:59:50]** We're trying to stream more regularly. We're looking at. We're looking at some data and specifically I'm gonna try to cheat. Oh wait, is that what I want?

**[01:00:06]** Doink.

**[01:00:09]** Yeah. Okay, so during this speed. Yes. So I'm going to go from here.

**[01:00:26]** I'm going to move this guy somewhere. Oh, wait. Okay. Grab and y. I'm going to move it out here. Sure.

**[01:00:39]** Oh, I can control that. Nice. And so now if I turn off auto keying, then it probably won't fit, but it's like theoretically it would.

**[01:00:52]** There you go.

**[01:00:56]** So if I wanted to, I could match this. Go. I could try to match the speed to the speed of the treadmill, but which would like make the feet not slide on the ground, which would sure would be fun. But I'm not going to try to hit that too closely. But I am going to clear this and re.

**[01:01:15]** Add it. And then now not that. Oh, oh, oh, oh, oh. Run that. Okay, so it's too far.

**[01:01:27]** I'm being chased.

**[01:01:30]** Nice. That's cool.

**[01:01:35]** Non veridical, not scientific data, but you know, fun for looking.

**[01:01:45]** It's like definitely too far.

**[01:01:50]** Thank you. It is a nice skelly rig. This is the. Yeah. Come a long way.

**[01:01:57]** Owing mostly to ol. Andres. Wait, not that one. I want to do this one. Yeah, and then that guy.

**[01:02:05]** It's going too far. So it wants to go less far and see if I can do the left heel. Clear all motion paths. Not motion path.

**[01:02:24]** There we go. That's not far off.

**[01:02:32]** Okay, zoom in, Zoom in to him. There you go. And do this. And then. Yeah.

**[01:02:42]** And then we pretend we're walking.

**[01:02:46]** Yeah, that's not bad.

**[01:02:50]** I'm gonna turn these. All right, guys, you gotta go, you gotta go, you gotta go.

**[01:02:57]** Alt P. Clear parent. Bye. And now we click upon him once again and we go back to Here. Oh, but these guys are still there. And we grab all of them and we say grab NY back there.

**[01:03:12]** And then we push play and there we go. Haha. Look. It's like we're walking for real, except not. It's like we're walking on a moving pathway.

**[01:03:26]** The Skelly is rigged. That feels like something that. I don't know, we could probably do something about that. Like the right way to save all the data to make it like, easier for all parties, particularly animators, is something we're sort of continuously working on.

**[01:03:50]** But yeah, I'm mostly working on the like. Most of my like scientific. Oh, Jesus. Why? Ah, get in there.

**[01:04:02]** Most of my scientific interests are in like this data and this data and this data is kind of like. I'm just not familiar with it. So I. Part of what we're kind of like trying. So like, the project is kind of trying to transition at this point because it has gotten big enough and complex enough that it's.

**[01:04:25]** It's like, you know, we need to kind of start outsourcing a lot of the work. And so, and that's. It's. And it's working. We're kind of getting there.

**[01:04:35]** People are helping out. But I'm trying mostly to get more useful information, like out there into the world so that other people can kind of help out. So that is to say, old Jawa 64, if you have. If you're like, God, the data is this way. And I sure wish it was that way.

**[01:04:54]** Like, if you can find a place to like, just put that information out there, like write something up on a GitHub issue or post in the server, we will take it into consideration. I can't promise we're going to divert all effort towards making you happy, but it will definitely be something that we think about in terms of. Especially if you start going into the 2.0 and start thinking about how we want to start packaging the data and what we want to make available and this and the other place.

**[01:05:23]** But yeah, Skelly is rigged. He says, oh, it's a joke. See, I don't know. I don't even know enough about animation to know what that is because it's always like, people have all these opinions about, you know, what should go where. And I just.

**[01:05:39]** There's like a point in the process where I just kind of have to like, give up, give up control.

**[01:05:48]** But yeah, what a champion. Look at him go.

**[01:05:54]** Okay, let's do this. I'm gonna take that. I'm gonna say, oh, go away. I'm gonna say you, your location is in now and has always been item zero. Bye.

**[01:06:10]** And I'm gonna go zoop. Look at you. And then I'm gonna probably go, Oh wait, I can do this. Ha. Got all that space.

**[01:06:41]** Oh, I do need to recalculate.

**[01:06:47]** Clear all motion paths, add motion path and yeah, let's do that. Let's give you, let's give you a center of mass path too. Oh, let's give you a base of support. Let's give you a center of mass. Let's give you center mass, motion path and then let's get rid of your armature.

**[01:07:10]** Let's get your trap points. Let's get. You don't need to be here anyway. And yeah, you're looking, looking grand.

**[01:07:25]** Cool.

**[01:07:30]** Yeah. So this is roughly speaking the, I would say the high water mark of the current version of FreeMap. FreeMap 1.6.3, I think. Although I guess this technically the stuff you're looking at now will be 1.6.4, which was generated with roughly this software. Different method for recording the videos which I will show in just a moment here, but processed with just regular old.

**[01:08:01]** Click this button and wait for a little while and then open it up in blender and then use the standard. This is all blender, the standard blender out on. And so it's pretty good. I'm pretty, pretty happy with it. Pretty stoked about it.

**[01:08:17]** And yeah, Aaron, we are going to continue to do like the proper validation and the proper sort of comparisons between the free mocap data, the traditional marker based data.

---

### Chunk 8 [01:08:15 - 01:18:14]

**[01:08:15]** Pretty happy with it, pretty stoked about it. And yeah Aaron, we are going to continue to do like the proper validation and the proper sort of comparisons between the free mocap data, the traditional marker based data, looking at, you know, the effects of different trackers and different cameras and all that good stuff and then at some point publishing like a proper validation study of, of the tool so that you can justify in your grants and papers using it. But if you don't need that level of justification, you just need some guy to tell you whether or not it's good or not. I'm here to tell you it's good. The data is good.

**[01:08:56]** The pipelines are robust and reliable. The data model output is like decent enough. Like you can definitely like CSVs and NPYs. You can get the data trajectories out of there pretty directly. The data is exported into the 3D model, is exported into BVH and FBX.

**[01:09:15]** If you are a researcher and you don't know what BVH is, look it up. It's like that. We should be using that more I think in the sciences. But.

**[01:09:29]** Give me a heal. Oh wait, give me a heal now. Oh, interesting. Goes away if I turn that on.

**[01:09:43]** Yeah, A lot of things to say about the cameras and sort of like the optimal configurations of cameras and whatnot. But long story short, three. Three cameras in front, one on the main, two flanking the side. That's about the best, sort of, that's generally speaking like the best orientation that we get. Make your scene really bright, get your exposure as low as you can while still seeing what stuff in the image and then, and then don't use the busted viewer to look at the data.

**[01:10:16]** Use. Use Blender.

**[01:10:22]** Yeah, much more to be said about that. If you have any further questions, check the docs, the documentation. Yeah, I don't like FBX at all. Fbx. It's like it's the one, it's.

**[01:10:33]** It seems like it's the most standard in a lot of applications. But yeah, there's like a million different versions. It's like binary. I just, I really don't like it. But.

**[01:10:44]** So we output in, in our 3D models, export like in. In the recording folder. In the 3D model folder we export FBX and BVH.

**[01:10:59]** Autodesk uses. That's really funny. So one of the things, so one of the aspects of like this version of the software is earlier in the stream I was mentioning, it's kind of like plateaued in terms of the complexity that it can handle and so there's a lot of things that like in a standard software you would have a lot more like options about like how to out, like I want to output this data in this format or that format. Like right, like Blender has, you know, the file has like the export and you can, you can choose to export things in all sorts of different formats. The 2.0 version of the software of FreeMap will be sort of designed with more modern app development tools and just sort of generally more sophisticated architecture.

**[01:11:54]** And so the hope is that we'll be able to just offer users like options on what they actually want. This version of the software we're really fairly constrained to have kind of just like we have options in there, but like it's not robust, it's not super clear how to use things. And you know, so it's a little like there's anti patterns everywhere and like just general problem. So we have been living using a strategy of just kind of like dump a bunch of standard files into the recording folder and then like try to make it as obvious as we can, try to make documentation as clear as we can and then just kind of like trusting users to like be able to do what they want to do. Which is a little bit counter to like our standard philosophy of like universal access, but it's also kind of like, you know, is what it is.

**[01:12:47]** And. But yeah, in the future we should be able to have a more robust like exporter that would allow you to sort of like make your own choices, which will sort of also hypothetically be set up. And this is kind of where some of the opening of this project comes in. Once that architecture of like an exporter for freemocap is kind of in place, it should be then easy or easier for members of the community to say like, hey, I want a USD exporter. Like, and I would say, great, here's the instructions and templates on how to build an exporter for free mocap because, you know, just with like available time and whatnot, like USDA people really like USD, people like gltf, people like, you know, I don't know, people use Dae collada, you know, oh, Mikael Rollerball, whoever they are, has a lot of, I think super valid opinions about whether the data should come out in like narrow, tidy format or wide format.

**[01:13:51]** Like, should it be a parquet file, should it be a CSV, should it be a TSV, should it be a SQLite, should it be all there? And in the future what we want to do is want to continue to maintain, I think the policy of sensible defaults where we as the developers make the decisions about what should happen when you push the big friendly button. By having sensible defaults and a relatively one click single big friendly button pipeline, people who don't have experience and therefore don't have opinions have. It will have an easier time sort of producing data that they can use.

**[01:14:43]** And in addition to that we also can start building a more robust exporter method so that people who do have experience and therefore do have opinions can sort of make those decisions. Say actually I want, I don't want the tidy format, I want the wide format. And then so you as a user can get what you need. And then also if we do it properly build the software and it's sort of like a clean architecture, it will also that structure will lend itself to more like community developers, which is sort of really necessary for this type of open source project. Because once we make our sensible defaults, if we do that intelligently, we will sort of leave a lot of useful breadcrumbing and scaffolding and templates that would allow people to come along and say, oh, I want to build a USD exporter capacity.

**[01:15:32]** And so you do that. Give the pr and we say thank you. We check it and we say now when someone comes along and says hey, I wish. Hey, can you export USD? The first person that asks that we say no, but you can make that code.

**[01:15:44]** And then they do it and then they. And then the second person that comes through and says hey, do you export to USD? We say yes. Thanks to user XYZ who helped us write that code.

**[01:15:58]** More than one cam and not if you have it set up. Oh, oh yeah. Thank you Jawa for answering that question.

**[01:16:09]** Yes. So the question was do you have to do the calibration board currently? So yes, for multi camera recordings. So as Java pointed out, if it's a single camera recording, no you don't. And in that case you'll get just kind of like the Flat Stanley version of the data which we do save out.

**[01:16:32]** Like MediaPipe produces 3D data, but it's kind of garbage so we save it to disk. But the blender stuff is just based off flattened data. If you want to do multi camera recordings then you do have to do the calibration which will probably stick around for a while. I do think before too long not top priority, but like once the 2.0 is sort of up and running, I've been thinking a lot about ways that you could kind of use rigid body assumptions to auto calibrate so you wouldn't have to use the calibration board all the time. You would just be able to kind of set up the camera to kind of like stand in front of them.

**[01:17:08]** And it could use, you know, expectations that your eyes are always the same distance apart hard or like your, you know, that the, the standard, standard rigid body estimates apply. And you could use that to kind of get a decent calibration. And I think the way that that will work is we'll have that kind of auto calibrating based on the body type of system setup. It'll kind of like approximate or guess at like the scale. So it won't be like veridical units.

**[01:17:37]** Like it won't be like a millimeter, won't be a millimeter in real space, but it'll get it good enough and it'll get the data kind of up and running and looking good without the need to do a proper calibration. And then we'll just kind of include in the tutorials and the documentation and the website blah, blah, sort of like something that says like you can do it, you can get the data without calibrating with a proper calibration object. But if you care about the veriticality of the data, if you, you know, if you want your millimeters to be millimeters, you're going to want to have something like this. And then we will.

---

### Chunk 9 [01:18:00 - 01:28:00]

**[01:18:00]** A proper calibration object. But if you care about the veriticality of the data, if you, you know, if you want your millimeters to be millimeters, you're going to want to have something like this. And then we will. We are currently selling. So technically shop.freemocap.org is working.

**[01:18:19]** You can go to it. You can buy a charcoal board. It uses like a print on demand service. So like it's kind of slow and pretty expensive and there's like, you know, like shipping costs and stuff like that. But you can order it and it will.

**[01:18:34]** You'll get one of these in your, in your mail at some interval. It's a yard sign and you can split it and then heck and fold up and put in your backpack and then eventually this will be a bunch of like information and tutorials. But yeah, if you, if you like to pay shipping fees and wait a long time, shop.frocap.org you can go buy your Truko board today. But if you wanted to, you know, you can also like we're, we're like continuously working on that and like trying to improve it and you know, eventually we'll figure a bunch of stuff out. We'll figure everything out.

**[01:19:17]** Okay, I'm going to move on from this to talk about skellycam, which has been the center and bane of my experience. There you go. That's the one.

**[01:19:37]** Reminds me, Paul, we should probably be checking that queue just in case anyone does click through it.

**[01:19:45]** Yeah, eventually I want. So the shop right now just sells the charcoal board and I think stickers. It does it through a print on demand service which is like I said, relatively slow, relatively expensive and then has like, you know, like annoying shipping costs that I don't really like. It is a. But, but it does work.

**[01:20:05]** It does exist and you can do it and it will eventually get to you.

**[01:20:13]** And yeah, eventually that shop page. I also want to be selling like, you know, both cheap and not so cheap cameras. Kind of, you know, sort of originally from the dropship. It's kind of like tested and validated so that you can know that you're getting a good, a good enough to do the job kind of camera. There are some challenges there in terms of the sourcing and all that kind of stuff.

**[01:20:44]** But that is eventually the plan is to sell the little pieces of equipment and that you'll need to do this, that run the software. That should be like a little bit of income to sort of support the project and also just kind of like a thing we can Tell people, because people, people often come in and ask like, what kind of camera should I use? And right now like our best I option is to like send them to Amazon or Alibaba and just say kind of like click on something that looks like a camera and hope for the best. Because you just really don't know what you're getting until it shows up at your front door. So we can do a little bit of that work in that vetting and sort of, you know, kind of at first started to do it as like a drop shipping thing, but eventually handle kind of like the, you know, the logistics and you know, buy things in bulk so we can sell them for cheaper and figure out how to handle that stuff.

**[01:21:38]** And then the idea would be to sell like entry level bundles that use like these like cheapo, cheapest possible cameras and sort of like maintain that like, hey, here's the cheapest possible bundle that you can use, that you can buy that will allow you to sort of like start recording like research grade mocap data in your mouth, living room or basement and then sell those at like very close to cost. And then also in addition to that, sell higher end, more research grade, you know, higher frame rate, you know, just, you know, changeable lenses, like just more research grade kinds of cameras as well. And then basically, you know, sell the higher level stuff, the higher grade stuff with a higher margin so that the, the higher grade equipment sort of subsidizes the cost of being able to basically like allow people to buy cheap cameras for very cheap. This is the plan. We will get it done at some point, in some interval, God knows when or where.

**[01:22:52]** But yeah, we'll see. We will see. And yeah, 3D print a dimple object. Thought about that, thought about that. One of the trickies with like 3D printable stuff is like the, you know, the tolerances have to be good and also like it needs to be like big enough to be seen from the camera, like from a farther distance, which can be, which can be challenging, but I think there's a lot of options there.

**[01:23:18]** I've also had the thought of building something like this was something that it was, it was like there was like a brief period and I want to say like, like the 2008-2012 ish type of time period where people like people would put these like little tech demos on their sites so that would like detect an image and then like put a 3D model on it and you kind of like, like play around like sort of like an augmented reality type of thing that Would be pretty easy to do both with the board, like the Trugo board itself, but also just like with the Skelly logo, which I think would be super fun to kind of like if you hold up the board it shows like a little like rotating Skelly skull that and that just like in the camera image. But we'll get there. That's Easter eggs 3D printed ink stamper screen print could work. Yeah, I mean these little, these little fiducial Aruko markers.

**[01:24:25]** Like we use the grid because it's really helpful for the calibration in a lot of ways. But like, oh, do I have a version of that? I don't think do. We've been playing with different versions of this board too. So there's one.

**[01:24:40]** So this is 5x7 which is good for a number of reasons. But if we made. If made we the. Oh, I think it even has. Yeah in the.

**[01:24:50]** I don't know when exactly we added this, but can I do this?

**[01:24:59]** I don't like the. It's. I don't know if you can read this but it says full Charuco 7x5 and mini charcoal 3x5. I really don't like the word mini here because that's a misnomer. But if we support the pattern that's just a three by five grid, then all of a sudden just printing this onto a standard eight and a half by 11 or a four sheet of paper, you can now calibrate a significant, a more significantly sized space.

**[01:25:28]** Whereas the current system where if you print this onto an 8.5 x 11 paper you can really only track it for pretty small spaces.

**[01:25:40]** Anyway.

**[01:25:48]** Yeah, let's see, where are we at? Okay, let's talk about Skellycam. So up until now we've been talking about the current state of the situation of Freemo Cap and looking at this kind of like reasonably high watermark video like data quality stuff. I'll make this available somewhere I think. I don't know exactly when or where or how but like we're going to be adding like this little data drop down here in the.

**[01:26:16]** In the current 1.0, 1 point I guess 1.6 version of the software. You can download some sample data. We're going to be adding to this so you can, you'll be able to download like some treadmill data. You'll be download like I've got some data of like someone doing like American Sign Language, some dancers doing cool dance things and just a variety of like other types of recordings that we will soon be made available for download for samples.

**[01:26:46]** But that's for the future.

**[01:26:51]** Yeah. Let's talk about. Let's talk about Skelly Camp. Okay. How long have I been streaming?

**[01:26:56]** Hour and a half. Great. That's a. That's a good amount of time.

**[01:27:03]** How long do I. How long do I have in my emotional gas tank?

**[01:27:10]** Realistically? Probably have about a half an hour left, which is not enough time to dive into the Skelly Cam stuff which is not a shock in any way, shape or form because you can. You, you could have known from the start that I wasn't going to get to anything because my plan, what I was going to talk about involved the word and I said I was going to talk about this and. And then I was going to talk about this, which is. Which is ridiculous.

**[01:27:38]** One thing at a time, thank you very much.

**[01:27:43]** But I can still show off what's going on, so.

**[01:27:51]** Oh, I didn't even do that. That's just. Can you go back?

**[01:27:57]** Great. Always multiple ways to that do.

---

### Chunk 10 [01:27:45 - 01:37:45]

**[01:27:45]** So la da da.

**[01:27:51]** Oh, I didn't even do that. That's just. Can you go back? Great. Always multiple ways to do things.

**[01:28:00]** Let's make a new guy on top of that. Let's lock. Let's lock this layer. And now I can draw.

**[01:28:12]** Wait. Oh, draw stuff. Okay, So.

**[01:28:25]** So the one point, the vert 1.0 architecture of Freemocap, like I said, is basically just big honking pile.

**[01:28:38]** Soon is a registered trademark of Valve Softworks. Is very funny. Soon TM is the other joke.

**[01:28:46]** Chiruko T shirt is funny too. They actually do make fiducio markers that are designed to be worn on clothing. They. They involve kind of. It's like they're like.

**[01:28:56]** It's more like blobby circles. So instead of looking for right angles, they're just looking for like circles within circles. So they make these kind of like bubble looking things that are designed to be worn.

**[01:29:08]** But I'm not really going to worry about that. It would be a Charuco bird T shirt is funny to me in a variety of ways just because it's like it wouldn't function as a calibration tool, but it is just kind of like it's funny to me to develop an emotional attachment to a calibration object. But nonetheless, here we are.

**[01:29:34]** Yeah, minimally Skelly T shirt. We definitely need to have Skelly on a T shirt. That's. That's for sure.

**[01:29:45]** Yeah. Right now we got stickers.

**[01:29:49]** Stick it to a shirt, just don't wash it.

**[01:29:53]** Okay, so skellycam. Skellycam. The cam of Skelly.

**[01:30:01]** So first of all, the general architecture of freemocap and it has been this way for a while and it will continue to be is that there is the standard, the main Free mocap sort of core software. That's the one that lives@GitHub.com freemocap freemocap. And it has the code to run the GUI and sort of have all the buttons and do all the work. The actual functionality of Free mocap is split. We used to have a mono repo which is like all the data and one big giant blob.

**[01:30:37]** And we have split it years ago at this point into. We started using a more poly repo approach.

**[01:30:50]** Which splits the responsibilities. So there's FreeMo Cap, there is Skellycam which handles the camera stuff. There is Skelly Tracker which handles the 2D tracking on the image and the. Yeah. The convolutional neural networks, the media pipes.

**[01:31:15]** Not present, not in the past, but I Think currently also like the charcoal tracking. So basically the responsibilities of Skelly Tracker is taken images and spit out 2D tracking data and then we have stop Skelly. I did not space these very well, did I? Skelly Forge, which takes in the data from multiple cameras and produces the 3D output, sort of doing the triangulation and the gap filling, filtering, rigid body corrections and generating like the 3D data. And then Skelly Viewer, which currently just runs like the kind of busted viewer in the gui, might kind of go away.

**[01:32:12]** And then what is currently called the freemocat Blender Add on, but will soon be renamed to the appropriate Skelly Blender. Both because it is an appropriate name within the namespace of tab. Oh, I love streaming. Thank you. I've look, I have, I have looked for that button, I've searched for it, I didn't find it.

**[01:32:39]** But then, then all my con, the legend comes along. It's like hit tab dummy. Now here we are. Thank you. Look how professional I look now.

**[01:32:54]** Yes, Skelly Blender is the part. So Skelly Cam does cameras. I'm not going to write that. Skelly Cam's job is to do cameras. Skelly Tracker's job is to track.

**[01:33:06]** Is to. What's the word? Not process. Yeah, process the images from the cameras and to produce 2D data. Skelly Forge's job is to combine the data from multiple cameras into the cleaned up 3D output.

**[01:33:22]** Skelly viewer's job is to visualize the data in the gui. But again, that might. I'll probably just say that's going to go away because that's going to get subsumed by like the freemocap proper stuff. And then the Skelly Blender, the freemo Cat Blender Add On's job is to export the data into Blender. So all of these things have kind of been getting worked on in sort of very relatively interesting.

**[01:33:48]** We've been working on them a lot and there's kind of. Each of them has its kind of like 1.0 version, which is the sort of the production version. And that's kind of like running in the main gui. And some actually at this point they're all like, well, Skelly Blender is probably the one that is going to need the most refactoring to pull it into the 2.0 architecture. But yeah, everything also kind of lives in this kind of like it's got the 1.0 version which is kind of under like maintenance and like, like Less development, more maintenance.

**[01:34:19]** Although we're sneaking stuff in like the, the blender ground, like the charcoal ground plane correction is sort of. That's, that's, that's new features. And then we're transitioning into the 2.0 version which is going to be the, the sort of the. The full from scratch refactor. And all of these sub skellies have a sort of a.

**[01:34:39]** A nascent to somewhere between nascent extant 2.0 architecture of all of them, I think. Yeah. Skelly Blender is. It's. I'm going to like deprecate the current repo and like make a whole new repo for it.

**[01:34:53]** Skelly Forge is probably the one that is mostly still running. Like, it's kind of. It's kind of running in both modes, but that's a separate point. So. But of all of these, the one that has gotten the most, the most 2.0 work.

**[01:35:13]** Yeah. Nice. Let's see. Kind of orangey color. Skelly cam has gotten like the most attention.

**[01:35:23]** And I've been. I've been. I've been living in skellycam world for a thousand years and I want to leave, but I cannot leave because the cameras.

**[01:35:35]** The cameras. Cameras, man. It's complicated.

**[01:35:40]** So. And I'm gonna. So. But it is now working and I will show it to you. Of the whole system, I guess I can draw.

**[01:35:47]** There's sort of a.

**[01:35:50]** Well, yes. Of the whole system. The cameras are really the star of the show. That's where the data comes from. That is the beginning of the pipeline.

**[01:36:02]** That's the moment of transduction where we are converting environmental energy in the form of photons into some kind of pattern of electrical activity on a sensor which gets read to disk. And then all the rest of the pipeline happens from that point. So the cameras have always been kind of like the core and the heart of the thing. And in particular because 2.0, the main. One of the main goals of 2.0 is to provide real time output.

**[01:36:30]** Real time 3D output. That puts a lot of constraints on what the Skellycamp what Skellycam can do. The 1.0 version of the software, the Skellycam basically just ran just like it runs the cameras in individual threads and then saves on the disk and then synchronizes the frame after the fact. So because of that, the frames themselves are not synchronized sort of to each other. They're kind of like lined up afterwards.

**[01:36:57]** So there is somewhere between roughly like half of a frame duration of variability between the individual frames, which isn't a lot. That's like 15 milliseconds. But it's measurable. Like, it would affect the output. And also importantly, you don't get the data until after the recording is already done.

**[01:37:17]** So for that region we call 1.0 is kind of working on a staged pipeline where it's like, record it, analyze it, record it, process it, visualize it, and it has to happen in that order. So for that reason, like, 1.0 could never be real time. There's actually even challenges to, like,

---

### Chunk 11 [01:37:31 - 01:47:30]

**[01:37:31]** Where it's like, record it, analyze it, you know, record it, process it, visualize it. And like, it has to happen in that order. So for that reason, like 1.0 could never be real time. There's actually even challenges to like, Even displaying the 2D data, like, as they come in. This is not even withstanding the fact that the way that I implemented the image streaming to the GUI is really inefficient to the point that you get like a lot of Q lag if you have like, more than like three cameras.

**[01:38:04]** But by far the most common thing people have ever asked about Freemodel cap is, does it work in real time? Ah, Milton. I heard about Milton. I'll give it a shot. I'll try it out later.

**[01:38:18]** Because, yeah, the infinite canvas thing is really just what I want. And Krita is kind of overpowered for that.

**[01:38:26]** Thank you for the recommendation.

**[01:38:36]** Yeah, so does it do real time? Can it be interactive? And that's, that's the kind of thing that, like, from a scientific perspective, from this, as a research tool, and realistically for it as like an animator's, like, mocap tool, real time output is not super critical. It's much more important to be able to produce high quality output at the end of the pipeline. Whether or not we can produce 3D Mocapi data at runtime is secondary, but it is nonetheless, because I am an idiot, I have decided to.

**[01:39:17]** We're going to be 2.0. The 2.0 architecture is like the main sort of productive constraint that I had in mind when thinking about how to set it up is that I want to be able to connect to the cameras and produce synchronized frames at runtime that can be analyzed at runtime and produce some quality of 3D data.

**[01:39:45]** Because doing that would allow the real time 3D interactive motion capture output.

**[01:39:54]** Again, from a technical perspective, how much does that add? It would allow you to create VR applications, it would allow you to do interactive stuff. But more importantly to me, for that is the way that a real time. The way that real time data output will change the workflow of people using this software. Right now, the best workflow you can hope for is set it up, turn on the cameras, record the data, push process, wait for a while, the data pops up and you go, oh, hey, look, that's what it is.

**[01:40:30]** And if you made a mistake, you got to run it again. If you said, oh, I want to do something. If you want to move the cameras, you got to run it again. You got to. The workflow has a lot of kind of like click and wait behavior in it.

**[01:40:48]** And that's fine, it's workable. But if it was able to produce real time output, that was an approximation of what you would get if you were running it full bore. It would allow for a much more, a much shorter, much tighter feedback loop between the user and the data that they're producing. It will make it a lot more fun for sure. It'll make it a better teaching tool for sure.

**[01:41:17]** It will make it. And it'll just generally elevate everybody's work because the feedback loop will be so much tighter. So for that reason, and also again because I am an idiot, 2.0 is targeting this kind of, this real time output.

**[01:41:37]** Other ads coming up.

**[01:41:41]** So within that space we had a couple of constraints, right? So we want 2.0, we want real time processing and real time output, but we don't want to sacrifice like the quality of the staged pipeline. Because the staged pipeline has a higher sort of quality capacity. Because with a real time pipeline you are constrained by the power of your, by the power of computer, by the framing of your cameras. Like if you have a 38 frame, 30 frame per second cameras and you're trying to process each frame, you have 33 milliseconds per frame, which is not very much time.

**[01:42:18]** So you're going to wind up taking your speed accuracy knob and sort of cranking it towards speed, but at the cost of accuracy and position of the final data. So what you really want is you want to be able to produce real time 3D skeleton output, but you also want to be able to record all the data at the same or better level of fidelity that you could if you weren't doing the 3D output. So we want to be able to protect the part of the code that actually saves the data to, to videos so that we can always go back and then reprocess the data to get the same high quality sort of staged pipeline. So we want to be able, we want real time output, but we don't want to do so at the cost of the better precision and increased precision that you get from a staged output. Also, if you imagine like a user who's using like a, not a particularly powerful computer, they may not be able to do real time, but they should be able to still record the videos and then process it after the fact.

**[01:43:19]** And maybe it takes them, you know, hours to actually produce the output, but it will be the same output that they, that like, like it will take their wimpy computer an hour and a Half to do what my computer can do in 20 minutes. But in the end, we'll both be looking at the same data that's at the same quality. This is the dream.

**[01:43:42]** So, yes. So skellycam. And so. And again so. Because that technical requirement is like the hardest one, like, relative to like, you know, running some tracking algorithms on images while doing, like, the data cleanup and the triangulation and even shoving it into Blender.

**[01:44:04]** The cameras are really the big monster here because they're the ones that are. Because it's fragile. Like, you have to connect to a device and you have to start an image stream, and if you mess up and drop a frame, that frame is gone. If the camera. If you're recording from six cameras and one of those cameras crashes, then that recording is kind of busted now.

**[01:44:28]** So it's like a camp. Like, it's kind of like trying to connect to seven printers that all print at 30 pages per second and which all use printers. And we know what that's like. So, like, when thinking about the 2.0, that ad starting in a minute. So I guess I'll just handle that when it comes thinking about 2.0 and thinking about, like, the technical challenges of, you know, because there's going to be changes.

**[01:44:59]** Like, there's big changes to the architecture of Skelly Tracker, Scaly Forge and Skelly Blender, but they're more. They're more minor by comparison.

**[01:45:09]** So the strategy, the development strategy that we have picked up, that we've been adopting is very akin to what we did for the 1.0, which is rather than trying to build the entire 2.0 freemo cap architecture again from scratch, I have been heavily focused on rebuilding. So Skelly Cam and then Skelly Cam. And like the development of The Skelly Cam 2.0 kind of becomes a microcosm of the entire project. And I'm going to let the ad roll. Bali, like, chill.

**[01:45:43]** How we're going you doing it? Is it playing? Is there any for me to know? I don't know.

**[01:45:55]** I don't even know how I. It doesn't show me anything anyways.

**[01:46:07]** I've been noticing that the. The camera that I've displayed is like, I'm doing the narrow, narrow view, but I've been doing a lot. But I've been looking at the camera up here, which shows me like the full frame image. So I don't know if I've been off screen. Off screen.

**[01:46:22]** You can deal with it later. It could probably be a little bit wider.

**[01:46:29]** Okay, if you're not, I assume that the ad has either played or not played. No, there it is. Now it's saying ad, Blake. AD break.

**[01:46:48]** Anyways, Okay, and we're back.

**[01:47:10]** So without any further ado, let us discuss new Skelly cam. Real quick on the architecture. So, free mocap1v1 looks like this and basically is a big Hong compile of Python code.

---

### Chunk 12 [01:47:17 - 01:57:14]

**[01:47:17]** Real quick on the architecture. So freemocap1v1 looks like this and basically is a big honkin pile of Python code with a QT GUI and just generally pretty sloppy approach to a lot of things. Mea culpa. It was my first time.

**[01:47:41]** Freemocap 2.0 is going to be built on much more modern architecture where we're still going to have a bunch of Python code running in the back end In a fast API plus plus really server 2.0, we're still going to be doing Python backend. I don't know exactly when, but like obviously at some point the bottleneck is going to be the fact that it's written in Python. At that point I'm already sort of thinking about a world where we're writing the back end code in Rust and I'm sort of looking for how that will happen. 3.0. Right.

**[01:48:28]** For now it's Python. If you don't like it, direct all complaints to our refunds department. So the back end code is kind of. This is where like the work is being done is on the back end code. And then we also will have, let's say in this nice color here, a nice friendly front end which will be written in React and TypeScript and running sort of.

**[01:48:57]** And it's currently an Electron app. I think I might trans. I might swap that out with Tori. But Electron is venerable. It does the job.

**[01:49:10]** It runs half the pieces of like the majority of softwares that you use in your life that are not a like browser window are actually secretly browser windows that are actually Electron. So basically the front end connects to the back end and communicates via HTTP requests to create cameras, connect to cameras. And then the data, the image data is currently. And what I'm going to show you is transmitted via WebSocket. But the WebSockets, they do the job, but they're a little slow.

**[01:49:46]** And I'm playing around with some other methods for sharing the data that should. The image data specifically that should be faster.

**[01:49:55]** XR Animator. I have heard of XR Animator. Ah, it's based on Electron. I'll check it out. Thank you.

**[01:50:03]** Always curious about at this point. Just kind of like scope and people stuff. Oh, full body motion capture. Oh, I've seen this. I have seen this.

**[01:50:14]** They're clearly using.

**[01:50:17]** This is. This is absolutely Media pipe right here. So I'm guessing that they're doing kind of a single camera situation. Yeah, yeah, yeah. So they're running like a single camera media pipe process.

**[01:50:31]** Yes. I will absolutely crib their Notes. I think I already have crib their notes, but I will continue to crib their notes.

**[01:50:44]** We support them.

**[01:50:47]** But yeah. So before I burn out too quickly, let's actually show you what the code looks like. The current state of Skellycam 2.0 is that it works pretty well. It's what I might call an MVP minimum viable product. I posted a YouTube video a while back, right.

**[01:51:07]** I think I may have even said it was MVP at that point, but really at that point it was proof of concept. Just kind of like showing that the piece is connected, but like you didn't have the controls that you needed to really use it as a tool to record videos. Current Skelly Cam as it exists on the skelly cam/john/development branch, it works and it does. Like actually. And so that.

**[01:51:37]** That version of skellycam was used to record these videos. So without any. Let me show you what that looks like.

**[01:51:52]** So one of the other nice things, one of the very, very nice things about using Electron is you get to use their bundler. So currently we still have to install free mocap3 command line, which is obviously going to be prohibitive for like large portions of the population because most people don't know how to do that. We have tried to make it as easy as we possibly can, but there's only so easy you can make that. And a very significant portion of this is some of the stuff I was playing with of the development has been geared towards having like a single click installer that, you know, freemocap.org download and you download an installer for your operating system and then it just runs harder to set up than I could have ever, ever predicted. But we're getting there.

**[01:52:44]** And yeah, technically you've already done that with skellycam, but we'll get there. Okay, so to run, to run Skelecam 2.0 you have to go to the John development branch and then in the code. Can I zoom in on you? Nope. There is skellycam, the package skellycam which has all the backend data.

**[01:53:14]** Then skellycam UI which has all the react, Electron whoseits and whatsits in there.

**[01:53:21]** There's a readme that's specific to the John development branch that has like instructions on how to run stuff if you're into that. But long story short, you run the. This is webstorm, so I'll run the front end from here. You go into the skellycam UI folder and run NPM run dev. And that looks.

**[01:53:50]** And a Bunch of stuff will happen. And then if, unless I screwed something up, you'll see something what looks an awful lot like this get a little bit screwy. So this link right here, currently if you click it, it breaks the thing because it captures the link in the UI and then breaks everything. And that's. You can't.

**[01:54:12]** There's no way to go back. So, you know, minimum viable product is not alpha. We are not yet in alpha state. Alpha state will happen when these kind of like known busted parts, like minimum viable product means you can use it for its intended purpose. But it is known to be busted.

**[01:54:31]** There are broken bits. Not all the buttons do everything, you know, sometimes the solution is shut it down and restart it. We'll get there. So currently this is the front end running in kind of like lobotomized mode. Right.

**[01:54:46]** So it's just the ui. Ui. It's just the UI with no, no server background. So it's. It can't do anything, it can't detect cameras, it can't do anything.

**[01:54:55]** All that interesting. So to do interesting stuff, I will run this. This is just the same repository in pycharm, the other one's in webstorm, you could do it all through Terminal, but this is just what I choose to do.

**[01:55:20]** Yeah, and then from here you run.

**[01:55:25]** So in this, here's the code, here's Skellycam. And here at the main function, you just run the main function, the main file, doink, doink, doink.

**[01:55:43]** And it pops open this fast API server and this fast API server which you can click that and it will take you to this, the swagger docs. This is like proper fancy guy API. It's got all these fun endpoints and stuff like that. And it's got things like cameras detect and camera groups. So a camera group is a set of synchronized cameras and you can, it's kind of vaguely based off of like doing crud operations on camera groups.

**[01:56:20]** That's kind of the basic thinking here. Nascent video endpoints that I think currently doesn't work. And then you got the whole thing. It's all very, all very professional. Approaching professional.

**[01:56:34]** We'll get there.

**[01:56:37]** And let's see. So this is the pycharm. Yeah, got that there. And now that the server backend is running Skellycam, the user interface, you see this little WebSocket connect, it has a little check mark that means it's connected to the back end and you're ready to go. So again, like UI wise.

**[01:57:08]** So the little like refresh thing should probably be like a magnifying glass, because that's the thing that does the camera detection.

---

### Chunk 13 [01:57:00 - 02:06:59]

**[01:57:00]** And you're ready to go. So again, like UI wise. So the little like refresh thing should probably be like a magnifying glass because that's the thing that does the camera detection. So you hit that button detects all the cameras you have attached. And I have nine cameras attached to my computer because it's a totally normal number of cameras.

**[01:57:24]** One of the cameras is this one. So that's the one that's showing.

**[01:57:30]** See, I'm going to try to do this where I'm.

**[01:57:35]** You kind of like. Does it play here? Oh, it does. So I have a little thing here that, that shows the server logs in the, in the ui, but it's not complete. It's a little, obviously a little bit busted.

**[01:57:46]** But so I'm going to try to keep this so I can see this, the Python server output in the back here.

**[01:57:55]** Yeah, so nine cameras, bunch of USB cameras, this one logi camera and then this, this cam link 4K which I will check off. So in terms of performance, the current version of skellycam on this computer, which is a reasonably beefy computer, can I think reliably, pretty reliably connect to nine USB webcams, stream them at 30 frames per second at 1280p 720x1280 resolution, and save them to disk without missing any frames and getting like very high levels of synchronization. Nine cameras is like, you shouldn't use nine cameras for this. But we kind of. My thinking has been that the standard recommendation I give people is like three camera recordings are really, I think, kind of a small sweet spot.

**[01:58:50]** This recording, we use six kind of as like a little bit of a stress test. But also it's just like a way to get more cameras. Hypothetically. Eventually you should be able to cover a larger space with more cameras. So for practical purposes, three to six cameras is kind of what I recommend.

**[01:59:11]** But because the, this computer is a relatively beefy computer, I've tried to target setting it up so that it can handle nine cameras at full frame rate and sort of. So basically the assumption like if this computer can handle nine cameras, then a more sort of average gaming PC can probably handle six cameras and a more like wimpy, maybe laptopy type of computer can probably handle three cameras. And you know, that's kind of the hope. Currently, I believe the biggest bottleneck to being able to handle like more cameras is this little guy right here trying to shove that much data, that much image data through a websocket. It's just, it's Just.

**[01:59:53]** It's just not what a websocket is really for. So I've been experimenting with a bunch of different data transfer protocols before figure it out. I've looked into, I think the. I've looked at grcp, that's rc. Rcp, which is not the right tool for the job.

**[02:00:15]** I've looked into zero mq, which probably could work, but interacts weird with Electron because it's a native app or something. UDP I could do and I think could work, but currently the one that I'm kind of targeting is memory mapped files, which I think can probably do the job. I don't know. If I was smart, I would walk away from camera town right goddamn now and like focus on the rest of the pipeline because we're so goddamn close. But I can't.

**[02:00:48]** I can't. I'm stupid and I can't leave and I have to. I have to do it. So we'll see the E. Or wait, sorry. What am I doing here?

**[02:01:01]** Ah, I was looking for this. Oh, what have I done?

**[02:01:10]** You can tell the stream has been going on because I'm losing brain.

**[02:01:25]** Yes, I am catching up on chat. I will look into those things as they go.

**[02:01:34]** Two hours. My brain will fully explode soon, but until then I think I'm making progress. So all that is to say, technically, if I really wanted to, I could probably connect to all eight of these cameras. I'll probably do that in a second, but for like both. But it runs on this computer with nine cameras.

**[02:01:59]** But it's. It struggles a bit, but it works relatively like a charm with like three to four. So let's try that. So. So I click the button.

**[02:02:16]** If I. If I click the button under the hood, it does camera group create. So the detect button hits this endpoint. The connect button hits this create button and that sends like the camera configs to the back the back end server and the Python uses. At this point it's OpenCV.

**[02:02:39]** But we're gonna start doing other camera methods before too long.

**[02:02:44]** Doing great powering through connect. Let's see what that's. I think it'll work. So it does a bunch of stuff, connects to the cameras, sends. So you got these hey, what's up?

**[02:03:00]** Settings and all that type of stuff. And I was not actually looking at which cameras were attached. But we can do this. Look at that div. I don't know how.

**[02:03:12]** I am not a. I don't know how anything works. So.

**[02:03:21]** So we've got this guy. Hello, We've got this Guy. Hello. We've got that guy. Hello.

**[02:03:35]** And we've got. Who's number four?

**[02:03:42]** I said I had eight cameras attached to my computer. I didn't say I have eight cameras attached. Like. Well, what am I looking at there? I'm seeing these.

**[02:03:53]** Yes. Oh, are you hanging down the back?

**[02:04:05]** Aha. Hello, this guy.

**[02:04:11]** So.

**[02:04:16]** And pause for applause. And. Yeah, there we go. So now I need, you know, the. What's the word?

**[02:04:28]** The exposure is a little busted. And these two are rotated. So let's rotate them around. That is camera four, which wants to be 90. And then this is camera three, which wants to also be 90.

**[02:04:43]** And then this is. Camera two is too bright. So let's bring your exposure down. Four is also a little bright. Let's see.

**[02:04:52]** Bring your exposure down. And then we push this button that says apply settings to cameras. And it should work as well. Pauses for a second. And then there we go.

**[02:05:04]** Oh, and then it hits this bug that happens sometimes where it does things wrong, but then it does it intelligently. And I don't know why the sides are all dark now, but that's okay. Let's copy settings to the cameras. Copy. Copy all settings to cameras.

**[02:05:20]** And then 9, 3, and 4. 90. And that should work.

**[02:05:34]** Why are we dark? We're going to be less dark in a second. Dark.

**[02:05:43]** Try this. This recommend. Recommend exposure thing is a little 1, 2, 3. Where's the other one? Attached?

**[02:05:53]** Oh, five. Who's five? You're five. Five is good. Let's see if we can get that exposure up.

**[02:06:06]** There you go. That works. Oh, don't. Don't be stupid. Come on, buddy.

**[02:06:14]** Sure, that works. And who's you? You're right there. So, yeah, so, Yeah, obviously, like a little ugly, but it does the job. You got these.

**[02:06:34]** You know, this is not efficient. Like, it should show more information in the top there, but, you know, who cares? This. You know, we could obviously do that. And the div.

**[02:06:46]** Like, the images should, like, resize to fill the space better. But when in doubt, just do Control Shift plus and then bump it up until it fits well. And most importantly,

---

### Chunk 14 [02:06:45 - 02:16:45]

**[02:06:45]** And the div, like the images should like resize to fill the space better. But when in doubt, just do control shift plus and then bump it up until it fits well. And most importantly, this little guy right here, this recording button works in theory. I've used it, I mean I've done it like a thousand times. It's just now I'm on, people are watching.

**[02:07:11]** So I wanted to, I wanted to continue to work.

**[02:07:16]** It's got a light mode that kind of works. So you can like do like, you can add a auto increment, you can add a tag to the recording, you can delay the start for a number of seconds. All these little things, the colors are all screwy, it's visually ugly and blah blah blah. You know again like anti patterns but those architecturally much more sophisticated than it was previously. There's a whole conversation, Lord, Lord, help me.

**[02:07:43]** There's a whole conversation about what is actually going on in the back end. To sort of get the images to where they need to be complex involves a lot of like, like shared memory stuff and like sync, multi process synchronization and all this thing. I might do another video to talk about like that kind of nitty gritty detail stuff. But I'm not, not, not today, not this day.

**[02:08:10]** God, that's ugly.

**[02:08:14]** And that's, you know, it's fine, we'll get there. So if I do, if I click record, it hits the start recording endpoint and then I can do this stuff. It kind of pauses for a little bit as the, the videos begin, but it records and you know, it can record for indefinite amount of time it is recording like everything is going to disk each frame. So there's, there was many, many iterations of this, but one of them and actually currently in free mocap where we, in order to avoid like the difficulties of saving to disk, we would just save the frames in memory. So basically it was like a built in memory leak.

**[02:09:02]** So you had the maximum recording length was defined by the number of frames your RAM could hold until it overflowed and crashed. But now we're not doing that anymore. So you can record indefinitely. I will stop this recording and then my favorite part will show up which is after it has saved the videos to disk, it will spit out some stats, some statistics about the recording itself. It takes a long time to produce those statistics for a number of reasons.

**[02:09:33]** But here, here they go. So this tells us and this is so videos are saved to disk. I'll show you those. Just so you know I'm speaking the Truth they go to your home folder and they go to home home/skellycamdata recordings and then the default names are just based off of the timestamp that one is today and you've got this info JSON which should does not currently include the camera configs but it will soon and then synchronized videos folder. So notice that this synchronized video like recording folder with a synchronized video folder inside of it is the same basic layout of the free mocap data output, which makes the whole thing nicely backwards compatible.

**[02:10:25]** To get this recording, we recorded it with skellycam and then we just dragged it into the free mocap data folder and then process it directly from there and it worked exactly the same.

**[02:10:39]** In this video folder you have the videos themselves, they are rotated appropriately and they are frame perfect synchronized. Every video has exactly the same number of frames and those frames occurred at very very similar timestamps. So there's a whole folder of timestamps we might look that a little bit. But this so recording name stats txt is the same thing that's in this sort of console output here. So time step recording for this recording number of cameras 4 total frames 1477, 49 seconds total.

**[02:11:19]** And then this is the fun part. Frame rate is 30fps. So you get the meat, the median, the mean, the standard deviation, the minimum and the maximum. Probably the min and max don't mean as much as they because I think that's probably just like first and last frame stuff. But whatever.

**[02:11:34]** But they are recording perfectly. This is my favorite part. The inter camera frame grab synchronization is 2.91 milliseconds. So that means that for these 1400 recorded frames from these four separate cameras, each frame is on average the frames were grabbed within 291 microseconds of each other, which is so insane. That's like approach that's not really approaching like hardware.

**[02:12:06]** Like when you have research cameras you use a hardware sync like they have dedicated ports in them that you can hit hit with a TTL pulse so you can get like, like microsecond level synchronization. These are USB webcams being managed through Python and OpenCV. And so there's a lot, a lot, a lot of work that went into being able to manage everything so that you can be both, so you can be running each of the cameras in a way that the camera process is protected from getting like any kind of hiccup that would lead to like a frame drop and, but also like, like they're communicating with each other enough that they, the grabs, the frame grabs are synchronous. And in addition, because I am crazy, we also keep a pretty fastidious level of what I'm calling frame lifespan timestamps. So for each of these 1477 frames, we log the timestamp of each sort of stage of the image's life.

**[02:13:17]** So the frame grab is when the software sort of grabs the image from the device. That is sort of, that moment is like the closest moment to like the moment in time that that image actually captures. Idle before retrieve. Retrieve is where most of the time is actually being sent. That's when the, the, the image buffer off of the USB port is like processed into an image like an actual image using like jpeg conversion or mp4 or something.

**[02:13:51]** I don't really know how it's doing it, but that's the part that takes the most time. And then it gets copied into this like shared memory thing. There's, there's this whole shared memory ring buffer thing for transferring the data, this whole thing and then it's saved to disk. And then so you get this really nice measure of where of like exactly how much time is being spent at each phase of the frame's lifespan which, which is really, really nice for being able to debug and extend. And this is the level of fastidiousness of the milliseconds matter type of programming that is going to allow us to do real time processing.

**[02:14:30]** Because.

**[02:14:36]** Basically during runtime the software is producing synchronized multi frame packets that sort of come out at exactly the frame rate of the individual cameras. If the cameras ran at different frame rates, it would, it would probably, it would, it would be throttled down to the slowest one. Someday we'll, we will expand our world where we can have like multiple camera groups running that can handle like different frame rules, frame rates and blah, blah, blah. But for now it's hard synced and it produces synchronized frame packets. So we will be able to, I've got some sort of proof of concept in various places to show that we'll be able to utilize this framework that's basically as the frames come out, you can do all the tracking and triangulating of the frames as you receive them and have confidence that they are all sort of synchronous to that sort of 2.91 milliseconds.

**[02:15:42]** 2.91 microseconds of precision.

**[02:15:49]** Yeah. Have I thought about publishing on Steam? I have a little bit thought about publishing on Steam. I know it's a thing people do there. There's some.

**[02:15:58]** There's some other mocap thing that has. That's published on Steam. The main reason why I haven't done it is just kind of like. Like one thing at a time. But I think that once we have the.

**[02:16:13]** Yeah, the electron bundler that gives the nice standalone app I think I actually have. Yeah. So if I look for that, like, I have, like this. This skellycam app on my computer is the one that was installed from the Skelly Cam installer. Is it here?

**[02:16:31]** No, I think I've cleared it. No. There you go. Technically. Yeah, technically, this Skelly Cam 2.0 installer would hypothetically work, but I wouldn't share it.

**[02:16:43]** So I'll have to look into how.

---

### Chunk 15 [02:16:30 - 02:26:21]

**[02:16:30]** Is it here? No, I probably. I think I've cleared it. No, it's. Yeah, there you go.

**[02:16:35]** Technically, yeah, technically this Skelecam 2.0 installer like would hypothetically work, but I wouldn't share it. So I'll have to look into how Steam sort of handles things. But I suspect that once that is working we will probably be able to distribute through Steam. And that's. That's a good idea because I like how they operate.

**[02:16:59]** But I'll have to look into it. It's sort of in the same slightly different space from like.

**[02:17:11]** I think it was. Was it Jawa a little way up the board?

**[02:17:17]** Yeah, Jawa. About like a couple messages up was posting a link to the extensions.blender.org add ons, like official add ons list and I have looked into getting the free mocap Blender add on like officially listed there with like sample data and stuff like that. And it's absolutely doable. There's like a couple of things that we have to do to the code to make it like compatible with their rules. Like we do some things that's like not technically allowed but you know, I think it'll be good because it's like as a method for distribution and discovery.

**[02:17:54]** Like it'll be good for folks and I'll keep the Steam distribution option in mind because that would be a cool way to distribute.

**[02:18:06]** But what else are I going to show? Is there anything else I wanted to show here? But yeah, so it works. It works. Honestly, not to toot my own horn but like toodlee doot.

**[02:18:21]** It works really fucking well. Like I am unaware of any other camera based software that even attempts to get this level of synchronization from standard USB cameras using you know, just simple software based synchronization.

**[02:18:40]** And I think that for like this, I think this is like already. Well it needs some polish. Like there's some like some gotchas and some anti patterns and some like busted workflow that I think would be like prohibitive for most folks. Like for like standard usage. But like with a little bit of polishing I think like this would get to what I would consider in my scientific heart to be something, something approaching like a contribution.

**[02:19:13]** Like a thing. Like hey, I've like, I think like free mocap I think has is like it's a contribution but like and I think the user friendliness of it is where it's real. I think that's where like the magic really comes from and like the connection to Blender and like the pretty animator Outputs. It's kind of like the blending of like scientific concerns with like the needs of artistic animators and stuff like that I think is all. I'm obviously half a decade at this point and counting on that project.

**[02:19:49]** But like I, I don't think I would have. It would be hard for me to kind of like tell a story about things that Free mocap does that don't. That you cannot find that you couldn't find it in other software like multi. Multi camera calibration, you know, that kind of stuff. But like a lot of the paid software, like they do stuff like that, they suck and they're expensive and we hate them obviously out of.

**[02:20:10]** For moral principle. But like it's the same technical thing. This right here, I don't think this exists anywhere else. I don't think that there is, there is another way to connect to standard, you know, un. Like unadorned USB webcams and get you know, sub millisecond synchronization and so.

**[02:20:36]** And it's, it's cool. Let's see if I can do. Let me see. I'm gonna. Always good to check if you can close things out.

**[02:20:44]** So closed, theoretically I should be able to open it up again and connect to six cameras and I'm just gonna also see, look like this kind of stuff here, like. Oh, it doesn't just, it doesn't. It just doesn't do it right. Because I don't know how to do this right. I'm like, I'm learning this, this from front end stuff and it does an okay job but like we're getting there.

**[02:21:11]** Yeah. Yeah. My God's noticing that the. What we're looking at here is I would say poorly represented by Free Mo. Come on.

**[02:21:31]** I know how to type. How long have I been streaming? I'm streaming long enough that I can no longer use the keyboard.

**[02:21:38]** This is the, the ui, the turn off this dark reader thing. Like at this point I think these are videos are probably from like 2000, like 2022 or something like that. This was when we were like. It was just getting into Blender. Like this is like the matplotlib version and stuff like that.

**[02:21:57]** So, so like the side to side, you know, like side by side, like we've made a lot of progress and yeah, we absolutely need to be updating this. It's like very much in that space. I've been quiet like, you know, it's been. I hit a certain point in the project like at this point a couple of years ago where you know, we were kind of hitting a certain stride. I think it was right around the time that the 1.0 was kind of starting to, like, be viable as a tool.

**[02:22:29]** And we were starting to see, like, growth in the. In the Discord server. That was. Back then. We probably had.

**[02:22:36]** If we had a thousand, I'd be surprised, but think people were coming in and like. And, you know, it kind of got to this point where I was like, okay, we're actually at a pretty comfortable rate of growth right now, but I don't know that we could candle, like, all. All that much more. So I kind of made a decision to kind of like, I stopped posting, like, demo videos about it. I didn't mean to stop streaming, but I did stop streaming.

**[02:23:03]** And it was somewhat intentional, just as a way to kind of like, you know, sort of like, circle the wagons a little bit and try to make sure that we could develop basic workflows, documentation, make sure that, like, the culture of the Freemo Cap Discord server could handle incoming new people. Because at the time it couldn't. Like, if people came in and asked a question, it would just sit there until like. Like, usually, like, I would have to notice it and answer those questions. And like, it was.

**[02:23:32]** It was just too much. So, like, I kind of intentionally kind of like. Like, you know, got a little quiet, but we're ready to wake up again. Like, I think we can handle more like the. The I'm.

**[02:23:45]** I'm so, like. I guess I don't know what the word would be like. Proud. Proud. Probably proud.

**[02:23:51]** Enamored with, like, everything that's going on in that Discord server of, like, just people are. People show up. Like, every day I show up, I could look and there would be some messages from, like, usernames I've never seen before. Some that I recognize. Like, Aaron I recognize, obviously.

**[02:24:10]** And then Mikkel has always been around. Like, he just pops in and it's like, hey, you should change your data model. You should clean up your data output. But, you know, but then also just like, people asking questions, people I've never heard of before, and then other people answering them. And like, it's really what you want.

**[02:24:26]** It's really amazing. And yeah, and I think a big part of it for me was really wanting to get, like, a good installer together so that the instructions. Because, like, the concern was like, I would post, like, the fear that I had because I've done enough stuff online to know that, like, sometimes things go viral and sometimes that's a good thing, but sometimes it's really not and the fear that I had is that I would be posting something that looked particularly good and then I would wake up and then my, you know, couple hundred people in a Discord server became. Might become like 5,000, 10,000 people in Discord server and that's, that's. I didn't want that that's a nightmare but now I think we're getting to that point and I also, I didn't want to like have to say like oh yeah open up your terminal and install conda as your installation method but yeah, I think we're getting there now and I think I'll probably call it about there for the stream oh did we connect to four it?

**[02:25:39]** Yeah hey look at that and let's, let's get everybody looking straight yeah we're a little dark but that's okay can we recommend.

**[02:25:58]** Come on, come on.

**[02:26:05]** Oh yeah recommend exposure thing actually works pretty well so now we have six cameras and so let's just do a quick recording here and.

---

### Chunk 16 [02:26:15 - 02:36:15]

**[02:26:15]** And so just do a quick recording here and.

**[02:26:34]** Brady Bunch reunion. Yes. You sort of get used to seeing yourself like my brother was here recently. He's what I look like from the side is like you just, you get used to it. Hello.

**[02:26:50]** So.

**[02:26:53]** So remember with six cameras we were getting perfect, perfect recording. No frame drops 30fps and 2.29 milliseconds of inter camera sync. Now with six cameras we look at the same, same thing and we get damn near the same performance which, which, which we love. We sure do love that. So now one of my camera slots is taken up by this, this guy here.

**[02:27:23]** So let's close it down again. Bye. It doesn't clear this screen even though you know it's listed. Listen, listen. One at a time, one thing at a time.

**[02:27:36]** So now we uncheck the cam link and then we reconnect again. And this should now connect to eight cameras, which again is more than you should ever like. I wouldn't recommend using eight cameras from ocap, but you know, I can imagine somebody else we might want to have eight cameras.

**[02:28:00]** How many people do I have working on the code base? It's a good question. So skellycam right now is more or less a one person job.

**[02:28:11]** Total number of developers, core developers is me, my PhD student Aaron, good old Phillip Queen who is a grad student like object who's been working with us for a while. He, he's probably writing the most code right now. But Aaron has been mostly focused on like recording data and like cleaning up the outputs and like if you're using the software it's got some, some pop ups around like oh, we fixed this problem, we fixed this calibration thing, the ground plane calibration. Philip has been doing more of the maintenance and kind of like getting things kind of cleared up and then, and then good old AJC Andres down in formerly Chile, currently Brazil, has been writing, been doing like most of the updates in the blender add on have been coming from him. So like four total.

**[02:29:19]** And then there's like, you know, smatterings of people here and there who kind of like pop in with a little pr. A little fix here. Mikol Michael, I never know how to pronounce his name. He's been doing a lot of conversations on GitHub again he's been mostly focusing on helping us clean out our data output. And hey, you should structure it like this instead of that makes it better for data analysis.

**[02:29:47]** But that's about it. So, so skellycam proper, this one has been Most it's been mostly me working on this. Philip. I've been bringing Philip in and he's done a little bit. He made the camera detection code that endpoint and he's done some stuff here and there.

**[02:30:05]** It's been the kind of thing where it's been such a voyage of discovery for lack of more obscene language that like the whole like the, the code base had just been such a state of flux. It just wasn't really in a position for external help and.

**[02:30:28]** But yeah, it's kind of like. But now that it's kind of like it. It's working now. Oh, I think, I think I can do a refresh of. Yeah.

**[02:30:41]** Okay now. So at 8.0 we're now starting to see a little bit of frame lag. But I think if I. So if I pause it it should catch up. Yeah.

**[02:30:51]** And so yeah, so now we're back. That's again, that's the websocket problem.

**[02:31:02]** But this is always fun. So if. I don't know if I can.

**[02:31:13]** I don't know if you're able to see it but pausing it, you can sort of check. You can't really see it very well because of the lighting. But like it's a fun way to kind of see the real time synchronization. But even though the front end is now starting to be a little bit laggy, if we record from it, it's somewhat intelligent about the way that it manages its priorities. So even though the front end is now getting noticeably screwy, the back end, it's actually handling the recording.

**[02:31:48]** Including the stop recording thing which took a second to go through.

**[02:31:57]** Perfect, perfect frame rates. And the inter camera grab sync. Sync has now gone up to 571 microseconds which good enough for government work.

**[02:32:14]** Jawa said. Yeah. 80 LV. Yeah. I think they posted about us like some years ago.

**[02:32:20]** It'd be fun to reach out back. There's been a couple people that were kind of like involve the 2 point with 1.0 and like the, the pre 1.0 with alpha that. Yeah I'm be very excited to bring in when they got two times 21 and two. Yeah. Yeah.

**[02:32:38]** Thank you. Yeah it's. It's been, it's been. I have been putting in some time, some hours and it's like yeah, I mean the code is coming a long way that like the general architecture is coming a long way. The sophistication of the architecture is coming a long way.

**[02:32:54]** The processing pipelines come a long way and just yeah, the community itself is coming a long way. Just kind of like, like, like it's all well and good to make a cool software but if people can't find it, people can't use it. Like it's not really doing anything for anyone.

**[02:33:09]** So yeah, it's good, I'm happy with it.

**[02:33:14]** And yeah, What else I could go in and do like one could. I couldn't. If it wasn't two and a half hours into the stream, I could go in there and talk a lot about like oh, did we crash? Yeah, we crashed eight cameras. Why did we crash?

**[02:33:43]** Oh this, I know this. There's, there's a race condition in the, in the, in the, the alignment part that I know how to fix it just. But there it is technically possible for the, the multi frame grabber to grab like to like Ms. Grab and like you. And then it, it's set up that like if it gets the wrong frame number pukes itself out.

**[02:34:12]** I can fix that with a little bit of logic. It's like it doesn't happen until you start taxing it, but it can be fixed.

**[02:34:23]** Great question. Do I feel pressure from AI making this obsolete suddenly? No, absolutely not. So I use AI extensively, extensively to make a lot of this stuff. I also.

**[02:34:36]** So Skelly Bot is a tool I made. I've been using it to teach my classes now for I'm about to start my sixth semester using it. I have a PhD in cognitive science. Like I know how AI works. FreeMap has always technically been an AI based software because the code, the tracking that runs the actual image detection is a convolutional neural network that's trained on data.

**[02:35:03]** So technically speaking it's not large language model based, but it is, you know, it's AI based by some definition the term AI, but. And so yeah, there's a lot of tools.

**[02:35:20]** Yeah, Java knows what's up. There's a lot of tools out there that are coming out that like Gaussian splatting and a lot of stuff like that. Like there are some tracking methods now that are using transformers that probably get better performance than, than like these ones that I think are using CNNs. I don't know if they're, I don't know if it's like a transformer, CNN or whatever, but where am I at?

**[02:35:51]** But yeah, the thing about the current landscape of technology and AI is everything is very, very heavily focused on just generative AI. Generative AI produces data that is useful. I'm not an AI hater by any means. In fact, I hate the tech corpos and their fascist approach to life, but I think that properly.

---

### Chunk 17 [02:36:00 - 02:45:58]

**[02:36:00]** Focused on generative AI. Generative AI produces data that is useful. I'm not an AI hater by any means. In fact, I hate the tech corpos and their fascist approach to life. But I think that properly managed like AI should be like a liberatory technology.

**[02:36:20]** Like if we as a people can learn how to harness it and just get better at everything, it could wind up like helping us free ourselves of the stupid landscape of corpo tech fascists that we currently live in. But even from like, from a practical sort of software based perspective, there is a very, very important difference between like a generative AI thing that you like so generative AI and like a computational research scientific tool.

**[02:36:53]** Because for example, like 3D from 2D, right? The single camera approaches to motion capture that estimate the depth from a singular image. For those types of cameras, when they are measuring the 3D orientation of my body, they're making some kind of machine learning driven inference based off of some statistics. And necessarily it's an inference, it, it's a guess, it's a statistical guess.

**[02:37:23]** When I do multi camera calibration and use the charcoal board and do like a bunch of like old school, you know, like, like epipolar geometry and stuff like that. Those are not inferences, those are computations. And so the they, those are truth preserving operations. So from the raw data coming off the cameras through the various sort of processing stages, because I am explicitly not using trained models to produce the output, I can trust each step of the process in a sort of, they're truth preserving operations. So my epistemological grounding associated with the original measurement from the cameras is maintained through the pipeline so that I can then look at this sort of finalized output and say I believe that that data tracks the reality that it measured.

**[02:38:20]** And the only part of that pipeline that uses machine learning based inference is the part that draws, that estimates the 2D skeleton from the image. And very, very importantly, that stage of the pipeline has direct eyeballs on validation. You just look at it and say, oh yeah, that's doing an okay job. So this is an AI software, but the AI sort of goopy statistical inference part is being very, very carefully managed in order to allow for this to be a scientific tool. So if so like the paid softwares like the, your Rokokos and your Move AI or whatever the hell else like they are very explicitly, I don't know if they would say in public, but I have heard them say it in private.

**[02:39:10]** Like they're not trying to make a scientifically valid tool. They're not trying to make data that it has like empirical validity because they cheat. They have as part of their pipelines like machine learning neural network, like neural networks that are trained on what good data looks like and they take your crappy data and they run it through their good data neural network and then they spit out something at the end and that looks good but loses its connection to the empirical reality that you're claiming to measure. So yeah, I don't really see myself or Free mocap being invalidated by AI. If anything, I'm super stoked about the possibility of AI bringing more people into the fold.

**[02:39:59]** AI helps people write better code. Andres man, I watched this guy, I watched his, his skill sets just like leapfrog because he knows how to use AI to sort of punch above his weight and yeah, and I think that the, you know, I've used AI in my classes, I've used it for teaching, I've used it to help like level people up and I've used it to level myself up. And so I'm excited to start like really leaning more heavily into that and trying to build more like, like assistive tools that are kind of like built like have eaten our documentation and can give people like, you know, speaking of the website, let us, let us end this stream before the next ad break comes in four minutes by looking at like the original sort of like you know, mission statement. Free mocap project aims to provide research grade markerless motion capture software to everyone for free. We're building a user friendly framework that connects an array of bleeding edge open source tools.

**[02:41:06]** Bleeding edge changes by the years but still true bleeding edge open source tools from computer vision machine learning communities to accurately record full body 3D movement of animals, robots, humans, animals, robots and other objects. We want to make the newly emerging mind boggling future shaping technologies that drive Free mocap's core functionality accessible to communities of people who stand to benefit from them. We follow a universal design development philosophy with a goal of creating a system that serves the needs of professional research scientists while remaining intuitive to a 13 year old with no technical training and no outside assistance. A high quality, minimal cost motion capture system we transformative, blah blah blah. We hope the system blah blah blah blah.

**[02:41:46]** It's this part right here like this idea of trying to make something which is simultaneously a high level research tool but also is accessible to like some random kid that wandered in off the street. And I think that if we, if we can sort of bring the AI LLM sort of that side of it using kind of like the things that I've learned about using AI in a teaching environment to bear, I think we could really continue to do something really special and make something which sort of like it starts out as this kind of a tool and like we have like the big friendly buttons on it.

**[02:42:29]** That would allow like a non technical person to use it but also like somewhere in the wings have some like, some like local or remote, some kind of like LLM type of AI that's like saying hey, do you want to understand a, any part of this? Like does any part of this pique your interest? Do you want to know more about the cameras? Do you want to know more about the, the geometry? Do you want to know more about the scientific application?

**[02:42:53]** Do you want to make a blender scene from this stuff? And like, like feeding that with our own sort of shaping of stuff so we don't. We're not trying to like corpo suck data out of people, just really trying to like elevate people's connections. I think there's really a lot of possibility there and I. Yeah, we'll get there. Skellybot.

**[02:43:12]** Skellybot exists. Okay, two minutes until an ad comes and I, I am, I'm done. I'm done. I'm signing off. Thank you, thank you for watching and coming along.

**[02:43:28]** Thanks for following on this update. This recording is going to go to YouTube and then we'll probably, we'll try to chop it up into sort of more editable parts. Should hopefully getting my people record setting. No, there was definitely in the old days when I was like I think my max was like 20 or 30 or something like that back when I had like funnels and like it would post announcements to like Twitter. Back when that existed this was a just raw stream.

**[02:44:06]** So for you who showed up, thank you for making your way in here. I assume that you have some kind of a notification bell that goes off when I start streaming so thank you for that. My plan is to start streaming more on the regular. I would love to stream on like a weekly basis just to sort of be a little more communicative about what's going on and yeah, okay, I'm gonna pass out. Okay.

**[02:44:31]** First let me do the tradition of I can raid y' all into somewhere.

**[02:44:40]** Who's there? Code Nico Codemico I believe is still using a Rokoko suit.

**[02:44:52]** If we ever get this is long term growth potential is of getting Code Miko to use free mocap real time. But realistically I think it'll be a second before we're there, but who knows? I'll stream y' all in there. You're. I wish there was someone I knew who was smaller, but I don't know anybody.

**[02:45:10]** So how do I do this? I think I do. Go there. Go there.

**[02:45:19]** I say slash raid. Yes. And I do code. Miko, do you do the whole thing like that? Probably not like that.

**[02:45:30]** Invalid username. Okay.

**[02:45:34]** RAID channel.

**[02:45:44]** Okay. Hate to throw you all into a giant server with a thousand people, like multi thousand people running it in the chat. I've never. I've never understood people like that. That particular vibe of, like.

---

### Chunk 18 [02:45:45 - 02:47:06]

**[02:45:45]** Okay. Hate to throw y' all into a giant server with thousand people, like, multi thousand people running it in the chat. I've never. I've never understood people like that. That particular vibe of, like, in the chat stream, but, you know, whatever works.

**[02:46:04]** Okay.

**[02:46:09]** All right. I think that's it. I think it's going to boot y' all out, if it hasn't already.

**[02:46:15]** I don't know. Yeah. But thanks for showing up and. See you around. And I'm gonna try to stream on a roughly weekly basis, probably around this time of, like, Thursday afternoons.

**[02:46:30]** I'll probably. I'll put a schedule up on my actual page and.

**[02:46:38]** Oh, no. All right, I'm gonna go. I'll hit the button before the ad starts. Oh, we're in an ad right now. Never mind.

**[02:46:43]** Okay, bye. Does that go? Are we done? I think we're not done.

**[02:46:54]** We are. I think they're gone. I can never know. In any case, emotionally. Emotionally, I am finished.

**[02:47:05]** Okay, goodbye.

---
