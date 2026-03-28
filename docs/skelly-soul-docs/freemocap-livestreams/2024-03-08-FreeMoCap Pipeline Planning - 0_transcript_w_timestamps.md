# Transcript: 2024-03-08-FreeMoCap Pipeline Planning - 0

## Source Information

- **Source Type:** Local File
- **File Path:** `C:\Users\jonma\syncthing-folders\jon-alienware-pc-synology-nas-sync\videos\video_eater_downloads\playlists\[OLD] FreeMoCap Development\2024-03-08-FreeMoCap Pipeline Planning - 0\2024-03-08-FreeMoCap Pipeline Planning - 0.mp4`

---

**Total Duration:** 01:02:38

---

## Full Transcript

### Chunk 1 [00:00:01 - 00:10:00]

**[00:00:01]** Okay, now let's do this thing I said in the last recording that didn't work because the mic didn't work. And then you will never know about. Will just be confusing, which is we're gonna do this.

**[00:00:17]** So I need to.

**[00:00:25]** Yeah, so, so we're working on the cat mo cap and we, this, we got to step away from it for a bit because this is kind of. We just, this is how it works. But this is the main sort of like, hey, this is sort of the main output, the main artifact from that particular exploration. And basically it is a pipeline that will work for this project and we will be exploring that at a later date. And now why am I doing that?

**[00:01:06]** I also, I want to start doing. I need to start making like that kind of a planning. I want to clean that up a bit and sort of use it as a plan. Yeah, like basically making like free mocap global planes. Because this is basically where is it?

**[00:01:32]** Like this is basically like the free mocap pipeline. And there's been a couple iterations of like a diagram like this. And every time I write it out I get sort of a better thought of it. This is specifically for cats, but. But it's like cameras measure some observable thing in the world, generate raw data, synchronize videos, I guess pre process.

**[00:01:51]** And this is all 2D tracking here and then 3D reconstruction which produces like raw 3D data, post processing state agnostic data informed. And then I like this distinction that came out where there's sort of this like distinction between studying things from a holistic point of view by looking at the full body center of mass dynamics and this kind of reductionist model which is the standard model, which is like so standard that is often not even named. But it is like a reductionist approach to research where you, you're trying to get it down to like the, the smallest possible, most precise unit that you can measure, which I think in this case would be like estimates of muscle activity from the movement of the skeleton. And these two things obviously want to be best of friends because the holistic model tells you like, oh, this is the full body dynamics. This is the, the human as a.

**[00:02:49]** Or the creature I guess as like a, as a physics object. And then this, the reductionist model is more like. This is the precise control signal. This is like human as a, like robot. Human as meat robot.

**[00:03:10]** Different guys. Different guys, different tasks, complementary. See how they're, they're in love with each other. Okay. And I think that the move shall be.

**[00:03:22]** I'm trying to Remember where I put this? This is like, old. This. I have it. This is the lab server check.

**[00:03:30]** Yeah, this is the guy.

**[00:03:39]** I'm just gonna.

**[00:03:43]** I'm just gonna be. I'm just gonna be a bit confusing, guys. I don't. It's fine. Don't worry about it.

**[00:03:51]** You'll be okay. You'll figure.

**[00:03:56]** Great. So this is kind of what I want to work on, Like cleaning up. It's not actually accurate, so. Not accurate.

**[00:04:11]** P.S. it's an old diagram. Not accurate.

**[00:04:21]** Not accurate.

**[00:04:27]** Not necessarily accurate to any present or planned. There we go.

**[00:04:43]** But, yeah, okay.

**[00:04:48]** But, yeah, but this is. Okay, so actually, can I. Oh, I can, can't I? Let's see. And then I.

**[00:04:58]** Can I copy you? Can I paste? You paste. Hey, paste, huh?

**[00:05:05]** Download. Yeah.

**[00:05:22]** Great. So I've learned these lessons. Okay.

**[00:05:33]** Control t. See, This is one of those things where it's like, I drew this out by hand back before I knew how to use this fancy guy. And I may go back to it. I don't know. It's kind of nice to have the constraints.

**[00:05:57]** It's kind of accurate.

**[00:06:01]** It's accurate. Ish.

**[00:06:05]** Take a look. Let's just.

**[00:06:12]** Yeah, okay.

**[00:06:20]** I think.

**[00:06:23]** Okay, so what do we have here? I guess that's one question. We have a. Okay, first of all, make a new layout. Sanki.

