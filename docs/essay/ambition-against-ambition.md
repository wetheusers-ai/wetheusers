# Ambition Against Ambition

*Part of **We the Users***
*How a user-owned internet keeps power from re-concentrating*
*Working draft v0.3 · June 22, 2026*

---

> "If men were angels, no government would be necessary. … Ambition must be made to counteract ambition."
> — James Madison (Publius), *The Federalist* No. 51, 1788

## The thing we got wrong

The companies that own today's internet hold four kinds of power at once, and that is the whole problem.

They **control** the machinery — the servers, the code, the keys. That control gives them **power** — the ability to decide what you see, what you may say, who is let in and who is cast out. They have made that power pay, and the **money** has entrenched them past the reach of any rival. And they have granted themselves the **authority** to set all the rules, by the simple device of a terms-of-service agreement no one reads and no one negotiates. Control, power, money, authority — gathered into the same few hands, answerable to no one but their shareholders.

We have lived under this so long it looks like nature. It is not nature; it is a design, and a bad one. The deepest thing a new internet has to get right is not any single rule but the *separation* of those four powers[^seppowers], so that running the software does not also mean ruling the people who use it, and so that money cannot simply buy the rest. This is the oldest lesson in the book on government, and it is the one the internet skipped.

## Four kinds of power

It helps to keep the four straight, because they are easy to confuse, and the confusion is exactly where domination hides.

**Control** is operational command: whose hands are on the machine. **Authority** is the *recognized right* to make a rule or settle a dispute — power that people accept as legitimate. **Power** is the raw capacity to make others comply, legitimate or not. And **money** is the value moving through the system, which, left unchecked, converts into all three.

A free internet needs all four to exist — someone must run the software, someone must settle disputes, the thing must be paid for — but it needs them *held apart*, in different hands, checking one another. The design that follows is one long attempt to do exactly that.

## Three tiers

The structure has three tiers, and you have met them: **Individuals** at the base — people, each with a name; **Communities** in the middle — the places people gather, each with its own name and its own rules; and above them a single thin federation: **the Commonwealth**. The pattern is the one the American founders reached for — *federalism*: a citizen, a state, and a federal government, each holding powers the others do not, with the contested questions pushed down to where the people they affect can settle them.

The whole design can be read off one table — who holds what:

| Domain | The Individual | The Community | The Commonwealth |
|---|---|---|---|
| Your data & identity | holds it, self-custody, portable | sees only what you grant | sets the portability & identity standard |
| Community rules & moderation | picks a Community; can leave | sets its own code, within the floor | sets the floor + interconnection rules |
| Revenue model | consents; shares in the value | chooses (ads / subs / other), within the floor | sets disclosure rules; takes a capped fee |
| Membership | joins the Commonwealth by affirmation | admits & removes its own, with due process | adjudicates breaches of the Covenant; severance |
| The protocol & software | uses it | builds on it | runs it — and it is open and forkable |
| Amending the Covenant | ratifies | proposes | the governing bodies — never the operators alone |
| Rewards / returns | receives the value back | competes on the split | capped at every tier; no permanent rent |

Read down the columns and the separation comes into focus. The Individual holds the self. The Community holds the rules of its own house. The Commonwealth holds only the thin shared floor, the protocol, and a capped fee — deliberately the least of the three, because it is the one place where power could re-concentrate. Most of what makes the old internet oppressive — the rule-setting, the moderation, the revenue model — lives at the Community tier, close to the people, where it can be argued with and walked away from, not dictated from a single center.

## Friendly rivals

Communities compete for members. That is a feature, not a danger — *if* the competition is the friendly kind. The aim is a world where the way to win members is to be better to belong to, and where the moves that hurt people simply do not pay.

The master mechanism is **cheap exit**. Because the Covenant guarantees that your data, your identity, and your connections come with you, a Community cannot hold you hostage; the only way to keep you is to earn you — with better terms, better moderation, a better share of the rewards. Everything else in the floor exists to keep that exit real: mandatory, comparable statistics so you can see how Communities actually treat their members; duties to interconnect so no Community can wall itself off; limits on concentration so none can swell into the next incumbent.

That single mechanism turns the rivalry from destructive to constructive:

| Encouraged — friendly | Discouraged — unfriendly |
|---|---|
| Win members with better terms, rewards, moderation | Lock members in; hold their data hostage |
| Build new services atop the shared protocol | Race to the bottom on extraction or ad-load |
| Honor interconnection; settle disputes fairly | Dump spam, abuse, or costs onto other Communities |
| Publish comparable stats; compete in the open | Hide practices; mislead members |
| Grow by being good to belong to | Monopolize, collude to fix terms, or capture the Commonwealth |

The principle underneath is plain: friendly competition is just what a market looks like when leaving is easy, and unfriendly competition is what it looks like when leaving is hard. Keep exit cheap, and the rivalry stays friendly on its own — not because Communities are virtuous, but because predation stops paying.

## Who belongs

Two questions of membership have to be answered honestly: who belongs to a Community, and who belongs to the Commonwealth at all.

