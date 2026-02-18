# Transcript: 2024-11-23-[HMN24#08] Intro to My Dumb BS (visual control of foot placement when walking in rough terrain)

## Source Information

- **Source Type:** Local File
- **File Path:** `C:\Users\jonma\syncthing-folders\jon-alienware-pc-synology-nas-sync\videos\video_eater_downloads\playlists\Neural Control of Real-World Human Movement (Fall 2024)\2024-11-23-[HMN24#08] Intro to My Dumb BS (visual control of foot placement when walking in rough terrain)\2024-11-23-[HMN24#08] Intro to My Dumb BS (visual control of foot placement when walking in rough terrain).mp4`

---

**Total Duration:** 01:32:21

---

## Full Transcript

### Chunk 1 [00:00:00 - 00:10:00]

**[00:00:00]** Okay. Hello everybody. So by now you all should have completed about the second draft of your final project. If you haven't started that yet, you're the only one, so probably you want to get on that pretty quickly. No, I'm just kidding.

**[00:00:19]** You're all good.

**[00:00:22]** There's no official final project. I will sort of make up some sort of arbitrary rules around how many words you must have put into the server and I don't have those numbers yet, but just if you haven't put any. Talk to the bot about anything. And the beauty about the way it's set up is if you're talking to it, it's on topic. It doesn't talk about things that aren't relevant to the class.

**[00:00:50]** I think that the. The global project of this class is exploring that space. And so if you're contributing to that, then you're contributing to the project.

**[00:01:04]** This is the third to final class, the anti. Penultimate class, if you're into that kind of thing.

**[00:01:16]** This class I am going to be talking about my own personal research program. The things basically just going through the papers that I published on the topic of visually guided locomotion, which has been sort of the thing I've mostly worked on until, you know, basically COVID ruined everything. It didn't ruin everything, but it certainly changed things. Maybe ruined it. It's hard to say.

**[00:01:39]** Time will tell. And yes, we're going to go through that feels very strange sort of talking about. It's just historically I've just learned it's like it always feels really narcissistic to talk about my own work. But it's like also like that's a stupid reaction. That's the thing I'm most qualified to talk about.

**[00:01:58]** And it's been peer reviewed so it counts as sort of. It's part of the global conversation. So it's worth valuable to talk about. Not that that's really the only metric there. So yeah, so today we're going to talk about that in the spirit of things.

**[00:02:12]** It's going to be a pretty sort of fast sort of journey through it, but you'll have a lot of background to understand both the context of what was going on and also you now have kind of the backside view of the story that happened. These are papers that first one's from 2013, when I was in grad school. First one we'll talk about. Although I have some. I might reference something before that.

**[00:02:37]** But yeah, it's kind of like the very strange broad swath of topics that we've covered is the things that I have kind of picked up along the way, not including the sort of open source software bent, which was sort of. That was the transition that happened when I sort of lost faith in the academic system. But still I participated fully in the academic system. And we'll talk about that.

**[00:03:04]** Next week is Thanksgiving break, so I understand how that tends to go. So it will be like a slightly off topic topic lecture that I have referenced before and I'm gonna. It's gonna be basically about the neurophysiological effects of most. Let's say in a more topic appropriate way. It's gonna be talking mostly about like sympathetic parasympathetic nervous system sort of layer.

**[00:03:30]** Like the sort of. The deep, deep layers of your nervous system. On a practical perspective, it's going to be about the sort of neurophysiological effects of trauma on the body. It is technically relevant to the topic of the course as everything is. Which is kind of part of the main joke of the title.

**[00:03:47]** But I wanted to talk about it just because it's like there hasn't really been an area of neuroscience that I've learned about that has had a more profound effect on the way that I look at myself and the look of other people and the way that I generally interact with humans than that particular topic. So I am both taking the opportunity to put those thoughts into kind of lecture form and also sharing them in sort of a public service announcement style of talk. So if you're not going to be here, that's fine. Everything that happens is recorded and put online. And the playlist of that is in the resources channel right there.

**[00:04:29]** And you know, the audio should be okay after I started wearing this thing. So. But I haven't actually watched them. So that's kind of on you. And then on the last day of.

**[00:04:40]** And the class after that is the last class of the semester. There is no final. So if it's on the schedule, that's just free time for you. And so I will take the last. So the last lecture of the semester will basically be me presenting my project to.

**[00:04:56]** To you. Sort of a finalized version of finalized in the sense that anything gets finalized in the course of a semester. But let's just. The final version of the sort of ongoing presentation I've been making every week where we sort of scrape the bot and put the things online and look at stuff. So because of that I'm going to stop kind of putting too much attention into like, hey, let's look at this big cloud of words.

**[00:05:23]** Because it is now getting to the point that the cloud is so big that it is hard to really. It's becoming hard to make sense of in its current form. So I'm not even going to bother looking it up. So I'll stop talking about that so much this time and next time. And then on the final day, I'll give the last half sort of like the one last look at it, presenting it in a form that you all will be able to play with.

**[00:05:55]** I talked about this at the beginning of the semester, but I will show you how to set up your own Skelly Bot servers, if you are so inclined. It's basically click five links and then you have your own version of this thing, if you so desire. And then leave time at the end, like the last half, for sort of the talking about what you guys are interested in, what you guys got out of it, that kind of thing. So sort of prepare yourself emotionally to speak in class. If that happens.

**[00:06:26]** I'll turn off the recorder during that time because I know that's uncomfortable. Yeah. So that's about the trajectory, and hopefully that will not accrue too much additional stress into what I'm sure is already the standard level of this time of the semester.

**[00:06:48]** Cool. Okay. Anything else to talk about? Nah, I think we're good.

**[00:06:58]** Okay. So how do I talk about all of this? So, long story short, I got my bachelor's degree in 2008, and I was studying in philosophy. I have a bachelor's of arts in philosophy as my first degree and was focusing on things like philosophy of mind, philosophy of science, philosophy of language, had a sort of this evolution of cognition, bent to it and applied for a bunch of grad schools in philosophy, and by grace of God, was not accepted into any of those programs. And then year later, I sort of retooled.

**[00:07:42]** I got a job at an autism research facility and learned that data is kind of cool. It's cool to say things for reasons like empirical stuff is neat, measurements are nice. And so retooled my applications and wound up. I applied to a bunch of programs in cognitive science, mostly applying for, like, psycholinguistics and natural language processing, stuff like that. I also didn't get into any of those programs.

**[00:08:08]** And it just turns out that the one program I did get into did not have a language person on hand. So I wound up working instead with my advisor, Brett Fajian. I literally just looked through the list of people said, because I was doing, like, the thing right, the personal statement had just, like a blank spot for each school Like, I really am excited to work with professor so and so. And when I was sort of prepared to submit to rpi, that's when I went through and was like, oh, shit, there's no language people here. So I just looked for what seemed like some other cool thing and there was Brett Fagen.

**[00:08:42]** I study visual control of locomotion. I'm like, that seems cool. And wrote him in. And now here we are. So that's also why there's this AI spin on things of the sort of the deeper dives into the natural language processing side of that.

**[00:08:58]** It's not completely out of nowhere. It's kind of fun that that has sort of reemerged in my research life since I sort of had assumed that that was not something I was going to do. So now we're in this sort of fun space where there's the blend of the two things in my experience.

**[00:09:16]** Yeah. So how to. So that's the rough background. And when I. Let's see.

**[00:09:27]** So in the server, in the lecture space, in the 1119 Mathis Papers is the thing this link here will take you to.

**[00:09:45]** It's a folder in the standard repo that's basically just a list of papers that I published, either first or you know, how papers work. So first author. First author usually means, like, that's the student or postdoctor who.

---

### Chunk 2 [00:09:45 - 00:19:45]

**[00:09:45]** It's a folder in the standard repo that's basically just a list of papers that I published either first or you know, how papers work. So first author. First author usually means like that's the student or postdoctor, whoever who did the work. Last author is usually the person who sort of ran the relevant lab. So a lot of these are for me and some of them are people who kind of like followed up on some of my work later.

**[00:10:12]** You can see they have dates and the chronology is roughly. We're going to follow that along. Another useful link for thinking about any researcher is their Google Scholar link.

