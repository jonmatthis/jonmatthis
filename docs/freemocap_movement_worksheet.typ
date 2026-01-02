// ============================================================================
// FREEMOCAP COUNTER-HEGEMONIC PROJECT WORKSHEET
// A Strategic Framework for Liberating Knowledge, Education, and Science
// ============================================================================
Error: there is no registered task type 'cppbuild'. Did you miss installing an extension that provides a corresponding task provider?

#set document(
  title: "FreeMoCap as Counter-Hegemonic Project",
  author: "FreeMoCap Foundation",
)

#set page(
  paper: "us-letter",
  margin: (x: 1in, y: 1in), 
  numbering: "1",
  number-align: center,
  header: context {
    if counter(page).get().first() > 1 [
      #set text(9pt, fill: gray)
      #emph[FreeMoCap Movement-Building Worksheet]
      #h(1fr)
      #emph[Liberating Knowledge Production]
    ] 
  }
)

#set text(
  font: "New Computer Modern",
  size: 11pt,
  hyphenate: true,
)

#set par(
  justify: true,
  leading: 0.65em,
)

#set heading(numbering: "1.1")

#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  v(0.5em)
  block(
    fill: rgb("#1a1a2e"),
    width: 100%,
    inset: 16pt,
    radius: 4pt,
    [
      #set text(fill: white, weight: "bold", size: 16pt)
      #it.body
    ]
  )
  v(0.5em)
}

#show heading.where(level: 2): it => {
  v(0.8em)
  block(
    stroke: (left: 4pt + rgb("#e94560")),
    inset: (left: 12pt, y: 8pt),
    [
      #set text(fill: rgb("#1a1a2e"), weight: "bold", size: 13pt)
      #it.body
    ]
  )
  v(0.4em)
}

#show heading.where(level: 3): it => {
  v(0.5em)
  text(weight: "bold", size: 11pt, fill: rgb("#0f3460"))[#it.body]
  v(0.3em)
}

// Custom components
#let epigraph(quote, author) = {
  block(
    width: 100%,
    inset: (x: 2em, y: 1em),
    [
      #set text(style: "italic", size: 10.5pt)
      #quote
      #v(0.3em)
      #align(right)[— #author]
    ]
  )
}

#let callout(title, body, accent: rgb("#e94560")) = {
  block(
    width: 100%,
    fill: accent.lighten(90%),
    stroke: (left: 4pt + accent),
    inset: 12pt,
    radius: (right: 4pt),
    [
      #text(weight: "bold", fill: accent)[#title]
      #v(0.3em)
      #body
    ]
  )
}

#let worksheet-field(prompt, lines: 3) = {
  block(
    width: 100%,
    inset: (y: 0.5em),
    [
      #text(weight: "medium", fill: rgb("#333"))[#prompt]
      #v(0.3em)
      #block(
        width: 100%,
        height: lines * 1.5em,
        fill: rgb("#f8f9fa"),
        stroke: 1pt + rgb("#dee2e6"),
        radius: 4pt,
        inset: 8pt,
        []
      )
    ]
  )
}

#let completion-prompt(start) = {
  block(
    width: 100%,
    inset: (y: 0.3em),
    [
      #box(
        fill: rgb("#e9ecef"),
        inset: (x: 8pt, y: 4pt),
        radius: 3pt,
        [#text(style: "italic")[#start]]
      )
      #box(
        width: 1fr,
        stroke: (bottom: 1pt + rgb("#adb5bd")),
        inset: (bottom: 2pt),
        []
      )
    ]
  )
}

#let resource-link(title, url, description) = {
  block(
    width: 100%,
    inset: (y: 0.3em),
    [
      #link(url)[#text(fill: rgb("#0066cc"), weight: "medium")[#title]]
      #h(0.5em)
      #text(size: 9pt, fill: gray)[#description]
    ]
  )
}

// ============================================================================
// TITLE PAGE
// ============================================================================

#align(center)[
  #v(2fr)
  
  #block(
    width: 80%,
    [
      #text(size: 32pt, weight: "bold", fill: rgb("#1a1a2e"))[
        FreeMoCap as Counter-Hegemonic Project
      ]
      
      #v(1em)
      
      #line(length: 60%, stroke: 2pt + rgb("#e94560"))
      
      #v(1em)
      
      #text(size: 16pt, fill: rgb("#0f3460"))[
        A Strategic Worksheet for Liberating \ Knowledge, Education, and Science
      ]
    ]
  )
  
  #v(2em)
  
  #block(
    width: 70%,
    fill: rgb("#f8f9fa"),
    inset: 20pt,
    radius: 8pt,
    [
      #set text(size: 10pt, style: "italic")
      #set par(leading: 0.8em)
      
      "The great revolution in the history of man, past, present and future, is the revolution of those determined to be free."
      #align(right)[— *Toussaint Louverture*]
      
      #v(1em)
      
      "Information is power. But like all power, there are those who want to keep it for themselves."
      #align(right)[— *Aaron Swartz*]
      
      #v(1em)
      
      #set text(style: "normal", size: 9.5pt)
      *On tools:* The Haitian revolutionaries got their muskets from the French. They got their military tactics from the French. They got the language of universal liberty from the French Revolution — then held France accountable to ideals France never intended for them. Tools are not ideologically fixed to their origins. The code doesn't know who's running it. *Appropriate everything.*
    ]
  )
  
  #v(3fr)
  
  #text(size: 10pt, fill: gray)[
    Based on Jonathan Smucker's _Hegemony How-To_ and political organizing theory \
    Prepared for the FreeMoCap Foundation
  ]
  
  #v(1fr)
]

// ============================================================================
// TABLE OF CONTENTS
// ============================================================================

#pagebreak()

