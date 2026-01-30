#set document(
  title: "Hegemony and Paradigm: How Gramsci Illuminates Kuhn and Vice Versa",
  author: "Research Report",
  date: datetime.today(),
)

#set page(
  paper: "us-letter",
  margin: (x: 1.25in, y: 1in),
  numbering: "1",
  header: align(right)[_Hegemony and Paradigm_],
)

#set text(
  font: "New Computer Modern", 
  size: 11pt,
)

#set par(
  justify: true,
  leading: 0.65em,
)

#set heading(numbering: "1.1")

#show heading.where(level: 1): it => block(
  above: 1.5em,
  below: 1em,
  text(size: 14pt, weight: "bold", it)
)

#show heading.where(level: 2): it => block(
  above: 1.2em,
  below: 0.8em,
  text(size: 12pt, weight: "bold", it)
)

// Title
#align(center)[
  #block(text(size: 20pt, weight: "bold")[
    Hegemony and Paradigm
  ])
  #v(0.5em)
  #block(text(size: 14pt)[
    How Gramsci Illuminates Kuhn and Vice Versa
  ])
  #v(1em)
  #block(text(size: 11pt, style: "italic")[
    A Comparative Analysis of Consent, Crisis, and Revolutionary Transformation
  ])
  #v(2em)
]

// Abstract
#block(
  fill: luma(240),
  inset: 1em,
  radius: 4pt,
  width: 100%,
)[
  #text(weight: "bold")[Abstract:]
  Antonio Gramsci's theory of hegemony and Thomas Kuhn's philosophy of scientific revolutions share profound structural parallels that have been recognized by scholars in Marxist science studies, feminist epistemology, and Science and Technology Studies---though explicit comparative work remains surprisingly sparse. Both frameworks describe how dominant systems achieve stability through *naturalization of "common sense"* rather than coercion, accumulate internal contradictions that produce crisis, and undergo revolutionary ruptures that transform not just content but the very categories through which reality is understood. These parallels offer strategic insights for contemporary leftist organizing: building counter-hegemonic institutions requires the patient, long-term "war of position" that both thinkers, in their distinct domains, identify as prerequisite to transformational change.
]

#v(1em)

= Gramsci's Hegemony: Power Through Consent

Gramsci developed his theory of hegemony in the _Prison Notebooks_ (1929--1935), grappling with why the socialist revolutions that swept Russia in 1917 failed to materialize in Western Europe @gramsci1971. His answer centered on *civil society*---the dense network of schools, churches, media, trade unions, and cultural institutions that in advanced capitalist societies provide "fortifications and earthworks" behind the state. Unlike liberal conceptions of civil society as a neutral associational sphere, Gramsci understood it as the terrain where ruling-class ideological dominance is manufactured and maintained @eir2012.

*Hegemony* describes the process through which a dominant class establishes "intellectual and moral leadership" over allied and subordinate groups, securing their _consent_ to arrangements that serve ruling-class interests. As Gramsci wrote, the state equals "political society + civil society, in other words hegemony protected by the armor of coercion" @gramsci1971. This distinguishes hegemony from mere domination: the hegemon must sacrifice some narrow corporate interests, make compromises, and frame its particular agenda as serving universal values @emory2014. Perry Anderson's landmark essay "The Antinomies of Antonio Gramsci" (1976) traced how this concept transformed classical Marxism's understanding of the relationship between economic base and ideological superstructure @anderson1976 @anderson2017.

The concept of *common sense* (_senso comune_) captures how hegemony operates epistemologically. Common sense comprises the incoherent, contradictory, taken-for-granted assumptions through which ordinary people understand their world---assumptions shaped by ruling-class ideology but experienced as natural, timeless truths @femia1981. Gramsci's educational project aimed not to impose abstract philosophy from above but to work within common sense, extracting its rational kernel ("good sense") and elaborating it into coherent counter-hegemonic consciousness @sassoon1987.

*Organic intellectuals* are central to this project. Unlike traditional intellectuals who imagine themselves autonomous from class interests, organic intellectuals emerge from specific social classes and articulate their worldview @boggs1976. They "do not simply describe social life in accordance with scientific rules but instead articulate, through the language of culture, the feelings and experiences which the masses could not express for themselves" @thomas2009book. The construction of counter-hegemony requires developing organic intellectuals from the working class while winning over traditional intellectuals to the revolutionary cause.

