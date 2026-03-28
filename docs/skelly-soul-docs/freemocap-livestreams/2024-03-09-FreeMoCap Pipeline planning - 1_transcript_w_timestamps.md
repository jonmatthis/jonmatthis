# Transcript: 2024-03-09-FreeMoCap Pipeline planning - 1

## Source Information

- **Source Type:** Local File
- **File Path:** `C:\Users\jonma\syncthing-folders\jon-alienware-pc-synology-nas-sync\videos\video_eater_downloads\playlists\[OLD] FreeMoCap Development\2024-03-09-FreeMoCap Pipeline planning - 1\2024-03-09-FreeMoCap Pipeline planning - 1.mp4`

---

**Total Duration:** 01:25:27

---

## Full Transcript

### Chunk 1 [00:00:01 - 00:09:58]

**[00:00:01]** Okay, let us. Let's keep going on this guy, huh? Not that guy. That's a different guy.

**[00:00:18]** I had some thoughts on how to update that because is Krita a multi window friendo? Did you do that? Can I have more open at once or do I gotta convertcha to the thing? New window.

**[00:00:34]** Nice. I'm really digging Krita. Krita. Krita.

**[00:00:40]** I should. Yeah. Well.

**[00:00:48]** Not quite at this moment I think think but soon I shall be.

**[00:00:59]** The system of donations to open source project needs work because the thing is is like it's always put in these places where it would be a huge diversion for me to like go somewhere else and start thinking about money. There's a couple organizations, there's ways of dealing with this. But like just thinking about it from like a strategic perspective. It's like you have to find a situation where people it's like either can give in one place that gets distributed too many or they are. They have to already have their wallet out.

**[00:01:34]** Like they're buying something that they want. And there's like hey, do you want to like throw a couple extra bucks or like even better like turn on like a low recurring amount which is like the Wikipedia model. Wikipedia's like Wikipedia is like periodic just like guilt push. It's like hey, could you click here just like one time.

**[00:01:55]** Okay. Anyways, focusing here we are. So we've got. I realized I think there's three general. I think I had like a structure thought you.

**[00:02:15]** And this is going to be like the main pipeline and I want to have like observables different color. What color we going to use here? Let's pick colors.

**[00:02:33]** I want that dude's thing that gives a good like I bet there's a plugin that's like triads and stuff like that.

**[00:02:42]** But I like. Okay, here, here it's a little red spaced. Ooh, yeah, that looks good. Sure.

**[00:03:04]** Yeah.

**[00:03:09]** What the was that? Oh yeah. Saturate.

**[00:03:27]** Sure, why not? And so we've got like the stage and I really. I've decided I'm also. I'm gonna. So yesterday or whatever this was talking in terms of like the real time pipeline which is fine.

**[00:03:43]** I'm gonna stop talking about it like that just because it doesn't really. It's the same pipeline. It's just like are you doing it in on videos in a loop or are you doing it on single frames and sort of keeping track? Doesn't really matter.

**[00:04:00]** I can do because I've picked them. They just. They're here now I can go doink okay, so this is going to be this stage or whatever. And then up here I think we're going to call these. We're going to talk about the observables and down here we're going to talk about the output.

**[00:04:25]** I'll bet there's a way to change those colors retroactively, but I don't know it and I don't want to find. I do want to find out, but I don't care to look right now.

**[00:04:34]** Output. Okay.

**[00:04:40]** And so in the stage we have.

**[00:04:54]** Okay, and so we have.

**[00:04:59]** It's fine, it's fine. So we got the real world. Oops, Let's put it here. Measurement.

**[00:05:12]** The part we don't have a part control over. So we have skellycam.

**[00:05:27]** What does cameras. Is that mostly what it does? It does cameras. Yeah, let's do videos. It produces videos.

**[00:05:41]** But will it import videos? Is that necessary? I think eventually it will be, but who gives a shit? It's equivalent at some level. Okay, Camera ship.

**[00:05:51]** Okay. And then we're gonna do the full whole route here because we can do that. And then from skellycam we go to Skelly Tracker. That's right, Tracker, which does.

**[00:06:18]** 2D tracking in images.

**[00:06:29]** Again, I know that it also does 3D in images, but it's not valuable. So it's. In any case, at some point this will also. It does produce a 3D estimate, but not in a way that is useful to us at this juncture.

**[00:06:48]** I'm not going to fix it. Well.

**[00:06:53]** Now this is a little bit trickier, but I think I'm still just gonna. I'll make it kind of like one of these because we're still. This is still clearly not endgame.

**[00:07:10]** And this is like, I'm just gonna call it, call it any. Or I'll call it camera calibration because the name doesn't actually matter.

**[00:07:30]** Camera, Camera capture, volume calibration.

**[00:07:53]** And like it's kind of off the main pipeline because it doesn't. It happens like previously. But it is what leads to our ability to do 3D reconstruct, slash triangulation.

**[00:08:18]** The thing is like everyone here, like the world's all like machine learning, AI, blah, blah, blah, statistical inference methods, hooray. And they are super powerful, but they're not as like direct measurement and computation is always going to be more reliable than inference from training data. So what we do is we use both. Use both of these things, you see.

**[00:08:43]** Okay, so we don't have a name for that guy yet. It's any pose. It's whatever.

**[00:08:49]** And then we have Skelly Forge, who we have decided is going to stay one one blob because Skelly Forge does post processing.

**[00:09:11]** Post processing and specifically does.

**[00:09:23]** Data agnostic cleaning.

**[00:09:33]** And then it does data aware cleaning.

**[00:09:42]** I'll list that shit out later, but I guess I'll do it now. Am I getting rabbit holed? A little bit, but I think it's fine because this is kind of the part where I'm still trying to. I kind of get it, but I'm trying to figure out how to talk about it in a way that makes sense to other people. So this is stuff.

---

### Chunk 2 [00:09:45 - 00:19:40]

**[00:09:45]** Now am I getting rabbit holed? A little bit. But I think it's fine because this is kind of the part where I'm still trying to. I kind of get it but I'm trying to figure out how to talk about it in a way that makes sense to other people. So this is stuff like filtering, smoothing.

**[00:10:05]** We don't really do much of that, but it's fine. We could filtering a smoothing are kind of like friends. And then you got your gap filling, etc. And that's your shit where it's like, it's like it doesn't matter what the data is. It's irrelevant what the data is.

**[00:10:25]** It's just like it's a time series with a gap in it. It's a squiggly line that is jaggedy and we want it to be smoother. So it doesn't matter the content of the data like whether or not it's like a, you know, like, I don't know, like a missile launched or a rocket. Rocket launch, Missile launch, rocket, whatever. Yeah.