**[00:10:28]** This is the kind of thing that I know that there is also a PubMed version of this thing. There's a public non Google version of this. But Google Scholar is a. It does most of this automatically and it keeps track of things like citations, which is like 12. That's pretty good.

**[00:10:44]** H index is kind of a fun number. It's the number of papers you have that have at least that number of citations. So I have at least 13 papers that have 13 citations, which is cool. And that's like this. Anything that has this sort of effect of like a leaderboard, like, oh, here's a single number that sort of is supposed to measure some degree of progress is not reliable.

**[00:11:07]** It's sort of a gamified system. The classic thing to say there is once a metric becomes a target, it ceases to be a good metric. So these are numbers that are trying to make it so that you can't just game it and pump the numbers up so you look cooler than you are. But all of them are gameable. And a lot of these numbers, so things like fmri, a lot of medical case studies, they just get huge numbers of citations.

**[00:11:31]** So even comparing these numbers across fields doesn't really work. But anyways, so there's kind of this list of publications cited by is how many papers have cited that particular paper? You can organize by both. A lot of these on the list are not what I would call real publications. Like a lot of these are conference publications.

**[00:11:54]** Most of these that say Journal of Vision, they're published abstracts that I submitted to conferences and they were technically peer reviewed. But if you click it through, it's not even a full paper. It's just like 300 words.

**[00:12:08]** But yeah, and I will talk. So this is the paper that I mostly.

**[00:12:20]** Let's see, can I get this? Do I have. Yeah, this is one of those papers that like, even though it's from 2012, like, I still don't have access to it in many places because of JEP is the SO Journal of Experimental Psychology, Human Perception and Performance. This is a paper. I was on it when I first got to grad school and it's the first thing I did that wasn't really.

**[00:12:43]** It was sort of the start of this stuff. But I didn't have too much. I had ownership over it for sure, but I wasn't driving that particular train. But this was.

**[00:12:54]** See this is even the author manuscript. So it's like figures at the end which I absolutely hate.

**[00:13:00]** I'm actually just gonna. Let's just out of spite.

**[00:13:08]** Yeah, yeah, yeah. See what I'm saying? They don't even. There we go. DOI should do it.

**[00:13:40]** Yay. Good job Sci hub. And also the dark reader extension makes everything dark. I feel like I've said that many times, but I'm always just feel like explaining.

**[00:13:53]** So this was so the. The sort of philosophical tradition that I was raised in in my grad school days is called ecological psychology. Largely pushed by this guy James Gibson who was a pilot in the sort of 70s and I don't know, whatever, I haven't told that story in a while. But ecological psychology. James Gibson generally good stuff.

**[00:14:19]** I think largely a lot of issues with it these days. But it's about looking at. So this is supposed to be like the top down view of a person moving through the world. And this sort of. This is an object that's coming.

**[00:14:30]** And so it's a lot of conversation around like how we can see, like the change of the sort of object, the angles of objects that we can see in the world. And as we're moving and these things are changing, how do we sort of figure out our affordances? Like how do we fit? Like I can. Someone's coming and I'm trying to pass them.

**[00:14:47]** Can I pass behind them or do I have to wait for them to go? Sort of is dependent on like how fast they're moving and how fast I can move. And I can determine, you know, I don't get direct information about where this person is, but I can try to infer some of those numbers by like how quickly they're getting larger in my visual field. Sort of kind of like self driving car styles of math if you think about that. Yeah.

**[00:15:12]** So and this paper was looking at.

**[00:15:17]** So this was like old school VR. This was VR before Oculus, which was a very different affair. It was like a $40,000 helmet that weighed like a kilogram and a half and I had to wear like a backpack and Follow the person around that had GPUs on it and. And the person was walking through. I don't know if there's going to be pictures of that on here.

**[00:15:38]** These kind of like bamboo environments, black and white paper, and these sort of two things were closing and you're trying to figure out, you're clicking a button, they move for a while, then they disappear. And you have to say, I could have made it through that. I could not have made it through that. And then we change all sorts of wacky stuff in the VR environment and do a bunch of weird comparisons and sort of find that there's this interesting relationship between if you crank the gain and sort of make yourself moving faster in the VR space, then you sort of decouple the visual information from your knowledge of your body. And then there's interesting effects that happen there.

**[00:16:15]** So that's kind of the background. And that was sort of like. That was what. When Brett Fajan said on his website, I study the visual control of locomotion, that was the kind of things that he was mostly talking about. So just moving through complex environments and steering and stuff like that.

**[00:16:31]** Very good stuff. But if you'll notice, there's not a lot of physics in that. Like, the biomechanics of the body is just not really present. Like, the model of locomotion that we're talking about here is basically eyeballs floating through space. Like they can move, you can move forward, you can move backwards, but there's no conversation around footsteps.

**[00:16:52]** Like your feet on the ground. Like any of that sort of gravity doesn't show up here. And so as I was doing that and sort of like trying to figure out where I was going to situate within that sort of space, I started gravitating towards those kinds of questions, like the biomechanic Y types of things and.

**[00:17:15]** That. And I also just. Just worth sort of noting because I came into grad school with basically no background in anything. I got accepted into that program because I knew how to write. And at the time I was applying, my professor, former advisor was trying to wrap up the publication, wrap up the dissertation of a math person who was really good at math but not so great at writing.

**[00:17:40]** And I happened to sort of apply at the right time that Brett was like, you know, I think I'd rather teach this kid math than teach another math kid how to write. So I showed up with. Because I showed up with no background in neuroscience or experimental psychology or any. Or programming or any of that. All of it was sort of equally difficult for me, which is sort of how my research program eventually developed into being this like weird mishmash sort of cross disciplinary thing because I didn't have a background to fall back to.

**[00:18:10]** And so I just, you know, I wound up doing a little bit of psychology, a little bit of biomechanics. I wound up sort of falling in with a robotics crowd and things like that. And I think one of my main sources of luck, of which there are many, many in my life, is that Brett was the kind of advisor who allowed me to pursue those types of research areas, even though he did not have expertise in that. Remember he had a conversation with me at one point saying this biomechanics stuff is really good, but you just have to know if you're going to go this route, I can't really help you with that part. And so he helped me with many, many parts of it.

**[00:18:51]** But he sort of was willing to go along with an advisee doing something that was not part of his expertise, which I didn't appreciate so much at the time. But in retrospect, a lot of people wouldn't have done that. So thanks, Brett. I should think about time someday. But yeah, so, yeah, so coming out of that space, there was a couple other publications from that era of the VR type of environment.

**[00:19:22]** I was figuring out sort of my own space within that. And I realized as I was trying to dig up these old videos, I realized that I had posted them to YouTube 11 years ago, so they're actually still on there, which is very convenient.

**[00:19:43]** And like I said,

---

### Chunk 3 [00:19:30 - 00:29:29]

**[00:19:30]** And I realized as I was like trying to dig up these old videos, I realized that I had posted them to YouTube 11 years ago, so they're actually still on there, which is very convenient.

**[00:19:43]** And like I said, so I was like, was still. I'm kind of like a big hiker, backpacker type of thing. So when I was like, before I went to grad school and I was, I was like on a backpacking trip with my brother thinking about like, what am I going to study? The foot placement over rocky terrain thing was very present because I'm like walking over rocky trails with a backpack on and stuff like that. And so that became kind of the domain, that connection between how do you navigate through complex environments and then how do you sort of make sense of the fact that our visual system is sort of grounded in this very sort of brute force physical reality.

**[00:20:22]** Trying to understand how those parts fit together became a part of my sort of main research program. And I wound up sort of again, in retrospect, I now realize that virtual reality is very closely related to augmented reality and mixed reality or something like that. So I didn't really think about that at the time, but in effort to try to understand how that foot placement stuff came in, originally tried to do it in VR. But there's a lot of weird aspects of having like stuff on the ground in VR and near space and far space. And again, it was a very different time.

**[00:21:01]** The VR was much harder to work with. It's still super hard to work with, but it was even harder back then. So I came up sort of, I can't remember exactly how with this idea to put a projector on the ground, which I think at this point I can share. I think statute of limitations have passed. I found that projector by going into it.