The *historical bloc* (_blocco storico_) names the composite of class forces, institutional arrangements, and ideological formations unified under hegemonic leadership. Gramsci borrowed this term from Georges Sorel to replace the mechanical base/superstructure distinction with a more dialectical conception of how economic, political, and cultural elements interpenetrate @sorel1999 @bates1975. A stable historical bloc achieves equilibrium between structure and superstructure; when contradictions accumulate and this equilibrium fractures, *organic crisis* emerges---"the old is dying and the new cannot be born" @ruccio2020.

= Kuhn's Philosophy of Science: Paradigms and Revolutions

Kuhn's _Structure of Scientific Revolutions_ (1962) transformed philosophy of science by demonstrating that scientific development proceeds not through steady accumulation but through discontinuous revolutions separating incommensurable paradigms @kuhn1962. His framework shares striking structural homologies with Gramsci's political theory.

*Normal science* describes the routine puzzle-solving activity of scientists working within an accepted paradigm @sepkuhn2018. Like Gramsci's common sense, the paradigm comprises taken-for-granted assumptions, values, techniques, and exemplary problem-solutions that scientists internalize through education and apply without critical examination. Kuhn emphasized that this "dogmatic" commitment to tradition is productive: scientists committed to a paradigm can pursue detailed investigations impossible without shared assumptions @kuhn1963. As he argued in "The Function of Dogma in Scientific Research" (1963), unquestioning adherence enables the intensive work through which paradigms reveal their potential---and their limitations.

*Anomalies* are results that resist assimilation into the paradigm's framework---puzzles that remain unsolved despite repeated attempts @kuhn1970. Unlike Karl Popper's falsificationism, which holds that single reproducible counterexamples should trigger theory rejection @popper1970, Kuhn showed that scientists routinely explain away anomalies, set them aside as special cases, or blame experimental error. Only when anomalies accumulate, become "particularly troublesome" by casting doubt on commonly used equipment or core assumptions, and resist repeated solution attempts does *crisis* emerge @hoyningenschwob1993.

During crisis, confidence erodes in the paradigm's capacity to solve its problems. Alternative paradigms---typically proposed by younger scientists or outsiders not fully socialized into the dominant framework---compete for adherents @wray2011. The transition between paradigms is not "rationally compelled" by evidence alone; it involves social, aesthetic, and promissory factors. Kuhn's provocative claim that scientists "work in a different world" after a revolution points toward *incommensurability*: key terms change meaning, standards of evaluation shift, and the new paradigm cannot be fully translated into the old framework's categories @sepkuhn2018.

Margaret Masterman identified over twenty different meanings of "paradigm" in Kuhn's original text @masterman1970. In his 1970 Postscript and subsequent essays, Kuhn clarified two primary senses: the *disciplinary matrix* (the entire constellation of shared commitments within a scientific community) and *exemplars* (concrete puzzle-solutions that serve as models for further research) @kuhn1970. By the 1990s, he largely replaced "paradigm" with "lexical structure" while maintaining that revolutionary change involves untranslatable conceptual shifts.

= Scholarly Connections: Gramsci Meets Kuhn

Explicit scholarly work directly comparing Gramsci and Kuhn remains limited but significant. *Agustí Nieto-Galan's* "Antonio Gramsci Revisited" (2011) provides the most sustained engagement, arguing that historians of science have "tacitly shared the hegemonic values of the élites of their time" under "the rhetoric of neutrality and objectivity" @nietogalan2011. Drawing on Steven Fuller's analysis of Kuhn's mentor James B. Conant @fuller2000, Nieto-Galan shows how Cold War politics shaped _Structure_'s reception and historiographical implications. Robert M. Young had earlier proposed that Gramsci's work "would become a very useful reference for future historians of science" @young1977.

