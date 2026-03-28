# Transcript: 2024-08-09-2024 08 07 - FreeMoCap Architecture planning

## Source Information

- **Source Type:** Local File
- **File Path:** `C:\Users\jonma\syncthing-folders\jon-alienware-pc-synology-nas-sync\videos\video_eater_downloads\playlists\[OLD] FreeMoCap Development\2024-08-09-2024 08 07 - FreeMoCap Architecture planning\2024-08-09-2024 08 07 - FreeMoCap Architecture planning.mp4`

---

**Total Duration:** 00:25:01

---

## Full Transcript

### Chunk 1 [00:00:00 - 00:10:00]

**[00:00:00]** All right, so it is the 7th of August 2024 and we're just having a meeting to talk about sort of some architecture plans and general kind of like division of labors and the organizations of the main software with the sub skelly repositories and things like that. Talking about these items which are which live in the Notes Folder of the FreeMot foundation repository. So that's GitHub.com freemocat freemocatfoundation, endnotes and kind of disorganized, but everything tagged with the current date is the relevant bit.

**[00:00:45]** So basically I started with this kind of like, you know, just scraping on paper and then I tried tried to clean it up a little bit with this draw IO board which the RAW version of which is in the folder somewhere. But basically, so we're thinking in the direction of kind of what we're starting to call Primocap 2.0, which is kind of like a cleaned up version of the current architectures. And the main architecture of the FreeMo CAP software is that there is sort of like a core software repository, like a core like primary gui, which is the freemo cap slash freemo Cap repo. And the functionality of that sort of primary core software is comprised of the sort of combined capacities of all these sort of sub repos, like sub scalar reposition. Skelly Cam is the sort of star of the show for the most part, but there's others.

**[00:01:50]** And the plans going forward is to kind of like clean up some of that like the poly repo format there to sort of like clean up, operationalize a lot of it, sort of get more clear about the division of labor and the responsibilities and the relationship between the different subcategories. And eventually, and that's what I talked to Philip about previously of like sort of have each of the sub skellies sort of follow a specified structure where like each one should be able to kind of have like a standalone mode in addition to being sort of pulled into the main like Voltron machine and sort of run as a part of the main free mocap thing. So more to talk about there, but for now I just want to talk about the basic layout and do it kind of more in the context of this Oops to do kind of. It's sort of conceptually like loosely related to the idea of like the processing pipeline, but it's sort of not fully related to that. There's some complexity there, but I think it's still helpful to think about it.

**[00:02:56]** We're on the sort of on the left you have like the start of the process, the place where the empirical data comes in. And that's handled by skellycam. Skellycam's job is to connect to cameras and or load from videos which obviously different in many ways but also quite similar in many others. But it sort of generally handles. The idea is like skellycam's job is to handle cameras sort of slash videos.

**[00:03:27]** It's sort of basic capacities or things like, like viewing the camera, start, stop recording, connect to cameras, load videos, sync videos which would involve. Which is currently handled by the Skelly synchronized sub repo. But I think we should probably pull that in and I think that would be Skelly Cam. But I could, I could hear arguments that it might want to go in a different place or. Or an argument that it should remain standalone but sort of whatever.

**[00:03:51]** Yeah. And then it should also handle like know extracting or sending camera configs and there's a web socket and there's a kind of a whole conversation around how we want to define like the API of each of these things. So the formatting of like the list here, you know, sort of different for each repo. But that's fine. But anyways, so skellycam mostly will be spitting out multi frame objects where a multi frame and is basically if you're imagining this sort of running in like a real time type of mode it would be one object slash dictionary like object of images per camera along with timestamps and metadata and things like that.

**[00:04:37]** So again in a real time mode skellycam's main job is to spit out those multi frames at a cadence that matches the frames frame rate of the cameras or something like that. In a non real time mode, you know, sort of think about things comparably whatever those images, basically raw images or compressed for front end or raw for processing or saving whatever can go mostly into Skelly Tracker. And Skelly Tracker's main job is to do image analysis and computer vision. Like sort of it handles the it. You know we've got the sort of the inheritance, the base tracker and multiple trackers and all that kind of stuff.

**[00:05:19]** But mostly its job is to process images and pull out usually two dimensional data. Like you there's you know and I think in our world even when we are producing 3D data from 2D data that's still kind of. It's basically just dummying the 3D aspect by just like saying the depth is one or whatever.

**[00:05:42]** So SkellyTracker's main job is to produce 2D data and that 2D data kind of splits. There's sort of this other like this is a non existent sub Skelly right now like Skelly Calibrate. Currently we just use any pose for that but I think we're probably going to start evolving beyond that in various ways. But whatever that winds up looking like it is still going to be pulling in data from SkellyTracker and mostly in the form of like the charuco data and stuff like that. In addition to that it's also gonna be spitting out.