#align(center)[
  #text(size: 18pt, weight: "bold")[Contents]
]

#v(1em)

#outline(
  title: none,
  indent: 1.5em,
  depth: 2,
)

#v(2em)

#callout(
  "How to Use This Worksheet",
  [
    This worksheet is designed for both individual reflection and group discussion:
    
    + *Individual first pass:* Each core team member completes sections independently
    + *Compare and discuss:* Share responses and identify patterns, disagreements, tensions  
    + *Synthesize:* Develop shared answers that represent collective understanding
    + *Revisit quarterly:* These questions aren't "solved" once — return to them as the project evolves
    
    Set aside dedicated time. This isn't a 30-minute exercise — budget 2-3 hours for serious engagement with each major section.
  ],
  accent: rgb("#0f3460")
)

// ============================================================================
// FRAMING
// ============================================================================

#pagebreak()

#align(center)[
  #block(
    width: 90%,
    fill: rgb("#1a1a2e"),
    inset: 24pt,
    radius: 8pt,
    [
      #set text(fill: white)
      #text(size: 14pt, weight: "bold")[Framing: What Are We Actually Doing?]
      
      #v(1em)
      
      FreeMoCap the motion capture software is *Stage 1* — a concrete demonstration that:
      
      #v(0.5em)
      
      #set text(size: 10.5pt)
      - Research-grade scientific tools can be free, open, and accessible to everyone
      - You don't need a university affiliation to do real science
      - You don't need a \$200,000 budget to produce knowledge
      - The barriers are artificial, maintained by institutions that benefit from scarcity
      
      #v(1em)
      
      #text(size: 11pt)[
        The *actual project* is much larger: dismantling the current hegemony of knowledge production — the interlocking system of universities, academic journals, proprietary software, professional credentialism, and institutional gatekeeping that determines who gets to participate in science, education, and the creation of knowledge.
      ]
    ]
  )
]

// ============================================================================
// PART 1: MAPPING THE ENEMY
// ============================================================================

= Mapping the Enemy — The Current Hegemony

#epigraph(
  "Before you can overturn a hegemony, you need to understand it clearly. What are the structures you're fighting? How do they maintain power? What ideology justifies them?",
  "Strategic Principle"
)

== The Institutional Landscape

Map the interlocking institutions that control knowledge production:

#v(0.5em)

#table(
  columns: (1.2fr, 1.2fr, 1.5fr, 1.5fr),
  inset: 8pt,
  align: (left, left, left, left),
  fill: (col, row) => if row == 0 { rgb("#1a1a2e") } else if calc.odd(row) { rgb("#f8f9fa") } else { white },
  
  [#text(fill: white, weight: "bold", size: 9pt)[Institution]], 
  [#text(fill: white, weight: "bold", size: 9pt)[What it Controls]], 
  [#text(fill: white, weight: "bold", size: 9pt)[How it Maintains Control]], 
  [#text(fill: white, weight: "bold", size: 9pt)[Justifying Ideology]],
  
  [*Universities*], 
  [Access to education, research resources, credentials], 
  [Accreditation, degree requirements, tenure system], 
  [_"Expertise requires formal training"_],
  
  [*Academic Journals*], 
  [What counts as "real" knowledge], 
  [Peer review gatekeeping, impact factors, paywalls], 
  [_"Peer review ensures quality"_],
  
  [*Proprietary Software*], 
  [Tools for knowledge production], 
  [Licensing, prices, closed formats], 
  [_"Professional tools cost money"_],
  
  [*Professional Associations*], 
  [Who counts as "qualified"], 
  [Certifications, ethical codes as gatekeeping], 
  [_"Credentials protect the public"_],
  
  [*Funding Agencies*], 
  [What research gets done], 
  [Grant systems, overhead rates], 
  [_"Competitive funding ensures quality"_],
)

#v(1em)

*Add others you identify:*

#table(
  columns: (1fr, 1fr, 1fr, 1fr),
  inset: 10pt,
  rows: (auto, 2.5em, 2.5em, 2.5em),
  fill: (_, row) => if row == 0 { rgb("#e9ecef") } else { rgb("#f8f9fa") },
  
  [Institution], [What it Controls], [How it Maintains Control], [Justifying Ideology],
  [], [], [], [],
  [], [], [], [],
  [], [], [], [],
)

== The Hegemonic Common Sense

#callout(
  "Key Insight",
  [Hegemony works by making contingent arrangements seem natural and inevitable. What do people currently believe that serves this system?],
  accent: rgb("#e94560")
)

*Complete these sentences as a "normal person" embedded in current structures would:*

#completion-prompt("To be a real scientist, you need")
#completion-prompt("Research isn't valid unless")
#completion-prompt("Education requires")
#completion-prompt("If software/journals/education were free,")
#completion-prompt("People outside institutions can't do real research because")
#completion-prompt("We need universities because")

#v(1em)

#worksheet-field("Where did these beliefs come from? Who benefits from people believing them?", lines: 4)

== Cracks in the Edifice

No hegemony is total. Where is the current system failing?

#table(
  columns: (1.2fr, 1.2fr, 1.5fr),
  inset: 8pt,
  fill: (_, row) => if row == 0 { rgb("#1a1a2e") } else if calc.odd(row) { rgb("#f8f9fa") } else { white },
  
  [#text(fill: white, weight: "bold", size: 9pt)[System Failure]], 
  [#text(fill: white, weight: "bold", size: 9pt)[Who Experiences This?]], 
  [#text(fill: white, weight: "bold", size: 9pt)[What Do They Currently Blame?]],
  
  [Reproducibility crisis], [Researchers, public], [_"Bad actors," not systemic incentives_],
  [Student debt crisis], [Students, families], [_"Expensive schools," not credentialism itself_],
  [Journal paywalls], [Everyone outside elite institutions], [_"Greedy publishers," not the publication model_],
  [Adjunctification], [Early-career academics], [_"Budget cuts," not the tenure system_],
  [Research irrelevance], [Practitioners, public], [_"Ivory tower," not funding structures_],
  [Proprietary lock-in], [Researchers, educators], [_Specific vendors, not proprietary model_],
)

#v(0.5em)

#worksheet-field("Key question: These people are experiencing real problems with the system. How could you help them see the SYSTEMIC cause rather than blaming individuals or specific bad actors?", lines: 4)

== Who Benefits, Who Loses

#columns(2, gutter: 1.5em)[
  *Under the current system, who benefits?*
  
  #table(
    columns: (1fr, 1.5fr),
    inset: 6pt,
    fill: (_, row) => if row == 0 { rgb("#c9ffc9") } else { rgb("#f0fff0") },
    [*Who*], [*How*],
    [Tenured faculty at elite institutions], [],
    [Academic publishers], [],
    [Proprietary software companies], [],
    [], [],
    [], [],
  )
  
  #colbreak()
  
  *Who loses?*
  
  #table(
    columns: (1fr, 1.5fr),
    inset: 6pt,
    fill: (_, row) => if row == 0 { rgb("#ffc9c9") } else { rgb("#fff0f0") },
    [*Who*], [*How*],
    [Students (debt, limited access)], [],
    [Adjuncts and contingent faculty], [],
    [Under-resourced institutions], [],
    [Global South academics], [],
    [Independent researchers], [],
    [The public], [],
  )
]

