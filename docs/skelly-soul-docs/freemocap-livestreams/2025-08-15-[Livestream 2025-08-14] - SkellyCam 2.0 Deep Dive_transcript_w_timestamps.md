# Transcript: 2025-08-15-[Livestream 2025-08-14] - SkellyCam 2.0 Deep Dive

## Source Information

- **Source Type:** Local File
- **File Path:** `C:\Users\jonma\syncthing-folders\jon-alienware-pc-synology-nas-sync\videos\video_eater_downloads\playlists\[2025+] FreeMoCap Livestreams\2025-08-15-[Livestream 2025-08-14] - SkellyCam 2.0 Deep Dive\2025-08-15-[Livestream 2025-08-14] - SkellyCam 2.0 Deep Dive.mp4`

---

**Total Duration:** 03:09:07

---

## Full Transcript

### Chunk 1 [00:00:09 - 00:09:59]

**[00:00:09]** Okay, so.

**[00:00:15]** So obs is showing me is not streaming right now, even though I am definitely streaming. It says my whatever is excellent, which I appreciate support. And so we're just gonna. We're just gonna go and we're gonna assume it's fine because it probably is fine. Okay.

**[00:00:42]** Oh, jeez.

**[00:00:50]** All right.

**[00:00:55]** And does the audio sound okay on your side?

**[00:01:06]** It's hot here, so I have an AC running in the background, but I also have noise suppression turned on, so hopefully that will work. And yeah, we'll just sort of take it as it goes, I suppose.

**[00:01:28]** Such a weird energy when the stream first starts. What am I doing?

**[00:01:36]** But yeah, Okay.

**[00:01:49]** Here, right, Sure. This is Milton, which was recommended to me last time by. Honestly, Micon could have been somebody else. Just like a nice, simple infinite whiteboard app, which should come in handy because I'm gonna do a lot of drawing today.

**[00:02:20]** Yeah. So welcome to today's Stream. It is August 14, 2025, and today we are going to talk about Skelly Cam. Skelly Cam. Good old Skelly Cam, the heart of the Primo Cap software.

**[00:02:43]** What am I doing? I'm gonna. This. Oh, not.

**[00:03:02]** Skellycam project logo. So, yeah, so we're talking about Skellycam specifically. We're talking about Skellycam 2.0, I suppose we could call it, which.

**[00:03:22]** To Skellycam 2.0, which currently lives on the John Slash Development branch. John Development branch. Dwink. Fix the logo. I did fix the logo.

**[00:03:38]** Great, good for me.

**[00:03:41]** And yeah, so that branch has sort of special instructions. We'll sort of. We'll talk about it. I talked about this a little bit last week in the stream. I did last Thursday, roughly around this time.

**[00:03:57]** Mostly kind of in the context of sort of showing off that it kind of does work and which is an important point for the state of the FreeMo CAP 2.0 development cycle. Because Skellycam working means the rest of it is kind of like ready, ready to start, to get. Start getting built.

**[00:04:21]** And yeah, so today we're going to do a deep dive into skellycam and talk about a lot, a lot about how it works, what it's built on, what the general architecture is, how we are shuffling around such a tremendous amount of data streaming in from a bunch of cameras. Same time. Talk a little about the packaging, maybe talking about. Yeah, we talk about all sorts of things.

**[00:05:00]** I feel like I had a. Actually, I feel like I had a plan at some point, but we'll just write it out here. I did have a plan. So we're going to start with. Change the color to that.

**[00:05:19]** Nope, that's too purple. That. The plan is we're going to do a Skelly Cam demo. No, we're not. Yes, we're going to do a Skelly Cam demo.

**[00:05:36]** We're going to talk about Skelly Cam's place within remote cap. Oh man, I love this app. This is great. Am I not streaming anymore? No, I am.

**[00:05:51]** Okay. I got the. Yeah, there's like the 4 second lag there. So 1100-0210-0031-0004 1000, 4 1000. Roughly 41000 worth of lag.

**[00:06:10]** Yeah. So Skelly Cam demo, it's placed within Freemo cap and kind of like how it sort of situates itself. And then we'll talk about the guts.

**[00:06:23]** Guts of skellycam which I imagine will be somewhat self describing. But I will. Let me see if I can try to hit the main pieces right now versus the general architecture of a camera group.

**[00:06:47]** Probably focus on the. Yeah, there's a little bit ipc. IPC interprocess communication. That is the main, that's the main challenge here. That's the main issue with skellycam is because if you are trying to connect to a large number of cameras and those cameras are trying to dump a large amount of images into the, into the world and you want to be able to simultaneously record those and process them and get them where they need to be, inter process communication becomes the big challenge.

**[00:07:20]** And I don't want to get too, too deep into the weeds. But there's. We have a combination of a publisher subscriber pattern pub sub and a pretty complicated system of shared memory which is sort of what's doing the main job and.

**[00:07:47]** Camera group IPC pub sub shared memory and talk a little bit about the camera loop now. That's fine. I'll get there. We'll get there when we get there. And then I want to talk about sort of like what would it be like.

**[00:08:15]** Kind of like where we're at, I guess.

**[00:08:23]** Yeah. What works?

**[00:08:34]** Yeah, Current status. Status and roadmap, which is basically like here's the parts that work, here's the parts that are broken. Here's the parts that are broken that like I'm not going to do anything with for now because I got to work on other parts because I'm trying to get the actual like main thing working.

**[00:09:00]** There's gonna be a lot of stuff that's like, you know, help requested kind of thing. Particularly on the react side which you talk about. Yeah, general architecture.

**[00:09:17]** Yeah. I don't know how to do front end development, so I was able to kind of like hack and slash my way through with the bot, but there's a lot of kind of details. Turns out front end development is like a whole thing and I am not experience in it, so it's doing the job. So AJ was posted in the server just now with your 120 FPS cameras and it sort of like it connective and then immediately overloaded the front end. It's like yes, that is that.

**[00:09:58]** Yep, that makes sense.

---

### Chunk 2 [00:09:46 - 00:19:45]

**[00:09:46]** Was posted in the server just now with your 120 FPS cameras. And it sort of like it connected and then immediately overloaded the front end. It's like, yes, that is. Yep, that makes sense. That's what I would expect to happen.

**[00:10:02]** And you were suggesting like, you know, being able to turn off the streaming, which I think is a good idea, headless mode, stuff like that. And just kind of like being smarter because there's already a system in there that's trying to stop it from overloading the front end, but it doesn't work all that great. So get there.

**[00:10:25]** Okay, sure. Great plan.

**[00:10:36]** And.

**[00:10:43]** Down. So yeah, I'm gonna talk a little bit more about some of the nitty gritty of what's. Oh, talk about the build. The build. The building guys.

**[00:10:52]** The building. The building of the thing.

**[00:10:59]** Where I want to put that. I don't do that. I gotta do that near the beginning because if I try to get started.

**[00:11:07]** Build in installer because it's an electron. So it can. I have kind of a proof of concept of like a single click installer like mostly works and I will try to show it off here.

**[00:11:33]** But I want to do the demo first because it's. Do the demo first. I'll do the demo first because you should lead with your. Your strongest whatevers.

**[00:11:47]** So. Yes. So on the John development branch of Freemo Cap Skellycam, there are special instructions on how to run the dang thing. Long story short, you got to run the Python server backend and at the same time you got to run the Electron front end. And here's how you do it.

**[00:12:08]** And there's some Linux stuff because there's always Linux stuff. Here's how you do it. Here's how I do it.

**[00:12:19]** So I generally these days I will have both a copy of PyCharm and a copy of Webstorm Running. PyCharm and Webstorm are Python and like web development IDEs from JetBrains. I believe they're both free now. I think they used to be paid and I think that they are now free. I'm not 100% sure about that.

**[00:12:45]** I run them through this toolbox thing and I do get. I think I get access to it for my school. So it may not be free, but I think at this point both of those are free and you could use VS code just as easily. I just like using these because they're more sort of dedicated to the languages involved.

**[00:13:04]** Yeah, and here's how you do it. So it doesn't matter which order you use. To do them, which order you start them in. So here in the skellycam repo, John developed a branch and the. So the raw skellycam folder as the Python package.

**[00:13:24]** In here there's a double underscore main file and you just want to run that blink, run it, run it and all this fun stuff will pop up and it says oh, we got all these routes. And then it's like here's where the back end lives. There's like an API, it's running on localhost and using fastapi. Yeah, ready to go. Oh wait, I can click on this and boom.

**[00:13:54]** Look at all these endpoints. Look at these auto generated swagger docs. Look at all of these. Look at all these things you can do and connect to the cameras. So actually theoretically you can run the server in.

**[00:14:11]** What's the word? Headless mode. You just, you just got to click it through this. So like I can detect the cameras, try it out, execute. And then look, there's all the cameras that are attached to my computer.

**[00:14:22]** So theoretically you could run the whole thing from this. But it wouldn't really be fun and I think it would involve some copy pasting of the. The hardest part would be this camera group create because you have to like generate your own config files but you can connect to like Camera zero easily enough. I use it to test, but I don't, don't recommend it.

**[00:14:45]** Boop boop boop. Anyways, so here we are, we've got the back end running good for us. Look at it go. That popped up when I hit the executed the camera detect. It goes boop.

**[00:14:58]** And it hits it and says here's your camera. Then it sends it back to the front end and currently the front end it doesn't do anything. It just, you know, there is no front end. It's just this like demo page and that just catches the JSON. So now that we have server running we can go to and open this up in webstorm.

**[00:15:18]** But again you can do this through VS code. You can do it through two separate terminal windows. To my knowledge it. I think it works on Mac and Linux, but I have, I mostly am testing it on Windows so don't know for sure.

**[00:15:38]** Nordvpn. Calm down.

**[00:15:49]** Okay, what's going on webstorm? What you thinking about? Why are you being weird? It's people watching.

**[00:15:59]** Be cool man.

**[00:16:06]** Come on. Come on, buddy. Never doubt. Okay, so. Oh, that's free mocap.

**[00:16:17]** I have started the process of porting over from Scalycam to Freemo cap. But we are not. We'll talk about that. Talk about that at the appropriate phase of the presentation.

**[00:16:34]** This window. Thank you. And.

**[00:16:42]** Yeah, so now here we are. Same thing. Skellycam, this folder skelecam UI that has all of the front end user interface code. So it's got all of the Node, React, typescript, Electron. It's a lot of config.

**[00:17:09]** The Electron folder has all the Electron related stuff and this SRC folder, Source folder has all the REACT code for the renderer process, I suppose. And electronbuilder JSON has all that stuff. And then package JSON has all the main business and the most important one is this NPM run dev, which if we just. I'm just. I'm gonna do it through webstorm just because.

**[00:17:41]** Why not?

**[00:17:45]** So now this terminal is the logs from the server and I run this. The logs from the, from the front end are not particularly interesting. If you're going to look at logs, you're most going to be looking at the console logs in the app. But don't worry about that for now. You would.

**[00:18:06]** Yeah. And so now this guy's popped up. The websocket is connected. Oh, you can click it.

**[00:18:16]** Apparently you can click it. Great.

**[00:18:21]** And it has.

**[00:18:24]** Yeah. So it's detected all the cameras that are attached. These are all valid cameras. I have currently eight cameras connected to my computer, hardwired with usb. And nothing particularly special about that except that I managed.

**[00:18:42]** I got a lot of USB ports on my computer. If you're wondering how I pull that off. The main trick is to take all of your peripherals that are not cameras and run them through a hub because they don't need the bandwidth, but your cameras do. So, yeah, this one right here, cam link 4k, that's the one that's running this camera. It used to not work, but these days it actually can connect to that.

**[00:19:08]** It just. I don't, I don't. It's like I tried it once and it connected and I was like, great, I don't want to think about that. So if you. It theoretically works now, but I'm not interested in playing around with that.

**[00:19:22]** So.

**[00:19:26]** Let's, let's play it easy and connect to just four. For the record, I do not recommend connecting to eight or nine cameras. That is not a thing that I think is going to be like useful for most people. In most cases, I am using this stupid number of cameras.

---

### Chunk 3 [00:19:30 - 00:29:29]

**[00:19:30]** Or for the record, I do not Recommend Connecting to 8 or 9 cameras. That is not a thing that I think is going to be like useful for most people. In most cases. I am using this stupid number of cameras mostly as a way to stress test the code to make sure that basically on the assumption that if this computer, which is a reasonably beefy powerful computer, if this computer can run eight or nine cameras, then a wimpier computer can run three or four cameras, which is the number that I generally would recommend if you're interested in doing mocap Y stuff.

**[00:20:09]** So let us. Alright, so we got these. We can set some config variables here, but I'm just going to leave them as they are actually. I'm going to do.

**[00:20:25]** And we go click. You see the back end is charting up this little server logs thing down here.

**[00:20:34]** It relays, hey, what's up? That's me. It relays logs from the back end. I think it only does info or above. Mostly just because it was overwhelming the websocket and it's.

**[00:20:49]** There's a lot of, there's a lot of things that need to be improved and made more efficient. But this should give you a sense at least of what's going on. Hello, that's me. I am dark. Let's see if we can use this recommended exposure setting.

**[00:21:05]** So I'm going to set that. There's a lot of things again about the visuals that I don't love. Like really, there should be some kind of summary of the settings here. You shouldn't have to like expand it to see the settings, but like the current primo cap, you can set this recommend thing. Click this little button here and it will connect it, it'll attach to the next one.

**[00:21:26]** It'll. What's the word? What am I trying to say? It will copy those settings to the rest of the cameras, which can be helpful. And now if I run this.

**[00:21:37]** Oh, wrong button. Shouldn't have clicked that button. Now it's going to break. Is it going to break? Yeah, yeah, yeah.

**[00:21:45]** For example, these are the things that we need to work on. So like the whole issue of like there's a button that doesn't get disabled and if you click it at the wrong time, it kills the program. This is what we're dealing with. So the solution to that is don't click that button. Yeah, it's a great plan.

**[00:22:04]** So when in doubt, restart the whole thing for the Python server. Just like kill it and restart it for the front end. Usually there's not much reason to do anything other than just like Control R and it will just refresh the page. So this is Chromium. This is an Electron app, which means that this is secretly just a little Chromium installation.

**[00:22:26]** So all of your standard browser shortcuts will work. So Control R refreshes the page. Control Shift R refreshes it harder, I guess kills the cache. I don't know.

**[00:22:41]** There are some things that are remembered. Most things are not. For example, the camera settings are forgotten across refreshes, which is annoying. But we can fix that. There's got to be, like a persistence thing, I guess.

**[00:22:53]** I'm gonna hit recommend. I'm gonna hit connect to all the cameras. Oh, I guess I. So this is the button I wanted. That's the Apply Settings settings.

**[00:23:02]** This is Connect. So Connect works if there's no connection, applies when there is a connection. Obviously, having a button that is broken and kills your code is not ideal, but there we go. Look and see. Now, the exposure is better when you do the recommend option.

