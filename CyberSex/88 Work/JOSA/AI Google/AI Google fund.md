
https://humane-intelligence.org/post/ai-red-teaming-app-oss-funding-announcement-google-org/
https://humane-intelligence.org/product/oss-release/
https://docs.google.com/document/d/1Xuyhw88B26rmYspmhTF-8ua8j7ygB817XKwA5kSGa-Q/edit?tab=t.0





Humane Intelligence ? Google.org-Funded OSS Red Teaming App (Updated 31 Jan 2026)
======================================================================

What this is
- Humane Intelligence (nonprofit founded by Dr. Rumman Chowdhury) received full funding from Google.org to rebuild and open source its AI red teaming web app. The project goal: decouple the React front-end, rebuild the backend in Python, and release under an OSS license so more orgs can run red teaming for social-good AI systems. ?cite?turn0search0?

Key takeaways from the internal memo (19 Dec 2025)
- Motivation: Monolithic Next.js app worked for early needs; Python now preferred for LLM work, so backend must be rewritten. OSS release lowers adoption cost and grows the evaluation ecosystem.
- Target users: Highest demand is from orgs building AI-for-good systems; managed instance will remain for non-technical clients.
- Technical plan (Option C): keep React frontend; rebuild backend in Python with data transformers + viz; add LLM/GenAI helpers; support multiple model providers. ?cite?turn0search1?
- OSS archetype: ?Trusted Vendor? ? strong core maintained by HI, community can extend; avoids vendor lock-in while keeping a paid managed instance. ?cite?turn0search1?
- Licensing being evaluated: MIT, Apache 2.0, or BSD-3; final choice likely with legal counsel.
- Governance: will add governance + contribution plans; may join Digital Public Goods Alliance; possible future handoff to a foundation after ~2 years.
- Funding ask: Total USD 250k
  * Phase 1 (completed, self-funded) code investigation ? $5k
  * Phase 2 Python rebuild (staff + vendor + UX) ? $150k
  * Phase 3 OSS release (maintainer, license counsel, DPG prep) ? $100k
- Contacts: Mala Kumar (Interim ED) mala@humane-intelligence.org; Julie Hollek (Head of Eng) julie@humane-intelligence.org.

Current status & timeline (public updates)
- Work kicked off July 2025; OSS release planned around Nov? Dec 2026. 
- Blog confirms Google.org funding and three-phase plan; initial OSS release targeted for late 2026. 
- HI is recruiting a Python engineering firm via an Expression of Interest (EOI); submissions due 6 Feb 2026 (rolling review). ?cite?turn0search2?

How you can engage / apply
- If you're an engineering firm: submit the EOI form on HI?s ?Work With Us? page before 6 Feb 2026; include portfolio for Python, FastAPI/Django, LLM integrations, and OSS experience. ?cite?turn0search2?
- If you're a funder: they are seeking USD 250k (Phase 2?3). Reach out to Mala or Julie (emails above) or info@humane-intelligence.org; mention Google.org-funded OSS red teaming project and request partnership deck.
- If you're a user org wanting early access: ask to be included in the managed-instance client list or future OSS beta via info@humane-intelligence.org; highlight your model stack and evaluation needs.
- If you're a contributor: watch for the public roadmap and GitHub repo to open in 2026; sign up to their newsletter for announcements. 

Is there an application demo?
- Public site has a high-level product page and marketing video; no interactive public demo of the new Python backend yet. The existing managed-instance UI is shown in the ?Red Teaming App? page, but backend rewrite is in progress. ?cite?turn0search6?

Practical next steps for you
- Decide role: funder, engineering vendor, or adopter.
- If vendor: prepare a concise EOI (team, Python/LLM portfolio, OSS track record) and submit by 6 Feb 2026.
- If funder: draft a brief stating amount, timeline, and whether support is unrestricted or project-specific; email leadership.
- If adopter: request to pilot on their managed instance; share your models/APIs you want red teamed and data-handling constraints.

Quick facts
- Org type: 501(c)(3) nonprofit; HQ US.
- Program lead: Interim ED Mala Kumar; Engineering lead: Dr. Julie Hollek.
- Deliverable: First OSS release targeted Q4 2026; Trusted Vendor model with managed instance retained.
- Tech shift: JS monolith ? React frontend + Python backend with LLM helpers.
- Budget remaining to raise: ~$250k for rebuild + OSS release phases.

JOSA Application Plan (for Humane Intelligence OSS Backend EOI)
- Fit check: JOSA is a Jordan-based nonprofit promoting open tech (est. 2011); aligns with HI?s OSS + AI-for-good goals. ?cite?turn0search1?turn0search3?
- Opportunity: Humane Intelligence seeks an engineering firm to rebuild the Python backend of its OSS red-teaming app; EOI deadline Feb 6, 2026 (rolling). ?cite?turn0search0?

What to submit (EOI form asks for org background, team, portfolio)
1) Org profile: mission, legal status in Jordan, years active, key partners.
2) Relevant work: highlight Nuha (Arabic hate-speech AI), local LLM workshops, open-source contributions; include repo links and any Python/FastAPI/Django/LLM projects. ?cite?turn0search12?turn0search14?
3) Team: list senior Python engineers, data/ML leads, and DevOps (cloud: AWS/GCP; infra for Hugging Face/LLMs). Include CV links.
4) Approach: propose keeping HI React frontend, building Python backend with FastAPI (or Django REST), asynchronous task queue (Celery/RQ), Postgres, and adapters for multiple model providers.
5) Delivery: 3 phases mirroring HI plan?(a) backend rewrite & tests, (b) OSS hardening/security, (c) handover & maintainer onboarding.
6) Budget & timeline: align to HI?s Phase 2 ($150k) + Phase 3 ($100k). Offer a detailed milestone/burn-rate schedule with optional UX/annotation/audio features as stretch.
7) Compliance & OSS: suggest Apache-2.0 compatibility; reference JOSA?s open-source governance experience; propose community contribution playbook in Arabic/English.

How to apply
- Go to HI Work-With-Us page and click ?Submit interest? under OSS Backend Engineering EOI (due Feb 6, 2026). Link: humane-intelligence.org/get-involved/work-with-us/. ?cite?turn0search0?
- Prepare a 3?4 page PDF + portfolio links before filling the form; submissions are rolling, so send ASAP (January 31, 2026 today).
- Follow up after submission via info@humane-intelligence.org and copy mala@humane-intelligence.org + julie@humane-intelligence.org referencing the Google.org-funded OSS backend project.

Prep checklist for JOSA this week
- Assemble portfolio (Nuha, workshops, any OSS repos) and brief case studies (problem, stack, impact, links).
- Confirm availability of 1?2 senior Python/LLM engineers for 12 months; note part-time if applicable.
- Draft milestone schedule with deliverables, acceptance criteria, and risk mitigations (data privacy, model eval safety, multilingual testing).
- Record a short 2?3 minute screencast or slide walkthrough of a similar backend/LLM project to attach as unlisted video link.
- Get board/finance sign-off on budget range and contracting terms in USD.
