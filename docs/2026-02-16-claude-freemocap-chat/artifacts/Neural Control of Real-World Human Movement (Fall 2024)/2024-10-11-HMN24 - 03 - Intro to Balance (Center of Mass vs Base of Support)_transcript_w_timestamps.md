# Transcript: 2024-10-11-HMN24 - 03 - Intro to Balance (Center of Mass vs Base of Support)

## Source Information

- **Source Type:** Local File
- **File Path:** `C:\Users\jonma\syncthing-folders\jon-alienware-pc-synology-nas-sync\videos\video_eater_downloads\playlists\Neural Control of Real-World Human Movement (Fall 2024)\2024-10-11-HMN24 - 03 - Intro to Balance (Center of Mass vs Base of Support)\2024-10-11-HMN24 - 03 - Intro to Balance (Center of Mass vs Base of Support).mp4`

---

**Total Duration:** 01:15:23

---

## Full Transcript

### Chunk 1 [00:00:00 - 00:09:59]

**[00:00:00]** Okay, great. Hello.

**[00:00:05]** So welcome to October, if you already had one of those, but welcome to October 8th. So, yeah, so the. So today we're going to talk about balance and center of mass and base of support and talk about that kind of thing. And then after about an hour of talking about that kind of stuff, we're going to do some group stuff again. But there's going to be sort of like our first kind of technical split option.

**[00:00:38]** So if you are a person who is interested in code and programming and that type of thing, you'll have the opportunity to kind of split off and work on that kind of thing. If you're not interested in that, you can hang out and we'll do more like that, review types of stuff. If you've never done it but are curious, then you're interested in it. Interested is not experienced. That's a separate thing.

**[00:01:04]** So the first thing I want to sort of show before we get into the meat is this thing that's going to be kind of like a rolling kind of checkpoint throughout the semester, which is the AI weird aspect of this class where I have now the first instance of an example of scraping the server. So basically pulling all of the chats you've been having with the bot, effectively that like markdown text file that gets attached to the top of each chat. I pull that out, run it through the AI, say, summarize this, pull out the main points and main topics, and then basically do that for like each chat in each channel, in each category, and then the whole server. And the idea is to sort of use that to try to get a sense of like, what you guys are working on, what you're interested in. And for now it's kind of like, it's just descriptive.

**[00:01:56]** So it's just like y' all are doing what you do. And then this is sort of pulled and you can look at it if you want. But one of the things we're going to do in that second half of class is sort of starting to steer this a little bit. So say, what are some things, things that seem to be coming up for a lot of people and like, can we sort of get more details about those topics? Can I look at that and say, oh, they're really interested in this thing.

**[00:02:16]** Let me talk about that next lecture. That kind of sort of more of a feedback loopy type of thing. So the thing is a zip file, so if you download it, it will go to your downloads folder, whatever that may be for you.

**[00:02:37]** Why are you slow?

**[00:02:47]** Why are you so slow?

**[00:03:02]** So you can unzip that so that it's just a regular folder in your. Oh, come on now it's giving you all that invalid thing.

**[00:03:27]** So it's here. So in the server, in the resources channel at the top, there's a thread called Server Scrape checkpoints and there's a zip file. And I am totally happy saying that this CheckPoint is. The zip file is corrupted and we'll figure that out later. Cool.

**[00:03:44]** So if you can figure it out, great. If not, it's a bunch of basically like poorly formatted summaries of the things. Things we've been talking about. And we'll just call this foreshadowing.

**[00:03:58]** There's a couple other things in that resources channel too that I added. One is this link up here to a YouTube playlist of these videos, except for last one's video because I forgot to save it. I forgot to hit save save at the end of this. And I wasn't saving to a video format that is forgiving of closing the thing mid recording. So that video is lost.

**[00:04:24]** Rip lost data. It happens. And then. So yeah, and then. Yeah, that's another one of those.

**[00:04:31]** Like maybe we'll get to the thing where I can scrape the video and pull the transcript and get the topics out and put that into that. But we'll see about that. There's also this link to another playlist called AI Stuff, where I talk about things like building stuff, Skelly Bot and like using it in classroom settings like this. So if you're interested in that kind of like meta AI ed tech stuff. Watch that.

**[00:04:56]** Yeah, and then the third thing I added to the server is in this lectures category over here. This one down here, which the string of numbers is the date. So 2024, 10 08. Just a way to write your date concisely. That's called Little Endian, meaning the little things are at the end of the number.

**[00:05:16]** So here's the big, big endian. Little Endian. That's what that means. If you ever come across that again, Compsite people might. No one else will.

**[00:05:27]** In that I put a link to an outline of what I'm going to talk about today, which is some terse. No. Are these links that work? These links don't work, but maybe you can figure it out. They're over here.

**[00:05:42]** Okay, cool, Cool. So far, didn't really give you any option choices there.

**[00:05:56]** Did you say we were creating the vaults? Yeah. So Obsidian calls folders vaults and so you want to be opening that folder as a vault. If you feel like Playing with that stuff. Go to any chat and just download the MB stands for Markdown.

**[00:06:13]** It's the thing that turns this looking text into this looking text. So you just type it out in the raw. And then if it's MD and the thing that you're looking at knows how to process markdown files, it turns it into that. So download any. The chat at the top or download this.

**[00:06:42]** Markdown, I feel, is the sort of the seed of the revolution, because it is. We have just generally internalized this idea that, like, text is like Microsoft or Google, when it really, really isn't. Like, text is like a behavior that you do on a keyboard and we want it to look nice, but this is the RAW that we actually care about, is this. And so it's also the first sort of entry point to like, hey, there's such a thing as interpreted text. You type this thing, the computer knows how to make it pretty.

**[00:07:15]** And yeah, also Google Aaron Schwartz, if you know who that is, he's one of the people who sort of came up with the original definitions for Markdown. And you should look up who he is and then steal every paper ever published. A lot of professors be like, be careful. Don't go to Sci Hub or you'll accidentally steal papers. I'm telling you explicitly, go to Sci Hub.

**[00:07:40]** Steal papers, steal textbook from Libgen. As a scientist, as operating under my academic freedom, it is the best thing I can do for you to say, fuck every publishing industry. Steal all their data. Steal all their. Yeah, they think it's their intellectual property.

