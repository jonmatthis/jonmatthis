# Transcript: 2024-03-12-FreeMoCap PR Reviews - freemocapfreemocap#562, #552, #536

## Source Information

- **Source Type:** Local File
- **File Path:** `C:\Users\jonma\syncthing-folders\jon-alienware-pc-synology-nas-sync\videos\video_eater_downloads\playlists\[OLD] FreeMoCap Development\2024-03-12-FreeMoCap PR Reviews - freemocapfreemocap#562, #552, #536\2024-03-12-FreeMoCap PR Reviews - freemocapfreemocap#562, #552, #536.mp4`

---

**Total Duration:** 01:41:14

---

## Full Transcript

### Chunk 1 [00:00:01 - 00:10:00]

**[00:00:01]** Okay, let's do some PR reviews. Pull request reviews. Because we're going to do cameras too at some point. But right now let's just do this because it should be relatively quick. So starting in Freemo Cap.

**[00:00:16]** So first of all, we have there's like multiple PRs and multiple repos. And I don't know of one place I can go to to look to find those, which means that it's on me to just like, remember to go to like all of them, which doesn't seem right. I'm probably tagged or something.

**[00:00:41]** Oh, that's a different person, I guess. Ugh, I hate this though.

**[00:00:58]** So we'll figure that out. Pr. Maybe it's in the projects board anyways. Oh, that actually probably is the place to look, but we don't have it set it up like that. So actually.

**[00:01:10]** So that's probably what we should be doing.

**[00:01:17]** Nine.

**[00:01:22]** Control z.

**[00:01:28]** Get all prs.

**[00:01:45]** Oh, wrong, wrong, wrong. Must be 3. No, 2. 1. 1.

**[00:01:51]** Haha. And also don't be writing on the background layer.

**[00:02:02]** Right on that layer.

**[00:02:07]** Nice. So it's a 4K image. So if I'm at full size, this is going to be like roughly 1080p, which means I have the periphery for like expansion or whatever. This is my new approach. So the task I think I'm writing on here is going to be too big because now I'm zoomed in.

**[00:02:29]** That's too small. Sure. And let's.

**[00:02:48]** Perfect. All right, that's. Is that going to help here? Yeah. Why not?

**[00:02:52]** Because it should.

**[00:02:56]** I don't care.

**[00:03:02]** Get prs. Prs in one place. This is. That's Poly repo problems.

**[00:03:17]** Because if it was a mono repo, big honking big repo, this would not be a thing we have to deal with. So there's a couple of things we got to work on with our workflow because we have poly repo. And if you don't understand that, what a great set of googleable terms. Poly repo monorepo. I should probably look that up.

**[00:03:40]** Okay, so first one. So here we are. Start from the top. Free mocap. Actually, we could probably write this down too.

**[00:03:52]** Freemo Kip. Pull requests. There are three. They are all from fleep. Start from the top.

**[00:03:59]** The one. I guess this means not finished in the. Oh, okay. And then this is Pull request. Because it's like the first branch, then the other one's coming into it.

**[00:04:09]** It's like this is the main branch and it's like, can I. Could I. Huh? Pull request. Your. I am requesting that you pull from my branch I on this branch, I, Philip Queen on this branch am requesting to main that you pull from me.

**[00:04:25]** It's a fucked up. It's like opposite land language. There's a lot of. So much of the world, like, especially in science is opposite land language. It's like you can say it in either direction and it makes sense anyways.

**[00:04:39]** Okay, so we are trying to make the user the main freemocap data path settable stylistically. Like, I think we should start using like, if you're going to write a variable name, write the real variable name and put. If it's a variable name, put it in backticks.

**[00:05:04]** Okay. Figure out logging reference. So this is. This is when I turn the recorder on.

**[00:05:14]** So. Right. Jesus.

**[00:05:23]** Some things are beyond water. Okay, so right now logging configuration References the FreeMap data path, which I think this is called freemo cap base data or freemo. It's not freemocap data. Whatever that variable is, should be consistent within the code in here.

**[00:05:44]** This is called the init file. Similarly, just do. Just write the thing dunder init PY with the backticks because I think this is. It converts the underscores to markdown formatting. If you don't put it in backticks to reference the user path, we need to get.

**[00:06:01]** This is also just like I'm calling shit out. Not necessarily work for a human, but work for a robot for sure.

**[00:06:11]** To reference user path, we either need to get the GUI state information in the INIT function or move the logging configuration or only set the file handler once we get the GUI state, separating it from the rest of the logging effect. So definitely not the last one because like all the logging stuff needs to happen. Logging stuff. So you're like, oh, can we separate our concern? No.

**[00:06:32]** Okay. So arguably you could call that separation of concerns. But I think it's also a violation of coherence. Coherence? High coupling, low coherence.

**[00:06:45]** No, the opposite. It's like do all your logging shit at the same time.

**[00:06:55]** I think that the key there is that we should not be doing work in the INIT file. I believe that the.

**[00:07:09]** I remember Endurance. I talked to Endurance about this at some point back when we were first discovering. See, this is how it does the swoop. These is it does little things and if you turn it down small enough, you can see the individual pieces.

**[00:07:23]** And he said that he put the logging in the INIT file, the logging configuration in the INIT file to make sure that we always have the same logging configuration. Wherever we are cross processes and stuff like that. Like you don't have to set it intentionally because it's just. It's in the init. But I do think that we have run into a couple issues there.

**[00:07:49]** It's so like you could also just like look for the user data file when you call the like in the init file in the configure logging. If there's a relevant piece of information from the user, then we can do it there, Right? You can just look for the user user file and then say like oh, if it's not there, make it. But then you're like doing file system calls in the INIT file and that's like even worse. I think that this is kind of the way that I've been kind of moving towards setting things up is really thinking in terms of the entry points.

**[00:08:31]** So like INIT is going to get hit every time you want to like import something. That's not really going to be super helpful. Oh maybe, whatever.

**[00:08:59]** Trying to see if it's actually anyways maybe, maybe not. I don't know. Who cares? We'll figure out later. So the INIT file is going to get hit every time you import something.

**[00:09:11]** The main entry point is only going to get hit once. So I think that moving the configure logging stuff to here to the main file is the right move. However, if you do that, if we do that, then we also have to deal with the fact that we're no longer putting it in the INIT file. We should make that consistent across the sub repos and also deal with the fact that we down. We now may have.

**[00:09:46]** We now may have to be more intentional with our logging. We're also kind of like moving in that direction of being more intentional about it.

**[00:09:56]** Just like. Or more explicit I guess would be the term.

---

### Chunk 2 [00:09:46 - 00:19:44]

**[00:09:46]** We now may have to be more intentional with our logging, but we're also kind of like moving in that direction of being more intentional about it.

**[00:09:58]** More explicit I guess would be the term here.

**[00:10:03]** Because we were having issues with the multiprocessing stuff anyways. Possibly because of the same thing. Because it's hitting the configure logging thing more than once. Once and something was getting duplicated inside of it.

**[00:10:16]** So it's like yet another. It's like it's one of those things like this is a place. It's. There's not a quick answer here because there's multiple answers and they all have very different like cost landscapes. So.

**[00:10:29]** And then also deciding how and where to set the user path. Have user set path. Then you can put it on the welcome screen, which seems gross. You can have it sort of set.

**[00:10:43]** It could be set at the like. Well, so they're not going to find a good place to put it in the GUI as it stands because the GUI as it stands is already packed and broken. So we really need to be moving towards like a pop up like settings screen that just sort of like houses all the main settings. That would also play into the whole switching to like having user state, which traditionally I've seen that as like app state.

**[00:11:14]** And it's something that you can, it's like you can use like a singleton pattern for that which I think is considered to be. That's like its global state. So that's also not, you know, we don't love that, but we don't mind it. We, you know, we use it when we have to.

**[00:11:33]** And this also can. Like having having an app state that's like a big dictionary of all the user data is related to this conversation on like using the init file for stuff and using the main file for stuff. Because you know, if we are going to be setting singletons and sort of like things that should be kept like global state. If we have something that we're setting that affects the behavior of the individual pieces of code within the software, we need to be careful about that because this is now a way that something that you could write code that could break for unexpected reasons because you're now changing the context, the global context where it's operating in.

