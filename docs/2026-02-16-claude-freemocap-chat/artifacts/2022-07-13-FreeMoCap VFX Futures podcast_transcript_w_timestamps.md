# Transcript: 2022-07-13-The FreeMoCap Project VFX Futures podcast

## Source Information

- **Source Type:** YouTube Video
- **URL:** https://www.youtube.com/watch?v=Bqt8ZC5C4h8
- **Video ID:** `Bqt8ZC5C4h8`

---

**Total Duration:** 00:34:34

---

## Full Transcript

### Chunk 1 [00:00:09 - 00:10:00]

**[00:00:09]** Hi everyone. Welcome to this latest episode of VFX Futures. I'm Ian Fails from befores and afters and today we're going to be talking about free open source markerless motion capture with free mocap. To help me do that, I'm joined by John Mathis. Hi John, how are you?

**[00:00:29]** Hello, how are you? I'm good. John, whereabouts are you in the world at the moment? So I'm currently in my apartment in Boston, Massachusetts, United States of America, and I'm recording from Sydney. So we're on opposite ends of the world.

**[00:00:45]** But you know, this is how we connect these days, Zoom and probably for a long time to come, I think. I suppose we'll see. John, a few weeks ago I noticed a post that you had made on Twitter and it sort of filtered around the world actually on LinkedIn and some other places about free mocap. Now I want to talk exactly about what that actually is later, but what might be interesting is to hear about yourself a little bit, where you come from, what you do, and then we'll sort of tell the story of how FreeMobCap became a thing. So that's great.

**[00:01:28]** What do you do? So I am presently a professor studying human movement neuroscience, entering into my third year. And my, so my background, my bachelor's degree is in philosophy. And then somehow made my way into a neuroscience lab studying locomotion. And especially during my, you know, got my PhD with Brett Fajian from RPI and then in my postdoc I was working with Mary Hayhoe at University Texas at Austin.

**[00:02:03]** And especially during that time I started getting into an area of like sort of building my own methods to study human movement, especially in the natural environment. And my postdoctoral work was people walking outside over rocks wearing eye trackers and wearing kind of a, you know, IMU based motion capture systems sort of analogous to like a Rokoko or Xsense. And so during that time I kind of developed a sort of more technical ability to kind of like hack apart stuff and do some basic computer vision. And that sort of, that research project got me this position here in Boston. And now I am sort of into a new space of studying human movement.

**[00:02:53]** And then sort of the way that the timing of the past, I guess coming up on two years now, was right around the time that I was sort of starting to get my feet under me in Boston. And sort of the lab was built and sort of like about ready to get started. The pandemic hit. And so we all got kind of booted back to our homes. And this Project of sort of like I had been interested in markerless motion capture since, I know, since Open Pose came on the scene in 2017.

**[00:03:25]** And I've always had in the back of my mind like this could be used to just build a motion capture system. Because I've been working with mocap since like 2008 and you know, time was right. So put the time in. Yeah, I guess for people who don't know what. What does the markerless side of motion capture mean?

**[00:03:46]** Because we're very familiar with suits. But. But maybe just explain for people who. Not who are not too sure. Sure.

**[00:03:52]** So you're the most. The image of motion capture that most people have in mind is sort of like the Spandex elastic suits with the reflective dots on it. There's other forms of motion capture, but that's kind of a classic one. So those dots are markers. They're usually the retro reflective markers that are designed to be picked up by the camera.

**[00:04:13]** So the cameras are usually not like your standard like color. Color video cameras are infrared and the markers and cameras kind of work together to make it kind of easy for the system to reconstruct the three dimensional points. And then the output is a bunch of, you know, 3D dots floating around. You connect the dots and sort of, you know, fit that to your rigs and all that kind of stuff. And that technology has been around, you know, decades, many decades, forever.

**[00:04:41]** Feels like. Yeah, I'm trying to think of like the earliest thing I can think of would be like Nikolai Bernstein, who was a, who was a Russian researcher in like the 30s and 40s who was drawing on top of images. But arguably this goes back to like Muybridge and the picture of the horse running across that was a bar bet by Leland Stanford, which sort of the origin of both video and motion capture. So that's. So then markerless motion capture, in contrast, is the idea of recording the same kind of information of sort of precise recording of a person's movement without the benefit of markers in the image.