For an **Individual**, joining the Commonwealth is by affirmation, and it is nearly irrevocable — no one can be exiled from the network itself, and your shadow and your identity are always yours. Joining a **Community** is a different matter: each one sets its own standards and may remove people who break them, but only within the floor, which guarantees due process (notice, reasons, a chance to answer, an appeal) and forbids any removal that confiscates your data or your portable identity. This is what makes communities-with-standards tolerable. Being removed from one Community is not exile; you leave *with your shadow* and join or found another. Exclusion is never digital death, and that single guarantee is what lets Communities differ sharply from one another without anyone being trapped or erased.

For a **Community**, the door works differently. Forming one is open to anyone. But to join the Commonwealth — to interconnect with the rest and draw on the shared protocol and the shared rewards — a Community must **enter the Covenant**: it commits, in advance, to the floor, to portability, to transparency, to the duties of interconnection, and to the terms under which it may itself be severed. That last point is the quiet key. Because the rules of severance are part of the agreement every Community accepts on the way in, a Community later cut off for breaking them cannot cry foul — it consented to those terms when it joined. This is consent of the governed, applied to the Communities themselves.

It is also where this design can learn from the one the founders left unfinished. The U.S. Constitution never specified whether or how a state could leave, and the silence was answered, eventually, by a civil war. Writing the terms of severance calmly into the founding agreement — in advance, in plain view — is how the Commonwealth declines to inherit that wound. Severance, when it comes, is not a power seized by the center; it is the enforcement of a rule the Community already agreed to, reached through due process, and even then the Community's members keep their portability, so no one is trapped by the punishment of their Community.

## The money

Money is the solvent that dissolves every other safeguard, so the design watches it closely. The Commonwealth funds itself with a **fee**, a percentage of the activity it carries, but the fee is capped, its books are open, and it is set by the Commonwealth's governing bodies rather than by whoever happens to run the software; the honest expectation is that it should *fall* as the network grows, not rise. Communities choose their own revenue models — advertising, subscription, something not yet invented — and compete on how much of the proceeds they hand back to their members. And at every tier, the returns to founders, engineers, and investors are **capped**: they may be paid, and paid well, but none draws permanent rent on a public square. The throughline is a single rule stated four ways — money must not be convertible into authority.

## Ambition against ambition

Who, then, holds the authority the old companies kept for themselves? Not one body, on purpose. The Commonwealth's governance splits the work the way a constitution splits a government: those who set the value-laden rules — where the floor sits, what counts as the unfriendly kind of competition — held apart from those who interpret the Covenant and judge whether it has been broken, and both held apart from the operators who run the software and merely *execute*. No one of them legislates, judges, and runs the machine at once; each can check the others. Exactly *what* those bodies are, and how each is chosen — a panel drawn **by lot** from the membership, say, so ordinary people and not only insiders hold real authority[^sortition]; a seasoned body to interpret the rules; rotation and fixed terms against entrenchment — is among the most important things the framers have to work out. The principle is fixed; the design is theirs to get right.

Beneath all of it sits the deepest check, the one no incumbent ever faced: **the software is open, and the Commonwealth can be forked.** If the Commonwealth itself betrays the Covenant — if the center tries to become the very thing we left — the Communities and their members can take the protocol and route around it. The operators serve a public that can leave them. That is the final reason control cannot harden into domination here: in the end, even the center governs only by consent.

This is what Madison meant, arguing for the Constitution, when he wrote that the great security against a concentration of power is to give each part the means to resist the others — that *ambition must be made to counteract ambition*. We are not building a system that depends on good people staying good. We are building one in which the structure itself keeps any part from ruling the rest.

## The hard problems

None of this is settled, and the honest edges are sharp. Who decides where vigorous competition becomes predatory, and can that line be drawn clearly enough to enforce? How is a Community's freedom to set its own standards squared with an Individual's right not to be excluded unfairly? How binding can the floor be before "federalism" becomes dictation from the center, and how loose before the floor stops meaning anything at all? What keeps the Commonwealth's power to sever from becoming a tool of capture dressed as enforcement? How is the fee set so it neither starves the center nor lets it grow fat, and should it ever cross-subsidize weaker Communities, with all the dependence and gaming that transfers invite?

These are not afterthoughts. They are the agenda of the Covenant — the questions the framers must answer in the open, deliberately, rather than leave to whoever ends up writing the code.

## A structure, not a savior

The genius of 1787 was not that it produced wise rulers. It was that it produced a machine in which power was set against power, so that the wisdom or folly of any one person mattered less. That is the bet here, carried onto the internet: not a benevolent company, not a charismatic founder, not a flawless set of rules, but a structure — Individuals who can leave, Communities that must earn them, a Commonwealth held thin and checked and forkable — in which no part can rule the rest, and the ambition of each is bent, by design, toward the people they are all meant to serve.

[^seppowers]: Dividing power so that no part can dominate is the heart of the separation-of-powers tradition: Montesquieu, *The Spirit of the Laws* (1748); and James Madison in *The Federalist* — No. 10 on controlling faction, and No. 51 on the "compound republic" of divided, mutually checking powers (1788).
[^sortition]: Choosing a deliberative body by lot, sortition, is no longer only an ancient idea: Ireland's Citizens' Assemblies (2016–18) led to national referendums; the German-speaking Community of Belgium (Ostbelgien) created a standing citizens' council by lot in 2019; and the OECD has catalogued hundreds of such bodies. See Hélène Landemore, *Open Democracy* (Princeton University Press, 2020); and OECD, *Innovative Citizen Participation and New Democratic Institutions* (2020).