#v(1em)

#callout(
  "Critical Question",
  [The people who lose vastly outnumber those who benefit. *Why hasn't the system already changed?*],
  accent: rgb("#e94560")
)

#worksheet-field("Your analysis:", lines: 4)

// ============================================================================
// PART 2: THE COUNTER-HEGEMONIC VISION
// ============================================================================

= The Counter-Hegemonic Vision

#epigraph(
  "What new 'common sense' are you trying to create? What does the liberated landscape look like?",
  "Strategic Question"
)

== The World We're Building

*Complete these sentences as someone living in the world FreeMoCap is building:*

#completion-prompt("Anyone can do real science because")
#completion-prompt("I learned [skill/knowledge] by")
#completion-prompt("When I need research tools, I")
#completion-prompt("Knowledge is validated by")
#completion-prompt("Education happens")
#completion-prompt("My work is valued because..., not because I have credentials from")

== Core Principles of the New Hegemony

What are the foundational beliefs of the world you're building?

#block(
  fill: rgb("#f8f9fa"),
  inset: 16pt,
  radius: 8pt,
  width: 100%,
  [
    *Draft 5-7 core principles:*
    
    #v(0.5em)
    
    #for i in range(1, 8) {
      [#i. #box(width: 1fr, stroke: (bottom: 1pt + rgb("#dee2e6")), inset: (bottom: 4pt), [])]
      v(1em)
    }
  ]
)

#v(1em)

For each principle, you'll need to articulate:
- *Why it's true* (the positive case)
- *What current belief it displaces*
- *What changes if people accept it*

== Prefigurative Politics

#callout(
  "Definition",
  [*Prefigurative politics* means embodying the future you want to create in how you organize now. FreeMoCap should BE the proof that another way is possible.],
  accent: rgb("#0f3460")
)

#table(
  columns: (1fr, 2fr),
  inset: 10pt,
  fill: (_, row) => if row == 0 { rgb("#1a1a2e") } else { rgb("#f8f9fa") },
  
  [#text(fill: white, weight: "bold")[Principle]], 
  [#text(fill: white, weight: "bold")[How FreeMoCap Demonstrates This NOW]],
  
  [], [],
  [], [],
  [], [],
  [], [],
)

#v(0.5em)

#worksheet-field("Where does FreeMoCap fall short of its own principles? (Be honest)", lines: 3)

#worksheet-field("What would it look like to more fully embody these principles?", lines: 3)

// ============================================================================
// PART 3: THEORY OF CHANGE
// ============================================================================

= Theory of Change — How Hegemonies Fall

#epigraph(
  "Smucker is clear: being right isn't enough. You need a plausible theory of how the current system gets replaced by yours.",
  "Strategic Principle"
)

== Historical Models