**[00:21:25]** We had moved into this lab space of somebody who had recently retired and I. 11 years is beyond statutes of limitation. I just went into like an empty conference room and like literally took the projector off the ceiling. And that's the projector that I used to write my dissertation. So this projector was basically one of those in an office that wasn't being used.

**[00:21:49]** And like some years later like someone else moved in and I could like overhear them in that conference space. Like, oh, that's weird, there's no projector. We should get one. Then they replaced it and we're good. So just goes to sew, steal things.

**[00:22:00]** There's never a consequence. I don't think that's the lesson. But in this case that's what Happened. So this is me in a 360p video. You can kind of see in the background.

**[00:22:15]** Oh, I guess it's going to loop. Is it going to loop?

**[00:22:22]** So this computer back here is running Vicon.

**[00:22:30]** And you can't. I don't know if you can see them, but like these cables here, like a Vicon based motion capture system. And I'm wearing like the Spandex with the, with the reflective dots and the projector is being controlled. I can't remember what program was controlling it, but Yuli Vigdorchuk was an undergrad who wrote the code for it, which they.

**[00:22:53]** And basically what's going on? Just maybe slow this down.

**[00:23:01]** Is it. So the motion capture system is detecting the location of my feet, specifically this marker on my foot, and comparing it to the location of these projected squares on the ground. And then if one comes in contact with the other, it sort of changes, changes its color. It plays this little sound and then logs it as a collision. And then the instructions.

**[00:23:25]** And so this is basically you just put a bunch of random dots on the ground and you tell the subject participant, I'll never get that out of my mouth. But the participant to walk from one end of the room to the other and don't step on any of the little squares of light. So you're in sort of simulated color. Complex Terrain. The original title of which paper?

**[00:23:47]** Not that one.

**[00:23:51]** Oh, I guess we can go on to this. The original title. Nope, that one. There's this unfortunate phase where this 2013 paper came out was after this one. But the peer review process for this one took so long it's published second.

**[00:24:07]** So the 2014 paper is actually the original.

**[00:24:12]** And yeah, the original title was Over Rough Terrain. And then a reviewer complained and said, it's not really rough. And I said, okay, so I change it to Complex Terrain. And so the instructions were walk from one end of the room to the other without stepping on any of the top obstacles. And then we recorded the body and the collisions and the speed and stuff like that.

**[00:24:33]** And so this was the. And I guess we're playing slow now. Yeah. So this is at half speed, very short space. It's about five steps, but it's what we had.

**[00:24:44]** And then. So that was the full vision condition. So that's walking with as much vision as is available. So we would assume that that's going to be the highest performance that you would expect to see. And then, because then we added this additional check of just detecting where the person was.

**[00:25:01]** So specifically the take the average position of the head, put it on the ground, draw a circle around it, and then only show obstacles that are within that range. So as I'm walking through the space, it's the same, it's actually different in different terrains, but now they are only visible within some available distance. So we can then do kind of like a parameter suite type of experiment where you start with full unconstrained vision and you get some metrics of performance. For performance. We're going to call things like collisions, like how many times did you hit the things I said not to hit?

**[00:25:39]** And walking speed, basically, which is a whole other conversation around preferred walking speed and stuff like that.

**[00:25:49]** And then we can. Where did I put that? So it's here probably. Yeah, see, there you go. Look at that.

**[00:26:02]** Figure 1 is the methods figure, because I was trained well.

**[00:26:08]** More pages. I don't know why I'm doing this on my local thing there, but basically. So full vision would call about five to six steps. And then you can then limit the visibility window according to sort of estimated step length, which is roughly like 0.7 times your leg length. And see how measurements such as mean number of collisions and normalized walking speed vary as a function of that sort of look ahead distance.

**[00:26:38]** And I call this kind of a parameter sweep experiment because you get to sort of just take one number and kind of like turn the knob. And it's a nice way to run an experiment because there's no, there's no real hypothesis there. Hypothesis testing is bad. If you didn't know that that's not how we're supposed to do science anymore. Look it up.

**[00:27:00]** The new statistics is how you can start that, which I guess at this point is like 15 years old, but still. But you're kind of like, you're guaranteed to find a result here because with full vision, that's best performance. What else could you possibly want? And if you turn division down to zero, you're just going to be walking basically at chance and hitting random obstacles. And so the question is, at what point when you're turning that knob do you start to see a deviation from full performance?

**[00:27:28]** And in this particular case it was around 1 to 2 ish steps. And this little guy is a significant difference. And that's why you're not supposed to use p values, because that's not relevant.

**[00:27:41]** Whole other conversation at this particular phase. I discovered when I was doing this particular experiment that actually the instructions that I was giving were loose. And what was happening was that. So I did whatever, 12 subjects or participants or whoever and the results were, were valid, but there was a little bit of murkiness to them for other reasons. And I realized that the instructions that we were giving had a bit of, had too much play in them because we basically just said walk from one end of the room to the other as well as good performance as you can.

**[00:28:22]** And what was happening was that people were basically adopting one of two strategies. One group was saying, ok, I have to make sure I don't hit any of these obstacles and I'm willing to slow myself down in order to do that. And so their walking speed would drop, but their sort of stepping accuracy stayed pretty good. And then another group was saying, I'm just going to walk at full speed and just do my best to avoid the obstacles. So they're prioritizing their walking speed over their accuracy.

**[00:28:52]** And so if you split the data apart, you would get these sort of like, sort of slightly cleaner results. And so future later studies in that sort of regime, I just set a minimum time, so you had a minimum time to get from one place to the other, which basically forced everybody into this preserving walking speed strategy, which made more of this signal sort of show up in the stepping accuracy, which is sort of a fun lesson in why instructions are important.

**[00:29:28]** But yeah, and then I.

---

### Chunk 4 [00:29:15 - 00:39:15]

**[00:29:15]** Which made more of the signal sort of show up in the. In the stepping accuracy. So. Which is sort of a fun lesson in why instructions are important.

**[00:29:28]** But yeah, and then I.

**[00:29:31]** Okay, yeah, here's. Here's the origin of Skelly. That's the first Skelly. Aaron. This was a. I don't know if I can find it really quick, but this.

**[00:29:41]** I had read a paper by art Kuo from 2007 and he was. It's a biomechanics paper and he was using like a skeleton to sort of show the person moving. And I was just kind of like, yeah, no, that's right. There's like the physics is important and it's represented by the skeleton. And so that was kind of the origin of why everything has a skeleton in my life.

**[00:30:04]** And this also, I believe statutes of limitations have passed. The original vector graphic that I got this from was like back before I really understood intellectual property. I understand it now. I just don't respect.

**[00:30:20]** Was like a sample reel from a tattoo artist in Florida who had a bunch of skeletons doing strange things and saying, if you want to get this tattooed on yourself, you can. And most of them were front on, but there was one side view and he was holding a. Had a cowboy hat and had a pistol. So that's the origin of this particular guy. So if you know that guy, tell him thank you.

**[00:30:46]** Tell them thank you. Because I absolutely never gave them credit. I don't think I could ever find them again if I wanted to.

**[00:30:56]** But. So the idea was. So what? Basically this paper. Because there was overlap between this paper and the one I'm going to talk about next.

**[00:31:06]** Some of the ideas are here in different forms. But this is also where I was first trying to think about this notion of a center of mass and how consideration of locomotion in this form of a compass gate walker.

**[00:31:45]** Am I gonna find it?

**[00:31:49]** That's me.

**[00:31:54]** That's me again, I will find a little animation of this gif. GIF Tools type gif.

**[00:32:12]** I wish this was a real video, but imagine this is like an actual video of a thing. So this is called a. It's a compass gate walker. Sort of like there's a citation there for like one of the first sort of considerations of it. But like there's toys that do this, like little like tinker toy, like sort of like wobbly feet things.

**[00:32:33]** Sometimes they look like penguins. They kind of like wobble back and forth. But these are. This is a physical model of something. It doesn't have a controller.

