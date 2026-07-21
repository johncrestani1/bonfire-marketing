// ============================================================================
// PODCAST PRESS SHEET v8 — Typst template
// Compile:  typst compile press-sheet-v8.typ press-sheet-v8-private.pdf
//           typst compile press-sheet-v8.typ press-sheet-v8-public.pdf --input private=false
// ============================================================================

// --- Parameter: private (true = include email/phone/telegram) ---------------
#let private = {
  let raw = sys.inputs.at("private", default: "true")
  raw == "true"
}

// --- Colors -----------------------------------------------------------------
#let CLR_DARK      = rgb("#1A1A1A")
#let CLR_NAVY      = rgb("#013161")
#let CLR_RED       = rgb("#E63946")
#let CLR_GREEN     = rgb("#259F70")
#let CLR_AMBER     = rgb("#FFB700")
#let CLR_SUBTITLE  = rgb("#585858")
#let CLR_FUN_FACT_BORDER  = rgb("#585858")
#let CLR_CONTACT_BORDER   = rgb("#E0E0E0")

// --- Fonts ------------------------------------------------------------------
#let font-headline = "Orbitron"
#let font-body     = "SF Pro Text"

// --- Section spacing --------------------------------------------------------
#let SECTION_GAP = 10pt
#let LEFT_SECTION_GAP = 18pt

// --- Page setup -------------------------------------------------------------
#set page(
  width: 8.5in,
  height: 11in,
  margin: (top: 0.15in, bottom: 0.15in, left: 0in, right: 0.3in),
)
#set text(font: font-body, size: 9.5pt, fill: CLR_DARK)
#set par(leading: 0.3em)

// --- Helper: ghost section header (bordered rectangle with label) -----------
#let ghost-header(label, border-color) = {
  box(
    width: 100%,
    stroke: (bottom: 1.5pt + border-color),
    inset: (bottom: 2pt),
    text(font: font-body, weight: "bold", size: 10pt, fill: border-color, upper(label)),
  )
}

// --- Helper: text-only section header (right column) ------------------------
#let section-header(label) = {
  v(SECTION_GAP)
  text(font: font-body, weight: "bold", size: 11pt, fill: CLR_DARK, upper(label))
  v(0pt)
}

// --- Helper: styled link (black text, navy underline) -----------------------
#let styled-link(url, label-text) = {
  underline(stroke: 1pt + CLR_NAVY, offset: 2pt, evade: false,
    link(url, text(fill: CLR_DARK, label-text))
  )
}

// --- Image root -------------------------------------------------------------
#let img = "images/"

// ============================================================================
// TOP BANNER
// ============================================================================
#pad(left: 0.3in, {
  block(
    width: 100%,
    inset: (left: 0.0in, right: 0.0in, top: 8pt, bottom: 6pt),
    stroke: 3pt + CLR_DARK,
    {
      align(center,
        stack(dir: ttb, spacing: 6pt,
          text(font: font-headline, weight: "bold", size: 40pt, fill: CLR_DARK, tracking: 2pt,
            "JOHN CRESTANI"
          ),
          text(font: font-headline, size: 9pt, fill: CLR_SUBTITLE, tracking: 1.5pt,
            "AFFILIATE MARKETING  •  BOOTSTRAPPED  •  SOFTWARE DEVELOPMENT"
          ),
        )
      )
    }
  )
})

#v(0pt)