#v(1em)
#figure(
  table(
    columns: (1fr, 1fr, 1.5fr),
    align: (left, left, left),
    stroke: 0.5pt,
    inset: 8pt,
    [*Kuhn*], [*Gramsci*], [*Structural Parallel*],
    [Normal science], [Hegemonic stability], [Dominant frameworks operate unquestioned through naturalized assumptions],
    [Paradigm], [Common sense], [Shared conceptual schemes structure perception and limit imagination],
    [Scientific community], [Historical bloc], [Groups cohere around shared frameworks, institutions, practices],
    [Anomalies], [Contradictions], [Accumulating problems destabilize the dominant framework],
    [Crisis], [Organic crisis], [Confidence fractures; alternatives become thinkable],
    [Paradigm shift], [Counter-hegemonic revolution], [Transformations rupture dominant categories],
    [Incommensurability], [Ideological rupture], [Different frameworks cannot fully communicate],
  ),
  caption: [Structural parallels between Kuhnian and Gramscian frameworks],
)
#v(1em)

The *Sociology of Scientific Knowledge* (SSK) represents the most important site where Gramscian and Kuhnian frameworks interpenetrate. The Edinburgh School's "Strong Programme" (David Bloor, Barry Barnes, Steven Shapin) built on Kuhn's social epistemology while sharing methodological commitments with Marxist sociology @bloor1976. Their "symmetry principle"---analyzing true and false beliefs with the same types of explanations---parallels Gramsci's critique of ideology's claim to neutrality. Barry Barnes's _T.S. Kuhn and Social Science_ (1982) extended this framework @barnes1982, while Shapin and Barnes analyzed science education as "social control" @shapinbarnes1977. However, SSK scholars generally avoided explicit Marxist framing---Kuhn himself, though benefiting from Marxist critiques, distanced himself from SSK, calling himself a "pretty straight internalist."

*Feminist philosophy of science* offers perhaps the richest synthesis. Sandra Harding drew on Kuhn to argue that science is situated within historical context, proposing "strong objectivity" that incorporates feminist standpoints @harding1991. Donna Haraway's "situated knowledges" challenges what she calls the "God Trick"---the claim to a view from nowhere---in terms directly resonant with Gramsci's critique of supposedly neutral knowledge @haraway1988. Helen Longino's "contextual empiricism" uses Kuhnian underdetermination arguments to show how values "fill the gap" between evidence and theory acceptance @longino1990. These scholars explicitly challenge "the hegemony of dominant 'spectator epistemologies'" @sepfemep2020 @doucet2018.

Richard Levins and Richard Lewontin's _The Dialectical Biologist_ (1985) represents explicitly Marxist philosophy of science, arguing that dominant ideologies "set the tone for theoretical investigation of phenomena, which then becomes a reinforcing practice for the ideology itself"---a directly Gramscian formulation applied to biological science @levinslew1985.

= Revolutionary History Through a Gramscian Lens

Gramsci's analysis of revolution distinguished between *war of maneuver* (direct assault on state power) and *war of position* (protracted struggle within civil society) @gramsci1971. In Russia, where "the State was everything, civil society was primordial and gelatinous," war of maneuver succeeded in 1917. In Western Europe, where robust civil society provided defensive fortifications, the same strategy failed during the revolutionary wave of 1919--1920. This analysis shaped Gramsci's strategic reconceptualization @anderson1976.

The *Italian Risorgimento* served as Gramsci's paradigm case of *passive revolution*---transformation of political structures without genuine mass participation @thomas2009book. The northern bourgeoisie around Cavour failed to develop hegemonic leadership incorporating Southern peasants; the Action Party of Mazzini and Garibaldi lacked the "Jacobin" qualities necessary to mobilize popular forces. The result was "revolution-restoration" establishing capitalism without dismantling feudal remnants @femia1981. *Trasformismo*---the absorption of opposition leaders into the ruling coalition---neutralized potential challengers. By contrast, the French Revolution's Jacobins served as Gramsci's model of successful hegemonic construction, converting bourgeois demands into universal aspirations embracing the peasantry.

The 1968 movements demonstrated what Christine Buci-Glucksmann called "a confusion of a crisis of hegemony... for a revolutionary crisis" @buciglucksmann1980. The movements revealed hegemonic fractures but lacked organizational continuity and organic articulation with working-class institutions. Power "was not 'for the taking'"---the robust civil society of advanced capitalism proved resilient. This experience validated Gramsci's warning about the necessity of sustained war of position in Western conditions.