**[00:12:26]** So we're now talking about like again we got to become more specific about how we reference these things by name. But I think GUI state is the thing that maps onto the concept of app state. And I think that app state is the way that people in the field of software development Talk about these things. And I think that app state is basically a big old honkin. It's not a dictionary because it's almost always in like web dev language, which is JavaScript, TypeScript shit.

**[00:13:03]** But it's like a hierarchical data format that's just like a bunch of parameters. It's a parameter tree. We call it in FreeMap Labs Geek, we've called that a parameter tree. It's also dictionary. In Python land it would be a dictionary or a pydantic model or a fucking data class.

**[00:13:22]** Jesus. It's so complicated. Anyways, so yeah, like. So.

**[00:13:33]** I have gotten wrapped up in a ball. Where are we?

**[00:13:42]** Yeah, and so this will the concept. There's like. So we're also. We're moving towards being much more careful about our front end and our back end should put this here because I'm no longer tied to the fucking text here anyways, Pen properties.

**[00:14:20]** I feel like I'm fucking up right now.

**[00:14:26]** We'll find out. Okay, I am, because I got to move this back again and it's not gonna follow the window. It's fine. So yeah, moving to front end and back end. Front end would be, you know, the GUI currently qt, but soon to be some sort of web app.

**[00:14:46]** And then the back end is all the currently all Python, soon to be Fast API, which is also Python. There's just gonna be. We're gonna put it behind like a proper server.

**[00:15:04]** And so this, the app state, which includes things like where is that, right? Like where the user will set the data path and stuff like that is going to come from the gui, no matter what the ui, the view, the whatever. And so this app state, if it's going to keep track of all these settings and stuff like that, is going to want to live in the front end and it doesn't. We won't go into the back end, which will be an easy thing to control once we switch to the architecture that is previewed in the skellycam fastapi branch, which is much more careful about this maintenance of front end, back end processes and you know, starting from the main entry point and trying to move away from everything being the init file.

**[00:15:58]** Jesus.

**[00:16:01]** And you wonder why people are confused. Jesus. Okay, where the hell were we? Anyways, we're at the top of the first PR 16 minutes in. Okay.

**[00:16:19]** Oh yeah. So again, this is where so like having the female cap data variable be global. It's currently global. This is like I don't know what that variable is right now. So I don't think there's a variable called freemo cap data.

**[00:16:33]** There definitely isn't. There is in the blender code. But whatever this is, if I think this, I think it's called freemocap Base Data Folder path. There's like that big stupid folder full of paths and stuff. Anyways, so these are my thoughts.

**[00:16:52]** Oof. There's 17 files changed.

**[00:16:57]** Oh, formatting.

**[00:17:03]** So this is our GUI state, which is kind of like app state.

**[00:17:09]** And so the problem with passing it down is it just adds all these little tendrils through it. And I think that's how I've gotten fucked up before. I was like in one of the earlier iterations, Endurance made a variable called app state in Screaming Snake case and I did stuff like this and it wound up being a problem and I can't remember. Like I think I and I over corrected and now we're trying to recorrect and I need to think about it more. Yeah, see, look.

**[00:17:42]** Look at all this place. Like it's 17 files. It's being like, like tendrilled down everywhere. So it's just like this is where I think having it be like it's just set it as a singleton and then have whoever needs to import it like it's fine and we'll just be mindful about who gets to create it, I guess. Well, we'll do it from the top level main.

**[00:18:10]** We'll do it from the entry point, top level main guy there. And then, and then we won't ever have to do inter process communication with it because it will never. It will never hop the front end back headline will just live fully in front end land.

**[00:18:38]** Okay. Remembering as I'm recording this that I've been doing these recordings. It's verbal protocol analysis. Verbal protocol analysis. It is stream of consciousness.

**[00:18:48]** Dump the data into a recorded form. It is not in communication. Sorry, we can clean it up later with the robot, but right now it's like I don't have. I don't have the spare levels of abstraction between working and communicating.

**[00:19:11]** I think this is what he, Philip is referencing when he says primo cap data variable or whatever he says.

**[00:19:27]** Or maybe I will ask the viewer to be mindful of which pronouns I'm using. You track my headspace for fuck's sake.

**[00:19:36]** Okay, fix links to doc. This is probably easy because. Yeah, easy peasy.

---

### Chunk 3 [00:19:30 - 00:29:28]

**[00:19:30]** Of which pronouns I'm using. You track my headspace for sake.

**[00:19:36]** Okay. Fix links to doc. This is probably easy because. Yeah, yeah, easy peasy.

**[00:19:49]** Is it that?

**[00:19:58]** Okay. I would have thought it would redirect, but maybe it's weird. There is a weird redirect.

**[00:20:14]** Which I don't understand. Oh ho. Hey, hey.

**[00:20:23]** Why is monitor two on the right? Monitor three is in the middle, Monitor one's on the left.

**[00:20:30]** I think it has to do with the order that they're plugged in on the back of the thing, but I don't want to dig. No, these are daisy chained anyways. Did you know you can daisy chain display ports? It's like the point. Okay, where are we?

**[00:20:44]** We are looking at PRs. We're 20 minutes in. Great. This one should be easy.

**[00:20:54]** Who are you? That seems right. Yeah. So one of the. I'm starting to view it as a nice thing about.

**[00:21:02]** But it is. It does require a change of thinking. I think one of the nice things about Writer side as a documentation thing is it puts all the markdown in one folder called Top Topics and then you use an XML file to arrange them into a nice format. So that means that I think you can still rearrange them in folders inside of the topics thing. I just haven't really played with that.

**[00:21:27]** But it does make the URLs kind of simpler, provided that the names of the individual files are like named nicely. Like, it is a kind of violation of like one of the Python principles of assume context. I think it's like from. That's one of the things from like the Zen of Python, which is. It's an Easter egg.

**[00:21:54]** You can get it somewhere, but it's like it in.

**[00:22:14]** Okay, I don't know, maybe I made that up.

**[00:22:20]** But it does. So like we. You just have to make sure that the names are meaningful. I've also kind of fallen out of love of Snake case. Even though that is a pep8 thing.

**[00:22:30]** I just think it looks. It just looks ugly. And I think that that like hyphen kind of kebab case I think looks nicer for human readable stuff. So anything in Python I will keep the convention of Snake case whatnot. But when I've left.

**[00:22:44]** When I leave Python, I think if it's like. If it's intended to be read by human eyes and it's like, yeah, I just. I don't know. Web dev land is wild because there's like other naming bunches. Like yeah, some kind of.

**[00:22:59]** But like just whatever works for you, man. Like Just don't put a colon in a file name. Don't put a colon in the file name. Don't put white space in a file name. Other than that, man, just go to town.

**[00:23:09]** It's like, okay, whatever you want. So, like, multiple dots. What? I get no slashes, too, obviously. Okay.

**[00:23:23]** Are you good? I think you're good. Files change, too. Yeah. Yeah.

**[00:23:28]** I should check that.

**[00:23:31]** Should check that. Not that you would make that mistake. Yeah, that's probably the kind of thing. Oh, wait. Do we have references to.

**[00:23:47]** Do we have. Where. Where do we put references to these ones? Is it in the welcome screen? Who added those?

**[00:23:55]** Did I add those?

**[00:24:01]** Someone else added them. I like that.

**[00:24:12]** This is just gonna be a PRS video. We're not getting any cameras right now.

**[00:24:19]** Especially because, like, when I tried to turn on skellycam with this running, it hit a mistake. I thought that had been fixed, which was that it sees all. There's seven cameras on my computer right now, and it sees all seven and tries to connect to all seven, even though these three are blocked. I thought I'd fix that. It's probably just some stupid thing, but I don't really want to.

**[00:24:46]** I want to, like, draw the diagram. That's what I'm really itching to do.

**[00:24:54]** But we'll get there. I was looking for. I was trying to figure out who did. Oh, this.

**[00:25:14]** Do this.

**[00:25:17]** And then check out the branch. Little thing there. Yeah.

**[00:25:25]** In. All right, now we look at.

**[00:25:31]** It's just one commit, right? Yeah. Aha. And hit F4. Boom.

**[00:25:41]** Oh, wait. But I want to check this same place on main.

**[00:25:54]** I'm now just kind of like, this is me just playing with a tool.