**[00:06:34]** Oh, and I hit B, E. And I wish I could make you darker back there. Can I do that? Who cares? Okay, so we've got a.

**[00:06:49]** This is like a process diagram. Is that what you would call that? Flowchart.

**[00:07:01]** Flowchart. I'm like, doing archaeology on my own notes. This is also keeping track of, like, oh, this is a one frame. This is like the, you know, one frame pipeline, I guess. One frame, right?

**[00:07:19]** So this is like the. The fate of a given measurement.

**[00:07:28]** As it goes through the process into its, like, final form.

**[00:07:35]** Which I am also, because I'm decided we're just going to hit. Hit these philosophy terms harder because why not? These are the desiderata. Desiderata. It is the thing which is desired.

**[00:07:49]** Why'd you come here, friend? What was your goal? Well, I wanted to get these skeletons, you see. It's like, well, then there you go. And then you got this measurement right.

**[00:07:57]** This is all the empirical shit that. This is all the information that you. That you could. That you were able to slurp out of the environment.

**[00:08:07]** And then these are all the computations.

**[00:08:11]** And either they are truth preserving, in which case they are science, or they are not truth preserving. They are aesthetically bound. Then they are art. And of course these two things are friends can be friends. And it's a balance.

**[00:08:28]** It's a spectrum. We love it as a group. Okay.

**[00:08:35]** Doo doo doo doo down here.

**[00:08:41]** This is like a. So and then we. We group it by sort of repo. Apologies for the color but not that hard. So that was some work that we did, I guess.

**[00:09:00]** Sure. And then this. Ugh. Apologies for that color. This is the same.

**[00:09:07]** These are. These are corresponding. Okay. So yes, we have 1, 2, 3. So you have 2D tracking, 3D reconstruction, export data.

**[00:09:17]** I probably would put. I would like actually separate like cleanup from the reconstruction. Then we have the export data which is like producing the actual outcome. Which one came first? Probably these things came together.

**[00:09:33]** Okay, cool. So that, that helps me shock if you may.

**[00:09:44]** May or may not understand.

**[00:09:47]** Now.

**[00:09:58]** When did I write this? This was.

---

### Chunk 2 [00:09:45 - 00:19:40]

**[00:09:45]** Understand?

**[00:09:47]** Now, When did I write this? This was.

**[00:10:04]** That was in November. So a couple months.

**[00:10:14]** Cool. And let's see here. So let's take all you. I don't need any of you anymore. Now let's sketch out what we're actually doing here.

**[00:10:27]** I don't need you to be.

**[00:10:42]** Oh yeah, sure. Why not?

**[00:10:46]** Cool. That's fun.

**[00:10:50]** Now I'm gonna paint you in. Right.

**[00:10:55]** Bye. Wait, I don't know if that's what we're supposed to be doing. Let's just. Can we get rid of you and make a new guy?

**[00:11:10]** Okay, I changed my mind. Lock them and. Okay, so what's the goal? Right now I want to.

**[00:11:27]** Gonna be black anyway.

**[00:11:34]** Okay. All right, so let's redraw that top level pipeline.

**[00:11:47]** Okay. But actually. So I like this distinction of like here is. So time is going this way.

**[00:11:59]** And this is an idealized like single frame duration.

**[00:12:15]** So for a 30fps camera, this is going to be 33 milliseconds, which. Yeah. Okay, now how do I do this part? Do I grab them.

**[00:12:40]** And then that guy. Yeah. Nice.

**[00:12:47]** Okay, and so this is. If we want to be able to have real time, which we do well, then we need to process everything within a single frame. We don't actually care if we have real time because we could always just drop a. Drop the frame rate by half and have double the time. But this is just like it's a thought experiment.

**[00:13:14]** So that means that in that time you have to go from having. What color am I doing? Pink. Sure.

**[00:13:21]** The measurement.

**[00:13:29]** Look, you've done it. You've measured the world. There's a person. Look at them go. And there's a camera, and there's another camera, and there's another camera.

**[00:13:50]** And there's no water, but there will be.

**[00:13:55]** I already drank it off screen. Don't worry. Okay. And blue. Sure.

**[00:14:05]** Okay, so here we go. So pink is the world actually. Yes. That's not true.

**[00:14:15]** And now better to do that. Yes. Kind of yellow like the sun. Because you see, what happened was this. Mr. Sun hit you with a light ball and that hit the sensor of the camera.