**[00:23:25]** It does this process where it just. Basically it connects to the cameras and it cycles through a bunch of exposure settings and then it chooses the one that has a luminance of about half. So all the pixels are roughly. I don't know, if I collapse across color, I should collapse across color, but all the luminance of the pixels is all roughly 127, which is half of 255. And then I think it recommends the exposure setting that's like one level darker than that.

**[00:23:57]** Because for motion capture, we want to have darker than you would normally want for a camera, because we want to minimize that blur.

**[00:24:09]** Oh, look. And it's even reporting those values. Yeah. Cool. Good.

**[00:24:14]** Didn't used to do that.

**[00:24:17]** Yeah. And so here I am. Hello. I am four cameras. These two cameras, as you may have noticed, are rotated wrong.

**[00:24:27]** So who are you? Your camera three. You're camera two. So camera, we're going to do 90. We're going to rotate them by 90, and then we're going to hit the correct button this time.

**[00:24:38]** And then it's going to go back and it's going to take longer than it should because of some dumb bug that makes it do weird. And then that happens. And then it notices that happens. And it shuts down the cameras and restarts them again. Don't worry about it, or actually do worry about it because it's annoying and I would like to fix it, but there's a.

**[00:24:53]** There's just. It's a. It cropped up at some point. It used to be. It should be that when you change those settings, it should just change real fast.

**[00:25:00]** And like that should be that. But there's. And for. And for a little, for a brief moment, that's what happened. But then at some point some bug emerged where when you change the settings of the cameras, the frame rate drops.

**[00:25:13]** I don't quite know why, I don't know if you noticed, but like one of the cam, this camera got really bright for some reason. I don't know, man. I don't know. So I put something into the code that if it detects like, I think it's 30 frames in a row that are at the wrong frame rate, it just shuts it down and restarts it. So that was the reason for that.

**[00:25:37]** But.

**[00:25:40]** But. Sup? We're good. We're doing great.

**[00:25:47]** Cameras, Camera town, usa population, all of us.

**[00:25:57]** And yeah, that's, that's. So that's. That's connecting to cameras. These ones are right next to each other. So that's fun.

**[00:26:08]** Actually, let's.

**[00:26:16]** Yeah. So, yeah, so this is connect. Don't push it when you're already running. This is apply settings to cameras. This is redetect.

**[00:26:26]** Available cameras also probably wouldn't recommend doing that while you're already connected. And then this X plus closes down the camera group and then you can reconnect to it and that should work reasonably well. So shut it down. They all die as they should. I see the green lights turned off.

**[00:26:45]** It doesn't clear the page, but don't worry about it. And then if I do it again, it'll be good.

**[00:26:56]** And it should remember the setting. Yeah, it remembers the settings from last time because I didn't refresh it. And then.

**[00:27:06]** I do need to refresh it. And then here we go. Boom. Sup? Here we go.

**[00:27:12]** Nice.

**[00:27:15]** We have the div.

**[00:27:19]** Like it's doing its best to sort of fit, but it's obviously not using space that efficiently. But again, it's just a browser, so you can just hit Control shift plus or minus and just sort of zoom until you get roughly the configuration you want.

**[00:27:41]** This is one of those things, like, I don't really understand how Flexboxes work, so if you do, please help.

**[00:27:49]** Down here we've got a little frame rate detector, like real time frame rate detector, which is really useful, particularly because it shows the difference between the front end frame rate, which is the line here in blue. That's what you're seeing in the front end in the GUI. And you see that one's coming in at about 66 milliseconds per frame, which is half the appropriate frame rate, gets both fast half of the correct frame rate.

**[00:28:24]** I kind of go back and forth in the GUI of reporting frame rate either as mean frame duration, so how long each frame is, or the inverse of that, which is the more conceptually simple frame rate FPS frames per second. So whichever one, it's one of these things I think, where when you're at certain points in the dev cycle and analysis, the cycle frame duration makes more sense. But then I think the more common FPS is a more intuitive term, but so the orange line down here, this is like. Yeah, this. Yeah.

**[00:29:07]** I'm glad it's there, but it could be better.

**[00:29:11]** Yes.

**[00:29:15]** Pinocchio hey Java, just catching up on your things, Pinocchio?

**[00:29:23]** I will check out Pinocchio, but I, I have a solution that makes installers. It's, it's.

---

### Chunk 4 [00:29:16 - 00:39:13]

**[00:29:16]** Hey, Java, just catching up on your things, Pinocchio?

**[00:29:23]** I will check out Pinocchio, but I. I have a solution that makes installers. It's, It's. There's a lot of options to make installers for simple software. However you want to define simple. This is.

**[00:29:39]** This is not. This is not simple. But yeah, I'll show you my method in a second here. It works pretty well and does a decent job. But yeah, so the frame rate display, I don't even know if you'll be able to read the lines down there, but the orange one being flat at 32 milliseconds, that's what you want.

**[00:30:00]** The back end frame rate is the thing that determines the videos that get recorded. And we try to be intelligent about like throttling the front end in order to make the back. Like, we protect the back end, we protect the recording of data to disk, and we try to make the actual display of the visual data squishy. Because, yeah, like, the frame rate of the UI is not really too important. It's not critical in the same way that recording the data is.

**[00:30:41]** But yeah, so this is a time series, this is a histogram. It's like a relatively small number of samples that keep. Remember, that's why it doesn't keep going for very long.

**[00:30:55]** It's a helpful diagnostic. And I also noticed that I can use this as a measure of how much I'm loading the system, because I can. The back end code stays pretty stable, but the front end code will vary as I put more load on the system. So I can use that as a method which is useful.

**[00:31:16]** Oh, yeah. And then one of my most favorite parts, because a lot of the work is trying to make the cameras, the frame grabbing between the cameras really, really synchronized. We want these images to be coming in at as close to the same time as possible because the synchronization between the images from the cameras is going to be a thing that determines the quality of the 3D reconstruction, because the triangulation. So the more accurate it is, the synchronization between the cameras in a very real way will define like a base level of accuracy that we can get. So we want that to be really precise.

**[00:32:00]** And so if we do this and click on, I don't know if we'll be able to.

**[00:32:10]** I'll run an ad. I'm going to wait until the ads done before I do the exciting demo.

**[00:32:19]** Hey. Stuff. I don't think anyone's watching right now, but Twitch shows ads don't love that. I'll figure it out or I won't. Oh, no, I'll figure out how to stream to YouTube and they won't have ads.

**[00:32:42]** And we're back. I apologize for ads.

**[00:32:48]** Moving on. Here we are, we have three cameras. We can see them all here. If I push the pause button, then you zoom in, You can see that you can get a sense of the level of synchronization between the frames. This is what we call, we call that like 10 o', clock, 10 o', clock, about 10 o'.

**[00:33:19]** Clock, that's maybe like 9:30. So there will be a time when we're like making more carefully calibrated diagnostics. And I want to have arduinos with flashing LEDs at regular intervals. And if I can do like an, like, like, like an addressable LED thing and have them like zipping across at, you know, one, one, you know, one millisecond, like all sorts of stuff you can do just to get like, physical measurements. AJ Was doing the sort of, the classic move of just pointing all the cameras at a clock and then seeing which frames get, get logged.

**[00:34:04]** Problem, of course, is that most of the clocks that we would find on, you know, cell phones or laptops or just, or anything on the web is, is not like the, the frame rate of the clock is going to be like, relatively low. So someday I will get my hands on like a sports clock, like the big, like the big red ones with, like that, that actually measure milliseconds. And then I'll get a good sense of what's going on. But anyways, this is. So this is streaming.

**[00:34:34]** We've got this. It's synchronized in real time. That's very important. But the previous methods, the current sort of 1.0, 1 point X, I guess. V1skellycam uses the staged pipeline, so it records all the videos independently and then synchronizes them after.

**[00:34:56]** Oh yeah, that's right, A.J. yeah, I'm actually going to pull that up. I'm going to finish the thing I said. I realized that like, the, the chat is not shown in the video. So if you look at the recordings that make it to YouTube, I occasionally just like stop and say a random thing because I'm seeing something pop up in chat.

**[00:35:17]** But yeah, so the previous versions of like, v1skellycam recorded the videos independently and then sort of lined the frames up after the fact, which does a decent job. But it does mean that the, the synchronization between the frames, you would expect to be about plus or minus somewhere between one to a half of a frame duration. I think it's like plus or minus half a frame duration. So you would expect that the range of a given frame group from a multi camera recording would have a timestamp range about one frame duration, 15 to 30 milliseconds.

**[00:36:02]** Garfield without Garfield. It is like Garfield without Garfield. That's not even old Internet, that's like old new Internet. Yikes. Yeah.

**[00:36:15]** But I'm going to show this. As Andres pointed out, he had a. So here we are in and the. The Discord server which at this point I think it's a. It's over 2,000.

**[00:36:36]** I think it's around it. I think it's. I think it's between two and two and a half thousand people which is a lot. Which is great. And yeah, yeah.

**[00:36:45]** So this, this is recording with this is the 120 FPS cameras that he's got that and then like turning the cell phone on and off which is another, another classic test which is basically the camera flash test and that playing and yeah. So within that I don't know what the duration of the turn on moment is, but it's within a singular frame which is very fast.

**[00:37:26]** We're into it.

**[00:37:32]** Yes. So real time synchronization between the frames which is very good. Synchronization is tight. How tight you ask? What are we talking about?

**[00:37:41]** Great question, glad you asked. Let me make the UI small again because the again very easy and will be relatively easy to sort of like adjust the camera image scaling. But for now I just zoom in on the entire UI which means that if you go a certain the UI elements sort of match the. They shrink and whatnot. So occasionally you want to build it back like that.

**[00:38:10]** This panel here lets record videos and there's all these things you can set timestamps, subfolders, auto increment delay, start. But I'm just going to do a quick demo. Currently does not record audio but there is nascent audio recording code in the code. I just you know, sort of one thing at a time type of thing. But I have like in the past like proof of concept recorded audio synchronously to the video which for mocap, like for a practical perspective for mocap not necessary.

**[00:38:48]** But from a workflow level audio is so goddamn helpful because first of all you can like record while talking which turns out people really like it. I think pairing audio with video, I think it's going to be big. But even like from a research perspective.

---

### Chunk 5 [00:39:00 - 00:49:00]

**[00:39:00]** Talking, which turns out, people really like it. I think pairing audio with video, I think it's going to be big. But even from a research perspective, from an artistic perspective, obviously you want to be able to pair both, because then you could just play the audio with the mocap and it will look like Skelly's talking. From a scientific perspective, the audio is important because then you can say things like, okay, you know, trial two. You know, increasing the treadmill speed to two and a half.

**[00:39:31]** Like, you can say things into the microphone that will become a part of the record. And especially now in these days of basically free audio transcription methods from, you know, Whisper et al, it's really going to be helpful to have, like, audio stream as you go.

**[00:39:53]** But apparently I don't have that, so suck it up. But let's record something, shall we? Let's give it a. Let's give it a tag. Let's say in stream.

**[00:40:07]** Twitch. Stream. Twitch. Twitch, stream. Demo 4 camps.

**[00:40:16]** And.

**[00:40:23]** I'm mostly at this point trying to make sure I know which ones will be.

**[00:40:30]** Yeah, okay, so I'm gonna do.

**[00:40:35]** I'm gonna do something. Okay, so Starting recording in 5, 4, 3, 2. 5, 4, 3, 2, 1, start. And then 1, 2, 3, 4, 5, 5, 4, 3, 2', 1, stop.

**[00:41:00]** I've been doing that test just to make sure that you're not like what you're clipping on the beginning and the end of the recording. You'll notice that when I push recording, the UI does pause. And that's a real pause. That's a real. Because in the moment in the code, we don't create the video recorder until you push record, mostly because the recording name isn't defined until you press record.

**[00:41:37]** So the first. It takes a little bit of time for the back end properly pauses for about maybe a second or so. There's ways around that. It's a little more complicated than what we're doing. But for now, just don't expect the first second to record.

**[00:41:57]** We'll look at the actual recording in a second. But you will notice that there's all this fun one pink text that shows up. So, yeah, and this text is also saved to disk. I'll show that in a second. But this is showing the statistics of the recording, particularly with the statistics of, like, the timestamps.

**[00:42:20]** There was. There is a fairly pathological approach to logging embodied in this project, and that is. That is very much maintained through the timestamps. I record a lot of timestamps of, like, every single. Every single, like, moment in the.

**[00:42:45]** In an image's life is timestamped and that gives us this fun log after the fact. The important ones are so. So name of the timestamp is there. Apparently I didn't need to put that leading underscore. I should probably clean that in the end.

**[00:43:01]** Number of cameras is 4 total frames 258.328 seconds duration. And then these are the kind of the main numbers to care about. So frame rate these 30 FPS cameras. Frame rate 30 frame duration 32. And then this is my favorite one of all.

**[00:43:20]** And inter camera Frame grab sync 0.264 milliseconds. That is 264 microseconds of variation between the cameras. Now that's the median. So looking at these numbers sort of and thinking about how to think about the numbers, the median is I think probably like the most, the most like reliable measure of central. The most reliable measure of central tendency because it is not affected by outliers.

**[00:43:50]** The sort of the story that people tell is if you have 10 people in a room and you sort of calculate their average salary and then some billionaire asshole walks in, they don't have a salary but the average net worth of the mean person in the room shoots up when that rich asshole walks in, but the median does not. So median is a good measure of central tendency because it is not robust to outliers. But you don't use all your data so it's not sort of a little, seems like it's a little bit cheating. Mean on the other hand does use all of your data so it is affected by outliers. And the main sort of way to use those numbers is if the mean and the median are different then you know that you have like outliers in your data that are sort of shifting things around.

**[00:44:38]** So so the median inter camera frame grab sync which is the difference between the timestamps of each frame within a multi frame Object is around 2.6 milliseconds. The mean is 0.34 which is a difference of about 50% coefficient of variation which is noticeable.

**[00:45:05]** The min and the max is the min and the max from that, from that, from that sample. Like all the samples. I don't know how reliable those numbers are because I'm pretty sure that like the first and last frames of a recording are weird. So I suspect that like the, the max duration variation was 2.2 milliseconds. Still pretty, pretty good.

**[00:45:29]** But I would, I would want to see if that was like always the last frame or always the first frame. But who knows? Looking down here, into the stamp, into the life cycle, I guess every frame goes through a couple of stages. The frame is grabbed from the camera, we'll be going into the guts in a second. But I'll just.

**[00:45:51]** High level frame grab is basically when OpenCV sort of like this is right, this is kind of like at my depth of understanding. But the grab Moment is when OpenCV basically says to your OS, hey, that USB that we're watching, data is streaming by and we're mostly ignoring it. But when I say grab, grab that buffer, don't let that buffer evaporate. And so it grabs it. And so now, and so that moment I believe is the, is like the best approximation of like the moment of measurement, like when the, when the camera is recording the world.

**[00:46:37]** The frame grab timestamp is the measurement number. If anyone here is a camera engineer who has a different opinion on that topic, please let me know. But yeah, so after the grab, so you've, you've sort of, you've, you've reserved the buffer, you've called dibs, you've said, hey, don't let that evaporate. But it's not in a useful format. It's in some, I don't know, probably something that is described in the 180 page PDF document that defines the universal video codec from the USB foundation.