**[00:25:59]** Welcome Screen Dialogue Shift. Wait. Welcome Screen dialogue. Thank you. And.

**[00:26:16]** Yeah, Philip added it. Why did you add that?

**[00:26:26]** What does it look like? Forgot. Have I forgotten the face of my father?

**[00:26:41]** That should import. Oh, that was probably. This is the last loaded.

**[00:26:50]** So much work. And yeah, you see Discord.

**[00:26:57]** This is a Discord problem. Not. There's a known thing where. If you are in a voice channel in Discord and you start free mocap, you will get. Your audio will get cut invisibly.

**[00:27:09]** And the way to get back is to just click the thing again. And for a long time I assumed it was us. It's not us. It's Discord is stupid. There is something in the MediaPipe OpenCV import that's happening in the code that.

**[00:27:23]** That temporarily, like, temporarily hiccups your audio stream. And you can hear it in Spotify. Like, if you're like presumably any other audio when I'm running Spotify. I don't know about other audio formats or streams. I'll hear like a little pause in the music when at a certain point of the Freemo cap setup.

**[00:27:45]** And it is Discord who sucks at reconnecting to the to the device when there's a hiccup because obs can do it. It's not us. It's a combination. The fault of this matter is a combination of either media pipe or OpenCV and Discord. Not me.

**[00:28:13]** Could have sworn it was me.

**[00:28:18]** Okay, what are we looking for here? We are looking for.

**[00:28:31]** Where is it? Where did like.

**[00:28:40]** No. How do I get to that guy?

**[00:28:48]** Does this work even? No one. To my knowledge, no one has ever filled this out. Also, I don't know if anyone's ever given money through this route. I don't know.

**[00:28:59]** We don't have a way to know if it come in. And there's the number of people who have donated is like less, possibly more than this many. I don't think more than this many.

**[00:29:14]** And the total volume of cash flow from donations is not far off.

**[00:29:23]** Just me and a couple friends could handle it on a warm day.

---

### Chunk 4 [00:29:15 - 00:39:15]

**[00:29:15]** Total volume of cash flow from donations is, is not far off.

**[00:29:23]** It's just me and a couple friends could handle it on a warm day.

**[00:29:30]** I also know I haven't checked this in long ass time either. Okay. I don't know where to get. I don't see anything that would tell me how to get.

**[00:29:43]** Is it a hover text? Wait, we don't see hover text for some reason. Is it a tooltip? I don't know. Anyways, point is, I don't know what the point is.

**[00:29:56]** Like there's, there's nothing multi camera, there's nothing that would show this. Where, where, who, where are we?

**[00:30:05]** In the welcome screen?

**[00:30:14]** Is there a frame shadow? Oh yeah, it is a little bit. Is it?

**[00:30:20]** We gotta burn this thing to the ground. You, you gotta go. Thank you for your service. It's time to go away. Get into the ground.

**[00:30:38]** It's just wrong tool for the job. We have better, better tools for making nice UIs. And they ain't buy side six, they ain't Python, they ain't Qt. It's this, it's the one we've put infinity billion trillion dollars into. It's the one that's been used by billions upon like how many humans, how many humans have used and touched this thing versus whatever the shit PI side six is.

**[00:31:10]** It's just like optimization by exhaustion. That's not true in any way, shape or form. But it's just like everything I said pretty much doesn't hold up the scrutiny. But still I'm sick of, sick of, sick of trying to write UIs in Python.

**[00:31:29]** Okay, okay. So you're good at my review. I guess I can say I don't know where those, I don't know where to get to those.

**[00:31:48]** I don't know where to see this in the gui.

**[00:31:56]** See these links single multi camera.

**[00:32:13]** I looked for them at roughly See what I'm doing here?

**[00:32:23]** 02520 I don't know how long I've been looking for these things. I don't know how long I've been 32 in the video. The associated PR video.

**[00:32:49]** Now I put a link to it here, except I'm not going to because there is no link. Can I preload a YouTube video? I don't want to do that right now. I'll just be mysterious.

**[00:33:09]** Oh, is that, is that, what does it mean that it is resolved? Is it in, Is it here?

**[00:33:30]** Can I unresolve it?

**[00:33:36]** Jesus. Fuck. Oh, unresolved. But then does that block the pr?

**[00:33:48]** I think that's A setting. Actually, I think it's a setting. I think that you can tell it whether or not all conversations need to be resolved.

**[00:34:03]** Running out of. I got steam. Okay. And then rule is that the person you. I approve it.

**[00:34:13]** Philip merges it for internal PRs. That's how we do. So that way if he has the opportunity to be like, oh, wait, I guess he could be. Oh, wait. About the fact that I don't know.

**[00:34:26]** Oh, yeah, they're there. How to get to these things. But like, where would it.

**[00:34:35]** I looked, right? I looked.

**[00:34:45]** Okay, so we're in the layout. We said, here's the layout and it's a V box, so it's going to get stuffed.

**[00:34:58]** If that makes sense.

**[00:35:02]** Okay.

**[00:35:05]** So first thing we do is we.

**[00:35:14]** Where's welcome Screen? Dialogue. Dialogue. It's the pop up. It's the first time.

**[00:35:22]** Pop up. Wrong name. Because this thing is. This is called welcome Screen. I see.

**[00:35:30]** I see. This is why. This is why Philip wrote all of this. Because he made this whole thing. Gotcha.

**[00:35:35]** Okay. Figured it out. Okay. We should just call this like first time pop up or something like that. Can I do that?

**[00:35:47]** I can. Can I do that in?

**[00:35:56]** Kind of want to add that as like a secondary pop up thing. Like maybe these are all links. So I don't want to want to add like a non link.

**[00:36:10]** Okay. I guess it's just fine. We should. It's mostly that we should change the name from welcome screen dialog to some other thing.

**[00:36:23]** Wait, blah. How do you type? Figured it out.

**[00:36:30]** I was confused because the welcome screen dialog, the physician, heal thyself stuff shares a name with naming, naming, Head conflicts. I'll call that Head conflicts with the welcome widget. What's it called? God damn it. This is why people don't do it.

**[00:37:13]** Because it's more hard. It's like work. And I have enforced kind of like a sloppiness around language, so. Because that's what I do. I learned from watching you.

**[00:37:25]** But it's just. It's getting bigger and the slop. We can't handle the slop. I can't handle the slop. Where in the fuck does that guy live?

**[00:37:33]** Is it a widget? Oh, it's called the home widget. It's. I am wrong. It's called home.

**[00:37:41]** It says welcome. Ugh.

**[00:37:55]** So it doesn't conflict with the name. It conflicts with the words on the tab.

**[00:38:01]** Christ in space. I don't know. I don't know.

**[00:38:12]** I'm just gonna write it all out.

**[00:38:24]** Can I do Dizzy Guys what's the name for the Dizzy eyes guy? There we go. No, that's the wrong one. Who's the squirrely eyes guy?

**[00:38:38]** Fuck me running.

**[00:38:44]** Who are you? Face with Spiral eyes. Sure. I mean, I can do spiral. Hello.

**[00:38:55]** This is where I'm at. This is how we do.

**[00:39:03]** Home. Home widget.

**[00:39:12]** Home widget. Py. I think that's.

---

### Chunk 5 [00:39:03 - 00:48:59]

**[00:39:03]** Home. Home widget.

**[00:39:12]** Home widget. Py. I think that's sufficient.

**[00:39:21]** Too much headspace. I think the spiralized man says it off. This is the purpose of Emojis is it's an emotional punctuation. It's tagging an otherwise out of context text blob with a, with a headspace. It's like, by the way, this is where I'm at.

**[00:39:41]** And if anyone says otherwise, ask them what it's like to have a pension.

**[00:39:54]** Okay. Okay.

**[00:39:59]** And yeah. Good done task. Muppet Arms succeed physically.

**[00:40:11]** The other one, the other one wasn't. It wasn't ready. It was just blathering. Oh, it's the check mark that was like, oh, green check mark. But that's the tests.

**[00:40:23]** This and this is a bigger guy. This guy wants to merge. It is a pull. No, it's a pull request. But it does not have the ready tab or whatever the other does.

**[00:40:38]** This one because there's a ready for review. Because I think right now we're kind of. We're dealing with the fact that it's just two of us, you know. Well, it's three. The summer routine two and five.