// ============================================================================
// TWO-COLUMN BODY
// ============================================================================
#grid(
  columns: (3.0in, 1fr),
  column-gutter: 0.2in,

  // ========== LEFT COLUMN ===================================================
  {
    // --- Headshot (flush to left page edge, nudged up) ---
    v(-8pt)
    image(img + "jc-headshot-pink-blazer.png", width: 3.0in)

    v(LEFT_SECTION_GAP)

    // --- THE BUSINESS section ---
    pad(left: 0.15in, {
      ghost-header("The Business", CLR_DARK)
      v(4pt)
      link("https://bonfireterminal.com", image(img + "bonfire-wordmark-600.png", width: 2.5in))
    })

    v(LEFT_SECTION_GAP)

    // --- FUN FACT section ---
    pad(left: 0.15in, {
      ghost-header("Fun Fact", CLR_FUN_FACT_BORDER)
      v(4pt)
      text(size: 9.5pt, style: "italic",
        "John has visited 50+ countries and kitesurfs or skis in as many of them as possible."
      )
    })

    v(LEFT_SECTION_GAP)

    // --- CONTACT section ---
    pad(left: 0.15in, {
      ghost-header("Contact", CLR_CONTACT_BORDER)
      v(4pt)

      if private {
        // Private contact info with icons
        grid(columns: (12pt, 1fr), column-gutter: 4pt, row-gutter: 3pt,
          image(img + "contact-icons/email.png", width: 10pt),
          text(size: 9pt, styled-link("mailto:john.crestani@gmail.com", "john.crestani\u{0040}gmail.com")),
          image(img + "contact-icons/phone.png", width: 10pt),
          text(size: 9pt, "(310) 292-9369"),
          image(img + "contact-icons/telegram.png", width: 10pt),
          text(size: 9pt, styled-link("https://t.me/marketeering", "\u{0040}marketeering")),
        )
        v(2pt)
      }

      // Public contact info with icon
      grid(columns: (12pt, 1fr), column-gutter: 4pt, row-gutter: 3pt,
        image(img + "contact-icons/website.png", width: 10pt),
        text(size: 9pt, styled-link("https://johncrestani.com", "johncrestani.com")),
      )

      v(2pt)

      // Social icons row 1
      grid(
        columns: (1fr,) * 6,
        column-gutter: 2pt,
        align: center,
        link("https://youtube.com/@johncrestani",
          image(img + "social-icons-v4/youtube-logo-grey.png", width: 18pt)),
        link("https://x.com/johncrestani",
          image(img + "social-icons-v4/x-logo-grey.png", width: 18pt)),
        link("https://instagram.com/johncrestani",
          image(img + "social-icons-v4/instagram-logo-grey.png", width: 18pt)),
        link("https://linkedin.com/in/johncrestani",
          image(img + "social-icons-v4/linkedin-logo-grey.png", width: 18pt)),
        link("https://github.com/johncrestani1",
          image(img + "social-icons-v4/github-logo-grey.png", width: 18pt)),
        link("https://crunchbase.com/person/john-crestani",
          image(img + "social-icons-v4/crunchbase-logo-grey.png", width: 18pt)),
      )

      v(2pt)

      // Social icons row 2
      grid(
        columns: (1fr,) * 6,
        column-gutter: 2pt,
        align: center,
        link("https://www.dnb.com/business-directory/company-profiles.m3m3tic_llc.406df7cc2095065dbc0f0e3da35b99cf.html",
          image(img + "social-icons-v4/dnb-logo-grey.png", width: 18pt)),
        link("https://www.clickbank.com/blog/john-crestani-clickbank-finding-freedom-digital-age/",
          image(img + "social-icons-v4/clickbank-logo-grey.png", width: 18pt)),
        link("https://www.digistore24.com",
          image(img + "social-icons-v4/digistore24-logo-grey.png", width: 18pt)),
        link("https://warriorplus.com",
          image(img + "social-icons-v4/warriorplus-logo-grey.png", width: 18pt)),
        link("https://rumble.com/v2qy7x0-ep298-john-crestani-influencer-marketing-101-for-businesses-of-any-size.html",
          image(img + "social-icons-v4/rumble-logo-grey.png", width: 18pt)),
        link("https://fourthwall.com",
          image(img + "social-icons-v4/fourthwall-logo-grey.png", width: 18pt)),
      )
    })
  },

  // ========== RIGHT COLUMN ==================================================
  {
    // --- ABOUT (starts ~1in further left, curves to current position) ---
    pad(left: -72pt, section-header("About"))

    // Mission statement (italic quote)
    pad(left: -68pt,
      text(size: 9.5pt, style: "italic", fill: CLR_DARK,
        "\u{201C}I build tools that let one person do what used to take a team of ten.\u{201D}"
      )
    )

    v(1pt)

    // Bio bullets with decelerating curve: starts far left, eases to current position
    let about-bullets = (
      "Left corporate marketing in 2012; earning seven figures per year solo by 2014",
      "600K+ YouTube subscribers",
      "Sold over 20,000 books on late-night cable TV infomercials",
      "Taught himself to build software using AI; built Bonfire Terminal, an AI maximalization harness for nontechnical creators.",
      "Obsessed with Rust, Lua, CLIs, mushrooms, and Mars colonization.",
      "Lives in Malibu with two daughters",
    )
    let about-offsets = (-62pt, -42pt, -26pt, -14pt, -5pt, 0pt)

    for (i, bullet) in about-bullets.enumerate() {
      pad(left: about-offsets.at(i), {
        grid(
          columns: (14pt, 1fr),
          column-gutter: 4pt,
          text(fill: CLR_GREEN, weight: "bold", size: 10pt, "✓"),
          text(size: 9pt, bullet),
        )
      })
    }

    // --- INTRODUCTION ---
    section-header("Introduction")

    par(justify: true,
      text(size: 9pt,
        "John Crestani went from affiliate marketer of health supplements to community leader of 50,000+ entrepreneurs; featured on Forbes, CNBC, and Entrepreneur. An AI maximalist, he built Bonfire Terminal an AI harness for nontechnical creators with zero coding experience. No team. No VC. Just AI. His argument: stop renting your tools from the cloud. Own them. John, welcome to the show."
      )
    )

    // --- TOPICS ---
    section-header("Topics")

    for (i, topic) in (
      "AI as Your Entire Product Team",
      "What Visiting Russia Taught Me About Marketing",
      "From Affiliate Marketing to Software Company",
      "Why Creators Should Own Their Tools, Not Rent Them",
      "What 735+ AI-Assisted Builds Taught Me About Prompt Engineering",
      "Shipping Enterprise Software Without Writing a Line of Code",
      "The Death of Online Education",
    ).enumerate() {
      grid(
        columns: (14pt, 1fr),
        column-gutter: 4pt,
        text(fill: CLR_AMBER, weight: "bold", size: 10pt, "✓"),
        text(size: 9pt, topic),
      )
    }

    // --- INTERVIEW QUESTIONS ---
    section-header("Interview Questions")

    for question in (
      "You had 600K YouTube subscribers teaching affiliate marketing. Why risk that audience by pivoting to AI software?",
      "Walk me through building a feature. What does the conversation with AI actually look like?",
      "Zero employees, competing with VC-funded teams of 50+ engineers. What is your actual unfair advantage?",
      "What is the most expensive mistake AI made in your codebase, and how did you catch it?",
      "If someone listening right now has a software idea but can't code, what should they do Monday morning?",
      "You run 4 different AI providers in one product. Which one is best at what?",
      "The affiliate marketing industry has a credibility problem. How do you think about that with a tech audience?",
    ) {
      grid(
        columns: (14pt, 1fr),
        column-gutter: 4pt,
        text(fill: CLR_RED, weight: "bold", size: 10pt, "✓"),
        text(size: 9pt, question),
      )
    }
  },
)

