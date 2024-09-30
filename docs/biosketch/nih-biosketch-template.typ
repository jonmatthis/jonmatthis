#let nih_biosketch(
  name: "John Doe",
  era_commons_username: none,
  position_title: "Research Scientist",
  email: "john.doe@example.com",
  phone: "+1 (xxx) xxx-xxxx",
  education: [],
  personal_statement: [],
  positions: [],
  contributions: [],
  scholastic_performance: []
) = [
  // Header
  set page(
    paper: "us-letter",
    margin: (1in, 1in, 1in, 1in)
  )
  align(center)[
    text(20pt, bold)[#name]
    text(12pt)[#position_title]
    text(12pt)[#email • #phone]
    if #era_commons_username != none {
      text(10pt)[eRA Commons Username: #era_commons_username]
    }
  ]
  
  // Section: Education/Training
  set align(left)
  text(16pt, bold)["Education/Training"]
  for #edu in #education {
    text(12pt, italic)[#edu.degree]
    text(12pt)[#edu.institution, ", ", #edu.location, " (", #edu.dates, ")"]
  }
  
  // Section: A. Personal Statement
  text(16pt, bold)["A. Personal Statement"]
  for #statement in #personal_statement {
    text(12pt)[#statement]
  }
  
  // Section: B. Positions, Scientific Appointments, and Honors
  text(16pt, bold)["B. Positions, Scientific Appointments, and Honors"]
  for #pos in #positions {
    text(12pt, italic)[#pos.title]
    text(12pt)[#pos.company, ", ", #pos.location, " (", #pos.dates, ")"]
    for #detail in #pos.details {
      text(12pt)["- ", #detail]
    }
  }
  
  // Section: C. Contributions to Science
  text(16pt, bold)["C. Contributions to Science"]
  for #contrib in #contributions {
    text(12pt, italic)[#contrib.title]
    text(12pt)[#contrib.description]
    for #pub in #contrib.publications {
      text(12pt)["- ", #pub]
    }
  }
  
  // Section: D. Scholastic Performance
  if #scholastic_performance.len() > 0 {
    text(16pt, bold)["D. Scholastic Performance"]
    for #school in #scholastic_performance {
      text(12pt, italic)[#school.institution]
      for #course in #school.courses {
        text(12pt)["- ", #course]
      }
    }
  }
]