# Transcript: 2024-05-10-SkellyCam Interim Update [2024-05-10]

## Source Information

- **Source Type:** Local File
- **File Path:** `C:\Users\jonma\syncthing-folders\jon-alienware-pc-synology-nas-sync\videos\video_eater_downloads\playlists\[OLD] FreeMoCap Development\2024-05-10-SkellyCam Interim Update [2024-05-10]\2024-05-10-SkellyCam Interim Update [2024-05-10].mp4`

---

**Total Duration:** 00:40:11

---

## Full Transcript

### Chunk 1 [00:00:01 - 00:10:00]

**[00:00:01]** Okay, so working through skellycam. Say that first part again. Stop all. So skellycam John fastapi branch, it installs through pyproject toml and then run entry point is skellycammain run the Whatever. And so then basically this runs this Run UVicorn server.

**[00:00:26]** So. So which just runs a fast API app, which is made through this. This is like a string to where the factory is to make the app. And when it runs, it gives you this URL here and it runs on your local host, which is like your. The.

**[00:00:45]** It's your network card, which is the same way you connect to the Internet, but it's not connecting externally, it's connecting locally. And I'm pretty sure puffmachine might know more about this than I do. So if I say anything wrong, just shout it out or judge me in silence and tell me later.

**[00:01:05]** Yeah. So basically this then defines these routes that you can get to. So API app factory.

**[00:01:19]** This is the part that actually makes the application that is running behind the server. And then these apps are defined. If you click on enabled routers, you go into that. These are the routers and the main one to look at right now. So basically these are nice because you can then like this is.

**[00:01:49]** So this little interface is from. Is built automatically by fastapi. It's like a swagger thing. It uses Open API or something like that. And you can just hit the endpoint and you.

**[00:02:02]** The server hears it and then gives you a response and it says hello from Skelly and skellycam backend. And that route you can see right here is just HTTP localhost 803 hello. And if I just go to that URL, It just gives you that same message.

**[00:02:33]** Because what happens when. When I hit the execute and it sends this command is the server hears the request come in, health check, control B. And then this is the API call. The green means that it's from the API and it sends back this JSON that just says blah, blah, blah. And then that's what you.

**[00:02:59]** The response body is what you see there. Okay. And so then camera connection router. So this is sort of the main one. There's a detect cameras and, you know, startup and blah, blah, blah.

**[00:03:14]** The websocket is sort of, you know, it's set up kind of, but it's a little broken, so it's not actually working.

**[00:03:22]** The camera connection mostly is, and so that has slash, connect.

**[00:03:34]** And sort of several versions of that. So a get is basically it's a call that you get that sort of just like give me information. Like you don't send much. I don't know, whatever. This is sort of getting beyond my desk.

**[00:03:48]** But the test one is set up that it will attempt to connect to I think all available cameras with default settings and then record just this single number of frames and then shut down. So it's just a way to kind of test the connection and then eventually we can also. It doesn't record yet, but it also doesn't display anything yet. But we build around that.

**[00:04:16]** So when I hit that one I can put. So I'm going to shut this down and return it on back on with the debugger on. And then if I go to connect, test. See, connect, test here, same guy there and hit it. Oh, I forgot to put.

**[00:04:40]** Wait, no, stop. I forgot to put the debugger. But that's okay. Oh, there you go.

**[00:04:51]** Oh. So yeah, so let's write. Cool. Do everything.

**[00:04:58]** A lot of logs. So it goes through, connects to the cameras. We haven't detected them. So it detect. It runs the detect method, which is the same thing that's hit from this place.

**[00:05:12]** Detects the cameras, sees. I'm on Windows. You can tell the levels here by the color. So trace is like details, applies a config. And then this is sort of getting.

**[00:05:32]** Okay, we don't need you anymore.

**[00:05:39]** From Skellycam core memory, Memory down here, whatever. So we're building like memory buffers in a shared memory system that we're going to put the frames into so they can communicate without having to sort of go through like. Like when you're talking like your network card or pipes or any inter process communications are very sort of costly and difficult thing. So this is just a way to just save the direct directly save the bytes that come off of the camera and then access them from elsewhere without having to have any additional overhead. So that starts by just.