// ============================================================================
// FOOTER: AS SEEN ON (pinned toward bottom)
// ============================================================================
#v(1fr)

#line(length: 100%, stroke: 0.75pt + CLR_NAVY)
#v(2pt)

#pad(left: 0.15in, {
  grid(
    columns: (auto, 1fr),
    column-gutter: 12pt,
    align: (left + horizon, left + horizon),

    text(font: font-body, weight: "bold", size: 8pt, fill: CLR_SUBTITLE, tracking: 1pt, "AS SEEN ON"),

    grid(
      columns: (1fr,) * 4,
      rows: (auto, auto, auto),
      row-gutter: 3pt,
      column-gutter: 8pt,
      align: center + horizon,
      // Row 1
      image(img + "logos-v3/forbes-wikimedia-grey.png", height: 16pt),
      image(img + "logos-v3/entrepreneur-wikimedia-grey.png", height: 16pt),
      image(img + "logos-v3/cnbc-wikimedia-grey.png", height: 16pt),
      image(img + "logos-v3/bloomberg-wikimedia-grey.png", height: 16pt),
      // Row 2
      image(img + "logos-v3/fox-business-wikimedia-grey.png", height: 16pt),
      image(img + "logos-v3/inc-wikimedia-grey.png", height: 16pt),
      image(img + "logos-v3/business-insider-wikimedia-grey.png", height: 16pt),
      image(img + "logos-v3/eofire-grey.png", height: 16pt),
      // Row 3
      image(img + "logos-v3/nowthis-grey.png", height: 16pt),
      image(img + "logos-v3/lifemastery-grey.png", height: 16pt),
      image(img + "logos-v3/ae-grey.png", height: 16pt),
      image(img + "logos-v3/affiliatesummit-grey.png", height: 16pt),
    ),
  )
})