**[00:07:56]** It's not. It's ours. Steal it from them. Okay, so none of that is relevant, though. So we've been talking a lot about center of mass.

**[00:08:09]** I've sort of described it at various levels and today I brought a series of props to help present that. Hey, Aaron, could you screw that together? Thank you.

**[00:08:23]** So part of, I think also part of the pattern that's emerging is I show up late, I set up, takes a while, I'm frustrated and sweaty. I eventually get it working. I give like a little update on like the technical back end and AI nonsense. I have some sort of like moral outrage moment. And then I talk a little bit about like philosophy of science and then we get into the actual topic of discussion.

**[00:08:47]** So this is the philosophy of science part. So I've talked about the concept of reductionism, which is one of those things where it's like, it's such a fundamental aspect of the way that we live in this sort of society and the way that we basically, the way that we do science in the Western tradition is a heavily reductionist tradition, meaning that you take a big complicated thing and you chop it up into tiny, tiny, tiny little pieces, and then you look at those pieces in isolated environments. And then you sort of hope that the things that you learn about those small scale, isolated things will scale up to the larger actual desideratum of your study.

**[00:09:31]** And generally speaking, it does. Right? That's why we do cell biology, that's why we learn about genetics, that's why we learn about particle physics and periodic tables and stuff like that. Those are all fundamentally reductionist approaches to science. Reductionist kind of sounds like an insult, but it's not.

**[00:09:47]** It's just a description of a way of looking at things.

**[00:09:53]** The counter to that doesn't really have so defined of a name, but I generally sort of think of it as like more of a holism where.

---

### Chunk 2 [00:09:45 - 00:19:44]

**[00:09:45]** This kind of sounds like an insult, but it's not. It's just a description of a way of looking at things.

**[00:09:53]** The counter to that doesn't really have so defined of a name, but I generally sort of think of it as like more of a holism where instead of taking the thing that's sort of. Because the problem that reductionism solves is that science is impossible. Right. Rule number one can't be done. We mere primates do not have access to capital T, true facts of the world.

**[00:10:12]** We can only approximate it with a bunch of sloppy empirical measurements and then statistics. The problem of induction and black swans, if you want to dig into that hole. And so because we can't actually do the thing we want to do, which is like, have true knowledge of the real world, we have to cheat and take various sort of sidesteps and whatnot. So the traditional Western reductionist view of science is chop it up into little pieces and hope that those pieces sort of fit together into something that resembles the whole. A more holistic approach cheats in a different way where instead of taking the whole thing and chopping it up into little parts and thinking about all those parts in isolation, you take the whole complicated thing and you kind of just like squish it down into what you think or hope is like the minimum possible.

**[00:11:08]** Like the simplest possible model of that thing that captures the dynamics of the whole thing. So things like center of mass, which talked about, and we'll show some pictures in a second, is fundamentally that approach. And I've mentioned before, this is like not necessari. This is not something you're likely to find in like specific textbooks. This is more like the things I've cobbled together in my research.

**[00:11:33]** It's sort of inspired a lot by robotics approaches. If you look up passive dynamic walkers is a classic one. Art quo, Andy Ruina, Steve Collins, all those good folks looked at how sort of taking the whole complicated object and then reducing it down to a single point mass can be very helpful towards trying to understand what's going on there.

**[00:12:09]** I think I forgot to.

**[00:12:15]** Yeah. So I brought a stick. So this stick, this is like the. The middle part of like a floor lamp. And I found it on the street.

**[00:12:28]** I tried to use it. It wasn't. Didn't really work right. And then I realized that the middle part not only comes apart so I can put it in my backpack and bring it to class. I used to have like a broomstick that I cut at a meter and brought it in the class.

**[00:12:43]** But this thing Pulls up also very nicely. This turns out to be actually one meter long. So I think somewhere at some factory, someone ordered a bunch of like meter long poles and cut them up. And then now this is a meter stick. So it is aluminum or metal and roughly straight.

**[00:13:07]** It has some extent, but we can ignore that. And it also is in even sections. So this part here is the geometric center of the stick. And if I put this little thing here, then I can know that this is both the geometric center of the stick. It is also the center of mass of the stick.

**[00:13:29]** So if I take this object, I want to do this now or later, I'll focus on this. So basically, if I take this stick and I chop it up into like 1cm sections, so there will be 100 in a row. And I took the average position of each of those points. Literally just take the XYZ of this one, XYZ of that one, XYZ of that oneS, add up all the X's, add up all the Y's, divide them by the number of chunks, the resulting average position will be here. And it turns out that from a point of view of like balance physics, that is the point that you need to support in order to keep the thing from falling down.

**[00:14:14]** Whoa. Right. So that is true when you're supporting it from the bottom. It is also true.

**[00:14:24]** So this is called loop. Pull the loop through itself. That's called a girth hitch. If you pull it through again, this is called a Prusik. And it tends to and it stays where it lives.

**[00:14:40]** I have trusted my life and the lives of many people I love to knots in various contexts. So a Prusik I can nicely put over that little yellow spot, crank it down so it will stay. And in the same way that balancing it from below the center of mass keeps it sort of where it needs to be from above. It's the same basic idea. So there's more mass on this side than there is on that side.

**[00:15:13]** So I move it over a little bit and hooray, balance. Right. So in this case, because this is a uniformly massed object, the geometric center of it and the center of mass are the same place.

**[00:15:30]** Yes. I also found these on the street. There's a lot of fun things on the street if you know where to look. These are like, like old school, like ankle weights, I think. Like, you know, or put them on your ankle, I don't know.

**[00:15:46]** And this is like carpet pad. So it's high friction. And if I roll it up like this, that.

**[00:16:01]** Okay. So I'VE changed both the geometry and the mass distribution from the point of view. So the geometry in the sort of the long axis of this thing hasn't actually changed much at all. Right. It's the same length around the.

**[00:16:19]** In this particular, particular case. So for any 3D object, you have a long axis, you have a middle axis, sometimes called intermediate axis, you have a short axis, which is the short one. Sometimes they are symmetric. In this case, the middle and medium intermediate are symmetric. So you get that.