**[00:06:27]** You have to like see what size the data is going to be and so you can make enough space for it. And so we basically we put. So the image is going to be. This is 6 megabytes raw. Like a raw 1080p image is 6 megabytes, which is, you know, we can compress it, but we want to compress it like outside of the frame capture loop because compression is expensive and takes time, so we want to do that elsewhere.

**[00:06:53]** And then this 217 bytes is like data like, like the timestamps and the camera ID and just like metadata about what's in there. And so the total buffer Size that I just set aside like a gigabyte of memory just for clarity. That's more than anyone would, more than we would need. But it's an easy number. And this is the name of that shared memory that is the way to connect to it from other places on this thing.

**[00:07:23]** But whatever details, trace data and it goes through, waits for the cameras and then it starts. So the main stick here is that it's a trigger camera system. So the previous systems like it would sort of turn on the camera and then start collecting frames in a loop, just like, give me a frame, give me a frame and then sort of emit them. And then other systems would sort of need to grab those frames to sort of, you know, record them and whatnot, which works. But the challenge is that if you have a bunch of cameras and they're all running in their own loops, then synchronizing them can be difficult.

**[00:08:01]** So this is using a system that happens in a lot of research cameras and research grade camera systems where you use research, machine learning, research types of cameras typically operate through hardware triggers. So you have a wire that you stick into it and it sends a pulse and so you can trigger it to send a frame back to you with a direct pulse of electricity. So you can get super, super high precision, which we don't really. It's just hard to get with simple software.

**[00:08:40]** So I built this system up so it's kind of using the same kind of approach where each or the cameras are all run in like a loop, like a multi camera loop. And then they get triggered with like multi processing triggers and whatnot. So there's instead of them, instead of the cameras running in a loop and sending out frames whenever they get a frame, there's this like higher level sort of loop that's sending out triggers to the cameras. And then when the cameras. Yeah, so you trigger the camera and then when the cameras trigger listening loop.

**[00:09:26]** So the cameras are the cameras. Instead of running a frame grabbing loop, they're sending, they're running a listener loop.

**[00:09:34]** And they. So the camera says get frame. And then when it, before it gets the frame, it like waits in this like really sort of tight while loop that's looping like 10 times per millisecond, which seems very, very fast. And it is fast. And it's like enough that you might notice in the system, but like your computer can run much, much faster than.

---

### Chunk 2 [00:09:45 - 00:19:45]

**[00:09:45]** While loop, that's looping like 10 times per millisecond, which seems very, very fast. And it is fast. And it's like, enough that you might notice in the system, but your computer can run much, much faster than that. So it's not really eating up that many resources. And it's running in its own independent process.

**[00:10:07]** So you're not going to get any blocking, Python, Global Interpreter lock, and all that kind of stuff. So it's protected from anything else going on in your computer. So here's that trigger. It does this grab, which basically just tells, like, the camera device to, like, get the frame from the camera, but it doesn't decode it yet, which is like the part where it actually turns it from, like, whatever. Whatever's coming out of the USB into something that you can, like, look at as an image.

**[00:10:45]** And it only returns a boolean. Like, there's no visual image output yet. But after it does that, it waits for a. It says, okay, I did it. And then it waits for another trigger that says, like, the listener guy.

**[00:11:02]** Like, waits for them to all say, okay, I did the grab. And then once it hears that from all of them, it fires another trigger that says, okay, just realize I can do this. Oh, wait, not that. No, yeah, There do, do, do, do. Yeah.

**[00:11:32]** And then when they hear the retrieve trigger, then they go and they do the actual retrieval step, which.

**[00:11:44]** This step takes like 1 millisecond and very, very fast. This step takes like 7 milliseconds for a 1080p video, 1080p image on a pretty powerful computer. But the point is that by triggering those separately, you can get much tighter time precision between them. And then once it does that, we now have. So we now have the actual image.

**[00:12:16]** So we immediately grab a timestamp as quickly as possible using perf counter ns, which gives us an integer, hypothetically, in nanoseconds, which is realistically more precision than you get out of this type of system. But it means that you're not giving, like, a float with, like, a floating point imprecise number. It's like an integer. And then you go into this shared memory and you put the frame.

**[00:12:51]** And this is like some crazy thing where you've, like, in the setup of this, I reserved a buffer, which is just a very long string of memory addresses, basically. And then convert the image with the metadata into a payload of bytes, doing the metadata separately from the image, because the image is basically already in bytes, so you don't have to spend any effort converting that. But the metadata is super tiny. So you can pickle that and you don't notice that amount of time because it's so small. So doing those things separately also can save some time.