**[00:10:45]** If it's like earthquake data or skeleton data, you still are using a Fourier transform just to filter it at some level. Data aware cleaning is going to be your like enforcing rigid body constraints, which is sort of like the, like. Oh yeah, the shoulder and the elbow we're going to assume as a rigid body. So any variation in that length is error and we're going to clean that out. Like you have to know that it's a shoulder that's connected to an elbow to be able to do that.

**[00:11:29]** So it's data awareness. We are currently doing stuff. Oh, cleaning might not be.

**[00:11:47]** Maybe it's not just cleaning, it's also like manipulation because it's like virtual markers.

**[00:11:59]** And like.

**[00:12:08]** So I don't know if like this is kind of. This one in particular is like wait, is that, is that, should that be here? I think it should because it's kind of like, I guess this, the forge aspect is like you're spitting out the completed data. Virtual markers are like, we only measure like shoulder and shoulder but you kind of need a marker to be here. Like you need a data point here.

**[00:12:29]** So we calculate this chest center by taking just like the average of these two points. So those are called virtual markers. And it's just like a part of the, part of the game we have. All of our markers that have underscore center are virtual markers. So we have a neck center, a chest center, a hip center and a head center.

**[00:12:48]** And those are all calculated by just taking the weighted sum the individual things, which if you only have two, the weighted sum is the same as the average. Actually, it's all. The weighted sum is always equal to the average. If the weights are the same.

**[00:13:09]** Anyways, who cares? And then from that we have exports.

**[00:13:22]** Not my problem anymore is what we say at this point, exports to including like save a disk, Including Santa Send to Blender is not really the end of our pipeline because we do make blender code. Well, well, well, fine.

**[00:13:59]** Skelly, Forge.

**[00:14:03]** Well, I don't. This is another one without a name. Well, I guess it has a name right now, which is that it's like blender shit.

**[00:14:17]** What is this part at a computational level, what is happening at the blender part? We're creating. It's like we're creating like the animation stuff, but I'm just going to call it blender stuff for now.

**[00:14:39]** And then we'll kind of. Because it's like it's creating, like it's creating the rig and the armature.

**[00:14:46]** I mean, the rig is the armature, I think. And then it's like putting a mesh on it and doing. Does it do anything else? Like, it makes it into an fbx. It makes it into a blender scene and FBX scenes, but it's not.

**[00:14:59]** Is it doing any computations?

**[00:15:04]** I mean, I mean, obviously it is, but is it doing any like interesting computations? Or is it just like attaching stuff to stuff? Is there data manipulation? Is there something that comes out of this at the end, which is like a new piece of information that we didn't have before? I'm not sure Andres is playing with ik, but he's definitely.

**[00:15:27]** If he's doing it in a way that we will be able to pull out. Because I think the main. Actually, I think this is kind of like the workflow is the blender is a tool that allows you to use like their very powerful computational stuff to do manipulations on the data that do produce meaningful outputs and meaningful changes to the data. And I think that as we are making those, when we see them solidify, we say, okay, we're going to slurp you back out. And now you're going to be in the main pipeline.

**[00:15:55]** And that's what happened with the rigid body constraints. That was from Andres. And I was like, ooh, I want that.

**[00:16:07]** It's just such a. The cleaving point is so strong. But the.

**[00:16:15]** We'll see, we'll see.

**[00:16:22]** It's just like making an additional sub repository seems like a high cost, but maybe it Isn't it? Depends.

**[00:16:32]** We do tend to. Well, we need a better workflow for doing the updates and stuff like that. And it's.

**[00:16:41]** I need people, I need money. I need enough money to pay full timers. Anyway, blender stuff. What are we doing here? We do blender stuff.

**[00:16:54]** Yeah. Nailed it. Okay, so that's the pipeline. Hooray.

**[00:17:01]** Create sketchup.

**[00:17:16]** Don't judge me.

**[00:17:21]** Okay. Doink. I said doink. Thank you.

**[00:17:34]** Come on. Come on. Oh, that's just bad iconography and whatever the hell's going on here.

**[00:17:46]** Okay, like it doesn't have. I, I guess it doesn't have the, the diagonal icon doesn't show up for whatever reason, but it still, it still grabs that control point. It's fine. Just kind of like, Yep, that's, that's that open source flavor. It's like that is not on the priority list.

**[00:18:07]** I'm sorry, you're gonna have to figure that out. And because it's an open source project, we're like, oh, if it wasn't an open source project. Be like, fuck you. This is how we do. Okay, so now here.

**[00:18:26]** Oh, hey, what the shit?

**[00:18:37]** Okay, so now let's talk about the output. Because this is easy and the observables will be harder because it's a little bit. It won't be that hard, but it should be fine. Okay, It.

**[00:19:21]** Output. What do we call it? Strip. Output. Strip.

**[00:19:32]** Okay, so what's the outputs? See the outputs here? Hey now, hey now, hey now.

---

### Chunk 3 [00:19:32 - 00:29:30]

**[00:19:32]** Okay, so what's the outputs. Do the outputs here. Hey now.

**[00:19:38]** Hey now. Hey now.

**[00:19:45]** You know, you can just put. There's like AI image generation stuff. Krita plugins.

**[00:19:57]** Krita, what are you built on?

**[00:20:03]** What's your deal? Krita? Tell me. So KDE is apparently a group of interest.

**[00:20:13]** They make a bunch of stuff.

**[00:20:16]** Gpl.

**[00:20:19]** Use a gpl, you cowards. But, but this is like they've been around. They're venerable enough that like agpl, like closed. Closed AGPL closed a loophole.

**[00:20:34]** It says mirror this mirror. Can I make it? Oh, they don't even have issues on here. That's interesting. They have their own like internal GitHub looking thing.

**[00:20:46]** It's the KDE thing. Yeah, it's like an. It's an interesting. And I, you know, I'm curious. We'll see.

**[00:20:55]** C. I should just learn C. I mean, I already, I technically have been taught it. The only tech. The only, like, official computer science education I got was two semesters of comp Sci in my first year of grad school where they taught me C. And I was able to do it, but it's just kind of like. And it's like, it's. It's not that hard.

**[00:21:25]** It's just uglier. It's just, there's more syntax and you have to be more mindful about like, types and pass by value versus pass by reference and stuff like that. Okay. Anyway. Output.

**[00:21:37]** Output. Pink. Output is pink. We decided that already. You see?

**[00:21:43]** Okay, Skelly cam. This one's easy. So you have.