**[00:05:23]** So when you put. Because marker based motion capture, the subject has to be wearing special stuff in order to make the reconstruction easier. And markerless systems are basically like far more advanced computer vision these days almost. These days are pretty much all using sort of neural network deep learning based methodologies. And that technology is getting to the point where you can just feed these neural networks RAW video and they will spit out pixel locations.

**[00:05:57]** It's like, oh, here's your eye, here's your shoulder, here's your elbow, and that's Strange magic.

**[00:06:09]** It's the kind of thing like I don't, I kind of understand the underlying technology, like I understand it enough to use it. But it is sort of an emerging area that basically the technology of people in my field don't tend to use the word AI all that often, but the sort of common term would be AI. AI based tracking methods to perform tasks that used to really only be possible with dedicated hardware in terms of like specialized markers and specialized cameras. And so that's markless in a nutshell. So I again, the history of that, I couldn't tell you the full history, but I noticed it in 2017 when Open Pose, which is from some lab who, I can't remember, I don't know the names of the people, but it was from Carnegie Mellon released like a, you know, a demo video of people like dancing and they're having the skeleton drawn on top of them.

**[00:07:09]** And I remember seeing that and thinking, that's the future of motion capture. I need to learn, I need to learn how to use it. And so I went to their GitHub and went through their.

**[00:07:24]** I discovered at that point that these, the people that make these tools are not speaking to the general population, they're speaking to other advanced computer scientists. And so I basically then spent the next three or four years trying to figure out how to interpret the documentation in these GitHub tutorials in order to be able to produce something that looked as cool as what they were showing on their demo vid. Yeah, right. We will get to what Free mocap ultimately has become or is at the moment, which as I said is a free and open source markerless motion capture system, but importantly uses very cheap hardware to make that happen. We'll get to that.

**[00:08:08]** But John, in that three or four year span in which you got excited about the possibilities of markerless mocap, what kind of experiments or things did you do to help yourself learn and find out more about it in the community? Sure. So I guess around at that time still today, there was kind of two sides of the work I was doing. The primary work I was doing was the NIH funded visual control of locomotion stuff using basically IMU based motion capture and eye tracking to record people's eye movements and foot placement as they're walking over terrain for all these health applications. That's where my funding came from.

**[00:08:56]** That's the papers I was publishing at that time and that's where most of my work went into.

**[00:09:02]** And sort of on the side I was playing around with Open Pose, which was that first software and really struggling with it, because it's really hard to get these things working if you don't know what you're doing. And I guess. So I was playing with open post. I was finally getting it to work. I was sort of learning how the data was being saved.

**[00:09:24]** And I was also making these sort of center of mass, sort of biomechanics analysis gifs that I was posting on Reddit and discovering that if I made one of these things and posted to Reddit, it would get, you know, a couple tens of thousands of points, which is cool. Yeah. But what were they? They were gifts. They were, they were gifts of.

**[00:09:45]** So the, the first one was a, an athlete named Simonster. She's a French parkour guy. And I saw the animation of him doing this really intense handstand where he was.

---

### Chunk 2 [00:09:45 - 00:19:45]

**[00:09:45]** So the first one was an athlete named Simonster. He's a French parkour guy. And I saw the animation of him doing this really intense handstand where he was just. He set up his cell phone, he was doing a handstand, going down and pushing himself back up and doing all this amazing stuff. And I realized watching that gif, that because of my training in biomechanics and robotics and all the sort of education I had, I had a certain visual intuition looking at that animation that's like, I'm looking at this.

**[00:10:23]** I know where his center of mass is. I know center of mass, basically this like the summation of a person's mechanics, you know, sort of center of gravity, center of mass, same thing. And I know that, you know, it has to be within the boundaries defined by his hand because, you know, he can't pull on the ground, he can only push it. So we. So I knew, watching that, like I knew what, what the mechanics of that situation were.

**[00:10:47]** And I realized that I also knew how to draw that intuition on the animation. So I went home and I opened up matlab, which is the only way I knew how to code at the time. Since learn Python and manually frame by frame, drew X's over each joint, hundred, couple hundred frames through, calculated the center of mass, calculated the base of support, which sort of defined by his, like hands. And you know, lo and behold, it popped out exactly the way it had to pop out because of physics. And, you know, took me like two, three hours.