**[00:14:35]** And then as a result, you were born.

**[00:15:00]** Great. Love it. Happy that you made it.

**[00:15:08]** And then this part right here, this is the magic part. This is the part. This is where the magic happens, as they say. This is the moment of transduction.

**[00:15:28]** This is where the philosophy happens.

**[00:15:43]** Transduction.

**[00:15:50]** And that's the part where environmental energy is transduced into electrical energy. And there is something magical. What is the relationship? What is. How is.

**[00:16:04]** What is there's now an electrical signal. And we're going to analyze that electrical signal, and we think it's going to tell us something about your brain. What the shit? How is that? It's something in the pattern.

**[00:16:18]** It's something in the shared statistics. It's something in the mathematics. It's something in the something. I don't know, but there's a. Like, it's a pattern of photons that turned into a pattern of electrical pulses.

**[00:16:28]** And I'm gonna look at that and I'm gonna say, your brain did a.

**[00:16:36]** Your spine said squish. I don't know. So. And we look at that. We have a little existential crisis as a treat, and then we move on.

**[00:16:44]** Okay.

**[00:16:50]** And then we. From. Okay, so now everything after this is kind of just. It's just. Just shuffling numbers around.

**[00:17:12]** I don't know. Oh, oh, right. No, we're doing the thing.

**[00:17:17]** I guess we're gonna.

**[00:17:20]** No, yeah, we're doing the thing. Let's do the thing. Let's be. Let's be efficient without times. Okay.

**[00:17:33]** All right.

**[00:17:36]** This is. Well, this is your PC, I guess.

**[00:17:45]** This is usb.

**[00:17:50]** That's not really how your computer works, is it?

**[00:18:24]** That's your computer. And then that turns into.

**[00:18:32]** We're going to measure the signal. Signal is going to be green. Nope.

**[00:18:56]** Now it's electricity.

**[00:19:02]** And then that will go into some other color. Let's go around the circle. That seems like a nice way to organize that. And then it'll be. This is.

**[00:19:10]** So now this is Skelly Cam. Well, it's all free mocap, but let's. The whole picture says free mocap, so you don't need to specify that.

**[00:19:21]** Skellycam. Skellycam is a sub repository of the FreeMap project. You see, it is the part of the software that does all the camera shit. And what it does is it does a bunch of loop de doos so that it will produce.

**[00:19:39]** I don't like that.

---

### Chunk 3 [00:19:31 - 00:29:30]

**[00:19:31]** And what it does is it does a bunch of loop dee doos so that it will produce.

**[00:19:39]** I don't like that.

**[00:19:47]** Oh, we're trying to make an artifact that stands on its own. So I should write down the things that I said.

**[00:19:55]** Skellycamp. Ugh. But writing takes so long, camera stuff. Because free mocap is for the children. And then it produces.

**[00:20:14]** A new data. And we had a way of specifying this on the previous thing, right? We were trying to say, what's this? Triangle calibration. So there's a calibration step.

**[00:20:23]** That's whatever. Da, da, da, da.

**[00:20:28]** I'm gonna choose one right now, which is a. Let's choose some iconography, shall we? Give ourselves a nice neutral color, because we're not picking sides. Box is a sub. Repo, Subrepo, Sub repo.

**[00:20:55]** And a triangle is a data. Data type.

**[00:21:08]** Oh, it had. I had individual. I had inner parts. Ugh.

**[00:21:17]** I think let's do the high level first and then we'll zoom in. Right? Yeah. Data.

**[00:21:27]** Yeah, great. The circles will be like snake processing steps or something like that. Okay. Control, clip. Click, click.

**[00:21:37]** Yeah, sure. And now you produce a new data type, which is a triangle named 2D data.

**[00:21:58]** And you, my dear friend, are pixel coordinates on an image plane.

**[00:22:22]** And what that looks like.

**[00:22:28]** Is the data type is going to be held in like NPY and NPYcsv. I already. Okay, where's the old version of this? Because I have.

**[00:22:50]** I've drawn this out before in a more complete way. Where was that, though? Jesus. That was. Oh, I know what that is.

**[00:23:01]** That was for. That was for the meeting with the Marmoset people. They didn't listen to me and so now their project doesn't work. Whoops.

**[00:23:17]** I don't know what they're. I. No, I mean, there's a lot going on there. But they did ask for my advice, and then I told them how to do it, and then they didn't do it that way. And then it didn't work.