**[00:47:09]** But I'm not, haven't been down there yet.

**[00:47:18]** Then. So the next stage of frame retrieve is when that buffer is decoded into something resembling an image in OpenCV, Python, NumPy, whatever, OpenCV in Python, it returns a numpy array which is equivalent to a bitmap.

**[00:47:40]** And I think that number, it tends to be where time is taken. It tends to be the majority of the time is spent during that retrieve operation. It's relatively CPU heavy and I think that's what a codec is, I don't really know. Then we copy it out to camera shared memory, we record it to disk, and then this number down here is another important thing to look at, which is for a given frame, how much of the time of that, in this case 30 millisecond loop was being spent actual processing actual work and how much is being spent idle. So in our particular case, roughly 60% of the frame loop was being spent doing work and roughly 40% was spent idle waiting for a new frame to become available to the camera.

**[00:48:32]** So great, yeah, important in various ways.

**[00:48:45]** So yeah, let's look at, let's, let's look at the data itself. What do you say?

**[00:48:57]** Hey. Mhf. Mhf. I'm guessing it's the coding that.

---

### Chunk 6 [00:48:46 - 00:58:44]

**[00:48:46]** So yeah, let's look at, let's, let's look at the data itself. What do you say?

**[00:48:57]** Hey, mhf. I'm guessing it's the coding, the camera stream, ie mjpeg. I think so. I think that's true.

**[00:49:07]** I get a little like my brain, like the layer of cameras that I'm currently on is trying to wrap my head around like around like the concept of a camera stream and how that relates to like the kind of the more like naive but functional view of a camera as a thing that produces images in a, in a real fast way. I know that the camera stream is like the more modern sort of way of handling it. It does like. I think it does like compression and deframes or something like that. I don't really know.

**[00:49:41]** It's like in the guts of OpenCV, I do aspire to understand it, but I have other things to do.

**[00:49:53]** In the camera config object There is the capture 4cc which is for four character code and the writer 4cc which is for the video. And our default is in fact mjpg. So yes, it appears that that is. We think so. We think that's what's going on there.

**[00:50:15]** I've tried a couple different options there. MJPG was the one that seemed to have the best performance at a certain point. The bottleneck is that it's Python, but we can live our life also. Hello, MHF players. Thanks for showing up.

**[00:50:31]** You appear to be the thing says you're a first time chat, so. Hi, Code, no data. Actual data.

**[00:50:46]** What's going on here? Why can't I.

**[00:50:51]** My computer is working harder than I really.

**[00:50:59]** Where am I actually with the. Let me check my. Check how. I'm at 70% CPU, that should be fine.

**[00:51:13]** I can't open an Explorer much as I would love to.

**[00:51:33]** Great. See, normal, regular thing.

**[00:51:46]** So I'm like I'm copying a large amount of data over to make space to record this. And realistically if I was smart, I would have waited for this to be done before I started the stream. But I'm not smart.

**[00:52:01]** It'll be fine. See, it's normal for it to take measurable time for your File Explorer to show you your data. That's. That's totally normal and like a sign of a healthy computer. Okay, so the data gets saved to your.

**[00:52:23]** What is going on? This is not my default.

**[00:52:34]** Hello. Howdy foa. Hello. Yes.

**[00:52:42]** Okay, well, I don't know where, why we're doing any of that, but yeah, there we go. Nope. That was not right. Oh, that's right.

**[00:52:56]** Hey.

**[00:53:01]** Okay, so there we go. Edit that post.

**[00:53:13]** The data gets saved to your home folder skellycamdata into a folder called Recordings.

**[00:53:25]** There you go. That's the one. So it's the year, month, day, time, plus local gmt, whatever, and then whatever tag you added to it. So these folders from skellycam are structured exactly the same as the ones from Current and Past Free mocap. So probably not going to get to it on this particular stream.

**[00:53:49]** But the data I was showing last time was recorded on skellycam. And then I just dragged this recording folder into the Free mocapdata Recordings folder, and then you could just process it from there. Because Freemo Cap V1, V2, whatever, is just looking for a recording folder. And inside of that it wants to find a folder called Synchronized Videos. And in that, it's expecting to see videos that have the exact same number of frames, and those frames should be synchronized with each other.

**[00:54:19]** So here we go. And that's me. And look, we go. Oh, yeah. So, okay, so if you remember, in the recording, I did start 1, 2, 3.

**[00:54:33]** So it looks like it. It kind of missed most of that, like fisting. It got a little bit, and then I count back down and then I endofist and I click the button. So, yeah, so the. The stopping is good.

**[00:54:46]** You lose like, you know, some portion of a second at the beginning of the recording.

**[00:54:55]** This is more of a placeholder than an actual useful thing at this point. But I want to start kind of like automatically saving, like a readme to the recording folder that's sort of explanatory. A lot of the thinking around Freemo Cap is based off of my experience as a grad student, postdoc and researcher in general, and my general lifetime of just the person who's just clicking around.

**[00:55:23]** You write the docs, you write the documentation, you do the live streams, you make tutorials, you make the code, you try to make things intuitive. But I'm expecting that most of the people who are using this are the people who are just like, where's the data? Let me click around inside of the folders. I'm always trying to think about what can be done in the folder to help that person who's just clicking around and looking at stuff. And a really easy way to do that is just, like, save useful pieces of text.

**[00:55:49]** It costs nothing to save a little markdown file. I'm also thinking about, like, one issue is that for a, you know, thinking about the Sort of the hypothetical, like non technical, you know, high school kid, they may not know what a MD is. So in like a computer, I think a standard computer may not have an associated file with md, but I think saying readme is a little bit of like, hey, double click it, you know. Also I could just do Txt if I need to in the recording folder, the timestamps folder. This stats.

**[00:56:26]** Txt. That's the same sort of stats file there.

**[00:56:36]** Yeah, I mean I just kind of have, I'm just, I'm trying to like remember what it was like to like, you know, before I knew how computers worked. And a lot of people learned like, you know, like random files with strange, you know, extensions which I guess most computers don't even show you the goddamn extension anymore until you turn it back on. Because the tech industry doesn't like or respect you. And we're living in a sort of two or three decades of world where the primary business model of the corporate capitalists that run the world is predicated on a ignorant user base. Like they do not want you to be good at computers because if you're good at computers then you stop being locked into their system.

**[00:57:24]** So a lot of the sort of the, the structure of current OS is not designed to. It is, what is it? The paradox of the active user is a design decision, but we try to treat it as a problem to be solved anyways. So folder full of timestamps saved as CSV. You get one timestamp log per camera.

**[00:57:51]** But the one that you probably really should be looking at for the most part is the, this one, which is for the full recording. So the cameras have their individual timestamps and the recording timestamps are based off like they should, they have like statistics of the variation between the cameras. Yeah, their platform, their wall garden. Exactly.

**[00:58:16]** We are, I am not, we are not agnostic about the nature of the world. This is CSV. I don't know why it's not opening up with this extension data wrangler.

**[00:58:36]** Is it like, oh, we're in restricted mode, fine, trust me, trust me. And then it gives you this.

---

### Chunk 7 [00:58:30 - 01:08:29]

**[00:58:30]** This extension data wrangler, is it like, oh, we're in restricted mode, fine, trust me, trust me. And then it gives you this, look at all these datums.

**[00:58:52]** I'm also like, I have a long history of being like continuously annoyed and disappointed and misled by timestamps from other people. So if there is any timestamps that I am not logging that you wish I was logging, you just let me know and I will do it. Because it's like most cameras, the vast majority of cameras do not log timestamps. And if you have a camera that, that claims to log timestamps, my request is for you to get that string of timestamps, calculate the difference between the frames and calculate the variability of those frame durations. Because I'm going to bet you, I won't bet you that much money because I don't know your camera set up.

**[00:59:42]** But most cameras don't log timestamps. And the ones that do lie about it, they take the number of frames divided by the, by the frame rate and then they say, here you go, that's your timestamp. Actually, it's not even that. It's the number of frames divided by the recording length and they give you the presumed calculated timestamps. But they don't measure frame drops, they don't measure lag, they're just guessing.

**[01:00:10]** So these are measured timestamps. They're grabbed synchronously to the image being grabbed. So they should be, they should be trustworthy. And you know, this is, you know, there's, there's a lot of them which can be its own kind of problem, but for the most part you're only going to need like the first sort of 3ish rows. The recording frame number is counting up from 0.

**[01:00:34]** The connection frame number is probably not useful to anyone, but that is the frame count since the camera group was connected. So conceptually, camera group is a group of cameras that are sort of reporting synchronously timestamp from recording start. So starting at very close to zero and counting upwards timestamp in UTC. So number of seconds since 1970 or whatever that number is local time, ISO 8601 format which is international standard of some kind.

**[01:01:18]** Yep. If you're into that. Is that recording? Yeah, that's local. It's local, don't worry about it.

**[01:01:29]** Timestamp in the perf counter, which is so in Python, if you want to get a high accuracy timestamp, you use time perfcounter ns, not time time. It's not updated Fast the number that time perfcounter reports. So time perfcounter gives you the answer in seconds, which is more conceptually useful. But then you get floating point error. Time perfcounter NS gives you timestamps in nanoseconds, which you really shouldn't trust.

**[01:01:58]** Nanoseconds when Python reports them. But they're integers, so you don't get floating point error.

**[01:02:05]** So and. But the number is arbitrary. So this again is kind of like. I don't. I can't imagine a world where this is useful.

**[01:02:11]** But this is the frame. This is the inter camera grab range. That's just the range in milliseconds. I guess I can check real quick. What the.

**[01:02:21]** Oh, yeah. So you know that 2.2. Oh, yeah, there you go. That's. That.

**[01:02:26]** The long one remembers like. Oh, the long worm. That's the second frame. So it's still kind of getting started up, which makes sense frame duration and then. Yeah.

**[01:02:34]** All these guys. Yeah. Are they useful? I don't know. I'm glad I have them.

**[01:02:41]** I will use them. Whether or not you will use them is sort of up to you, but you deserve real time stamps and Kelly cam Ellie's gonna give them to you. Deli it is. Yeah, that's. I don't know.

**[01:02:56]** That was a. Oh, yeah, what's up? That's filming. Oh, yeah. This other fun thing, one of the things you kind of get from like the fastidious levels of timestamps, again, not so useful from like a standard user perspective, but from a developer's perspective. And this is also Data Wrangler is just like a nice VS code extension that I'm using here.

**[01:03:16]** And it gives you like the histogram at the top so you can kind of get a sense of what the health of that measurement is. Like a nice little histogram. Like, this is good. A weird goobly one like that. Like, there's more going on.

**[01:03:30]** And in particular when I see this, this is a bimodal distribution, right. There are two distinct things happening here. There's short frames, then there's long frames. That might be related to compression or something like that, but I don't think so. I don't really know.

**[01:03:47]** But these are the events. Like someday when it gets to that point where that becomes the thing that I want to sort of think about, we can look at stuff like that and say, like, okay, like, you know, what's going on in the short frames versus the long frames. Is there anything. Is there anything we can do? Like, can we like Pull them out and identify and sort of like, is there something like at the OS level and the code level, like what is.

**[01:04:09]** What is happening that's bumping us from one regime of the bimodal distribution to the other regime?

**[01:04:17]** I'm not gonna. It's good enough for now for me it's not. I'm. I always want it to be better, but I'm moving on because I. I've been doing camera. I've been writing this camera code for years now and I need to.

**[01:04:30]** I need to reach. It's ready to start making skeletons out of these. The. The pictures are good. We should start building skeletons.

**[01:04:45]** Yeah. Yeah.

**[01:04:55]** I don't really. I could connect to more cameras, but it tends to work better once they connect to too many. The front end starts to lag. I guess that's worth doing. I will shut this down, deselect the cam link because it's weird.

**[01:05:10]** That's the one that's connecting to this Sony camera.

**[01:05:17]** I should probably do something that actually notices when the cameras have disconnected. But don't worry about it. And down here. And let's go ahead and connect to.

**[01:05:33]** I'm not going to do the recommended thing because it can be. The recommend exposure thing can be slow, particularly when you're connecting like eight cameras at the same time when your computer is already being taxed by streaming and all that. But this should come in and. Oh yeah, I'm using B Show to connect. I could be using msmf, which is the Microsoft Media format.

**[01:06:03]** D Show has been working great for me in the past. I haven't tried the MSM, FMs, whatever, but it could easily do. So it's set up in the code. Do that. Okay, so that's probably going.

**[01:06:14]** And now I need to refresh the page because it's stupid. It doesn't notice. Hey, what do you know? Here we are seeing it's all dark because we knew that. We predicted that.

**[01:06:23]** And it's actually running. Actually it's really smooth.

**[01:06:30]** Do you love that? If you're ever running it and it starts to lag. So like if you move your hand and then the image doesn't lags, it doesn't start moving for a couple. For some time. Just pause it.

**[01:06:44]** And so what you'll notice is if you'll like wiggle your fingers, then pause it. If there's frame accumulation, your fingers will wiggle for a little while and then they will pause. And that means that you effectively cleared the buffer and you can restart it and you'll be back to good until it starts to accumulate again. But don't. Listen, listen, listen.

**[01:07:08]** Oh, my God. Jawa. You have now spoken one of my deep fears. To camels. To camels.

**[01:07:15]** In five generations. Yes, the millennials understand how computers work. Gen X and Gen Z, kind of. No, Gen Alpha, man. They're back to Boomer level.

**[01:07:26]** Like, it's, it's, it's brutal. They've been abused by web apps and Chromebooks, and I am taking as one of my personal mandates to try to fix this problem. The children, they yearn. They yearn. They want to understand it.

**[01:07:43]** They know that their lives are driven by the little magic rectangle. They want to understand it and they're primed to understand it. But they have been raised in a world of web apps and smooth buttons and login to do anything, and it has left. Like, I work at a high level research university and like, for any given room of undergraduates, there's going to be a good chunk of them that, like, do not functionally understand. If I say, like, download a file and open it, they're confused.

**[01:08:14]** If I say, if I gave them a keyboard and said plug the keyboard into the computer, they wouldn't know what to do. And it's not their fault, but it's our job to fix that shit. The children yearn for the nights.

---

### Chunk 8 [01:08:15 - 01:18:14]

**[01:08:15]** Gave them a keyboard and said, plug the keyboard into the computer. They wouldn't know what to do. And it's not their fault, but we. It's our job to fix that. The children yearn for the minds.

**[01:08:29]** They don't. They don't yearn for the mind. They yearn. They yearn. They just yearn.

**[01:08:35]** In general, like 10 Alpha 8, they're yearning. They deserve it. Gen Z, at this point, they need to start stepping up and helping out. But Gen Alpha, they still. They're the ones that really.

**[01:08:51]** They're the soft ones.

**[01:08:58]** MHF was asking about the algorithm to do the correct exposure settings. I talked about that a second ago. It's dumb. It's real dumb. It's in the code.