**[00:32:43]** It doesn't have a motor, it doesn't have sensors. It's just the shape is such that if you put it on a slope of the right kind of angle, it will generate this gate and the gate is not particularly stable. It will fall over if you nudge it. But it has this kind of like very human like quality. I'm actually going to look Steve Collins Passive dynamic.

**[00:33:10]** Yeah, there we go.

**[00:33:16]** This 27 second video was very formative in my life.

**[00:33:24]** This is a baby Steve Collins who is now a professor at Stanford or something like that. And this is him with his. I think he was an undergrad at this point.

**[00:33:38]** Passive walker. At Andy Rowena's lab. Both of you met Andy. Aaron, you meet Steve I think. But this is again a walker.

**[00:33:45]** It's got no motor, it's got no sensors, but it can walk down this sort of particular regime of slope. And it has this like very natural appearance. Like it looks like it. There was something about just like that looks like people. And that was enough I thought to myself as I saw this thing.

**[00:34:09]** And so that sort of started this kind of consideration of like how is it that we may be able to exploit our sort of base level physical reality when we are controlling our bodies using visual information in our nervous system and stuff like that.

**[00:34:31]** Do to do. And now it will move back to local copies of things.

**[00:34:49]** Oh actually you know what, it's actually better to keep it online because then I can click on the links more easily.

**[00:34:59]** And so then this was very exciting time for me to get published in this little guy. Very, very similar experimental design but with cleaner thoughts because all this was done after the first one, even though the publication dates are different. And so this was starting to think now about this little symbol typically means center of mass. And this is sort of an inverted pendulum arc that you might take. We'll see a better version of this figure later.

**[00:35:30]** But there's this idea that during your single support phase you're following this. You're not. It's not like a fully ballistic, not like your nervous system turns off, but there's a lot of momentum to your body. And if you keep your leg relatively stiff, which we do, we don't like to walk with a straight trajectory. Even though you will still read clinical textbooks that say that the up and down movement is wasteful.

**[00:35:54]** It is not wasteful because we're exploiting these pendulum dynamics. So this is kind of like the basic physics. Mechanical exchange during walking on flat ground with no targets on the ground. And so there's this sort of body of literature that suggests that humans are exceptionally good, we are exceptionally efficient locomotives, like we are top tier of the planet. It's like us and horses, which is why we like to ride horses.

**[00:36:23]** Even when I said that birds are better at being bipeds than we are, mostly in terms of agility and speed, in terms of energetic cost, distance traveled, we're pretty high on that list of all animals of just the ability to walk without burning a ton of calories. And, and the body literature in this area suggests that a big part of that is because we have this sort of capacity for exploiting these physical dynamics in order to move with sort of like highly efficient movements. So same basic picture there.

**[00:37:04]** And yeah, so this was looking at the center of mass trajectory during the different trajectories. Again, so this is the same basic manipulation, except now I'm doing half step increments. So there's more conditions. And there was a minimum walking speed, so you don't see, only people were sort of more specified there. So there's this result that you kind of like around the 2ish distance things start to level off, suggesting that your speed gets back to, you know, 0.95, which is slow for walking, but it's a small space and your collisions sort of get close to zero and same kind of thing.

**[00:37:48]** And so the idea was this was sort of the origin of this idea that comes up later of looking by the time you can see. So if what you're trying to do is control this ballistic traffic trajectory and you're trying to sort of send your center of mass down a path that will allow you to sort of hit a particular target, then what you need to be able to do that is to set up the initial conditions of this step appropriate for the train that's coming up down the road. And so in order to set up the conditions of initial conditions of this step appropriate for this terrain, you have to see this terrain before this step hits the ground, which puts you about here, which is about two and a half steps ahead. So I really don't. I moved very rapidly away from like the step counting thing.

**[00:38:35]** And I still see people citing me saying like, oh, math is whatever says that we need to see two steps ahead. And it's like it's really not about the number of steps. It's just kind of this physical dynamics thing.

**[00:38:47]** But I was there, is there videos of this one? I don't know if they will. I don't know. There was sort of a point in time where they made it really hard to publish videos, so I don't know if they were here, but I.

**[00:39:04]** Where was it? Yeah, so this was a. I had, like, a simple mechanical model of a pendulum, and I compared it to the program.

---

### Chunk 5 [00:39:00 - 00:49:00]

**[00:39:00]** I.

**[00:39:04]** Where was it? Yeah, so this was a. I had like a simple mechanical model of a pendulum and I compared it to the person's step and then found that when you didn't have that look ahead distance that you want, your body's trajectory diverged a lot from that sort of basic physical prediction, suggesting that rather than using the nice momentum of your body, you are basically using your muscles to fight against physics to put yourself in the place you need to be, which works. I mean, people don't just fall apart when they can't see enough ahead. But the assumption here is that this is energetically costly because you're fighting your physics, whereas out here your physics is very much, you're exploiting them and taking advantage of the inherent momentum going on there.

**[00:39:58]** And then blah, blah, blah. So, and this was a. So that was fine. So we kind of get this distance of like you have to see about two and a half steps ahead, you know, basically, so you can sort of see far enough ahead to take advantage of your base level physics. And then this.

**[00:40:25]** Getting now into this 2015 paper or journal of vision, same basic idea. So I switched away from doing obstacles. So rather than like avoid stepping on the obstacles, it's step on these specific targets. And they were these little circles that are about 0.5 centimeter, sorry, 30 centimeter radius.

**[00:40:48]** And.

**[00:40:53]** They were typically there was like a white noise texture under here, but it was turned off here. And so here, rather than looking for. How often do you hit the things I said not to hit? It's like measuring how accurately you can place the ball of your foot on the specific dot. And now we had invisibility triggers.

**[00:41:09]** So whereas before they were turning on, now they are turning off. And so as you're stepping towards it with like a 70 millisecond lag between the systems, the targets would become not visible. And so that previous one was showing a 0.5. So it turned off as your foot was swinging towards it.

**[00:41:33]** This one, it turns off basically as your foot is leaving the ground from the previous one, it disappears.

**[00:41:46]** And yeah, you're just showing that off. Then this one, it turns off halfway towards the step to the previous target. So again, the same basic kind of parameter sweep of looking at, at what point does your accuracy, stepping accuracy start to be hindered by that?

**[00:42:06]** And then I think in practice we actually added extra distance because there's like 70 milliseconds of lag. So I had to make the distances a little bit larger so that when you take into account the lag, I Don't know who you are.

**[00:42:27]** And we got. Yeah. So here you go. Here's how we did that. Way to go.

**[00:42:34]** This cacophony here. I apologize. I didn't know any better at the time. This is showing stepping error. Aaron.

**[00:42:44]** This should have been a little violin plot or something like that. I didn't know how to do that. So this is every step, I think every step of every step of every person. I don't know. But the stepping accuracy that you would see when you could see the full vision.

**[00:43:00]** Oh yeah, these number. That's what it was. So the numbers were not the even numbers because this is with that lag taken into account. So this is when it turns off when you're, you know, quarter, like just 20, 25% left of the step, no real effect. And then it kind of like grows and then it specifically gets worse.

**[00:43:18]** If you can't see it during the preceding step. I must have given a better figures in that. There you go. So, yeah, so basically the stepping error increases. It's pretty flat.

**[00:43:34]** Like you don't really. Once your foot has left the ground, it already knows where it's going to go. But in that preceding step, that's when you really suffer from not being able to see the target. And again, these aren't huge numbers. You're not going to tumble off the cliff.

**[00:43:48]** But it's a measurable difference. And so you can sort of see what's going on there. Different ways of measuring accuracy.

**[00:44:00]** Yeah. And then people. Oh, there was this like. I don't even remember what this is about.

**[00:44:12]** You can see the use of unnecessary color gradients to let you know that he's outside.

**[00:44:18]** But now you sort of like with those two pieces together, you can kind of like define this sort of like critical range where you have to see it by the. Wait, what is it you have to see? You have to see it by this point at the latest. Must see terrain relevant to step N by this point. I cite myself, but you don't really care about it after this point.

**[00:44:41]** So there's just sort of this range where it seems like that's where the information should be the most useful for getting accurate foot placement.