**[00:23:25]** And then they got mad at me.

**[00:23:32]** Like, I don't know, man. Like, if only someone would have told you not to put your cameras in that place before you hard mounted them in. Like, where was it? Oh, Jesus.

**[00:23:53]** I Dropbox you.

**[00:24:00]** I need to get Dropbox out of my life entirely out of my life.

**[00:24:07]** Like, that is. Dropbox is such a perfect example of software rot. Because it used to be very.

**[00:24:22]** It was just such a clean, perfect little program. It did exactly what it needed to do. Fuck you.

**[00:24:30]** And then they just, like, it just rotted. Like it just stopped being good. They kept adding a bunch of stuff and it's like none of it wasn't what anyone wanted them to. What are we doing here? Okay, I'm just looking.

**[00:24:46]** This is because I've used Dropbox for a very long time. I was like, so I have a lot of stuff in it and it's backed up in various places, but like, it's just kind of like annoying to access. What the shit am I doing? Marmies.

**[00:25:02]** I think I want this one.

**[00:25:09]** Yeah, different era.

**[00:25:17]** Okay.

**[00:25:33]** Yeah, same basic. This is before I knew how to do this.

**[00:25:39]** And then this is back before I knew that. Camera projection. Yeah, yeah, yeah. It's like, okay, it's still accurate, but it's not. Not in a useful way.

**[00:25:53]** Okay, nevermind. This is back. This is when I was doing. This is. We're still doing this.

**[00:25:59]** It's just kind of like, you know, I realized that a lot of academia, academic research gets like, I could have, I already did this. I could have done this. I could have done this on my own a thousand times over. But there is such a big difference between, hey, I can do something I did at once and hey, I made something that other people can also do this thing. And I just kind of like, I know I could do that part.

**[00:26:30]** Like, I know I could get some cat mo cap. I could have gotten that by, you know, Monday. But then it wouldn't have been generative. It would have been productive, but it wouldn't have been generative. And I think that's an important distinction.

**[00:26:42]** Okay, so we're going to wind up doing this. So npy, those are the files.

**[00:26:52]** The shape will be. Oh, this part I did do correctly, I think. Oh my God, it's so bright though.

**[00:27:04]** So bright.

**[00:27:09]** Yeah, cool, cool, cool. So I already knew this. So it's going to be. Shape is going to be number, number of cameras by number of frames.

**[00:27:34]** By number of.

**[00:27:39]** What are we calling these fucking things now? I guess tracked points. I always want to say markers, but they're not markers. The whole point.

**[00:27:50]** People call them key points. I think I don't like that either. Tracked points.

**[00:27:59]** And then by an X. Oh wait, no. Doink, doink. Pixel X.

**[00:28:11]** No, not necessarily. Because it's not going to necessarily be pixels X Y and that could be pixel X by pixel Y or it could be norm normalized screen position X, Y. The difference between those is if this is your screen, I should be using colors for the these it could be, let's say. So zero, zero is here. Give me a color.

**[00:29:00]** Ugly. Hideous. I apologize to the world.

**[00:29:09]** Okay, fine. Doink, doink, doink.

**[00:29:16]** Not that color. It's right next to it gotta have a different color. Everywhere has to be a different color. Sure, the blue doesn't show up super well, but I don't care. I'm sick of thinking about other.

---

### Chunk 4 [00:29:16 - 00:39:11]

**[00:29:16]** Not that color. It's right next to it. Gotta have a different color. Everywhere has to be a different color. Sure.

**[00:29:26]** The blue doesn't show up super well, but I don't care. I'm sick of thinking about other people for the time being. So it could be going from here to here. That could be.

**[00:29:40]** So this is going to be positive X. And this is going to be the kind of fucky part. This is positive Y. Like it points down. So like zero at Y is up is up here.

**[00:29:59]** And then like if it's a 640 by 480 image, then this is 480 down here. So this is either going to be zero to 480 or zero someone else clean this up. 0.10. And then same over here, it's going to be zero to. Was this 640?

**[00:30:23]** Assuming at 640, which is, I don't know, just like a default or 0 to 1. This is a pixel. This is the normalized screen coordinates. And so then if you want to get a given point.

**[00:30:45]** Rgb, rgb, rgb. Red, green, blue. Yeah, sure. Apologies to the colorblind. Da da da da da.