**[00:11:23]** And I woke up the next morning because, you know, you got to post in the morning on the east coast, that's what everybody knows, and posted it and walked to work, which was like a 10 minute walk at the time. And when I got to work, it had like 3,000 points. And I was like, oh, shit, I guess, I guess that's a thing. Yeah, people are interested. Wow.

**[00:11:43]** I guess people are into it. Yeah. So then I made a couple. I made, I don't know, maybe half a dozen or more of those over the next couple years, each one increasing effort from the one before it because I can never do the same thing twice. And that every one of those was hand labeled.

**[00:12:02]** I would go through every frame and just click, you know, hundreds of times to label the dots and thinking all the while, wouldn't it be great if there was an automated system to do this? And then, you know, that's. I think that's kind of the basis that things kind of grew out of, sort of. I kept making these animations, I kept learning More and more technical skills. And then all of a sudden I had things kind of aligned in the right way and kind of here we are.

**[00:12:40]** Right. So again, perhaps for someone who doesn't know how that really works technically, how did you take what your experience with those GIFs and turn it into what effectively is a motion markerless motion capture process?

**[00:12:59]** So the gifts were always kind of, there was always a challenge because there was always a single camera. Because it's just, I just find videos online. So it wound up kind of, there are certain constraints about the kinds of stuff you could do. Like it has to be kind of a straight on shy, you know, it can't be like up and to the right, which is how people like to film stuff. If the person's moving, if the camera's moving, you know, there's challenges there.

**[00:13:26]** But so mostly what I was learning from that was how to work with video, how to work, you know, basically doing like computer vision based programming. The only. And you know, I was doing, working with a single video with hand labeled data points. And so, but, but keep in mind that at this point I was already getting a postdoc. I had already gotten a whole PhD where I was doing research using traditional motion capture, like a Vicon system.

**[00:14:00]** So I had already kind of internalized like the basic geometry of like oh, you have all these cameras and they're calibrated and if you project you can get the 3D stuff. So I was kind of, it was a lot of kind of percolation happening where I had sort of this long experience working with motion capture, you know, bicom based stuff in my grad school. And then in my postdoc I was working with like imu, like sort of like a suit that you wear as opposed to having cameras and then making these sort of like video based things. I was also working with eye tracking which is all video based. So sort of like the pieces started to come together and then also like another important factor there and the reason why you saw the video was I started getting, I have some experience in like publishing like viral video clips online.

**[00:14:50]** Like what is the Internet? Like how does it like to see stuff like what are the things that people respond to, what are the things people don't respond to? And that is its own weird skill that I wouldn't have expected to pick up. But you know, and then again the pandemic happened and some, you know, the things came together. So all of those factors of like basic understanding of motion capture, basic understanding of human movement, you know, basic computer vision Basic understanding of how to like, market on the Internet kind of came together into this system.

**[00:15:28]** And when did it become free mocap? What was your thinking behind making it open source and giving it that name? So that was an interesting moment in my life because basically, so like I said, I had been sort of thinking about making a system like this for years and just never really having the time to put it together. And when the pandemic happened and my sort of, well laid, my whole research plan basically just collapsed on itself. I had a bunch of students working for me and I was like, all right, well the only thing that we had, and one of the students I had given this task of like, let's use GoPros and we'll just, we'll see if we can get this to work.

**[00:16:14]** And my plan was like, he would work on that while we were waiting for some equipment to come in. And then we sort of focus on like the quote unquote, real work. And then the pandemic happened and all of the plans that I had, every one of them evaporated except for this one. This was the only one that we could actually work on from home.

**[00:16:34]** So we all kind of worked together to make this system using GoPros. And the plan at the time was get it working using GoPros and then steer in the direction of sort of more like fancier, expensive, like research grade cameras.