**[00:16:38]** You can also Google the intermediate axis theorem, otherwise known as the tennis racket theorem, which says that you can spin it around the short axis, you can spin it around the long axis, spin around the middle axis, it flips midair. Not relevant, but fun. There's some cool gifs of people doing stuff on the space station, but that's not important right now. So unsurprisingly, I've changed. Basically I've changed the geometry a little bit.

**[00:17:04]** Not in an important. Not in a relevant dimension, but I've changed the physics a lot. So now this side is much heavier than that side because. So before we were just taking the geometric mean. You just take the positions of each of those points, take the average, and it happens to line up with the center of mass.

**[00:17:23]** In this case, that doesn't work because all of those points that I'm adding up do not have the same density. This is full of sand or something, I don't really know. So I can put the thing over here and there we go. So now this is the center of mass. So the geometry for our basic approximations hasn't changed, but the physics has changed quite a bit.

**[00:17:56]** And so the center of mass has changed. And so that balance point has changed both when you're supporting it from the bottom and when you're supporting it from the top. Right. Basic idea.

**[00:18:12]** If I wanted to do another one, there's two of them.

**[00:18:20]** I can.

**[00:18:29]** There we go. Once again. Even heavier. So I can move it basically all the way over here and it's not quite right, but now, yeah. So now it's the center of mass of the whole stick system is very close to the big bob at the end.

**[00:18:52]** Notice that the first time I moved it, I had to move it all the way over here. The second time I had to move it far less. That's because of torque is a thing. This is really hard. This is really easy.

**[00:19:04]** When we talk about the musculoskeletal system, this will come up again. If you're curious about how, notice that my arm also resembles a long stick. And my shoulder, which is the main thing leaving it up, is this long and attached right here. So it's much more like doing this than doing this. So, spoiler alert.

**[00:19:28]** Your muscles are, like, unbelievably strong relative to the tasks that they can perform because they're operating at a massive mechanical disadvantage. That's not important right now.

**[00:19:39]** So. Yeah. Okay, so this is.

---

### Chunk 3 [00:19:30 - 00:29:29]

**[00:19:30]** Unbelievably strong relative to the tasks that they can perform because they're operating at a massive mechanical disadvantage. That's not important right now.

**[00:19:39]** So. Yeah, okay, so this is intuitive center of mass. There is a difference between the geometric center of a rigid object and the center of mass. And center of mass also you'll hear it be called center of gravity. Those are the same thing.

**[00:20:02]** This is gravity being used in the term like density. Center of gravity just feels a little more old school to me. Or in space, in all contexts that matter for us. Center of mass, center of gravity are the same thing. So if you ever see cog in a paper, it's the same thing.

**[00:20:18]** It's just using a different term. Yeah, center of. It's like, yeah, basically center of density would be another way to say that. But that's not quite right. Okay, so this is a stick made of trash I found on the street.

**[00:20:36]** Excuse me. This is a little wooden fellow. And it also has a center of mass which I could measure if I wanted to. I'm allowed to chop this up, but I don't want to. But it is here.

**[00:20:52]** If our friend did one of those. Oh look, it tips over. So I have to move it sort of more to this abdomen area. So as you move the mass of your body, the center of mass shifts. Like I said last time, center of mass is not a part of your body.

**[00:21:07]** It is a description of your body. And if you do one of these types of shape, the center of mass can be outside of your body. So the center mass is like here. Because it's below that point of rotation, it becomes passively stable. And I can kind of perturbation rejecting, which we'll talk about shortly.

**[00:21:32]** So this would be a link, but it's not. So I click over here. So. So this center of mass approximation is like, I think a very important and very useful hyper simplification of the full complex object. It falls under the general heading of like classical mechanics, which is like a part of mechanical engineering, if you're trying to find the right building to walk into.

**[00:22:03]** And it specifically falls, falls under. I think it's called the finite element theorem, which basically says that you're allowed to look at the center of mass as a proxy for the dynamics of the whole thing. So taking this complicated object, chopping it up into finite elements and then finite small but not zero, and then looking at the mean of those points tells you about the, the, the full. Tells you things about the dynamics of the full complex object. And I think that's honestly, I find that, like keys, I find helpful to think about that because this is also complex.

**[00:22:52]** It's like dangly.

**[00:22:55]** But if you sort of throw it, no matter what you do, it still follows a nicely ballistic trajectory. And you can also use this to show that even if it's spinning, it will spin around its center of mass and follow a ballistic trajectory. So, you know, each of these keys is a rigid body. They're connected by rigid bodies, so there's no stretch or strain or anything like that. In the ballistic case, it wouldn't matter.

**[00:23:23]** But I think it's funny to do that with people.

**[00:23:32]** So in this case, I don't know how much this stick weighs. I know that it's 1 meter long. I don't know how much these ankle weights weigh. But if we wanted to, we could figure out the mass of the weights in units of stick mass using this kind of math and sort of learn things about the forces at play and things like that. And if we were trying, if we were controlling this with muscles, that information would be very relevant to us.

**[00:24:07]** If you want to do that for like a human person, it's. So basically, I want to be able to calculate the center of mass of a person, but how do I get those numbers? Well, it turns out someone chopped up a bunch of dead people and weighed them. And we have these anthropometry tables. A really common one is Winter, which is from like a biomechanics book.

**[00:24:35]** And I think these tables here, it shows where they came from. I think it was like, like air force data. They chopped up cadavers and looked at the relative densities and did a bunch of statistical analyses, and you get numbers. So this is the geometry of it. And so these numbers here, like you have to be able to read it, but it says 0.520 h, where h is the total height of the person.

**[00:25:04]** So this is estimate of sort of relative proportions of different body segments in terms of just in units of height. Importantly, all the dead people they chopped up were men. All the dead people they chopped up were old men because they were dead. Often there's a correlation between age and dying. There are newer anthropometry tables that look at a broader demographic, different genders, different sort of body mass indices or whatever.