**[00:31:00]** Yeah, so there you go. That's your thing. X, Y. And then you, if you want, if it normalizes you multiply it by the resolution to get the pixels. Anyways, who cares?

**[00:31:10]** That's the main idea. Oh wait, no, let's draw this out because we're still kind of doing this.

**[00:31:17]** I forgot where we were.

**[00:31:21]** Oh, actually, can we do.

**[00:31:25]** Okay, so we are saving this.

**[00:31:30]** We're using sync thing now, which is like. Are we doing this? It's where I initially went. So that's what we're going to do it. Okay.

**[00:31:39]** New folder. It's like a gut check thing. Like if I go look for something and I look for something, like the first place I look, if it's not there, that's where it should be. Wherever else it is, we'll move it to that location. So going to do this.

**[00:31:53]** Creta.

**[00:31:57]** Data. I don't know. Sketchers. Yeah, go get. And we're going to go in there.

**[00:32:15]** Date. No, we know what we're doing here. Freemo Cap Pipeline 2024.

**[00:32:34]** Yeah, right. We saved that. And what we really want to do is set up some kind of a autosave, which I would assume we can do. I need to stop covering my mouth when I'm talking because I got to imagine it's not great for the audio, but I never watch these after I record them, so what the hell do I know?

**[00:33:06]** Configure Krita autosave. What is your autosave?

**[00:33:16]** Auto save interval. Is that a thing?

**[00:33:23]** Auto save interval. Every seven minutes. Unnamed. Unnamed Autosave files are hidden by default.

**[00:33:32]** Every.

**[00:33:35]** Every.

**[00:33:44]** That seems fine. Okay. And same as the thing. Backup file. Suffix.

**[00:33:49]** Number of backup files kept. No, no, no.

**[00:34:02]** Yeah, it's. People always give me shit. It's like, why do you want voice memos? You can just type it out. It's like, no, you can't.

**[00:34:08]** It's not the same compress.

**[00:34:19]** No. We invented. We've been speaking for way longer than we've been typing.

**[00:34:29]** Okay, so we got that. Save that. Great. Good job. And now this is this part.

**[00:34:34]** We'll see.

**[00:34:41]** We are going to add a new source. It's going to be.

**[00:34:52]** You fucking.

**[00:34:55]** I wanted to autosave a PNG and then put it up here. But I just realized, like, the autosave that it's doing is saving a KRA file, which is not the same thing. And I have given up. Great. Cool.

**[00:35:11]** Sorry, guys. You get what I give you, presumably. Actually, whatever decision I'm making is going to be available elsewise. So you can watch it. You can see the full thing while I'm doing it.

**[00:35:21]** Presumably. I don't know. We'll see.

**[00:35:28]** Boop. Green man. Look. Ugly. Awful.

**[00:35:34]** Hate it. Let's give you some. We're ready for some. Ready for some pink in here. We got the red, though.

**[00:35:40]** Okay. Green, red, blue. We're already. Okay, so we got this hard blue, this hard red, this hard green. I guess we're up here.

**[00:35:45]** Here. Sure.

**[00:35:51]** That's a hand. What's off? I can't. I can't. Okay.

**[00:35:58]** One, two, three.

**[00:36:09]** Perfect.

**[00:36:16]** That's better.

**[00:36:24]** That's perfect. That's a perfect person. Okay, now we zoom out. Have a metaphor. Okay, so.

**[00:36:35]** Yeah. Cool. And so that's. That's Skelly Cam. And after Skelly Cam, we get.

**[00:36:49]** Skelly Tracker. Who's new. New to the party. Okay, so wait, are we still in this color? We are.

**[00:36:58]** Great. This whole guy is Skelly Tracker. No, we don't need to do that. Okay, we'll just do that later.

**[00:37:08]** ZV produces 2D data. Oh, that's what I need to do.

**[00:37:18]** I don't care. Great.

**[00:37:25]** I'm going to mark this data.

**[00:37:31]** Because this is an important moment. 2D.

**[00:37:38]** Oh, wait. No. Fuck. I did this wrong. I'm wrong.

**[00:37:43]** Yeah. Okay, great. See, this is why we do this. Because we got to clarify our brains.

**[00:37:50]** Let's grab.

**[00:37:54]** I think we can do that.

**[00:38:00]** I got an idea. Who cares? And then we say, this guy, This guy. And we grab all of this because you see the mistake, what we've done. Horribly, unforgivable mistake.