#table(
  columns: (1fr, 1.2fr, 1.5fr, 1.5fr),
  inset: 8pt,
  fill: (_, row) => if row == 0 { rgb("#1a1a2e") } else if calc.odd(row) { rgb("#f8f9fa") } else { white },
  
  [#text(fill: white, weight: "bold", size: 9pt)[Movement/Project]], 
  [#text(fill: white, weight: "bold", size: 9pt)[Hegemony Challenged]], 
  [#text(fill: white, weight: "bold", size: 9pt)[How They Won]], 
  [#text(fill: white, weight: "bold", size: 9pt)[Lessons for FreeMoCap]],
  
  [Free Software Movement], 
  [Proprietary software as default], 
  [Built viable alternatives, created licensing infrastructure, changed developer culture],
  [],
  
  [Open Access Movement], 
  [Journal paywalls], 
  [Mandates, repositories, demonstrated demand, Sci-Hub as civil disobedience],
  [],
  
  [Wikipedia], 
  [Expert-only encyclopedias], 
  [Just built it, proved it worked, became too useful to ignore],
  [],
  
  [Linux], 
  [Microsoft/proprietary OS hegemony], 
  [Server dominance first, enterprise adoption, Android],
  [],
)

#worksheet-field("What do successful counter-hegemonic projects have in common?", lines: 3)

== Your Theory of Change

#block(
  fill: rgb("#e9ecef"),
  inset: 16pt,
  radius: 8pt,
  [
    Complete this theory of change:
    
    #v(0.5em)
    
    *If* FreeMoCap #box(width: 1fr, stroke: (bottom: 1pt + rgb("#adb5bd")), [])
    
    #v(0.8em)
    
    *Then* [constituency] will #box(width: 1fr, stroke: (bottom: 1pt + rgb("#adb5bd")), [])
    
    #v(0.8em)
    
    *Which will cause* [institutional change] #box(width: 1fr, stroke: (bottom: 1pt + rgb("#adb5bd")), [])
    
    #v(0.8em)
    
    *Leading to* [broader shift] #box(width: 1fr, stroke: (bottom: 1pt + rgb("#adb5bd")), [])
    
    #v(0.8em)
    
    *Until eventually* [new hegemony] #box(width: 1fr, stroke: (bottom: 1pt + rgb("#adb5bd")), [])
  ]
)

#v(1em)

#worksheet-field("What are the key assumptions in this theory? What has to be true for it to work?", lines: 4)

== The Stages

If FreeMoCap motion capture is Stage 1, what are the subsequent stages?

#table(
  columns: (0.5fr, 1fr, 1fr, 1.2fr, 1.2fr),
  inset: 8pt,
  fill: (_, row) => if row == 0 { rgb("#1a1a2e") } else if row == 1 { rgb("#e9ecef") } else { rgb("#f8f9fa") },
  
  [#text(fill: white, weight: "bold", size: 9pt)[Stage]], 
  [#text(fill: white, weight: "bold", size: 9pt)[Focus]], 
  [#text(fill: white, weight: "bold", size: 9pt)[Goal]], 
  [#text(fill: white, weight: "bold", size: 9pt)[Success Looks Like]], 
  [#text(fill: white, weight: "bold", size: 9pt)[Enables Next Stage By...]],
  
  [*1*], [Motion capture], [Prove FOSS can match proprietary], [Adoption in labs, citations], [Builds credibility, community],
  [*2*], [], [], [], [],
  [*3*], [], [], [], [],
  [*4*], [], [], [], [],
  [*5*], [], [], [], [],
)

#v(0.5em)

*What capabilities/resources/credibility do you need to build at each stage?*

#completion-prompt("Stage 1 → 2 requires:")
#completion-prompt("Stage 2 → 3 requires:")
#completion-prompt("Stage 3 → 4 requires:")

== Multiple Fronts

Counter-hegemonic projects usually require pressure on multiple fronts simultaneously.

#table(
  columns: (1fr, 1.2fr, 1.2fr, 1fr),
  inset: 8pt,
  fill: (_, row) => if row == 0 { rgb("#1a1a2e") } else if calc.odd(row) { rgb("#f8f9fa") } else { white },
  
  [#text(fill: white, weight: "bold", size: 9pt)[Front]], 
  [#text(fill: white, weight: "bold", size: 9pt)[What Victory Looks Like]], 
  [#text(fill: white, weight: "bold", size: 9pt)[Who's Already Fighting Here?]], 
  [#text(fill: white, weight: "bold", size: 9pt)[FreeMoCap's Role]],
  
  [*Tools* (FOSS research software)], [FOSS default for research], [NumPy, R, Jupyter, etc.], [Active combatant],
  [*Publishing* (Open Access)], [Paywalls gone, new validation], [PLOS, arXiv, Sci-Hub], [?],
  [*Education* (alt credentials)], [Degrees not required], [MOOCs, bootcamps], [?],
  [*Funding* (alt models)], [Research funded outside grants], [Crowdfunding, citizen science], [?],
  [*Community* (indie research)], [Legitimate research outside academy], [Indie researchers], [?],
)

#worksheet-field("Where should FreeMoCap focus? Where should it build alliances?", lines: 3)

// ============================================================================
// PART 4: PUBLIC NARRATIVE
// ============================================================================

= The Public Narrative

#epigraph(
  "Your narrative must serve the LARGER project, not just the motion capture software.",
  "Strategic Principle"
)

#callout(
  "Marshall Ganz's Framework",
  [
    *Story of Self* → Why YOU? What choice led you here? \
    *Story of Us* → Who is WE? What binds us together? \
    *Story of Now* → Why NOW? What's the urgent ask?
  ],
  accent: rgb("#0f3460")
)

== Story of Self

*Why are YOU, Jon, fighting to liberate knowledge production?*

#worksheet-field("The Encounter: When did you first experience the injustice of the current system? What specific moment showed you something was wrong?", lines: 4)

#worksheet-field("The Choice: What moment of choice committed you to this fight? (Not a gradual drift — a moment when you could have done otherwise but chose this.)", lines: 4)

#worksheet-field("The Cost: What have you given up or risked by making this choice? (Sacrifice demonstrates commitment and values.)", lines: 3)

#worksheet-field("The Values: What deep values drive this work? Not 'open source is good' but the VALUES underneath — justice? freedom? democracy? human flourishing?", lines: 3)

#block(
  fill: rgb("#fff3cd"),
  stroke: 1pt + rgb("#ffc107"),
  inset: 12pt,
  radius: 4pt,
  [
    *Draft your Story of Self (3-4 sentences, conversational):*
    #v(0.5em)
    #block(height: 4em, width: 100%, fill: white, stroke: 1pt + rgb("#dee2e6"), radius: 4pt, [])
  ]
)

== Story of Us

*Who is the "we" fighting for liberated knowledge? This must be MUCH bigger than "FreeMoCap users."*

#block(
  fill: rgb("#f8f9fa"),
  inset: 12pt,
  radius: 4pt,
  [
    *The broadest possible "we" — who has been harmed by or excluded from the current knowledge system?*
    
    - Students crushed by debt for credentials that gatekeep knowledge
    - Researchers at under-resourced institutions  
    - Global South academics locked out by paywalls and equipment costs
    - Independent researchers dismissed as "not real scientists"
    - Practitioners who can't access research relevant to their work
    - Curious people told "you're not qualified to understand this"
    - #box(width: 1fr, stroke: (bottom: 1pt + rgb("#dee2e6")), [])
    - #box(width: 1fr, stroke: (bottom: 1pt + rgb("#dee2e6")), [])
  ]
)

#completion-prompt("The shared experience — what do all these people have in common?")

#completion-prompt("The shared enemy (not 'universities' — the SYSTEM, the ideology):")

#completion-prompt("The shared vision — what world are 'we' building together?")

#block(
  fill: rgb("#fff3cd"),
  stroke: 1pt + rgb("#ffc107"),
  inset: 12pt,
  radius: 4pt,
  [
    *Draft your Story of Us (3-4 sentences):*
    #v(0.5em)
    #block(height: 4em, width: 100%, fill: white, stroke: 1pt + rgb("#dee2e6"), radius: 4pt, [])
  ]
)

== Story of Now

*Why is THIS MOMENT critical?*

#worksheet-field("What's happening RIGHT NOW that creates opportunity or urgency? (AI democratizing/concentrating capabilities, reproducibility crisis, student debt crisis, pandemic lessons, institutional distrust, climate crisis...)", lines: 4)

#worksheet-field("What window is closing? What opportunity will we lose if we don't act?", lines: 3)

*The specific ask (for different audiences):*

#table(
  columns: (1fr, 2fr),
  inset: 10pt,
  fill: (_, row) => if row == 0 { rgb("#1a1a2e") } else { rgb("#f8f9fa") },
  
  [#text(fill: white, weight: "bold")[Audience]], 
  [#text(fill: white, weight: "bold")[What Do You Want Them to DO?]],
  
  [Someone experiencing the system's failures], [],
  [A potential contributor], [],
  [A potential ally organization], [],
  [Someone with resources], [],
  [Someone with platform/influence], [],
)

== The Integrated Narrative

#block(
  fill: rgb("#e8f4ea"),
  stroke: 2pt + rgb("#28a745"),
  inset: 16pt,
  radius: 8pt,
  [
    *Weave them together. This should take 3-5 minutes to tell. Practice out loud.*
    
    #v(0.5em)
    
    *[Story of Self — your encounter with injustice, your choice, your values]*
    #block(height: 3em, width: 100%, fill: white, stroke: 1pt + rgb("#dee2e6"), radius: 4pt, [])
    
    #v(0.5em)
    #align(center)[_"And I discovered I wasn't alone..."_]
    #v(0.5em)
    
    *[Story of Us — the shared experience, the shared enemy, the shared vision]*
    #block(height: 3em, width: 100%, fill: white, stroke: 1pt + rgb("#dee2e6"), radius: 4pt, [])
    
    #v(0.5em)
    #align(center)[_"And right now, we face a critical moment..."_]
    #v(0.5em)
    
    *[Story of Now — the urgency, the opportunity, the ask]*
    #block(height: 3em, width: 100%, fill: white, stroke: 1pt + rgb("#dee2e6"), radius: 4pt, [])
    
    #v(0.5em)
    #align(center)[*"That's why I'm asking you to..."*]
    #v(0.5em)
    
    #block(height: 2em, width: 100%, fill: rgb("#fff3cd"), stroke: 1pt + rgb("#ffc107"), radius: 4pt, [])
  ]
)

// ============================================================================
// PART 5: ALLIANCE MAPPING
// ============================================================================

= Alliance Mapping

#epigraph(
  "You're not fighting alone. Many movements share pieces of this vision. Who are your allies?",
  "Strategic Principle"
)

== Allied Movements

#table(
  columns: (1fr, 1.2fr, 1.2fr, 1.5fr),
  inset: 7pt,
  fill: (_, row) => if row == 0 { rgb("#1a1a2e") } else if calc.odd(row) { rgb("#f8f9fa") } else { white },
  
  [#text(fill: white, weight: "bold", size: 8pt)[Movement]], 
  [#text(fill: white, weight: "bold", size: 8pt)[What They Fight For]], 
  [#text(fill: white, weight: "bold", size: 8pt)[Overlap with FreeMoCap]], 
  [#text(fill: white, weight: "bold", size: 8pt)[Key Organizations]],
  
  [Free Software], [Software freedom], [FOSS as default, anti-proprietary], [FSF, SFLC],
  [Open Access], [Free access to research], [Against paywalls, open publishing], [SPARC, PLOS],
  [Open Science], [Reproducibility, transparency], [Open tools, data, methods], [COS, FOSTER],
  [Right to Repair], [Ownership of technology], [Against proprietary lock-in], [iFixit, Repair.org],
  [Citizen Science], [Public participation in research], [Research outside institutions], [SciStarter],
  [Hacker Culture], [Information wants to be free], [Tool-building, sharing knowledge], [Hackerspaces, CCC],
  [Library Movement], [Public access to knowledge], [Against information enclosure], [ALA, Internet Archive],
)

== Potential Organizational Allies

#table(
  columns: (1.2fr, 1.5fr, 1fr, 1fr),
  inset: 8pt,
  fill: (_, row) => if row == 0 { rgb("#1a1a2e") } else { rgb("#f8f9fa") },
  
  [#text(fill: white, weight: "bold", size: 9pt)[Organization]], 
  [#text(fill: white, weight: "bold", size: 9pt)[What They Do]], 
  [#text(fill: white, weight: "bold", size: 9pt)[Alliance Potential]], 
  [#text(fill: white, weight: "bold", size: 9pt)[Who Do You Know There?]],
  
  [Software Freedom Conservancy], [], [], [],
  [Internet Archive], [], [], [],
  [Electronic Frontier Foundation], [], [], [],
  [Mozilla Foundation], [], [], [],
  [Wikimedia Foundation], [], [], [],
  [NumFOCUS], [], [], [],
  [Center for Open Science], [], [], [],
)

== Intellectual Lineages

What thinkers/traditions inform this work?

#table(
  columns: (1fr, 2fr, 1.5fr),
  inset: 8pt,
  fill: (_, row) => if row == 0 { rgb("#1a1a2e") } else if calc.odd(row) { rgb("#f8f9fa") } else { white },
  
  [#text(fill: white, weight: "bold", size: 9pt)[Thinker/Tradition]], 
  [#text(fill: white, weight: "bold", size: 9pt)[Key Ideas]], 
  [#text(fill: white, weight: "bold", size: 9pt)[How It Informs FreeMoCap]],
  
  [Ivan Illich], [Deschooling, convivial tools, institutional critique], [],
  [Aaron Swartz], [Information liberation, guerrilla open access], [],
  [Richard Stallman], [Free software as freedom, not just price], [],
  [Paulo Freire], [Critical pedagogy, education as liberation], [],
  [Yochai Benkler], [Commons-based peer production], [],
  [Elinor Ostrom], [Governance of commons], [],
)

== Building Alliances

*For your top 5 potential allies, develop an approach:*

#table(
  columns: (0.8fr, 1.2fr, 1.2fr, 1.5fr),
  inset: 8pt,
  fill: (_, row) => if row == 0 { rgb("#1a1a2e") } else { rgb("#f8f9fa") },
  
  [#text(fill: white, weight: "bold", size: 9pt)[Ally]], 
  [#text(fill: white, weight: "bold", size: 9pt)[What You Offer Them]], 
  [#text(fill: white, weight: "bold", size: 9pt)[What You Need From Them]], 
  [#text(fill: white, weight: "bold", size: 9pt)[First Step]],
  
  [1.], [], [], [],
  [2.], [], [], [],
  [3.], [], [], [],
  [4.], [], [], [],
  [5.], [], [], [],
)

// ============================================================================
// PART 6: ORGANIZING FOR THE LONG HAUL
// ============================================================================

= Organizing for the Long Haul

#epigraph(
  "Counter-hegemonic projects take decades. How do you build an organization that can sustain this?",
  "Strategic Question"
)

== The FreeMoCap Foundation as Vehicle

*Is the FreeMoCap Foundation the right organizational vehicle for the larger vision?*

#table(
  columns: (1fr, 1.5fr, 1.5fr),
  inset: 10pt,
  fill: (_, row) => if row == 0 { rgb("#1a1a2e") } else { rgb("#f8f9fa") },
  
  [#text(fill: white, weight: "bold")[Consideration]], 
  [#text(fill: white, weight: "bold")[Current State]], 
  [#text(fill: white, weight: "bold")[What's Needed for Larger Vision]],
  
  [Legal structure], [501(c)(3)], [],
  [Name/brand], ["FreeMoCap" = motion capture], [],
  [Mission statement], [], [],
  [Governance], [], [],
)

#v(0.5em)

#callout(
  "Critical Question",
  [Should there be a broader organizational entity that FreeMoCap is one project *within*?],
  accent: rgb("#e94560")
)

#worksheet-field("Your thinking:", lines: 4)

== Developing Leadership

#block(
  fill: rgb("#f0f0f0"),
  inset: 12pt,
  radius: 4pt,
  [
    #text(style: "italic")[
      "Strong people don't need a strong leader." — *Ella Baker*
    ]
  ]
)

#v(0.5em)

*What leadership roles will you need that don't exist yet?*

#for i in range(1, 4) {
  [#i. #box(width: 1fr, stroke: (bottom: 1pt + rgb("#dee2e6")), inset: (bottom: 4pt), [])]
  v(0.8em)
}

#worksheet-field("How do people BECOME leaders in your organization? (Make this explicit)", lines: 3)

== Organizational Culture

#table(
  columns: (1.2fr, 2fr, 0.8fr),
  inset: 8pt,
  fill: (_, row) => if row == 0 { rgb("#1a1a2e") } else { rgb("#f8f9fa") },
  
  [#text(fill: white, weight: "bold")[Value]], 
  [#text(fill: white, weight: "bold")[What It Looks Like in Practice]], 
  [#text(fill: white, weight: "bold")[Current State (1-10)]],
  
  [Radical accessibility], [], [],
  [Distributed leadership], [], [],
  [Long-term thinking], [], [],
  [Solidarity with allied movements], [], [],
  [Prefigurative practice], [], [],
)

#v(0.5em)

*Cultural patterns to AVOID:*
- Founder dependency
- Insider/outsider dynamics
- Technical elitism
- Burnout/martyrdom culture
- Purity politics
- Short-term thinking

#worksheet-field("Which of these are you most at risk for?", lines: 3)

// ============================================================================
// PART 7: STRATEGIC QUESTIONS
// ============================================================================

= Strategic Questions to Keep Asking

#epigraph(
  "These aren't one-time questions. Return to them regularly.",
  "Ongoing Practice"
)

== The Smucker Questions

#callout(
  "Ask yourself monthly:",
  [],
  accent: rgb("#e94560")
)

#block(
  fill: rgb("#f8f9fa"),
  inset: 16pt,
  radius: 8pt,
  [
    #set text(size: 10.5pt)
    
    *"Is what we're doing likely to advance our mission, or does it primarily express our identity as [open source developers / academics / hackers / activists]?"*
    
    #block(height: 2.5em, width: 100%, fill: white, stroke: 1pt + rgb("#dee2e6"), radius: 4pt, inset: 6pt, [])
    
    #v(1em)
    
    *"Are we building power, or are we performing righteousness?"*
    
    #block(height: 2.5em, width: 100%, fill: white, stroke: 1pt + rgb("#dee2e6"), radius: 4pt, inset: 6pt, [])
    
    #v(1em)
    
    *"Who are we bringing IN to this work who wasn't here before? Or are we just activating the already-convinced?"*
    
    #block(height: 2.5em, width: 100%, fill: white, stroke: 1pt + rgb("#dee2e6"), radius: 4pt, inset: 6pt, [])
    
    #v(1em)
    
    *"What have we WON recently? What concrete victory can we point to?"*
    
    #block(height: 2.5em, width: 100%, fill: white, stroke: 1pt + rgb("#dee2e6"), radius: 4pt, inset: 6pt, [])
  ]
)

== The Scale Questions

#block(
  fill: rgb("#e8f4ea"),
  inset: 16pt,
  radius: 8pt,
  [
    *"Is what we're doing now building toward the larger vision, or are we getting stuck at Stage 1?"*
    #block(height: 2em, width: 100%, fill: white, stroke: 1pt + rgb("#dee2e6"), radius: 4pt, [])
    
    #v(0.8em)
    
    *"Are we building the organizational capacity to do MORE than motion capture software?"*
    #block(height: 2em, width: 100%, fill: white, stroke: 1pt + rgb("#dee2e6"), radius: 4pt, [])
    
    #v(0.8em)
    
    *"Are we connecting with allied movements, or operating in isolation?"*
    #block(height: 2em, width: 100%, fill: white, stroke: 1pt + rgb("#dee2e6"), radius: 4pt, [])
  ]
)

== The Sustainability Questions

#block(
  fill: rgb("#fff3cd"),
  inset: 16pt,
  radius: 8pt,
  [
    *"Can this continue without Jon?"*
    #block(height: 2em, width: 100%, fill: white, stroke: 1pt + rgb("#dee2e6"), radius: 4pt, [])
    
    #v(0.8em)
    
    *"What happens if a key contributor burns out or leaves?"*
    #block(height: 2em, width: 100%, fill: white, stroke: 1pt + rgb("#dee2e6"), radius: 4pt, [])
    
    #v(0.8em)
    
    *"Are we moving at a sustainable pace?"*
    #block(height: 2em, width: 100%, fill: white, stroke: 1pt + rgb("#dee2e6"), radius: 4pt, [])
  ]
)

// ============================================================================
// PART 8: IMMEDIATE ACTIONS
// ============================================================================

= Immediate Actions

#epigraph(
  "Strategy without action is fantasy. What are you doing THIS MONTH?",
  "Call to Action"
)

== Top Priorities for Next 90 Days

#table(
  columns: (0.5fr, 1.5fr, 1.5fr, 0.8fr, 0.8fr),
  inset: 8pt,
  fill: (_, row) => if row == 0 { rgb("#1a1a2e") } else { rgb("#f8f9fa") },
  
  [#text(fill: white, weight: "bold", size: 9pt)[\#]], 
  [#text(fill: white, weight: "bold", size: 9pt)[Priority]], 
  [#text(fill: white, weight: "bold", size: 9pt)[First Concrete Step]], 
  [#text(fill: white, weight: "bold", size: 9pt)[Deadline]], 
  [#text(fill: white, weight: "bold", size: 9pt)[Owner]],
  
  [1], [], [], [], [],
  [2], [], [], [], [],
  [3], [], [], [], [],
)

== What You're NOT Doing

#callout(
  "Strategy means choosing",
  [What are you explicitly deprioritizing?],
  accent: rgb("#6c757d")
)

#for i in range(1, 4) {
  [#i. #box(width: 0.6fr, stroke: (bottom: 1pt + rgb("#dee2e6")), []) _(Why:_ #box(width: 0.3fr, stroke: (bottom: 1pt + rgb("#dee2e6")), [])_)_]
  v(0.8em)
}

== Accountability

#columns(2)[
  *Who will you share this with?*
  #block(height: 2em, width: 100%, fill: rgb("#f8f9fa"), stroke: 1pt + rgb("#dee2e6"), radius: 4pt, [])
  
  #colbreak()
  
  *When will you review progress?*
  - 30-day check-in: #box(width: 1fr, stroke: (bottom: 1pt + rgb("#dee2e6")), [])
  - 90-day review: #box(width: 1fr, stroke: (bottom: 1pt + rgb("#dee2e6")), [])
]

// ============================================================================
// PART 9: READING & RESOURCES
// ============================================================================

= Reading & Resources

== Core Strategic Reading

#block(
  fill: rgb("#f8f9fa"),
  inset: 16pt,
  radius: 8pt,
  [
    === Tier 1: Essential
    
    #resource-link(
      "Hegemony How-To: A Roadmap for Radicals",
      "https://www.akpress.org/hegemony-how-to.html",
      "Jonathan Smucker — Core strategic framework"
    )
    
    #resource-link(
      "Deschooling Society",
      "https://www.arvindguptatoys.com/arvindgupta/DESCHOOLING.pdf",
      "Ivan Illich — Foundational critique of institutional education"
    )
    
    #resource-link(
      "Tools for Conviviality",
      "https://www.davidtinapple.com/illich/1973_tools_for_conviviality.pdf",
      "Ivan Illich — Technology that liberates rather than dominates"
    )
    
    #resource-link(
      "No Shortcuts: Organizing for Power",
      "https://www.janemcalevey.com/no-shortcuts",
      "Jane McAlevey — Organizing vs. mobilizing"
    )
    
    #resource-link(
      "Working in Public",
      "https://press.stripe.com/working-in-public",
      "Nadia Eghbal — Open source sustainability and community"
    )
    
    #v(1em)
    
    === Tier 2: Deepening
    
    #resource-link(
      "Pedagogy of the Oppressed",
      "https://envs.ucsc.edu/internships/internship-readings/freire-pedagogy-of-the-oppressed.pdf",
      "Paulo Freire — Education as liberation"
    )
    
    #resource-link(
      "Pedagogy of Hope",
      "https://archive.org/details/pedagogy-of-hope-reliving-pedagogy-of-the-oppressed",
      "Paulo Freire — Hope as ontological necessity"
    )
    
    #resource-link(
      "Emergent Strategy",
      "https://www.akpress.org/emergentstrategy.html",
      "adrienne maree brown — Adaptive organizing"
    )
    
    #resource-link(
      "The Wealth of Networks",
      "https://www.benkler.org/Benkler_Wealth_Of_Networks.pdf",
      "Yochai Benkler — Commons-based peer production"
    )
    
    #resource-link(
      "Guerrilla Open Access Manifesto",
      "https://archive.org/details/GuesrillaOpenAccessManifesto",
      "Aaron Swartz — Information liberation ethics"
    )
  ]
)