**[00:40:53]** Working on this because other people are on the team, but really it's only Philip who's doing active PRs into this code base.

**[00:41:06]** Yeah. So we're kind of like, we're, we're allowed for, we're allowing for a bit of slope and the way that we handle that stuff because we know that we're going to be able to talk about it.

**[00:41:17]** But then we do get to these cases where like I have very limited headspace to look into it. And, and it's like, oh wait, now this tag that would have been helpful isn't there. And I think a lot of these things are just kind of like this. Yeah, this is kind of where we're at. Like we're at the sort of like, you know, the crossover point of like, you know how much slop hurts.

**[00:41:48]** Like, like the cost of, of doing stuff more carefully with more tags and more blah blah, blahs versus like how much it hurts when you don't do that. It's like there's some crossover points that are happening and the solution is we just need a bigger team. Like or at least more full time stuff or I think like a couple like a layer of the hierarchy.

**[00:42:20]** More coverage I guess of. Because.

**[00:42:29]** I'm not yet to the point where I can not approve PRs into main free mocap.

**[00:42:36]** Not because I necessarily think that something's not gonna work, but just because there's, there's a lot more like long range tendrils that I feel like I need to manage right now because I think that we are in a, a guttering state of like that's the kind of the. That's the engine is like, it's like, all right, like is this gonna regret. We're going good, but like we're pushing it beyond. We're in, we're in the orange red zone of how much this particular state of the software can handle. So.

**[00:43:17]** Deary me.

**[00:43:23]** One. Yeah, let me. Yeah.

**[00:43:31]** 1, 2, 3. Ah, there we go. I knew there should be more lines.

**[00:43:45]** Okay, you are connected to 1, 2, 3, 3, 4, 5. 1. There we go. This is why we like trees. Because you get a lot of coverage for relatively fewer editions of entities.

**[00:44:12]** Relatively few additions to the ontology gets you a lot of additional connections. This is all like. That's a kind of a fundamental thing I think of why. Because there's a certain level where like adding things to the ontology is the cost.

**[00:44:35]** Okay. Leave it there. Mystery. We're talking to another person again. That's that we've shifted into that headspace.

**[00:44:43]** Interesting. Piaz. Anyone else? Okay, so now this is the one that's a little more. Bigger.

**[00:44:53]** I can't remember. Okay. And this is how we're handling the Poly Repo thing currently. I don't know if we can because like it would be nice if we could do this more directly. Directly in like by using GitHub's like linking methods.

**[00:45:16]** I don't think we can see outside. This is.

**[00:45:29]** Despite all the stuff I'm saying here, I still think that the Poly Repo is, is the right approach. See, there's a lot ton of conflicts.

**[00:45:40]** It's just that like, because in the code I think it helps a lot. It helps tremendously and in a lot of other places it helps tremendously, but it does just make this part of the job in like the wrangling, it's just more wrangling. So we just got to improve our wrangling methods. Okay. I don't think this one is.

**[00:46:00]** I don't think that this one is like ready to go. I think we're still in a testing phase with it and so this might, this might be the place to put the charuko, like treat the Churugo board like a skeleton thing.

**[00:46:15]** Okay. Currently we define a lot of media pipe specific variables that are passed around. Free mocap. Yeah.

**[00:46:26]** Skelly tracker. We'll see about that.

**[00:46:31]** It is a track because it's like I understand the tracking stuff, the stacking stuff for sure but the skelly forge stuff like the connections and things like. Because like there's a full pipeline component of this type of stuff so the question of where it lives is kind of. It's kind of whatever like I don't know like and whether it's going to be in like one piece or two pieces or one piece in like you know one piece with two in a house does not matter Then all references can be can instead pull generalized variables from the parameter model. Okay yeah so. So from can pull parameter model.

**[00:47:25]** We'll see it in the code that are the data loader class which okay yeah so that sort of semi vestigial data saver stuff.

**[00:47:38]** This is a won't fix I think just why.

**[00:47:50]** This I think it's a won't fix that's a no and the data saver too I think is probably going to go away there I think in that thing I was learning about some modeling like pedantic model stuff and was I using the machine at that point? Hard to remember but I think most of those lessons learned are present in a much cleaner state in the FreeMap data handler no, the FreeMap data model I don't remember what it's called specifically but the data model that holds the FreeMap data in the FreeMostat blender add on sub repo which Aaron has pulled into some other small like a. Forget what he called it he called it like pre blender which is like not how like I understood it's not that that's like the name is wrong, the headspace is wrong there it's.

---

### Chunk 6 [00:48:45 - 00:58:43]

**[00:48:45]** Like a. Forget what he called it. He called it like pre Blender which is like not how like I understood. It's not that that's like the name is wrong. The headspace is wrong there.

**[00:48:58]** It's. I think that is the anatomic like that is the data aware manipulation which is reference. I talk about the data aware stuff in like the Pipeline 1 video. Oh that's interesting. I know the videos so I can tell you where to go.

**[00:49:17]** It's just another thing of like this. It's another task that I was waiting for the AI to do for me that I realized that I can do because I actually also have a brain. It's like how am I going to automate that? It's like you could just do it. It's like wow.

**[00:49:32]** Shockingly powerful move.

**[00:49:37]** Yeah. So I think that both of the. These are both not fixed thankfully.

**[00:49:45]** Also you update the various sub repos which. Using the. Yeah. So this is another poly repo thing. The goal is to have these passed into the sub repos which will prevent a lot of.

**[00:49:55]** Yes. And so this is kind of the main issue there for me with the. With the where does it live type of thing because it's like in my mind I kind of want like.

**[00:50:15]** This. I just need to make this follow the Krita thing. But I don't. There wasn't an obvious way to do that anyways. You can see this well enough.

**[00:50:24]** I kind of want this the top level to be free mocap like I come before. It's like a one way type of thing. And then these are the sub repos like all the sub skellies.

**[00:50:49]** So the idea of Skelly tracker holding that def. The definition stuff would mean that either. Well I guess it could get imported into main free mocap and then passed down from frame free mocap to the other guys. Because like you're saying it's going to have to get pushed down to the other. The other folks which I don't.

**[00:51:17]** I don't hate that.

**[00:51:24]** I think there's also kind of a question of like in the next phase of life what is gonna. What does the main free mocap like? What is the main free mocap repo? Once all the functionality has been pulled to the sub repos and the answer is it's like it's mothership. Like it's.

**[00:51:44]** It's the one from whence all like that's the top of the tree. Top or bottom of the tree. Root of the tree.

**[00:51:58]** But there's sort of like there's almost wants to be like some separate place that sort of holds stuff that kind of is like a middle zone. Like stuff that the. I guess you can. It's like a question of responsibility. Ugh.

**[00:52:13]** Because I do think that like we are going to do things with the MediaPipe data to build the skeleton.

**[00:52:24]** So there's a part of me that wants to. That's resisting putting that stuff in the Skeletracker repo because it's like a keep them anemic thing. Like don't tell functions about stuff that they don't need to know about. Because then if we're working in skellyforge or the blender stuff and we're like, oh wait, this connection needs to be this other way. Let's go back to Skelly Tracker who has nothing to do with this and change things over there.

**[00:52:56]** Like that feels wrong.

**[00:52:59]** So then you can say, oh, we'll just keep that. Keep like the tracking part in Skelly Tracker and then move the connections part to Skelly Forward. But then it's like, wait, now we've taken one thing and split it up into two and spread it across the sub reposition. And so all of these things. It's an optimization algorithm basically.

**[00:53:15]** And like all these things are violations of various levels of like severity and flagrancy of a bunch of just soft rules that don't.

**[00:53:28]** It's truly just like which of these will scale better? Like which of these will be easier to work with once we have a bunch of stuff once things expand.

**[00:53:40]** And the answer is like just kind of. You just got to make a gut check and go with it. And then just like it's. It's a lot of kind of like learning from experience and then also just like reading the, the books and like they. People have worked these things out, patterns and stuff like that.

**[00:54:01]** And also like just look at what the big big ones do and find alignment there. Okay, so this. And so I think all. I think. I think most of the work here was done in Skelly tracker.

**[00:54:17]** Oh, 54 probably. Oh my God, that's big. Okay. It was probably just versioning and stuff. Okay.

