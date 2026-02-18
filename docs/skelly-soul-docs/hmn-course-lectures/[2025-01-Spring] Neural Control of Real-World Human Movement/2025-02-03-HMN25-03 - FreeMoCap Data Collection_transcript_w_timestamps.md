# Transcript: 2025-02-03-HMN25-03 - FreeMoCap Data Collection

## Source Information

- **Source Type:** Local File
- **File Path:** `C:\Users\jonma\syncthing-folders\jon-alienware-pc-synology-nas-sync\videos\video_eater_downloads\playlists\[2025-01-Spring] Neural Control of Real-World Human Movement\2025-02-03-HMN25-03 - FreeMoCap Data Collection\2025-02-03-HMN25-03 - FreeMoCap Data Collection.mp4`

---

**Total Duration:** 01:29:51

---

## Full Transcript

### Chunk 1 [00:00:02 - 00:10:00]

**[00:00:02]** Okay. Hello everybody and welcome to Wednesday.

**[00:00:09]** So today is a very special day because today we're going to do some data collection, which is always a very exciting time in any scientist's life when you, you get some numbers, you take some recordings, and then oftentimes you spend the next while analyzing that data. So how it goes matters a lot. This is not a particularly high stakes situation, but yeah, it'll be fun. So we're going to do. I'm going to try to finish up what I was talking about last time and then I'm going to set up the cameras and do a quick recording, do a couple of quick recordings with the free mocap software which I made with my lab over the past six years or so.

**[00:01:06]** And then if all goes well, it should pop something out that's worth looking at today. And then I will do some additional fiddling with it. And I either have something to say about that on Monday or wait and give myself an extra bit of time and talk about that on Wednesday.

**[00:01:30]** So if you're not, yeah, your job is mostly to just sit and listen and try not to fall asleep. But if you fall asleep, I understand you're got a lot going on.

**[00:01:45]** So. Behold a human person. It is roughly speaking, this shape. See, this is a complicated shape, but it's not nearly as complicated as this weird object. But if we needed to, because we are finite beings with finite technology and finite time, if we wanted to study the, this complicated object, this the desiderata of our research being to understand how humans move through the world, you have to make simplifications, you have to make assumptions, you have to do things like that.

**[00:02:26]** And so last time I talked about can I do this?

**[00:02:38]** That works. So last time I talked about my personal favorite oversimplification of a complex physical object, which is to take that object and reduce it down to a single point mass that we call the center of mass. Center of mass. We often hear it called like center of gravity, which in that term, in that meaning, gravity is sort of meant in like the old school sense of like density, because density and mass are kind of the same thing in some conceptions. But the beauty of the center of mass is that it's a rather simple thing.

**[00:03:15]** The center of mass is the concept of center of mass is the thing that's the intuition that says that if I want to balance this stick on my finger, I put my finger under two fingers, under the midpoint of the total distribution of mass on the thing, and it balances there because there's the Same amount of pull on this side as there is on that side. And if it's a symmetric object, the center of mass corresponds to the geometric center of the object itself. If it is non, that's the wrong direction. Oh, I did that.

**[00:03:58]** What am I trying to do? I'm trying to do this if the weight is non symmetrically. So linguistically we tend to interchange mass and weight, language wise. In imperial units, we actually don't have a dedicated measure for mass, we just use pounds, which is actually a measure of weight. Weight is a measure of force.

**[00:04:20]** It's like how much force am I putting into the ground? So if you assume that gravity isn't changing, mass and weight are interchangeable. But just because I spent an hour and a half last week or on Monday talking about SI units, I should specify that when I say weight, I typically mean mass and vice versa. But until we go to the moon, that won't be a problem. Anyways, center of mass when the weight is non, the mass is non uniformly distributed, the, the center of mass is not going to be the same as the geometric center of the object.

**[00:04:56]** But the same basic idea maintains like there is as much mass on this side of the base of support, which is this, as there is on that side. And so the center of mass of the thing is right around here. And so if I wanted to hold this object off of the ground stably, I need the base of support to be under the center of mass of the object itself. If I put the base of support outside of the center of mass, it'll fall in that direction, which is not particularly mind blowing, but it is an apt description of what balance is at a very sort of low level of physics.

**[00:05:37]** Let me make sure we have enough time to sort of say all the things I want to say should be fine.

**[00:05:46]** So last time we also talked about when an object is flying through the air, it has this nice ballistic trajectory, which is caused by the transduction and exchange between kinetic and potential energy in a gravity well. And there's MGH is potential energy, 1/2 MV squared is kinetic energy. And even though this object is complicated in its form, the trajectory that it takes in the air is exactly the same as it would be if I was throwing an equivalent mass in a. Like if you condense this down to like a single lead sphere and I toss it in the air, it would follow the same trajectory. If I spin it, it spins around its center of mass because it's in a.

**[00:06:38]** When it doesn't have anything to push off against, you don't have any. There's nothing to react, no reaction force to push you in any direction. Things balance out and you get sort of simple, predictable physical behavior.

**[00:06:57]** We also talked very briefly about one of my favorite things, which is pendulae. Pendulums. Pendulums, Pendulae, which. This is an example of a pendulum. You've seen them in various places of your life.

**[00:07:12]** And it's basically a mass hanging below a standard pendulum is a mass hanging below a pivot point. And if without, you know, if you pull it back and let it go, it'll swing back and forth for quite some time until friction bleeds off enough energy that it will eventually slow down. And the reason for that sort of conservative motion is the same kind of transduction between potential and kinetic energy. So if you imagine that's a pivot point, that's the bob, the mass of the pendulum. Let's assume that this string doesn't weigh anything.

**[00:07:53]** Or at the very least it weighs much, much, much less than this. If we wanted to, we could also just imagine that if it's shaped, if this is the shape, the center of mass of the thing is still going to be definable mathematically in some place there.

**[00:08:13]** But here it is up here. And then we let it go. It's up here at rest. So it's kinetic energy equals zero. And its potential energy is at.

**[00:08:27]** Let's just say it's max. And then, so we let it go and it drops. And then it gets to this point here where it's at the lowest point of its swing. And at that point its potential energy is at its minimum because it's the lowest it's going to get. You could even say the potential energy is zero if you want to talk about it that way.

**[00:08:50]** But its kinetic energy is going to be its maximum. It's going to be moving the fastest. It's going to move here after you drop it. And then it's going to be moving so fast that it will have momentum because of that whole inertia thing, that first law that will carry it up the other side of the swing until it gets here. And then again it will briefly pause.

**[00:09:12]** Kinetic at velocity zero. Kinetic energy zero. Kinetic energy zero. Potential energy max.