**[01:09:09]** So here we are in skellycam. Let's do a quick little jaunt. I don't want to do that. I'm going to hit Shift Shift and then search for recommended recommend. There you go.

**[01:09:26]** It's in here. Actually, I'm not sure if that's the code or some other code. It connects to the camera and then it just grabs images. It sets the exposure to each settings, grabs a couple images, measures the mean luminance, which is just take the average pixel value.

**[01:09:45]** I think I need to. I should probably deal with the color channels more intelligently. But it looks for the exposure setting that has a mean luminance of about half. So the pixel value is about 127.5. And then it recommends the exposure setting that's like.

**[01:10:04]** I think it's either one or two steps below that. It's dumb, but it works. It can be slow, but it does tend to work. Mostly it's like, really, if you're doing mocap, you want your room to be really bright. Like, stand in front of a sunny, sunny window, get some spotlights.

**[01:10:23]** Like, you want it to be really, really bright because you need there to be enough light in the room that when the camera opens its shutter for a short amount of time, because you set your exposure low, it gets enough light to register an image. And it's. The exposure is open for a short enough amount of time that you're not. That the subject is not moving significantly during the exposure time of the frame, because that's what blur is. The image is blurring.

**[01:10:56]** Actually, if I do this here, Like, this blur represents, roughly speaking, like, the distance that my finger traversed during the time that the frame was open.

**[01:11:15]** Ooh. Control of the. I spent a lot of my time staring into fun lights. Not as much these days, but, yeah, it's tricky. Yes.

**[01:11:27]** Yeah, yeah. I love like dumb smart. Dumb smart solutions are the best. It's like the elegance of brute force. You know, actually, since we're talking about it, let's give that.

**[01:11:40]** Let's. Let's see how we do. Let's. Let's give them a. Let's see how.

**[01:11:44]** Oh, this eight camera spread handles. Oh, wrong button. Don't. The big friendly button is the one that smushes.

**[01:11:56]** Hey, see, look. That time it didn't have to reset and it looks great. Mitchev asks, are you disabling auto exposure in the code or is that something you need to deal with manually?

**[01:12:09]** We are doing it in the code. So here you have manual, auto and recommend asterisks. The code configuration sets the exposure to manual or auto. Generally, I recommend manual because auto. The auto setting of exposure is almost universally too bright to be good for mocap because the setting is trying to make the image good for what we want to see with our eyes.

**[01:12:41]** But what we generally want to see is too much blur. So I tend to recommend just doing it manual kind of setting it that way. However, apparently the Mac AV foundation codec, like, I don't know if Mac allows you to do manual settings. I think it's always. I think it's always auto exposure, and I don't think that's unlikely to change.

**[01:13:10]** While we're still using OpenCV for a primary camera method, we're looking at other things like sort of like PI uvc. Oh, yes, this is. This is now lagged. See. So I was gonna say finish the thought before I do the thing.

**[01:13:27]** Yeah. So on. On Max it is apparently always auto exposure. So the manual stuff does nothing. So I think we'll probably be able to fix that someday.

**[01:13:39]** What other options do I have on Mac? I don't fully know what other like OpenCV has been. Has been a boon because it's just like, it's such a great little way to connect to cameras, but it's also like it's limited in a variety of ways. So I think the solution would be to go a layer deeper and look at like Lib uvc, which is closer to the metal, as they say. I might have to learn C. I don't want to, but even if I did LibGVC, I don't know if you could bypass the Mac sort of constraints.

**[01:14:20]** I think I'm also. I'm like, I'm relaying stuff that Philip has tried. So I do have a Mac, but I haven't really tested much on it, it's possible that it's like going. But we're talking about like the physically attached cameras because I think he was using a USB camera. I don't know.

**[01:14:41]** You know, we'll do our best to make everything work on every system but if part of the game is to say, hey, if you're on a Mac, you're going to get blur. So sorry, that's kind of the hardware, you know, we do what we can with what we got. And kind of the hope and part of. As I sort of said. Oh, it was.

**[01:15:07]** Oh, the lag caught up. Sorry. I was going to demo how to handle that but.

**[01:15:20]** Get bigger.

**[01:15:26]** Oh, I was also going to show demo recording from eight cameras. So. Yeah, but if you want to know about implementation details, stick around because I'm about to dive. I'm about to dive in but I'm going to. I'm going to demo recording from eight cameras to show that it works.

**[01:15:43]** So 5, 4, 3, 2, 1 and then record 1, 2, 3, 4, 5 and then what are they doing? And then close.

**[01:16:03]** So if you were paying attention, you notice there was more time spent in the plus and minus like around the start and end.

**[01:16:12]** Currently the way that the frame, the timestamps are saved is super inefficient and so for longer recordings like 5, 10 minute recording, the timestamp savings, it'll take like minutes. You have to wait and it's kind of. You just kind of have to like sit and wait and hope. I'm almost. That's mostly just because of the way that I'm calculating.

**[01:16:34]** It is stupid. This branch here, numpy timestamps, calculates them using numpy methods which once I have that working, which probably within the next couple of days, the timestamps will save like that. But you do get that. And look at that once again. Eight cameras, 205 frames, perfect frame rates and the inter camera sync has gone up to 453 microseconds median inter camera sync time.

**[01:17:08]** Don't we love that?

**[01:17:11]** Oh, oh, I guess it forgets the tag which is probably. Okay, I should probably check that auto increment thing.

**[01:17:21]** Oh, did we get the. Excuse me for a moment. I forgot to check if this works.

**[01:17:29]** So the recording gets that recording thing. It does not. Oh, that might be on that branch. We should be. This should have the more information in it with like the camera configs and some other route like the version of freemo, cap, scalicam, etc.

**[01:17:48]** Currently it just has this stupid. So the recording start of you know. Yeah, we'll figure it out. It'll save everything you need. And if it.

**[01:18:02]** If you ever find yourself saying, God, I wish that this piece of information wasn't saved, and I wish it was, just let me know.

**[01:18:11]** Talking about live demo luck angers the guy. That is true.

---

### Chunk 9 [01:18:00 - 01:28:00]

**[01:18:00]** It'll save everything you need. And if it. If you ever find yourself saying, God, I wish that this piece of information wasn't saved, and I wish it was, just let me know.

**[01:18:11]** Talking about lab demo luck angers the guy. That is true. I try not to say things about the cameras when they can hear me, but they're. They've been friendly. We have, we have.

**[01:18:21]** We've. I've been. I've been melding me and cameras. We're close. Like, we have a cautious understanding of each other's culture and I believe that we both have our best interests at heart, but they are.

**[01:18:33]** They're finicky little beasts, man. They got you.

**[01:18:41]** Okay, let's keep that up. And we're gonna. Yeah, yeah. Look at that. It's fun.

**[01:18:50]** So many cameras.

**[01:18:57]** Yeah.

**[01:19:00]** I believe if you are running skellycam, the thing that will cause things to start breaking, as Andres noticed, is the connection to the front end, like the streaming of the images to the front end. That's where the things will start to break first. And eventually I think it breaks so hard that it actually shuts things down, which is stupid. We really want to be protecting the back end and the front end should never break the back end because that opens up the possibility of something in the UI causing a recording to fail, which, as a scientist, the very possibility of that offends me at a deep, deep level.

**[01:19:51]** This code is like. It's as good as I could get it, which is far from as good as it can be. Yeah, I'm not a. I'm not a. I guess I'm becoming a front end guy. I see the power of front end. I aspire to it, but.

**[01:20:06]** And I'm kind of starting to wrap my head around the mental models around of Electron and react. Getting a little bit more familiar with Typescript and kind of learning what it is and is not good at.

**[01:20:22]** But yeah, you know how it goes.

**[01:20:32]** Yeah. So that's. So that's skellycam. That's how it works. It works pretty well.

**[01:20:37]** Oh, I was going to do the thing. Sure. Let's go ahead. Let's try. I'm not going to be able to get that running.

**[01:20:47]** I was going to say that I was going to try to build it, but it will certainly fail. Actually, let me try it like this first.

**[01:21:05]** Mhs have now discovered obvious thing. Is there a reason to have the preview always on? No, there is not. And absolutely there needs to be a button that just says shut off the display and let it run in the background. Maybe something like keep track of whether or not it's on.

**[01:21:19]** Something like that. There's a million million ways that that can be fixed. And mostly I'm just trying to get it to the point I felt like for me to feel like I could sort of like give this to the world and say, hey, here, this here's a tool that shows cameras in my head. Like it had to display the images to some level of fidelity. Otherwise it wasn't a complete product or a complete tool, I should say, I suppose.

**[01:21:46]** And now that it works, it's like I'm happy to kind of like make that a turn offable thing. But while I was in the development cycle, if I was wary about giving myself to too many outs like that because I wanted it to work.

**[01:22:03]** Yeah, but definitely being able to turn that off would like deload the system a lot.

**[01:22:13]** What was I going to do? Someone else?

**[01:22:19]** Yeah, so that's. Oh right, that's what I was going to do. I was going to try to build it and probably I'm going to see if the NPM build works because if it does, then this is fun. I can shut down the front end and the server keeps. That's another thing.

**[01:22:35]** The server keeps running when the front end shuts down. So currently those cameras are still connected.

**[01:22:42]** Oh no, it's not. Why did that happen?

**[01:22:48]** I don't know why that happened. Don't worry about it.

**[01:22:57]** I'm pretty sure this is going to give me a bunch of errors that I'm not going to be able to fix.

**[01:23:04]** Like I know how to fix them. It's like. But it's. Oh yeah.

**[01:23:13]** So the way that the. So one of the other main things that I really, really, really, really want for free. Mocap in general. Skellycam in general.

**[01:23:27]** Well, what do you know about that?

**[01:23:31]** Is a single click installer, Proper installer. I really, really want to get away from this world where installing FreeMap requires command line interface knowledge, where the first step of our instructions are create a virtual environment for Python. Like, you know, we've done a lot of work to make the installation process as easy as possible and I'm pretty proud of that. I think we've done a good job. But also it's, you know, if the software requires command line knowledge to run, that's going to.

**[01:24:04]** That's knocking off 80% of the world. Right? 90% of the world, 95 plus. Because of the thing we were just talking about. Like it's, it's intimidating and it's reasonable to be Intimidating.

**[01:24:14]** So, again, a lot of the effort around the 2.0 development is putting it into a context where we can have freemocap.org download and then you just click it and it runs in a way that people are accustomed to. Turns out that's really hard. Turns out that's a whole separate layer of complexity. Okay, cool, that worked. And so we've been using Electron in and it does a decent job.

**[01:24:44]** But there's the challenge of, like, bundling the Python. I used PI installer, but then it had issues with like, it would interact with. Apparently a lot of antiviral software just automatically nukes any PI installer executable. It finds it hasn't been signed. So I just, you know, let's deal with that.

**[01:25:05]** So I've been using this thing called Nuitka, which I think, okay, I'm going to see if this works. Cd. I think I want to do it from. No, no, I do it from here. I run it, I say go.

**[01:25:23]** And it doesn't like it because I move the icon. I'll do it later. Theoretically, I can now produce a skelechem installer that I could. If you have a Windows computer at this point, I can give it to you and you can run it on your computer and it should work. It's a little janky.

**[01:25:36]** I don't fully trust a lot of it. I can get the Linux and Mac stuff. Building it's just, you know, one thing at a time. But that's, that's, that's really exciting for me just because of the, you know, the core mission of accessibility is, you know.

**[01:25:56]** Yeah. Trying to make the most accessible software ever. Like step one is open a terminal and make a Python environment like, that's not accessible. It's, you know, we do our best. So that's not going to build right here.

**[01:26:13]** That's fine. Ok. Hour and a half in always takes so long.

**[01:26:21]** Let's get into the guts. We've done the demo now let's talk about, let's talk about sort of skellycamp's place within the. Sort of the general.

**[01:26:34]** The broader project of freemo Cap, Basically.

**[01:26:53]** So I can actually dot this whole thing. So, So I'm trying to think of how I want to present this information.

**[01:27:20]** So Free mocap at its core is intended as a scientific research tool. The fact that we have such a large artistic aspect to our community is kind of like, is like, you know, it's intentional and you are a. It's, it's like. And you're targeted. Like, I'M thinking about the artist animator users, but the, you know, the bar is much higher for standard for scientific software than it's for, like, animation tools.

**[01:27:53]** So by maintaining this. And I am trained as a scientist and I'm thinking about scientists and researchers, so I'm always sort of.

---

### Chunk 10 [01:27:45 - 01:37:44]

**[01:27:45]** Creator users. But the, you know, the bar is much higher for standard for scientific software than it's for like animation tools. So by maintaining this. And I am trained as a scientist, I'm thinking about scientists and researchers. So I'm always sort of thinking about it in that perspective.

**[01:28:01]** And you know, a scientific tool can be an artistic tool, but not necessarily the other way around. So we're thinking about it like that. So, So here we are, here's this. There's. So this is the hypothetical real world.

**[01:28:21]** This is a capital T. True facts. You know, there's a person out there in the world and we want to know about them. So we have these things. These are cameras.

**[01:28:39]** Cameras, cameras. These are three cameras and they are connected to your computer through USB connections. And these cameras are measuring the light that is sort of entering into their field of view as measured by.

**[01:29:08]** This weird little.

**[01:29:11]** One sec. Just sifting through the. All the camera sensors. I have ripped out of my cameras throughout my life.

**[01:29:23]** Yeah. So as measured by this small, maybe this network, this little wafer of silicone in the middle is a strange object who is created to absorb light and then record that light as voltage and then save that and send that to your computer. So, so the, the data comes in and I'll draw out the rest of this in a second. Actually, you might as well do it now.

**[01:29:57]** Camera, camera, camera. So you get person, person, person. Right.

**[01:30:19]** So the cameras are making the measurements, the cameras are doing the recordings. And so if you're thinking about, oh, I'm going to have an ad break in a second, but I'll talk until that happens. So if you think about freemocap as a research tool, as a scientific tool, an empirical apparatus that is designed to get accurate measurements of the world, those measurements are images. They're images from cameras which are sort of reducible down to patterns of voltage coming off of the camera sensors. And the voltage is.

**[01:30:49]** Has a law like relationship to the pattern of illumination in the scene that they are recording. So long story short, the Skellycam and the camera aspect of FreeMap, that's kind of the empirical basis. That's the source of all of the empirical data from which the rest of the thing will be calculated. And that's gone. It's gone.

**[01:31:08]** It's playing a commercial. So I'll pause until they come, until folks come back.

**[01:31:19]** Wait, is it playing? Am I playing? Does it tell me when it's done? I can never remember.

**[01:31:27]** I'll just putz around for 30 seconds.

**[01:31:32]** There's like a proper thunderstorm going on outside. That's nice.

**[01:31:39]** No commercial yet. Anyways, I'll keep talking. So, yeah, so the cameras. Then I'll talk about this. Nice.

**[01:31:50]** I don't know. It's like there's the constant warfare between ad blocks, ad blockers, and people trying to swerve ads. So I'm never sure where Twitch lives.

**[01:32:02]** It's always like, sometimes we do love U block. Anyway, so the cameras come. The cameras make the measurements, and then those go into, you know, processing, and then that sort of gets fed into skellyforge and then the output. The outcome is this.

