---
beat: ten_intimacy_and_threat
act: 3
pov: kai
location: Tide-pool grotto, inner chamber
time: After first confrontation, deep night
---

## Summary
After driving Thalos back temporarily, Kai and Freddy retreat to the inner grotto. Wounded and vulnerable, Kai finally lets Freddy in—both to the sacred space and to himself. Their first full intimate scene (Heat Level 3). But in the afterglow, Kai senses it: Thalos is circling back. The Shell is flickering.

## Key Events
- Kai leads Freddy to the inner grotto, bleeding from the fight
- Freddy tends the wounds—first time touching Kai's true skin
- Kai shows him the Lunar Shell: pulsing weakly, beautiful, dying
- "If he takes this, the cove dies. And I die with it."
- Their intimacy: desperate, tender, transformative
- Post-intimacy: Kai's eyes snap open. "He's coming back. Now."

## Axis Shifts
- intimacy: +5 (reaches 12, Heat Level 3)
- threat: +1 (now at 10)
- sanctuary: -1 (now at 3 - CRISIS threshold)

## Choices

### Choice A: "We face him together. Now."
- target: scene_ketsu_stand_together
- type: CONTINUE
- shifts: trust +2
- note: United front, immediate action

### Choice B: "Hide the Shell—we can't let him find it"
- target: scene_hide_shell
- type: ALTERNATE
- shifts: sanctuary +1, threat +0
- note: Buys time, different tactical approach

### Choice C: "There has to be another way. Talk to him."
- target: scene_negotiate_thalos
- type: ALTERNATE
- shifts: trust +1
- note: Freddy's human hope, Kai skeptical but follows

### Choice D: "Stay here. Protect each other. Let the town fend for itself."
- target: scene_ten_intimacy_and_threat
- type: LOOP
- max_attempts: 3
- escalation:
  - attempt_1: "Kai holds you closer. 'The diner. The cook. The elder.' He doesn't have to finish."
  - attempt_2: "The Shell flickers. Somewhere above, glass breaks. The diner."
  - attempt_3: "'I can't lose you,' you say. 'You won't,' he answers. 'But we have to go. Now.'"

### Choice E: "[IF intimacy >= 12 AND trust >= 10] Bond with the Shell together"
- target: scene_dual_bond
- type: GATE
- requires: intimacy >= 12, trust >= 10
- shifts: sanctuary +3, revelation +2
- unlock_text: "Kai looks at the Shell, then at you. 'There's one way to make it stronger. But you'd be bound. To this place. To me. Forever.'"

## Mood
Desperate intimacy, post-coital dread, love against doom

## Notes
- Heat Level 3 scene—tender but not explicit (cozy romance guidelines)
- The Shell's weakness is the ticking clock
- Gated choice offers an alternate resolution path through bonding