**[00:54:28]** I would really like to drop like right now because we're not really set up to be used in other people's code. Like we really don't need to support anything else. But I don't know what other people are doing with this stuff. Who knows?

**[00:54:48]** Okay. Yeah, it's a variable name. That's why there's so many things touched. Warning String. Logger.

**[00:54:58]** Logger. We need. Yeah. Thanks for that. But we also want type hints everywhere.

**[00:55:07]** Yeah, this is the kind of like P3Ds. Like just name it the full thing. Just write the whole goddamn thing out. Please, please, can we. Can we just.

**[00:55:20]** Could we just.

**[00:55:23]** This is not. We are not writing straight C code. We are not like whatever. Which was the. There was one.

**[00:55:31]** There was one level. There was an era where variable names are limited to four characters. And so you still see a lot of stuff where things are smooshed into four characters. And I think just like this was. This is Lily code, Karashka code.

**[00:55:49]** They are far too young to have that. Like, they've just. They've picked that up from culture. There's like a four. There's like, it's like, oh yeah, it's hacker.

**[00:55:59]** Like, it's all these like small smush little things.

**[00:56:06]** Seen them just. There's kind of. It's a. It's like an aesthetic of like the really like. Which is like, to be fair, like the aesthetic helps because it makes it less characters.

**[00:56:17]** Which, that's another little trade off. And once you know, then you know. So now we're writing too many characters when we could be writing less. But I think I just, I just come like, what? Like, no, this is not better for any human brain.

**[00:56:34]** You, you have like, I would not believe, I don't believe you that way if you were to tell me that this is better than this. I just don't believe you. And definitely not. If you're thinking universal design students and like, like thinking in the perspective of like, someone who might be looking into this for the first time because they were digging through it and it's above their head. How can we be kind to that person?

**[00:56:56]** How can we invite them in? And the answer is make sure that it is self explanatory at any scale.

**[00:57:07]** Not feasible in its entirety, but you can make an effort for it. I believe that this is numpy formatted docstrings. I think I prefer the Google formatted docstrings, but I don't remember exactly.

**[00:57:28]** Basically because the Google one is more like just writing. It doesn't have like, anytime I see something like this, I'm like, eh. Although it does allow you to be more explicit. So we should just pick one.

**[00:57:46]** This is another like number of tracked points. Body is like, that's where I start going. Like, I start like, well do. That's actually getting too long. Can I shorten that down to numb?

**[00:57:59]** Is that explorer? Is that explicit enough for this hypothetical babymind? I don't know.

**[00:58:07]** This is all new. Capture volume calibration by camera.

**[00:58:16]** Ugh. What the shit? Is this in the right place? I think there might be more work in here than should be by camera reprojection filtering. Did we do that?

**[00:58:27]** I don't remember writing this. This looks like. This feels like. This feels newer. We don't want to reproject.

**[00:58:36]** This is Philip's code. This is his reprojection stuff. Why is it in capture volume calibration?

---

### Chunk 7 [00:58:30 - 01:08:30]

**[00:58:30]** Like this feels newer. We don't want to reproject. This is Phillips code. This is his reprojection stuff.

**[00:58:41]** Why is it in capture volume calibration? Is. Is it. It's new. It says it's new.

**[00:58:47]** Was it moved? I don't know. Whatever is. It's not. Media pipe.

**[00:58:51]** Generalized media pipe. Whatever. So I'll check by later. I'll. I'll look into this later.

**[00:58:56]** Who cares right now? I'll just, I'll just skate on through. Oh my God, this is a long pr.

**[00:59:04]** Where are we at time wise? We're at an hour.

**[00:59:08]** It looks nice.

**[00:59:15]** Okay, so he's adopting, right? Because so, and this is one of the reasons why I don't love Python and why I prefer classes in Python because it's like. So he's doing more functional code right here. See, now I'm talking to a. Now talking about Philip to another hypothetical person.

**[00:59:38]** And so he's using. And so basically it's all within this file. There's these functions, and he's using the naming convention of the leading underscore to signify that they are private. However, Python does not allow you to make these private functions. You can import them from anywhere, which means that now the global namespace is cluttered up with a bunch of references to little functions that you're not supposed to use, but there's nothing to stop you from using it.

**[01:00:05]** In JavaScript Land, TypeScript Land, you explicitly set. You say you would write export, Def, blah blah blah. You explicitly say which. Within a given file you can explicitly define which components, functions, whatever can be imported from other places by calling, you have to set it as export to allow it to be imported elsewhere. So you can have a bunch one file, you can have more one file systems that have many, many little sub, little teensy little bits in them.

**[01:00:39]** You. And you don't clutter up the global namespace because they are not exportable from elsewhere. In Python, if you have a big class, then these become methods of that class, and you still have to use the soft naming convention of a leading underscore to signify that you're not supposed to use it. IDEs like Pycharm respect that, and in the debugger it won't show them to you. I don't know if VS code does that, but in pycharm if it has a leading underscore, it's explicitly treated as a protected variable.

**[01:01:16]** But that's pycharm being nice. And that's like. That's what you get from the first two characters Being py, I don't know if VS code does that. I don't think it does.

**[01:01:31]** Blah, blah, blah. So this is kind of like, this is my argument against functional code, like my argument for object based programming in Python, because I don't. Because Python is so namespacey that you don't want to clutter up the global namespace because your soft convention of leading underscore is not enforceable. The other option is, do they have to be private? Like could you just drop the leading underscore and say, hey, now you can do this from anywhere.

**[01:02:07]** And if you find yourself importing it, well then that's how you get circular imports.

**[01:02:13]** Because everything is going to get hit in here when you import that thing. So now you have to be really careful about like, ugh, like think about life cycle Python. I'm becoming much more. I'm falling out of love with Python and falling in love with Typescript.

**[01:02:31]** Even though it's like, it's weird and goopy and fucky, it does feel a lot more explicit. And I think that the. You can kind of just tell by like, what's people using, what are people using? Like Python is good for data analysis. I don't know if it's good for software building.

**[01:02:50]** Like, it's just, it's too squishy. Like, like, I don't know. I don't know. I don't know. What are we doing here?

**[01:02:59]** We've got this plot stuff. Why is this in here? Was it just moved? Why is it in capture volume calibration?

**[01:03:09]** What's it doing in here?

**[01:03:13]** I don't know.

**[01:03:18]** All right, bye.

**[01:03:28]** Save Media pipe 3D data. Oof. Is this. God, there's a lot of work happening here. There's a lot of path work happening here.

**[01:03:40]** This is ugh. It's ugh. Oof. Yeah. See all this whole thing, this entire file and these 65 lines of text could be handled because this is the only work that's the only work that's actually happening here.

**[01:04:01]** If it's a numpy file, saving it to disk is just save NP save, no question. And all of this work is trying to figure out where to save it.

**[01:04:14]** And so this just happened. Like slurp, wherever this is being called from apparently needs to know where it's being saved. So whoever asked it to be saved or produced it should know where it's being saved and just like handle all this stuff elsewhere above this. I don't know, like, it sort of depends on the details, but like. Yeah, and this is this is way too specific.

**[01:04:45]** Save MediaPipe 3D data to NumPy array. That's not. We don't need a function for that because it does. That's. That's like the whole point of, of like, like it doesn't matter what the data is.

**[01:04:58]** It's an umpire array. And so to save it to disk, NP save. And so. And then in questions of like, responsibility and who like anemic code stuff, we have now learned that whoever is calling this needs to know where to save it. And so whoever owns that function, that information needs to get there at some point because we don't want to be calculating it at this point because it's clumpy.

**[01:05:31]** And then boom. Like, that's a good. Like, we love a good net negative pr. We cannot get enough. Like if, like, we're like, that's like.

**[01:05:45]** If we can have a leaderboard of net negative PRs, the person who like removes code is way better than the person who adds code.

**[01:05:58]** Deary me. Okay. Import shit, blah blah, blah. Oh, you're here, you're using it.

**[01:06:09]** So we are deleting a lot of stuff. So this might be this threshold by confidence.

**[01:06:19]** Did you get moved?

**[01:06:25]** Do do doop doop doop doop. Bunch of fucky shit. What's going on? I don't know what all this is.

**[01:06:35]** I don't know. Yeah. So why is there so much work going on in the capture volume calibration?