**[00:25:42]** But by and large, a lot of those differences are small. And relative to the scales that I tend to look at in my research, they don't really shift the numbers that much. So just kind of use these because it's a standard and it's around so these names here correspond to roughly to these guys up here and they give you the name of the thing, the definition in terms of anatomical axes. So the foot is defined as the lateral malleolus to the head of the metatarsal tube. So malleolus is that guy on the outside.

**[00:26:23]** Metatarsal is your to. I don't know. Malleolus 2 is like, it's like your index toe knuckle, if that's the thing. And then it gives you the segment weight as a proportion of total body weight. So your hand is roughly 0.6% of your body mass.

**[00:26:43]** If you have standard, standard size hands, forearm, upper arm, your foot is about 0.01. So like 14%.

**[00:26:57]** It seems high, but I don't know. Your leg is 0.046 point. Oh, sorry, 4%. Yes. Thigh is 10%.

**[00:27:06]** And then it gives you like foot and leg is, you know, added up ones above it. So in the center of mass calculation I was showing last time with the blender thing and that little ball is moving around, around. Those were calculated by using these numbers. And we'll talk about that in a little bit. But just wanted to show roughly where that stuff comes from.

**[00:27:31]** I also. So some time ago in different life, I made a bunch of gifs and posted them on Reddit. In fact, before Reddit was, it was still a cesspit, but it was a different kind of cesspit. And basically I would just go and find videos of people doing interesting things and then just overlay them with basically center of mass analyses. So this is the hand forearm, blah, blah.

**[00:28:03]** It's a planar view. So meaning that it's basically a view from straight down one of the XYZ axes. So you basically get to ignore the 3D aspect of it and just focus on the 2D. The vertical lines show the extent of the base of support, which is basically where his hand is. And then the thing to notice is that the center of mass always stays within that boundary because it has to, because if it didn't, it would fall over.

**[00:28:31]** And there's a bunch of these.

**[00:28:39]** This one is wacky. So this one I was getting fancier, so I was actually stabilizing the image. And this guy's very good at this type of thing. And so once again, just always stayed there. Center basis for shifts where he shifts his hands and see like he's doing.

**[00:28:59]** See, look how screwy this like. Yeah, yeah, he's a freak. Archer using dynamics to sort of pop himself up. But keeping it within this range. The important thing to know that his hand can only push on the ground.

**[00:29:17]** So if the center of mass ever left those boundaries, he cannot pull it back. He can only push it farther away. And this one?

---

### Chunk 4 [00:29:15 - 00:39:14]

**[00:29:15]** His hand can only push on the ground. So if the center of mass ever left those boundaries, he cannot pull it back. He can only push it farther away. And this one is a violation of that rule. So this is balance beam, otherwise known as the hardest.

**[00:29:36]** What's it in sports, she does this cool thing, but, oh, no, she falls. But then she pulled it back in. The most important part of that video for me is this point right there where it does go out, but she has a grip on the bar so she can pull back in. This is the same basic idea, the wobble. The center of mass is noise in the estimates.

**[00:30:08]** All right, so those links are all there. There's a bunch of them. Click through them.

**[00:30:15]** We'll talk about them at some later date, perhaps.

**[00:30:29]** Okay, so roughly speaking, that is the important thing. There is center of mass. We did talk. And then also this concept of base of support. Your base of support is just like the shape on the ground of your support surface.

**[00:30:47]** My base of support is defined by my feet. This thing's base of support is defined by that little point. It is not passively stable for various reasons, which I will describe.

**[00:31:25]** Okay, so real quick, physics. Newton was a guy. He did a thing. He, among other things, is he came up with this sort of theory of mechanics, which is embodied by Newton's three laws of motion, which are false and wrong theoretical models of reality. This is, I think, a great example of how wrong theories are still useful.

**[00:32:02]** Newton had a theory of reality where there was such a thing as position and velocity. And wasn't until far later that some guy named Einstein came along and wrote some papers. I really don't like ascribing these thoughts to specific people, because really, they're just the specific humans that wrote it first. People say Newton invented calculus, but Leibniz also invented calculus at the same time in Germany with better notation. Oftentimes these are just ideas that are just ready but beside the point.

**[00:32:33]** So Newton's theory of classical mechanics is false on a scientifically theoretical basis. If we wanted to actually calculate things like momentum, we would have to take into account things like relativity theory and E equals MC squared and whatnot. But we tend to move at speeds that are so much slower than the speed of light that it would be not only insane to require that level of precision, but impossible to measure at that level of precision. So we instead just use the. The three regular laws.

**[00:33:08]** So that's what is it? Basically, law one is inertia exists. Things moving in a straight line tend to keep moving unless acted on Object in motion tends to stay in motionless, acted upon by force. Number two is really our best friend here. F equals ma.

**[00:33:27]** So force equals mass times acceleration. If you have a mass that is accelerating, that is called a force. Mass is measured in kilograms. Acceleration is measured in meters per second squared. Or really distance is measured in meters.

**[00:33:41]** Time is measured in seconds. Acceleration is meter over seconds squared. And so kilograms times meter squared, we call that Newton. Correct. And then three is for every action there is an equal and opposite reactance.

**[00:33:57]** So you push on something, it pushes back.

**[00:34:05]** So I spent a lot of my earlier academic life thinking hard thoughts about pendulae pendulums. Pendulae. I even brought up show and tell book. This book is called 7 Tales of the Pendulum. It's great.

**[00:34:24]** Great. It's about basically like seven cases of like ways that like pendula pendulums have been like very core to the way that we do science for a very long time. And there's all sorts of crazy stories in here about like using pent, like using clocks to be able to traverse the Atlantic Ocean. Like you had to invent the clock before you could traverse an ocean. Using changes in the period of a pendulum to figure out the density of the ground below you to find iron Foucault pendulums, which are like the things in museums that knock the sticks down if they go in a circle.

**[00:35:01]** But anyways, so this is called a free body diagram. And this is a hanging pendulum. Let's call this L. That's an L. And let's call that. Who cares? Let's call that that.

**[00:35:19]** So that's basically this. So we have a point of mass dangling below a point of rotation. And we're going to pretend that this stick has no mass, which we kind of approximate by this thing because the mass is so heavily towards this side. And I'm going to make this about balance and posture in a second by basically taking this and putting it up like that. But let's focus on the basics for now.