**[00:16:54]** And right around the time that it started working with GoPros, the George Floyd protest started happening in America. And all of a sudden I was sitting here introspecting pretty hard about all the sort of rights, privileges and responsibilities that I am sitting in now as a professor, as a white man in power in America, with all of this scientific and technical knowledge that the American taxpayer paid for. And I started kind of thinking, well, maybe it's not the right move to steer this in the direction of more expensive cameras. What if I steered in the direction of the cheapest possible cameras? Because also around that time I realized there really aren't a lot of options out there for low cost motion capture.

**[00:17:47]** It's like people are still talking about the Kinect, which is like a dead technology that has been unsupported for like 10 years. And I'm sitting here, you know, I discovered Blender, which sort of really opened my eyes to like the power of the open source community.

**[00:18:04]** And so, you know, so I was sitting there like, okay, I remember I was looking for, like, I was looking for tutorials on how to load motion capture data into Blender, and I wasn't finding them. And then eventually I found there's this guy. Royal Skies is like a YouTube guy who finally made like here's how you use Kinect for Blender. And watching through his videos and especially like his final sort of like wrap up video is when I realized the reason why I have been finding mocap tutorials for Blender is because the people who are using Blender can't afford motion capture in almost any form. And so, okay, so there's this need, there's this gap.

**[00:18:45]** And in terms of like, you know, meaningful, like social problems, inaccessibility of motion capture technology is maybe not at the top of the list of like injustices in the world, but it was one that I could, you know, directly affect from where I was sitting. So it was originally called Open mocap. And then I got a little more. I started reading more into sort of like the Free Software versus Open Software debate and you know, sort of thinking also there was already, there was already a repository on GitHub called Open Mocap. It's like a dead repository from like eight years ago.

**[00:19:23]** But then I was like, you know, I might as well just go pretty aggressive on the open source thing and call it freemo Cap, in my brother's words, if I saw Free mocap and Open mocap next to each other, I'd pick Free mocap first.

**[00:19:37]** Well, it kind of works both ways, doesn't it? Because it's free as in open source. But then you're freeing the process up for.

---

### Chunk 3 [00:19:30 - 00:29:29]

**[00:19:30]** My brother's words, if I saw free Mocap and Open Mocap next to each other, I'd pick free Mocap first.

**[00:19:37]** Well, it kind of works both ways, doesn't it? Because it's free as in open source, but then you're freeing the process up. I'm assuming that's. You enjoyed that. Yeah, yeah, it's pretty on the nose.

**[00:19:52]** But John, I think what would be great for readers, listeners, sorry as well, is like if they got their hands on it, what does it provide them? What do you do with free mocap? How do you set something up to shoot a mocap scene? So if you got your hands on it now, you'd have. It'd be a bit of a struggle if we're being honest, but if you got your hands on it in like a couple months to a year, it's basically you set up some cameras.

**[00:20:20]** Right now it's all focused on these like $20 USB webcams. Hook them up to your computer, you know, point them at the subject of the scene, you know, push, record, hold up like a calibration board, which is like a checkerboard with some, you know, they're called fiducials, the like trackable patterns in the middle there and then do the movement and then what. Get what comes out of that is a reasonably accurate recording of the. Basically the skeleton of the person in three dimensions. So like, you know, I'll basically think about the three dimensional trajectory of each one of your joints in space gets output from this system.

**[00:21:09]** We haven't really done much by way of like the formatting, but the idea is to make it sort of compatible with your blenders and your Mayas and your Houdinis and whatever else, whatever the software you want with the idea being, you know, for me as a scientist, that's the data that you want to analyze, to look at whatever kind of neuroscience question you might have. But if you are an animator or a video game designer, those are also the motion capture assets you would use for your animation scenes or your video game assets, whatever it is that you're doing with that. Right. And you've set this up. But as you mentioned before, it's.

**[00:21:48]** Unless I've got this wrong, it's leveraging on open pose and possibly other tools as well, isn't it? Yeah. So Open Pose, MediaPipe and Deep Lab Cut or the. And then any pose is doing the camera calibration. So yeah, it's actually in terms of like, we're actually writing very little, like meaningful sort of heavy lifting code over here, little to none.

**[00:22:12]** It's basically the task that we're doing is the way that I think about it is like we're trying to provide a framework so that other people can take advantage of all these technologies without having to spend four years sitting on their couch banging their head against their laptop, trying to get the dang things working. Because like I was saying, like, there's all of this amazing stuff coming out of the computer science, computer vision community, but you got to think about the people who are making it. They're all living in survival mode too. They don't have the time. It's hard to make code usable by the general population.