**[00:21:50]** Oh, maybe it's not so easy. Well, it is easy, but there's like, there's. There's freckles on it. Wrinkles to it. Term dermatological analogy.

**[00:22:03]** Okay, so main output. Main. Okay. Okay. Data is.

**[00:22:20]** Videos, Images. Ooh, Goodness. Check, Checks. Synchronized.

**[00:22:52]** Cams pointed. Good.

**[00:23:01]** Unpack that later. And cams configured. Good because like, you can point the cameras in the wrong direction. So like, this is. I'm like a little low in this thing.

**[00:23:16]** So they're not pointed that good. This would be a little bit better. This would be bad. Similarly, who are you? Who are you?

**[00:23:26]** This one. Similarly.

**[00:23:33]** Actually don't know if it will give me enough control here to make it actually bad. It should. It's color range, color stuff. Wish you would have a. Come on.

**[00:23:47]** Where's the exposure, my dude? Configure video. There we go.

**[00:23:55]** All this stuff. See some of this. This is one of those things where like, I don't know if this is camera controls or if this is like post processing. That looks better though. Actually, I kind of like that better.

**[00:24:10]** Okay. It's too dark. Who cares?

**[00:24:17]** Default. Auto.

**[00:24:21]** Can't. Auto. This is probably on camera. I can't tell. And then I can't tell and I don't know.

**[00:24:30]** Default default. Okay. Camera control. Okay. Okay.

**[00:24:35]** When video proc amp.

**[00:24:43]** Thank you. I'm so glad you were able to save all that time writing whatever the. I assume it's video process amplification amplifier point is. I'm so glad you saved the time. Clearly you needed the space.

**[00:25:01]** And.

**[00:25:07]** There's no mouse over and there's no question mark.

**[00:25:11]** It's fine. It's great. It's great. It's great. It's great.

**[00:25:17]** Oh, yeah. See, this is our guy. This is this weird number that is this strange thing. Focus doesn't do anything right. It shouldn't on this camera.

**[00:25:25]** Yeah, you can't. Oh, it's auto.

**[00:25:31]** Yeah. There's no difference to go back to auto exposure, though. So see, that's not good. That's not good. I it up and I killed it.

**[00:25:49]** I may have.

**[00:25:55]** Wake up Betty. Welcome back.

**[00:25:59]** Okay, this. This is a rabbit hole. But.

**[00:26:09]** See, so see how there's no blur because the exposure is so low that the time that the window is open is not enough for there to. For it to pick up motion. It is wobbly. But that's just because it's a global shutter. Or not a global shutter.

**[00:26:24]** So what's it called? Rolling shutter. That's just look it up.

**[00:26:32]** Nine now. So the question is, like, is it better to have it like. This is clearly too dark, but it could be. This is probably like. I would.

**[00:26:44]** This is maybe a little dark. Depends where I am in the room, what I'm wearing. Da da da. I don't have any melanin, so I tend to show up pretty well.

**[00:26:54]** And. And I will. I will take this from doing mocap Y stuff. I will take this over this where you can see it's blurring all over the place. You see that?

**[00:27:05]** Don't just tell the difference. This is like a weird. You know, like the thing of like. Like, oh, you have like a wobbly pencil. You can just do that.

**[00:27:11]** But it's like blur, blur, blur. You can't tell shit what's moving here. It looks nice when I'm not moving. And you might say, oh, that's better. But this.

**[00:27:23]** That's too dark. This is better for a mocap because you see how there's less blur. You can still probably see it. There's some blur in my fingers. Whereas if you've got the nine, there's.

**[00:27:35]** It's. It's rolling, shuttered, but it's not blurring.

**[00:27:40]** My wrist feels weird. I did that too much.

**[00:27:46]** And then auto. But see, like. So Auto takes it too high, right? Because look at all this blur. And I don't know.

**[00:27:54]** I still don't really know. I don't.

**[00:27:59]** I don't know how there would be setting auto. I don't know if it's on the camera itself or it's happening in software because you can just analyze the image and be like, oh, it's too bright. Let me bump it down. But whatever it is, it's not what we want because of the blur.

**[00:28:22]** And all of that is to say that there is a difference between the physical orientation of the cameras and the software configuration of the cameras. And those are the goodness checks. And that's what we're doing down here. Was there anything else we need to check? Synchronized camera's pointed.

**[00:28:36]** Good. Yeah. Goodness. It's not checks, it's criteria and then diagnostics.

**[00:28:51]** So.

**[00:28:56]** I'm tempted to put timestamp data up here in, like, the main data output because I consider it to be so crucially essential to. I'm going to do it. I'm just going to do it. Like, technically speaking, you only need the images, but if you trust Skelly Cam to have synchronized them, then you don't need the timestamps, but you shouldn't trust anything to do anything. So if you're.

**[00:29:26]** Because it's like, I know that a lot of people are gonna be like, no, you don't need the timestamps. That's.

---

### Chunk 4 [00:29:15 - 00:39:14]

**[00:29:15]** Trust Skelly Camps. You have synchronized them. Then you don't need the timestamps, but you shouldn't trust anything to do anything. So if you're. Because it's like, I know that a lot of people are gonna be like, no, no, you don't need the timestamps.

**[00:29:29]** That's secondary. But it's just like. But I.

**[00:29:35]** Okay, enforce your philosophy. Why not? Like, it's not secondary. Because don't trust me. Like, what's wrong with you?

**[00:29:42]** What's wrong with you? Like, have you seen how hard this is? Don't trust me. Don't. Like.

**[00:29:47]** Don't. Like. Like you're thinking here, like, oh, no, I trust them to have done their job right. Don't do that. Don't.

**[00:29:55]** I promise you. Like, you can appreciate the work that was done. You can appreciate the expertise that went into it. Don't trust it. Begging you, please.

**[00:30:08]** What am I doing? And why am I doing it? I want to grab you. What's your. Who's it.

**[00:30:16]** How do you. Give me. What's your tea, T. Thank you.

**[00:30:31]** Yeah.

**[00:30:34]** B. B, wait. Control shift A, B. Nailed it. I should be using colors here, but I'm not going to. Video images.

**[00:30:46]** It's not, though. It's not the actual data. You can't calculate anything from it. It doesn't. Nothing on the later steps.

**[00:30:51]** Relies on it.

**[00:30:58]** Fine. Which is why I will put this additional layer down here of diagnostic data, and then we'll just enforce kind of like a culture around diagnosis and check your numbers and, like. Because right now there's a thing of, like, some people coming into the server, and they're like, oh, the hands don't work. And then like, my folks are like, oh, what version did you use? And it's just kind of like, wrong response.