**[01:32:27]** Is this sort of measured sort of person, right? And so this is.

**[01:32:35]** This is sort of the output data.

**[01:32:44]** Each camera its own thread, the keys camera is actually its own process. So you get that settable thing, but we'll get to that in just one second. So the. So within the sort of space of Free mocap, I'll talk about sort of the different work that's getting done in each level, but within this whole system, this part where you connect to the cameras, that's the hard part. That's the place where you're connected to the real world.

**[01:33:11]** It's the place where you're taking measurements. And it's the only place in the pipeline where if you get something wrong, you cannot redo it. Like when you get to, like, Skelly Tracker, which does the 2D tracking, or skelly Forge triangulation and cleanup, if you do something wrong, you can always reprocess the same videos over and over and over again. But if you miss a frame coming off the cameras, you can never get it back. So from a technical perspective, skellycam is both kind of like the spiritual heart of the code, because as a research tool, it is the point of empirical measurement, but it's also the place where, like, the constraints are the most.

**[01:33:55]** The most, I don't know, constraining. Like, images are big, they're large. An image is a large data blob, and cameras produce them even like a garbage cheapo. Webcam produces images at 30 frames per second. So if you're recording from nine cameras, eight cameras, even three, four cameras, 30 frames per second, 720p.

**[01:34:19]** Like, you can do that math. Like uncompressed. That winds up being like gigabytes per second. So you can do compression, you can do JPEGs. You got to be clever.

**[01:34:30]** But the main point of it is, like, in the development space, in the sort of spiritual heart and development space of FreeMap, Skellycam is kind of like the core. So a strategy that I have adopted in V1 and also now in V2 is when I'm thinking about building the larger process of free mocap.

**[01:34:57]** This whole thing is free mocap proper, rather than trying to build the whole thing at once. The strategy that I've been adopting is, the first thing that I do is, is I just built skellycam. I say I'm not going to worry about the processing and the reconstruction and all that stuff. I'm just going to pretend like the only thing that I'm doing in my life is building a tool that can synchronously record videos from cameras and now in V2 also stream synchronized images so you can do real time processing. But to start, I don't worry about those processing stages because it's already too damn hard.

**[01:35:37]** So I focus all of my attention building skellycam and then once scalicam is working, then I can attach the other sort of reconstructive parts that actually produce like the motion capture data.

**[01:35:48]** So skellycam kind of becomes like a microcosm of freemo cap as a whole.

**[01:35:55]** And yeah, so that's what. And so that's. So now at the stage of the development process that we're on, we're now at the place where I'm saying, hey, skellycam is now working well enough that I'm now going to start thinking about the rest of the process. And I'm not starting from scratch because I kind of, I tend to dive back and forth. You know, Aaron and Philip and Andres have obviously been working diligently to make sure that, you know, V1 is working.

**[01:36:22]** And like we got, it's, you know, SkellyTrack or SkellyForge are kind of like ready to go. But the event, like current, the state of the project now, like the big, I think sort of milestone event is that Skellycam 2.0 is now working well enough to produce the kind of real time motion capture data that I really want for V2, while also maintaining the fidelity of the staged pipeline that we currently have. Because if you're doing a real time processing pipeline, you're always going to be constrained by whatever computer you're on. And if you're doing 30 milliseconds, 30 frames per second, then a 30, 30, you have 30 milliseconds of processing time per frame. That's very, very constraining.

**[01:37:11]** So a big part of the strategy is like making sure that it's producing synchronized images at runtime, but it is also always saving. Well, if you turn the recording on, always capable, I guess I should say, of saving every image to disk so that you can. You can always go back and then reprocess what you were getting in real time with turning the speed accuracy knob all the way from speed during real time to accuracy during post hoc processing.

---

### Chunk 11 [01:37:30 - 01:47:30]

**[01:37:30]** You can always go back and then reprocess what you were getting in real time with turning the speed accuracy knob all the way from speed during real time to accuracy during post hoc processing.

**[01:37:48]** Yeah. So let's talk guts. Let's get into the guts of it.

**[01:38:00]** So first of all, so core architecture, we have the backend server, backend server process, which is python Specifically running fast APIs doing most of the work there.

**[01:38:27]** And that's the part that's actually connecting to the cameras. When we get into the actual proper free mocap, that's where the processing is going to occur. And then we have this front end client UI user interface, and that is the Electron react typescript.

**[01:38:52]** And the two systems communicate with each other through an HTTP, you know, HTTP, HTTP endpoints to issue commands. I guess I'd be going this way, wouldn't it? Connect to cameras or change the settings. Those are all going through HTTP endpoints to ask for the front end client server UI to request the server to do stuff like connect to cameras, the data for the images and then later for the rest of the data. The real time streaming data is being handled through a web socket.

**[01:39:46]** Whoa.

**[01:39:49]** Thunder, Thunderbolts and Lightning.

**[01:39:53]** And so the images are coming in through the websockets. This part right here, that's the main. Including video. Yes, I'm streaming the video through a websocket. It's not the right way to do it, but it's the way that I could get to work.

**[01:40:08]** I know that there. I'll get to that in a second. Currently, yes, the video is streaming through the websocket. As I make a jpeg, I compress the images to JPEG and I put them into a byte array. It's like a whole dumb thing.

**[01:40:27]** It does the job, but it's not the right solution to the problem. There are many other ways. And this is all being done through local host. So we're doing kind of web dev styles of 1 second, 1 second on that. So we're using the network card, which is kind of good for convenience, but it's also kind of stupid because it's all local on the same machine.

**[01:40:58]** So there are ways to share the data that would just. That wouldn't have to hit your network card. That could be much, much faster. And there's also methods, MHF pointed out, WebRTC, there's many other et ceteras that are optimized for video streaming that are much, much more efficient than what I'm doing here.

**[01:41:23]** The disadvantage of those other systems is That I could not get them to work. I was able to get the websocket working pretty well. And the websocket, I should say this part is the bottleneck, but it's not, it's not that bad. It does the job, I think for most people's machines you should be able to stream, I would probably say up to like six cameras without too much issue, six 30fps cameras. But ultimately, as Andres noticed when he tried to hook up the 120fps cameras, it bogged down in the front end.

**[01:42:00]** And that was the thing that wound up killing it. So I think I spent more time than I could possibly express trying to come up with other ways of sharing the data that would stream like that would be more efficient. And this was the most reliable system I was able to get working. I dream of better options, but I also know that I should. I need to move on.

**[01:42:30]** Is WebSocket based on TCP? I believe it is TCP. I have also tried UDP. Yes, yes.

**[01:42:42]** And just. Yeah, UDP I think is probably the low, but then it's like you're limited. Like they can only send 65 kilobyte pack the whole thing. On Skellycam, if you look at all of the branches, there's development, there's numpy timestamps which I'll get done. There's also rerun lmdb like memory mapped database I think is probably the fastest or memory mapped file swap I think is probably the fastest way to share data since it's on a local machine.

**[01:43:14]** 0MQ I think could work. WebRTC, I tried WebRTC and GRCP, I have tried both of those and they are optimized for this. The main issue with those is that they're so complex for a local host solution because a lot of what's happening with WebRTC and GRPC is it's got this whole thing about these security layers and these folders fallback servers like stun or whatever the hell is going on there.

**[01:43:45]** And it's designed for like streaming over the web. So trying to set that up for a local host connection is like. It was just, it was a nightmare and it, I would assume it would run better because it's like GRPC or whatever. Like they do like codec stuff under the hood. Like they do compression and like, you know, if you're sending the same image over and over again, like you don't need to send the background every frame.

**[01:44:15]** You, you know that, that type of stuff. And there's all those optimizations like happening and available through those other methods, I just wasn't able to get it set up. So I, believe me, believe me, I tried. And it's mostly it was just like outside of my wheels, my wheelhouse, like I'm just not familiar with it. And eventually I just decided I had to make the call and kind of like live like the websockets are like totally good enough and I needed to move on to other parts of the project so we can actually have the whole thing going.

**[01:44:53]** And my assumption, and my hope is that members of the community could probably help out, especially if you're a person who's dealt with WebRTC, if you live like front end web dev kind of lifestyle, if that's more of a familiar domain to you, you would probably be able to get things working that I was not. Pretty much everything you see on the front end was me communing with the machine. It's not vibe coding per se because I definitely, because the vibes were bad and I definitely went through and did cleanup. But I'm like very much operating above my level at the front end stuff because I'm being power leveled by the fact that AI is really good at designing front end code. Like, it knows React, it knows web dev, it knows web dev probably better than Python.

**[01:45:49]** But also when I was building the server in Python where I did know things quite well and I was optimizing things down to that like millisecond scale, it was obvious to me that the, the bot was not producing like the bot cannot produce Python code that's better than I can write. It produces bad, I would say not bad, good enough, intermediate, amateur level, talented amateur, but regularly made mistakes that I was like, oh, that's super inefficient. Oh, that's super inefficient. That's super inefficient. In the Python server code.

**[01:46:26]** I can recognize those points and I can, I just don't use AI to write that code. On the React side, on the front end with React and TypeScript and Electron, because I'm unfamiliar with it, I am not able to correct its mistakes in the same way. I am now, over the course of developing skellycam to this level, I am now getting to that point where my mental model of React and React and Electron specifically have been like a whole headspace.

**[01:47:01]** Let me do it. I was trying to get this running again.

**[01:47:07]** Yeah, I'm starting to like speed things up and make things more efficient, but I'm certain that there's just like that for people who have like the same level of expertise and front end development that I have at this point in like back end number crunching would look through my front end code and be like, oh, this is hot garbage. You should, you should probably remove some of this hot garbage. And then I suspect it would then.

---

### Chunk 12 [01:47:15 - 01:57:11]

**[01:47:15]** The same level of expertise and front end development that I have at this point in like back end number crunching would look through my front end kind of be like, oh, this is hot garbage. You should probably remove some of this hot garbage. And then I suspect it would then run, you know, significantly better. Outside of the strong possibility of someone just being like, oh, here's how you set up your GRPC local server and then here's how you can do your LMDB memory mapped database and then do, and then get things better. But these are kind of like efficiency improvements that I think should not.

**[01:47:57]** One of the rules of like don't waste your time, don't waste your time optimizing something that already exists when you're over creating something that doesn't exist yet. We can come back and make the cameras work better once the whole pipeline is working.

**[01:48:20]** Also just in general, a part of this phase of the project is me trying to get better at communicating the needs, the things I need help with. That's what these streams are about. Then also we're going to be generating some combinations of AI assisted and manual methods of chunking out these long form recordings into smaller pieces and then having GitHub issues and stuff like that with the tasks and the constraints. Because it's a lot to ask to just say hey, dive in and help. That's not a reasonable request.

**[01:48:52]** But if I can put a lot of notes and make a discussion area where it's like camera efficiency discussion, then we could, we could have a conversation in that space that would be more helpful because I know there's a lot of people in the general vicinity of this project who really want to help and I, and I, I deeply appreciative of those of those types and really trying to be like, trying to create an environment where that help is sort of possible to receive because there's, it's, it's difficult to make alignment when it's an asynchronous distributed project. So what was I doing? I was running this because I wanted it because I was already running.

**[01:49:42]** Don't open two of them and to do record, no connect. Turn you off and connect. Yeah, thanks. I also think it sounds like a plan. It definitely resembles a plan.

**[01:50:01]** It's interesting, you know, like you get to a certain point especially, especially I think in open source life. Once again pitching this book Working in Public by Nadia Egbal the Making and Maintenance of Open Source Software. The there that's lag.

**[01:50:21]** Oh no, it caught up. Nope, didn't.

**[01:50:28]** Okay, so there I'M swinging. I say pause. It keeps going for a while until it claws lag. Now it's actually paused. And so now if I hit resume, the lag is gone anyways.

**[01:50:42]** You get it. But yeah, at a certain point it becomes like community management, like that's. That becomes the hard part, ceases to be writing the code. It becomes like managing, learning how to accept help, learning how to leverage a supportive community in a way that is like mutually beneficial for everybody. Because you know what I'm saying?

**[01:51:07]** Okay, so I wanted that little thing in the corner to be going and now it's going to. How we doing? How's my brain? Almost at two hours, which means that mental reserves are dwindling. But we're doing fine.

**[01:51:25]** Let's talk about the code. Let's get into the nitty gritty. This is the larger architecture, I guess let me go from the front to the back, which I think is recommended in most context.

**[01:51:42]** So in webstorm.

**[01:51:47]** No webstorm in Skellycam ui where the code mostly lives.

**[01:51:54]** I'm not going to talk too much about the electron side because it's not too much happening there, but in the source code. I'll start with the websocket. The websocket might want to be running in the main function. Moving on. There's also.

**[01:52:13]** There's an RTK data store, but where are we here? So in context. WebSocket context. Use WebSocket. Hook.

**[01:52:24]** See hook goes react. React has hooks.

**[01:52:30]** It.

**[01:52:33]** Yeah, it receives the images, they've been unraveled into a one dimensional byte array which gets processed and chopped up and then put into state and then that gets eaten by the components and displayed.

**[01:52:55]** Great.

**[01:53:00]** That's the front end, more or less. Let's talk about the back end.

**[01:53:18]** In the code. If you really wanted to trace it out, you would start at the double underscore main and look at how it opens up a UVicorn server which is what's running the code. I guess I can show you from the logs it starts the server, starts listening on threads, adds all these routes.

**[01:53:47]** Then the server becomes available. It connects to the websocket and then starts waiting for requests. And the main request that we will care about here, aside from the camera detection, which is interesting in its own right, is in Skellycam in the code, this folder called API that's handling most of the API connection, the HTTP, the WebSockets, I guess the server I put in here, which the. Yeah, anyways. Chorus Gotta do chorus.

**[01:54:25]** Always gotta do chorus for Whatever reason. Do the little chorus song and dance and. Yeah. The HTTP and the cameras and the camera router and the. This one.

**[01:54:46]** Yeah. Camera group create. That's the guy that actually connects to the web. It creates the camera group, which is a synchronized group of cameras. Currently it's really set up to just have one camera group, but I'm trying to make the architecture aligned with having the potential for multiple camera groups running at the same time.

**[01:55:13]** So. So you might want to have like face cameras, you might have eye cameras, you might want to have like, you know, maybe you have fast cameras and slow cameras. You want them to both run at their own frame rate. Currently, a camera group will.

**[01:55:29]** It will run at the rate of the slowest camera in the group. So if you have three 60fps cameras and one 30fps camera, if you put them all in a group, that camera group will run at 30fps. For reasons which shall become apparent soon, where everybody go, oh, Yeah, and.

**[01:56:12]** I think I. I had aspired to like, oh, I might still draw some pictures. We'll see.

**[01:56:18]** Yeah, I'm going to draw some pictures because here's the code in, you know, camera group. And then we go into get skellycam amp, which is a singleton. And then you go into Control B into the group and. And then this is the scalicam application and it sort of queries a camera group manager.