**[00:13:39]** And. Yeah, and then this part right here is where you put it into the buffer using like numpy kind of slicing ish syntax. And then you increment an index and then, and then the camera, and then that's the end for the camera. The camera is now done just. It just passes along.

**[00:14:00]** But there's this other guy in this camera group called the frame wrangler who has, who has his own listener task. And this guy lives at like the higher level, like in the main. Main threads, like outside of the camera triggering threads. And it's just running this sort of like more.

**[00:14:25]** It's like an asynchronous task and where are you?

**[00:14:34]** Yeah, so it runs this async loop which is not as protected and not as fast as a multiprocess. But that's fine because it's at the top level and it can sort of run this more like lazy sort of listener that, you know, go. Oh. It asks the shared memory manager whether or not there's a new multi frame payload available, which just basically asks all the camera shared memories, like if there's a new thing available. And then if it is, then it goes into this and it double checks that you still have one there because you have to be very careful because nothing is protected.

**[00:15:24]** So you're reading and writing from the same memory. So you can't have in this synchronously. So you can have collisions that will just make the program crash. There's a lot of protection to make sure that doesn't happen.

**[00:15:41]** Oh yeah. And then you can separately grab either the next frame or the latest frame. So if the front end is lagging, you don't need to get every frame, you just get the most recent one and then your frame rate drops and that's fine. But if you want to record the data to disk, you want to get every single frame and if it lags, that's okay. So you can do that separately.

**[00:16:02]** And that just goes in. In to this? Yeah. So before I was showing you the put frame and this one now calls the retrieve frame. And this is just the opposite as the other part.

**[00:16:16]** So instead of putting stuff into that, it just pulls it out of it and then re recreates the frame outside of that same process. Does a bunch of logging because I'm trying to keeping track of how fast things run actually.

**[00:16:38]** Yeah, so you get like this. So camera zero wrote frame zero to shared memory at index zero, offset zero bytes. Took 5 milliseconds. Checksum is this, which is just literally take the whole buffer and just sum it up so you get a big number that you can check later to make sure that you got everything right. And then this is all the.

**[00:17:03]** It's been 11 milliseconds since the previous run through. Camera is ready to get the next frame. And then this is the multi camera saying we're triggering them, blah, blah, blah. Oh, right. And that's where we are right now, actually.

**[00:17:18]** The listener doesn't work. There's something blocked somewhere, which is not surprising at all. But.

**[00:17:27]** But yeah, I was able to get, I think, seven cameras. Six, seven. I think after, like, I was able to get, I think up to five cameras. Oh, I have the notes right here. Yeah.

**[00:17:39]** Up to five cameras running 30fps, 1080p0 frame drops, you know, and at full 30fps. And then once I added a sixth camera, it jumped up to 40 milliseconds, which is like 25fps. And then I ran out of USB ports.

**[00:18:04]** Good. Yeah.

**[00:18:08]** The frames, it's like something like first in, first out, stuff like that. And the frame, because. Is not responding properly. Yeah, yeah. If one.

**[00:18:24]** So currently, if one camera stops responding properly, the whole system will just stop. It'll grind to a halt. Okay. And so that's like one of the, like handling stuff like that is sort of like, you know, we get to that later. But you're right that with this, like, we just need to have some kind of a process that basically says if one camera doesn't respond within a certain amount of time, we'll skip it and then just have an empty frame for that one.

**[00:18:51]** Okay. Because, you know, right now it's like, you know, it's a.

**[00:18:59]** Would. It would. It would get stuck in the.

**[00:19:04]** The trigger loop. Yeah, it would get stuck here.

**[00:19:10]** Okay. So. So the cameras that are working fine will wait until the frames is used. No, no, no, no. So that's kind of the beauty of this.

**[00:19:24]** I should. Like, if I was drawing this, it would be easier, but this whole process cannot tell what's happening outside. So the cameras just put the frames into the memory and then it's the job of the listener loop to pull them out.

**[00:19:43]** So basically,

---

### Chunk 3 [00:19:31 - 00:29:30]