**[01:06:48]** This got. Got clumped.

**[01:07:01]** Okay. Yeah. So this. Oh yeah. Okay, so this.

**[01:07:04]** Now this makes sense. Right? So now we're deleting a lot of media pipe specific stuff because presumably a lot of this was moved to Skelly tracker.

**[01:07:19]** I think we could probably call this a success. I think like I added trace and success and success tagged it as pink.

**[01:07:33]** But there is like a bit of weirdness because something in the linter doesn't. Doesn't notice that I added those. So it always. It's always like, I'm like logger trace. It's like I've never heard of this before in my life, but running it works.

**[01:07:44]** So it's a more. More logger shit. Oh, that's interesting. Okay. Yeah, I hit the.

**[01:07:51]** There's like a. The headspace of like I just hit that point. So I need to be done. I'll be done soon enough.

**[01:08:08]** Blah, blah, blah, log of, log of.

**[01:08:15]** Oh, you're making this more explicit. Makes sense. Yeah.

**[01:08:20]** I think a lot of the way that we're handling this, this blender stuff, I think we should sort of. We should base. I think we should. We should chop chop.

---

### Chunk 8 [01:08:15 - 01:18:15]

**[01:08:15]** Oh, you're making. It's more explicit. Makes sense. Yeah.

**[01:08:20]** I think a lot of the way that we're handling this, this blender stuff, I think we should sort of. We should base. I think we should, we should chop. Chunk that off and kind of use it as a starting point for like, like, like community plugin, add on stuff and just basically say it's like just put a script in this place and then we'll, we'll look and we'll get a list and we'll just run that script.

**[01:08:49]** Like we can set a parameter model, I guess, sort of thing. Because that's basically what's happening here in the exports tab is it's just like here's three scripts. You can run whichever one you want, but they're behind radio buttons, which are very static. So if we just had it. And I think they're all default.

**[01:09:07]** They pull like default default types of settings, if they pull any. So if we replaced that. So we just. First of all, there's only one blender output. Great.

**[01:09:19]** And then we just take whatever that kind of concept and like the infrastructure of like sending scripts to sub processes and like giving them access to like the file system and the parameters. So whatever.

**[01:09:33]** First of all, security stuff you have to say like we have to have some way of vetting like that type of thing. Unless it's in a. Like a lot of, A lot of software just has on the community stuff, they're just like, listen man, like Wild west, good luck.

**[01:09:49]** But yeah, so we can set our blender output to be the one that we choose and then just have another place that's like there's a folder called plugins or whatever and we're going to look in there for a script that calls your entry point and then does whatever. Like maybe like a folder like Dunder Main. Like we can enforce like you put your package in here, we're going to look in there for Dunder Main where it should be and we're going to run it. And then whatever happens after that is up to you. And so then we can just dunk dynamically like at load or whatever or just have a file watcher on that folder, which we already have for the CSS stuff and just look for, you know, look for stuff in there and I think like if it's a single file, just run it and it should be in the if name equals main block.

**[01:10:39]** If it's a folder, then we look inside of it for the Dunder main, wherever it should be.

**[01:10:48]** There you go. That's a Plugin system. Great. But I think we're there, we're at that point the community would, would want to make stuff for sure. It could be a new widget that pops up.

**[01:11:05]** It could be a web app. Doesn't matter. Do whatever you want. God, that would be great. Oh my God.

**[01:11:13]** And then we just like host it somewhere and like, let's just let them host it on GitHub and we'll just sort them by star count. Like, I don't want to keep track of your shit.

**[01:11:28]** User count. You can probably get it from the user data. That seems like a reasonable thing to pull. Like, which add ons, which plugins do you have? Activated.

**[01:11:37]** Oh my God. Okay, we gotta be done.

**[01:11:42]** Blender shit, blender shit. Chop that up, validate, raise, pydantic, pedantic model. Don't even. Just whatever, whatever this is being used for. Pedantic model.

**[01:12:01]** Blah, blah, blah, words. We got to get all this text out of our code. We got to move it somewhere else and we got to start putting. We got, we got to, got to, got to add internationalization. That's going to be one of those things that like, none of us will ever know how much of a pain, how much of a problem that is, because everything we're doing with ourselves and through the community is in English.

**[01:12:23]** We have been pinged by 102 countries.

**[01:12:31]** Many. How many of them speak English?

**[01:12:36]** So I think once we move to web app land, we get a lot of internationalization stuff for free. In QT land, it's like i18. It's i18 everywhere. But I think in web app, Web app land we get that for free. Qt, they have something for it, but I don't know, it's weird, screwy.

**[01:12:52]** And I think we'll have to do some of our own fuckery to like, they want you to have like the, the translation files like ready to go. And at this point in my life, I am quite confident that if we just had all of the English text in one good clean place with like a good file name system, and I like me with my current skill set, could build a little like AI watcher, cron job or whoever that will just translate it to what, like to the full panel plea of languages that an AI can translate these days, which is a lot, and then we'll just invite the community, we'll put some stuff in the, in the UI that will basically say like, hey, if you're a native speaker, this is like some way to tag AI generated text. I think we should just have that in general, like culturally like a font. I don't know.

**[01:14:01]** Stage. Stage magic.

**[01:14:05]** Move your head as the connection happens. Okay.

**[01:14:18]** Yeah. And we'll just invite members. If it says if you're a native speaker of this language and and you see something wrong, submit a. Here's how you do a PR or here's a little like internal GUI that just allows you to fix it and push a button and then it sends a PR or whatever logs it publicly. But then they'd have to consent to that.

**[01:14:38]** Make a checkbox.

**[01:14:44]** Or just say click a button and it all auto generates a little one shot patch PR and you just do it there. I like that. I like that because it's like. It's also passive teaching and it's less work for us. Which.

**[01:14:59]** Yeah, okay. Change some naming there. Sure, sure. Yeah. Virtual marker.

**[01:15:06]** Shit. This is going to female cat data handler does that. We can get rid of this thankfully. Or it's. It's sort of like, like virtual marker handled.

**[01:15:19]** So how. Blah blah blah blah blah blah blah blah blah blah blah. Not here. Not in the center of mass calculation. Which again why the are.

**[01:15:27]** Oh no, we have to be. Because it's namings and stuff like that. Okay. Yeah, that's it. Like I can't believe we're still.

**[01:15:35]** It's like when I see stuff like this, I'm like, God, how old is this? And I remember I did it, I think. But it's just like. It's weird that I would have called it that. This is not the naming convention we're gonna use.

**[01:15:47]** It doesn't matter because it's all gonna go away. Great. Obviated. I have solutions to this in the free mocap blender code which I've been fucking asking you guys to look at for a long time. So I don't matter.

**[01:16:02]** I'm not concerned that you have duplicated some effort here getting to salty mode because we're in hour one. We're.

**[01:16:14]** It's like, it's like who's gonna check whose work first? It's like you don't get like I'm right. Sorry, when in doubt. It's not a question.

**[01:16:45]** Not because I'm always right, because I'm usually not right. It's just that like I don't have the energy if it's like. It's like I like it this way. Well, I like it this way. It's like, oh, well, agree to disagree.

**[01:16:55]** It's like, no, sorry, that's not how trees work. What the shit is all of this? Calculate anatomical data.

**[01:17:06]** This is new.

**[01:17:13]** Okay, so we don't calculate center of. Okay, so. Ah, naming. So this is. We have been speaking at possibly with cross namings, because like this.

**[01:17:28]** Because I was saying data aware, which includes things like virtual markers and stuff like that. Because you have to know that this is the shoulder and that's the shoulder to calculate that this is the chest. But I may have been using the term anatomical data pipeline processing stuff, which includes things like center of mass.

**[01:17:52]** It's also in the same space. I would put this in Skelly Forge.

**[01:17:58]** No, this will go into Skelly Forge. Remembering what the pipeline was. Pull that up. I'm not going to. I need to be done in 130 because my brain is melting.

**[01:18:07]** Data saving pipeline. Okay, so he's pulling pipelines.

**[01:18:14]** This is.

---

### Chunk 9 [01:18:00 - 01:27:53]

**[01:18:00]** Remembering what the pipeline was. Pull that up. I'm not going to. I need to be done in 130 because my brain is melting. Data saving pipeline.