**[00:22:55]** I'm mostly just trying to make that connection easier. This is a lot inspired by Deep Lab Cut, who I think have been doing a similar task to, to connect really like high level computational neuroscientists to the same kinds of community for, mostly for like animal tracking, for like neuroscience research. And so I'm kind of pulling a similarish move, but instead of connecting computational neuroscientists to, you know, computer vision researchers, I'm trying to connect general population to those same kind of communities and again, just trying to make it so that the general populace can take advantage of all these really amazing advances that are coming out. Which right now they are free, they are available, but there's this huge technical barrier to being able to use them. So I'm just trying to smooth out that transition a bit.

**[00:23:51]** And because it is leveraging on those other tools already in existence, does that mean, because you mentioned machine learning previously, that it leverages any machine learning implementations that the other tools have? Yeah, oh yeah, it's. It uses them directly. Yeah. So which also means that it inherits their licensing.

**[00:24:12]** So open pose has the most challenging license wise. It's free for commercial stuff, but it's like Deep Lab code, it's open. And MediaPipe is a Google project, which is also open. But that's actually sort of a secondary aspect of this, is considering it as almost an educational tool to say, hey, here's like, so here you are, you're a person, you just want to record some people moving for whatever reason you might have to do that. And everyone has their own reason for wanting to measure people.

**[00:24:45]** So the goal for me as a scientist and as an educator is to make a tool that allows you to, to use these new technologies to do the thing you want to do with as little effort as possible. So that way, but also like expose to you as much of the underlying technology as I can so that you, who previously had no familiarity with this stuff, now have a little bit of familiarity and sort of the idea is that if you use this for long enough, eventually these things will just become familiar and you will sort of pick up some familiarity with this sort of like really important and emerging technology just by way of your own desire to do the things you wanted to do that involve recording humans. So that's something that I, you know, as a, as an educator, that's kind of an important part of this project is making sure that it does do both of those things. And it's also, interestingly, like something that as an open source developer, I am freely available to do because there's a lot of proprietary softwares that do similar stuff, but they always have to reach a point where they have to hide some level of their operation from their users, because their business model is to some extent predicated on their users never understanding how their software actually works. Whereas for me, I want you to understand every piece of it from top to bottom.

**[00:26:19]** That's a fun thing about working in this space. The other cool thing I think for the moment is the Blender ui. And that's, I guess, as you mentioned, part of the open source thing, but also that you felt it was accessible. Are you looking to change that or open that up or allow it to be in other tools as well? Oh, absolutely, absolutely.

**[00:26:42]** Like, Blender is very much a, is, you know, I'm pointing straight at it right now from a sort of development standpoint. I've been focusing almost all of my efforts recently on just like the core components of it, the core Python bits, just because, like, it has to work and ideally it works in the most generalizable way that you can, which for me means Python. But now that it is starting to work and starting to stabilize, connecting it to Blender is, you know, or basically that community is a very big part of the next sort of phase. And I think the first part of that is just going to be like a file reader, just like reading the data into a Blender scene. But I have like half of a broken Blender add on that will continue to be developed.

**[00:27:36]** Because I think that, you know, I was very like learning, learning about Blender, really. I found, I found it to be very inspiring, just sort of like the story of how that software was developed. And it really, it struck me as just like the right way to do things. Like the open source community is what the scientific community pretends to be. And I think that we should really adopt more of that model and I think that, you know, one of the beauties of the open source community is that if you, if you are working on an open source project that's related to another open source project, you just combine forces.

**[00:28:11]** And so that's now that FreeMokApp is starting to be more of like a stable process, you know, table software that actually works. Connecting it to, you know, something like Blender is a very big part of hopefully next, you know, call it next, let's call it the next year. By this time next year there will be some meaningful blender integration. You can heard it here first. It's very early days.

**[00:28:37]** But has, has anyone been experimenting with this and showed you any results?