**[00:09:23]** And then it will. Then the same process repeats in reverse. And as long as there's no other way place that the energy can go, it will continue like that forever. In reality, there's always going to be things like friction on points like this. There's always going to be things like air resistance that will be bleeding off some of the energy.

**[00:09:41]** So it will eventually, if we plot it over time. And we plot. Let's say this is the angle here, theta we want. And we drop it from here. It'll go like this and then it will slowly.

**[00:09:56]** We call that damping out. If it was.

---

### Chunk 2 [00:09:45 - 00:19:45]

**[00:09:45]** And we plot, let's say this is the angle here, theta you want. And we drop it from here, it'll go like this and then it will slowly, we call that damping out. If it was a ideal system, this would just be like a nice sine wave forever. But because there's going to be some bleed due to friction, this will be the nice trajectory there. So that is a.

**[00:10:12]** This is a standard hanging pendulum. And look at it go. Pendulae are very, very, very, very important in the history of science. They are sort of part of almost every important measurement in history, like gravitational constants, electro coulomb force. Apparently there was a time when they used to use the period of a pendulum to do prospecting for iron ore. Because you can measure the period of a pendulum very, very accurately and it's going to be defined by the density.

**[00:10:50]** It's like the gravitational constant. The gravitational force is a part of that equation of motion. So apparently they would just like move these very, very, very precise pendula over parts of the ground where they thought there might be iron ore. And if they measured a change in the period, that's a reason to believe that there's a higher density in the column between you and the center of the earth. I read about this in a book. I've had a hard time validating, verifying that information, but nonetheless it's very.

**[00:11:22]** It's a pendulae. Pendulums, very good stuff.

**[00:11:29]** Pendulums are also a nice example of that periodic motion I mentioned briefly last time. How when we think about time, there's stopwatch time which always counts up, but then there's kind of like wall clock time that resets every so often. And with something like an oscillator like this, you're thinking in that phasic sort of like time goes from zero to some maximum and then it resets and then that's. We call that a full cycle. Many, many parts of biology have this kind of like phasic behavior.

**[00:12:02]** A lot of my research historically has been on locomotion and that has a lot of pendulums in it. The main one that you would think about with the pendulum is like the swinging leg. But there's another much more dramatic and central pendulum which is the inverted pendulum of your sort of standing body. So this is a pendulum hanging from a central pivot point.

**[00:12:29]** But you could lift this thing up until it's all the way on top and then have it be up here as an inverted pendulum and at this place. So at the bottom here, this is a Stable point. Because if we just let it run, this is where it will wind up. This is in the language of dynamical systems, this is called an unstable point. Because technically speaking, if you placed this here precisely at the angle of deflection equals zero, this would stay.

**[00:13:06]** It would sort of stand up in the same way that this marker stands up on the desk.

**[00:13:15]** But the reality, but because this is an unstable point, any perturbation to the left or the right is going to cause it. Like if you, if this is not perfectly straight, if it's a little bit off to the right, then gravity is going to pull it down and then it's going to keep pulling it down until it falls down there. So you can balance a. So you can hang a pendulum and it's passively stable, gravity does all the work for you. You don't have to worry about it.

**[00:13:50]** If the pendulum has, if the base of support has extent, if it's non zero base of support, you can balance it happily on a flat surface and it will also stay there passively forever. But if it's not, then you can balance it. Then the only way that you can balance it upright is if you are actively controlling it. So this is the classic broom trick where you can just balance something on your hand and you can do it because I'm moving around the base of support to make sure that the whole thing never falls over, but I can't. So this is all by way of preamble to the recordings we're about to do.

**[00:14:43]** So if you think about in some idealized pendulum, and this is the center of mass on top of it, remember we're spending a lot of time thinking about force equals mass times acceleration, where this is the mass, which we're assuming the mass doesn't change. So we can sort of assume that force equals acceleration, some approximation. And so if you're, you know, in the idealized form, you manage the standing up here, if the projection of the center of mass onto the floor, if the distance from that projection from this infinitesimal base of support is zero, then it'll be happily standing upright forever. If instead we're off by a little bit and the projection of the center of mass has a distance here from the base of support, then in a very intuitive sense that gravity pulls things down gravitatively, pulling like that, and then this distance there will be sort of pushing the object away. So that's why it's unstable, because any deflection from zero and it will start to fall.

**[00:16:06]** And the farther that it falls the more it gets pushed away. So it will be accelerating away from that sort of stable point.

**[00:16:17]** And so if you're supporting it like the broom, then you can fix that by moving around the base of support on the ground. But if you yourself are the pendulum in question, and you are, imagine my center of mass is here, and I'm standing on my one little leg. I can, the only way that I can really have any control over where my body is is by the forces that I'm putting into the ground through my foot.

**[00:16:55]** So if we now imagine that's me, that's my center of mass, this joint here is the only place that I can push into the ground. And so if I'm leaning a little bit too far forward, I can push with my toe and push myself back. If I'm leaning a little too far back, I can push with my heel. Not really. I can lean forward.

**[00:17:21]** I can do something to try to change the forces to push myself in that direction. But in general, if I don't have monkey feet or grippers on the ground, I can only really push. So that means that my center of mass has to stay within this base of support range in order for me to be able to maintain standing posture without doing something dramatic like taking a step, that's usually what we can do. So if we're assuming that the task is to stand upright without taking a step, the goal condition there is the center of mass stays within the base of support so that I can sort of move around the forces I'm pushing into the ground and sort of push my body back and forth to where it needs to go. So that is balance and standing posture.

**[00:18:16]** In a nutshell, all of this that we're doing here, it falls under the category of biomechanics. Anytime you hear anyone talking about like forces and mechanics and Newton's laws and centers of mass and joints and torques and stuff like that, you're. You're hearing someone talk about biomechanics. But if you think about sort of like, zoom out a little bit from those low level physics and start thinking instead about the, you know, start thinking about this physical object now as a biological system with a biological system with muscles and neurons and sensory systems and stuff like that, you can start trying to ask the questions from the sort of neuroscience perspective of how does all of that sort of play out in a human person with things like joints and muscles and stuff like that. So how do I, if I'm.

**[00:19:11]** If I. Because we're very, very good at standing up, this body configuration with the two feet and the arms that are up there off the ground. This is wild in the animal kingdom. This is a wild way to be. Musculoskeletally, Pretty much all other mammals are quadrupeds.

**[00:19:31]** The only other bipeds out there are birds, and most of them fly the ground. Birds are arguably better bipeds than we are because they have, like, 450 million years of evolution on us. So good for.

---

### Chunk 3 [00:19:30 - 00:29:30]