**[00:35:52]** So this is the mass, we'll call it. And then this is gravity.

**[00:36:03]** Gravity is 9.8 meters per second per second. Let's call it 10. So gravity is pulling down, which means that this string is pulling up because gravity is pulling down at 10 meters per second per second. But this thing isn't moving. Right.

**[00:36:19]** And we know that if there's something, if there's a force acting on a mass, then it has to be moving. So if there's a force acting on the mass and it's not moving, then there has to Be an equal and opposite force acting statically stable. Great. So now let's push it up here. This is still L, same length.

**[00:36:43]** Let's call this theta. Don't. You don't have to worry about it. Gravity is still pulling down the same force, same mass it has, except now we know that it will pull. This will now accelerate.

**[00:36:59]** So gravity is pulling like this. And then we do some vector decomposition thing. And then it's like the string is still pulling on it, but it's not aligned with the axis of gravity. So there's this leftover arrow, and that arrow is pushing this way, which means it's going to accelerate that way. And then it does like this.

**[00:37:27]** So, details, details. But the important thing here is just to note that basically you have a mass here that's sort of. You can lift it when it's at its sort of zero point. So right now. So we can look at.

**[00:37:43]** So the theta when it's here is zero. Like just say the angle of deflection from the vertical point is zero. Great. And then we move it over here, we say angle is theta, which is just some arbitrary angular number. Could be 12 degrees, it could be one radian.

**[00:37:59]** Doesn't matter. And when we put it over here, it has.

**[00:38:05]** If we let it go, it will swing back. And intuitively, we kind of know. We've probably seen the demo where you pulled the thing and let it go and it comes back, doesn't hit your face or whatever. Once it's the Internet and then you edited the video and you do get hit in the face.

**[00:38:21]** So as it goes over here, it will pick up speed, it'll pick up momentum, and it'll get back to the same point that it was before, except now it's going to. Instead of its velocity being its angle being zero, its velocity being zero, its angle will be zero, but its velocity will be high because it's swinging. And then that will sort of take it up over here until it bleeds off all that speed. And then, spoiler alert, that would be negative data if there's no friction or whatever in the system. And then now we're over here and we're in the same place we were before.

**[00:38:57]** And so we're going to go back, and so we swing back and forth. And so there's two main things to note here. So this point here. So think about. With mechanics, you pretty much have potential and kinetic energy, if you're not thinking about things like stretch and strain.

**[00:39:14]** So.

---

### Chunk 5 [00:39:00 - 00:48:59]

**[00:39:00]** So we swing back and forth. And so there's two main things to note here. So this point here. So think about. With mechanics, you pretty much have potential and kinetic energy, if you're not thinking about things like stretch and strain.

**[00:39:14]** So when I take the thing and I throw it up and I catch it, when it leaves my hand, it has kinetic energy going up, back. So potential and kinetic energy, whatever potential energy is mass times gravity times height. Mass doesn't change, gravity doesn't change. Let's just say potential energy is the same thing as height. Kinetic energy is 1/2 MV squared.

**[00:39:43]** 1/2 doesn't change, mass doesn't change. Who cares about square? Let's just say kinetic energy is the same thing as speed. So. So you have your height and you have your speed, and that basically defines your mechanics.

**[00:39:59]** Yeah, so when you throw something into the air, you start out with a lot of kinetic energy pointing up. And as you go up to the next time step, gravity is going to pull down, it's going to sort of bleed off some of your vertical height.

**[00:40:15]** And then eventually it's going to take all of your upward kinetic energy and then you'll have to sort of hang up here at this apex point, maximum height, zero velocity in the vertical. And then it repeats that process and you do this nice parabolic trajectory. And if you want it to be nice and parabolic, you have to care about the square. But that's not important right now.

**[00:40:45]** Yeah, so hanging pendulums are. I'll just mention this just for the symmetry of it and it might come up later. I guess I'll come up with the jumping stuff. So when you have a pendulum that's a simple harmonic oscillator swinging back and forth, they're sort of two to three points to really think about. One is at the apex here where it has the maximum height but zero.

**[00:41:16]** What's the word? Velocity. One is down here where it has minimum height but maximum velocity, and then the opposite on the other side. And it's one of these things where like you can, if you want to look into state spaces, you can take the height here and the velocity there. And a nice pendulum will trace a nice ellipse.

**[00:41:49]** Look up the Wikipedia page on Pendula and you'll see some really cool gifs of the state space diagrams of hanging pendulums. The most important and most relevant thing for the standing posture case, which is what we're here to talk about, is that a thing to note about this is that this is passively stable where it is, if I perturb it from its sort of happy zero point, the resulting acceleration will pull it back towards that happy stable point. And because there's damping energy gets lost in the system, it will sort of die down back to where it is. So if this is time, we're doing dynamical systems modeling because I put time on the axis. So congratulations, you now know how to do that.

**[00:42:43]** And then this is theta. If I deflect this thing down to whatever theta is, it will pull itself back towards theta equals zero. It'll pass through it because of the momentum and it'll go back and forth. If there's no friction or anything like that, it'll just do that forever. There is friction, it will come back to its happy stable point.

**[00:43:11]** Now all of these same dynamics work if you flip it upside down, except it's no longer friendly and passively stable. So this is where it becomes neuroscience. So now this is the floor. So we were doing a regular pendulum. We're now going to do inverted pendulum.

**[00:43:43]** This is another highly googleable term is inverted pendulum. Human movement, you'll get all sorts of stuff, particularly during locomotion. So now we have the same guy attached to a point on the floor. We still have L, we still have M. And oh, I forgot to mention, if you wanted to calculate the forces like the newtons and stuff like that, because this is a meter, you could calculate those things in units of. I guess you wouldn't know kilograms either, but you could get some weird wacky unit that was equivalent to that.

**[00:44:24]** So yeah, so that's what we'll call it center of mass.

**[00:44:33]** And we'll call this base of support. So remember with this type of thing I drew the vertical lines showing where. I don't know if this is actually going to show up anywhere, showing where the extent of the base of support is. With this guy, that region of controllability is an infinitesimal, a non existent thing because basically this deflection point here is theta equals zero. And whereas before with a hanging pendulum, if I perturb it from that point, the resulting acceleration will pull it back towards that point and it will sort of cycle through there.