**[00:38:23]** What we've done is we have ascribed the wrong data to this part of the pipeline. The 2D data doesn't come until later. Skellycam, you idiot, produces in synchronized videos.

**[00:38:50]** B, B, B, B, B. Oh, did you. Have you done a thing? Have you done some weird.

**[00:39:09]** Why? Why, though?

---

### Chunk 5 [00:39:00 - 00:49:00]

**[00:39:00]** Have you done a thing? Have you done some weird.

**[00:39:09]** Why? Why though? But why though?

**[00:39:16]** Oh, because of this. Okay, so I got you, buddy.

**[00:39:29]** See? Perfect.

**[00:39:32]** Okay, so you, Skelly cam, my darling friend, have you produce in your own color.

**[00:39:58]** Whatever you produce in synchronized videos.

**[00:40:11]** So right now, Hmm. We're drawing this. We're. Okay, let's keep on the pattern. We're doing the.

**[00:40:26]** The shtick of real time. So this isn't videos. This is multi frame packet.

**[00:40:35]** You don't get to make the in synchronized videos joke. It's okay.

**[00:40:41]** Jesus.

**[00:40:47]** So what you don't produce is that what you do produce? I don't really like this triangle thing. It's awkward to write a triangle, but it's fine.

**[00:40:58]** Synced multiframe.

**[00:41:10]** Frame payload.

**[00:41:18]** Images.

**[00:41:21]** All right, now I can do.

**[00:41:29]** N. So that's going to be number of cameras.

**[00:41:38]** Images that are res width by height by color. Eg for a 640x480 RGB image, going to be 640 by 480 by 3 by N by number of cameras.

**[00:42:19]** Great.

**[00:42:22]** Jeez. It's like sometimes it was just like I started trying to explain things and it was like, ah, Jesus. So complicated. And I'm like, no, no, no, trust me. Every One of these 10,000 pieces is simple is the thing.

**[00:42:37]** And I promise you that's true. It's just that there are. There are a lot of them actually. Don't hate that. Okay, can I rotate you?

**[00:42:49]** Yes, I can. Can I scale you? Yes, I can. Whoa.

**[00:42:56]** Rot items. Squish kids. There you go. Look at you. Perfect.

**[00:43:06]** Now no one can ever have any questions about this because it's so clear.

**[00:43:14]** Oh, deary me. It's like, right, so like I'm supposed to be putting all this energy into like publishing papers and like that. Stupid. I'm gonna put this in an 8 page PDF that some old dinosaurs can read and tell me that they did it in the 80s. The.

**[00:43:35]** You did. If you did, I wouldn't have to do this.

**[00:43:43]** No respect. The disrespect is part of the product.

**[00:43:48]** Okay.

**[00:43:51]** Okay, cool. So this is Skelly Cam. Good job, Skelly Cam.

**[00:44:09]** Skelly cam.

**[00:44:15]** Oh, dear God in heaven. Great.

**[00:44:22]** We're running out of paper, but we're also running out of steam, so that's good. Okay. The lesson I'm trying to learn right now is that I should probably zoom the fuck out and say that now in a more different color.

**[00:44:40]** We're going around the line. We're going to this kind of. Let's go More of this Hard, hard. Blue.

**[00:44:51]** We already had got blue. It's fine. Who cares? Make it a little bigger.

**[00:44:58]** Big L. And this is gonna be Skelly tracker.

**[00:45:09]** And you, dear friendo, have tracking shit. So this is where you've got your. Currently, we mostly use media pipe.

**[00:45:23]** Easy, fast, not particularly robust. We've also got your open poses.

**[00:45:32]** And we've recently been playing with your deep lab cuts.

**[00:45:38]** And it does 2D tracking of skeleton in image. And it's like. Yeah, it's like. Yeah.

**[00:45:58]** And I know there's a bunch of stuff that does 3D from 2D. That ain't us. Just. We can talk about it later. Like, it's fine.

**[00:46:06]** But it's. We don't respect their epistemology, bless them, Their philosophical underpinnings. We find a bit. Susan. We believe that some of their computations may not be proof, may not be truth preserving, pejorative.

**[00:46:40]** Yeah, I said it. I. I said it. Okay? And I'm sorry that these want to use inference to make up for the fact that they don't understand how to do projective geometry. Listen, who among us could not sympathize?