**[00:19:30]** Mammals are quadrupeds. The only other bipeds out there are birds and most of them fly the ground. Birds are arguably better bipeds than we are because they have like 450 million years of evolution on us. So good for them. But generally speaking, like, for animals as big as we are, to support your entire body weight off the ground with just two feet is wacky.

**[00:19:57]** It's like unprecedented. There's no other animals, at least in the mammalian kingdom, that have bipedal locomotion. Kangaroos are a good example, but they can't really walk on two legs. When they're moving, they can bounce on two legs, but when they're in place, they sort of crawl around on four feet and they use their tails. Animals like bears and apes and stuff like that can walk on two feet, but they tend to be.

**[00:20:30]** They're knuckle walkers. We are, I believe. I'm always like waiting to be find a counterexample. But at this point I should probably just accept that there aren't any. We're like the only obligate bipeds in the mammalian kingdom, where obligate biped means we really don't have another option here.

**[00:20:46]** It's bipeal or nothing. And we are also, as far as I can figure out, the only animal that has two of the main limbs of the sort of tetrapod. This is tetrapod shape, head, two limbs on top, two limbs on bottom and a spine. We're the only ones that have really well adapted upper limbs that have nothing to do with locomotion. Even ground birds, they have wings, but they tend to kind of suck as appendages go.

**[00:21:19]** But we gave up a lot to have these grabbing objects and the cost was that we now have to do this sort of gymnastics routine every time we want to get from point A to point B. So thinking about this, like the neural basis of bipedalism and standing posture is one of those things that feels like kind of like a baser level of behavior than we tend to think about when we're thinking about the majesty of human, you know, neuroscience and biology. But it's really fundamental and it's really core to like what we are as organisms and creatures. So I think it's worth consideration here. And yeah, yeah.

**[00:22:05]** And so with that, I think we can start transitioning towards like the data collection part of this. So if we assume now that we all have the shared desire to understand how we weird bipedal humans manage to stand as effectively as we do stand upright and Walk around effectively as we do. We can start now trying to think of this as empirical scientists and start asking the question if the desired outcome, the desiderata of our research endeavors, is to understand the neural basis of, let's say, just for simplicity's sake, standing posture, what are the measurements that we can take and what are the analyses that we can do that would give us insight into the underpinnings of that behavior?

**[00:22:58]** And there's a lot of options, but we're going to do some simplified. It's not even all that simplified, but we're going to take a full body perspective. Like you could go in and say, oh, well, I want to figure out the sensitivity. Like, how do we detect our lean angle? Like, is it the vestibular organs in our inner ear?

**[00:23:17]** Is it the pressure under our foot? Is it the proprioceptive forces in our ankles? How can we measure the sensitivities of those things? How can we sort of understand those circuits? What are some other animals we can look at?

**[00:23:30]** And you can do the kind of like the classic reductive, like biological stuff and start looking at the properties of the muscles. And we could cut up some cadavers and see what's the density of somatosensory organs in the bottom of the feet. We could do that kind of like zooming in on one part of the task. But necessarily doing that will leave out the actual behavior that we care about and what we would call the ecologically valid behavior behavior of the organism in question. Performing the task that we care about in the real world or something close to the real world that, you know is the.

**[00:24:10]** If we assume we care about standing posture, then we care about standing posture in the real world. We don't care about standing posture in the lab in some weird artificial environment that we concocted so that we could have something that we could study. We might have to use that to be able to make any progress. But secretly we will feel a little bit sad because we will know that we have created an artificial representation of the thing in question and we are not actually studying the thing itself.

**[00:24:42]** So with that said, yeah, I won't do the whole biz about this. But also, jumping exists. We're going to record some jumping too. Jumping is kind of like this, except instead of like leaning, you're putting force into the ground. If you put more force into the ground than you weigh, you'll leave the ground until you have bled off that additional energy, and then you'll come back down and do something roughly equivalent to that.

**[00:25:19]** Yeah.

**[00:25:26]** Yeah. Okay.

**[00:25:30]** How do you feel about that so far?

**[00:25:33]** Emotionally prepared for what is to come. Great.

**[00:25:41]** So in a little bit here, I have an hour to go, which should be enough time. Spoiler alert. I'm going to set up some cameras, and those cameras are going to allow us to Record full body 3D kinematic data of a human person standing in space. This human person is me. I would love to do a thing where we record you guys and do that, but time doesn't really work out.

**[00:26:10]** And so this weird conflagration of cheap cameras and free software will give us an approximation of my body at 30 frames per second down to some level of precision at the centimeter scale of precision for my joints. And the approximation will be roughly equivalent to this. It will tell me roughly where my head was, where each body segment was, where each joint was. And this will be kind of like the. This is the data model that will come out of it.

**[00:26:49]** And this is where I'm going to start thinking as we go. And I'm going to record myself doing a couple of behaviors. So the first thing I'm going to do is calibrate because I have to do that. And I'll tell you about. Talk about that as it goes.

**[00:27:08]** Then I'm gonna do a standing task. So I'm gonna stand on two feet. Then I'm gonna stand on one foot, and then I'm gonna stand on the other foot.

**[00:27:24]** And then we're gonna probably. I'll ask someone to pull out a timer. We'll do like 20, 20, 30 seconds of standing in each one. So this will be recording one, this will be recording two. Sorry.

**[00:27:34]** 01, and then two. I'm going to do the same thing. I'm doing this different than I've done in past years, but I'm going to do the same thing. Except now I'm going to do the same thing while holding on to a chair.

**[00:28:05]** So I'll like. So I'll start out doing just like, freestanding. And then next time I'll like, lean over and, like, have my hand on the desk and sort of do the same kinds of tasks.

**[00:28:17]** Then after that, I'm going to do. I'm going to take a couple big jumps, just standing, jump as high as I can jump. And then we'll do another one where I'll do like. I'll jump in place for like 30 seconds. And then at that point, that'll be enough recordings.

**[00:28:43]** So that. Yeah, so we're going to. So this will be. So we'll get 1, 2, 3, 4, 5 total recordings, which should process in the moment, depending on how fast, how long it takes to set up. I may or may not truncate the processing so that we can get through them all, but your task as you're watching the show is just kind of think about these behaviors and think about them relative to the kind of the biomechanic y center of mass types of conversations we've been having so far and just make some predictions about what these data will look like.

**[00:29:28]** And you could think about it as.

---

### Chunk 4 [00:29:15 - 00:39:14]