Contemporary applications remain contested. Brecht De Smet's _Gramsci on Tahrir_ (2016) analyzes the Egyptian revolution through passive revolution and Caesarism: the uprising destabilized the regime without producing lasting transformation, culminating in Sisi's coup---"a third force intervening when contending classes cannot resolve their conflict" @desmet2016. The Latin American "Pink Tide" has generated intense scholarly debate: Tom Chodor sees Venezuela as genuine counter-hegemony @chodor2014, while Gaudichaud, Modonesi, and Webber argue the entire cycle represents passive revolution that demobilized social movements while maintaining extractivist capitalism @gaudichaud2022.

The right has also appropriated Gramscian strategy. Alain de Benoist's Nouvelle Droite advocated "Gramscism of the Right" (_pour un gramscisme de droite_) since the late 1970s, pursuing cultural "metapolitics" before electoral engagement @debenoist2017 @bar-on2001. Steve Bannon explicitly deployed Gramscian frameworks in constructing Trumpist populism, building counter-hegemonic narrative and using alternative media for ideological warfare. This appropriation strips Gramsci's class analysis while retaining strategic insights about cultural politics.

= Contemporary Left Strategy and Gramscian Theory

Contemporary leftist thinkers have developed Gramscian theory for present conditions. *Chantal Mouffe's* _For a Left Populism_ (2018) argues the current "populist moment" signals neoliberal hegemony's crisis and offers opportunity to construct new progressive blocs @mouffe2018. She advocates constructing a "political frontier" between "those from below" and "those from above," mobilizing common affects rather than abstract categories. Crucially, Mouffe frames left populism as war of position---setbacks for Syriza, Corbyn, and Podemos reflect the long-term nature of hegemonic struggle, not proof of strategic failure. Her earlier work with Ernesto Laclau, _Hegemony and Socialist Strategy_ (1985), remains foundational for post-Marxist approaches @laclaumouffe1985.

*Stuart Hall* pioneered analyzing Thatcherism as hegemonic project, recognizing it constructed new consensus "drawn from some of the 'common sense' hopes and fears of ordinary people" while being supported by New Right think tanks @hall1979 @hall1988. His warning that the left must "take the forms of hegemonic politics more seriously" remains urgent---neoliberalism achieved dominance through decades of cultural and ideological struggle, not just policy implementation.

*Nancy Fraser* analyzes "progressive neoliberalism"---the alliance of mainstream liberal currents (feminism, anti-racism, LGBTQ rights) with finance capital---as the hegemonic formation that dominated from the 1990s until its crisis @fraser2017 @fraser2019. Her prescription: build a "progressive-populist" bloc combining egalitarian redistribution with substantively inclusive recognition politics, linking struggles against racism and sexism to critique of financialized capitalism.

*Jane McAlevey's* work on organizing offers practical methodology @mcalevey2016 @mcalevey2020. Her crucial distinction: *mobilizing* reaches those who already agree; *organizing* expands the base by reaching those who don't. "If we want to actually change the power balance, we have to learn to organize." Her methods---"structure tests" measuring real organizing strength, developing organic leaders from within workplaces, building supermajority support---translate Gramscian theory into union practice.

The record of recent movements is sobering. *Syriza* capitulated to the troika in July 2015 after briefly challenging austerity, having "shifted decisively towards parliamentary politics, neglecting the grassroots forces that had propelled it." *Corbynism* achieved counter-hegemonic success in shifting discourse but failed to develop independent organizational base outside Labour's institutional structure. *Podemos* entered government as junior partner, leading critics to argue it subordinated itself to "progressive neoliberals." Common patterns emerge: programs steadily moderated; parties acted as "movement-parties" initially but abandoned grassroots forces; they relied on elite-level negotiations rather than mass mobilization.

*Brazil's MST (Landless Workers Movement)* represents a more successful application. Rebecca Tarlau describes their strategy as "contentious co-governance"---activists enter mainstream institutions not as reformers vulnerable to cooptation but as part of building counter-hegemonic leadership @tarlau2019. The MST explicitly draws on Gramscian theory; activists "transform institutions from within while maintaining movement base."

= Critiques and Alternative Perspectives