**[00:44:54]** And then this paper. No, that's 2018. Am I missing it? No. 2017.

**[00:45:00]** No. Oh, did I not get in here? 20.

**[00:45:07]** Okay, well, this is the fun thing about being older. You can just Google yourself. Critical control phase.

**[00:45:16]** You gonna talk about me? Ha. Nice. I made it.

**[00:45:22]** So this paper is in a journal called Proceedings of the National Academy of the Sciences, often abbreviated as pnas, which is funny. My advisor would really work hard to say pnas, but everybody says pnas and like not everybody recognizes that. That is funny. It is funny. Just in case you were curious.

**[00:45:46]** So this paper is basically the long and short of my dissertation.

**[00:45:51]** And I guess they. Oh, it's nice. So this one is publicly, it appears publicly available when we access it through this site, through this university. I don't know, I don't know if it would be elsewise, but this is. So this is that same kind of idea.

**[00:46:10]** And this, Aaron, we talked about this. This is like the linear inverted pendulum stuff. And so same basic idea, too many colors. I apologize. But the idea is like as you are walking and you sort of have these sort of basic pendular dynamics in this.

**[00:46:25]** So the basic physics of like regular walking is that when you, when you're feet hit the ground, the back one is pushing in the direction of motion. The front one, because you tend to step in front of your body, has like a breaking force. So it's like pushing against the direction of motion. And if those two things are symmetric, then they cancel each other out and all you're left is sort of with an up vector that pushes your momentum up. And as you walk out of here, just like key into the fact that there is a feeling of like flow from one step to the other.

**[00:46:57]** And that is kind of what's happening here. You should follow me, Mr. Robot. Thank you.

**[00:47:06]** And so the idea was that if you can sort of, you know, these collision costs are lossy, like you lose energy in this collision. So we tend. So the, again, the literature suggests that we have a push off force from our back leg, partially mediated by just like the springiness of your Achilles tendon, but partially sort of energy driven, like muscularly driven. And so if it wasn't, if these two forces were symmetric, then the energy loss means that you would slow down. But if you just push off a little bit with your back leg, or as those little sort of passive robots, if you're on like a little bit of a downhill, you can recoup that energy loss and then have a nice stable gait cycle.

**[00:47:51]** Or if you're looking ahead and you're saying, oh, actually these sort of preferred footholds are not available. Like there's something in the way, there's a rock, there's a puddle or something like that, you can alter those push off forces to change the dynamics. And so that as your foot hits the ground, you're starting with sort of lesser velocity. And so you'll follow a different trajectory, and that will sort of make other available foothold. So if I am here and I see that this.

**[00:48:22]** Yeah. So I wish I could step here, but I can't because there's mud or something. So I need to either step a little bit farther. Let's say I want to step a little bit farther. So I see that here.

**[00:48:32]** And I say, okay, so in step two, I'm going to push off more so that when I sort of interact my center of mass, like, imagine the center of mass sort of projected onto the ground, that trajectory interacts with a different foothold position, and then I can gear there. All right, that's what it is. I could either change my push off force or change my previous foot location. But because we were prescribing the footholds, you don't really have that option. So this is of kind.

---

### Chunk 6 [00:48:45 - 00:58:44]

**[00:48:45]** And then I can do there. Oh right. So I could. Right, that's what it is. I could either change my push off force or change my previous foot location.

**[00:48:54]** But because we were prescribing the footholds, you don't really have that option. So this is kind of starting to get more of a picture of like the way that we could sort of control our bodies as a function of the visual world. And then here's this not particularly useful picture but.

**[00:49:17]** Oh, and actually do have.

**[00:49:23]** Download. Oh, there we go. Good job.

**[00:49:28]** This was playing way too slow. A matlab based animation. Oh, this is too changing colors when you're in the critical phase of control for whatever the thing is there.

**[00:49:45]** Yeah. And then I'm not particularly a fan of the figures I made for this but it got complicated and we sort of did our best.

**[00:49:56]** But long story short, that hypothesis sort of plays out like it tends to be what you would expect or the. Yeah, where's the critical control phase hypothesis? This was also the first like actual proper hypothesis driven paper that I had done because all my previous stuff at that point had been of my first author publications were these parameter sweeps where it's like you're guaranteed to find a result. This one felt much more like sniping where I was like I have a specific expectation in mind. And.

**[00:50:34]** Yeah, I mean, so the results are again, the numbers are not huge, but there is a effect where basically the. So this particular. So like if you only sort of flashed the targets on during this very narrow phase of gate, these are like 250 millisecond windows. So when you're walking it actually feels. Feels like you can't do it.

**[00:50:58]** But if you look at the numbers, your data is as good as when you have the full previous step and then you see these sort of not huge explosions in error, but performance is worse when you have equivalent visual information at a different phase. Or actually in this case you can see the targets for twice as long. It's just a little too early or a little too late.

**[00:51:26]** So that was fun and da da da. Anything else to show here? Yeah. And then you know, stop experiments and stuff like that, blah blah, blah. If you are curious about kind of like the theoretical aspects of this, the intro to this paper is basically like a review article of like all the stuff I just said.

**[00:51:49]** The experimental stuff I think is fine, but it's not really. It's not necessary.

**[00:51:56]** Yeah. And so then I graduated and then I became Dr. Mathis. It was fun and exciting and yeah, blah blah blah. Long story Short. I wound up going to UT Austin to work with Mary Hayhoe, who was world expert OG person studying eye movements during natural behavior.

**[00:52:20]** And I think I could probably find. Hey, how Eye movements.

**[00:52:29]** Yeah, eye movements during natural behavior. The thing I just said.

**[00:52:34]** And she. That's Mary.

**[00:52:42]** I don't think I'll be able to find the video. She does not have the same YouTube presence that I do, but she studies a lot of things. Like the kinds of eye movements that you make when making a peanut butter and jelly sandwich was sort of her claim to fame. Or like when you're making tea in the kitchen. So that kind of thing.

**[00:52:58]** So she studied eye movements, but she also did not have like a biomechanics Y bent to her. So when I came along, it was sort of like, how do we kind of merge these things together? That was my postdoc. So postdoctoral researchers typically kind of like, they show up. They are not as.

**[00:53:14]** Like they're not students anymore. So you have. It's. You're kind of like a semi independent researcher in a more established researcher's lab. So I had a much more.

**[00:53:24]** So I similarly am deeply indebted to Mary for the freedom she gave me. But it was a little. But also like, I was a postdoc, so that's kind of more. And that's me from the past also. Skelly.

**[00:53:41]** Yeah. So.

**[00:53:48]** That was kind of the end at that point of the sort of the projector stuff, because at the time it was like, okay, great. So we got this nice result, nice dissertation stuff, good publication records and all that kind of kind of thing. But there's this issue where it's like they're just walking five steps in a lab with projectors on the ground. Like, this is not really. It's natural.

**[00:54:10]** Ish. It's pseudo ecological. It's better than sitting at a computer screen. But it's not quite the same as what we would call natural behavior.

**[00:54:22]** So I sent out I. What's the word? So with Mary, and I was sort of learning how to do eye tracking. I was learning basically how to like, do computer vision, how to work with cameras. And it was hard.

**[00:54:42]** It was very hard. The thing that I think I have the most to thank Mary for is that she allowed me to be. To get basically on paper, nothing officially done for the first, like, two years of my. Of my postdoctoral research because I was desperately trying to figure out how to combine natural eye tracking with some form of motion capture in an outdoor environment. And I think I have to go back into the history Books here.

**[00:55:18]** And I wound up using something called. It was an IMU based motion capture system. So it's like a suit of like sensors that you could wear.

**[00:55:29]** And. And then like eye tracking, eye tracker. Like the original one was. It was an older version. Then some of my later stuff was using like the same one that you saw here.

**[00:55:42]** And going a little bit out of order historically.

**[00:55:50]** Do, do, do, do, do.

**[00:55:59]** It wound up looking like this.

**[00:56:05]** No. What are you doing?

**[00:56:10]** I'm more shocked that an ad is able to make it through my firewall of ads than anything else. I just. Yeah. So this is. I can't remember who this was, but he's wearing these little straps are IMU sensors basically.