**[00:29:15]** Relative to the kind of the biomechanic y center of mass types of conversations you've been having so far and just make some predictions about what these data will look like. And you could think about it at the full joint level down to the level of knees and ankles and shoulders and stuff like that, but that can be a little overwhelming. So I would also recommend thinking about it just in terms of if you boiled this whole thing down to just a ground plane, a foot and a leg and then a center of mass, what would you expect to see? Like what's going to be the difference between standing on two legs versus standing on one leg? What's going to be the difference between standing on one leg free versus standing on one leg while leaning on a table?

**[00:30:03]** What's it going to look like when I take a big jump? What's it going to look like when I take a bunch of jumps and yeah, think about it, make some predictions.

**[00:30:25]** Because there's your ability to make predictions about what this is going to go is how you know that you're operating within a theoretical framework. They're thinking about. There is an assumption that I am making that boiling down this hyper complex object into a singular 3D point mass and saying we'll be able to say things about that. We'll be able to predict the motion of that point mass and say things about that point mass that will tell us things about the global organism. That's a theoretical framework.

**[00:30:57]** That's a pretty strong bold claim. But we're going to operate within that space and yeah, we're going to try to do this without crashing my computer too, which is always fun.

**[00:31:18]** So great.

**[00:31:31]** Has anybody here worked anywhere near motion capture before any physical therapy or anything like that? Yeah, so it's one of these things where motion capture mostly where you will have seen it will be behind the scenes of movies and video games and stuff like that. You know a lot of like Lord of the Rings stuff of golem and smog running around.

**[00:32:05]** But it has been around and used to study human movement for quite some time. Arguably like the invention of video was technically what am I doing here? That I got that I have this. This. Yes.

**[00:32:36]** And then this. So the original like video was created to study horses in motion based off a bar bet from Vanderbilt, the guy like the robber baron about whether or not horses ever was there was ever a point in their gallop where they had all four feet off the ground. So you've probably seen the picture of like this like a bunch of horses, old timey video Basically, to solve that bet, Vanderbilt commissioned a photographer to. To take a bunch of sequential videos of pictures of a horse in full gallop and was able to show that there is, in fact, a phase where they're all off the ground, where the feet are all off the ground.

**[00:33:25]** But since then, motion capture has been used in the study of human movement and clinical stuff for as long as we've been doing that.

**[00:33:39]** What am I doing? I'm doing this. Okay. But also, traditionally, it's not a very common thing to do because it's very, very expensive. The motion capture lab I have in Richards has like a quarter million dollars worth of motion capture equipment in it.

**[00:33:58]** And it's in a room that was specifically built for the purpose of doing motion capture. And it's, you know, it's a very good system. It's very, very precise, but it's also a huge pain to use. And it's just. It's expensive.

**[00:34:12]** So the, you know, there's. The number of people out there who are studying human movement is much, much larger than the number of people who can afford motion capture. So that was kind of a part of the motivation that I had for making this strange system was basically realizing around 2017 when a software came out called OpenPose that used convolutional neural networks to basically draw a stick figure on a person in a video. And I saw that, and then sometime later realized that that capacity to basically draw a 2D skeleton estimate on a person in a scene was kind of enough to build a motion capture system out of. And then that was sort of an idea that I had.

**[00:35:23]** And sort of the thought was, yeah, that's a cool idea, but, like, I don't know how to write code, and that seems like way too much work, so I guess I'll never do it. And then three years later, Covid hit and I lost access to my lab for an indefinite period of time. And I also lost faith in the academic system pretty much entirely and started like, rethinking the idea that using. I'm going to have to unplug this camera now.

**[00:36:09]** Sure.

**[00:36:12]** I'll turn you off later.

**[00:36:19]** Yeah, I kind of. I started to really doubt the core principle of science, which is that the best thing that we can do as scientists is to publish papers in esoteric journals that exploit us for profit. And started thinking about, like, you know, is this behavior actually making the world a better place? And started. Had the uncomfortable realization that I don't really think it does.

**[00:36:46]** I think it's a good thing to do. I think that scientists are generally trying to improve the world, but we're trapped in these systems of communication. It just doesn't serve. It made sense in the 1800s, it just doesn't make sense now. So I personally transitioned away from publishing papers and journals and towards using the skills and understandings that I have from my sort of history of scientific research to build tools that people can actually use in their real lives.

**[00:37:26]** So this is one of them.

**[00:37:32]** So real quick, if you want to look it up, Free mocap, just Google Free mocap. You'll find it. Free mocap. It's pretty. Oh, I'm not on the Internet.

**[00:37:41]** Am I on the Internet? I am on the Internet, yeah.

**[00:37:46]** Hey, look, people make videos about me.

**[00:37:51]** But yeah, you can look it up. It was a whole. It's been a whole process.

**[00:37:58]** And let's get to it. So.

**[00:38:03]** So FreeMap stands for free Motion Capture. It is a markerless motion capture system. The majority of, like traditional motion capture, you wind up. You wear the spandex with the suits and the reflective dots. This is markerless.

**[00:38:16]** So the idea is to use sort of like the modern, sort of. What's the word?

**[00:38:25]** The arising technology of just like computer vision and sort of like the wacky stuff we can do with that to play the role that the markers used to play in traditional motion capture systems. Let's talk a little more what that means. I'm actually doing it.

**[00:38:48]** The hardest part of making this process, the most sophisticated part of the code by. By a mile, is the part that connects to the cameras. Maybe it shouldn't have been as surprising. Should I do this?

**[00:39:04]** Yeah, I think that makes sense. So everything is Skelly. Skelly's the logo. It's like a skeleton. See, it's kind of how it works.

**[00:39:13]** My personal journey.

---

### Chunk 5 [00:39:04 - 00:48:59]

**[00:39:04]** Yeah, I think that makes sense. So everything is Skelly. Skelly's the logo. It's like a skeleton. See, it's like kind of how it works.

**[00:39:13]** My personal journey as a researcher, I was a philosopher. I got a bachelor's degree in philosophy. Then I started doing more perceptual motor neuroscience and kind of like was studying vision from like a vision science perspective and was feeling not. It felt insufficient, it felt like incomplete. And it wasn't until I started digging into.

**[00:39:37]** I started like found my way into some of the more biomechanics approach to movement that because I was studying visually guided locomotion in an environment that really didn't have any consideration of like the physics of being an object moving through space. And when I started reading the biomechanics papers was when a lot of things started to click for me. And those papers had a bunch of skeletons in it. Calm it down. And that's why there's skeletons everywhere.

**[00:40:05]** Because it's sort of like this. It's like kind of a joke that I study neuroscience from the perspective of a skeleton because that's like physics wise, it's mostly skeleton. The neural components are really not. Not really. Newton doesn't really notice the neuroscience parts of it.