**[00:31:22]** Like, oh, my data didn't work. Get. Give me the data. I'll look at it. Like, that's the response.

**[00:31:25]** Like, I don't. Like. No offense, but I don't trust your ability to analyze the situation enough to not waste my time by me, like, asking you questions. Show me the data, and I'll tell you if it's bad. And I'll.

**[00:31:37]** And like, it's. And then. And like. And now I have your data, and that's. And so now I. I actually.

**[00:31:45]** I will be motivated to do it because I'll get something out of it, which is I get to see how you've. I get to see your data, and if you don't like that, don't fucking ask me to do any work. For you, like, sorry, I'm sorry that I gave you something for free and then it didn't work the way you wanted. Now you came here and asked me for fucking extra labor. My dude, my hypothetical dude, please tell it to the bottom of the ocean for me.

**[00:32:13]** And I am not here. I'm not here for that. This is the beauty of open source. It's like, I don't like it. Okay, fuck off.

**[00:32:21]** I don't care. Wonderful. Wonderful. Okay, Diagnostic data is timestamps per frame.

**[00:32:35]** Anything else?

**[00:32:42]** No, that's actually it. Everything else is sort of calculator from that.

**[00:32:47]** I don't want to talk about derived data. Fine, I will. Jesus.

**[00:32:55]** That's going to go into the observables now.

**[00:33:01]** Move on. We're top view derived data shall come up here also. These are in the wrong order. This is. Oh, this is the wrong order.

**[00:33:14]** Nice.

**[00:33:20]** It should go stage output observables. Because observables is basically visualizations on derived data.

**[00:33:31]** Great. Alrighty. Thank you everybody. Thanks for coming to the show. I appreciate everything about you.

**[00:33:48]** T. Remember that. Remember we learned that as a group. Ah, that was great. We're gonna delete the bottom step anyway, so it's fine. Oh, that's too far back anyways.

**[00:33:59]** So kind of the same guy as this anyways.

**[00:34:09]** Sometimes it just. It just all catches up at once. Control D. Pipeline strip and a grab whip and I see. Who are you? That's your name.

**[00:34:31]** Why don't you tell me when I'm hovering over you with this thing? But you do tell me when I hover over you in this thing. Is it be. I wonder if it's because there's like tremor.

**[00:34:45]** Not like, not like clinical tremor, but just like it's not perfectly still because it's attached to a biological system. You see?

**[00:34:55]** What was it? Control R. Control R. Nope. Oh, that was Control Shift R. Control R. What's Control Shift R? Reference images tool.

**[00:35:16]** Another time.

**[00:35:34]** Oh, you see how I fly. Stop, Stop.

**[00:35:47]** All right. Different layer.

**[00:35:50]** Did I get a bit there? Yeah. I'll want you later. Fine. What's your deal?

**[00:35:54]** Lasso. Oh, where'd it go? Oh, because I'm using my mouse. You just don't have one. Okay.

**[00:36:11]** It's funny that I'm like, oh, do I have space? It's like, zoom out.

**[00:36:17]** Yes, you do. You have invented this entire space. You can have as much room as you want.

**[00:36:33]** See, I should use guides and stuff here to make this line up. But I mostly right now I'm just trying to have enough room to Write. Because this is clearly. And this is not end goal either. Control R. Hey.

**[00:36:54]** Oh. How did you control oh? I guess just. Oh. Grabbed everybody on the layer.

**[00:37:01]** That makes sense. It's a nice thing to have.

**[00:37:09]** Come on, come on, come on. Hey. Control Shift A. Control T. Control Shift T. No, tablet event. Control R. And then I hit T. Move that there.

**[00:37:26]** It breaks up the arrow, but I don't care. Is that a song? And then also put the part where I said I don't care. I was lying, apparently. I can tell from my behavior.

**[00:37:49]** I was like, wait, why am I using a mouse with a tablet? I'm like, I can't get enough precision out of this mouse. It's like, well, if only you had a tool for that in the same hand that you were using to control the mouse. Listen, I don't need your attitude.

**[00:38:08]** Blah, blah. Okay. Mm. Mm. Okay.

**[00:38:13]** Now we're back to this strip and Control R. Now look at all of this room for activities. T Grab. Thank you. Hey, and eventually you're all gonna. You're all gonna move up and then you'll be sorry.

**[00:38:31]** Okay? Alrighty. Me running. I'm already out of steam. How are we doing?

**[00:38:38]** 38. 20 minutes left before I turn into a plumpkin. Okay, pink. We got this. Pink.

**[00:38:45]** Let's make. Let's just keep it. Let's keep it simple. What's the saying? Keep it simple, you son of a b.

**[00:38:57]** B for brush. We're on pink. Pink's good. We're just gonna do that. Shut up.

**[00:39:04]** You know, this eventually will want. There'll be some. There'll be some clever hierarchy of colors and shapes and stuff like that, but for now, we just.

---

### Chunk 5 [00:39:00 - 00:49:00]

**[00:39:00]** Good, we're just gonna do that. Shut up. You know, this eventually will want. There'll be some, There'll be some clever hierarchy of colors and shapes and stuff like that, but for now we just, we just, we just clump it together. Because this is just for my brain for later.

**[00:39:19]** Right? Like this. Like this. Sloppy. This is not for external consumption.

**[00:39:24]** This is for me.

**[00:39:29]** So I can have a better time later. Okay. Skelly tracker. What's the data? What's the data?

**[00:39:35]** What's the data?

**[00:39:38]** Oof. This is really quality. Who cares? Data is two dimensional tracking data.

**[00:39:56]** The form. I'm not going to talk about the form. It'll probably be numpy arrays for speed, but there's all these other like options like plex. Plex, Jax.

**[00:40:07]** There's some shit. Anyways, 2D tracking data, it will be of the shape.

**[00:40:18]** This is gonna be smaller.

**[00:40:21]** Okay. Data for now it's gonna be a numpy array for currently a numpy array.

**[00:40:30]** No, I'm not gonna specify because then. Because it's like people just get hung up on things and it's like, ugh. It's like, Wait, what is that? It's like, hey, it's. It's equivalent is what it is.

**[00:40:42]** My dude, calm down. My hypothetical dude. Okay. And it's gonna, it's gonna be number of chems, number of cams by number of frames. This is the video case again.

**[00:40:59]** We're still talking in that space. If it's, if it's not a video, it's just one. So in real time it'll just be one Ooh. Or two. You could just clump them.

**[00:41:11]** We could pre clump them in real time.

