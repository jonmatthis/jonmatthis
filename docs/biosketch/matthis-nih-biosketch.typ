#import "nih-biosketch-template.typ": nih_biosketch

#show: doc => nih_biosketch(
  name: "Dr. Jane Smith",
  era_commons_username: "JaneSmith123",
  position_title: "Principal Investigator",
  email: "jane.smith@researchlab.edu",
  phone: "+1 (123) 456-7890",
  education: [
    {institution: "Harvard University", location: "Cambridge, MA", dates: "Sep 2000 - Jun 2004", degree: "B.Sc. in Biology"},
    {institution: "Stanford University", location: "Stanford, CA", dates: "Sep 2004 - Jun 2008", degree: "Ph.D. in Molecular Biology"}
  ],
  personal_statement: [
    "I am well-suited for my role in this project due to my extensive training in molecular biology and my previous experimental work on related topics. I have a strong technical expertise and a collaborative scientific environment."
  ],
  positions: [
    {
      title: "Postdoctoral Research Fellow",
      company: "Stanford University",
      location: "Stanford, CA",
      dates: "Jul 2008 - Present",
      details: [
        "Conducted research on molecular mechanisms of disease.",
        "Published several high-impact papers in peer-reviewed journals."
      ]
    }
  ],
  contributions: [
    {
      title: "Significant Contribution to Science",
      description: "My research has significantly advanced the understanding of molecular mechanisms underlying disease.",
      publications: [
        "Smith J, et al. (2010). Molecular insights into disease mechanisms. Science.",
        "Smith J, et al. (2012). Advances in molecular biology. Nature."
      ]
    }
  ],
  scholastic_performance: [
    {
      institution: "Harvard University",
      courses: [
        "Biology 101: A",
        "Chemistry 101: A",
        "Physics 101: A"
      ]
    },
    {
      institution: "Stanford University",
      courses: [
        "Advanced Molecular Biology: A",
        "Genetics: A",
        "Biochemistry: A"
      ]
    }
  ]
)

#doc