**[00:06:18]** Skellytracker also produces like skeleton like sort of the raw tracker skeleton data like MediaPipe et cetera.

**[00:06:27]** And that's gonna go mostly into Skellyforge where So in terms of like the development of these sub like Skelly Cam has gotten by far the most attention. Skelly Tracker is sort of has the. Is sort of second most identified. Skelly Forge is in there. It's doing a lot of.

**[00:06:47]** It's doing the jobs well but I would say its identity is a little bit more like undefined at the moment. So there's sort of some of the, some of the earlier stuff is sort of more descriptive and sort of the. The right side of this is a little bit more like prescriptive and you know, open for interpretation and discussion. But I think so Skellyforge main job I think should be basically creating the 3D data like that. We use question marks around whether it should handle the triangulation or if that should be part of Skelly Calibrate.

**[00:07:21]** Whatever. Oh a Skelly calibrate. Its output is camera calibration info which means lens intrinsics which is the basically undistortion numbers and then camera extrinsics which is 6 degree of freedom position which is a XYZ position and an XYZ rotation. So Skelly Calibrate's main job is to calibrate the cameras and create the capture volume. So Skelly Forge then its job is to possibly triangulate.

**[00:07:49]** But it could be argued that would go elsewhere. Doesn't seem super matter. But it also handles things like cleaning and post processing which is like gap filling and Butterworth filtering and stuff like that. That's the kind of just like generic data processing side of it. Like it's sort of like you know, data now what's the word?

**[00:08:08]** Like like signal processing. Like without any context of what it means. It's just like oh these are squiggles. We need to clean them up. And then it would also handle like, the conversion and creation of basically what Aaron's skeleton model.

**[00:08:28]** And it could handle things like tracked point to key point mapping, which is something that came out of my more recent blender rabbit hole, where the idea would be that your media pipes, your openpose, your whatever, they produce tracked point data, which is mostly what's going to come out of Skelly Tracker. And then skellyforged could have the mapping object that says, oh, here's how we map these tracked points from whichever track that we care about into these standardized key points which we have defined relative to this skeleton. So conversation to be had there, but we can sort of talk about that. And then skellyforge would also handle things like center of mass and then rigid body corrections and things like that. And then I also put these here in green.

**[00:09:18]** Like, these are things that are sort of more animation focused. So like foot locking, where you like pin the foot to the ground. Something that you would want for an animator, but you could argue is sort of like a little bit too aggressive on the data manipulation to be good for science. But that kind of depends on the application. Face shape keys.

**[00:09:38]** There's all this stuff happening there with the, you know, Philip and Andres, there's like a whole. If you guys haven't noticed, there's like a whole little subculture in the public server forming around, like, figuring out how to process face data, which is super cool and fun. And shape keys. Face shape keys is sort of like a animationy thing that I wasn't even aware about, but it sort of is.

---

### Chunk 2 [00:09:45 - 00:19:44]

**[00:09:45]** Subculture in the. In the public server forming around like figuring out how to process face data which is super cool and fun. And shape keys. Face shape keys is sort of like a animationy thing that I wasn't even aware about. But it sort of is a.

**[00:10:00]** Is a. It's a very different way of thinking about mocap data than I was. Than I would. So it feels more animate Y. But you know it's also things like finger.

**[00:10:10]** Like the finger cleanup and some joint angle clips like you can look at like the. Like. Oh like the. Here's the reasonable anatomical limits of joints. Let's clean up the data that way.

**[00:10:21]** Basically these stuff in the green is sort of Skelly Forge ish things that are potentially more animated than scientific. But there's going to be some gradient there based off application and that's sort of also going to. Oh, I could have changed the picture here but yeah on this side. So Scully Forge kind of produces this skeleton data, 3D data cleaned up, process, post process, whatever you want to say. And this is.

**[00:10:49]** This guy here is basically like the main. Like sort of like polished output, not raw output but sort of polished output. And then that could feed into Skelly Blender which we would be that blender out blender output the blender add on whose main job is to produce a blend scene and then produce all the animation file types. And then this would have like its own blender add on associated with it which is sort of a lot of Andres stuff that kind of has you know, more bells and whistles and controls and like you know, checkboxes and sort of like the kinds of controls and interface that an animator would want. But sort of the idea is that you know this is kind of a terminus of our pipeline.

**[00:11:30]** Like it's sort of like we're going to give you the add on, we're going to give you some control over that. But it's kind of like that's sort of beyond. We don't really like worry too much about what happens after that. That's kind of outside of our scope.