**[00:40:24]** He mostly notices the skeleton. Anyway.

**[00:40:31]** So this is the latest form of the software. Actually it's not the main. So the current stage of development of freemocap is that the core software is a little bit behind the development side of it. So we're using this camera stuff. It's very slow for some reason.

**[00:41:05]** Why are we so slow?

**[00:41:14]** Okay, there we go.

**[00:41:18]** Oh, right, I have to turn you off over here. Okay. Apologies to. Oh, I guess we can do that. So turn you off.

**[00:41:31]** Okay, there you go. Then we shut you down again.

**[00:41:44]** So this is one of those places where like all the stuff streaming by is where all the work went. And then the outside is quite simple in comparison.

**[00:41:56]** Reasonably confident that this will work. But anytime.

**[00:42:21]** Okay. Hopefully that should work better. We can hope.

**[00:42:33]** Yeah. So as a scientific tool, motion capture is in the very crowded space of being a camera based research tool. So the environmental energy that we are encoding and recording in this case will be light. So light bounces off of me. Bounces.

**[00:42:59]** Goes through the lens of the camera, gets absorbed by the camera sensor, which is just a little rectangular silicone wafer. Silicon wafer. Whichever one of those is accurate. And yeah, and then we will be recording the. We will be pulling samples from a light cone from three different locations in space 30 times per second.

**[00:43:27]** And there's been a lot like, A lot. A lot like years of my life has been spent making sure that the videos that get recorded from these cameras are synchronous. So as these cameras are pulling, as each camera sort of pulling frames from its field of view, there's a lot of code under the hood that's making sure that each camera is pulling at close to the same time as the others as possible. So we're pulling synchronized videos. So we talked about the mentioned last time, the sort of the concept of like spatio temporal calibration in recording and sort of that just like the spatial components and the temporal components.

**[00:44:09]** Great. The temporal components here are handled by the software. So we are going to assume that all the samples from each camera are synchronized in time to some approximation.

**[00:44:21]** So the second part of that is the spatial. So let's see. So those are all rotated. Are they rotated the same way? They are.

**[00:44:34]** Which is counterclockwise.

**[00:44:44]** That should work. Did I get that right? I got it backwards. It's always backwards.

**[00:44:53]** Yeah. Nobody's here.

**[00:45:00]** Okay, good.

**[00:45:04]** Yeah, great. So it's not using the space particularly well, but don't worry about that. So.

**[00:45:23]** So now I'm going to point the cameras. So I'm going to stand roughly here and so I'm going to try to point the cameras that they can all get a good view of that sp.

**[00:45:40]** All right. Oh, we have that one. That's nice.

**[00:45:46]** We also have that. That's nice.

**[00:45:57]** Okay. Now unfortunately, I am.

**[00:46:04]** I am going to. I'll do that later. So the images are a little dark. I think that is the nature of the beast. Another part of the game here with freemocap was building the cheapest possible system I could possibly get.

**[00:46:20]** So intentionally targeting like garbage cameras. These are really garbage cameras. Like, they cost $10 a pop on the assumption that as a researcher, buying four GoPros is nothing. But if I'm trying to make something that's accessible to the world, GoPros are expensive. So trying to build it on the cheapest possible hardware was a part of the game.

**[00:46:46]** Okay. So we're going to have to do some projective geometry at some point. So I mentioned that we have the temporal synchronization and happening through the software. But we are also going to need to know the position of each of these cameras in space. We're going to specifically need to know the 6 degree of freedom position, so XYZ location, then XYZ rotation, so 6 total numbers, 6 degrees of freedom.

**[00:47:16]** And the way we're going to do that is by way of a calibration routine that involves a calibration object. This is called a charuco board. These little markers here are called ARUCO markers. And this is a calibration object which many every scientific tool will have some calibration component to it. And the typical pattern for calibration is you use the system to measure something that you know the answer to.

**[00:47:49]** I'm going to use this to measure the position of these corners in the board, because I know that these corners are all 58 millimeters apart. Like, I know that these blast squares are 58 millimeters wide. So if I use this system and I record this shape, I know what the right answer is. So if I record the position of the board and I check the numbers and it says, yeah, these are 58 millimeters apart, then I now have some confidence that the system is working as intended. And now I can use it to measure the unknown thing, which is the body and space that I'm not going to have any other additional measurement and insight about.

**[00:48:28]** So every form of scientific research is going to involve calibration at some point. In some cases, that calibration is done at the factory where they make the tool, but in this kind of more hacky DIY world, we make do with our own stuff. Ok, how are we doing on time?

**[00:48:50]** All right, so recording. So basically what this looks like is I take the board and I show it to the cameras.

---

### Chunk 6 [00:48:45 - 00:58:45]

**[00:48:45]** We make do with our own stuff. Okay, how are we doing on time? All right, so recording. So basically what this looks like is I take the board and I show it to the cameras and I make sure that each camera has shared views. So in this case they can all see it at the same time.

**[00:49:06]** I'm going to need to turn that off. Actually you can look here, but I have to turn this off because there's too much light. You got to be careful with the light so you can look there if you need to.

**[00:49:25]** So basically the cameras can see the board. They have shared views of the board. So you can do the kind of. The actually not so simple math of if I am camera A and I can see the board from this angle and at the same time camera B can see the board and I see it from this angle, then camera A must be in this position relative to camera B and vice versa.

**[00:50:02]** Make sure that works.

**[00:50:13]** Usually when I do this part of the class, I bring my grad student in to help me out. And this time he was busy. So I was like, I can do it all on my own and I can do it all on my own. But it is definitely one of the cases. Like, I sure wish Aaron was here.

**[00:50:25]** It'd be nice to have an additional nervous system doing this stuff.

**[00:50:33]** So now I'm just manually moving stuff from one folder to another just because of the stage of software. It's in and primo cap we're doing.

**[00:51:01]** You're gonna run. You gonna crash anyone?

**[00:51:13]** UV sync.

**[00:51:32]** Okay. We may also another traditional. So I tested a lot of this, but I didn't. I'm realizing I didn't test like every part of it.

**[00:51:47]** So we might find ourselves having a little bit more running on trust that I would have preferred.

**[00:52:18]** Okay, well as that runs, let's see. What are you doing? Why?

**[00:52:35]** Okay. Calling the audible. So remember how I will have to process these offline because it's not set up and I don't have the brain space to do the online debugging. So this will be a lot more prediction than usual. Just usually I can make this happen in the same time.

**[00:52:56]** But now.

**[00:53:02]** So we've done calibration, now we're going to do simple standing. So two foot standing. One foot and one foot on the left, one foot on the right. We call this a control condition because this is the one where we're not. There's nothing will be manipulated in this case.