**[00:41:15]** Which is a classic way to like that would actually be a good move because it'll be smoother. Like if the real time processor just gets the average of every three frames, it'll be at 30fps. It'll be 10fps real time. But it will be smoother because you'll be sacrificing 66% of your data. Because take three data points, replace them with the mean of those data points.

**[00:41:44]** That's just the classic smoothing window. Smooth. And you have sacrificed 60% of your data in order to have one cleaner estimate on the assumption that the time scales are not blah, blah. You'll just be lagged. Who cares?

**[00:41:58]** Number of cameras, number of frames, number of tract points, And then 2D. So it'll be X, Y and it'll be, you know, pixel coordinates, normal sticky coordinates. Doesn't matter.

**[00:42:21]** Great.

**[00:42:24]** And how Will we know if it's good?

**[00:42:30]** There's not a lot of ways to know if it's good, I guess.

**[00:42:38]** Confidence values, I guess because all these trackers give you confidence values but they are not fucking trustworthy. They're not trustworthy and they don't. And they're not commensurate. So MediaPipes 0.8 confidence is not the same thing as OpenPot is. 0.8 confidence is not the same thing as deep lab cut.

**[00:42:56]** 0.8 confidence. And none of these fucking things should be trusted. And they all call them different things because the computer science community just like makes shit up as it goes along. So MediaPipe calls it visibility, Openpose calls it confidence. I think Deeplab Cut also calls it confidence.

**[00:43:15]** But the numbers are all weird and you shouldn't trust them anyways because never ever, ever trust a neural network to tell you it's confidence. Because they don't. They don't. They're not good at that. Like 0.99 is quite a bit different from 0.1.

**[00:43:29]** Beyond that man, that is an open fucking question. Okay. Confidence, smoothness, Reprojection error. We don't get reprojection error yet. This is going to be some.

**[00:43:52]** This is where it going to get, it's going to get gloopy where you're going to have to like loop back because we're not going to like. We're going to use the 3D reconstruction to tell us how good the 2D tracking is.

**[00:44:09]** Get there. Okay, cameras, frames, conference. What else do we got in 2D tracking land.

**[00:44:20]** That tells us if it's good that we can determine with this data alone. That's the game we're playing is we're keeping it stage by stage. So we are right, so we don't have reprojection error. We get that from here. So we assume that it's a waterfall situation.

**[00:44:37]** So each successive stage has the stuff from the previous one.

**[00:44:46]** Diagnostic data. Do we have diagnostic data? I guess we have computation time. I guess we don't really measure this now, but we will. Like just how long did it take to process that data?

**[00:45:01]** Is it this? So this like confidence and smooth. These are all derived data types. Does 2D tracking, I guess we do get. Get confidence is pre.

**[00:45:15]** Is. It's like it's reported diagnostic but these are all it's. It, it. It's kind of like timestamps. I'll.

**[00:45:25]** I'll count confidence, I guess.

**[00:45:29]** And.

**[00:45:39]** Because it's a new data type, it's a new data blob. That we won't. It's not derived. So yeah, that's diagnostic data. And then like confidence threshold, I guess that's a cleaning technique.

**[00:46:00]** It's a quality criteria. Is. Is the confidence value above a certain amount, Is the smoothness above a certain amount. And I guess it's a little bit different than these because these are, this is, this is computable. This, I guess, is computable.

**[00:46:17]** You could just look at how much of the, much of the subject is visible in the scene. But it's also, you can't. That's not directly computable. Also like the, the, the brightness and stuff being set is also not directly computable. So let's move on.

**[00:46:35]** So computation time is a diagnostic doesn't really tell us about the data quality, but it does tell us about the pipeline.

**[00:46:45]** We get that from here. It's fine. Okay. We're talking data. We're not talking software data and computations, I guess.

**[00:46:53]** And the media. The ML reported confidence value is also diagnostic data. I can't think of anything else. If I do, I'll come back later. Okay.

**[00:47:03]** And now we're doing the 3D reconstruction. Let's just assume that camera calibration has already occurred and it went fine.

**[00:47:15]** Let's just, let's just go. We're gonna cut this off a little bit. Let's just assume it worked out just fine.

**[00:47:28]** Assume it's fine.

**[00:47:35]** Dear me. Okay. And so this gets us. The data we get from this is the 3D trajectory data.

**[00:47:53]** And this. Yeah. So we don't have a skeleton yet. We just have trajectories. Right.

**[00:47:57]** And so this is why Skelly Forge is a good name because you are forging the Skelly. But until that point, you don't have a Skelly. You just got some dottos. You got some. You got some swoop de doopty dottos.

**[00:48:08]** In space, they have names, but we don't. But the names are arbitrary. Left elbow could be called flobbity boop bop a dibba dope and it would still be the same data and be treated in exactly the same way.

**[00:48:22]** Okay.

**[00:48:28]** Hooray. 3D data. We also know its shape. We also know this one shape. Okay, so actually, I guess we can do that.

**[00:48:37]** Okay. We can actually, we can also define the shape over here, which we will do. We'll say it's going to be number of cameras. Let's just. Yeah, just data blob.

**[00:48:50]** And we're number of cameras, number of frames. And then I'm just gonna.

---

### Chunk 6 [00:48:45 - 00:58:45]

**[00:48:45]** Cameras. Let's just. Yeah, just data blob. And we're. Number of cameras, number of frames.

**[00:48:59]** And I'm just call this kind of a tuple because if it was a dictionary, this would be the leaf. Or if it was a tree, this would be the leaf. And the leaf is an image. And an image will be resolution, Width by height. Oh, fuck me.

**[00:49:32]** Width by height by color. RGB. So a 640 by 480 image would be a 640 by 480 color image would be 640 by 480 by 3.

**[00:50:00]** And it's either width, height or height width. It's sort of. I can't tell if it depends or if I've just never internalized that it's always the same because I. In my mind it's like, this might be the other way. Just kind of like dyslexic vibes.

**[00:50:18]** But I'm pretty sure it changes and I'm pretty sure it's like, oh, are we in a row first coordinate system or a column first? It's like, I don't know, just plug it in. And when it's wrong, it's the other way.

**[00:50:34]** If you're ever in a situation where it's coming up, you're like, wait, is it. Which one is which? Just fucking guess. Grip it and rip it. Punch it.

**[00:50:41]** If it breaks, it's the other one. There's only two options. Easy. Okay.

**[00:50:52]** Okay. So now we are in the 3D trajectory data. And this shape is going to be. We're no longer number of cameras because we've lost track. We don't.

**[00:51:00]** The number of cameras is no longer relevant. It's. No, it's not in the data. So this is a. This is my.