**[00:45:26]** If you're up here, you're not quite so lucky.

**[00:45:32]** This is the place where if we.

**[00:45:43]** So this is called the vertical projection of the thing, which is basically just, you know, if this was X, Y and we call this Y, just say Y equals Y equals zero. And now this is X and that's the vertical projection.

**[00:46:04]** And so just like before, the thing that I deleted at some point in My life, I started calling erasing things on a board, deleting them, which is always fun.

**[00:46:20]** So kind of like before, you have gravity pulling down on this thing here, which means in this case, you have gravity pulling down here. You have sort of the structure of the stick pushing up. And if it's balanced here, happily, then these things cancel each other out perfectly and nothing bad will ever happen.

**[00:46:47]** Now, if there's a little bit of deflection from that point in the same way this thing, gravity is still pulling down, the stick is doing its best, but they're misaligned, so there's a resulting. Oh, sorry.

**[00:47:06]** Yeah, that's right.

**[00:47:09]** So the. There's some geometry stuff you can do here if you want, silver toa, whatever, trigonometry. But basically the amount that they are separated from each other means that the force of. Basically this one's not relevant. The stick is doing its best to keep you up, but now it is also pushing you away.

**[00:47:33]** And the gravity that's pulling also sort of leading to a push in. In a direction away from that happy stable point. So this. So with a tangling pendulum, a deflection leads to this nice sort of result, relaxing back to zero. This is a.

**[00:47:58]** Even a small deflection will push it away. So it is a passively unstable thing. And if it's. I guess. I guess this is the ground, so you hit the ground, or if you have.

**[00:48:11]** If you can go around, then it goes back around and the angle basically goes down to the bottom and it gets pulled to the other attractor point, which is the bottom. This is technically a stable point, but any infinitesimal shift will cause for accumulating error and it will get pushed away. This is not. There you go. And if you do the state space diagram, you have like, basically regions of this space.

**[00:48:47]** I'm not going to explain this, but you can look for the pictures and ask the bot about it. This is. What is it called? I think this is theta. This is theta dot.

**[00:48:58]** And for some of those.

---

### Chunk 6 [00:48:45 - 00:58:44]

**[00:48:45]** Basically regions of this space. I'm not going to explain this, but you can look for the picture and ask the bot about it. This is. What is it called? I think this is theta.

**[00:48:55]** This is theta dot. And for some of those. Some of the space there is periodic orbits. The other is not periodic orbits. Yeah, they're in our particular case, a non periodic orbit means that you fall over and hit the ground or you either have to like change your base of support or you have to hit the floor.

**[00:49:28]** Great. So much like science, standing is also impossible. It is a passively unstable system that can cannot be reconciled. Which is a shame actually. No, luckily we do have nervous systems.

**[00:49:43]** So this is passively stable. Congratulations. There it goes. And it's still an inverted pendulum. It's just that the center of mass is so close to the ground that I have to perturb it pretty far for it to get out of that sort of happy zone.

**[00:50:00]** And then it does fall over to the ground. In this case, the center of the base of support is still a point of X has an extent. But if I let go, it will slowly accelerate the acceleration. This is one of those like it's a compounding error. So it starts out, the acceleration is small, but then it gets.

**[00:50:25]** But then on the next time step it's a little bigger and the next time step is bigger. And so it slowly picks up speed until it falls over.

**[00:50:37]** And if that was the whole story, then that would be the whole story. But luckily for us, we have sort of non zero base of support and a whole nervous system attached to a bunch of weird electrical springs that we can use to sort of actively control it. So this one is like. I'm sure everyone's done this with broom. If you haven't, you should this.

**[00:51:00]** I am basically monitoring the error in the deflection from zero. And I'm using a combination of like the weight in my hand and also like looking at it. And then I am actively moving the base of support to keep. Basically if it's accelerating in this direction, I move the base of support so it accelerates in that direction. I'm trying to sort of make it be zero.

**[00:51:27]** I could make it kind of swing back and forth, but it's an active process that I'm doing that is allowing the thing to stay up even though it is passively unstable.

**[00:51:46]** And the best video I have about that is this one.

**[00:52:03]** Oh, this is the wrong. I don't have the overlay here, but she's standing on this ball. Aaron. This is basically like the wobble board stuff and put a link to the wrong part.

**[00:52:20]** I'll fix it later. But basically, because she's on her toe, her base, her anatomical base of support is very small, but she's on this ball that actually spreads out the center of pressure, or it sends out the base of support and allows her to move her center of pressure in order to counteract the movement. So it's one of them. Oh, my God, she's standing on that thing. That's so impressive.

**[00:52:49]** It is very impressive. But it's actually easier than standing on solid ground because it extends her ability to move the base of support. And if I had an overlay, you'd be like, wow.

**[00:53:13]** So obviously that's a lot. It will all be on the test. There's no test, and if there was, I wouldn't put that on there.

**[00:53:25]** But do look up the Wikipedia page about pendulae. It's surprisingly deep. Wikipedia is the greatest intellectual achievement of humankind up to the present moment. And anyone that says otherwise is taken.

**[00:53:43]** But yeah, so we're going to now look very briefly at like. So if you recall the last time when I was here doing the recordings, I.

**[00:54:00]** We had the two recordings of me balancing on my feet.

**[00:54:25]** Yeah. So the one hand I was. I was balancing. So I was standing on two feet and I leaned all the way forward and all the way back and all the way to the right. All the way to the left.

**[00:54:34]** And then standing on one foot and do that.

**[00:55:21]** Actually, I'm going to. I'll play this and we'll probably be able to tell which one is.

**[00:55:44]** So.

**[00:55:49]** So you can see. So the ball here of center of mass calculated in the ways that we do that. The sticks are the rigid body segments that we use to make approximations. And, you know, the mass of each one has been calculated the. According that table with the center based off the.

**[00:56:06]** I forgot there's a point on that table that shows, like, where the mass is relative to the proximal and distal joint. Proximal is close to the center, distal is far away from the center.

