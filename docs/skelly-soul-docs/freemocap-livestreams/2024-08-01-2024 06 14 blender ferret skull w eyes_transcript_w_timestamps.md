# Transcript: 2024-08-01-2024 06 14 blender ferret skull w eyes

## Source Information

- **Source Type:** Local File
- **File Path:** `C:\Users\jonma\syncthing-folders\jon-alienware-pc-synology-nas-sync\videos\video_eater_downloads\playlists\[OLD] FreeMoCap Development\2024-08-01-2024 06 14 blender ferret skull w eyes\2024-08-01-2024 06 14 blender ferret skull w eyes.mp4`

---

**Total Duration:** 00:07:01

---

## Full Transcript

### Chunk 1 [00:00:00 - 00:07:01]

**[00:00:00]** Oh, that's the gaze target. So right now both the eyes are just doing a damped track onto this thing which is defined here. That guy.

**[00:00:15]** Yoink. Yeah. So the eyes are copy location of the socket, which is this guy. And then they are damped track onto the gaze target which is this guy. Hello.

**[00:00:30]** And yeah. So you know, you could put constraints on that and you know, whatever, like figure out like rotation constraints. And then eventually we can do like open some stuff and actually model the muscle connections and things like that, which will be very fun.

**[00:00:51]** Can also turn that off. And let's see this. And let's turn this edit mode. And now here's the model of the eye. There's like a little point light in there just because it looks cool.

**[00:01:09]** And you can kind of let you see the iris openings. But go into the. Let's see. Go into the data. Yeah.

**[00:01:16]** And then I select the inner ones and scale that up and down. Look at that. Whee. So that can be, you know, driven. It could be reactive.

**[00:01:26]** Doesn't matter. Go negative. Which probably doesn't happen in real life. Yeah, I just sort of like eyeballed the location of the eye socket center, which was based off of. Let's see, tab again.

**[00:01:43]** Yeah, right. I just took the mean. I collapsed these three vertices and made a attached the eye socket empty to the mean average of those points, which I guess didn't. I don't think that vertex survived. But that's fine.

**[00:01:59]** Yeah. And then here's the I camera. Oh, which is over. You can see over there.

**[00:02:05]** And it is hypothetically. Let's see. Grab. You select. Select and camera.

**[00:02:13]** And so this is the same.

**[00:02:18]** Those are the numbers that we get from. Oh, this isn't the right one. But that's the field of view that they list on their site. And yeah, fun, fun stuff. We.

**[00:02:30]** Oh, sorry guy.

**[00:02:35]** And. Oh, right. I forgot it turned off. So let's see. Grab.

**[00:02:39]** You grab. You turn you back on. And there you go. Grab. We.

**[00:02:47]** So this is doing. This is in cycles mode, which is showing like the light and what's it called, like Ray Tracy type of stuff. I guess these three lights are from some lights in the scene. They're just giving some light on things. You can see a reflection, which is cool.

**[00:03:05]** Do this kind of mode.

**[00:03:10]** Oh, wait. I guess I can. I don't know if I can. Anyways, who cares? Yeah.

**[00:03:14]** So you know, this is just the start. Millions and millions of other things can be done with this. We could, you know, apply more physical models to the light calculations. We could Project world stuff onto the retina through the iris, through the material. So this is the, these are the materials that are.

**[00:03:36]** These are the cornea sclera and iris is sort of just an occluder. But the cornea, you know, there's all these, these values, whatever these are like index of reflection, roughness, subsurface scattering, specular reflections, all these type of stuff defined in kind of like animation terms. But you know we, if we can get measurements of these numbers then we can do all the stuff that we need to. So like with like IOR you can see it sort of changes index refraction as it should. And then like I don't really know what a lot of this other stuff is.

**[00:04:09]** But yeah, we'll figure it out. Figure it out. And then. Yeah, then you can also. This is just the mesh of the eye.

**[00:04:18]** It's really simple at the moment. But you know we. Let's see. Actually I think I can subdivide. Yeah.

**[00:04:27]** So we can add more geometry as we need to. And the nice thing is is that the same geometry that defines the mesh of the eye also defines coordinates in the eye. So we can, if you can figure out just like where different points.

**[00:04:47]** Right. Like as we start, when we start protecting things, if we just figure out where the ray trace of it hits the face of the mesh, then there you go. That's all you need. Well, I mean that's all you need to get in retinotopic coordinates, which is a good chunk of the game. And then eventually of course, this whole guy, I don't know what's parented properly.

**[00:05:11]** This guy will be attached to a spooky skeleton. Can I do this just for speed? It's not going over. Why not? I don't understand.

**[00:05:20]** Anyways, who cares? Yeah, wee fun stuff. Skulls. Skulls and ferrets.

**[00:05:29]** That's fun. Actually I haven't done this before, but yeah, because the eyes are tracked to the gaze point, when you move the skull, it keeps fixation. Actually I think I can grab, you shift, click, you control P object grab, grab. Hello. Yes.

**[00:05:47]** Haha. Now I've got that. Oh, except in this view over here. Wait, go over here. Click the camera zero.

**[00:05:58]** Yeah, now it's fixed. Now back over here. Click the skull G. And now so the eye, look, the eye camera location there is fixed in head coordinates. And so this is the effective location of where the eye. You know, if we want this camera position, which we can obviously move around, but this would be like the effective location of where we would want the camera.

**[00:06:24]** So then we would mount it on the head and have a mirror that would basically, like. If you. If you sort of like, the light bounces off the mirror and then into the eye. So if you just do the geometry. This is the location of the camera over here is.

**[00:06:43]** You can sort of figure it out from that. I hope this recording is getting my mouse position. If it's not, this might be confusing, but yours. You'll figure it out. It's not rocket surgery.

**[00:06:54]** Okay, bye. We're done. Have fun. We'll come back to this, obviously, but this one I want to show you. Okay, bye.

---