**[00:11:43]** There's also this. This is another non existent one. This is sort of scaly metrics again based off some stuff Aaron's been doing. And the idea would be that the job here to kind of handle like analysis like stats static report like more like research based kind of questions. Things like Skelly Forge that's just sort of part of the.

**[00:12:06]** The base activity of doing motion capture. Skelly metrics would kind of be like okay now we have Now I want to know more specific things that are sort of relevant to some domain of inquiry. So I might do that sort of calculation there and producing like, you know, static stats, statistics and static reports and whatever sort of. Again, this doesn't exist yet, just kind of imagining it. And then Scaly Viewer is going to be our sort of visualization tool that will handle like visualizing 3D 2D time series data and images, which kind of.

**[00:12:42]** This is another kind of break from tradition where the. I think we actually are going to. So right now, Skelly Cam, like the existing operating one, holds its own GUI for viewing the data. And I think when we had talked about the independent role of each subscali possibly within this same recording, I was talking about it in the context of each sub Skelly would hold its own ui, which it might to some extent, but we might also just let Scaly Viewer do that job. So like, for example, like viewing images and stuff like that, you know, we could build that independently into Skelly Cam, but we could also have skellycam just use Skelly Viewer for its visualizations.

**[00:13:31]** And I realized that sort of like while I was doing that this morning that, you know, we've had a lot of conversations around like being wary about like circular imports and circular dependencies. We got it like, where are we going to put this, that and the other? And I realized that if you just think that each of these sub skellies can either have the existence of like living together, like sort of being pulled together into like the main freemo core and sort of operating that way, that's fine. And they could also, you could also imagine them operating in a standalone mode where they are the main, the main store of the show. And then in that mode they could pull in from the sub skellies on their own and just construct whatever they need to operate in standalone mode.

**[00:14:20]** And that would not have to be a circular input as long as you're sort of. As long as that's managed properly. So like, skellycam can depend on Skelly Viewer in order to run in a full standalone mode, but it can also just as easily not have a front end and just attach its API to the core API and then live happily there.

**[00:14:50]** So yeah, that's kind of the main idea. Skelly Cam handles images. Skelly Tracker takes in either videos or connects to cameras and produces multi frames which are synchronized images. Skelly Tracker does image analysis, computer vision on those images and produces usually 2D data. For example, charuco data, mediapipe tracks, open pose tracks like just 2D data in general calibration, relevant information.

**[00:15:18]** So I'm saying charuco, but in the future I'm hoping to sort of move away from the dependency on Chauco boards, but still just you know that it would still be 2D image data that goes into this calibrate to produce the capture volume calibration and lens intrinsics, camera extrinsics, things like that. Skelly Forge's main job would be to take in 2D data and sort of have a copy of the, of the capture volume definition in order to create 3D data, clean it, post process it, shove it into our sort of preferred like data model output and then make that data available for Skelly Viewer. Spit it over into Skelly Blender to produce animators. Yeah, Skelly Bender produces blend files and animation output data types and handles things like retargeting and reorganization and for things like Unity or Unreal or whatever. Like that can kind of be Skelly Blender's job, like put it in the animation space and then we can do animation stuff with it.

**[00:16:24]** And then that data can also go into scaling metrics. If you want to do more like analysis, like scientific types of analysis. I think a lot of the like the playground code that Aaron has of like oh, here's just a million little analyses you can do on the types of data like that might want to live in Skelly Metrics. And then there actually should be an arrow kind of pointing back from Skelly Metrics into Skelly Viewer. So Skelly Viewer's job is then to just visualize the data in its various formats.

**[00:16:51]** Sort of we'll have like the default visual output and also have it ideally be kind of like composable and configurable for people who want to make their own types of visualizations. And then sort of Skelly Viewer also just I think could generally have like a back propagation kind of like a role in everybody where scaly viewers job is sort of collectively to handle things like observability. Like if of all these things we're like, you know, its main life is to sort of represent a recording, but it also could live happily and sort of using these, these features as just a way to manage like observability and visualization and sort of, you know, bug keeping and whatnot for each of the different sub skellies.

**[00:17:36]** Yeah, okay, that. How long was that? 17 minutes. That's not bad.

**[00:17:43]** So before I cut the Recording. Is there anything that think needs to be said for clarity purposes? Does that make sense? Was it anybody willing to speak on camera? That all makes sense.

**[00:17:58]** The only major thing that I didn't see in here is dealing with the saving and exporting and splitting of our data files.

**[00:18:11]** And mostly the, the reason I bring that up is I think like Philip and I have been seeing the signs recently of how that's going to become a bit of a pain the more trackers we put in. Also as we put in like multi person tracking and stuff. Yeah. What we want to say will heavily depend on everything that's coming out. And so.

