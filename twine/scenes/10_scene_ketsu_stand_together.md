---
beat: ketsu_stand_together
act: 4
pov: kai
location: Tide-pool sanctuary, open water
time: Storm peak, midnight
---

## Summary
Kai and Freddy face Thalos together. Kai fights with his full guardian power while Freddy protects the Lunar Shell. The battle tests everything they've built—trust, love, the home they've found in each other.

## Key Events
- Storm breaks overhead as Thalos attacks
- Kai transforms fully—spire-crest blazing, sucker-limbs spreading
- Freddy stands at the Shell, hands in the glowing water
- Thalos taunts: "You fight for a human? How far you've fallen."
- Kai's answer: "I fight for home."
- The battle is fierce but not gratuitously violent

## Axis Shifts
- trust: +2 (now at 12)
- belonging: +3 (now at 10)
- threat: +2 (now at 11)

## Choices

### Choice A: "Pour everything into the Shell—strengthen it"
- target: scene_ketsu_thalos_defeated
- type: CONTINUE
- shifts: sanctuary +2
- note: Freddy's human heart feeds the artifact

### Choice B: "Call out to Kai—distract Thalos at the critical moment"
- target: scene_ketsu_thalos_defeated
- type: ALTERNATE
- shifts: trust +1
- note: Teamwork victory, same destination

### Choice C: "Find a weapon—anything to help"
- target: scene_freddy_fights
- type: ALTERNATE
- shifts: belonging +1
- note: Freddy joins the physical fight, gets minor injury

### Choice D: "Freeze—the violence is too much"
- target: scene_ketsu_stand_together
- type: LOOP
- max_attempts: 3
- escalation:
  - attempt_1: "Blood in the water—Kai's. He's still fighting. Move."
  - attempt_2: "Thalos wraps a limb around Kai's throat. Your legs unlock."
  - attempt_3: "You scream his name. The Shell blazes. And you run—toward them, not away."

### Choice E: "[IF belonging >= 10] Rally the town—they're already coming"
- target: scene_town_arrives
- type: GATE
- requires: belonging >= 10
- shifts: belonging +3
- unlock_text: "Torches on the boardwalk. The cook. The elder. The teen with the sketchbook. They came."

## Mood
Epic, desperate, love-is-action

## Notes
- This is the climactic battle
- Violence should be implied/emotional, not gore
- Freddy's role is crucial even without combat ability