**[01:56:44]** Yeah, the API. The cameras API is doing a lot of like, CRUD operations. So create, read, update, delete, destroy, and camera groups are handled with CRUD operations for the most part. You can you. Except for read, whatever.

**[01:57:06]** Yeah, we create. Start the camera group. Oh, yeah, there's a whole.

---

### Chunk 13 [01:57:00 - 02:06:59]

**[01:57:00]** Part you can you. Except for read whatever.

**[01:57:06]** Yeah, we create. Start the camera group. Oh yeah, there's a whole.

**[01:57:17]** Hub sub network.

**[01:57:21]** What did I say I was going to talk about general architecture. We can talk about that. We're not going to talk about what we talked about the install. We're not going to do anything with it. We're going to talk about the camera group and then we're going to come back and talk about the IPC including the pub sub network and the shared memory.

**[01:57:39]** The fancy shared memory ring buffers, the real stars of the show.

**[01:57:48]** I'll show you the code, then I'll draw the picture. Camera group is an object you call create on that which gets created from the camera configs that you're going to connect to this global kill slack. I'm going to use this as a moment to talk about. One of the challenges here is making sure everything dies properly because there's a lot of sub processing. Someone asked if they're running in a.

**[01:58:15]** They're all running in threads for the most part. They're all running in processes. So it's. I'll show you in a second. There's a toggle in there that will say run in threads versus run in processes.

**[01:58:29]** They work okay in threads, mostly because the scheduling is very careful. But each camera loop is reading from the camera, which is a blocking operation, and saving to disk in the video, which is also a blocking operation. So with multiple camera loops running, one of the nice things about splitting up the frame reading between the grab and retrieve steps is the grab is not blocking. So the grab can happen without blocking anything. But once you start trying to like.

**[01:59:05]** I don't think retrieve is necessarily blocking, but it's very CPU heavy, which I think I have also not played around with like the GIL free versions of Python. I don't know if it would be helpful for us here, but for the most part I'm like. Because the camera loops are all running, I guess I'll start drawing a picture. If you have camera one, camera zero, camera one, camera two and each of these is doing its work, you really want to be careful to make sure that they're not going to be blocking each other. And.

**[01:59:44]** And that because the nature of a camera is that as the images come in, if you don't request that frame when it's available, it's gone.

**[01:59:55]** So a little hiccup of 30 milliseconds or more is a dropped frame. So a lot of the complexity, obviously probably the majority of the complexity in skellycam is based around both protecting the camera loops by putting them in processes so that they don't get blocked by other things, and also just being careful with the scheduling of when they do the frame grabbing and stuff so that they're doing that frame grab in a synchronous way and that you're not finding yourself in a situation where one camera is trying to read while the other camera is trying to save to disk.

**[02:00:39]** Yeah.

**[02:00:45]** And so because of all these protections that we're putting in to the camera loops, another good chunk of the complexity is trying to make sure that they die properly, that if, if something crashes, if you shut down intentionally, that you're not left with these free running camera processes that persist until you restart your computer. For the most part that's handled with demon processes because they die when their parent dies. But there's a lot of loops. There's a lot of loops in a lot of places. And you're not asking stupid questions.

**[02:01:25]** Oh, hello mhf. You are not asking stupid questions. I appreciate you. You can't create a camera capture class that's responsible for grabbing the frame and finding the buffer to another thread to grab the current frame buddy.

**[02:01:43]** So there's someday, someday there will be a whole, there will be a whole like narrative conversation of all the different stuff stages of skellycam that have come through from the first time I figured out how to connect to the cameras to V1 to V2, to wherever we are. Now, what you have just recommended of just capturing the image and then passing it to another thread, I think that's actually what V1 runs on. It works okay, except that step of passing the image to another thread, you start hitting inter process communication costs. Now you're trying to move a large amount of data at a very fast rate from these very sensitive camera loops into some other place that can do the streaming and the recording and whatnot.

**[02:02:45]** And so now you start dealing with other bottlenecks of basically the cost of sharing information between threats, which is actually a great segue into talking about the PUB subnetwork. I'm not going to say too much about it. I'll show you where it lives.

**[02:03:04]** Skellicam, the core of the Python code API, handles the communication between back end and front end app, handles the lifespan of the application itself. And Core is where the real work is being done. In Core you have camera, camera group, frame payloads, IPC recorders, types, IPC interprocess communication. There's this pub sub guy right there.

**[02:03:36]** MHF is being very what's the word clairvoyant. I don't know. You're seeing what's coming. Shared memory is in fact the name of the game there. So the Pub Sub network was directly ripped from.

**[02:03:54]** I mean, it's not directly ripped, but it was inspired by ROS robotic operating system Puff Machine in the server. Good old Puff was playing with Ross and he was like, oh, they have a really cool like Pub sub network publisher subscriber pattern that they use to share information.

**[02:04:17]** And robotics are systems engineers in a very similar way to way free mocap is. A lot of my sort of scientific background is from hanging out with legged robotics researchers. So the Pub subnetwork is a really great way to do asynchronous message passing and we use it a lot for. It's like a series of basically queue objects to share messages. So that's how we do things like starting and stopping recordings, sharing camera messages.

**[02:04:51]** That's how I do mainly communication between the. All the different processes. But a multiprocessing queue, it just cannot handle image data.

**[02:05:05]** It's too much data. It's not fast enough and it slows down, particularly on weaker computers with higher cameras and higher frame rates and stuff like that. You could handle that by compressing the images to JPEG strings. But then you're kind of. You're making the problem better, but you're still dealing with pickling is the cost there.

**[02:05:27]** In fact, the solution to that problem is shared memory. So in the ipc, there's the Pub Sub network, which is a fairly, I think, standard approach to making the publisher subscriber pattern. Heavily, heavily inspired by robotic by the ROS2 pub sub pattern. And then there's another guy named shared memory. And arguably this is the reason why the whole thing works.

**[02:05:59]** And basically it's a fairly complicated process of basically making these shared memory ring buffers. I'm not going to go into the code because I don't think it's as illuminating as it could be. But basically the idea is.

**[02:06:22]** So let's just go over here. Here's a guy, here's cameras.

**[02:06:32]** They feed in to.

**[02:06:41]** Yes, do it like that. So camera zero, camera one and camera two.

**[02:06:55]** That guy is counterclockwise. No, they're all kind of clockwise, right.

---

### Chunk 14 [02:06:45 - 02:16:45]

**[02:06:45]** Zero.

**[02:06:48]** Camera one and camera two.

**[02:06:55]** That guy is counterclockwise. No, they're all kind of clockwise. Right. And so these are the camera objects running by a cameramanager. And then each of these little guys is a camera object.

**[02:07:17]** And yeah, these are the guys that are running. Camera workers, I think is the better term. And they are running in either a process or a thread, depending on your setting. Default is that they're all running in processes and shared memory. If we wanted to, let's say that we have the thing handling the websocket here that wants to send the data off to the front end.

**[02:07:47]** We have to get the images from the camera processes to the websocket. We also have to get the data to the disk to. These represent video files in a previous version of this world that there was like, they fed in. This is kind of what you were recommending of, like, the images were feeding into like a separate recorder process. And they would sort of feed the images in and then they would.

**[02:08:18]** The recorder would save it to disk. But then you have another. You have a bottleneck because the recorder is now being asked to save images to disk very fast. And if you have. And the load on that recorder worker, it scales with the number of cameras.

**[02:08:36]** So if you have, you know, let's say you have 30, you know, 30 FPS cameras, so 33 milliseconds per frame. Let's say it takes 5 milliseconds to save something to disk. And then now you have a maximum of six cameras that you can save to disk before the time that it takes to save sort of. Of passes that 30 millisecond cap. And now the recorder is starting to accumulate frames.

**[02:09:02]** And now you get into a situation where basically like, as the recorder would go on, you would get memory accumulation and it would fill up your RAM and then eventually crash your computer. And that was the original plan, was to handle that like that. And you know, having. Trying to be clever about saving and timing. But the nice thing about the fastidious approach to timestamp logging that I have is it allowed me to see actually how long does it take to save an image to disk.

**[02:09:34]** I didn't know. And now I can look at those values and I can see, oh, actually there's time inside of the camera loop to save to disk. So now the camera workers handle recording to video. So now that saves us from having to send the images on and have that reporting worker bottleneck in that whole business.

**[02:10:06]** But the. What is saying. So shared memory. Remember we were talking about shared Memory.

**[02:10:16]** So in Python land and sort of most other places, like a process or a thread or whatever, you're thread in the C sense, not in the Python sense. Process in the Python sense, not in the. Everyone uses different languages, but software often operates in the space of like one second. How did the process deal with I O slowdowns, EE slow hard drives? Would that lead to degradation to capture?

**[02:10:45]** So the. So eventually, yes, basically asking how does the cameramanager handle the possibility of what if your computer can't save to disk fast enough? The answer is that eventually it would lead to frame rate drop at the back end level.

**[02:11:12]** It would still work, but it would slow down and you would see that, okay, I need to stop streaming from eight cameras. Because that is speaking of accumulating problems, I was trying to show off, you know, so you would, you would see the. So my general rule of thumb, and it's a rule that I. The thumb that I would recommend for you. Okay, shut up.

**[02:11:44]** Shut down you4 cameras is respectable. I think we should all aspire to like in my mind I'm trying to make something that would be able to run three cameras on almost any computer. How we want to define almost any. You know, one of the beauties too is with the diagnostics that we're getting here, I'm hopeful that we'll be able to free. Mocap currently has a thing at the front that's like, please do you mind sharing anonymous user data or whatever.

**[02:12:27]** I think we can. I want to make that more robust and give users more control over what they share. But one of the things I would like to be able to request of users are those diagnostics plots. Like something that's like, hey, here's a snapshot of the computer, here's the hard drive, whatever the system thumbprint that you can get that says here's how many, process how many cores, here's how maybe we do a little loop or save something to disk and read it to disk and get some diagnostics from that and just get data streaming in from the user base that is telling us how the software runs on the panel plea of computers that are running this thing. I said this last time but you know, from that the user, the user settings that we get.

**[02:13:26]** We have received at this point checked in a couple of days. At this point it probably is 8,500 unique users since 8,500 unique IPs of all the people who did not uncheck that box since March of 2023. So it's like approaching 9,000 unique users probably. I mean the real number is larger than that. And this is the exciting part.

**[02:13:52]** The pings have come from. Last I checked, I think like 130 different countries, which is so cool. And you know, a lot of those countries are not. Are the kinds of countries that don't make you think they don't scream high computing power. When you look at the names of some of those countries they, they scream like, like who knows how old.

**[02:14:17]** Like who knows how old the computers that are running Freemo Cap are. I would, I would bet that somewhere out there in the world it is running on some busted ass machines. But it does the job. That's the goal of freemocap is that it should do the job on whatever machine it's on.

**[02:14:37]** Which is why the efficiency thing in my mind I'm trying to target something that would work with three cameras on most computers and then efficiency from there.

**[02:14:51]** 193. Yep, 100. I should, I don't want to, I don't want to like look up the numbers because it has IP addresses in it on the stream. But it was. I think it's like 132.

**[02:15:02]** It's. We're definitely running out of countries and you know, the majority of the countries that have not been hit are from Central Africa and stuff like that. But like every time I get like a new one it's always like, oh my God, someone used it in. You know what we got recently? It's like not Uganda.

**[02:15:24]** We got Uganda a long time ago but it's like small Central African nations. Yes, Skelly is coming. Skelly is coming to take. To take over. Skelly is here to help.

**[02:15:36]** But yeah, so I'm always trying to think about those folks. Like realistically I'm thinking about them. If you have like a decent gaming rig, I'm not worried about you, you'll be fine.

**[02:15:54]** I want a person with a decent gaming rig to be able to record from six cameras and if you have a powerful computer then you should be able to record from nine. But this is part of the universal design mandate. Then the real time processing is going to be a whole extra conversation. But the part of the, part of the main big aspects of the.

**[02:16:25]** Yeah, great segue into real time processing. So in terms of. Yes, like freemocap as like a scientific research tool. The critical thing is like the strength of the v1 code, the one that's currently like the.

---

### Chunk 15 [02:16:30 - 02:26:29]

**[02:16:30]** In terms of freemocap as a scientific research tool, the critical thing is the strength of the v1 code, the one that's currently the production code, I guess, is that it records to disk and then processes and then produces the data in this nicely staged pipeline. With that you can guarantee that you are processing every frame and that you can crank the knob. In terms of what size of model do you want to use, how much cleanup do you want to do? You can do types of cleanup that require you to have the whole data set available at once.

**[02:17:19]** But you push the button, you walk away, you come back later, you got your data. That's good, that's kind of. That's a pretty standard model. And as I desperately try to build a real time processing capacity, I am not willing to sacrifice the ability to do that offline staged processing. And I am not willing to have a real time processing option that might.

**[02:17:45]** Well, that might is a hard is a might is not a big word. But I am prioritizing that every camera should save every frame to its accordant video file because that way you can always process and reprocess these files on your own. If you have a wimpy computer, it might take you a long time, but you can get the data out and it will be caveat, caveat. It will be like this. You will be working with the same data that I am working with as a professional research scientist with the powerful computer.

**[02:18:25]** It just might take you a longer time to get it.

**[02:18:34]** That is maintained. But we do want to have a real time processing output. We want to have that for a lot of reasons. We want to be able to build interactive stuff. We want to be able to do VR, we want to be able to do all sorts of fun things.

**[02:18:46]** For me, again, thinking about it from the perspective of a researcher, streaming live. Yeah, live performances, right. We definitely like a lot of cool folks doing really cool like live demos and live performances. And something coming in live is key. Again, for me, thinking as the perspective of a research scientist and someone who trains students and bright young minds of future, future tomorrow, a tool with a real time output will yield wildly different workflows and wildly improved workflows.

**[02:19:24]** If the time if like the feedback loop necessary to see the effects of different settings, different camera configurations, different lighting. If that feedback loop is effectively zero, it will just elevate everybody's recordings. Like and it's. It's hard, I think to quantify how much the whole project will improve if there's a real time output. Because like I talked to Some scientists, and they're like, why do you even want real time?

**[02:19:52]** Like, like you don't. You don't need that. Like, that's not really helping anybody. And it's like, I promise you, everybody will do a better job if it has real time output because they'll be able to get better at it faster. Right now our workflow is slow.

**[02:20:06]** You have to do the recording, you press the button, you twiddle your thumbs, the data pops up. It's good or it's bad. And then you have credit assignment. It's like, why is it good? Why is it bad?

**[02:20:16]** There's credit assignment. That whole loop took 10, 15 minutes. If we can get that down to 150 milliseconds, whole different world.

**[02:20:27]** What we do is we want to have a way of getting. Maintaining the sanctity of the frame loop, maintaining the sanctity of the video recording, but also with what time is left. Also wanting to provide the world with real time processing. We use shared memory buffers. Where's my brain at?

**[02:20:55]** 220 out. 220.

**[02:21:02]** We use shared memory. Shared memory ring buffers. So what? A shared memory. So what shared memory is, is if you think about, you know, this is, you know, this is a process camera one, you know, it's.