**[00:19:31]** Cannot tell what's happening outside. So the cameras just put the frames into the memory and then it's the job of the listener loop to pull them out.

**[00:19:44]** So basically the parent sort of multi camera trigger just says grab a frame. And then the camera grabs the frame and then puts it into that shared memory buffer and then it just moves on to the next frame. It doesn't even, it doesn't check if anyone's looked at it. It just keeps moving on.

**[00:20:07]** Then the other process on the outside is the one that sort of like waiting for new frames to be available. And when they're available, it copies them out of the shared memory buffer. But the, but the cameras don't know that the listener exists. They're just putting the frames into the queue. And it's not exactly first in, first out because it's.

**[00:20:36]** We're basically putting them into a buffer at specific locations. And then because the buffer is a finite size, it just kind of loops through the available spots when it's putting frames in and then, and then keeps track of, oh, I just put a frame, she says, right here. It's like I just put a frame at this index here. So that when the listener comes in, it can check.

**[00:21:13]** Yeah, it checks for new frame is available, which checks if the. Yeah. So when the camera writes the image, writes the frame to the buffer, it increments this index that says I just wrote a frame to index number 12 or whatever. And then it moves on. And then the listener comes in and says, It says, first of all, should I look?

**[00:21:45]** Is there new data available? And that will check if the frame that I'm supposed to read is the same, is the one ahead of the one that was just listening. If it is, I just skip it. That's the part that's like, is there a frame available? There's no, okay, I'll come back.

**[00:22:05]** And then if it checks if there's a frame available, it says, yeah, a frame was written to index 12, but you have only read up to index 10. So yeah, you go grab another one.

**[00:22:17]** And so that it uses this parts of the shared memory buffer to do that communication of. I wrote something to frame 12 and oh, I just read from frame 13 or whatever. Actually just realized we don't actually need to put the read flag in there, but it's whatever. But that it's like, you know, this whole thing is set up to share like big images across processes. So we just reserve like one tiny little part, one little byte of that to also communicate like I just wrote to this number and I just read from that number so that the same communication happens across the board.

**[00:23:00]** But the cameras, I actually, theoretically, if the listener gets too far behind the writer. The writer, the loop will catch up. And I think I set it up that it will crash or throw. I set up that it's easy to turn it from like a warning or a crash or something like that. I think I set it up to be grumpy, so it would crash.

**[00:23:26]** But the buffer is large enough for 256 frames from each camera. So, you know, sort of it's, I think in the same place of like, what happens if one of the camera fails is also the question of, like, what should you do if there's. If the buffer catches up? You know, I think for different applications you might have different. You could.

**[00:23:51]** I think. I think at some point what we'll want to do is have some kind of a diagnostic that can. That will run a test on your computer and say, okay, you should probably have, like, your computer can handle a maximum of, you know, this many cameras at this resolution or that many cameras at that resolution. And we can base those decisions on these types of diagnostics. Yeah, yeah, I have different brand, different model cameras.

**[00:24:21]** Yeah, yeah, yeah. Faster. Clearly faster than the other. Oh, really? Yeah.

**[00:24:28]** And I think that's. That's something else. It's like you can see little pieces of it. It's not really implemented, but a lot of this is also clearly geared around like, getting that kind of diagnostic information, like, reliably and get. So that, you know, if someone gets the software turns it on, it can run a little boot sequence that just like, tries to send a bunch of fake images.

**[00:24:51]** Just like, you can easily make just like a random bunch of numbers that are the same size as an image and then just kind of send these little, like, test loops through and then give a report that says, oh, camera zero is doing this well and that camera is doing that well. And, you know, you can sort of have a little health check that sort of can help people figure out how to tune their system.

**[00:25:18]** Yeah. And then the other part that's exciting is so basically I got to the point where, like, the listener wasn't working properly. And I was like, that's when I sort of learned how tests work. So I'm not done yet, but I basically a lot. Close, close, Close tabs.

**[00:25:47]** Close all tabs.

**[00:25:52]** So the way I'm thinking about it is, like, there's a lot of, like, models in the, in the software. You know, like the camera config which has IDs and resolutions and da, da, da, da, da. And it sort of like has certain ways that it should be. And so the model, the pattern I'm going with now with the testing is like every sort of significant part of the data model can have its own set of tests that you can run and just test all these things. And the basic structure of how a test works is the machine was talking to me about this, I was asking the AI about it, and it's like, arrange, act, assert.