**[00:51:06]** My good friend.

**[00:51:10]** I don't call it this anymore, but I'm going to actually. Well, skeleton frame marker. Call this xyz.

**[00:51:24]** Xyz. This is what I called it in grad school. And this is why it's like it was a beloved. That was a beloved. Oof.

**[00:51:45]** Ah, come on. Oh, don't do that. Actually, no, actually, don't do that. That is good. Okay.

**[00:51:54]** X. Yeah. So this is a beloved data type to me. And whenever I'm talking numpy arrays. This is from old game Diaz. Like underscores at the end tell you the dimensionality.

**[00:52:14]** So this is skeleton data. The first dimension is frame number. The second dimension is marker number. Usually corresponds to some other list of strings that tell you the names and then the order in the list is the Order in the array and then XYZ is the data. If this was a tree, that'd be the leaf.

**[00:52:45]** Eight minutes.

**[00:52:49]** Okay, so we got. Yeah. So number of frames, number of tracked points. This is also why I have such a hard time giving up. Like just getting the name marker out of my mouth is because of that era of my life.

**[00:53:11]** I like that. Eraser track points. And then now X, Y, Z, maybe that's how I'll denote that Is like the thing in the parentheses is. If it was a tree, that would be the leaf. Like that's the actual data.

**[00:53:34]** And it's just like if it's a key, if it's a. In a, in a matrix, in a tensor. I don't know why I did that. So, like that. But just like those are the same word.

**[00:53:44]** Yeah. They're not the same. But, but, but you.

**[00:53:50]** This is the. Like every spot is filled, but it's filled with this. And these are going to be, I don't know, floats.

**[00:54:00]** And these and ints are floats. It kind of depends. If it's pixels, then those are ints, because you can't be in a sub. If it's normalized screen coordinates, then it'll be floats.

**[00:54:19]** And these, at least at this part of our life, are going to be u int8, which is going to be unsigned integer, 8 bits, which is going to be 0 to 255. 3 channels, red, green, blue, 0 to 255. Every pixel of this is one of those. Unless it gets compressed and it gets turned to a byte string. But then, but that ain't an image, it's just the string.

**[00:54:52]** That's how we slurp it around. Okay, okay, focus. These are floats, though. And how do we know if it's good? So we know if it's good.

**[00:55:07]** Ooh, we know a couple things. If it's good. I'm running out of steam. We'll see.

**[00:55:15]** Yeah. Okay. Okay. Okay. We know if it's good because of smoothness.

**[00:55:25]** Smoothness. Smoothness. Because of. Now we get reprojection error.

**[00:55:43]** Reprojection error is if you, if you're tracking a point on a 2D image, so you're tracking this point and then you reconstruct it in 3D. If you then reproject that 3D point back onto the 2D image. If you trust the 2D track, then the distance between that 3D point and that 2D image is an error measure. Because if you trust the two dimensional data, then it can tell you if the 3D reconstruction was good. And then you can kind of bootstrap that into a way of like dropping some of the 2D data.

**[00:56:31]** Philip has a reprojection method in there which is like, computationally looks right, but it has no observables in it. So I don't trust it. And I never will until I, like, visually see something that convinces me. And. And I don't know what that thing is.

**[00:56:47]** And that's part of what we're doing here, because it's like, it makes sense, it probably works. It's like, I'm sorry, I've been around myself too much too often. I have seen how humans do things. And the part where you're like, trust me, it works, is the part where I stopped trusting you. It's not because I don't trust you.

**[00:57:07]** It's because I am also a human. And in fact, I am aware of what humans do. And what humans do is find up what else. 3D data. So we got the smoothness, we got the reprojection error, we got gaps, but that's not their fault.

**[00:57:27]** That's going to mean you're not going to get gaps here if you don't have gaps here, and you're not going to get gaps here if you don't have. If you have. We're going to get gaps here no matter what. So gaps aren't a problem because like, if you, like right now you have gaps. If you're tracking my legs, there's gaps because it's not present.

**[00:57:46]** So. And that's not a problem. That's just the nature of the situation.

**[00:57:51]** Okay, diagnostic data. Do I have any diagnostic data? Reprojection error might technically count as diagnostic data.

**[00:58:01]** I'll count it. No, it's the same as the, as the confidence here. It's both a goodness criteria and a diagnostic data type because again, it's a new data that lives in the computer and we can use it later for observables and blah, blah, blah. So I'm going to call reprojection error or anything else.

**[00:58:33]** I can't think of anything else. I guess also computation time, but I think I'm gonna take that off because that just, it's like, it's just not. It's not what we're talking about.

---

### Chunk 7 [00:58:33 - 01:08:25]

**[00:58:33]** I can't think of anything else, I guess also computation time, but I think I'm going to take that off because that just. It's like, it's just not. It's not what we're talking about right now. Like, there's always like they trying to get this thing to like go faster and run faster and blah, blah, blah. Oh, right.

**[00:58:50]** We're not playing real time games right now. Which means I don't care how long it took. Great. Love that. Love that.

**[00:59:03]** Okay, Okay. All right.

**[00:59:32]** B.

**[00:59:35]** Okay.

**[00:59:41]** Okay, fine. Reprojection error. ML reported confidence.

**[00:59:49]** Okay, now we get into the harder parts.

**[00:59:55]** God, it's gonna need to get split up. I can already tell because there's two parts. There's two parts, so.

**[01:00:04]** Okay, make the call.

**[01:00:12]** Oh, it's the wrong layer. Pipeline strip.

**[01:00:29]** That's. Actually, I'm noticing this as like a problem with the poly repro approach is once you make a choice, it's harder to change.

**[01:00:40]** Kestlavai. I guess it's not hard to change. You just gotta plop off and you just gotta polyp out a new repo. But then the names don't quite. Ugh.

**[01:00:51]** Maybe you can still live there.

**[01:00:55]** Who cares? I got an idea. Bah.

**[01:01:01]** It's representative of the tumultuous emotional state of the Skelly. There we go.

**[01:01:11]** Hey, We still on output? We are an output. Give me your color.

**[01:01:33]** Okay.

**[01:01:36]** Pipeline strip. Global output. We're on the wrong level. Who gives a. I don't care. All right, I'm.

**[01:01:48]** I'm gonna run out of some steam here. But that's okay. I'll just still bang it out. So. Okay, so.

**[01:01:56]** Oh, interesting.

**[01:02:04]** Okay, so reprojection error sort of feeds back into this potentially.

**[01:02:14]** There is no additional data from this part.

**[01:02:21]** This is all like. This is all the same. Like the data is the same here. This is the part that produces new data.