**[00:56:30]** You can think of them as like fancy accelerometers, but it's more than that. But they're basically giving. Recording his body movements huge pain in the ass. I hope I never use IMU based motion capture again. Robot you must follow.

**[00:56:47]** And then he's wearing a backpack, running the eye tracker. And then this like daft punk shade here is an infrared blocking face shield. Because the IR sensors of eye trackers work great indoors, but you go outside in Texas and all of a sudden there's this huge black body radiation ball in the sky which is blasting infrared. So I had to find an IR blocking face shield that would block infrared, let visible light pass, but not be so dark that you couldn't move around. And so that wound up being a face shield made for people who are teaching people how to weld because the actual welding glasses are too dark, you can't see through them.

**[00:57:33]** So that's for people who are like standing and watching the student. So like a shade 3 instead of a shade 6. This is part of the journey. And they were wearing this so that the eye tracker could still work when it's inside of the helmet. And then this is like a DJI4 drone.

**[00:57:49]** At the time I was like, drones seem like that's an important technology. Mary had some extra money, so I got a drone. And now like watching Ukraine, I'm like, Jesus Christ. I. Yeah, world is horrifying. But that's okay.

**[00:58:05]** So here he is. Here I'm trying to. Also fun fact, that's the high water mark because this is Texas and flash floods happen. So this was, you know, check the weather before you go out type of thing. We did not discuss that in the IRB approval.

**[00:58:27]** And so, yeah, so he's. So here he is sort of. You can see the backpack there walking along these rocky terrain. Shoal creek in ut and his body's being tracked, his eyes are being tracked. And then the question was, that was hard enough.

**[00:58:44]** And then the question.

---

### Chunk 7 [00:58:30 - 01:08:30]

**[00:58:30]** They're walking along these rocky terrain, Shoal Creek in ut, and his body's being tracked, his eyes are being tracked. And then the question was. That was hard enough. And then the question became, how do you combine these two signals together? Which was also super hard.

**[00:58:54]** So the first publication out of this era was in Current biology, Fancy Pantsy paper. And this was the first laser skeleton, which is a full body motion capture with a laser shooting out of its face. So this is the body, these are the feet, and this is the gaze on the ground. And there's kind of like it, like sets, like burn marks. So every black dot is an intersection between that 3D gaze vector and the sort of hypothetical ground plane.

**[00:59:24]** And then the color is a measure of the density there. I'll come back to this in a second, but I have to show you. Was this on there?

**[00:59:55]** Yeah, I don't think it's actually on there, but.

**[01:00:01]** Okay. All the videos.

**[01:00:15]** Where would I have that?

**[01:00:19]** Oh, yes, supplemental.

**[01:00:30]** Oh, Mathis Current Bio Gaze in the control of foot placement.

**[01:00:56]** There we go. Supplemental information.

**[01:01:05]** Yeah. So this was.

**[01:01:10]** So this is arguably the cleverest thing I've done in my academic career because I had to. So the challenge was you have eye tracking data, you have motion capture data, and you know that these eye tracking data tells you what the eyes are doing, motion capture data tells you what the body is doing. But how do you align the two things? Because. Because basically the camera's at an arbitrary location in space.

**[01:01:34]** So how do you identify where things are? And so what I wound up doing is I took advantage of my favorite reflex, which is the vestibular ocular reflex, which says that as you move your head up and down, your eyes counter rotate. So as I move my head up, my eyes move down. And then I just had people stare at a dot on the ground that I measured the location relative to their feet and. And make a cross shape with your head.

**[01:02:02]** You can know from that that they are looking at this point. So the head movement plus the eye movement has to cancel itself out. And then I can do this fun convex optimization to find the orientation of the rotation to apply to the gaze vectors so that the gaze sort of clusters on the location that it is. So play that again. You can see it starts as this big cross, because I'm moving.

**[01:02:31]** This is probably me moving my head in a cross shape. And then as the number gets. As it gets optimized, then it starts to cluster around the location there. And then you can use that to basically align the gaze data to the Motion capture data. And in the standard ways of calibration, you calibrate on the thing that you know the answer to and then you put it into the world and see how that goes.

**[01:03:06]** You use the thing you know the answer to, which is the calibration to. You measure it. And if you get the answer you expected, then that should give you sufficient trust to use that same system to measure things that you don't know the answer to. For example, where are you looking as you're walking through the rocks? And the sort of epistemological trust sort of follows from there.

**[01:03:30]** I think this is actually still arguably. Yeah, here we go. This one. Arguably, this is one of those things where like I had to write a whole paper because you're not allowed to publish a 30 second video. But this video is basically like, I think the main output there.

**[01:03:55]** So this is subject. Oh, it plays at full speed and then again at slow speed. And there's a lot going on here. This is by the way, part of like a strategy I adopted as a cross disciplinary research which I call kind of like shock and awe. Because I was having this problem around this time of my life where I was doing this vision science stuff.

**[01:04:16]** I was doing this biomechanics stuff. But if you go and show like vision scientists don't care about biomechanics and biomechanists don't care about vision. It's like they think it's interesting, but it's not part of their interest. It's hard to convince them to care about it. So I wound up adopting this strategy of just trying to make these pretty flashy videos that put a lot of information on the screen.

**[01:04:39]** That way I can then go give a talk to a room full of whoever I want, say whatever I want. Nobody's going to listen to me while I'm talking because there's too much going on. And as they're watching the video, they find something in the video that is in their interest. And then they sort of, they cue into that and then at the end of the talk they say, hey, have you thought about this thing that I just thought of right now? And I can usually say yes.

**[01:05:01]** And they say, have you done that? And I say no, you should do it. But yeah. So this is the person walking. The dots are the right and left footholds and the gaze is sort of going.

**[01:05:14]** You can see that they're looking around and trying to. This is blinking and stuff like that. This is only look ahead. So this is time versus distance. So you can see looking at the distance of where these targets are going to be, there's these kind of like fixations in places that you don't step, which is either going to be obstacle avoidance or like search fixation.

**[01:05:39]** Some of the more recent research sort of looks at that. And this is like. I kind of like this one the most. This is the top down view. And again, Aaron, you can see this is like that, you know, that curve as of the center of mass as a function of where the foot goes, which is always kind of fun.

**[01:05:55]** And these are the fixations. What is that? Vertical ab movements, horizontal ad movements. You see most of the action's in the vertical because you're moving forward.

**[01:06:09]** And in the interest of.

**[01:06:16]** Obviously I could say much more about this stuff, but there is. Yeah. So the, the experimental design of this. We call this a quasi experimental design because I didn't have too much control over the behavior, But I had people walking in flat ground where, like, foot placement really didn't require visual guidance. It's like a packed earth trail.

**[01:06:38]** You got to look every so often, make sure you're not going to trip over a turtle or anything like that. But you can mostly put your feet wherever you want. This gravelly big, this size of rocks in the medium terrain, and then the rough terrain is the stuff that you saw. And then looking at how the gaze behavior shifts in these different environments as the locomotor task requires increasingly precise visual information to complete.

**[01:07:08]** Again in that spirit of overcomplicated figures. So this is the flat terrain, and this blob is like the accumulation of gaze data at a given distance. So this one, mostly you're not looking at the ground at all. You're just kind of just looking around and looking for birds and cactuses and stuff, because it's Texas.

**[01:07:34]** And this is sort of aligning it to like, the foot that's on the ground. Or you can like, align the gaze to upcoming footholds and see that there's not really a correlation between that gaze blob and the upcoming footholds. Because that blob doesn't really change shape as you sort of look at that. Compared footholds in the medium and rough, you can see that like, if you're looking this is that blob. You're looking a little bit closer in and it's a little more spread out because you're kind of glancing around a lot.

**[01:08:05]** And if you align or do like correlational analysis, doesn't super matter With a different sort of. With a different footholds, you can see that your gaze is more. You know, it condenses and gets peakier when you align to that n plus two step. So you're looking, and you're more likely to fixate your foothold. Like, I'm gonna look at this specific location and then step on that specific location.

---

### Chunk 8 [01:08:15 - 01:18:14]