**[02:21:15]** I guess it's n two processes to run Skellycam, where n is the number of cameras, because you got the main process, you have one process per camera. And then we have one additional process for basically the multi frame builder, whose job is to listen for available frames and then port it to the websocket. And then currently it just sends it to the websocket, but will eventually go well through the rest of the processing pipeline and then get you real time.

**[02:21:53]** And yeah, so in general operation, real time, lots of times we're coming from vmc. VMC Protocol, vmc. I have not heard of those. Is that a real thing or is that. Is it fmc?

**[02:22:14]** Are you saying fmc?

**[02:22:21]** Oh, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah. This one, I know this guy. Virtual Motion Capture Protocol. I've heard of this. There is an emerging protocol around streaming MOCAP data, and it's in my mind, I had forgotten about it.

**[02:22:41]** But thank you for. Thank you for that. I will keep in mind it's a protocol. So it's the kind of thing that it's like a set of rules about what the format should be. And so once we get to the point where that's a thing.

**[02:22:58]** Absolutely. I will try to make it align with that. I will look into that later. Thank you for reminding that.

**[02:23:08]** Reminding me of that.

**[02:23:13]** Yeah, I looked into this a little while ago. I wonder if it's changed. It's like six months ago, maybe not even.

**[02:23:19]** Yeah, so, right, so normally normal operation is that each of these processes. So the main process, camera processes, this multi frame builder, is also its own process. They have their own kind of like memory space and ipc. Interprocess communication is basically like the general vibes of the challenges of moving data from one to the other. So in Python the standard approach is to use like pipes and queues, but then you have to pay pickle prices which where things slow down.

**[02:24:02]** So shared memory is. Is this really cool thing where you can basically tell your computer to reserve a certain section of your ram.

**[02:24:17]** Basically you give it a name and then that memory now becomes shared. So each of the processes can sort of access, read and write from that same shared memory space and interact with that memory as if it was the memory in each of the processes. The advantage of that is you no longer have to do any pickling or any weird serialization or things like that. You can basically treat that memory object as if it was local to each of those little sub processes. And then you still have to deal with the fact that images are big and copying an uncompressed numpy image can still take countable milliseconds.

**[02:25:14]** But it is said to be about the fastest way to do IPC within, particularly a Python environment. Other languages have more or more options, but so, Yeah, and so what we wind up doing. I'm also not going to talk too much into the details of some of the wacky nonsense I'm doing with numpy record arrays. There was an earlier form of this. What are we doing?

**[02:25:54]** An earlier version of this project where I was relying in retrospect too heavily on.

**[02:26:09]** Brain. Brain exists on pydantic model. So I was using pydantic model everywhere, which are great because you get all this nice validation and sort of helpful for development, but they wind up being slow because they're doing all sorts of validation, resizing the image, also a thing that gets done.

---

### Chunk 16 [02:26:15 - 02:36:13]

**[02:26:15]** Models everywhere, which are great because you get all this nice validation and sort of helpful for the development, but they wind up being slow because they're doing all sorts of validation.

**[02:26:27]** Resizing the image, also a thing that gets done. One second, let me talk about that.

**[02:26:35]** So passing the data around as a pydantic model is slow. And so you could just pass it as I was doing something too, where I was sending the images through shared memory and then the metadata, like the timestamps and the frame number through pipes, and then you have to line them up, and that was a whole pain. But then I discovered this is one of these things. This is an AI. One of the things that happens when you're using AI for a lot of a lot is you hit these points of unknown, unknowns where you won't even be asking for something, but it'll just mention something in passing.

**[02:27:18]** It's like, wait, what the hell? What was that? I've never even heard of that. And that happened to me with these numpy record arrays, because I'm used to using NumPy ND arrays, like tensors, you might call them.

**[02:27:32]** And then I had a bunch of wacky nonsense for converting the metadata into a numpy array and then reading it back out. But then I discovered that you can define a D type and then define a record array, and then you can basically use dictionary notation, or in this case, dot notation, to have complex objects shared with numpy speeds. These are very, very similar to a C struct, if you're familiar with those.

**[02:28:11]** And it allows you to send more complex data while still this align equals true. This is all contiguous in memory, usually in Python, because Python is not optimized for speed.

**[02:28:30]** If you have a dictionary or a pedantic model, the data for that could be spread all out through your ram. So every time you want to access it, you have to kind of like you have to pull it from a bunch of different places at once. When data is contiguous in memory, it's just one big block. And so you can just grab this whole block and know that it's going to be the data that you want. So wind up building to do.

**[02:28:58]** The Python is using boxed values. I don't know what that means. I will look it up.

**[02:29:10]** Boxed values. That seems like that sounds like something Python would do. I should look that up. Like, I'm getting closer to the metal every day. Someday I'll learn how to write Rust code and be a real cool guy, but today I flop around in Python land.

**[02:29:33]** But yeah, so the shared memory objects we have, they're defined as an array of a certain size that can hold for the cameras basically a frame image plus metadata in an array.

**[02:30:00]** The cameras basically put data into the array one at a time and then when it gets to the end, it just loops around and starts overriding. So it's a ring buffer. So the camera objects all have their own individual ring buffer and they're putting the data into that buffer. And then they have to basically have.

**[02:30:33]** Let me draw it, I've drawn this before. So camera, camera, camera goes into, don't need all that.

**[02:30:45]** Camera, camera, camera. So these are the camera objects and then there's this kind of shared memory blob. And then each camera has its own shared memory ring buffer that it's feeding into. And then you have another process if you so desire, who's out here, which is this is like the multi frame builder.

**[02:31:25]** And this guy is.

**[02:31:31]** Basically looking at the latest images available in each camera's individual buffer and then saving them to yet another ring buffer who holds multi frame objects.

**[02:31:51]** So the camera share memories hold individual frame data. The multi frame shared memory contains sort of synchronized image blobs. And so that's. So the images on the front end over here, those are being fed out of. Those are being pulled out of these multi frame blobs.

**[02:32:17]** And now so critically, critically. Oh, we're doing an ad. We're doing an ad. It says we're doing an ad. I don't know.

**[02:32:30]** Oh, wait seven seconds.

**[02:32:39]** Images copies are referenced.

**[02:32:44]** I try to be. So is the image copied to reference? I try to be mindful about doing the right one. So minimizing copies using reference as much as possible. Sometimes you need some operations require a copy.

**[02:33:03]** When you're putting the data into the shared memory, it has to be copied. If you're doing other stuff, you don't have to copy it. I try to be careful about that.

**[02:33:14]** Minimizing. Yeah, like keeping track of how many copies occur and try to minimize that number.

**[02:33:23]** So yeah, so the data that gets saved to the shared memory buffer very critically when you're doing something with these kind of ring buffer type of objects. So you have a ring, you have a ring. Got ring, ring, ring. And let's say that you're putting stuff in piece by piece and then somebody else over here is like looking at the data. There's a very important distinction between the, between a process that is trying to read every single thing that comes in and something else which is just trying to pull the latest data data at the time that it looked.

**[02:34:10]** So I guess in an earlier version of this code where there was a secondary recording object that was doing the recording, the recorder would do a read next operation which would guarantee that the recorder would see every frame. And it's not going to skip frames. These days, now that the cameras have started handling their own recording, that's actually not. We don't actually use a read next operation. And the process, I can't remember, but the websocket, like the front end, it's doing read latest.

**[02:34:48]** So read latest doesn't care if it gets every frame. It just wants to know what's the most up to date data that's available at the time that I asked. That becomes very. So that distinction between reading every single frame and only reading the most up to date data is really important as we start thinking about real time processing. Because if we think about the images.

**[02:35:14]** So here's the grand. Here's the cameras. Cameras coming in. Cameras coming in. Then here's the great grand frame loop, let's say that's recording all the frames and that's the loop that's recording the frames to disk.

**[02:35:33]** And that's the one that we have to protect then. Now over here we have this new guy on the block and that's the real time processor. The real time processor is pulling images from the grand frame loop and doing its own kind of wacky process to do the stuff that we will talk about in a future stream, which is doing the actual image tracking and the triangulation and the cleanup to actually produce the real time skeleton 3D kinematic output.

**[02:36:09]** That process, it's heavy. It's a heavy process that.

---

### Chunk 17 [02:36:00 - 02:46:00]

**[02:36:00]** Triangulation and the cleanup to actually produce like the real time skeleton 3D kinematic output.

**[02:36:08]** And that process is, it's heavy. It's a heavy process that wants to be very independent of like the frame rate of the camera, right? Because if this real time loop, let's say, I mean I would be happy if we can get a real time loop that runs in, I don't know, let's say 100 milliseconds, right? That's, that's 100 milliseconds is 10, total is 10 FPS, 10 frames per second. So if you have a frame recording loop that's operating at 30fps and you have a real time loop that's operating at 10fps, then that's potentially an issue if the real time loop is done.

**[02:36:48]** If the real time loop was doing read next, if it was always grabbing the next, it's like I just processed frame 12 and now I'm going to, and I did a loop. Now give me frame 13, then that's a problem. And then I'm doing frame 14 and now it took me 300 milliseconds to get through three frames and there's 10 frames have just passed us by, then you get huge lag. And that's hard to work with. It's hardly real time.

**[02:37:15]** So instead of the real time pipeline querying for the next frame, it just says give me the latest frame. It processes frame 12, it does its real time loop, it takes however long it takes. Then it says, okay, I'm ready for new data. And it gets frame 25. No problem, no problem whatsoever.

**[02:37:38]** By keeping track of that read next versus read latest and basically making sure that the real time pipeline is always read latest, then our real time pipeline becomes self limiting. And we love that because we have done God's honest effort to carefully protect the frame saving process to get the data from the Cambridges into it, get the data from the cameras into n synchronized videos. Still funny. And we have very carefully protected that frame loop from whatever else might be going on in the software, as evidenced by the big difference between the blue line for the front end frame rate and the orange line for the recording loop. Then we can start building this real time loop in that sort of secondary outside space.

**[02:38:41]** And it will just run as fast as it can run. And if you have a computer that is really, really powerful, maybe you can get 15 frames per second. If you want to take that speed versus accuracy knob and you want to say, actually I don't care if it's jittery and noisy. I just want it as fast as possible. You can turn it down to dum dum mode and maybe you can get 25 frames per second in your real time pipeline.

**[02:39:08]** But if you're like, oh, actually I don't like this jittery nonsen, I want real time, but I want cleaner code, then you turn it towards accuracy. Now your real time loop maybe takes 150 milliseconds and you're getting whatever that math is, seven frames per second. All this is happening completely independently from the actual frame recording loop that defines again, going back to this original philosophy of science perspective of things, the frame recording loop is the empirical measurement, that is the part that defines the maximum, that is the empirical basis of all future investigations.

**[02:39:51]** If we do that process well and we record stuff in a clean and synchronous and safe and synchronized way, then there is then the limit of how high quality of motion capture can we produce is constrained by the technology and methods of motion capture. Because we can always go back and record.

**[02:40:18]** We can process and reprocess and I can right now go back and reprocess data that I recorded in 2021. Because in the end the synchronous videos recorded synchronously.

**[02:40:36]** One second, I'll answer that question. And then also, you know, if we're thinking about people in who have wimpy old computers that can't handle anything, they can just turn the whole real time processing off and then they can still play the fun game of doing motion capture. They just, they would just have, they would basically be living that staged processing life and they would record the videos and, and then do the processing. And then maybe they have to wait longer than normal, but they would still be able to get the same quality reporting out of their system that we would get out of a beefier computer. Over here.

**[02:41:13]** MHF asks, how much control do we have over the underlying frameworks we are currently using MediaPipe for the tracking and then any pose for the camera calibration. We have about as much control over those as we want to put energy into any pose. In particular, it works reasonably well as a offline, like as a stage processor. It does the job. But I have a lot of.

**[02:41:47]** It's kind of classic grad student code. It works really well for a very specific purpose and nothing else. And it has been a workhorse in freemocat for a long time. And it will sort of, it will stay in the, in the process for a while. But I have started kind of like trying to Rewrite some of the, the calibration codes so that we can be less dependent on that and start living, you know, like move away from the Chiruko board as a necessity and start doing like body based calibration, like body based calibration to get up and running and then Charuka based calibration to get like higher, higher.

**[02:42:24]** What's the word?

**[02:42:27]** Fidelity calibration. And that, that's on. That's coming, that's coming down the pipe.

**[02:42:34]** And yeah, any pose does triangulation as well. So it's camera calibration and triangulation. Any pose lib is not different from any pose. It's. They're sort of the same thing.

**[02:42:46]** We actually, I talked to Lily Rash Cook some time ago and it's kind of like, it's like, you know, I would like to do like the, the PR type of thing, but they're just not, they're not in a position to maintain that package. So we actually have. Oh, I guess it's in free mocap. I basically copied it over and there's a free mocap. Any pose object that does most of the work.

**[02:43:19]** It's really just doing standard techniques. It's using OpenCV and then sparse bundle adjustment which is just the way to do camera calibration or capture volume calibration. And it does a decent job, but it's busted in a lot of important ways. And so we're rewriting it to make it sort of be able to handle more to be something other than 3000 line long scripts of which only 100 lines are actually doing important work.

**[02:43:58]** Again, it's academic code. It's very good academic code, but it is academic code in terms of the tracking. We do use MediaPipe and MediaPipe is and continues to be a workhorse. MediaPipe also is optimized to run really nicely on a CPU. It can do GPU processing.

**[02:44:20]** V1 does not. V2 will use the GPU processing of MediaPipe. But we are also been doing a lot of work and this is Aaron and Philip. I think probably mostly Aaron on that particular part of the project has been doing a lot of work to make sure that.

**[02:44:46]** To build the rest of our processing pipelines in a way to be agnostic to the tracking algorithm that you are using. I will talk about this in a future stream. My brain is about to fall out of my head. But when we're doing so Skelly Tracker also if you go to the Skelly Tracker John development branch and look at the Churuco Tracker and the MediaPipe Tracker. And then Aaron, it's in.

**[02:45:14]** Skellyforge has some stuff. We're basically trying to build systems that, when you get down, basically support arbitrary tracking algorithms. So we've been looking, we looked at MediaPipe. It's like, we officially support MediaPipe. We technically, if you really want to dig through some deep guts of some of the available repos, we technically support open pose.

**[02:45:44]** Deep Lab Cut. If you look at some of the demo videos of me juggling on the wobble board, the juggling, the balls in the wobble board, those are tracked by Deep Lab Cut. We've been doing some rodent tracking stuff with Deep Lab Cut.

**[02:45:59]** What are some of the other.

---

### Chunk 18 [02:45:45 - 02:55:45]

**[02:45:45]** If you look at some of the demo videos of me juggling on the wobble board, the juggling the balls and the wobble board, those are tracked by Deep Lab Cut. We've been doing some rodent tracking stuff with Deep Lab Cut.

**[02:45:59]** What are some of the other ones? MMPose, YOLO, RTMPOS, whatever. There's a million of these tracking algorithms in the end, but in the end they all have the same basic shape, which is they take in an image and they spit out 2D data. And so we've been trying to do the work to make sure that our processing pipelines can be agnostic so that if you want to. Basically we want hot swappable tracking algorithms.