**[00:53:21]** And then we're going to do this sort of manipulation condition which is going to be very similar to this. But with this sort of. Sort of extra factor of I will be supporting myself on a chair or a table or something like that and your. I guess I can use this instead.

**[00:53:40]** And then we'll do the jumping stuff. So.

**[00:53:45]** Yeah, and we're not going to be getting real time output from this class, unfortunately. But that just means that your mental model of prediction must work across times. Okay. Now I unfortunately have to take my shoes off, which is fine, but I just always feel weird doing it.

**[00:54:07]** The main reason, if I had been smart, I would have at least worn lightly colored socks.

**[00:54:14]** But you can see how dark the ground is and you just can't see my feet relative to the ground. So I will Tom Sawyer up my feet.

**[00:54:31]** Now you can't.

**[00:54:37]** This is one of the.

**[00:54:41]** In a real recording, I would be like. I'd have lights and stuff like that. It's also one of these cases where like it tends to work best like outside in the sun because the sun is very, very bright. Yeah, there you go. Now you can see my feet.

**[00:54:55]** Still a bit dark. Still very dark.

**[00:55:00]** That one's good. Okay, so one and two are a little dark.

**[00:55:08]** Manual.

**[00:55:18]** Oh, it looks better on my screen.

**[00:55:26]** Okay.

**[00:55:29]** Okay. So can I have someone. Can I request a stopwatch person?

**[00:55:38]** Thank you.

**[00:55:41]** So I'm going to ask for like basically 30 second intervals. So I'll let you know when it's ready to go.

**[00:55:51]** I do have to turn this off again and I'll leave that down and. All right, where's the.

**[00:56:02]** And I want to be standing like here. Great. All right, I'll let you know it's not right now. So here we go. So I'm going to stand here and I guess.

**[00:56:14]** Yeah, start it now. So this is me standing. I'm kind of already bored of this. So I'm going to lean. I'm going to be sort of intentionally in all these cases leaning as far as I can lean, sort of within, ideally without moving my feet.

**[00:56:33]** So I'm leaning all the way to the right and all the way forward. Let me know when we hit 30 there. Cool. No, great. OK.

**[00:56:48]** So now I'm on one foot and my base of support has now gotten appreciably smaller. And I'm wiggling around both for fun and because I'm off balance. So again, sort of let's just look at what's happening bodily. I'm doing a lot of movement, but we have some strong predictions we can make about the position of my center of mass relative to my base of support. And you make those predictions even stronger.

**[00:57:16]** Thank you.

**[00:57:20]** And you, when the base of support gets smaller, your ability to predict the location of the center of mass gets better. Like you have more predictive capacity because it is a more constrained task. There are fewer ways that I can successfully complete the task of standing upright when I only have one foot on the ground than I do when I have two feet on the ground.

**[00:57:49]** And done. Okay, great.

**[00:57:57]** So with those predictions in mind, how am I going to do this? I think I will.

**[00:58:16]** Yeah, that works great. This is my now my standing stick.

**[00:58:24]** So same thing. Sorry, I don't know your name. Stopwatch friend. Stopwatch friend. What's your name?

**[00:58:33]** Isabel. Thank you. Same thing. Now for the, let's say, let's call this a support condition. We're now going to be using like a stick to support myself outside of my.

---

### Chunk 7 [00:58:30 - 01:08:30]

**[00:58:30]** Stopwatch friend. What's your name? Isabel. Thank you. Same thing.

**[00:58:35]** Now for the, let's say, let's call this a support condition. We're now going to be using like a stick to support myself outside of my biologically prescribed base of support. So we'll go over here and then we'll stand for a little bit. So just go ahead and start the timer or whatever this is, just kind of calibration purposes. And then now I'm going to do the same kind of task of leaning as far as I can relative to my base of support, except now I have this stick to sort of assist me.

**[00:59:16]** So with the knowledge and theoretical models of human body that you are armed with, how do you think this is going to change that data? So now I'm going to go onto my right foot similarly playing all over the place. And let's assume for like when we get this data back, the stick is not going to be in the data. We will know that it was there and we'll know that this hand is mounted to the ground.

**[00:59:48]** But if you think about what the data will look like, you can have some predictions there. And now we switch feet. So again, just think about it. What do you think would be different here?

**[01:00:11]** It's been a long day.

**[01:00:14]** Standing in place is not the hardest thing in the world, but I'm making it difficult and.

**[01:00:27]** Okay, cool.

**[01:00:33]** Okay, thank you, Isabelle.

**[01:00:39]** This next part, I hope I don't.

**[01:00:44]** I hope I don't die on camera. But if I do, just analyze the data.

**[01:00:55]** Okay, so for this one, I am going to record. I'll say three, because that's what I wrote. But this is going to be standing, high jump. So I'm going to try to jump as high as I can from a standing place. And again, think about what that will look like.

**[01:01:15]** Think about what it will look like at this level. Think about what's happening at the physics level. Where is the force coming from? Where is it coming from at the start? Where is it going at the end?

**[01:01:28]** What's happening in the middle? What could be measured? What could be inferred? What additional data will you wish you had?

**[01:01:38]** And if I break anything, you know, you can have questions about that. Okay, I don't need a timer for this. So record. It goes down here. Hello.

**[01:01:55]** I don't want to whack myself off there.

**[01:02:02]** I used to used to not weigh as much.

**[01:02:08]** Okay. And.

**[01:02:20]** And that's all the knees I have today. I have to do a little bit more. Okay, so big jumps, discreet jumps, pauses in the Middle, a lot of arm swinging and knee torquing. This big hip joint doing its thing and some amount of air time, some kind of cheating in the air time. Ooh.

**[01:02:55]** Okay, let's see. This is going to stay on when I do this next part. If it does, probably this will be more.

**[01:03:14]** Probably be more reliable. Okay.

**[01:03:21]** Okay, so now instead of doing several discrete high jumps, I'm just going to bounce in place. And I'll bounce in place for as long as I want to, which I'm not going to ask anyone to time it. I'm just going to go until I want to stop, maybe do at least 10. And then I'll just go until I'm tired. And I'm already tired, so we'll see how that goes.

**[01:03:45]** Also pointing out I pulled my legs up, I pulled the pants up both to expose the nice pale skin below, which does. Well, this feels bright to us, but our eyes, the human eye is incredibly good at adjusting to changes in luminance. So relative to a sunny day, it's basically pitch black in here. We're just really, really good at adapting to that. But.