**[00:47:04]** But not here in this house. In this house, we prefer computation to inference a thousand days of the week. Okay? So we got this data, New data, Data, images, data. Ah, that shit.

**[00:47:39]** Oh, that was a guide data. 2D data. Okay. All right. Can we, can we do this?

**[00:47:50]** Can we. Can we make the canvas bigger? Is that a guy? Is that a thing? Or we just make the whole everything smaller?

**[00:47:55]** That's what we do. Is that right? Everything. Is that the whole guy? Yeah, sure.

**[00:47:59]** Great. Love it. Look at me. And I got more time too. Just kidding.

**[00:48:08]** Great.

**[00:48:13]** Okay.

**[00:48:23]** Can it. Yeah. I don't know, man. Jeez.

**[00:48:28]** Sorry.

**[00:48:34]** You see, I saw the possibility of a thing, so I was like, oh, now I have to do it. Is it going to count it as an image, though? We're going to find out as a group.

**[00:48:45]** Bowse.

**[00:48:49]** Think Ghita.

**[00:48:55]** It does not consider it to be such.

**[00:48:59]** But.

---

### Chunk 6 [00:48:45 - 00:58:45]

**[00:48:45]** Wowz thinks it does not consider it to be such. I'll bet there is a super easy way to make it like just export as PNG on a regular basis. I'll bet it's in the scripts thing.

**[00:49:13]** Export layers.

**[00:49:26]** All right. And can we do that? Is that right? I think. I think so.

**[00:49:35]** Hold on.

**[00:49:55]** Sure.

**[00:49:58]** All right. A. B.

**[00:50:10]** Great. How we do that? And so you are Skelly Tracker. You are Skelly Cam. You are Skelly Tracker.

**[00:50:17]** Okay. And now we're getting into Skelly Forge, which is where it starts getting a little more.

**[00:50:24]** There's more. Well, like there's work to be done all over this place. So let's do this. Now we're going to be port pole and. Ooh.

**[00:50:36]** Okay. Let's draw them as boxes in the. Currently in their current form because there's some unspecified stuff right now. So Skelly Forge does. Ugh, fuck.

**[00:50:51]** Wait, we have the calibration step.

**[00:50:55]** Yeah, that's right. Okay, so right now it's any pose, but it's kind of like it's any pose is doing the heavy lifting, but we're doing some of the stuff. So I am going to call it freemo Cap. Freemocap. Anypose, one could argue that the work we're doing in freemocap is not like real work, but it's gonna be because I'm about to.

**[00:51:25]** I'm about to. I'm about to hit any pose with the refactor hammer. And so this has a secondary step.

**[00:51:45]** Great. Come on.

**[00:51:51]** Why are you. Now, Gray? What are you doing to me? Why are you gray now? What just happened?

**[00:51:58]** Go ZZ Why are you gray now? What just happened? I hate it. What happened? Why.

**[00:52:16]** What the.

**[00:52:22]** What the. Why are you.

**[00:52:26]** Oh, my God. This is gonna bother me so much. Is it here? Is it transparent now?

**[00:52:35]** Oh, What's happened? No, what happened?

**[00:52:51]** Oh, where are we in this video? We're about an hour in. That makes sense.

**[00:53:00]** Okay, I'm out. Okay, we're gonna do calibration and then we're gonna do.

**[00:53:11]** We're gonna do. Yeah. And then if this produces raw 3D and that goes into.

**[00:53:25]** Skellyforge, Which does pretty much. It does data agnostic. Well, I'm just going to do post. Say post processing. I'll say post processing.

**[00:53:49]** And does. It does data agnostic stuff and also like data. I'm going to call it aware. So data agnostic is the stuff where it's just like these are. We don't know what the content of it is.

**[00:54:07]** We just Know that it is a time series. We want it to be smooth. We know there's a gap, we want to fill it. Data aware is like. We know that this is human movement, this is motion capture data, this is kinematic data.

**[00:54:17]** So we're going to apply things like rigid body assumptions and stuff like that.

**[00:54:25]** And then it goes into exporting.

**[00:54:39]** I'm gonna make it orange because it's mostly blender exporting. And that is to disk.

**[00:54:52]** Hey, what? This should disk and to blender and to viz.

**[00:55:08]** Yeah, Right. And then this is kind of where.

**[00:55:19]** Oh, actually, no, that is right how we wanted to do it. Right, okay.