**[01:02:37]** Fascinating.

**[01:02:47]** Okay, so these are the things that you learn when you do this kind of shit. And that's why it's valuable. Boom.

**[01:02:57]** B, B. Oh, wait. No eraser is a brush in this world. Okay, so now we get a bunch of new shit over here. So we get. So we get like clean, cleaner 3D data.

**[01:03:22]** Raw 3D. That's ugly. Don't put that there.

**[01:03:29]** Zoom in.

**[01:03:34]** Raw.

**[01:03:40]** All right. Cleaner, clean as we can get it. Data. But it's the same.

**[01:03:51]** There's also this kind of part of it where I'm like. As I get more fluent with this tool, I will become better at doing this type of stuff in a Way that looks nicer. Like, even if I was like. If I had, like, some hotkeys or something where I could switch colors super easily, this would be a little bit. It would be cleaner if I had, like, some, like, way of jumping between colors that's like, jumps intelligently.

**[01:04:15]** Like, it's basically. What is it? Qualitative labels. Qualitative colors. Because I'm looking for maximum separation in the color space.

**[01:04:25]** Typically when I'm doing this. And I do clump them by color so I can. I could clump them by color family. So like. Like pinks and reds versus blues and greens and shit.

**[01:04:34]** But also, who cares? Nail it. And these are all the same. Actually, no, this step doesn't produce any new data, which is interesting.

**[01:04:50]** This step produces a bunch of new data you get. Because this part you start getting.

**[01:05:09]** Who was it? R. No, it wasn't a guy. I. There's no. What about you?

**[01:05:16]** What's your name? What's your deal? What's your name, friend?

**[01:05:23]** You know, you don't have.

**[01:05:28]** Oh, Similar color, contiguous section, bezier curve. Okay, we're just gonna do this for now, but we'll come back.

**[01:05:42]** Oh, it doesn't actually matter. You can chop it up. It's fine. I'll just get a little. Ugly bits.

**[01:05:45]** But we're already ugly. We have already passed the point of ugly.

**[01:06:03]** Yeah, we've already passed the point of ugly. So we can do whatever we want.

**[01:06:12]** B.

**[01:06:19]** God damn it.

**[01:06:23]** What was it? R. What is r? What does r stand for? X output. V. Nailed it.

**[01:06:34]** T. Great.

**[01:06:40]** Now we're going to get in like this. We're going to be doing something else. It's. It's. We're.

**[01:06:47]** We're losing the plot. But we're doing it semi intentionally. Okay, so rigid body constraints. That lets us get joint angles pretty much.

**[01:07:00]** Oh, wait, no. This is in the wrong order. This is in the wrong. Ooh, Ooh. Okay, Lasso.

**[01:07:10]** I can probably add.

**[01:07:14]** What's it called?

**[01:07:21]** Oh, no. Okay, t. Hot keys and stuff.

**[01:07:36]** Okay, so first you calculate virtual markers, and that lets you.

**[01:07:45]** Virtual markers let you. Oh, we're doing this Color.

**[01:07:54]** Oh, can I change your color? Is this how you change color? No. Wait, is it? Yeah, this won't work.

**[01:08:07]** I probably can, but I don't care. Okay. B. So virtual markers. Sure, why not?

**[01:08:12]** Virtual markers let you calculate.

**[01:08:20]** Body segments.

---

### Chunk 8 [01:08:20 - 01:18:15]

**[01:08:20]** Body segments.

**[01:08:41]** Body segments.

**[01:08:46]** And then not technically, but just like you need all the markers to be able to calculate all the segments. So like, you know, so it's a necessary step to get body segments. And then once you have body segments. Oh, yeah. Oh, yeah, yeah, yeah.

**[01:09:10]** Once you have body segments. Oh, that's a new data type. Body segments is a new. It's like a new. It's a new thing.

**[01:09:21]** I got you. Okay, so we're. We're definitely losing the plot here. Or we're. We're kind of losing the.

**[01:09:29]** Well, we're kind of. We're getting. I guess we're getting into the part. Right. This is actually like.

**[01:09:33]** This feels more like work because it's like I don't have these numbers up. Like everything before this, I'm like, there's no questions here. I know this stuff backwards and forwards, but this is like. Oh, wait, actually, like I'm getting some of those moments here. So virtual markers is a calculation.

**[01:09:53]** And then. And yeah, so you calculate the. And then rigid bodies is like.

**[01:10:02]** We're going to call it. It's a computational step. We'll call it calc because it's a calculation. This is not. There's no variability here.

**[01:10:12]** It will always come out. Actually, there's no variability here either. These are pure computations. The same inputs will always. There's no inference.

**[01:10:20]** So it's deterministic. Is the term.

**[01:10:25]** Rigid body constraints.

**[01:10:39]** Now, once you've applied the rigid body constraints, now you have a skeleton, or at least the kind of skeleton that I would want to take to dinner. Oh, that's how you should probably do that.

**[01:10:55]** I should be doing this in pink versus completeness. And so now you have. Now you have an actual skeleton. Like a connect the dots. You have one of these.

**[01:11:11]** I'm gonna call it skeleton. This is what we've been working for, guys. This is what we came for. Skeleton.

**[01:11:22]** You could have gotten it before, but it would have been bad. And actually you couldn't have gotten one of these from the previous data because there was variability in the segment lengths. So this guy doesn't have variability in the segment links. This guy does, but let's pretend he doesn't is kind of what we're saying here. This is the rigid body assumption.

**[01:11:43]** It's like, like, listen, this task is hard enough. Don't come fucking talk to me about your soft tissue bullshit. Like, like. We can get to that later. For now, let's just be one of these to make life easier for ourselves.

**[01:11:56]** Okay? Okay, sweetie. Hypothetical.

**[01:12:03]** Okay. Once we have the skeleton. Then we can do a lot of shit. And then we can calculate.

**[01:12:14]** Segment, center of mass. And then we get full body, center of mass, skeleton. Segment, full body, center of mass, skeleton. What else? Wait, shit, where were we here?

**[01:12:39]** Lost the plot. Joint angles.

**[01:12:44]** We can also get joint angles, And those are outputs for many folks.

**[01:12:59]** Oh, and we also get key point.

**[01:13:12]** I'm going to stick with the naming I've been using.

**[01:13:24]** Keep saying tracked point tract. No, because that's kind of the wrong language.

**[01:13:38]** Who gives a shit? Tracked point.

**[01:13:53]** Trajectories. So this is like. Like, what is the linear trajectory of my wrist in space? Like my wrist center in space versus what is the angle of my wrist? Those are different things.