**[01:04:12]** So I exposed my legs both because they are lighter and they are contrasting with the carpet. But I'm also trying to give the cameras a view of my knee as opposed to having it be blocked. Again, like if you're trying to predict where my knee is, it's going to be way harder if it's being covered by cloth than. Than it is if it's directly exposed. So it's not just a fashion statement.

**[01:04:39]** It's empirically grounded. Ok, so yeah, so we'll say we'll call this discrete jumps and we'll call this repeated hops and bounces. So again, thinking about the behavior, thinking about the mechanics, thinking about the joint torques, thinking about the fatigue, where does the energy come from? What did I have for dinner last night? These are the questions of biology.

**[01:05:11]** Okay, I'm not going to drop. Time out. Okay, so record standing here, give that nice calibration a bit. And now we hop. Okay.

**[01:05:27]** One, two, three.

**[01:05:32]** Oh my God. There's just so many people looking at me. It's fine. Also, I wonder, it's like other people below us, Are they wondering what's happening? I don't know.

**[01:05:45]** How long have I been jumping? How many jumps was that? I don't know. Okay, I think, I think that's 10 more. Okay.

**[01:05:55]** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. Okay, done. Okay, great. Data collected, NOT processed.

**[01:06:20]** Okay, let me see if I can get this thing running. I'll give it one. One more college try, as they say.

**[01:07:12]** Oh, I need to give myself enough time to clean up too.

**[01:07:20]** Okay, good.

**[01:07:48]** Alrighty, so let's see. So UV Venv.

**[01:07:59]** Come on.

**[01:08:04]** Do this from a terminal, then dot Ben scripts. Activate UV sync. Punch that and free mocap.

**[01:08:28]** Oh, Skelly, cap damage.

---

### Chunk 8 [01:08:16 - 01:18:15]

**[01:08:16]** Punch that and free mocap.

**[01:08:28]** Oh, Skelly cap. Damn it.

**[01:09:01]** Scripts. Activate UV sync and.

**[01:09:09]** Huh, huh, huh, huh.

**[01:09:19]** Oh, right. You can't see anything. Sorry.

**[01:09:35]** Sort of the fundamental nature of working on anything for any length of time, particularly if the thing you're making is something that other people are using, the version of, the thing that the people are using is the version that you are ashamed of. Because the code for this I wrote years ago. I've learned so much since then that when I look at this, I'm like, oh, my God, I'm so sorry to the world for what I've done to it. Okay, so this is freemelkat. This is the core software.

**[01:10:11]** And if I do that, click on that, say, set active record.

**[01:10:24]** Oh, yes, yes. Run calibration from active recording. Run calibration. Okay, so we're now running calibration data, and it's going through. I can put my shoes on at least.

**[01:10:48]** It's going through and detecting the boards in the screen, it'll take a little bit of time, but at this point, I think we should be able to get, like. We'll be able to look at something by the end of. Before the end of the day, which will be good.

**[01:11:15]** Does anyone have any burning questions while the thing is running? It's one of those things, like, I'm sure there are many questions, so can anyone choose one question from the many that are floating around?

**[01:11:33]** I also made a mistake because I was, like, talking during this calibration thing. So I was doing it, and there's a point I was like, blah, blah, blah. And then so it's longer than it needs to be, which is Rookie mistake.

**[01:11:50]** This is the code that I am, like, currently rewriting. Like, I'm currently rebuilding the calibration part of it, which will allow it to do much more.

**[01:12:03]** It'll be faster.

**[01:12:17]** Okay, I guess I could look at the other stuff, but I don't really want to do that. That feels like cheating. Like, I have recordings from the past, but that's. That feels like cheating right now.

**[01:12:50]** Yeah.

**[01:12:58]** Okay.

**[01:13:05]** Yes. Okay, now this stuff is going through.

**[01:13:13]** Yeah, Great.

**[01:13:16]** So now. Now. Now you have this object, which is. I can't write it for some reason. So camera zero.

**[01:13:28]** Camera one. Camera two, camera matrix. And then these are the two points that matter. Rotation, 1, 2, 3. Translation, 1, 2, 3.

**[01:13:39]** Camera one is defined as zero. So these are the six degrees of freedom that we need for each of the cameras. So we now know where all the cameras are. These are measured in millimeters. And theoretically, you know, one and a half.

**[01:13:52]** So 1500 millimeters is like one and a half meters. Thousand meters. So they say that they're, you know, meter to two apart, which checks out intuitively. So now that we have that, we can.

**[01:14:11]** Okay, I think let's look at the jump, the big jump. That's the most fun one, I think. So that was the. Actually, yeah. Oh, it's kind of off screen there, but we'll see how that goes.

**[01:14:39]** Set as active recording. Okay. Use the most recent calibration and that one's probably the shortest too. So go ahead and process.

**[01:14:54]** Okay. So if all goes well, if you see my blender, you do see my blender. Great. So now what it's doing is it's going through and in each of the videos is going through frame by frame. So let's say if it's 1,000 frames of recording, which is whatever 30 seconds or less than 30 seconds actually, then for three cameras you have 3,000 total images.

**[01:15:25]** And then in each of those images you have to run through and do the relatively heavy computation of using the convolutional neural network to try to detect where the person is in the screen in the recording. And that will look. Oh, actually that's from old. Okay, nevermind.

**[01:15:50]** Yeah. And so once you have done that, you will have 3,000 two dimensional estimates of where I was in space coupled with estimates for where each of the cameras were in space. And so you can do. Don't worry about that, that's normal. So from the two dimensional estimates in the images plus the six degree of freedom positions of the cameras, you can triangulate the position of each of those points by basically just imagining firing a laser.

**[01:16:28]** So like tracking my elbow from camera 1, 2 and 3, it. If you imagine you fired a laser from each of those cameras, the place where the lasers cross over each other is the position of that object in space.

**[01:16:41]** And all of that is going to happen under the hood very, very fast. And it's all just a bunch of. That kind of geometry hasn't changed in 1,000 years. It's the same stuff that's like Euclid level geometry. It's just now being done much, much, much faster on a strange rectangle of silicone and electricity.

**[01:17:13]** But yeah, once this pink line. Oh, are we still running? Oh, good. We can actually.

**[01:17:28]** Yeah, so it looks roughly like that. So this is the output from one of the videos. So this is.

**[01:17:41]** So from the perspective of, I guess that camera, this was the location of my right shoulder. That's the left shoulder. There's a bunch of points on my face. These are hips, ankles, toes. Basically tagging all the joint centers in two dimensional image coordinates, which we can.

**[01:18:09]** And so. Yeah, so that's a.

---

### Chunk 9 [01:18:01 - 01:27:59]

**[01:18:01]** Which we can.