Critiques illuminate limitations of Gramscian strategy. Autonomist and anarchist critics (Richard Day's _Gramsci is Dead_) argue hegemony remains "a logic of domination tied to the state," preferring prefigurative politics and affinity-based organizing over long-term institutional strategy @day2005. Orthodox Marxists charge that Gramscian emphasis on culture displaces focus on material class struggle and can justify reformism.

Feminist critics warn against counterposing "identity politics" to "class politics," emphasizing that interests "are not given but have to be politically and ideologically constructed"---making anti-racist and feminist work essential to any counter-hegemonic project, not diversions from it @laclaumouffe1985.

Robert Cox extended Gramscian analysis to international relations, analyzing how hegemonic powers establish global "common sense" through international institutions @cox1987. Stephen Gill's work on "disciplinary neoliberalism" shows how transnational capital imposes constraints that limit national-level counter-hegemonic possibilities @gill1995.

= Strategic Synthesis: Lessons from the Gramsci-Kuhn Parallel

The homology between hegemony and paradigm offers strategic insight. Both frameworks reveal that dominant systems achieve stability not through force but through *naturalization*---making particular arrangements appear as obvious common sense or neutral scientific fact. Both show that transformation requires not just critique but *construction of alternatives*: counter-hegemonic institutions parallel the new paradigms that emerge to address accumulated anomalies. Both emphasize that transitions involve *categorical rupture*---the new framework cannot be fully translated into the old's terms, requiring what Gramsci called developing "good sense" from within common sense.

The most important lesson may be temporal. Kuhn showed that paradigms reveal their potential---and their contradictions---only through sustained normal science; revolutionary transitions require accumulated anomalies and alternative frameworks already developed. Gramsci's war of position similarly requires patient institution-building, development of organic intellectuals, and construction of counter-hegemonic common sense over decades. The neoliberal right understood this: the Mont Pèlerin Society nurtured free-market ideas for decades before Thatcher and Reagan; think tanks, media networks, and educational institutions prepared the cultural ground. The left's failures often stem from expecting electoral victories to substitute for this groundwork.

== Toward Synthesis: Paradigm Shifts as Hegemonic Struggles

The Gramsci-Kuhn parallel illuminates both science and politics. Scientific communities function as historical blocs, with paradigms operating hegemonically to structure perception and limit imagination. Feminist and post-colonial science studies reveal how "the hegemony of dominant 'spectator epistemologies'" excludes marginalized perspectives and reproduces existing power relations @harding1991 @haraway1988.

Conversely, Kuhn's emphasis on exemplars---concrete puzzle-solutions that guide future research---offers practical insight for political organizing. Counter-hegemony requires not just critique but *successful examples* of alternative arrangements: cooperatives demonstrating economic democracy, participatory budgeting showing democratic governance, worker-owned media proving that information can serve public rather than corporate interests. These exemplars, like successful puzzle-solutions in science, become models through which new frameworks are learned and extended.

Both thinkers ultimately reject the choice between pure objectivism and pure relativism. Kuhn maintained that science progresses---later paradigms generally solve more puzzles with greater precision---while denying this progression aims toward timeless truth. Gramsci sought to develop coherent philosophy from within contradictory common sense, extracting good sense rather than imposing alien doctrine. Both frameworks suggest that transformational change requires working within existing systems while constructing alternatives capable of eventually displacing them.

= Conclusion: Strategic Framework for Counter-Hegemonic Practice

The synthesis points toward a strategic framework:

+ *Identify accumulated contradictions* in dominant arrangements
+ *Develop counter-hegemonic institutions* and organic intellectuals capable of articulating alternatives
+ *Build coalitions* (historical blocs) uniting diverse forces around shared vision
+ *Pursue sustained war of position* across cultural, economic, and political domains
+ *Prepare for moments* when organic crisis creates openings for more rapid transformation while recognizing that such moments cannot be artificially created

This is the patient, rigorous work that both Gramsci's hegemony and Kuhn's paradigm theory, each in their domain, reveal as prerequisite to genuine change. The comparison makes Kuhn more political and Gramsci more epistemological---which is exactly what a productive theoretical synthesis should accomplish.

#pagebreak()

#bibliography("references.bib", title: "References", style: "chicago-author-date")