**[01:08:15]** Footholds, you can see that your gaze is more, you know, it condenses and gets peakier when you align to that N plus two step. So you're looking and you're more likely to fixate your foothold like, like I'm going to look at the specific location and then step on that specific location. Specifically that sort of like plus two range. So aligned with the sort of previous result. But there's some details there.

**[01:08:39]** So kind of a, the result there is sort of like a. It's like cool. That makes sense. It's cool that you got numbers about it and it's cool that it lines up with that particular distance. There are some deeper analyses here about, you know, blah, blah, blah, this versus that and differences in like the first half of the step versus the second half of the step.

**[01:09:04]** And then, and then this sort of fun result was sort of a, this was an unexpected thing that wound up being I think kind of like the main empirical or like theoretical result here, which was that if you look at the look ahead distance, you can see there's sort of the medium and rough terrain wind up being more similar than otherwise. So there's not much of a separation there. But the purple and orange are medium and rough and then green is flat. So basically requires visual information to walk properly. Greenness does not require.

**[01:09:38]** You see, you're looking farther ahead in that flat terrain, but it turns out you're also walking faster. And if you sort of, instead of asking how far in distance you're looking, you ask how far in time are you looking? They line up right on top of each other, which basically means that you're looking at the place that is going to be where you will be in about one and a half or two seconds from now. Which happens to line up with a lot of other results in literature on like hand placement and sort of like hand manipulation stuff that suggest that that window is roughly our visual memory. Like we have all sorts of memory and sensory memory is like how long really specific spatial information lives in our perceptual nervous system before like, you know, you have to sort of look again to have accurate placement.

**[01:10:30]** So there's this, this was cool because like this was not expected. We weren't looking for this. But it just sort of like, oh, actually they line right up on top of each other and just sort of like. And then the number kind of lines up with other parts of neuroscience, other parts of, yeah, perceptual motor neuroscience, which kind of, which is cool and fun and kind of like this is why it's good to do these, like, ecological experiments that are sort of, like moderately controlled and that produce tons and tons and tons of data. Because then you have the opportunity to look at it and sort of like, see these correspondences that you may not have been looking for otherwise.

**[01:11:08]** And. Yeah, so that's fun. Is there anything else to talk about here?

**[01:11:17]** Yeah, and then lots of explanations about, like, how I did it and methods and stuff like that. Lots of extra data, extra numbers.

**[01:11:32]** Oh, yeah. This is the. This is what that calibration process looks like when the actual data.

**[01:11:43]** This looks familiar.

**[01:11:50]** Yeah. I'll just belabor the point here. So this is head orientation, so moving up and down. And these are the. You can see the eyes doing like the opposite movement, but there's not exactly.

**[01:12:00]** So this is like you're using an optimization algorithm to basically find the rotation vector that makes these two things cancel each other out. This is fun.

**[01:12:15]** I would say that this paper is the reason why I got this job, which is fun flashy stuff with laser skeletons. Everybody likes a good video. It's like, I know people who, like, published way more things and got like, way more, but, like, they didn't have cool videos. So it's just. It's harder to make the point like you, it's.

**[01:12:34]** You never want to be in a position of trying to convince somebody that something is good. You just want to show them something that they like and then they'll think it's good for you. It's very, very hard to convince people to care about something that's not their main thing. And if you don't realize that, think about how hard it would be to get you to drop whatever it is that you're doing to jump on somebody else's interesting thing. So a lot of the sort of.

**[01:12:58]** The strategic aspect of a lot of these sort of studies was like, I'm just going to do my thing and I'm going to present it in such a way that other people will see their own interest within it. And then whoever it is that comes along will sort of. I don't have to convince them to care about my dumb bullshit because they will see their dumb bullshit. And then now they like it and want me to be around. So, yeah, I try not to in this point in my life.

**[01:13:26]** I really try to not to be in a position where I have to, like, convince other people that things I'm doing are good, which is also part of my general sort of reluctance to acknowledge authority in all forms. So do. To do.

**[01:13:51]** Yeah. And then Time wise I think I'll just talk about. So yeah, so this is my friend Kate who's a professor at IU now who wound up doing a similar method and looked at people with stereopsis. So people who have amblyopia so sort of misaligned eyes so they don't get good stereo vision and then could also put like a blur filter of one eyes which basically allows typically set up. It ruins your depth perception, your binocular depth perception and was able to find these fun results that when you do that it makes medium difficulty terrain starts looking like hard difficulty terrain which is this result that if you lower the information content of the visual stream performance is degraded.

**[01:14:41]** And so it's this idea of you're gathering information more than you're doing a specific motor behavior. But that's a whole other conversation.

**[01:14:52]** Mathis did I put that one in here either? Mathis Retinal slow. Now for my favorite paper.

**[01:15:04]** This one is going to be a real assault on the old psyche because this goes real deep real fast and I. It would take another. I could probably build you up to it but it would take another entire lecture. So this was me basically going deeper into the. So got a new eye tracker.

**[01:15:24]** This is the people abstracter that you all saw. Much higher frame rate, much higher resolution. And I wanted to get deeper into the questions about the actual visual information that you're extracting. And I'm specifically looking at visual motion. Optic flow is often called.

**[01:15:43]** So the majority of the world is stationary. So if you are looking, if you sort of fixate a point on your table and move your head around, your visual information is seeing motion. When that happens because you're seeing the stationary world is moving relative to your head. And so the motion that comes out of that is very information laden. And a lot of this is like the Jurassic park.

**[01:16:07]** Like its vision is based on movement. A lot of our vision is based on movement. And we tend and we're very sensitive to motion in the scene. It's a lot of our visual system sort of handles that.

**[01:16:23]** And so a lot of this paper is like speaking to theoretical traditions that I think most people don't know about. So it's like one of these things like a lot of it just like wouldn't make sense if you're reading it. Like why are you spending so much time talking about this thing that doesn't make sense. But from a practical perspective the.

**[01:16:49]** Had these head centered videos which is based the camera on the head. Then you can align them so that the gaze is always at the center, which is basically an estimate of like the retinal. This is presumably similar to the information being projected on this fellow's eyeball and then doing computer vision and optic flow estimation, which again these days is like self driving car type of stuff.

**[01:17:22]** And looking at this is a fun figure, just about like showing that like you're a lot of what you're doing with your complicated body when you're walking is stabilizing your head because this is the acceleration at the hips, chest and head. And so you get these big acceleration spikes at this vertical strike is like heel strike. So you get a big spike in the hips, which is sort of like partially damped out at the chest. And by the time you get to the head, it's like a much smoother ride. And that's true in the forward, backward and left to right, but not so much in the vertical.

**[01:18:06]** Like in the vertical, your head is just kind of like along for the ride, which is I just kind of like the figure. I was getting better.

---

### Chunk 9 [01:18:00 - 01:27:59]

**[01:18:00]** Ride. And that's true in the forward, backward, and left to right, but not so much in the vertical. Like, in the vertical, your head is just kind of like along for the ride, which is. I just kind of like the figure. I was getting better at making these things at that point.

**[01:18:20]** And then I started looking at. So the second half of the paper is looking at the sort of. The kind of shapes that show up in the. The data. If you sort of.

**[01:18:34]** Yeah, so this is an eyeball fixating a point on the ground. So is this. And if you project the sort of retinal view onto the ground, you get this kind of ellipse. And then you get this. It's like very elongated at the upper visual field and very condensed at the lower visual field, which is good because this is the part that we care about.

**[01:18:52]** So, like, if we had the same amount of neural real estate associated with each of these spaces, then we get a. Which we don't. But if we did, then we would get more of our neural machinery processing the stuff that's closer up to you, which is a useful thing. Then you get to change the position that you're pulling that information from by doing all these eye movements that we've been talking about all semester.

**[01:19:20]** Sagittal plane view is just a slice down the side. So this is what it looks like from the side. That's kind of what it looks like from the front.

**[01:19:28]** And. Yeah, and I'll show some videos in a second, obviously.