**[01:18:08]** Okay, so he's pulling pipelines.

**[01:18:14]** This is also all in the blender code. This doesn't need to exist as we've discussed. You should for sure. Yeah. This is all.

**[01:18:23]** Go away.

**[01:18:31]** I can't. I can't parse this. A lot of this is. A lot of this is duplicated.

**[01:18:40]** It just not all of it. But it's like. It's. It's.

**[01:18:50]** Shouldn't be in free mocap. Like data saving pipelines.

**[01:19:00]** No, none of these should. Because, like. Because this was the one we saw before. Like, yeah, like, right here. This could just be one call.

**[01:19:12]** Wait, but why was the other one like. There was a thing that was like, if it's raw or something like that, is it pulling it from the name? Oof. Okay, great. This is.

**[01:19:22]** I am. Oh, my God. So much of this is gonna go away. Oh, thank God.

**[01:19:32]** So, like, what is. What's going on here? Run image tracking. Run image tracking process folder of videos. What I thought.

**[01:19:47]** Oh, no, I remember that. And then you go, me. I thought that was all in Skelly Tracker. Does this thing just call Skelly Tracker? Where do you live?

**[01:20:02]** My brain is gonna fall out of my head. This isn't Skelly track.

**[01:20:12]** So what's all this then?

**[01:20:15]** Setting. Oh, this is like Q. Yeah, yeah, yeah. So a lot of this.

**[01:20:23]** Yeah. Also, this is another sort of like. Like, a lot of this is like setting up the logger, which we should just do better, like checking if the file exists, which. Which do that upstream somewhere. Is that right?

**[01:20:41]** Because it's going to load. No, no, this is. This is file I O. Shit. That we shouldn't. Like, this should just be sending the data down, I think.

**[01:20:52]** I don't know. It depends on how the process is getting run.

**[01:20:59]** Run image tracking. And then this.

**[01:21:04]** Oh, my God. I guess it's here. I don't know if I can deal with this later. Pipeline check. Processing Pipeline check.

**[01:21:14]** We're doing a bunch of processing. Pulling strings from a dictionary is. No, this is pedantic. There's like, duh. I know this is.

**[01:21:26]** This is how we have done it. But we're not. This is. This is. No, we're not pulling strings from dictionaries anywhere that we can avoid it.

**[01:21:38]** Whatever this is will be a pydantic model or it will go away like. Or it shall be obviated. Triangulation pipeline functions. Why Are there all these pipeline things happening in here in this pr? Is this, like.

**[01:22:00]** I know that this happens. I understand, like, that you like that. It just. It PRs get gummed up. But I'm just.

**[01:22:07]** I'm like. I'm looking at it through this interface, so I don't get to see what's actually getting used. It's possible. Yeah. Scale three.

**[01:22:13]** No, that's skeleton.

**[01:22:20]** Get triangulated data. Get is not the right term. Get is. It's already there. Give it to me.

**[01:22:34]** File IO. Shit.

**[01:22:40]** Blah, blah, blah.

**[01:22:45]** Use keywords when you can. What is happening here? Oh, is this nested? Ugh, no. Oh, it's just.

**[01:22:56]** It's just. Yeah, this is. This is one thing. This is another thing. Yeah, this is another, like, file IO.

**[01:23:05]** Like, we don't want to be doing file IO in a working function, especially not one called get.

**[01:23:20]** In if statement.

**[01:23:25]** This is my dumb.

**[01:23:29]** This is my dumb post processing. This is also my dumb.

**[01:23:35]** Me. Yeah. Dumb change. Oh, this may be moved. See, like, this is the kind of thing that should absolutely be in SkellyTracker, which is probably where it is now, because these are parameters that MediaPipe has to know and then it produces.

**[01:23:53]** Yeah, maybe that's what it is. Like, this is all that you need to know to run MediaPipe. And then MediaPipe will send back whatever it decides to send back to you, which in this case, it sends us, like, models that. I actually don't know what they are on these. I can't remember.

**[01:24:10]** I didn't know how. I didn't know what pedantic was Last time I looked at media pipes code, I'll bet if I looked again, it would be pedantic. Or did they, like, frozen sets or some. I don't know.

**[01:24:24]** Yeah, and then I don't know. We'll have to see what it is Run to true from skip to. Oh, yeah, this. We talked about this of, like, the. There was like a cue conflict thing.

**[01:24:42]** Like, you check it. Like, it was like the checkbox was. Don't do it. It's like. No, no.

**[01:24:50]** Like positive affirmation. It's like it was the opposite. We did whichever one base equals media. There my media type. Okay, I see what's happening here.

**[01:25:10]** So it's sort of like there's a base and then it's. I see.

**[01:25:16]** I see what's happening. I. It's kind of. It's like setting a default. It's either a default or a workaround.

**[01:25:23]** It's like it's either setting a default or it's like it's a workaround for now. The other one, I think it's. It's fine for now. I don't. We'll think more about it later.

**[01:25:32]** Blah, blah, blah, blah, blah. Single video. Check, check. Single video. Ugh, hate that.

**[01:25:41]** This is where a lot of our gets broken. Like, this is the recording info model. I just want to apologize to the world at large for the sins that I have committed in this space.

**[01:25:52]** For they are ample. Naming, naming. Delete dead code. Delete dead code. No code.

**[01:26:03]** Graveyards, please.

**[01:26:10]** Whatever. Specific logs are good. Type hints are good. If return. Type hints are good.

**[01:26:15]** Whatever, whatever. Oh wait, but this is already there. Already is that. Did that get moved from somewhere? Because the current one has that.

**[01:26:29]** It just doesn't work. Or it does, but it's just some like, weird. There's like some life cycle where you have to like do it before you start it and it's like. And if you don't, then it works.

**[01:26:42]** You have to check it before you connect to the cameras. If you check it after you've connected the cameras, it doesn't do anything. It checks fine. It just doesn't do anything. And if you.

**[01:26:50]** Even if you do it right, it's it like hella slow. Which it shouldn't be because it's not a heavy computation. So it's blocking some somewhere because it's Python and there's Gil and it's.

**[01:27:08]** Okay, we have three minutes. I feel productive in this session. Yeah. Info to debug. Blah, blah, blah.

**[01:27:20]** Calibration. This is the auto format thing. It looks like.

**[01:27:29]** This is our calibration. No, it's auto format. Doesn't matter. God, I can't wait. I just cannot wait.

**[01:27:36]** I cannot wait to just take this whole gooey and just put it in the ground and just be like. Thank you, bye.

**[01:27:45]** We are ready. We are so ready. Oh my God, that's ugly to me. This looks wrong to my eyes.

---

### Chunk 10 [01:27:45 - 01:37:45]

**[01:27:45]** We are ready. We are so ready. Oh my God.

**[01:27:51]** That's ugly to me. This looks wrong to my eyes.

**[01:28:02]** This is all wrong. There's, there's a lot of. This is not how we do. Like, it's how we do, but it's not, we're supposed to do. CG Tinker once called me.

**[01:28:13]** I was like, this is wrong. You should fix it. And I was just like, you, dude.

**[01:28:19]** Because it was just, he was, it was just the classic, like, you're not supposed to do it like that. You should do it a different way. And I was like, oh, really? That's the problem? That's the top of the priority list that you want me to work on.

**[01:28:29]** I, thanks for calling it out. But also like, don't come to me and say like, I don't know, man. It was kind of like, it was, I, I, I did not receive it well, but it could have been meant well. But it's kind of like, I just get that way sometimes. Someone's like, hey, you should work harder.

**[01:28:48]** It's like you, Even when that's not what they're saying, sometimes that's what I hear. Okay, Some life cycle shit again. Like all of this shit is like python nonsense. Like making interactive code with. Making interactive UIs with non interactive code.

**[01:29:14]** Blah.

**[01:29:17]** Like the sort of JSTS framework is just, it's so much better. It's just like there's so much stuff that just made, that's just easier. One is like a lot of the signal slots and like there's just, just like you just emit. I mean it is signals and slots.

**[01:29:35]** Events, event based programming, whatever the hell it is, then an event doesn't matter.

**[01:29:52]** Whenever I see something like this, I'm like, I don't know what it is, but I don't. Like, feels like a mistake was made somewhere. This feels like wrong tool for the job. Like, that's too deep. That's way too deep.