**[00:55:36]** And then. Yeah, so this becomes data 3D and then this is raw. And then we have. This was better than the other one, data 3D. I think that we would say.

**[00:55:54]** Yeah, no, this is right, I think, yeah.

**[00:56:00]** So this Daily 4 produces two things, which is why it's a little confusing is because it produces 3D data that's been cleaned and it now starts to produce kinematic data.

**[00:56:21]** So I think that this means that skellyforge is going to get. I think skellyforge, I think is going to want to get split in half because those are different enough tasks that they don't want to live in the same house.

**[00:56:36]** So we're gonna split that up. And currently a lot of the kinematic stuff, like there's a bit of bleed between these two things and there's some duplicated effort between what's going on in Skellyforge and what was going on in the blender stuff.

**[00:56:56]** But we're gonna split that up. So we've already kind of like excised most of the working. The pure Python stuff has been excised from the blender add on stuff. And so we're gonna. I think the process of sorting these things out is gonna be that step.

**[00:57:15]** And then this will produce.

**[00:57:20]** So we don't need to say it's clean, it's just. This is raw. But the clean stuff is not called clean, it's just called the data. And so the output of this will be.

**[00:57:36]** 3D trajectories of the tracked points in the reference frame defined by calibration.

**[00:58:00]** And also we're going to get kinematic. We're going to get basically joint angles. It's going to be joint angles. Joint angles of a rigid body skeleton fit to these.

**[00:58:33]** And that'll be things like CSV, JSON. I don't fuck your c3d's. I don't know, man. Like do we? Do you really need a fucking c3d?

**[00:58:44]** I guess we.

---

### Chunk 7 [00:58:33 - 01:02:38]

**[00:58:33]** And that'll be things like CSV, JSON. I don't. Your C3Ds. I don't know, man. Like, do we.

**[00:58:43]** Do you really need this C3D? I guess we should do it just because. Oh, we should do it because them. Okay, never mind. Because it's a proprietary piece of C3D.

**[00:58:57]** Like it's a fucking proprietary data format. These fucking people. But if we can bleed their mode a bit by like making it more open, then we can do that. So fuck C3D. But we'll let you do it because I hate them.

**[00:59:09]** C3D. JSON numpy. Probably really shouldn't be JSON. Like, I don't think JSON's a kind of a heavy format. Maybe.

**[00:59:19]** Bson, can we do that? Ooh, maybe.

**[00:59:31]** Okay. CSV numpy arrays for the binary. So this is for the human readable.

**[00:59:39]** This is for the binary.

**[00:59:44]** I'm not gonna. I'm not gonna do it. You can do it.

**[00:59:50]** I'm not gonna waste my time with the.

**[00:59:56]** You want it, you do it.

**[01:00:00]** I don't respect those people.

**[01:00:05]** Like visual 3D and that whole C motion. Like, I. Like, I want your company to fail. Crash, burn and die. You're bad for the world.

**[01:00:15]** Give me your resources and off. Or bleed the resources back into the community at large.

**[01:00:25]** We will. We will. We will take over your very small amount of pull in the right direction. CSVs, numpy rays, BSANS. Who else?

**[01:00:39]** Oh, probably your bleh. This is also where we get hours. Where are we going here? What's happened? What's happened here?

**[01:00:49]** Why don't you.

**[01:00:55]** Oh, because we're racing.

**[01:00:59]** And probably also this is your FBX's and your DAES and your BVHS. I don't know any of these guys.

**[01:01:12]** I think this is the. This one is like the friendliest one. Xml. Is that how you make a skeleton with xml? I don't know.

**[01:01:24]** Anyways. And then also your dot blends and stuff. Okay. That's everything I have for one hour. I'll come back later, I'll clean it up.

**[01:01:39]** And I think this was good because I think I needed. This was like. I think the main realization part was that like the confirmation that Skelly Forge does need to get broken up.

**[01:01:57]** Yeah. Or at least like glumped significantly apart. Maybe it doesn't need to be broken up, but it just tells me a little about what the internal structure of it's going to be. I think that might be what it is a little more about like you know, the kind of. These are the two parts of Skelly Forge.

**[01:02:18]** Because I don't. We don't want. Because I think the cost of making a new repost should be pretty high. Um, and then, yeah, also, it's kind of like the. The.

**[01:02:32]** It's kind of breaking down. Like the abstraction is breaking down. But I think good work was done. Okay. I'm done by.

---