== Key Concepts Quick Reference

#table(
  columns: (1fr, 2.5fr),
  inset: 10pt,
  fill: (_, row) => if row == 0 { rgb("#1a1a2e") } else if calc.odd(row) { rgb("#f8f9fa") } else { white },
  
  [#text(fill: white, weight: "bold")[Term]], 
  [#text(fill: white, weight: "bold")[Definition & Application]],
  
  [*Hegemony*], 
  [Making your values become the "common sense" of society. FreeMoCap aims to make "motion capture should be free/accessible" into common sense.],
  
  [*Political Identity Paradox*], 
  [Strong group identity enables commitment but creates insularity. Balance community cohesion with outward focus.],
  
  [*Expressive vs. Strategic*], 
  [Acting to express identity vs. acting to achieve outcomes. Prioritize actions that advance mission over actions that feel good.],
  
  [*Organizing vs. Mobilizing*], 
  [Mobilizing activates existing supporters; organizing expands your base by reaching non-activists.],
  
  [*Conscientização*], 
  [Paulo Freire's term for developing critical consciousness — moving from fatalism to understanding systemic causes to taking action.],
  
  [*Prefigurative Politics*], 
  [Embodying the future you want to create in how you organize now. FreeMoCap should BE proof another way is possible.],
)

// ============================================================================
// PART 10: THE VISION DOCUMENT
// ============================================================================

= The Vision Document

#epigraph(
  "After working through this worksheet, draft a 1-page vision document that articulates the full scope of what FreeMoCap is building toward. This becomes your north star.",
  "Final Synthesis"
)

#block(
  stroke: 2pt + rgb("#1a1a2e"),
  inset: 20pt,
  radius: 8pt,
  [
    #align(center)[
      #text(size: 14pt, weight: "bold")[FREEMOCAP VISION DOCUMENT]
      #v(0.3em)
      #text(size: 10pt, fill: gray)[DRAFT]
    ]
    
    #v(1em)
    
    *THE PROBLEM*
    #block(height: 4em, width: 100%, fill: rgb("#f8f9fa"), stroke: 1pt + rgb("#dee2e6"), radius: 4pt, inset: 8pt, [])
    
    #v(1em)
    
    *THE VISION*
    #block(height: 4em, width: 100%, fill: rgb("#f8f9fa"), stroke: 1pt + rgb("#dee2e6"), radius: 4pt, inset: 8pt, [])
    
    #v(1em)
    
    *THE THEORY OF CHANGE*
    #block(height: 4em, width: 100%, fill: rgb("#f8f9fa"), stroke: 1pt + rgb("#dee2e6"), radius: 4pt, inset: 8pt, [])
    
    #v(1em)
    
    *THE CURRENT STAGE*
    #block(height: 3em, width: 100%, fill: rgb("#f8f9fa"), stroke: 1pt + rgb("#dee2e6"), radius: 4pt, inset: 8pt, [])
    
    #v(1em)
    
    *THE CALL*
    #block(height: 3em, width: 100%, fill: rgb("#fff3cd"), stroke: 1pt + rgb("#ffc107"), radius: 4pt, inset: 8pt, [])
  ]
)