**[01:30:03]** Why are we, why are we down there?

**[01:30:12]** Where are we here? Log view. Log view. Queue handler.

**[01:30:25]** This is our console moving forward.

**[01:30:33]** We don't have to make it, we don't have to make that ourselves. So much of this is us reinventing the wheel. It's reinventing the wheel with the wrong tools used the wrong way.

**[01:30:44]** I do love the solutions that come out of it though. Like, it's so creative what happens. It's just kind of like, it's very nice that we're doing this, but we have to understand the difference between like exploration and like production.

**[01:30:59]** Cause things get broke when you do them yourself. Because you're not special. Your solution is not special.

**[01:31:12]** You're not the clever one that figured it out.

**[01:31:16]** It's kind of like Philip. Well, this is actually a Philip direct thing because no one else will get the reference. But it's kind of like. Because you said this actually to me once, like, trying to get comfortable going on a high line. And it was like thinking about the equipment.

**[01:31:29]** It's like, what if my harness explodes? And he's just like. Like, you're not the special one. You're not. Like, that doesn't happen.

**[01:31:39]** Statistically speaking, that does not happen. And even though sometimes it does happen, that's law of large numbers. Like, it's not you. It's like, it's really hard. That's like internalized global statistics.

**[01:31:53]** No, my body doesn't. My body can't. But that's why we love highlighting is because that's where we get to with it. It's like, how much do you really trust a working load limit?

**[01:32:08]** Oh, where the shit even are? We process thread worker. Blah, blah, blah. Doing some blah, blah, blah. Configure logging.

**[01:32:16]** Ugh, this seems. No. Oh, God.

**[01:32:24]** Console log. That's just all you say. You say console log and you say cons. And I think you can. There's like, you can set the levels like right there in it.

**[01:32:32]** And it just goes. And it just goes here and it just goes there. See, look at it go. It says right there. Great.

**[01:32:41]** No, you don't. Oh, fuck me. Did I lose my place?

**[01:32:48]** I did browsers. This is why I don't like working in the browser.

**[01:32:58]** Or at least not the. Not the one that's co. Extensive with like the web browser. Because, like, I want diff. I use keyboard shortcuts for things. So like, like, like when VS codes in the browser, I use the wrong keyboard shortcuts and it doesn't work.

**[01:33:09]** And I don't like that export to Blender. Thread worker. This. How was it just moved? I think it was just moved.

**[01:33:21]** Why is there so much new code in this pr?

**[01:33:28]** Oh, this is a main file. I still don't. I learned I was doing this in Skelly Cam. I was like, I made one logger, I was pulling it into other places. And then I realized that if you do that, the logger doesn't tell you.

**[01:33:44]** Like, that's where the logger getlogger name is. The part where the log will tell you which file it was called from.

**[01:33:58]** So if you do like the global logger, everything is like, oh, this was called from configure logging. This is the configure logging logger.

**[01:34:10]** This. Yeah, this, this. It's like, I understand why C.G. tinker was upset. This is not the right way to do it.

**[01:34:16]** But I don't know. I think it was because it's like we're working. That interaction was like, we had very similar and very aligned goals, but I don't think either of us was kind of in the headspace to really wrap our head around the other person's project. Like, I tried in his space and he tried in my space, but like, it wasn't. We were.

**[01:34:41]** We were like working past each other and like, it is never quite connected. And I just, I checked and he. He marked his thing as.

**[01:34:51]** I forget the term. He's. He's like, I'm not doing this anymore. I was like, okay, I might go look in your code at some point. Like, we might.

**[01:34:58]** We might fork that and just see what's in there. Because I think he did have like a really nice, like, listener pattern that was driving Blender objects live, I think, through a websocket. And when I look back at those conversations, I remember him talking about stuff like that. But I didn't understand it at that point because I hadn't really gone into. I hadn't done Skelly.

**[01:35:21]** What was it? Which one was it? It was John Bot. OG John Bot was the. Where I learned about fast API and endpoint connections and restful APIs and blah, blah, blah.

**[01:35:31]** So I now, so now I now look back at what he was saying is like, oh, that is actually what I want. Which is like, free mocap is spitting out, you know, whatever JSON's at an endpoint or through a websocket. And then someone on Blender is like, I have received this and I'm going to move the armature accordingly. Which I think what he was building, but he was all doing it internally and like, he didn't have quite the firepower to handle all the live loading shit. Like the running media pipe shit.

**[01:36:02]** Like all this stuff just wasn't quite up to snuff. And I also think some of the, like, his, his, like the, the. The. They never looked right to me. Like I.

**[01:36:11]** Even when I got mine running, that's when I reached out to him was like, hey, I think this is all connected, but like, it's not looking right. So, you know, gobble, as they say in a very small village in Syria.

**[01:36:28]** It's like, it's a gubble. It's like a very strongly accented way to say Abel. Which Abel I don't know how to fucking. I don't speak Arabic, which means the past.

**[01:36:49]** A cough. But like in Levantine, it's not pronounced.

**[01:37:01]** So this doesn't want to be a test.

**[01:37:06]** Just, no offense, this is you trying to figure out how to do logical indexing. We don't need a test to see if logical indexing works.

**[01:37:20]** It's kind of like the same thing of like writing a 63 line function to handle NP save. It's like.

**[01:37:33]** Which I think is actually the same the same thing for this create nested dick from pydantic Same criticism to me like six months ago because.

---

### Chunk 11 [01:37:33 - 01:41:14]

**[01:37:33]** Which I think is actually the same. The same thing for this. Create nested dict from Pydantic. Same criticism to me, like, six months ago. Because I think that Pydantic just does this.

**[01:37:48]** I think it might literally just be model Dict just does this automatically. I think this is entirely.

**[01:37:57]** I don't know, like, if the model has models in it, I think that they automatically convert to dictionaries. If you call the Cobalt the top level one, I think that's like, part of the main point. I don't know. Skelly Viewer. Skelly, yeah.

**[01:38:10]** And I. We need to fix the naming of Skelly Viewer to have to be one word.

**[01:38:18]** Done. Sucking, Finished over an hour. I Under two. But I feel like a lot of good work was done. I said a lot of words, which is the important part.

**[01:38:34]** And now it's like, I don't know, Like. So I'm gonna send this. I'm gonna post this online and. Because I have talked to Philip about PRs before and code reviews before, and I think I have mentioned the main thing, which is, like, I'm gonna talk a lot of shit. I'm gonna talk a lot of shit.

**[01:38:53]** Like, I, like, listen, like, I'm a scientist, and that's how you're trained. It's like, you call it out when you see it because you. Because the baseline assumption is I am pulling punches relative to how hard, how harshly I judge myself. Like, everything I'm saying to you is being filtered through my, like, empathetic care of other people filter. When I look at my own stuff, especially stuff I wrote in the past, I.

**[01:39:18]** It's worse. It's so much worse. And it's like, you really just have to learn emotionally how to be. How to be comfortable with that level of criticism and scrutiny, because it is a compliment. I only.

**[01:39:32]** The only reason why I would tear your shit apart this dramatically is if I cared enough about your work to notice it this hard. And when I say it shouldn't be this way, it should be that way, the assumption is that I am speaking from my perspective. I am just. I am saying based on. From where I'm sitting right now, even if an hour and a half ago I said something differently, even if a week ago we had a conversation on this exact topic and I agreed with you that I was wrong in this moment, due diligence, I don't think that's right.

**[01:40:11]** And I'm going to say it straight up, because if I don't, I'm doing a disservice to the project as a whole. And the project in this case is free mocap. In other cases, it's the scientific endeavor. In other cases, it's the global state.

**[01:40:32]** I just got tired. That makes sense. I'm out. Good talk. It's great.

**[01:40:37]** Fix everything. Bye. Nothing you do will ever be good enough. And that's okay. That's part of the game.

**[01:40:44]** Alright. Bye.

**[01:40:49]** I don't even know if I put comments. I should have been putting fucking comments in. But that would have slowed me down. Oh. Because I'm.

**[01:40:58]** I was like. I was like, which button do I click to end it? And I was like, this one. But no, no, you fool. It's not the friendly green button.

**[01:41:06]** It's the friendly blue button.

**[01:41:14]** I.

---