**[00:28:45]** At this point I don't have any evidence that any other person outside of my lab has successfully gotten it to work, which is nobody's fault but my own because like the documentation isn't really where it needs to be. Like the, you know, the code is still a little spaghetti ish. But you know, I'm moving, I'm hoping to have something like an alpha release in the next couple next one to three months. And the goal of that is this is something that other people could reasonably use right now. It's still like you could use it, but it'd be, it'd be hard.

**[00:29:22]** And this has actually been, you know, with the release, you know, I have been contacted by some more experienced.

---

### Chunk 4 [00:29:15 - 00:34:34]

**[00:29:15]** That other people could reasonably use right now. It's still like you could use it, but it'd be hard. And this has actually been with the release. I have been contacted by some more experienced software developers who are like, hey, this is a cool project. Can you please, can we help you can fix your code, please.

**[00:29:37]** And so I've had a couple meetings with some experienced software developers because I learned Python during the pandemic. Like I was a matlab developer before that and a philosophy major before that. So like this is all sort of very like self taught kind of like seat of your pants kind of stuff that you know, luckily is, you know, I have enough experience that it's not complete spaghetti, but it's definitely going to be the kind of thing like get an alpha out so that something can be used and then basically gut the whole thing and rebuild it in a way that can, that will be more, that can grow in the future. Wow. I'm going to put a link in the show notes John.

**[00:30:21]** But what's the best place for people to check out a bit more about Freemocap? Probably freemocap.org I think I just got that domain recently and it redirects to a page about this, other than that, the GitHub. So GitHub.com johnmathis freemo cap, which has links to the Discord server, which is probably going like I don't know, 5, 600 strong at this point. And that's so. Which, you know, so those are, that's probably like, you know, the freemocap.org is probably the first one to go to.

**[00:31:00]** And then the GitHub is where the code lives and then the Discord is where conversations happen. Oh, I also stream on Twitch, Twitch TV, Freemocap. I've been doing that Thursday afternoons, 4 to 6 Eastern US time.

**[00:31:19]** I do actually love that you've sort of taken advantage of the viral or the sharing side of all this. It's nicely unusual and I think that's a fun thing that you're doing. It's been fun. I mean, you know, and it's kind of like, you know, to be perfectly honest, like I feel like if you're sitting here in 2021 looking at the future and you're no. And you don't feel like you're staring on the barrel of a gun, you should probably maybe pay better attention.

**[00:31:52]** So a lot of this kind of like viral sharing stuff is just kind of like you got to spread it out, you got to get it out to the people and you got to Give it as many hands as possible because I, I don't trust the ivory tower that I work in to do the right thing. So this is a lot of, you know, I'm thinking about, you know, I'm pitching, I'm a scientist pitching to the general population. And ideally I'm pitching to people at or below me on the social hierarchy, whatever that means. And often what that means is young people. Like, I feel like if I can get this into the hands of some young indie developers, some interested athletes, performers, dancers, whoever, give them this thing that they want.

**[00:32:38]** Everybody has a reason to want to record a person. And if accidentally, through the execution of their own desires, they learn a little bit about computer vision and AI and technology and science. That's probably a good thing.

**[00:32:59]** That's all I got sitting here as a white man in power in 2021. That's what I got. I like it. Now, John, the most important question is in your demo video, are you the juggler on the balance board? Right.

**[00:33:16]** I am the juggler on the balance boarder. I got a lot better at juggling over the past year and a half.

**[00:33:25]** And yeah, like I said, I've, you know, I've been hanging out with circus performers for, for a number of years now. I am not on. Like, I have friends who are so far beyond my level, it's unbelievable. But I can hang and I can juggle and that's part, you know, like that's, that's how you. What I know about how to go viral is you put some.

**[00:33:48]** The way I, the way I do my thing is I put stuff out there that doesn't over explain itself. It's just kind of eye candy and you stare at it and the longer you look at it, the more you see. And ideally what you see is what you are interested in. There's enough going on there that some part of it is going to attract your attention. And some people are into the tech, some people are into the mocap, some people can't get over the juggling.

**[00:34:15]** And I'm here for all of them. Nice. Well, it's been really fun talking to you about free mocap, John, and hope people can check it out. There'll be plenty of links in the show notes. Thank you so much for sharing that info with me, John.

**[00:34:31]** Really appreciate it. Yeah, thank you for your interest. Thanks for asking the questions.

---