// ============================================================================
// CLOSING
// ============================================================================

#pagebreak()

#align(center)[
  #v(3fr)
  
  #block(
    width: 80%,
    fill: rgb("#1a1a2e"),
    inset: 24pt,
    radius: 8pt,
    [
      #set text(fill: white)
      
      #text(size: 14pt, weight: "bold")[
        This is a living document.
      ]
      
      #v(1em)
      
      #set text(size: 11pt)
      The work of building counter-hegemonic power is never complete. Return to these questions. Revise your answers. Share them with co-conspirators. Build the infrastructure for a long fight.
      
      #v(1em)
      
      The current system wasn't built in a day. It won't fall in a day.
      
      #v(0.5em)
      
      #text(size: 14pt, weight: "bold")[
        But it WILL fall.
      ]
    ]
  )
  
  #v(3fr)
  
  #line(length: 40%, stroke: 1pt + rgb("#dee2e6"))
  
  #v(1em)
  
  #text(size: 9pt, fill: gray)[
    FreeMoCap Foundation \
    #link("https://freemocap.org")[freemocap.org] · #link("https://github.com/freemocap")[github.com/freemocap]
    
    #v(0.5em)
    
    Based on frameworks from Jonathan Smucker, Paulo Freire, Jane McAlevey, \ Marshall Ganz, Ivan Illich, adrienne maree brown, and others.
  ]
  
  #v(2fr)
]