**[01:14:09]** Both of which, like all of this, you could have calculated from the previous stuff, but you shouldn't.

**[01:14:19]** And I think we're just going to say that unequivocally, that all of our data of analysis should be derived from this rigid body skeleton.

**[01:14:30]** And I shall name you such.

**[01:14:46]** Going to make you a fancy color too, because you're so special. You're so special to me.

**[01:14:55]** Rigid body skeleton.

**[01:15:08]** Look at that. I use fucking yellow, y'. All. Do you see how important this is? Do you understand the fucking perceptual place of yellow in this color space?

**[01:15:23]** It's like a form of assault. Look at that. Jesus. Oh, my God. What are you.

**[01:15:30]** Oh, my. Jesus Christ. So aggressive. Oh, okay. And then.

**[01:15:37]** And then we do some blender shit.

**[01:15:44]** And then you do blender shit.

**[01:15:52]** And then that produces your FBXS and your whatever the hell else. Oh, actually, no, this is worth doing FBX and blue blend.

**[01:16:06]** Blend and your et ceteras and your whatnot. And then this is going to come back in the form of I don't know what fucking file format I'm going to use. Let's just say CSV, I think, is going to be the default output here. Because it's like, numpy arrays don't need to be saved. It's a proprietary data format file, a numpy array.

**[01:16:33]** Just load a CSV and convert it into a numpy array. Just do it once. I think I'm going to move away from saving numpy arrays. I think they don't pull their weight in terms of the complexity there. And anyone that's like, oh, man, I prefer numpy arrays.

**[01:16:50]** It's like, well, that's just because of your weird background. So just make a CSV to NumPy array converter and then live your happy life, you hypothetical human, you. And then the observables are just the. You can plot out of that.

**[01:17:12]** Oh, deary me.

**[01:17:19]** Where did you. Where did you get up here from?

**[01:17:25]** Some. Some moment of weakness, perhaps?

**[01:17:36]** I guess. That's not how that works, is it?

**[01:17:40]** There was a thing you could do. Someone showed me how to do it. It's like you. It's like Control R. No, not Control R. Control Shift R. Control alt R. Control alt R. There's a way to, like, click on it and it tells you what layer it's on.

**[01:18:06]** It's in the background.

**[01:18:10]** Oh dear.

---

### Chunk 9 [01:18:01 - 01:25:27]

**[01:18:01]** To like, click on it and it tells you what layer it's on.

**[01:18:06]** It's in the background.

**[01:18:10]** Oh, dear, dear, dear.

**[01:18:18]** E said this guy.

**[01:18:25]** Understand, Anders, Why also. Why also that where, where for where, where and whence, my dude? Where from and whence?

**[01:18:45]** Well, now I'm just confused.

**[01:18:50]** Are you immutable? Do you live forever? Can you be this layer? It's not though. See, it's right there.

**[01:19:01]** Okay, I have decided it doesn't matter and I don't care, because remember, we already. We are living in ugly land already, which gives us a lot of power.

**[01:19:14]** Can I select multiple layers at once? I don't know. I am. We're over an hour now. Yeah, that makes sense.

**[01:19:23]** Okay, I've said I don't care. No, I do. I do, though. Shoot. Wait, what just happened?

**[01:19:32]** Where did the.

**[01:19:42]** Okay, global outline Control R grab you? No, grab you T. You go down here.

**[01:19:57]** All the way down there. Thank you. Control R, grab all of you. Everybody else, and you hit T. Go up. Great.

**[01:20:09]** Then I grab the pipeline strip and you already know. Thank you. You go up and then the output strip. Are we doing this? Control T. No.

**[01:20:23]** Control Shift T. Nope. Control Alt T. What was it? It was this one. I think it's just Ctrl T. Or it's just T. Control T. Control T. Yeah, who gives a. Okay, Control R, Grab the whole guy.

**[01:20:47]** Hit T. Move it up. Why are you not coming along for the ride that I put you somewhere else? That's.

**[01:20:59]** Okay.

**[01:21:02]** You're on the. Oh, we duplicated the pipeline strip some at some point. Why did we do that?

**[01:21:11]** We didn't duplicate it. We just. I don't know. Who gives a shit? Okay, Control T. Yeah, R. T, grab you.

**[01:21:21]** Great.

**[01:21:24]** I go back to the global outline strip. We grab Control R, our observable friend. We hit T, we move them up, we put them there, and then.

**[01:21:43]** Then. And then we're kind of emotionally. I'm done with this. So control shift A. And then we take our.

**[01:21:57]** This yellow. But we don't. We have already. We saved this. So we're going to make it.

**[01:22:04]** Let's make it like an orangeish. Because it is the work that needs to be done.

**[01:22:13]** The stuff you can plot that will tell you if it's working.

**[01:22:35]** Any fucking questions?

**[01:22:40]** Oh, God. Which one? What do I plot? Well, convince me that it's working. I don't believe you.

**[01:22:47]** Convince me. Look at the code. No, because I don't really care how you did it. I just want to know if it worked. We can talk about how you did it later, but just show me if it worked.

**[01:23:02]** How can I show you if it worked? Well, assume it didn't work. Convince yourself. Show it to me. Was I convinced?

**[01:23:14]** I have been burned more times than you have tried, so I will be harder to convince.

**[01:23:24]** Cripes, I am baffled by this. I am baffled. Where. Where could you. Where do you live?

**[01:23:41]** Who are you? Where did you come from? How did you get there? Where's your house?

**[01:23:52]** Oh, dear.

**[01:23:57]** All right. Save hour and a half. Pretty good. Pretty happy with it. I'm gonna require people to watch this because this is the shit I can't be bothered to explain over and over again.

**[01:24:13]** It's too hard to think about. And it's like, this is the part where I'm going to require some mental effort from the people who want to work on this project. It's like. And if it doesn't make sense to you, like, then that's on you. Like, I will explain it to you as much as I can.

**[01:24:28]** As much as I. As much as I can. But. But, like, I just recorded an hour and a half video on a Saturday morning to explain it to you. So if you're like, I don't understand it.

**[01:24:35]** It's like, I have given. Have you. Have you exhausted the available media?

**[01:24:45]** Is the first question. Great. Saved. We're in. There's like, I start.

**[01:24:55]** And then in the first hour, we're good. And then in the second hour, we get into, like, salt zone. And then in the third hour, we get into rage zone. And this is. This is where I start yelling at the screen.

**[01:25:12]** Is this millennial Fox News?

**[01:25:17]** Is that us? Is that what's happening?

**[01:25:26]** Okay, we're done. Thank you. Bye.

---