**[00:56:19]** And you can sort of see stuff happening there. I'm going to. I'll go back to this at a later date, but I do want to show some.

**[00:56:30]** So, yeah, so this is the blender stuff. And Aaron was kind enough to pull into the raw data and get started showing basically like, representations that are sort of better equipped to show the differences between those two conditions, because you can eyeball this and you can maybe kind of see it, but that's not really results and it's also, the effects are actually small to see with your eyes. And so I'm going to show you it's not. It doesn't actually show that distinction, but it just shows a quick presentation of the kinds of ways we can start analyzing this data to start looking at those distinctions. And people who want to know more about this can split off and learn about that.

**[00:57:20]** And then other people we could start talking about, like the neural systems, neural anatomical systems that go into that type of balance and support stuff.

**[00:57:33]** So, long story short, basically you just, if you're not a code person, just let it wash over you. Remember before I showed you that big old spreadsheet of numbers? So first thing you do is you install packages that you need. Numpy is for numerical processing in Python. Pandas is for processing big spreadsheets plotly, if you're making plots.

**[00:58:06]** So this is one of those. Like many, many people have worked on these things for many, many years. Numpy in particular has a, has a sort of place in the history of numerical computing that humans can do. So it is a venerable guy.

**[00:58:26]** And then you basically point it to the place at your computer where the data lives and you say, hey, load in that bodytrajectories CSV. CSV stands for comma separated values. So if you look into that text file, it would just be a bunch of numbers with a comma between them and then enter and then a bunch of comma between them.

---

### Chunk 7 [00:58:30 - 01:08:30]

**[00:58:30]** You say, hey, load in that BodyTrajectories CSV. CSV stands for comma separated values. So if you look into that text file, it would just be a bunch of numbers with a comma between them, and then enter and then a bunch of comma between them. And that's how spreadsheets live at their sort of most basic level. Kind of the same way that, like your Microsoft Word document is the same thing as a RAW text document.

**[00:58:56]** A CSV is the raw version of what happens in my Excel. So you take that and pull it in. It looks something like this, this formatted square. That's what Pandas does, that package that handles these things.

**[00:59:13]** And then you pull out the center of mass trajectories, print them out just to make sure that you're not going crazy. These are the names of the. The points that we're tracking.

**[00:59:26]** And then blah, blah, blah. It's important, but we don't need to worry about it. And then you can take basically each of those points, and it has a trajectory over time. So this is the X position of the nose on this axis in meters. And then this axis shows time, or in our case, time.

**[00:59:48]** Time is frame number. We could convert this to things like seconds by multiplying the frame number by the frame rate. But the shape would be the same, but the scale would be different. Kind of like if we calculated those Newtons with this, assuming that this was a meter, you would get a certain number until you realize that I lied to you. This is not a meter.

**[01:00:08]** It's like 1.2 meters. Just the point to make. That way those distinctions are arbitrary until you want to. That would be just fine for you until you tried to compare your nose to somebody else who actually used a ruler. But oftentimes units are just like scalars.

**[01:00:25]** They don't really affect the shape of the data. So this is the path that my nose took on the X axis of whatever thing you're looking at.

**[01:00:38]** Pull it out. Same thing, except this is now the xyz.

**[01:00:46]** See me jumping over here.

**[01:00:50]** And same thing for center of mass. Once again, you see little jumps, jumps, jumps. So basically, things like the nose are like raw, measured points. Things like the center of mass is calculated from all of those trajectories plus the anthropometry table. And then you do this is to basically shuffle stuff around so that you can make a visualization.

**[01:01:15]** This is just basically showing for each point, for every frame that we have, what is the XYZ position of all relevant dots.

**[01:01:28]** And then the purple dot Here is the center of mass noticing. So this is basically like what scientific data visualization often looks like. It's very raw and it's very like. It's just not really set up for this type of stuff. It's not even scaling properly here.

**[01:01:45]** This could be cleaned up and we'll do that going forward. But this is one of the huge advantages of using something like Blender. This is a visualization tool for professional visualizers and animators. It's the exact same data. It's just this is being presented in something designed for like aesthetic visual outputs.

**[01:02:03]** And this is something designed to plot two dimensional data. And they begrudgingly added a 3D viewer. But it's also good just to sort of show that you're not crazy because you can plot it and it's like, oh, yeah, that looks like a person. Great. Also, notice the dots are not connected because the connections between the dots is not a measured part of the data set.

**[01:02:24]** Like, we know that the shoulder connects to the elbow, but we measured the shoulder, we measured the elbow. So this is just a raw representation. If you wanted to draw the stick figures, you would need to have additional information saying how to connect the dots, which we're not doing at this juncture.

**[01:02:41]** Now you go through, you pull out.

**[01:02:45]** So we're looking for. We're going to look for the ground projection, right? We're comparing center of mass to base of support. So we don't care about. So before we were talking about jumping, we cared a lot about that Z height number.

**[01:02:58]** Now we're looking at a ground projection. We throw away that Z height number because in our world, at this right hand rule, X, Y, Z, Z is up. In some cases Y is up. No one ever says X is up, but in our world Z is up. So we throw that away.

**[01:03:17]** We just take center mass, X, center mass Y. Then we take the points that define the base of support. Left heel, right heel, left foot, right foot index, which is the toe. This particular tracker has a very impoverished foot that just has a heel and a toe. But we pull those out and that's enough to make a rectangle on the ground.

**[01:03:40]** Pull out the. Yeah, do some stuff. Visualization code. Shuffle, shuffle.

**[01:03:48]** And you get this, which is a nice. So this is an animation which I'll play in a second.

**[01:03:57]** So if you're ever color coding parts of the body, the right side is red always. Because it starts with an R, you'll see it. People will dip that wrong all the time. And I'm saying from a moral position they are wrong. If you're color coding the body, the right side is red, the left side is any other color that isn't green because red, green is bad for color line.

**[01:04:18]** So right foot, left foot, center of mass, basically top down view. And it will play as much as it can.

**[01:04:38]** So this is the control case.

**[01:04:43]** So you can see me leaning back and forth and on your own time, stand up and lean. See what that feels like. And specifically see that. Notice that you can notice when you're at the edge and notice that the heels have far less to do than the toes and that you have a sense of that relationship between your base of support and center of mass, even though you may not fully realize that. So now you can sort of see what's happening from the top down.