**[00:18:38]** And also on, on that point, something Philip had pointed out before and something I've seen in skellyforge as it exists right now is that using it on its own is only so useful because at the end of it we just end up with this data that we can't like split and export into the current primo cap format. Meaning like we end up with like if I, if I run Skelly Forge on its own I'll get like the post processed numpy data array but not the like here it is, hands face numpy CSVs and stuff. Yeah. Functionality is just. Yeah.

**[00:19:16]** Yeah. So that's, that's kind of like. That's. That's. That's the past.

**[00:19:20]** So that's. And we can, we're going to. The future is going to look a little bit different but I think that each of these things. I didn't have it on here but I have in previous iterations like sort of. Each of these stages is going to have its own sort of form of persistence like things that's going to save to disk.

**[00:19:38]** So Skelly Cam will save videos. Skelly Tracker will save the 2D data in various formats.

---

### Chunk 3 [00:19:30 - 00:25:01]

**[00:19:30]** Iterations like sort of. Each of these stages is going to have its own sort of form of persistence, like things that's going to save to disk. So Skelly Cam will save videos. Skelly Tracker will save the 2D data in various formats. Skelly forward will save the 3D data in various formats.

**[00:19:48]** Scaly Calibrate will save the calibration. Scaly Metrics will save reports. Scaly Viewer will probably save videos. And Skelly Blender will save blend files and other animation formats. So it's going to have to be.

**[00:20:01]** And I think the question of like, yeah, like a lot, I think a lot of the growing planes you're describing are sort of, they are features of the 1.0, kind of like logjam, where there was this kind of like this idea of like there's a more central, singular pipeline that produces a standard output and we're just kind of over. We're outgrowing that as we sort of make things more generic. So I think we're gonna, so we will want to be sort of mindful of how, of how we save those things out. Because I think there is going to need to be some like, it's. We're gonna need to retain like the concept of like a recording and like the data, like sort of that is proliferatively associated with processing the data from a recording.

**[00:20:49]** Because in the end it's going to be like raw data remains videos, sort of like asterisks plus calibration equals raw data. And then all the different 2D data, 3D data, animation data metric data, visualization data is going to sort of be derived from that. And I think it's going to want to be some sort of databasey, central sort of JSON core sort of format that kind of keeps track of each of the data types, you know, 2D data, 3D data, etc. And rather than just saying like, oh, here's the body data, it might just be like there's kind of like a key value listing of, you know, oh, we have the 2D data. Oh, there's like three entries in that list.

**[00:21:40]** There's media pipe data, there's open post data, there's some other generic thing. Okay, cool. The 3D data. Yeah, we, there's this many keys on that list and each of the keys represents like a processing run and the pipeline definition is part of the metadata or something like that. And then as we get down to like the metrics of like the earth faith for the viewer, you know, we'll need to have an interface where the people, you know, people can kind of like see what they have available and sort of select.

**[00:22:13]** It's like, oh, I want this 2D data to feed into that pipeline and produce this kind of thing and then view, like, have views based off of that. That's complex. It's definitely future looking, but I think it's kind of, it's not too hard for me to imagine that it is just kind of like there would have to be a fair amount of like machinery built around that idea. Because I think right now our system is pretty good at sort of saying like we understand that there is like the staged pipeline and each stage sort of produces its own type of data. It's just that our current method assumes that there's only like one instance of like the 2D tracking step produces 2D tracking data.

**[00:22:58]** And we're just going to need to have like a more sort of complex model there where there is still this like sort of staged ish data types that gets produced. But the ways that we interact with like downstream data, like you know, 3D data which relies on 2D data, like the way that we handle those processes is just going to have to be able to sort of like pick from available options. And the way that we like save and manage like individual recordings is going to have to include that sort of concept that there could be different like multiple instances, probably at least you know, somewhat overlapping versions of each things. Because like, well, I guess not. Because yeah, I'm thinking like media pipe tracked data versus YOLO plus YOLO cropping plus media pipe tracking data.

**[00:23:51]** Like, you know, it's like these are like the configurations could be overlapping even if the data is kind of independent. And you know, this, it's the kind of thing like it's, it's, it's a challenge that we'll have to think about. But it doesn't seem like one we can't handle. It's just kind of like there's going to be a little bit of like figuring out as we go along on the basis of like lessons learned. And I think the bottlenecks that we, that you're encountering of like, oh, this is getting really cumbersome to deal with.

**[00:24:23]** That's where like you can kind of think about like what would be an idealized version of this, what, what could work. And then we kind of like test and try things out based on that. Does that make sense?

**[00:24:37]** Yep. Cool.

**[00:24:41]** Anybody else?

**[00:24:49]** All right, well, I'm going to turn off the recording now. If you're watching this in the future. Hi. I hope you enjoyed it and goodbye.

---