**[02:46:30]** Yeah, RTMPose, I think, is probably superior to MediaPipe. The main issue there is that installation is more of a challenge in the current world of freemocat v1.

**[02:46:46]** It's pip installed and again, because we're trying to target low XP newbies, we don't want to have a bunch of additional instructions outside of pip. Install free mocap or at this point, uv add free mocap. You know, rtmpos. Like it works in, like once you get it set up, it works really well.

**[02:47:12]** It's from MMPOS. Were they M.M. m.M. Lab. I don't know.

**[02:47:20]** It's like it's a group out of China that basically they, their, their whole shtick is they're like, we will make all of the computer vision algorithms that are that win Siggraph awards. We'll just, we'll will make them available through our package and it's cool and they work. But setting it up is challenging. It's like, it's steps. And, and so because of that we use, we use MediaPipe because, you know, it's simple pimple runs.

**[02:47:47]** You don't have to set up cuda, you don't have, you don't have to have a gpu.

**[02:47:52]** And, and yeah, and, but yeah, we, we do like, you know, I think MediaPipe does a pretty good job, but it is definitely optimized for speed. It's speed and weak computers. But as one of the other design constraints of the V2 version of FreeMap is to allow for, to basically make the data processing and modeling sophisticated enough that we can handle arbitrary tracking algorithms.

**[02:48:33]** Yeah, because in the end it's like, you know, Skelly Cam's job is to get images from camera. Skelly Tracker's job is to do image analysis from single cameras. Skellyforge's job is to accumulate the data from the Multiple cameras and generate, you know, the high quality, do all the cloud cleanup and post processing and whatnot to actually produce the analyzable output. And then Skelly Blender's job is to shove it into blender and all the other steps and processes and whatnot. Okay, this has been fun.

**[02:49:12]** I think I said most of the things I wanted to say about skellycam and the basics of it and the guts of it. I didn't talk about everything, but I talked about most things, which is pretty good.

**[02:49:30]** The real time pipeline and thinking about how to manage the real time pipeline while also not sacrificing the fidelity of the recordings.

**[02:49:44]** Is there any work on fidelity? The interpolation, prediction and key point. That's all the work that's happening in Skelly Forge. So the sub repository of freemocap called Skelly Forge does gap filling, interpolation and then a big part is rigid body correction. So as the data comes in it's noisy so the segments change size.

**[02:50:10]** So if you assume that you're dealing with rigid bodies, you can clean up the data a lot and then get to the point where you can start calculating joint angles. And you can't really make an FBX output if the segments are changing size. So we clean that up and that's all work that happens in skellyforge in this again, this will be the point of conversation of future streams. But if this is. If the whole thing is freemo cap, then the different layers are defined by the sub Skelly repos.

**[02:50:48]** So the camera layer.

**[02:50:54]** Camera layer. Oh, my night light turned on, my screen red shifted which is why my color stopped looking right. Skellycam's job is to pull synchronized images from camera. Skelly Tracker's job is to produce 2D pixel estimates from images. Skelly Forge's job is to handle aggregation and the stuff that requires data from multiple cameras and then blender output and viewer output and saving to disk as CSV in whatever format those are kind of handling elsewhere.

**[02:51:35]** Yeah, Skelly Forge is probably the one. It doesn't have an official development like a V. It doesn't have an official V2 development branch. Mostly because the work in Skelly Forge has been like ongoing again. Like Philip and Aaron have been doing a lot of work in that space. But I'm in the.

**[02:51:54]** In the last few last few minutes before I. Before I explode and die into goop.

**[02:52:02]** I.

**[02:52:11]** Is that it? Is that all I have?

**[02:52:21]** Yeah, I'm gone. That's it. I got. That's all I got left. I don't know where.

**[02:52:30]** Yeah, I've gone completely lost. It's pumpkin time, baby. It's pumpkin time.

**[02:52:39]** But yeah, right. I have started the work of pulling skellycam into Freemo Cap and then starting to basically dust off some prior estimates, some prior methods of building these processing pipelines. And it's hard to predict. It's hard to make predictions, especially about the future. But I suspect that we will be in some kind of proof of concept, real time reconstructed data within a short amount of time, within weeks.

**[02:53:16]** Ish. Whether or not it'll be good data is a whole second question. Because I'm not going to try to do anything too fancy. I'm just going to try to calibrate the cameras offline, triangulate and spit the raw data into some 3D space and we can worry about. I think there's going to be a lot of methods for doing real time rigid body estimation, like real time cleanup as it comes in, rather than just spitting raw data out into the world.

**[02:53:48]** But that's gonna. It'll be the same basic idea except because like, like I was saying, like the using skellycam as like a microcosm of free mocap really works well because it's the most constrained, like the websocket thing that's like, oh yeah, like it's really struggling to send all the images. It's not gonna bat an eye at sending like 3D kinematic data through the WebSocket. That's nothing compared to image data. So I'm not at all stressed about that and I won't show it.

**[02:54:19]** But I do have like a 3js scene in like. There's a version of this UI that is like truly identical except that this says free mocap instead of skellycam. And there's an additional button here that puts a view of a 3js scene. You may notice that the nice thing about this arrangement here is that we're doing HTTP and WebSocket connections to the electron front end, but you will also be able to stream it to anyone that can handle HTTP and WebSocket connection, which if you don't know is everything, anyone can do that. So if you have unreal and you can connect to that using the Same methods of HTTP and WebSocket, if you have, I don't know, whatever else there is, like whatever your personal VR game is, you can stream to that with HTTP WebSocket, a pattern that I expect to see a lot is this without the images, just shutting down the images and just kind of, like using it as a controller.

**[02:55:32]** And then, like, maybe you put in your websocket address and then it just streams the data to it. If we can start. Yeah, I mean, if someone else has already been doing the work of figuring out, like, a.

---

### Chunk 19 [02:55:30 - 03:05:29]

**[02:55:30]** Kind of like using it as a controller and then like maybe you put in your websocket address and then it just streams the data to it. If we can start. Yeah, I mean if, if someone else has already been doing the work of figuring out like a good, like a good protocol for streaming mocap data, I will happily hop on board with that to get some interoperability.

**[02:55:58]** Code Miko. Like I learned about VMC from like a code Miko scream that I like. I just popped into that where she mentioned it as like because she's doing Miko Miko verse or something like that. Like because she's obviously been like leading the tech. She's, she's been, she's been doing like real time mocap in her stream for, for years and years.

**[02:56:24]** And she uses IMU suits which you know, I have my own opinions about. I think if we're like hybrid system would be powerful but also like they're nightmares. Just if you've never used an IMU based mocap suit, it's. I don't recommend it for a variety of reasons, but she's got her, she's building like a, like a, like a V Chat, like VR Chat or like VTubers. VTubers.

**[02:56:53]** VTubers want the real time. And that's where I learned about this VMC protocol. I haven't really looked into it too much, but I will, I will happily adopt that standard if someone else has already done that work.

**[02:57:07]** Main reasons are imus are unbelievably sensitive to electromagnetic radiation. Like because they use accelerometer, so their IMU's Inertial Measurement Unit. They use accelerometers to tell where gravity is. That's fairly, that's. That's very reliable.

**[02:57:26]** That tells you where ground is. But they use a digital compass to tell, to get there, to tell where north is. And they rely on that. Yeah. So the, so the drift is crazy.

**[02:57:37]** And if you put like any piece of metal near them, it completely wrecks the data. So the current iteration of I guess it's Rokoko like they just cheat like that. That's the current approach. And like even Xsens, like the more like scientifically focused ones. The EMF radiation problem is it's insurmountable and so they fix it by using neural network cleanup stages which are non truth preserving.

**[02:58:12]** Like that's. As a research. I talked about truth preserving versus not truth preserving operations last time I think. But they use non truth preserving operations to make it, to make the data look good. But it Ceases to be a valid scientific tool when they do that also.

**[02:58:27]** And yeah, the drift. So imus are an inside out based system. So cameras are outside in, imus are inside out. So the data being measured internally to the sensor is trying to tell you what's going on in the outside world. So because they rely primarily on accelerometers, if you want to, you have the problem of accumulating error.

**[02:58:50]** So you know, say this is your IMU sitting on the table and it's measuring its acceleration and you're trying to figure out its position. You have to double integrate the acceleration signal to get the position signal. And then if you want to know the position on the next frame, you have to double integrate that acceleration signal and add it and add the change of position to your previous estimate. So each estimate relies on the previous estimate and each estimate has noise. So you get what's called accumulating error, which leads to drift.

**[02:59:27]** Like if you just leave it on the table and say measure your position over time because there's error in the acceleration signal and that gets magnified in the double integration process, it will drift over time. And again they have all sorts of methods for trying to avoid that. That's why like Rococo has their thing of like, you know, they try to detect if the feeder on the ground and then they say if there are the feet moving or not moving and it's, it's a, it's a huge pain in the ass. My whole postdoctoral research, like the laser skeletons on the ground and the rocks, my publications from 2018-22 or whatever, they use IMU based motion capture and bleh. Now if you really, really wanted to optimize for accuracy, and I have just failed my dream of getting out of here under three hours, what you would really want to do is combine the two systems together because it's like an accuracy versus precision thing.

**[03:00:25]** Accelerometers are so IMU based motion capture systems are high precision, low accuracy. So on a frame to frame basis, because accelerometers can run really, really fast and with relatively low noise, like their kilohertz range, you get a really precise measurement of the acceleration on each frame. But then the accuracy is low because they drift. Camera based systems are the opposite. The data that you get, the track that you get out of a camera is noisy, it's jittery, like it jitters, but it jitters around the true answer.

**[03:01:07]** So you get. So it's low precision but high accuracy. And anytime you have that kind of a situation, where you have two systems that have like opposite noise profiles.

**[03:01:19]** You are now in happy common filter territory where if you. Because basically you can say I'm going to trust the camera based system to tell me where the skeleton is, but I'm going to listen to the imus to tell me whether or not that jitter is real. Because if I'm sitting here like this, then the accelerometer is going to be like, oh yeah, he's actually wiggling his hand back and forth. But if you're only looking at mocap data from a camera based system and I hold my hand out and it's doing like this, you really can't tell from the camera based system unless you have videos that you can look at, which is another advantage of video based is you have eyes on camera that you can look at the video and use your giant human brain. But let's say you only looked at the mocap data.

**[03:02:11]** I met someone who studied essential tremor in the elderly. So like you get, it's like Parkinson's, like the sort of, like you get the shaky hand and for that, like the real shakiness of the actual thing, you know, for like something like freemocap or freemocap's getting pretty good. But like, let's say a noisy system, The oscillations and the actual signal are on the same scale as the noise you expect to see in the output data. So you just can't look at things in that way. So what you could do is if you slapped an IMU on the person's hand and then recorded from the IMU while you're recording from the camera based system, then you could get the best of both worlds and do the nice clever Kalman filter and get data out of the combined system, which is higher fidelity than either of the individual systems.

**[03:03:08]** That's kind of what a common filter is for sensor fusion, if you're into that, which I guess I am. Okay, this was fun. I'm gonna die now.

**[03:03:25]** Not like right away, but soon and for the rest of my life.

**[03:03:31]** But before I do, I'm gonna, I'm gonna yeet y' all off to some other folks. Thanks for showing up. Thanks for hanging out. It was really. I'm gonna streaming once a week I think is doable.

**[03:03:42]** Maybe someday I'll learn how to get out of here in under three hours. But like, it's, it's fun and it's like I really, I. It's. I spent a lot of time alone in this room thinking these thoughts with cameras running but they're not streaming, so.

**[03:04:00]** And so it's, it's. But. And I know that there's a lot of people who are really. You were interested in following the project and like I've said before, like learning how to communicate the nitty gritty and the details to the world at large are. It's, it's, it's kind of, it's where this project is.

**[03:04:17]** Like, that's, that's. I think, I think that with the cameras now working to the level that they're working, there's not a lot of like, really, I don't have a lot of like technical question marks in my head, if that makes sense. Like, I pretty much feel like I like maybe something with the bundling of the installer, but I think for the most part I, you know, we're pretty good to go. So I think the real, the thing that really stresses me out now is just the scale of work to be done and like all the parts and all the pieces. Pieces.

**[03:04:51]** And as the project grows, like the surface area grows and the work to be done grows. And so I'm kind of taking as like the main challenge of the present moment for myself to really learn how to work on like the community engagement and communication and you know, figuring out how to like, how to recruit help from the, from the world at large so we can get into like, you know, the world of a, of like a proper healthy open source ecosystem, if you will. And yeah, and it's. I think, I think we're doing pretty good. Someone showed up in my lab yesterday who was from a different.

---

### Chunk 20 [03:05:15 - 03:09:07]

**[03:05:15]** You know, the world of a. Of like a proper healthy open source ecosystem, if you will. And yeah, and it's. I think, I think we're doing pretty good. I.

**[03:05:26]** Someone showed up in my lab yesterday who was from a different lab and was in the server and was kind of like, you know, had been. A lot of people show up, I think having. Having been on like a little tour of the available options and he was like the freemo Cap community that exists in the server. AJ is at the core, but there's other people in the core. The fact that people can just show up to Discord Server, ask questions and get high quality answers and discussion, that's really, I think the thing that sets us apart from anyone else.

**[03:06:02]** I think I'm really curious to see what we're about to be in a world where we're going to start to get data back comparing like comparing free mocap to the other available softwares and I'm really curious to see what's happening there. I'll bet we hold up. But you know, I think, yeah, the community is really the part that makes arguably the more exciting thing.

**[03:06:30]** Okay, okay. Who. Who will I send you to?

**[03:06:41]** I want to send. There's always, there's always like the science and technology category is not popular. So I'll just find someone doing something that looks interesting.

**[03:07:00]** Yeah, Sure. That seems valid. And that's also looking for someone.

**[03:07:13]** Excessive tobacco use. I hope you guys can handle a potential successful excessive tobacco use.

**[03:07:25]** Oh.

**[03:07:30]** Yeah, and we'll just play the fun game of I hope this guy is not a Nazi. Never know these days.

**[03:07:42]** Do this.

**[03:07:48]** He seems friendly.

**[03:07:56]** Okay, I'm pushing the button. Yeeting y' all out. Have fun, be nice. And yeah, thanks for hanging out and I'll see you next week.

**[03:08:13]** So I've got next week I might. I will either talk about like progress towards like integrating skellycam into free mocap. One of these weeks I'm going to talk about Skelly Bot, which is the AI bot that I've been using in my classes for the past six semesters, which will be a bit. Would be a significant change of pace. But I need to get.

**[03:08:35]** I need to start speaking of communicating. Like, I'm not like no one knows I'm doing that, but I think it's actually really cool. So yeah, stick around, come around. It'll be Thursday afternoon at some unspecified time. Maybe some.

**[03:08:49]** Yeah, join this. Join the Discord server. You're all wonderful. I love you very much. Okay, goodbye.

**[03:08:56]** And yeah, okay.

**[03:09:07]** I.

---