**[00:26:56]** So you arrange everything as it should be, and then you do some action on it. Like in this one, just testing, making a configuration file. So I give it a bunch of numbers, I make a thing, and then I just make a bunch of assert statements that say these are the things that should be true. And then if one of them is false, then it fails and tells you why.

**[00:27:28]** And so then basically the way this now can work. So I did this for the configs, and I also have now done it for that shared memory stuff. So you take a bunch, you make a bunch of test images that have a certain shape and size, and then.

**[00:27:57]** You basically run through a dummy version of that process. I said, and just use the main parts of the memory model in the way that you're going to use them and then just make sure that they work.

**[00:28:16]** And so I just realized that it's so dumb because it's such a basic part of software development to write tests. And I just, like, never learned how to do it because I was raised as a scientist and scientists don't know how to do that type of stuff, even though they clearly should.

**[00:28:32]** And I just realized it's like, so now what I can just do instead of having to dig through all this stuff and figure out, oh, what broke? Why did that break? Why isn't it making it all the way to the end? If I just make a test for, like, each part individually and test that each part individually is doing all the things that part should do, then the. And if the code doesn't work at that point, then it's much, much easier to diagnose because you can have confidence that, like, the.

**[00:28:59]** That is not some stupid, like, oh, you tried to put too big of a thing into too small of a thing, like some uninteresting problem that's actually causing that problem, causing the thing to fail. And it also means that, like, I can talk to people like Philip, who is, you know, very interested in helping out with skellycam, but, like, you know, there's a lot going on here. So rather than saying, like, hey, dive into this, like, complicated thing, I can just say,

---

### Chunk 4 [00:29:15 - 00:39:13]

**[00:29:15]** I can talk to people like Philip, who is very interested in helping out with skellycam, but there's a lot going on here. So rather than saying, hey, dive into this complicated thing, I can just say, ok, here's the main parts. This part needs these tests and we can fill up and work on building the test for the individual components and have a way to both learn how each part works individually and also be able to work in a place that's not going to break the functionality of the main software because he's only building stuff in this tests folder.

**[00:30:01]** So you think this will come before the new gui? This will. Yeah, yeah. So, yeah. So this is also one of the really nice things about this type of a system of making like a back end server is that we can kind of decouple the process of development of like the back end functionality of like, oh, the image is in the memory and the blah blah blah from the front end functionality.

**[00:30:34]** That is the actual like the GUI part. So then I have this other very, very. I showed you some, I think I've posted. I don't know if I have, but there's like some other more sophisticated front ends like React and Vue and stuff like that.

**[00:30:52]** But the problem of the is that they're complicated. So just made this super, super dumb, dumb website sort of our HTML document that's just like a bunch of buttons. And then this sort of, you know, I say I wrote it but like this is like me and the machine wrote this code because I don't know how to do this. And it's just like, it's like, hey machine, how does shared memory work? Hey machine, like how do I write a website with a button on it?

**[00:31:24]** And so if I. How do I make a Tori app so it can make its own standalone? So if I then run. So, so package JSON is like the web dev equivalent of the pyproject TOML and it defines these scripts. So this is dev runs Tori dev.

**[00:31:44]** So that's like I could push this button in pycharm, but I'll just show you, if I type NP NPM NPM run dev, it runs this command and it pops up this simple ugly app. And.

**[00:32:18]** That is first of all it's a Tori app. So it has, it's like just a browser. So it's the same actually. Can I do this? Yeah.

**[00:32:29]** Nice.

**[00:32:32]** Sure.

**[00:32:37]** And so. Oh yeah, Main js. Yeah, so this is the index HTML and then down here you just import and run this main JS script here. And then if you recognize these URLs? They are the same ones as here.

**[00:33:00]** So basically the buttons. So there's this hello one that we talked about before and just so document is like. You can see it here too. This is my Firefox. It's like whatever, all this stuff and it gets the button and then when you click it, it runs this asynchronous function that does a fetch which is basically calls the route that lives here.

**[00:33:43]** That same one there on this port 800 8003, then waits for the response and then if it hears the response.

**[00:33:55]** Where are you? Oh, this one. Hi. It gives that.