**[01:19:36]** So I wound up getting very inspired here by fluid flow mathematics. There's a three blue one Brown video on divergence and curl, which actually cite in the methods here, that was the best explanation I had of that. And so this is. If you look at the divergence and curl of these things, then you find this interesting result that you can determine from the flow field at each moment whether you are going to be passing, whether your current velocity vector will take you to the left or to the right of the point that you're fixating. And so even just while fixating on the ground, the motion patterns across the full field you can extract, like this star at the peak in the divergence.

**[01:20:26]** And then there's this kind of saddle point and the curl that's either clockwise or counterclockwise. And those two things actually independently, like each one by itself, will tell you whether you're going to. Whether you're passing till your current velocity will pass you to the left or the right, the point that you're fixating, which is cool because this is also there are parts of our nervous of our visual system that are sensitive to this type of thing. It's like MST, MSTD like we talked about. Primary visual cortex is V1, MST is like V4, V5, something.

**[01:20:59]** So like at a certain point, and arguably there's actually points, there's machinery like on your retina, like in that. Remember that middle area? It's like a bunch of weird stuff going on in there. Some of that is actually sensitive to visual motion and differential patterns of visual motion. So theoretically you could be inferring stuff like this on your retina or else in your visual cortex, something like that.

**[01:21:27]** Which I think this type of behavior is so primitive that you would want it to be very easy to get. Like flies and bees and dragonflies are doing this type of thing. So you don't want to have to have this scale of firepower to be able to solve these types of problems. But yeah, And now I will show a variety. Oh, wait, Yeah, there we go.

**[01:22:19]** So.

**[01:22:24]** I think I can actually do this. I think there's a place list. Right. I would do that. That seems like something I would do.

**[01:22:42]** Yeah.

**[01:22:49]** Videos. And we'll put this as well.

**[01:23:02]** Yeah, so.

**[01:23:07]** Just do that.

**[01:23:20]** Yeah. So this is the same. Oh yeah. This is actually the demonstration. So this is the same rocks.

**[01:23:26]** This is my eyes. They look familiar. Same basic data, except now we have two eyeballs, which is nice. And this is the retinally aligned gaze. And I'm pretty sure in a second here.

**[01:23:37]** Yes, it's going to show that.

**[01:23:42]** So this is the first part of that analysis. So you just run this. This is classic computer vision, optic flow estimation. So you get a vector for each pixel that estimates the motion at that pixel. You can do that for the head centered view and for the eye centered view.

**[01:23:58]** And so you get this. So obviously the point that you're fixating has zero velocity. That's what fixation means. And we kind of cheated and sort of pinned that there because assuming that your visual system is better than our measurements. So you always have this kind of zero velocity at the point of fixation.

**[01:24:14]** And. And so because of that you have this kind of like rotationy patterns that show up there. Yeah. So this was another one of the clever things I've done in my life. You take that flow field, you invert it, so instead of pointing away, it points towards and you put a grid of massless particles on it and they sort of follow that trajectory and they all kind of wind up here.

**[01:24:35]** You keep track of their paths and you get this sort of nice. These are apparently the. You get these nice shapes that show up and you can see how they kind of like they bend around the 3D structure of the scene because of parallax, things that are closer to you move faster than things that move slow. It's like looking at the train window type of thing. And you can also see these kind of spiral patterns that show up.

**[01:24:59]** Some of the Carl stuff looked at the structure, the 3D structure stuff, but you kind of see there's these shapes that kind of emerge and so then a lot. And they show up much better in the fixation stuff than you do in the head centered stuff, which is obvious to you, but some people have issues. But that in the head, it's much more aligned to the trajectory of your head. So this yellow line here shows your head's velocity vector, then your gaze, your oculomotor system is fixating so that you can process stuff better.

**[01:25:36]** And so that's fun. And.

**[01:25:44]** Let's see, Running out of time, but that's okay. Kind of on point. And so then that was like the empirical data and then this was.

**[01:26:09]** Now I'm basically simulating. This is a simulation of a eyeball that's moving while fixating this point here. And you kind of can see these like shapes. So this one, it's moving in like a corkscrew path. But you can kind of like imagine why.

**[01:26:29]** Yeah, left as an exercise to the reader of like why some of those shapes show up.

**[01:26:36]** And then I would say this is probably the high water mark of that particular empirical part of my life, which maybe I'll get back to someday. But this is that same rocks data projected onto a flat ground. And then these are the actual eye movements that were being made with all the sort of simulated flow here. So this is the curl. You can see it sort of move to the left or right as the vector moves to left or right there.

**[01:27:09]** And then the sort of this like peak in the divergence map sort of also corresponds to that stuff. And there are some people who are out there trying to like, make some more sense out of this and try to like understand how, how and whether and if these types of signals are actually being used and how they might be. It's the kind of thing, like, if you look at the literature, like I said, there are. There's a lot of evidence that there's places in the nervous system that could be sensitive to this stuff. It's like sort of, it is consistent with.

**[01:27:41]** No, With like mechanisms that could detect information like this. Whether or not it actually is there, whether or not we actually use it, whether or not that's actually a part of the way we move around the world, is sort of an empirical question.

---

### Chunk 10 [01:27:46 - 01:32:21]

**[01:27:46]** With like mechanisms that could detect information like this. Whether or not it actually is there, whether or not we actually use it, whether or not that's actually a part of the way we move around the world is sort of an empirical question. But then, so the idea is that we can use this type like so going out into the world and measuring these things and saying, oh, hey look, there's these interesting patterns and shapes that show up and it would make sense if blah, blah, blah, and this and that. This is often the kind of stuff that drives research in more like animal stuff. And the actual electrodes in the brain style of experimentation where you are much, much more constrained.

**[01:28:27]** You can't have things running around. But this kind of gives a target to look for. Like this was how you might generate the hypotheses that you would take into a more controlled lab based setting.

**[01:28:40]** And trying to see if like this is actually like if these sensitivities are a, a part of a visual system and be a part of the strategies that we use to, to move around the world.

**[01:28:56]** It's fun. Mesmerizing. What's going on in there? Ooh. The answer is a lot.

**[01:29:05]** And in the three minutes I have left, I will also, I'll give a little shout out to my dude Carl, who.

**[01:29:21]** I found him as an undergrad and he sort of was in the lab for my postdoc and then stuck around and got a PhD with Mary and published. Basically you never learned the lesson don't put hard green on white. But you know, whatever. He continued a lot of these same kinds of explorations, but with a. He's much better at math than me.

**[01:29:50]** Actually. This part's just looking at some of the statistics. This is really helpful for neuroscience. As some have said. This is the diet that your visual system was raised on.

**[01:29:59]** They said the statistics of visual motion that your nervous system experiences during your everyday life. And then this is the paper I was actually looking for came out 2024 where he actually used photogrammetry to do 3D reconstructions of the terrain. Everything up until now was using that kind of flat ground plane. But now he's actually starting to get the 3D aspects of it and was looking at the different trajectories. And he has this really cool analysis showing how people would.

**[01:30:35]** He was look. So like, whether, whether you, how do you choose your footholds and so do you choose to step onto the rock versus going around the rock? And so he did this complex analysis there and found that like it's like it depends on how tall you are. And so there's unsurprisingly, but getting the numbers that whether or not I choose to step onto a rock and over it is. I'm more likely to do that than someone who is shorter than me because it's a higher cost for them.

**[01:31:04]** And so you could sort of look at these things and seeing how people navigated and sort of like, he was able to find, like, people tend to like slopes that are within a given regime. And being able to pull that out of the data is like, super cool.

**[01:31:20]** Yeah. Couldn't tell you much beyond that because even though I am on this paper and I. I read it to some degree of approximately. Yeah. This is his simulated potential foothold paths and sort of, you know, you choose the ones that sort of are on this side versus the sort of arbitrarily specified ones.

**[01:31:42]** Cyan on white. You'll. He'll learn. This is the 2015 paper, had this problem. He'll get there and.

**[01:31:56]** Yeah, I think that's the end of the class. So that's what I've done. That's my research. And thanks for watching and it's kind of fun, I think. I hope that you were able to.

**[01:32:07]** Thank you. I hope you're able to follow that more now than you would have been able to in September or whenever we started here. So thanks for coming along. Next Tuesday, we'll talk about trauma and then we'll talk about.

---