**[01:05:14]** And you can see now I'm shifting over. And even though this is a very impoverished view of very complex data, you still have a pretty good sense of what's going on. And you can also tell that this is the one where I'm not holding the weight because I think my computer can handle it, actually. And then you can also plot the whole thing and it sort of becomes this kind of schmear, which if you're thinking about things like dynamics, this is not a great way to look at it because you've now squished over time. But if you're worried about like, what space did I cover?

**[01:05:54]** How large am I even plot to be able to view it? This is a great way to show all the spaces that my foot has gotten to in this recording and just to see if it works. If it doesn't, it's not your fault. Although I think it will.

**[01:06:22]** Kettlebell. Okay, are those numbers in the missing. The coordinating. That's the time stamp. Oh, good call.

**[01:06:57]** See, this is why it's good to have an externalized nervous system.

**[01:07:10]** Okay.

**[01:07:23]** Okay. So this is a Pandas notebook, which I don't like in many ways, but they do the job I like. They're really good for like really simple stuff like this in educational context, but they don't scale in complexity at all. So it's like you people wind up getting especially like student, like objects tend to get stuck in Pandas notebooks for a long time in their trajectory.

**[01:07:47]** But. Oh, that's just one of recalculated it in my dark mode stuff.

**[01:07:59]** Okay, looking good so far.

**[01:08:19]** So this is the same. So this is now the data where I'm holding 20% of my body mass in my hand and I wasn't careful. Like I realized that Actually, the better way to represent this would be to.

---

### Chunk 8 [01:08:19 - 01:15:23]

**[01:08:19]** So this is the same. So this is now the data where I'm holding 20% of my body mass in my hand. And I wasn't careful. Like, I realized that actually the better way to represent this would be to like hold statically on one side and try to hold it out away from me because I was shifting it around a lot. So you might have to just kind of like gut check it.

**[01:08:42]** And it would also be nice if this was playing alongside the bigger visualization, which we can do. Andres actually wrote some code to make that easily doable. And. Yeah, so that's.

**[01:08:57]** Yeah. So there.

**[01:09:03]** Pause, pause, pause.

**[01:09:17]** So basically the fact. So here it's actually my center mass is still going to pull from my right foot, but when I shift over to my left.

**[01:09:37]** Come on here. Yeah. So you can, you know that my foot is moving and you can see the center of mass is just shifted a little bit on the outside. So this is one of those things where it's like to actually show this data more like to make that point that there is this distinction. This is kind of like it's like, oh, yeah, the effect is there.

**[01:10:00]** It could be measured. It could be done. Whatever. The behavior was not well set up to produce sort of good data. But we can go back and record new data.

**[01:10:07]** We could also basically just like give yourself a longer time standing there. We could take this representation and couple it to the bigger visualization so we can actually verify. And we could make the pause button work and then pause it and be like, oh, yeah, look, I'm standing here stable and supported, but my center of mass is outside of my base of support, because this center of mass is not the actual center of mass. Because we're not accounting for the fact that my hand. And now, instead of being 1% of my body mass, is now 21% of my body mass.

**[01:10:38]** We'd have to recalculate the center of mass of that in mind. And then theoretically, then it would shift back and start looking like the regular again. The control condition.

**[01:10:52]** Okay, you got all that? Good. Great. So, as per usual, I've also gone longer than I intended to. But that's okay.

**[01:11:04]** It's good stuff. So we have another 20 minutes, which I do think is enough time to sort of get started with some stuff.

**[01:11:15]** So just show of hands, like, who likes code and data? Who is interested in code and data? You don't have to be good at it. You don't have to ever done it before. You don't have to expect that you will be successful at it.

**[01:11:26]** But who is interested in at least seeing what it would look like. We can get you to the place where you can click the buttons and have the squiggle show up. Like who is interested in that versus who is less interested in that? Code people.

**[01:11:41]** Okay, cool. And a non code people. Great. The biggest problem would have been if everybody had said I want to do code. So this is great.

**[01:11:53]** Code people. I guess push back and then Aaron can you just try to get them as far as you can get towards this. Like mostly just like probably desktop VS code and then clone the repo. This is now in this notebook is now in the jupyter.

**[01:12:19]** Great.

**[01:12:22]** Other people we're going to. I want you to do the same kind of like group work thing again. Probably by next week I will be able to have some sort of more feedback loopy thing with the bot. But for right now we're still passively just pouring stuff into it and basically ask it the questions that came up for you when you were watching me talk about all this stuff. If you are interested in the mechanics of it, you can ask more about the robotics and control theory and systems and pendulum stuff.

**[01:12:56]** If you're more of a biologist, just think about the types of neural systems that would have to be in place for this to be able to work. You do not have a center of mass detector. That's not a thing that exists in your nervous system. You have a bunch of other modalities that give you other types of information and that has the sort of effective reality that we could. It's like functional equivalencies.

**[01:13:29]** Functionalism. I once had a professor say philosophy of mind is so hard it makes functionalism look interesting. Which I will not explain. I will just say and you can chew on that if you want.

**[01:13:41]** Yeah. So let's get started. We have like 15 minutes. So do these chats in the channel for this lecture and just pop something open ended this again. Whatever you found interesting, whatever you wanted to have more about, whatever sort of thing I said.

**[01:14:03]** And don't work alone. Work in clumps, clump up according to your local environment. And Aaron if you could go back and just get them started.

**[01:14:24]** Who's the coding crew? So code people go to the back and Aaron will go meet you. If you're not a code person and you're in the back, you might want to move forward.

**[01:14:38]** Do it. Do it. This may be your only chance to learn how code works. What's that? If you're interested in both, do code.

**[01:14:50]** So go code for now and you'll come back to this if you're interested in doing both. This is not a either or. You will be able to drop this opinion at your earliest convenience. And there is a benefit if you have a clump that is remain that has sort of that is congealing in some reliable way. There's a benefit to having at least one person from your clump getting some Code xp.

**[01:15:16]** But you're not going to be evaluated on your okay, I'm going to stop this record.

---
