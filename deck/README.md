# Launch deck — *We the Users*

`We-the-Users-Launch-Deck.pptx` — a 21-slide public launch-and-join deck.

**Audience & intent.** The public, to launch and join: emotional and punchy, a single
clear call to action (add your name on July 2), and deliberately light on governance and
economics machinery.

**Arc.** Cover → you cast a shadow → someone else owns it → we never agreed →
1776/2026 (the physical world then, the digital world now) → the vision → power divided
three ways → three guardrails → the thousand-year horizon → **the case, in five essays**
(a divider + one slide each: *We Never Agreed*, *The Shape of Your Digital Shadow*,
*Ambition Against Ambition*, *The Longer Race*, *The Ledger and the Spoils*) → what
launches July 2 → this one is for everyone → add your name → close.

**Design.** Navy-dominant with parchment interludes for rhythm; Cambria serif headlines
with Calibri for labels and support; the *digital shadow* as the signature (key statements
cast a soft drop shadow); an editorial template for the essay slides (large gold numeral +
title + thesis + essence). Brand palette: navy `#1B2A4A`, gold `#B08D3A`, ivory `#F1ECDD`,
parchment `#F4F1EA`.

**Current founding decisions are baked in:** the thousand-year horizon, the constitution as
the **Covenant + the Code**, governance framed as an open principle (no specific board
shown), capped returns, and forkability. The site is **wetheusers.ai**.

## Rebuild
```bash
npm install -g pptxgenjs react-icons react react-dom sharp
NODE_PATH=$(npm root -g) node build_deck.js
python /mnt/skills/public/pptx/scripts/rezip.py We-the-Users-Launch-Deck.pptx
```