**[01:18:09]** And so, yeah, so that's all well and good, it's useful information, but you would have a very difficult time doing any of the physics y kinds of stuff that we were talking about on this data, because you don't really have a measurement in this case of like where the ground is. Like, you don't really have a measurement of what up is you have up in the image, but you can see that the image is tilted. So if you're want to say, oh, you're moving relative to gravity, like you want to say your balance over your feet, those are all terms that happen in the reference frame of like the physics we said we call it the inertial reference frame. And this data is all coming in in camera sensor reference frame. This is 00 in image coordinates, just the upper left point of the screen and that's 00, meaning the upper left corner of the little silicone wafer at the back of the camera thing.

**[01:19:09]** So converting that into something that is pretty strange that that one is like running so much slower than the others.

**[01:19:21]** But to be able to be able to talk about this data in sort of these physically grounded terms that we've been trying to sort of build up requires a transfer and sort of a lot of computation to sort of to get this data referenced in a inertial reference frame. Okay, what's going on? Okay, cool. So now the pink lines are gone, which means we've done all the 2D estimation and this white much, much faster line is doing all of the triangulation. So 550,000 data points just cranking.

**[01:20:03]** Yeah.

**[01:20:07]** And how are we going doing that recording data? This takes a while now.

**[01:20:24]** Okay. Yeah, it's now saving stuff down to disk and now it will, with any luck, start cranking. Yeah.

**[01:20:42]** Come on, buddy.

**[01:20:45]** Yeah.

**[01:20:49]** Yes. And so now this part of the code is now sending. So at this point we've done the main task, we've recorded the person, We've done the two dimensional thing. The 3D reconstruction has actually already happened. And now a very important, often neglected step is occurring, which is converting it into a human, into some visualizable format.

**[01:21:13]** So something that we as humans can look at and make sense of. Because saving all the data out into like a massive CSV Excel spreadsheet is good, but it's still not a term that we can really make any sense out of. So, or format that we can make sense out of. So this is Blender, which is a 3D animation software. And this is where we see if it actually worked well.

**[01:21:38]** Which I feel.

**[01:21:42]** Let's see how it does. So not in the screen. There we go. Here I am. Okay, so this one is not looking the best.

**[01:21:57]** So you see this one, the image is upside down. It's going to fix. Oh, man. There we go. So that was actually a nice case where this is a good view.

**[01:22:12]** This is a good view. This one, it's seeing the skeleton upside down. So this reconstructive view is not going to look right because a third of the data is flipped upside down. And luckily I took a few steps forward and then it fixed itself. And so now this is a much better looking skeleton.

**[01:22:39]** So now that I know it works, I can belabor the point.

**[01:22:44]** It's a little bit rotated, which I can fix later. So rotate around X. There we go.

**[01:22:55]** This pink and blue ball here is the calculated center of mass. The skeleton is sort of more for visualization than actual data.

**[01:23:11]** This, these stick figures here, those are the rigid bodies that I was talking about. So this is the thigh, the upper arm, things like that. And cool.

**[01:23:35]** Yeah, great. So now.

**[01:23:47]** Okay, so it's not the best data I've ever gotten in my life. It's just very dark in here, but it's not bad. And if I look.

**[01:24:18]** So that is the trajectory of my center of mass in the Z coordinate. So the ground plane we're going to call XYZ up is Z.

**[01:24:31]** And. Yeah, so this is a time series plot. We talked about these last time. So the X axis is time and then the Y axis is whatever the Z value. That, however, is the height.

**[01:24:45]** That's the height of my center of mass above the ground. And if you recall, if gravity didn't change, my mass didn't change. So that means the height tells you my potential energy. If we assume that this is where I'm. This is my standing height, we can call that zero if we want to.

**[01:25:03]** That's zero potential energy. And then here we see something interesting happening. So before I. You've seen this several times. Now I do got to stop and we're going to talk about this at length next time.

**[01:25:18]** But just imagine at like my center of mass level. Like we have some guess about what this behavior corresponds to. So think about what is this dip, what is this peak and what is this dip again?

**[01:25:34]** And oops. Wish I didn't do that.

**[01:25:44]** Come on. There we go.

**[01:25:51]** So there we go. That's my lowest point. Skeleton is kind of screwy just because it's a weird view and I'm kind of off screen here.

**[01:26:05]** But go up and That's. That's the peak. That's the apex of the jump. That's the highest. This is the place.

**[01:26:17]** My potential energy is at its highest, and my kinetic energy in the Z position is zero. I am paused at that height, and now I'm coming back down.

**[01:26:33]** And again, the data is not the best in the world, but you can see that kind of.

**[01:26:42]** I don't just land with, like, straight legs. I land and I bend into it. There's intuitive reasons why, but then there's also, like, deeper biomechanical and physiological reasons why this is a lot of energy I have to bleed off, and I don't want to bleed it off directly into my joints. I would rather bleed it off into my soft tissue and let the muscles kind of pull against it so that I don't blow out my meniscus or something like that.

**[01:27:12]** And then I do it again.

**[01:27:18]** And so this is also kind of a nice example of why the center of mass is such a nice measurement. Because even in these cases where the data is not that great and the skeleton gets all warble garble in these particular moments, the overall trajectory is, roughly speaking, what you would expect it to be. So. So even in context where the data has fidelity issues, you can still talk about the global data because it's basically a giant smoothing algorithm to just collapse this entire thing down to a singular point. Whee.

**[01:27:53]** And I gotta go. But I can't help myself.

**[01:27:58]** In range around.

---

### Chunk 10 [01:27:45 - 01:29:51]

**[01:27:45]** To just collapse this entire thing down to a singular point. Whee.

**[01:27:53]** And I really. I gotta go, but I can't help myself.

**[01:27:58]** In range around frame 30. 30.

**[01:28:05]** Calculate the whole thing. Okay, Display.

**[01:28:23]** So that is the frame by frame measurement of it. You can see this, the 3D trajectory.

**[01:28:33]** Oh, why did it go. Oh, it's not doing the whole path. Oh, because it's much longer than that date. Paths.

**[01:28:54]** There you go.

**[01:29:00]** And here we can even take the whole guy. Hide them. Hide them.

**[01:29:12]** So that is the mechanical estimate of the global behavior. Okay, I will take my time. I'll clean this up. And think about. Think about the things we talked about.

**[01:29:31]** Make some general predictions. I'm gonna make an assignment for y' all for next. For the next. For next week about talking to the bot about predictions around this data stuff. And also about just, like, the concept of units and measurements and how it applies to your particular domain of inquiry, but just, you know, chew on it with your brain.

---