**[00:34:06]** We even have the websocket. Technically works, doesn't this is it this red area at a different point in development did display the images from the cameras, but I broke it to make was working and then I did the shift I mentioned towards the trigger camera method and. And then it broke. So that's part I need to fix. But yeah, it's like where is it?

**[00:34:37]** Yeah, if WebSocket, you know, check hi. When it opens, do this if it. That probably is going to. I don't really. I guess.

**[00:34:49]** I guess it's fine if it's already connected. I don't know. And then when you get. When it gets a message, it sort of tries to pull the JPEGs out and there's like another part that converts the multi frame payload into a front end payload. So that part actually compresses the raw images into JPEGs and then that's like an easy thing to send over this socket connection and grab them and decode them and turn them into canvases and blah, blah, blah, blah.

**[00:35:21]** So yeah, so like that's kind of the. So the. The. We were. I was talking with like Aaron and Philip and Trent the other day really this week about like the roadmap and the strategies we're going to take to basically like the rollout I guess of the 2.0 version and like, you know, making sure we can kind of like maintain the existing GUI but also kind of start like sunsetting it I guess is the term.

**[00:35:52]** Or like you maintain or maybe LTS or something like that. I don't know what the term is. Like we're gonna maintain it and make fix bugs and whatnot, but we're not gonna spend a lot of development work to like make it better because we're gonna be doing all this work to like, you know, revamp the back end. And in the meantime like skellycam, because it is both like the most like the core the most complex part of the technology because it's actually like doing empirical measurements. It's nice to keep it separated from like the part of like the rest of it, which is basically processing images, which, you know, can take longer.

**[00:36:28]** And if it crashes, it's no problem. You just do it again. Like, you know, it's sort of a little more safe. So skellycam is now acting as kind of like a microcosm where we're going to figure out like the architectures and the workflows and how to write front end code and then sort of like at some point start sort of like being like, okay, there's something people can use now. And then.

**[00:36:53]** Yeah. As we figured out with skellycam, we'll sort of start applying the lessons learned to like core Free mocap. And you had dark mode. Yes, yes. Oh my God, I'm so sorry.

**[00:37:09]** It's so bright.

**[00:37:12]** There's so many things in there that it's like when I started, when I finally started using, like I learned how to write JavaScript, I was like, oh my God, this is so easy. It's so much easier to do dark mode when you're doing in, in JavaScript than it is in Python. And also like, I know what, I didn't know what CSS was when I started this and sort of, yeah, I, I live my life in dark mode and every time I open up Freemo Cap, I'm like, no, it burns.

**[00:37:44]** Yeah, yeah. And also like, I still remember you had a request a long time ago of having the, the logs be something that you can turn off or turn down, like quiet them down so they don't say so much. So I added more logs, but they're more easy.

**[00:38:04]** With the lessons Learned from the 1.0, we can now go into the 2.0 and make sure that when we set up our logging that it's set up that you can, there's like a proper settings system that can keep like on the front end. You can say which level you want to see and just basically, yeah, like, and then something will, will just trigger this to do what? It's just change that value and then you're. And we can have all of the logs going into the log file and then just like, like whatever you, the user want to see will come into the front end.

**[00:38:49]** Yeah. So that's my, that's my presentation.

**[00:38:59]** A little bit.

**[00:39:02]** It's been fun though. It's like, it's. It's been kind of, you know, with like classes and stuff like that and then, like, I personally have spent. Been spending, like, almost all of my development time in Skelly Cam.

---

### Chunk 5 [00:39:02 - 00:40:11]

**[00:39:02]** It's been fun though. It's like it's. It's been kind of, you know, with like classes and stuff like that. And then like I personally have spent. Been spending like almost all of my development time in Skelly Cam and it's in like Philip and Aaron have been really holding it down in free mocap land.

**[00:39:21]** But like it's like I'm excited to start like merging. Merging the streams again is kind of the theme. And you know once this, once this kind of architecture, like you know, proper APIs and WebSockets and front end, back end separations and da da da make it into main free mocap just a lot of things will just improve and like a lot of old problems will just be. They'll just go away. They'll be obviated.

**[00:39:52]** Yeah. And won't that be fun? Oh, it's 12. I have to run soon but. Hi Ch Nice to see you.

**[00:40:05]** Hello. How are you?

**[00:40:10]** I was really curious.

---
